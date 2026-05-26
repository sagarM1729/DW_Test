from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp, sha2, concat_ws, lead
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse

def process_scd2_dimension(spark: SparkSession, table_name: str, primary_key: str, catalog: str = "main", source_db: str = "silver", target_db: str = "gold"):
    """
    P2.02 Phase 2 - Silver to Gold & Agg:
    Implement SCD Type 2 logic for dimension/fact gold tables where applicable.
    """
    source_table = f"{catalog}.{source_db}.{table_name}"
    target_table = f"{catalog}.{target_db}.{table_name}"

    print(f"Processing SCD2 for {table_name}...")

    # Read incoming Silver data (can be optimized to read only CDF changes)
    # For a classic SCD2 implementation, we compare incoming state against current Gold active records.
    df_incoming = spark.table(source_table)

    # Create a row hash to detect changes in attributes
    columns_to_hash = [c for c in df_incoming.columns if c != primary_key and c not in ['sys_load_timestamp', 'source_file', 'data_date']]
    df_incoming = df_incoming.withColumn("row_hash", sha2(concat_ws("||", *[col(c) for c in columns_to_hash]), 256))

    if not (DeltaTable.isDeltaTable(spark, target_table) or spark.catalog.tableExists(target_table)):
        print(f"Initializing {target_table} as SCD2...")
        # Initial load: all records are active
        df_initial = df_incoming.withColumn("is_active", lit(True)) \
                                .withColumn("effective_start_date", current_timestamp()) \
                                .withColumn("effective_end_date", lit(None).cast("timestamp"))

        df_initial.write.format("delta").saveAsTable(target_table)
        return

    # SCD2 MERGE Logic
    gold_table = DeltaTable.forName(spark, target_table)
    df_existing_active = spark.table(target_table).filter(col("is_active") == True)

    # 1. Identify records that have changed (exists in both, but hash is different)
    df_updates = df_incoming.alias("inc").join(
        df_existing_active.alias("ext"),
        on=primary_key,
        how="inner"
    ).filter(col("inc.row_hash") != col("ext.row_hash")) \
     .selectExpr(f"inc.{primary_key} as mergeKey", "inc.*")

    # 2. Identify entirely new records
    df_inserts = df_incoming.alias("inc").join(
        df_existing_active.alias("ext"),
        on=primary_key,
        how="left_anti"
    ).selectExpr(f"inc.{primary_key} as mergeKey", "inc.*")

    # 3. For changed records, we need TWO actions in the MERGE:
    #    a) Update the old record (set is_active=False, effective_end_date=now)
    #    b) Insert the new record
    # Delta MERGE requires the source DataFrame to emit two rows for changed keys.
    # We simulate this by taking df_updates and setting mergeKey=null for the new row to force an insert.
    df_updates_for_insert = df_updates.withColumn("mergeKey", lit(None).cast("string"))

    # Combine all records driving the merge
    df_merge_source = df_inserts.unionByName(df_updates) \
                                .unionByName(df_updates_for_insert) \
                                .withColumn("is_active", lit(True)) \
                                .withColumn("effective_start_date", current_timestamp()) \
                                .withColumn("effective_end_date", lit(None).cast("timestamp"))

    print(f"Executing SCD2 Merge on {target_table}...")
    (gold_table.alias("target")
     .merge(
         df_merge_source.alias("source"),
         f"target.{primary_key} = source.mergeKey"
     )
     # When matched, it means it's the old active record needing expiration
     .whenMatchedUpdate(condition="target.is_active = true AND target.row_hash <> source.row_hash",
                        set={"is_active": lit(False),
                             "effective_end_date": "source.effective_start_date"})
     # When not matched, it's either a brand new PK, or the new state of an updated PK (mergeKey was set to null)
     .whenNotMatchedInsertAll()
     .execute()
    )
    print(f"SCD2 processing for {table_name} complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--table_name", type=str, required=True)
    parser.add_argument("--primary_key", type=str, required=True)
    parser.add_argument("--catalog", type=str, default="main")
    args = parser.parse_args()

    spark = SparkSession.builder.appName(f"SCD2_Gold_{args.table_name}").getOrCreate()
    process_scd2_dimension(spark, args.table_name, args.primary_key, args.catalog)
