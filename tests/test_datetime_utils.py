# test_datetime_utils.py

import datetime
from src.utils.datetime_utils import timestamp_to_date_col
import datetime
# from pyspark.sql import SparkSession

def test_timestamp_to_date_col(spark):
    
    # Create a Spark session
    # spark = SparkSession.builder.getOrCreate()
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
    
    # Create a DataFrame with a known timestamp column using a datetime object
    data = [(datetime.datetime(2025, 4, 10, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)
    
    # Use the utility to add a date column
    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")
    
    # Assert that the extracted date matches the expected value
    row = result_df.select("ride_date").first()
    
    expected_date = datetime.date(2025, 4, 10)  # Expected: 2025-04-10
    
    assert row["ride_date"] == expected_date
