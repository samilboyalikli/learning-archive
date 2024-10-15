"""
SIMPLE ANALYSIS ON THE HOUSE PRICE PREDICTION DATASET FROM KAGGLE
"""

# TODO
#   1. (checked) ilk birkaç satırı show() ile görüntülenecek.
#   2. (checked) veri setinde kaç satır ve sütun olduğu tespit edilecek (count and columns).
#   3. (checked) sayısal sütunlar için temel istatistiksel özetler alınacak (describe).
#   4. (checked) Price, Area, Bedrooms, Bathrooms gibi sütunların max ve min değerleri tespit edilecek.
#   5. (checked) hangi sütunlarda eksik veri olup olmadığı kontrol edilecek (filter or na).
#   6. (checked) eksik veriler doldurulacak (fillna()).
#   7. Bedrooms değeri 3'den büyük olan evler bulunacak.
#   8. 2010'dan sonra inşa edilmiş olan evler listelenecek.
#   9. evler bulundukları lokasyonlara göre gruplanacak.
#   10. her bir lokasyonda kaç ev olduğu tespit edilecek.
#   11. lokasyon bazında ortalama ev fiyatları tespit edilecek.
#   12. Price Per Square Foot adında bir sütun oluşturulacak (metrekare başına evin fiyatı)
#   13. Price sütununa göre evler en ucuzdan en pahalıya doğru sıralanacak.
#   14. Area ve Price sütunlarına göre büyükten küçüğe sıralama yapılacak (alan aynıysa fiyat büyükten küçüğe).
#   15. eğer evin Garage deperi yes ise HasGarage adında bir değer oluşturulacak ve o değer True olacak.

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

