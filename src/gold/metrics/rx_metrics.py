from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, when, round as _round, expr
from delta.tables import DeltaTable
import argparse

def compute_metric_monthly_marketshare_trx(spark: SparkSession, catalog: str = "main", target_db: str = "gold"):
    print("Computing metric_monthly_marketshare_trx...")
    rx_enriched = spark.table(f"{catalog}.{target_db}.gold_rx_enriched")
    iqvia_enriched = spark.table(f"{catalog}.{target_db}.gold_iqvia_enriched")
    target_table = f"{catalog}.{target_db}.metric_monthly_marketshare_trx"

    rx_agg = rx_enriched.filter(col("company_flag") == 'Y') \
                        .withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')")) \
                        .groupBy("product_id", "geo_id", "month") \
                        .agg(_sum("trx_units").alias("our_product_trx_units"))

    market_agg = iqvia_enriched.withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')")) \
                               .groupBy("product_id", "geo_id", "month") \
                               .agg(_sum("trx_units").alias("total_market_trx_units"))

    gold_df = rx_agg.join(market_agg, on=["product_id", "geo_id", "month"], how="inner")

    gold_df = gold_df.withColumn("trx_market_share_pct",
                                 when(col("total_market_trx_units") > 0,
                                      _round((col("our_product_trx_units") / col("total_market_trx_units")) * 100, 2))
                                 .otherwise(0.0))

    if spark.catalog.tableExists(target_table):
        gold_delta = DeltaTable.forName(spark, target_table)
        (gold_delta.alias("t")
         .merge(gold_df.alias("s"), "t.product_id = s.product_id AND t.geo_id = s.geo_id AND t.month = s.month")
         .whenMatchedUpdateAll()
         .whenNotMatchedInsertAll()
         .execute())
    else:
        gold_df.write.format("delta").saveAsTable(target_table)
    print(f"Incremental aggregation complete for {target_table}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--target_db", type=str, default="gold")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("Gold_Metrics_Rx").getOrCreate()
    compute_metric_monthly_marketshare_trx(spark, args.catalog, args.target_db)
