from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, current_timestamp
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def ingest_to_bronze(spark: SparkSession, table_name: str, source_path: str, catalog: str = "main", target_db: str = "bronze"):
    """
    P1.01 Phase 1 - Source to Silver: Unity Catalog + Bronze
    Build one Bronze notebook per source file using Autoloader/Structured Streaming;
    create checkpoint path, support schema evolution, add metadata columns, and enable bronze change tracking.
    """
    table_config = config.get_table_config(table_name)
    if not table_config:
        print(f"Warning: Table config for {table_name} not found in config. Proceeding with default generic ingestion.")

    # Unity Catalog standard naming: catalog.schema.table
    full_table_name = f"{catalog}.{target_db}.{table_name}"
    checkpoint_path = f"/mnt/checkpoints/bronze/{table_name}"

    print(f"Starting Auto Loader for {full_table_name}...")
    print(f"Source: {source_path}")

    # Set up the Auto Loader read stream with schema evolution
    df = (spark.readStream
          .format("cloudFiles")
          .option("cloudFiles.format", "csv")
          .option("cloudFiles.schemaLocation", f"{checkpoint_path}/schema")
          .option("cloudFiles.inferColumnTypes", "true")
          .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
          .option("header", "true")
          .load(source_path))

    # Add required metadata columns
    df_with_metadata = df.withColumn("source_file", input_file_name()) \
                         .withColumn("sys_load_timestamp", current_timestamp())

    # Write stream to Delta table using Unity Catalog path
    query = (df_with_metadata.writeStream
             .format("delta")
             .outputMode("append")
             .option("checkpointLocation", checkpoint_path)
             .option("mergeSchema", "true") # Support schema evolution on write
             .trigger(availableNow=True)
             .table(full_table_name))

    query.awaitTermination()

    # Enable Change Data Feed for downstream incremental processing (Silver)
    spark.sql(f"ALTER TABLE {full_table_name} SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")
    print(f"Ingestion for {full_table_name} complete. CDF enabled.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest raw data to Bronze Delta Tables using Auto Loader")
    parser.add_argument("--table_name", type=str, required=True, help="Name of the table to ingest")
    parser.add_argument("--source_path", type=str, required=True, help="ADLS source path for the raw files")
    parser.add_argument("--catalog", type=str, default="main", help="Unity Catalog name")
    parser.add_argument("--target_db", type=str, default="bronze", help="Target database schema")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName(f"Bronze_Ingest_{args.table_name}") \
        .getOrCreate()

    ingest_to_bronze(spark, args.table_name, args.source_path, args.catalog, args.target_db)
