"""This file configures pytest, initializes Databricks Connect, and provides fixtures for Spark and loading test data."""

import os, sys, pathlib,pytest
from contextlib import contextmanager


# Run the tests from the root directory
sys.path.append(os.getcwd())


# try:
#     # from databricks.connect import DatabricksSession
#     # from databricks.sdk import WorkspaceClient
#     from pyspark.sql import SparkSession
#     import pytest
#     import json
#     import csv
#     import os
# except ImportError:
#     raise ImportError(
#         "Test dependencies not found.\n\nRun tests using 'uv run pytest'. See http://docs.astral.sh/uv to learn more about uv."
#     )
@pytest.fixture(scope="function")
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark=DatabricksSession.builder.getOrCreate()
        print('Using Databricks session')
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark=SparkSession.builder.getOrCreate()
            print("using local SparkSession")
        except:
            raise ImportError("Neither DatabricksSession nor SparkSession could be imported")
        return spark

