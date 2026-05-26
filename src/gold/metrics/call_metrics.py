from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, when, round as _round, expr
from delta.tables import DeltaTable
import argparse
import logging

logger = logging.getLogger(__name__)

def compute_call_consistency_monthly(spark: SparkSession, catalog: str = "main", target_db: str = "gold"):
    logger.info("Computing call_consistency_monthly...")
    call_enriched = spark.table(f"{catalog}.{target_db}.gold_call_enriched")
    target_table = f"{catalog}.{target_db}.call_consistency_monthly"

    df_calls = call_enriched.withColumn("month", expr("date_format(call_date, 'yyyy-MM')")) \
                            .withColumn("last_day_of_month", expr("last_day(call_date)"))

    df_calls = df_calls.withColumn("is_last_3_days", when(expr("datediff(last_day_of_month, call_date) <= 2"), 1).otherwise(0))

    agg_df = df_calls.groupBy("rep_id", "month") \
                     .agg(count("call_id").alias("total_no_of_calls_made"),
                          _sum("is_last_3_days").alias("no_of_calls_made_in_last_3_days"))

    gold_df = agg_df.withColumn("call_consistency",
                               when(col("total_no_of_calls_made") > 0,
                                    _round(col("no_of_calls_made_in_last_3_days") / col("total_no_of_calls_made"), 4))
                               .otherwise(0.0))

    if spark.catalog.tableExists(target_table):
        gold_delta = DeltaTable.forName(spark, target_table)
        (gold_delta.alias("t")
         .merge(gold_df.alias("s"), "t.rep_id = s.rep_id AND t.month = s.month")
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
    spark = SparkSession.builder.appName("Gold_Metrics_Call").getOrCreate()
    compute_call_consistency_monthly(spark, args.catalog, args.target_db)
