from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, current_timestamp, sha2, concat_ws, lit
from pyspark.sql.window import Window
from delta.tables import DeltaTable
import argparse
import logging

from src.utils.config import Config
from src.utils.transforms import standardize_data, apply_data_quality_and_quarantine

logger = logging.getLogger(__name__)

def upsert_to_silver_scd2(spark: SparkSession, table_name: str, config: Config, catalog: str = "main", source_db: str = "bronze", target_db: str = "silver"):
    primary_keys = config.get_primary_keys(table_name)
    bronze_table_path = f"{catalog}.{source_db}.{table_name}"
    silver_table_path = f"{catalog}.{target_db}.{table_name}"
    checkpoint_path = f"/Volumes/{catalog}/default/checkpoints/silver/{table_name}_scd2"

    logger.info(f"Starting Silver SCD2 Upsert for {silver_table_path}...")
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

        columns_to_hash = [c for c in latest_changes.columns if c not in primary_keys and c not in ['sys_load_timestamp', 'source_file', 'data_date', '_change_type', '_commit_version', '_commit_timestamp']]
        latest_changes = latest_changes.withColumn("row_hash", sha2(concat_ws("||", *[col(c) for c in columns_to_hash]), 256))

        if spark.catalog.tableExists(silver_table_path):
            gold_table = DeltaTable.forName(spark, silver_table_path)
            df_existing_active = spark.table(silver_table_path).filter(col("is_active") == True)

            df_updates = latest_changes.alias("inc").join(
                df_existing_active.alias("ext"), on=primary_keys, how="inner"
            ).filter(col("inc.row_hash") != col("ext.row_hash")) \
             .selectExpr(*[f"inc.{pk} as mergeKey_{pk}" for pk in primary_keys], "inc.*")

            df_inserts = latest_changes.alias("inc").join(
                df_existing_active.alias("ext"), on=primary_keys, how="left_anti"
            ).selectExpr(*[f"inc.{pk} as mergeKey_{pk}" for pk in primary_keys], "inc.*")

            # Issue #2 Fix: Ensure schema structure aligns perfectly for the union without adding duplicates.
            df_updates_for_insert = df_updates
            for pk in primary_keys:
                df_updates_for_insert = df_updates_for_insert.withColumn(f"mergeKey_{pk}", lit(None).cast("string"))

            # Align schema of df_inserts to match df_updates before union
            align_cols = df_updates.columns

            df_merge_source = df_inserts.select(align_cols).unionByName(df_updates.select(align_cols)) \
                                        .unionByName(df_updates_for_insert.select(align_cols)) \
                                        .withColumn("is_active", lit(True)) \
                                        .withColumn("effective_start_date", current_timestamp()) \
                                        .withColumn("effective_end_date", lit(None).cast("timestamp"))

            merge_condition = " AND ".join([f"target.{pk} = source.mergeKey_{pk}" for pk in primary_keys])

            (gold_table.alias("target")
             .merge(df_merge_source.alias("source"), merge_condition)
             .whenMatchedUpdate(condition="target.is_active = true AND target.row_hash <> source.row_hash",
                                set={"is_active": lit(False), "effective_end_date": "source.effective_start_date"})
             .whenNotMatchedInsertAll()
             .execute())
        else:
            cols_to_drop = ["_change_type", "_commit_version", "_commit_timestamp"]
            initial_df = latest_changes
            for c in cols_to_drop:
                if c in initial_df.columns:
                    initial_df = initial_df.drop(c)

            initial_df = initial_df.withColumn("is_active", lit(True)) \
                                   .withColumn("effective_start_date", current_timestamp()) \
                                   .withColumn("effective_end_date", lit(None).cast("timestamp"))

            logger.info(f"Creating initial Silver SCD2 table: {silver_table_path}")
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
    logger.info(f"Silver SCD2 upsert for {table_name} complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--table_name", type=str, required=True)
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--source_db", type=str, default="bronze")
    parser.add_argument("--target_db", type=str, default="silver")
    parser.add_argument("--config_path", type=str, required=True)
    args = parser.parse_args()

    spark = SparkSession.builder.appName(f"Silver_Upsert_SCD2_{args.table_name}").getOrCreate()
    config = Config(args.config_path)
    upsert_to_silver_scd2(spark, args.table_name, config, args.catalog, args.source_db, args.target_db)
