from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import argparse
import logging

logger = logging.getLogger(__name__)

def create_gold_call_enriched(spark: SparkSession, catalog: str = "main", source_db: str = "silver", target_db: str = "gold"):
    """ Enriches fact_call_activity with dimensions """
    logger.info("Building gold_call_enriched...")
    df_calls = spark.table(f"{catalog}.{source_db}.fact_call_activity")
    df_rep = spark.table(f"{catalog}.{source_db}.dim_rep_master")
    df_prescriber = spark.table(f"{catalog}.{source_db}.dim_prescriber")
    df_geo = spark.table(f"{catalog}.{source_db}.dim_geography")

    enriched = df_calls.join(df_rep, "rep_id", "left") \
                       .join(df_prescriber, "prescriber_id", "left") \
                       .join(df_geo, "geo_id", "left")

    target_path = f"{catalog}.{target_db}.gold_call_enriched"
    enriched.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_path)
    logger.info(f"Saved {target_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--source_db", type=str, default="silver")
    parser.add_argument("--target_db", type=str, default="gold")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("Gold_Source_Aligned_Call").getOrCreate()
    create_gold_call_enriched(spark, args.catalog, args.source_db, args.target_db)
