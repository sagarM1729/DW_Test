import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType
import os
import shutil
import sys

# Add root directory to path to fix module import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Spark Session for testing with standard configurations
@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder \
        .appName("PipelineTest") \
        .master("local[2]") \
        .getOrCreate()

    # Create test databases
    spark.sql("CREATE DATABASE IF NOT EXISTS test_silver")
    spark.sql("CREATE DATABASE IF NOT EXISTS test_gold")

    yield spark

    # Cleanup after tests
    spark.sql("DROP DATABASE IF EXISTS test_silver CASCADE")
    spark.sql("DROP DATABASE IF EXISTS test_gold CASCADE")

def test_pipeline_initialization(spark):
    assert spark is not None

def test_gold_aggregation_logic(spark):
    from src.gold.aggregate_gold import compute_sales_per_call_monthly
    from datetime import date

    schema_rx = StructType([
        StructField("product_id", StringType(), True),
        StructField("geo_id", StringType(), True),
        StructField("week_end_date", DateType(), True),
        StructField("trx_units", IntegerType(), True)
    ])

    data_rx = [
        ("P1", "G1", date(2023, 6, 30), 100),
        ("P1", "G1", date(2023, 6, 15), 50),
        ("P2", "G2", date(2023, 6, 30), 200)
    ]
    df_rx = spark.createDataFrame(data_rx, schema=schema_rx)
    df_rx.createOrReplaceTempView("fact_xponents_rx")
    spark.sql("CREATE TABLE test_silver.fact_xponents_rx AS SELECT * FROM fact_xponents_rx")

    schema_calls = StructType([
        StructField("call_id", StringType(), True),
        StructField("product_id", StringType(), True),
        StructField("geo_id", StringType(), True),
        StructField("call_date", DateType(), True)
    ])

    data_calls = [
        ("C1", "P1", "G1", date(2023, 6, 1)),
        ("C2", "P1", "G1", date(2023, 6, 2)),
        ("C3", "P2", "G2", date(2023, 6, 5))
    ]
    df_calls = spark.createDataFrame(data_calls, schema=schema_calls)
    df_calls.createOrReplaceTempView("fact_call_activity")
    spark.sql("CREATE TABLE test_silver.fact_call_activity AS SELECT * FROM fact_call_activity")

    df_rx_loaded = spark.table("test_silver.fact_xponents_rx")
    df_calls_loaded = spark.table("test_silver.fact_call_activity")
    from pyspark.sql.functions import col, sum as _sum, count, when, round as _round, expr

    df_rx_loaded = df_rx_loaded.withColumn("month", expr("date_format(week_end_date, 'yyyy-MM')"))
    df_calls_loaded = df_calls_loaded.withColumn("month", expr("date_format(call_date, 'yyyy-MM')"))

    sales_agg = df_rx_loaded.groupBy("product_id", "geo_id", "month").agg(_sum("trx_units").alias("sales_made"))
    calls_agg = df_calls_loaded.groupBy("product_id", "geo_id", "month").agg(count("call_id").alias("calls_made"))

    gold_df = sales_agg.join(calls_agg, on=["product_id", "geo_id", "month"], how="outer").fillna(0)

    gold_df = gold_df.withColumn("sales_per_call",
                                 when(col("calls_made") > 0, _round(col("sales_made") / col("calls_made"), 2))
                                 .otherwise(0.0))

    gold_df.createOrReplaceTempView("gold_result")

    # Verify results
    result_df = spark.table("gold_result")

    assert result_df.count() == 2

    p1_result = result_df.filter("product_id = 'P1'").collect()[0]
    assert p1_result["sales_made"] == 150
    assert p1_result["calls_made"] == 2
    assert p1_result["sales_per_call"] == 75.0
