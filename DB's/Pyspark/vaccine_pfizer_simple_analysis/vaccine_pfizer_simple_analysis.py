"""
SIMPLE ANALYSIS ON THE VACCINE PFIZER DATASET
"""

# TODO
#   1. tweet sayısı bulunacak.
#   2. pozitif/negatif tweet sayısı bulunacak.
#   3. "pfizer" kelimesini içeren tweetler bulunup görüntülenecek.
#   4. en uzun tweet bulunacak.
#   5. en çok geçen kelime bulunacak.
#   6. konu dağılımı analiz edilecek.
#   7. subjectivity/polarity arasındaki ilişki analiz edilecek.

import findspark
from pyspark.sql import SparkSession
import os

os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['hadoop.home.dir'] = "C:\\hadoop"

findspark.init()
spark = SparkSession.builder.getOrCreate()

pfizer_df = spark.read.csv("dataset_Vaccine_Pfizer.csv", header=True, inferSchema=True)


def schema(x):
    """
    |-- id: string (nullable = true)
    |-- Text: string (nullable = true)
    |-- Subjectivity: string (nullable = true)
    |-- Polarity: string (nullable = true)
    |-- Target: string (nullable = true)
    """
    x.printSchema()


def number_of_tweets(x):
    print(x.filter(x["Text"].isNotNull()).count())


