"""
SIMPLE ANALYSIS OF TITANIC DATASET FROM KAGGLE
"""

# TODO
#   1. (checked) Verisetinin Şeması çıkarılacak.
#   2. (checked) Şema GPT'ye verilecek.
#   3. İstenen datalar tespit edilecek.
#       3.1. (checked) veri temizleme işlemleri
#           3.1.1. (checked) tablonun kopyası alınacak ve analiz kopya üzerinde gerçekleştirilecek.
#           3.1.2. (checked) eksik değerler kontrol edilecek.
#           3.1.3. (checked) eksik değerler silinecek.
#           3.1.4. (checked) cinsiyet dağılımları hesaplanacak
#           3.1.5. (checked) şehir dağılımları hesaplanacak.
#       3.2. (checked) tanımlayıcı istatistiklerin hesaplanması (tüm sütunlar için)
#           3.2.1. (checked) ortamala
#           3.2.2. (checked) medyan
#           3.2.3. (checked) standart sapma
#           3.2.4. (checked) min/max değerler
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
    """This method gives you schema of dataset."""
    # root
    # | -- PassengerId: integer(nullable=true)
    # | -- "Pclass": integer(nullable=true)
    # | -- Name: string(nullable=true)
    # | -- Sex: string(nullable=true)
    # | -- Age: double(nullable=true)
    # | -- SibSp: integer(nullable=true)
    # | -- Parch: integer(nullable=true)
    # | -- Ticket: string(nullable=true)
    # | -- Fare: double(nullable=true)
    # | -- Cabin: string(nullable=true)
    # | -- Embarked: string(nullable=true)
    return x.printSchema()


class CleanedData:
    """
    This class includes data cleaning operations and some processes with cleaned data.

    Usable with these ways:
        CleanedData(dataset).city_d.show()
        CleanedData(dataset).gd.show()
        CleanedData(dataset).cd.show()

    also usable with these ways:
        CleanedData(dataset).show_clean_dataset
        CleanedData(dataset).show_gender_distribution
        CleanedData(dataset).show_city_distribution
    """
    def __init__(self, x):
        """
        Args:
            cd (dataframe): Cleaned data.
            gd (dict): Gender distribution.
            city_d (dict): City distribution.

        :param x: The input dataset.
        :returns: Returns the cleaned dataframe, gender distribution and city distribution
        """
        self.cd = x.na.drop(how="all")
        self.gd = self.cd.groupBy("Sex").count()
        self.city_d = self.cd.groupBy("Embarked").count()

    def show_clean_dataset(self):
        self.cd.show()

    def show_gender_distribution(self):
        self.gd.show()

    def show_city_distribution(self):
        self.city_d.show()


class DescriptiveStats:
    """
    This class includes some descriptive statistics.

    You can see output of this class with these ways:
        DescriptiveStats(dataset).a.show()
        DescriptiveStats(dataset).d.show()
        print(DescriptiveStats(dataset).m)

    also usable with these ways:
        DescriptiveStats(dataset).show_average()
        DescriptiveStats(dataset).show_describe()
        DescriptiveStats(dataset).show_median()
    """
    def __init__(self, x):
        """
        Args:
            a (dict): Average values
            d (dict): Descriptive datas
            m (dict): Median of columns

        :param x: The input dataset.
        :returns: Returns the average values, descriptive datas and median of columns.
        """
        self.a = x.groupBy().avg("Pclass", "SibSp", "Parch", "Age", "Fare")
        self.d = x.describe("Pclass", "SibSp", "Parch", "Age", "Fare")
        self.m = x.approxQuantile(["Pclass", "SibSp", "Parch", "Age", "Fare"], [0.5], 0)

    def show_average(self):
        self.a.show()

    def show_describe(self):
        self.d.show()

    def show_median(self):
        print(self.m)


def price_analysis(x):
    """Price Analysis Operations"""
    # TODO
    #   3.3.1. farklı sınıflardaki bilet fiyatlarını hesaplanacak.
    #   3.3.2. yaş ve bilet arasındaki ilişki analiz edilecek.
    return print(x)


def visualisation(x):
    """Visualisation Processes"""
    # TODO
    #   3.4.1. yaş dağılımı görselleştirilecek.
    #   3.4.2. cinsiyete göre hayatta kalma oranları karşılaştırılacak.
    return print(x)


def property_analysis(x):
    """Property Analysis Operations"""
    # TODO
    #   3.5.1. aile büyüklüğü üzerine bir sütun oluşturulacak.
    #   3.5.2. yaş gruplarının tanımlandığı yeni bir kategori oluşturulacak.
    return print(x)


def group_analyzes(x):
    """Group Analyzes"""
    # TODO
    #   3.6.1. cinsiyet ve sınıfa göre hayatta kalan yolcu sayıları hesaplanacak.
    #   3.6.2. farklı şehirlerden gelen yolcuların sayısı karşılaştırılacak.
    print(x)
