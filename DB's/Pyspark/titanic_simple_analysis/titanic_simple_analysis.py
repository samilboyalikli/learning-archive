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
#           3.3.1. (checked) farklı sınıflardaki bilet fiyatlarını hesaplanacak.
#           3.3.2. (checked) yaş ve bilet arasındaki ilişki analiz edilecek.
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
    # | -- SibSp: integer(nullable=true) (Siblings/Spouses)
    # | -- Parch: integer(nullable=true) (Parents/Children)
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


class PriceAnalysis:
    def __init__(self, x):
        self.fare_ob_class = x.groupBy("Pclass").avg("Fare").orderBy("Pclass")

        self.first_class = x.where(x["Age"] < 10) \
            .groupBy("Age") \
            .agg({"Fare": "avg", "Age": "avg"}) \
            .orderBy("Age")
        self.second_group = x.where((x["Age"] > 10) & (x["Age"] < 20)) \
            .groupBy("Age") \
            .agg({"Fare": "avg", "Age": "avg"}) \
            .orderBy("Age")
        self.third_group = x.where((x["Age"] > 20) & (x["Age"] < 30)) \
            .groupBy("Age") \
            .agg({"Fare": "avg", "Age": "avg"}) \
            .orderBy("Age")
        self.forth_group = x.where((x["Age"] > 30) & (x["Age"] < 40)) \
            .groupBy("Age") \
            .agg({"Fare": "avg"}) \
            .orderBy("Age")
        self.fifth_group = x.where((x["Age"] > 40) & (x["Age"] < 50)) \
            .groupBy("Age") \
            .agg({"Fare": "avg"}) \
            .orderBy("Age")
        self.sixth_group = x.where((x["Age"] > 50) & (x["Age"] < 60)) \
            .groupBy("Age") \
            .agg({"Fare": "avg"}) \
            .orderBy("Age")
        self.seventh_group = x.where((x["Age"] > 60) & (x["Age"] < 70)) \
            .groupBy("Age") \
            .agg({"Fare": "avg"}) \
            .orderBy("Age")
        self.eighth_group = x.where((x["Age"] > 70) & (x["Age"] < 80)) \
            .groupBy("Age") \
            .agg({"Fare": "avg"}) \
            .orderBy("Age")

        self.first_group_first_column = self.first_class.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.second_group_first_column = self.second_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.third_group_first_column = self.third_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.forth_group_first_column = self.forth_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.fifth_group_first_column = self.fifth_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.sixth_group_first_column = self.sixth_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.seventh_group_first_column = self.seventh_group.agg({"avg(Fare)": "avg"}).collect()[0][0]
        self.eighth_group_first_column = self.eighth_group.agg({"avg(Fare)": "avg"}).collect()[0][0]

        self.columns = ["Fare Average", "Age Range"]
        self.data = [
            (round(self.first_group_first_column, 3), "0-10"),
            (round(self.second_group_first_column, 3), "10-20"),
            (round(self.third_group_first_column, 3), "20-30"),
            (round(self.forth_group_first_column, 3), "30-40"),
            (round(self.fifth_group_first_column, 3), "40-50"),
            (round(self.sixth_group_first_column, 3), "50-60"),
            (round(self.seventh_group_first_column, 3), "60-70"),
            (round(self.eighth_group_first_column, 3), "70-80")
        ]
        self.new_df = spark.createDataFrame(self.data, self.columns)

    def show_price_average_by_class(self):
        self.fare_ob_class.show()

    def show_price_age_association(self):
        self.new_df.show()


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
