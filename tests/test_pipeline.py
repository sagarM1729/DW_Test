import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder \
        .appName("PipelineTest") \
        .master("local[2]") \
        .getOrCreate()

    spark.sql("CREATE DATABASE IF NOT EXISTS main")
    yield spark

def test_silver_dq_quarantine_logic(spark):
    from src.utils.transforms import apply_data_quality_and_quarantine

    schema = StructType([
        StructField("id", StringType(), True),
        StructField("qty", IntegerType(), True),
        StructField("amount", IntegerType(), True)
    ])

    data = [
        ("1", 10, 100), # Valid
        (None, 5, 50),  # Null PK
        ("3", -5, 100), # Negative Qty
        ("4", 10, -100) # Negative Amount
    ]

    df = spark.createDataFrame(data, schema=schema)

    def mock_save(*args, **kwargs):
        pass

    original_save = df.write.__class__.saveAsTable
    df.write.__class__.saveAsTable = mock_save

    try:
        valid_df = apply_data_quality_and_quarantine(spark, df, primary_keys=["id"], catalog="spark_catalog", target_db="default", table_name="test_dq")

        assert valid_df.count() == 1
        assert valid_df.collect()[0]["id"] == "1"
    finally:
        df.write.__class__.saveAsTable = original_save
