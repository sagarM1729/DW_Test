from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse
import logging

from src.utils.config import Config
from src.utils.transforms import standardize_data, apply_data_quality_and_quarantine

logger = logging.getLogger(__name__)

def upsert_to_silver_fact(spark: SparkSession, table_name: str, config: Config, catalog: str = "main", source_db: str = "bronze", target_db: str = "silver"):
    primary_keys = config.get_primary_keys(table_name)
    bronze_table_path = f"{catalog}.{source_db}.{table_name}"
    silver_table_path = f"{catalog}.{target_db}.{table_name}"
    checkpoint_path = f"/Volumes/{catalog}/default/checkpoints/silver/{table_name}"

    logger.info(f"Starting Silver Fact Upsert for {silver_table_path}...")
    spark.conf.set("spark.databricks.delta.properties.defaults.enableChangeDataFeed", "true")

    def upsert_batch(microBatchDF, batchId):
        logger.info(f"Processing Batch ID {batchId} for {table_name}")
        df_standardized = standardize_data(microBatchDF)
        df_clean = apply_data_quality_and_quarantine(spark, df_standardized, primary_keys, catalog, target_db, table_name)

        if primary_keys:
            windowSpec = Window.partitionBy(*primary_keys).orderBy(col("sys_load_timestamp").desc())
            latest_changes = df_clean.withColumn("rn", row_number().over(windowSpec)).filter(col("rn") == 1).drop("rn")
        else:
            latest_changes = df_clean

        if spark.catalog.tableExists(silver_table_path):
            if primary_keys:
                silver_table = DeltaTable.forName(spark, silver_table_path)
                merge_condition = " AND ".join([f"silver.{pk} = updates.{pk}" for pk in primary_keys])
                (silver_table.alias("silver")
                 .merge(latest_changes.alias("updates"), merge_condition)
                 .whenMatchedUpdateAll()
                 .whenNotMatchedInsertAll()
                 .execute())
            else:
                latest_changes.write.format("delta").mode("append").saveAsTable(silver_table_path)
        else:
            cols_to_drop = ["_change_type", "_commit_version", "_commit_timestamp"]
            initial_df = latest_changes
            for c in cols_to_drop:
                if c in initial_df.columns:
                    initial_df = initial_df.drop(c)
            logger.info(f"Creating initial Silver Fact table: {silver_table_path}")
            initial_df.write.format("delta").saveAsTable(silver_table_path)

    df_stream = spark.readStream.format("delta").option("readChangeFeed", "true").table(bronze_table_path)
    df_changes = df_stream.filter(col("_change_type").isin(["insert", "update_postimage"]))

    query = (df_changes.writeStream
             .foreachBatch(upsert_batch)
             .outputMode("update")
             .option("checkpointLocation", checkpoint_path)
             .trigger(availableNow=True)
             .start())

    query.awaitTermination()
    logger.info(f"Silver Fact upsert for {table_name} complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--table_name", type=str, required=True)
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--source_db", type=str, default="bronze")
    parser.add_argument("--target_db", type=str, default="silver")
    parser.add_argument("--config_path", type=str, required=True)
    args = parser.parse_args()

    spark = SparkSession.builder.appName(f"Silver_Upsert_Fact_{args.table_name}").getOrCreate()
    config = Config(args.config_path)
    upsert_to_silver_fact(spark, args.table_name, config, args.catalog, args.source_db, args.target_db)
