# Contributing to Pharma DataLake Framework

Welcome to the Pharma DataLake Framework! This repository manages the Medallion Architecture data pipelines running on Databricks.

## Architecture Guidelines
- **Bronze**: Must be append-only using Auto Loader (`cloudFiles`).
- **Silver**: Contains standardized, deduped, and explicitly verified data using `upsert_silver_fact.py`, `upsert_silver_scd1.py`, or `upsert_silver_scd2.py`.
- **Gold**: Consists of `source_aligned` denormalizations and domain-specific `metrics`. Metrics must be incremental and consume Silver via CDF where applicable.

## Developing Locally
1. Ensure `pyspark` and `delta-spark` are installed locally to run unit tests.
2. Run tests with `pytest tests/`.

## Code Style
- Avoid `sys.path.append` logic; the framework assumes installation via standard pip or Databricks wheel/workspace imports.
- Use `logging` rather than `print` for debugging and trace outputs.
- Adhere strictly to Unity Catalog naming standards (`catalog.schema.table`).
