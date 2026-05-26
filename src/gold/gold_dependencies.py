import json
import os

from utils.config import config

class GoldDependencyManager:
    """
    P2.01 Phase 2 - Silver to Gold & Agg: Gold Dependency Layer
    Build gold dependency notebooks defining input tables, trigger conditions,
    and dependency rules for dim/fact agg gold pipelines.
    """
    def __init__(self):
        self.tables = config.tables

    def get_dependencies_for_gold_table(self, gold_table_name):
        """
        Returns a list of source tables required to compute a specific gold table.
        """
        table_config = self.tables.get(gold_table_name, {})
        return table_config.get("derivedFrom", [])

    def validate_dependencies_met(self, spark, gold_table_name, catalog="main", source_db="silver"):
        """
        Checks if the required input tables exist in the catalog and have data,
        acting as a trigger condition before running gold aggregations.
        """
        dependencies = self.get_dependencies_for_gold_table(gold_table_name)

        if not dependencies:
            logger.info(f"No explicit dependencies defined for {gold_table_name}. Returning True.")
            return True

        logger.info(f"Validating dependencies for {gold_table_name}: {dependencies}")

        for dep in dependencies:
            full_table_path = f"{catalog}.{source_db}.{dep}"

            # Check if table exists
            table_exists = spark.catalog.tableExists(full_table_path)
            if not table_exists:
                logger.info(f"Dependency Failed: Table {full_table_path} does not exist.")
                return False

            # Check if table has data
            count = spark.table(full_table_path).count()
            if count == 0:
                logger.info(f"Dependency Failed: Table {full_table_path} is empty.")
                return False

        logger.info(f"All dependencies met for {gold_table_name}.")
        return True

    def get_execution_order(self):
        """
        Generates a naive execution order based on dependencies.
        Dimensions -> Facts -> Monthly Metrics -> Quarterly Metrics
        """
        dimensions = [k for k, v in self.tables.items() if v.get("category") == "dimension"]
        facts = [k for k, v in self.tables.items() if v.get("category") == "fact"]
        metrics_monthly = [k for k, v in self.tables.items() if v.get("category") == "metric_monthly"]
        metrics_quarterly = [k for k, v in self.tables.items() if v.get("category") == "metric_quarterly"]

        return {
            "dimensions": dimensions,
            "facts": facts,
            "metrics_monthly": metrics_monthly,
            "metrics_quarterly": metrics_quarterly
        }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Demonstration of the dependency manager
    manager = GoldDependencyManager()
    logger.info("Execution Order Strategy:")
    order = manager.get_execution_order()
    for layer, tables in order.items():
        logger.info(f"--- {layer.upper()} ---")
        for t in tables[:3]:  # Print first 3 for brevity
            deps = manager.get_dependencies_for_gold_table(t)
            logger.info(f"  {t} -> depends on: {deps}")
