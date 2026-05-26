from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, when, round as _round, lit, expr
from delta.tables import DeltaTable
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import config

def compute_sales_per_call_monthly_incremental(spark: SparkSession, source_db: str = "silver", target_db: str = "gold", catalog: str = "main"):
    """
    Computes 'sales_per_call_monthly' Gold metric incrementally using CDF.
    Instead of full read/overwrite, we stream CDF from fact_xponents_rx and fact_call_activity,
    identify the affected (product_id, geo_id, month) slices, and recompute/merge just those slices.
    For simplicity in this demonstration, we'll watch the primary driver (fact_xponents_rx).
    In a true multi-stream scenario, you would track both or use watermarks.
    """
    print("Computing sales_per_call_monthly incrementally...")
    rx_table = f"{catalog}.{source_db}.fact_xponents_rx"
    calls_table = f"{catalog}.{source_db}.fact_call_activity"
    target_table = f"{catalog}.{target_db}.sales_per_call_monthly"
    checkpoint_path = f"/mnt/checkpoints/gold/sales_per_call_monthly"

    # Set up CDF stream from the Silver Rx fact table
    df_rx_stream = (spark.readStream
                    .format("delta")
                    .option("readChangeFeed", "true")
                    .table(rx_table))

    def process_gold_batch(microBatchDF, batchId):
        # Identify the affected slices (product, geo, month) from the changes in this batch
        df_changes = microBatchDF.filter(col("_change_type").isin(["insert", "update_postimage"]))
        if df_changes.isEmpty():
            return

        affected_slices = df_changes.withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')")) \
                                    .select("product_id", "geo_id", "month") \
                                    .distinct()

        # Recompute ONLY for the affected slices
        df_rx_full = spark.table(rx_table).withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')"))
        df_calls_full = spark.table(calls_table).withColumn("month", expr("date_format(call_date, 'yyyy-MM')"))

        # Filter the full tables to only the affected slices
        rx_affected = df_rx_full.join(affected_slices, on=["product_id", "geo_id", "month"], how="inner")
        calls_affected = df_calls_full.join(affected_slices, on=["product_id", "geo_id", "month"], how="inner")

        sales_agg = rx_affected.groupBy("product_id", "geo_id", "month").agg(_sum("trx_units").alias("sales_made"))
        calls_agg = calls_affected.groupBy("product_id", "geo_id", "month").agg(count("call_id").alias("calls_made"))

        gold_batch_df = sales_agg.join(calls_agg, on=["product_id", "geo_id", "month"], how="outer").fillna(0)
        gold_batch_df = gold_batch_df.withColumn("sales_per_call",
                                     when(col("calls_made") > 0, _round(col("sales_made") / col("calls_made"), 2))
                                     .otherwise(0.0))

        # MERGE into Gold table
        if spark.catalog.tableExists(target_table):
            gold_delta = DeltaTable.forName(spark, target_table)
            (gold_delta.alias("t")
             .merge(
                 gold_batch_df.alias("s"),
                 "t.product_id = s.product_id AND t.geo_id = s.geo_id AND t.month = s.month"
             )
             .whenMatchedUpdateAll()
             .whenNotMatchedInsertAll()
             .execute())
        else:
            gold_batch_df.write.format("delta").saveAsTable(target_table)

    query = (df_rx_stream.writeStream
             .foreachBatch(process_gold_batch)
             .outputMode("update")
             .option("checkpointLocation", checkpoint_path)
             .trigger(availableNow=True)
             .start())

    query.awaitTermination()
    print(f"Incremental aggregation complete for {target_table}")

def main(spark: SparkSession, source_db: str, target_db: str, catalog: str, metric_name: str = "all"):
    # In a full project, you would replicate the CDF slicing pattern above for all metrics.
    # For this demonstration, we focus on proving the incremental logic on the main metric.
    if metric_name == "all" or metric_name == "sales_per_call_monthly":
        compute_sales_per_call_monthly_incremental(spark, source_db, target_db, catalog)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute Gold Layer Aggregations incrementally")
    parser.add_argument("--metric_name", type=str, default="all", help="Specific metric to compute or 'all'")
    parser.add_argument("--source_db", type=str, default="silver", help="Source database (Silver)")
    parser.add_argument("--target_db", type=str, default="gold", help="Target database (Gold)")
    parser.add_argument("--catalog", type=str, default="main", help="Unity Catalog name")

    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName("Gold_Aggregations_Incremental") \
        .getOrCreate()

    main(spark, args.source_db, args.target_db, args.catalog, args.metric_name)

    if metric_name == "all" or metric_name == "call_consistency_monthly":
        pass # To be implemented via CDF

    if metric_name == "all" or metric_name == "metric_monthly_marketshare_trx":
        pass # To be implemented via CDF

    if metric_name == "all" or metric_name == "weekly_aggregations":
        pass # To be implemented via CDF
