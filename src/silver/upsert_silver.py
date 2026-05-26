from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, trim, lower, to_date
from pyspark.sql.types import StringType
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def standardize_data(df):
    """
    P1.03 Phase 1 - Source to Silver: Standardise data types, column naming,
    date formats, codes, and business-friendly values.
    """
    # Trim whitespace for all string columns and lower-case common flag/code fields conceptually
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))

            # Example standardization: Make flags upper case or IDs clean
            if field.name.endswith("_flag"):
                from pyspark.sql.functions import upper
                df = df.withColumn(field.name, upper(col(field.name)))

    # Identify date fields based on naming conventions and enforce standard DateType
    date_columns = [f.name for f in df.schema.fields if f.name.endswith("_date")]
    for d_col in date_columns:
        # Assuming source is string 'yyyy-MM-dd' or similar, standardizing explicitly
        df = df.withColumn(d_col, to_date(col(d_col)))

    return df

def upsert_to_silver(spark: SparkSession, table_name: str, catalog: str = "main", source_db: str = "bronze", target_db: str = "silver"):
    """
    P1.02 & P1.04 Phase 1 - Source to Silver: Implement data quality checks,
    deduplication, and set up silver CDC/incremental processing aligned to bronze CDF.
    """
    table_config = config.get_table_config(table_name)
    primary_keys = config.get_primary_keys(table_name)

    bronze_table_path = f"{catalog}.{source_db}.{table_name}"
    silver_table_path = f"{catalog}.{target_db}.{table_name}"
    checkpoint_path = f"/mnt/checkpoints/silver/{table_name}"

    print(f"Starting Silver Upsert for {silver_table_path}...")

    def upsert_batch(microBatchDF, batchId):
        print(f"Processing Batch ID {batchId} for {table_name}")

        # P1.03: Standardize data
        df_standardized = standardize_data(microBatchDF)

        # P1.02: Data Quality Checks (PK Null check)
        if primary_keys:
            df_clean = df_standardized.dropna(subset=primary_keys)
        else:
            df_clean = df_standardized

        # P1.02: Deduplication using Window
        if primary_keys:
            windowSpec = Window.partitionBy(*primary_keys).orderBy(col("sys_load_timestamp").desc())
            latest_changes = df_clean.withColumn("rn", row_number().over(windowSpec)) \
                                     .filter(col("rn") == 1) \
                                     .drop("rn")
        else:
            latest_changes = df_clean

        # P1.04: Incremental processing using MERGE
        if DeltaTable.isDeltaTable(spark, silver_table_path) or spark.catalog.tableExists(silver_table_path):
            silver_table = DeltaTable.forName(spark, silver_table_path)

            if primary_keys:
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
            else:
                latest_changes.write.format("delta").mode("append").saveAsTable(silver_table_path)
        else:
            # Initial Load
            cols_to_drop = ["_change_type", "_commit_version", "_commit_timestamp"]
            initial_df = latest_changes
            for c in cols_to_drop:
                if c in initial_df.columns:
                    initial_df = initial_df.drop(c)

            print(f"Creating initial Silver table: {silver_table_path}")
            initial_df.write.format("delta").saveAsTable(silver_table_path)
            # Enable CDF for Gold layer incremental downstream
            spark.sql(f"ALTER TABLE {silver_table_path} SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")

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
