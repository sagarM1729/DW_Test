from pyspark.sql import SparkSession
import argparse
import logging

logger = logging.getLogger(__name__)

def create_gold_iqvia_enriched(spark: SparkSession, catalog: str = "main", source_db: str = "silver", target_db: str = "gold"):
    """ Enriches fact_iqvia_sales with dimensions """
    logger.info("Building gold_iqvia_enriched...")
    df_sales = spark.table(f"{catalog}.{source_db}.fact_iqvia_sales")
    df_product = spark.table(f"{catalog}.{source_db}.dim_product")
    df_geo = spark.table(f"{catalog}.{source_db}.dim_geography")

    enriched = df_sales.join(df_product, "product_id", "left") \
                       .join(df_geo, "geo_id", "left")

    target_path = f"{catalog}.{target_db}.gold_iqvia_enriched"
    enriched.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_path)
    logger.info(f"Saved {target_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--source_db", type=str, default="silver")
    parser.add_argument("--target_db", type=str, default="gold")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("Gold_Source_Aligned_IQVIA").getOrCreate()
    create_gold_iqvia_enriched(spark, args.catalog, args.source_db, args.target_db)
