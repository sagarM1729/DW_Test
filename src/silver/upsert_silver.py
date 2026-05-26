from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, trim, lower, to_date, lit, current_timestamp, sha2, concat_ws
from pyspark.sql.types import StringType
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def standardize_data(df):
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
            if field.name.endswith("_flag"):
                from pyspark.sql.functions import upper
                df = df.withColumn(field.name, upper(col(field.name)))

    date_columns = [f.name for f in df.schema.fields if f.name.endswith("_date")]
    for d_col in date_columns:
        df = df.withColumn(d_col, to_date(col(d_col)))

    return df

def apply_data_quality_and_quarantine(spark, df, primary_keys, catalog, target_db, table_name):
    """
    Separates valid rows from bad rows (Quarantine).
    Rules: PK cannot be null. Quantity/Amount cannot be negative if they exist.
    """
    valid_conds = []

    if primary_keys:
        for pk in primary_keys:
            valid_conds.append(col(pk).isNotNull())

    # Check for negative amounts/quantities if columns exist
    for c in ["qty", "amount", "trx_units", "sales_revenue"]:
        if c in df.columns:
            valid_conds.append((col(c).isNull()) | (col(c) >= 0))

    if not valid_conds:
        return df # No rules to apply

    # Combine conditions with AND
    master_cond = valid_conds[0]
    for cond in valid_conds[1:]:
        master_cond = master_cond & cond

    valid_df = df.filter(master_cond)
    invalid_df = df.filter(~master_cond)

    # Send bad records to quarantine table
    quarantine_path = f"{catalog}.{target_db}.{table_name}_quarantine"

    if not invalid_df.isEmpty():
        invalid_df = invalid_df.withColumn("quarantine_timestamp", current_timestamp())
        invalid_df.write.format("delta").mode("append").saveAsTable(quarantine_path)
        print(f"Sent {invalid_df.count()} bad rows to {quarantine_path}")

    return valid_df

def merge_scd1(spark, silver_table_path, latest_changes, primary_keys):
    """ Standard SCD Type 1 Merge """
    silver_table = DeltaTable.forName(spark, silver_table_path)
    merge_condition = " AND ".join([f"silver.{pk} = updates.{pk}" for pk in primary_keys])

    (silver_table.alias("silver")
     .merge(
         latest_changes.alias("updates"),
         merge_condition
     )
     .whenMatchedUpdateAll()
     .whenNotMatchedInsertAll()
     .execute()
    )

def merge_scd2(spark, silver_table_path, latest_changes, primary_keys):
    """ SCD Type 2 Merge for dimensions """
    # Calculate row hash for incoming
    columns_to_hash = [c for c in latest_changes.columns if c not in primary_keys and c not in ['sys_load_timestamp', 'source_file', 'data_date', '_change_type', '_commit_version', '_commit_timestamp']]
    latest_changes = latest_changes.withColumn("row_hash", sha2(concat_ws("||", *[col(c) for c in columns_to_hash]), 256))

    gold_table = DeltaTable.forName(spark, silver_table_path)
    df_existing_active = spark.table(silver_table_path).filter(col("is_active") == True)

    # 1. Changed records
    df_updates = latest_changes.alias("inc").join(
        df_existing_active.alias("ext"),
        on=primary_keys,
        how="inner"
    ).filter(col("inc.row_hash") != col("ext.row_hash")) \
     .selectExpr(*[f"inc.{pk} as mergeKey_{pk}" for pk in primary_keys], "inc.*")

    # 2. New records
    df_inserts = latest_changes.alias("inc").join(
        df_existing_active.alias("ext"),
        on=primary_keys,
        how="left_anti"
    ).selectExpr(*[f"inc.{pk} as mergeKey_{pk}" for pk in primary_keys], "inc.*")

    # 3. Simulate two rows for changed records to trigger update + insert in MERGE
    df_updates_for_insert = df_updates
    for pk in primary_keys:
        df_updates_for_insert = df_updates_for_insert.withColumn(f"mergeKey_{pk}", lit(None).cast("string"))

    df_merge_source = df_inserts.unionByName(df_updates) \
                                .unionByName(df_updates_for_insert) \
                                .withColumn("is_active", lit(True)) \
                                .withColumn("effective_start_date", current_timestamp()) \
                                .withColumn("effective_end_date", lit(None).cast("timestamp"))

    merge_condition = " AND ".join([f"target.{pk} = source.mergeKey_{pk}" for pk in primary_keys])

    (gold_table.alias("target")
     .merge(
         df_merge_source.alias("source"),
         merge_condition
     )
     .whenMatchedUpdate(condition="target.is_active = true AND target.row_hash <> source.row_hash",
                        set={"is_active": lit(False),
                             "effective_end_date": "source.effective_start_date"})
     .whenNotMatchedInsertAll()
     .execute()
    )


