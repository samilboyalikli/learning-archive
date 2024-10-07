"""
SIMPLE ANALYSIS OF TITANIC DATASET FROM KAGGLE
"""

# TODO
#   1. (checked) Verisetinin Şeması çıkarılacak.
#   2. (checked) Şema GPT'ye verilecek.
#   3. İstenen datalar tespit edilecek.
#       3.1. veri temizleme işlemleri
#           3.1.1. tablonun kopyası alınacak ve analiz kopya üzerinde gerçekleştirilecek.
#           3.1.2. eksik değerler kontrol edilecek.
#           3.1.3. eksik değerler silinecek.
#           3.1.4. cinsiyet ve şehir dağılımları hesaplanacak.
#       3.2. tanımlayıcı istatistiklerin hesaplanması (tüm sütunlar için)
#           3.2.1. ortamala
#           3.2.2. medyan
#           3.2.3. standart sapma
#           3.2.4. min/max değerler
#       3.3. fiyat analizi
#           3.3.1. farklı sınıflardaki bilet fiyatlarını hesaplanacak.
#           3.3.2. yaş ve bilet arasındaki ilişki analiz edilecek.
#       3.4. görselleştirme
#           3.4.1. yaş dağılımı görselleştirilecek.
#           3.4.2. cinsiyete göre hayatta kalma oranları karşılaştırılacak.
#       3.5. özellik analizi
#           3.5.1. aile büyüklüğü üzerine bir sütun oluşturulacak.
#           3.5.2. yaş gruplarının tanımlandığı yeni bir kategori oluşturulacak.
#       3.6. grup analizleri
#           3.6.1. cinsiyet ve sınıfa göre hayatta kalan yolcu sayıları hesaplanacak.
#           3.6.2. farklı şehirlerden gelen yolcuların sayısı karşılaştırılacak.
#   4. İstenen datalar bulunacak.
#   5. İstenen datalar kaydedilecek.


import findspark
from pyspark.sql import SparkSession
import os

os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['hadoop.home.dir'] = "C:\\hadoop"

findspark.init()
spark = SparkSession.builder.getOrCreate()

titanic_df = spark.read.csv("test.csv", header=True, inferSchema=True)


def dataframe_schema(x):
    """1. Dataset schema will be created"""
    return x.dfprintSchema()


def missing_values(x):
    """Missing Values Operations"""
    return print(x)
