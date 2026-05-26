from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, when, round as _round, lit, expr
from delta.tables import DeltaTable
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def compute_sales_per_call_monthly(spark: SparkSession, source_db: str = "silver", target_db: str = "gold"):
    """
    Computes the 'sales_per_call_monthly' Gold metric.
    Logic: TRx units generated per field call made, segmented by product and territory.
    Derived From: fact_xponents_rx, fact_call_activity
    """
    print("Computing sales_per_call_monthly...")
    # Load required Silver tables
    df_rx = spark.table(f"{source_db}.fact_xponents_rx")
    df_calls = spark.table(f"{source_db}.fact_call_activity")

    # Extract month from dates
    # Assuming fact_xponents_rx has week_end_date, we extract month (YYYY-MM)
    # Assuming fact_call_activity has call_date
    df_rx = df_rx.withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')"))
    df_calls = df_calls.withColumn("month", expr("date_format(call_date, 'yyyy-MM')"))

    # Aggregate sales (TRx) per product, territory (geo_id for simplicity here, or join with zip_territory_mapping if needed), month
    # Note: In a real scenario, we might need zip_territory_mapping to get territory_id from geo_id
    sales_agg = df_rx.groupBy("product_id", "geo_id", "month") \
                     .agg(_sum("trx_units").alias("sales_made"))

    # Aggregate calls per product, territory, month
    calls_agg = df_calls.groupBy("product_id", "geo_id", "month") \
                        .agg(count("call_id").alias("calls_made"))

    # Join aggregations
    gold_df = sales_agg.join(calls_agg, on=["product_id", "geo_id", "month"], how="outer").fillna(0)

    # Compute ratio
    gold_df = gold_df.withColumn("sales_per_call",
                                 when(col("calls_made") > 0, _round(col("sales_made") / col("calls_made"), 2))
                                 .otherwise(0.0))

    # Save to Gold
    table_path = f"{target_db}.sales_per_call_monthly"
    gold_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(table_path)
    print(f"Saved to {table_path}")


def compute_call_consistency_monthly(spark: SparkSession, source_db: str = "silver", target_db: str = "gold"):
    """
    Computes 'call_consistency_monthly' Gold metric.
    Logic: Ratio of calls made in the last 3 days of the month vs total calls per rep.
    Derived From: fact_call_activity
    """
    print("Computing call_consistency_monthly...")
    df_calls = spark.table(f"{source_db}.fact_call_activity")

    # We need to determine if call_date is in the last 3 days of the month.
    # Using Spark SQL expressions for simplicity.
    df_calls = df_calls.withColumn("month", expr("date_format(call_date, 'yyyy-MM')")) \
                       .withColumn("last_day_of_month", expr("last_day(call_date)"))

    # Flag calls in the last 3 days (last_day, last_day - 1, last_day - 2)
    df_calls = df_calls.withColumn("is_last_3_days",
                                   when(expr("datediff(last_day_of_month, call_date) <= 2"), 1).otherwise(0))

    agg_df = df_calls.groupBy("rep_id", "month") \
                     .agg(count("call_id").alias("total_no_of_calls_made"),
                          _sum("is_last_3_days").alias("no_of_calls_made_in_last_3_days"))

    agg_df = agg_df.withColumn("call_consistency",
                               when(col("total_no_of_calls_made") > 0,
                                    _round(col("no_of_calls_made_in_last_3_days") / col("total_no_of_calls_made"), 4))
                               .otherwise(0.0))

    table_path = f"{target_db}.call_consistency_monthly"
    agg_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(table_path)
    print(f"Saved to {table_path}")