def upsert_to_silver(spark: SparkSession, table_name: str, catalog: str = "main", source_db: str = "bronze", target_db: str = "silver"):
    table_config = config.get_table_config(table_name)
    primary_keys = config.get_primary_keys(table_name)
    category = table_config.get("category", "fact")

    bronze_table_path = f"{catalog}.{source_db}.{table_name}"
    silver_table_path = f"{catalog}.{target_db}.{table_name}"
    checkpoint_path = f"/mnt/checkpoints/silver/{table_name}"

    print(f"Starting Silver Upsert for {silver_table_path}...")
    spark.conf.set("spark.databricks.delta.properties.defaults.enableChangeDataFeed", "true")

    def upsert_batch(microBatchDF, batchId):
        print(f"Processing Batch ID {batchId} for {table_name}")

        # P1.03: Standardize data
        df_standardized = standardize_data(microBatchDF)

        # Apply DQ rules and quarantine bad records
        df_clean = apply_data_quality_and_quarantine(spark, df_standardized, primary_keys, catalog, target_db, table_name)

        # P1.02: Deduplication using Window (keep only latest change per batch per PK)
        if primary_keys:
            windowSpec = Window.partitionBy(*primary_keys).orderBy(col("sys_load_timestamp").desc())
            latest_changes = df_clean.withColumn("rn", row_number().over(windowSpec)) \
                                     .filter(col("rn") == 1) \
                                     .drop("rn")
        else:
            latest_changes = df_clean

        # Fix Bug #2: Use spark.catalog.tableExists
        if spark.catalog.tableExists(silver_table_path):
            if primary_keys:
                if category == "dimension":
                    merge_scd2(spark, silver_table_path, latest_changes, primary_keys)
                else:
                    merge_scd1(spark, silver_table_path, latest_changes, primary_keys)
            else:
                latest_changes.write.format("delta").mode("append").saveAsTable(silver_table_path)
        else:
            # Initial Load
            cols_to_drop = ["_change_type", "_commit_version", "_commit_timestamp"]
            initial_df = latest_changes
            for c in cols_to_drop:
                if c in initial_df.columns:
                    initial_df = initial_df.drop(c)

            if category == "dimension":
                # For SCD2 dims, we need to initialize tracking columns
                columns_to_hash = [c for c in initial_df.columns if c not in primary_keys and c not in ['sys_load_timestamp', 'source_file', 'data_date']]
                initial_df = initial_df.withColumn("row_hash", sha2(concat_ws("||", *[col(c) for c in columns_to_hash]), 256)) \
                                       .withColumn("is_active", lit(True)) \
                                       .withColumn("effective_start_date", current_timestamp()) \
                                       .withColumn("effective_end_date", lit(None).cast("timestamp"))

            print(f"Creating initial Silver table: {silver_table_path}")
            initial_df.write.format("delta").saveAsTable(silver_table_path)

    # Read Bronze incrementally using CDF
    df_stream = (spark.readStream
                 .format("delta")
                 .option("readChangeFeed", "true")
                 .table(bronze_table_path))

    df_changes = df_stream.filter(col("_change_type").isin(["insert", "update_postimage"]))

    query = (df_changes.writeStream
             .foreachBatch(upsert_batch)
             .outputMode("update")
             .option("checkpointLocation", checkpoint_path)
             .trigger(availableNow=True)
             .start())

    query.awaitTermination()
    print(f"Silver upsert for {table_name} complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upsert data from Bronze to Silver")
    parser.add_argument("--table_name", type=str, required=True, help="Name of the table to process")
    parser.add_argument("--catalog", type=str, default="main", help="Unity Catalog name")
    parser.add_argument("--source_db", type=str, default="bronze", help="Source database (Bronze)")
    parser.add_argument("--target_db", type=str, default="silver", help="Target database (Silver)")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName(f"Silver_Upsert_{args.table_name}") \
        .getOrCreate()

    upsert_to_silver(spark, args.table_name, args.catalog, args.source_db, args.target_db)
