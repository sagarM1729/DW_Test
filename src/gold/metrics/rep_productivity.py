from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, when, round as _round, expr
from delta.tables import DeltaTable
import argparse
import logging

logger = logging.getLogger(__name__)

def compute_sales_per_call_monthly(spark: SparkSession, catalog: str = "main", target_db: str = "gold"):
    """
    Computes 'sales_per_call_monthly' incrementally from source_aligned tables.
    For simplicity, assumes full overwrite of the monthly metric or a rolling merge.
    """
    logger.info("Computing sales_per_call_monthly...")
    rx_enriched = spark.table(f"{catalog}.{target_db}.gold_rx_enriched")
    call_enriched = spark.table(f"{catalog}.{target_db}.gold_call_enriched")
    target_table = f"{catalog}.{target_db}.sales_per_call_monthly"

    rx_agg = rx_enriched.withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')")) \
                        .groupBy("product_id", "geo_id", "month") \
                        .agg(_sum("trx_units").alias("sales_made"))

    call_agg = call_enriched.withColumn("month", expr("date_format(call_date, 'yyyy-MM')")) \
                            .groupBy("product_id", "geo_id", "month") \
                            .agg(count("call_id").alias("calls_made"))

    gold_df = rx_agg.join(call_agg, on=["product_id", "geo_id", "month"], how="outer").fillna(0)
    gold_df = gold_df.withColumn("sales_per_call",
                                 when(col("calls_made") > 0, _round(col("sales_made") / col("calls_made"), 2))
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
    logger.info(f"Incremental aggregation complete for {target_table}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=str, default="main")
    parser.add_argument("--target_db", type=str, default="gold")
    args = parser.parse_args()
    spark = SparkSession.builder.appName("Gold_Metrics_Rep_Productivity").getOrCreate()
    compute_sales_per_call_monthly(spark, args.catalog, args.target_db)
