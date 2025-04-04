"""
SIMPLE ANALYSIS OF TITANIC DATASET FROM KAGGLE
"""

import findspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
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
    """
    This class includes some price analysis as understand its name.

    show_price_average_by_class():
    For analysing price average according to class.

    show_price_age_association():
    For see price/age association.

    Examples
    --------
    PriceAnalysis(dataset).show_price_average_by_class()
    PriceAnalysis(dataset).show_price_age_association()
    """
    def __init__(self, x):
        self.fare_ob_class = x.groupBy("Pclass").avg("Fare").orderBy("Pclass")

        self.first_class = x.where(x["Age"] < 10) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.second_group = x.where((x["Age"] > 10) & (x["Age"] < 20)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.third_group = x.where((x["Age"] > 20) & (x["Age"] < 30)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.forth_group = x.where((x["Age"] > 30) & (x["Age"] < 40)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.fifth_group = x.where((x["Age"] > 40) & (x["Age"] < 50)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.sixth_group = x.where((x["Age"] > 50) & (x["Age"] < 60)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.seventh_group = x.where((x["Age"] > 60) & (x["Age"] < 70)) \
            .groupBy("Age").agg({"Fare": "avg"})
        self.eighth_group = x.where((x["Age"] > 70) & (x["Age"] < 80)) \
            .groupBy("Age").agg({"Fare": "avg"})

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


class PropertyAnalysis:
    """
    This class gives you a chance to calculate the family size of all passengers and calculate age groups.

    show_table_with_family_size():
    For calculate the family size of all passengers.

    show_table_with_age_group()
    For calculate age groups of all passengers.

    Examples:
        PropertyAnalysis(dataframe).show_table_with_family_size()
        PropertyAnalysis(dataframe).show_table_with_age_group()
    """
    def __init__(self, x):
        self.family_size = x.withColumn("Family Size", x["SibSp"] + x["Parch"])
        self.age_group = x.withColumn("Age Group", f.when(x["Age"] < 18, "Minor")
                                                    .when((x["Age"] > 18) & (x["Age"] < 65), "Adult")
                                                    .otherwise("Senior"))

    def show_table_with_family_size(self):
        self.family_size.show()

    def show_table_with_age_group(self):
        self.age_group.show()
