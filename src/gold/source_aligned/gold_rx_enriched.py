from pyspark.sql import SparkSession
import argparse

def create_gold_rx_enriched(spark: SparkSession, catalog: str = "main", source_db: str = "silver", target_db: str = "gold"):
    """ Enriches fact_xponents_rx with dimensions """
    print("Building gold_rx_enriched...")
    df_rx = spark.table(f"{catalog}.{source_db}.fact_xponents_rx")
    df_prescriber = spark.table(f"{catalog}.{source_db}.dim_prescriber")
    df_geo = spark.table(f"{catalog}.{source_db}.dim_geography")
    df_product = spark.table(f"{catalog}.{source_db}.dim_product")

    enriched = df_rx.join(df_prescriber, "prescriber_id", "left") \
                    .join(df_geo, "geo_id", "left") \
                    .join(df_product, "product_id", "left")

    target_path = f"{catalog}.{target_db}.gold_rx_enriched"
    enriched.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_path)
    print(f"Saved {target_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--source_db", type=str, default="silver")
    parser.add_argument("--target_db", type=str, default="gold")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("Gold_Source_Aligned_Rx").getOrCreate()
    create_gold_rx_enriched(spark, args.catalog, args.source_db, args.target_db)
