from pyspark.sql.functions import col, trim, to_date, current_timestamp
from pyspark.sql.types import StringType
import logging

logger = logging.getLogger(__name__)

def standardize_data(df):
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
            if field.name.endswith("_flag"):
                from pyspark.sql.functions import upper
                df = df.withColumn(field.name, upper(col(field.name)))

    date_columns = [f.name for f in df.schema.fields if f.name.endswith("_date")]
    for d_col in date_columns:
        df = df.withColumn(d_col, to_date(col(d_col)))

    return df

def apply_data_quality_and_quarantine(spark, df, primary_keys, catalog, target_db, table_name):
    valid_conds = []

    if primary_keys:
        for pk in primary_keys:
            valid_conds.append(col(pk).isNotNull())

    for c in ["qty", "amount", "trx_units", "sales_revenue"]:
        if c in df.columns:
            valid_conds.append((col(c).isNull()) | (col(c) >= 0))

    if not valid_conds:
        return df

    master_cond = valid_conds[0]
    for cond in valid_conds[1:]:
        master_cond = master_cond & cond

    valid_df = df.filter(master_cond)
    invalid_df = df.filter(~master_cond)

    quarantine_path = f"{catalog}.{target_db}.{table_name}_quarantine"

    # Issue #1 Fix: Removed .isEmpty() and .count() evaluations to avoid triggering full dataframe scans
    # inside foreachBatch. The write process handles empty dataframes natively without performance hits.
    invalid_df = invalid_df.withColumn("quarantine_timestamp", current_timestamp())
    invalid_df.write.format("delta").mode("append").saveAsTable(quarantine_path)
    logger.info(f"Appended bad rows to quarantine table: {quarantine_path}")

    return valid_df
