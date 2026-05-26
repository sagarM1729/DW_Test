import json
import os

class Config:
    def __init__(self, config_path=None):
        # Issue #3 Fix: Removed hard dependency on __file__
        # Allow passing the path explicitly or fallback to environment variable for Databricks compat
        if not config_path:
            config_path = os.getenv("PHARMA_CONFIG_PATH")

        if not config_path:
            # Fallback for local testing if neither argument nor env var is provided
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            config_path = os.path.join(base_dir, 'src', 'utils', 'tables.json')

        with open(config_path, 'r') as f:
            self.tables = json.load(f)

    def get_table_config(self, table_name):
        return self.tables.get(table_name)

    def get_tables_by_category(self, category):
        return {k: v for k, v in self.tables.items() if v.get("category") == category}

    def get_primary_keys(self, table_name):
        return self.tables.get(table_name, {}).get("primaryKey", [])
