from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, current_timestamp
import argparse
import sys
import os

# Add src to Python path if needed (for local testing/imports)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def ingest_to_bronze(spark: SparkSession, table_name: str, source_path: str, target_db: str = "bronze"):
    """
    Ingests data from ADLS/cloud storage into Bronze Delta tables using Databricks Auto Loader.
    """
    table_config = config.get_table_config(table_name)
    if not table_config:
        raise ValueError(f"Table configuration for {table_name} not found.")

    checkpoint_path = f"/mnt/checkpoints/bronze/{table_name}"
    target_path = f"/mnt/delta/bronze/{table_name}"

    # In databricks, schema inference is supported via cloudFiles.schemaLocation
    # We will let Auto Loader infer schema or provide hints. For simplicity, we use inference.

    print(f"Starting Auto Loader for {table_name}...")
    print(f"Source: {source_path}")
    print(f"Target: {target_db}.{table_name}")

    # Set up the Auto Loader read stream
    df = (spark.readStream
          .format("cloudFiles")
          .option("cloudFiles.format", "csv")
          .option("cloudFiles.schemaLocation", f"{checkpoint_path}/schema")
          .option("header", "true") # Assuming CSVs have headers
          .load(source_path))

    # Add required metadata columns for Bronze layer auditing
    df_with_metadata = df.withColumn("source_file", input_file_name()) \
                         .withColumn("sys_load_timestamp", current_timestamp())

    # Write stream to Delta table
    # Enable Change Data Feed for downstream incremental processing
    query = (df_with_metadata.writeStream
             .format("delta")
             .outputMode("append") # Bronze is append-only
             .option("checkpointLocation", checkpoint_path)
             .trigger(availableNow=True) # Good for scheduled batch-like streaming jobs
             .table(f"{target_db}.{table_name}"))

    # In a real Databricks notebook, you might use query.awaitTermination() if continuous.
    # For availableNow, it will process all available files and then stop.
    query.awaitTermination()

    # We also need to enable CDF on the table (if not already enabled globally via Spark conf)
    spark.sql(f"ALTER TABLE {target_db}.{table_name} SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")
    print(f"Ingestion for {table_name} complete. CDF enabled.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest raw data to Bronze Delta Tables using Auto Loader")
    parser.add_argument("--table_name", type=str, required=True, help="Name of the table to ingest")
    parser.add_argument("--source_path", type=str, required=True, help="ADLS source path for the raw files")
    parser.add_argument("--target_db", type=str, default="bronze", help="Target database schema")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName(f"Bronze_Ingest_{args.table_name}") \
        .getOrCreate()

    ingest_to_bronze(spark, args.table_name, args.source_path, args.target_db)
