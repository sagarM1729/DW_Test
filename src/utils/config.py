import json
import os

class Config:
    def __init__(self):
        # We assume the config is run from a notebook or script where the path might vary.
        # But for this repository structure, it's in src/utils/tables.json relative to the root.
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        json_path = os.path.join(base_dir, 'src', 'utils', 'tables.json')

        with open(json_path, 'r') as f:
            self.tables = json.load(f)

    def get_table_config(self, table_name):
        return self.tables.get(table_name)

    def get_tables_by_category(self, category):
        return {k: v for k, v in self.tables.items() if v.get("category") == category}

    def get_primary_keys(self, table_name):
        return self.tables.get(table_name, {}).get("primaryKey", [])

config = Config()