def compute_metric_monthly_marketshare_trx(spark: SparkSession, source_db: str = "silver", target_db: str = "gold"):
    """
    Computes 'metric_monthly_marketshare_trx' Gold metric.
    Logic: our product TRx / total market TRx
    Derived From: fact_xponents_rx, fact_iqvia_sales
    """
    print("Computing metric_monthly_marketshare_trx...")
    # This assumes fact_iqvia_sales is the denominator
    df_rx = spark.table(f"{source_db}.fact_xponents_rx")
    df_market = spark.table(f"{source_db}.fact_iqvia_sales")

    # We aggregate our products TRx (fact_xponents_rx)
    df_rx = df_rx.filter(col("our_product") == 'Y') \
                 .withColumn("sales_month", expr("date_format(week_end_date, 'yyyy-MM')"))
    our_agg = df_rx.groupBy("product_id", "geo_id", "sales_month") \
                   .agg(_sum("trx_units").alias("our_product_trx_units"))

    # Aggregate total market TRx (fact_iqvia_sales)
    df_market = df_market.withColumn("sales_month", expr("date_format(week_end_date, 'yyyy-MM')"))
    market_agg = df_market.groupBy("product_id", "geo_id", "sales_month") \
                          .agg(_sum("trx_units").alias("total_market_trx_units"))

    gold_df = our_agg.join(market_agg, on=["product_id", "geo_id", "sales_month"], how="inner")

    gold_df = gold_df.withColumn("trx_market_share_pct",
                                 when(col("total_market_trx_units") > 0,
                                      _round((col("our_product_trx_units") / col("total_market_trx_units")) * 100, 2))
                                 .otherwise(0.0))

    table_path = f"{target_db}.metric_monthly_marketshare_trx"
    gold_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(table_path)
    print(f"Saved to {table_path}")

def compute_weekly_gold_aggregations(spark: SparkSession, source_db: str = "silver", target_db: str = "gold"):
    """
    P2.03 Phase 2 - Silver to Gold & Agg:
    Aggregate source-aligned gold tables into weekly-grain gold aggregation tables and enable incremental updates.
    """
    print("Computing weekly-grain gold aggregations (P2.03)...")
    df_rx = spark.table(f"{source_db}.fact_xponents_rx")

    weekly_agg = df_rx.groupBy("product_id", "geo_id", "week_end_date") \
                      .agg(_sum("trx_units").alias("total_weekly_trx"),
                           _sum("new_rx_units").alias("total_weekly_nrx"))

    table_path = f"{target_db}.weekly_rx_aggregation"

    # Enable incremental updates by using MERGE based on the weekly grain PKs
    if DeltaTable.isDeltaTable(spark, table_path) or spark.catalog.tableExists(table_path):
        target_table = DeltaTable.forName(spark, table_path)
        (target_table.alias("t")
         .merge(weekly_agg.alias("s"),
                "t.product_id = s.product_id AND t.geo_id = s.geo_id AND t.week_end_date = s.week_end_date")
         .whenMatchedUpdateAll()
         .whenNotMatchedInsertAll()
         .execute())
    else:
        weekly_agg.write.format("delta").saveAsTable(table_path)

    print(f"Weekly aggregation saved to {table_path}")

def main(spark: SparkSession, source_db: str, target_db: str, metric_name: str = "all"):
    if metric_name == "all" or metric_name == "sales_per_call_monthly":
        compute_sales_per_call_monthly(spark, source_db, target_db)

    if metric_name == "all" or metric_name == "call_consistency_monthly":
        compute_call_consistency_monthly(spark, source_db, target_db)

    if metric_name == "all" or metric_name == "metric_monthly_marketshare_trx":
        compute_metric_monthly_marketshare_trx(spark, source_db, target_db)

    if metric_name == "all" or metric_name == "weekly_aggregations":
        compute_weekly_gold_aggregations(spark, source_db, target_db)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute Gold Layer Aggregations and Metrics")
    parser.add_argument("--metric_name", type=str, default="all", help="Specific metric to compute or 'all'")
    parser.add_argument("--source_db", type=str, default="silver", help="Source database (Silver)")
    parser.add_argument("--target_db", type=str, default="gold", help="Target database (Gold)")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName("Gold_Aggregations") \
        .getOrCreate()

    main(spark, args.source_db, args.target_db, args.metric_name)
