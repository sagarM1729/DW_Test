from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, expr
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def upsert_to_silver(spark: SparkSession, table_name: str, source_db: str = "bronze", target_db: str = "silver"):
    """
    Reads incremental changes from the Bronze table using Change Data Feed (CDF),
    applies deduplication and data quality checks, and uses MERGE INTO to upsert
    records into the Silver Delta table.
    """
    table_config = config.get_table_config(table_name)
    if not table_config:
        raise ValueError(f"Table configuration for {table_name} not found.")

    primary_keys = config.get_primary_keys(table_name)
    if not primary_keys:
        # If there's no primary key defined, we might need a different strategy (e.g. append only),
        # but the architecture specifies MERGE for Silver. We will assume append for fact/metric if PK is missing,
        # but the config mapping defines PKs for dims and facts.
        print(f"Warning: No primary key defined for {table_name}. Defaulting to append-only for Silver layer if necessary.")

    bronze_table_path = f"{source_db}.{table_name}"
    silver_table_path = f"{target_db}.{table_name}"
    checkpoint_path = f"/mnt/checkpoints/silver/{table_name}"

    print(f"Starting Silver Upsert for {table_name}...")

    # For a streaming MERGE approach with CDF, we use foreachBatch.
    def upsert_batch(microBatchDF, batchId):
        print(f"Processing Batch ID {batchId} for {table_name}")

        # 1. Filter out only the latest changes if a row was updated multiple times in the same batch
        # Assuming `sys_load_timestamp` is our ordering key.
        if primary_keys:
            windowSpec = Window.partitionBy(*primary_keys).orderBy(col("sys_load_timestamp").desc())

            # Keep only the latest record per PK in this batch
            latest_changes = microBatchDF.withColumn("rn", row_number().over(windowSpec)) \
                                         .filter(col("rn") == 1) \
                                         .drop("rn")
        else:
            latest_changes = microBatchDF

        # Basic Data Quality Checks (e.g. drop rows with null primary keys)
        if primary_keys:
            latest_changes = latest_changes.dropna(subset=primary_keys)

        # 2. Perform the MERGE operation
        if DeltaTable.isDeltaTable(spark, f"/mnt/delta/silver/{table_name}") or spark.catalog.tableExists(silver_table_path):
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
                # If no PK, fallback to append
                latest_changes.write.format("delta").mode("append").saveAsTable(silver_table_path)
        else:
            # Table doesn't exist yet, do an initial insert
            # Drop the CDF metadata columns (_change_type, _commit_version, _commit_timestamp) before saving if they exist in schema.
            # Typically these are added by readStream readChangeFeed.
            cols_to_drop = ["_change_type", "_commit_version", "_commit_timestamp"]
            initial_df = latest_changes
            for c in cols_to_drop:
                if c in initial_df.columns:
                    initial_df = initial_df.drop(c)

            print(f"Creating initial Silver table for {table_name}")
            # Ensure the table is created with CDF enabled for downstream (Gold) incrementally processing
            initial_df.write.format("delta") \
                .option("path", f"/mnt/delta/silver/{table_name}") \
                .saveAsTable(silver_table_path)

            spark.sql(f"ALTER TABLE {silver_table_path} SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")

    # Set up the streaming read from Bronze using CDF
    # Option 'readChangeFeed' ensures we only get changes.
    df_stream = (spark.readStream
                 .format("delta")
                 .option("readChangeFeed", "true")
                 .table(bronze_table_path))

    # We filter for inserts and updates (ignore deletes/preimages depending on business logic, mostly inserts/updates for SCD1)
    df_changes = df_stream.filter(col("_change_type").isin(["insert", "update_postimage"]))

    query = (df_changes.writeStream
             .foreachBatch(upsert_batch)
             .outputMode("update")
             .option("checkpointLocation", checkpoint_path)
             .trigger(availableNow=True) # Run once for all available changes
             .start())

    query.awaitTermination()
    print(f"Silver upsert for {table_name} complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upsert data from Bronze to Silver using CDF and MERGE")
    parser.add_argument("--table_name", type=str, required=True, help="Name of the table to process")
    parser.add_argument("--source_db", type=str, default="bronze", help="Source database (Bronze)")
    parser.add_argument("--target_db", type=str, default="silver", help="Target database (Silver)")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName(f"Silver_Upsert_{args.table_name}") \
        .getOrCreate()

    upsert_to_silver(spark, args.table_name, args.source_db, args.target_db)
