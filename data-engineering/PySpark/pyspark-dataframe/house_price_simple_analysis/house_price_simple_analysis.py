"""
SIMPLE ANALYSIS ON THE HOUSE PRICE PREDICTION DATASET FROM KAGGLE
"""

import findspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import os


os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['hadoop.home.dir'] = "C:\\hadoop"

findspark.init()
spark = SparkSession.builder.getOrCreate()

houses_df = spark.read.csv("House Price Prediction Dataset.csv", header=True, inferSchema=True)


def schema_of_df(x):
    """
    output (schema of houses_df):
        Root
        |-- Id: integer (nullable = true)
        |-- Area: integer (nullable = true)
        |-- Bedrooms: integer (nullable = true)
        |-- Bathrooms: integer (nullable = true)
        |-- Floors: integer (nullable = true)
        |-- YearBuilt: integer (nullable = true)
        |-- Location: string (nullable = true)
        |-- Condition: string (nullable = true)
        |-- Garage: string (nullable = true)
        |-- Price: integer (nullable = true)

    example:
        schema_of_df(dataset)
    :param x: This parameter means the dataset.
    :return: This method gives you schema of dataset.
    """
    return x.printSchema()


def show_first_ten_row(x):
    return x.show(10)


def row_count(x):
    result = x.count()
    return result


def column_count(x):
    result = len(x.columns)
    return result


def describes(x):
    """
    What i learned:
        1. "*" is a unpacking method. For example "print(for i in iterable)" = "print(*[iterable])".
        2. We are using item before describe it in "list comprehension". For example (i for i in iterable).
    Example:
        describes(dataset).show()
    :param x: This parameter means dataset.
    :return: This method gives you describes of some integer columns which indicated in "values".
    """
    values = x.describe("Area", "Bedrooms", "Floors", "YearBuilt", "Price")
    result = values.select(values["summary"], *[f.round(values[col], 2).alias(col) for col in values.columns
                                                if col != "summary"])
    return result


class AggProcesses:
    """
     1. agg funcs not be usable without groupBy() method.
     2. if we choose more than one column then we must use "," so we can not use "&" operator.
    """
    def __init__(self, x):
        self.values = ["Area", "Bedrooms", "Floors", "YearBuilt", "Price"]
        self.miv = x.select(*[f.min(i).alias(f"Min {i}") for i in self.values])
        self.mav = x.select(*[f.max(i).alias(f"Max {i}") for i in self.values])

    def min_of_values(self):
        self.miv.show()

    def max_of_values(self):
        self.mav.show()


class MissingDatas:
    def __init__(self, x):
        self.columns = ["Id", "Area", "Bedrooms", "Bathrooms", "Floors", "YearBuilt", "Location", "Condition", "Garage",
                        "Price"]
        self.x = x

    def control(self):
        for col in self.columns:
            result = self.x.filter(self.x[col].isNull())
            if result.count() == 0:
                print(f"{col} is full")
            else:
                result.show()

    def filling(self):
        filled_df = self.x
        for col in self.columns:
            result = self.x.filter(self.x[col].isNull())
            if result.count() == 0:
                print(f"{col} is still full")
            else:
                new_col = self.x.approxQuantile(col, [0.5], 0)[0]
                filled_df = self.x.na.fill({col: new_col})
        return filled_df


def bedrooms_biggest_than_three(x):
    """
    >>> houses_df.select(houses_df.Bedrooms > 3).show()
    output of this codes, gives us just boolean datas of selected columns.
    >>> houses_df.filter(houses_df.Bedrooms > 3).show()
    output of this codes, gives us all columns of filtered datas.
    """
    x.filter(x.Bedrooms > 3).show()


def year_built_search(x):
    x.filter(x.YearBuilt > 2010).show()


def location(x):
    x.groupBy("Location").count().show()


def price_order_by_location(x):
    x.groupBy("Location").avg("Price").show()


def price_per_square_(x):
    """
    withColumn("new_column_name", new_column_conditions)
    """
    x.withColumn("price_per_square", x["Area"] / x["Price"]).show()


def order_by_price(x):
    """
    orderBy(df.columnName.asc()/desc())
    """
    x.orderBy(x.Price.asc()).show()


def price_by_area(x):
    """
    orderBy([orderedByColumns], ascending=[boolean])
    """
    x.orderBy(["Area", "Price"], ascending=[True, False]).show()


def has_garage(x):
    """
    withColumn("new_column_name", new_column_conditions)
    """
    x.withColumn("HasGarage", f.when(x["Garage"] == "Yes", True).otherwise(False)).show()
