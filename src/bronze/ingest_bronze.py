from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, current_timestamp
import argparse
import logging

from src.utils.config import Config

logger = logging.getLogger(__name__)

def ingest_to_bronze(spark: SparkSession, table_name: str, source_path: str, config: Config, catalog: str = "main", target_db: str = "bronze"):
    table_config = config.get_table_config(table_name)
    if not table_config:
        logger.warning(f"Table config for {table_name} not found in config. Proceeding with default generic ingestion.")

    full_table_name = f"{catalog}.{target_db}.{table_name}"

    # Issue #4 Fix: Used Unity Catalog Volume path style instead of raw /mnt/
    checkpoint_path = f"/Volumes/{catalog}/default/checkpoints/bronze/{table_name}"

    logger.info(f"Starting Auto Loader for {full_table_name}...")
    logger.info(f"Source: {source_path}")

    spark.conf.set("spark.databricks.delta.properties.defaults.enableChangeDataFeed", "true")

    df = (spark.readStream
          .format("cloudFiles")
          .option("cloudFiles.format", "csv")
          .option("cloudFiles.schemaLocation", f"{checkpoint_path}/schema")
          .option("cloudFiles.inferColumnTypes", "true")
          .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
          .option("header", "true")
          .load(source_path))

    df_with_metadata = df.withColumn("source_file", input_file_name()) \
                         .withColumn("sys_load_timestamp", current_timestamp())

    query = (df_with_metadata.writeStream
             .format("delta")
             .outputMode("append")
             .option("checkpointLocation", checkpoint_path)
             .option("mergeSchema", "true")
             .trigger(availableNow=True)
             .table(full_table_name))

    query.awaitTermination()

    logger.info(f"Ingestion for {full_table_name} complete. CDF enabled.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Ingest raw data to Bronze Delta Tables using Auto Loader")
    parser.add_argument("--table_name", type=str, required=True, help="Name of the table to ingest")
    parser.add_argument("--source_path", type=str, required=True, help="ADLS source path for the raw files")
    parser.add_argument("--catalog", type=str, default="main", help="Unity Catalog name")
    parser.add_argument("--target_db", type=str, default="bronze", help="Target database schema")
    parser.add_argument("--config_path", type=str, required=True)

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName(f"Bronze_Ingest_{args.table_name}") \
        .getOrCreate()

    config = Config(args.config_path)

    ingest_to_bronze(spark, args.table_name, args.source_path, config, args.catalog, args.target_db)
