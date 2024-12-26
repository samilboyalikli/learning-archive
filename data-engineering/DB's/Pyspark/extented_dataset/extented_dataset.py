"""

Size of Titanic Dataset:            28 KB
Size of Large Titanic Dataset:      52.428.824 KB (50 GB)

It is necessary to enlarge the dataset 1.872.458 times.

TODO
    1. Step1 = 1.024
    2. Step2 = 10.240
    3. Step3 = 102.400
    4. Step4 = 1.024.000
    5. Step5 = 2.048.000
"""

import findspark
from pyspark.sql import SparkSession
import os


os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['hadoop.home.dir'] = "C:\\hadoop"

findspark.init()
spark = SparkSession.builder.getOrCreate()

titanic_df = spark.read.csv("test.csv", header=True, inferSchema=True)


def enlarge(x, y):
    """
    :param x: Name of the dataset
    :param y: Repeat range. When input is an odd number, output will be square of the input.
    """
    for i in range(y):
        x = x.union(x)
    return x


df = enlarge(titanic_df, 4)

rows = titanic_df.count()
rows2 = df.count()
print("Shape of Titanic Dataset: ", rows)
print("Shape of Large Titanic Dataset: ", rows2)
print(rows2 / rows)
