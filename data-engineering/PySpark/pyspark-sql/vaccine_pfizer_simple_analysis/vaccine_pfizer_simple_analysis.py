"""
SIMPLE ANALYSIS ON THE VACCINE PFIZER DATASET

This dataset will be show some relationship between subjectivity and polarity.
Here exist some descriptions about "components" and "queries" which I coded:

1. Components
    1.1. Subjectivity: A score between 0 and 1 that represents the degree of subjectivity in the tweet.
         1.1.1.    Objective: Score between 0.00000 and 0.33333. \n
         1.1.2.    Half-Objective: Score between 0.33333 and 0.66666. \n
         1.1.3.    Subjective: Score between 0.66666 and 1. \n
    1.2. Polarity: A sentiment polarity score, ranging from -1 (extremely negative) to 1 (extremely positive).
         1.2.1.    Hate: Score between -1 and -0.33333. \n
         1.2.2.    Neutral: Score between -0.33333 and 0.33333. \n
         1.2.3.    Love: Score between 0.33333 and 1.
2. Queries
    2.1. q1     |   Count of "hate" according to "objective" \n
    2.2. q2     |   Count of "neutral" according to "objective" \n
    2.3. q3     |   Count of "love" according to "objective" \n
    2.4. q4     |   Count of "objective" according to "neutral" \n
    2.5. q5     |   Count of "half-objective" according to "neutral" \n
    2.6. q6     |   Count of "subjective" according to "neutral"
"""

import findspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import os

os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['hadoop.home.dir'] = "C:\\hadoop"

findspark.init()
spark = SparkSession.builder.getOrCreate()

pfizer_df = spark.read.csv("dataset_Vaccine_Pfizer.csv", header=True, inferSchema=True)
tolerance = 0.001


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


def polarity(x):
    new_df = x.withColumn("Polarity_of_Tweet", f.when(x.Polarity < -tolerance, "negative")
                                                .when((x.Polarity > -tolerance) & (x.Polarity < tolerance), "neutral")
                                                .when(x.Polarity > tolerance, "positive")
                                                .otherwise("NULL"))
    new_df.show()


def contain_pfizer(x):
    print(x.filter((pfizer_df.Text.contains("pfizer")) | (x.Text.contains("Pfizer"))).count())


def tallest_tweet(x):
    max_length = x.select(f.max(f.length(x["Text"])).alias("max_length")).collect()[0]["max_length"]
    data = x.filter(f.length(x.Text) == max_length)
    data.select("Text").show()


def most_used_words(x, y):
    """
    :Example: most_used_words(pfizer_df, 5)
    """
    step1 = x.withColumn("words_without_mark", f.regexp_replace(x.Text, r"[^\w\s]", ""))
    step2 = step1.withColumn("lower_words", f.lower(step1.words_without_mark))
    step3 = step2.withColumn("splitted_words", f.split(step2.lower_words, " "))
    step4 = step3.withColumn("words", f.explode(step3.splitted_words))
    step5 = step4.na.drop()
    step6 = step5.filter(~(step5.words.isNull() | (f.trim(step5.words) == "")))
    result = step6.groupBy("words").count()
    result.orderBy("count", ascending=False).limit(y).show()


def subjectivity_of_targets(x):
    s1 = x.withColumn("Target", f.when(((x.Target > -tolerance) & (x.Target < tolerance)), "Neutral")
                                 .when((x.Target > tolerance), "Positive")
                                 .when((x.Target < -tolerance), "Negative")
                                 .otherwise(x.Target))
    s2 = s1.select("*").filter(s1.Target.isNotNull()).drop()
    s3 = s2.withColumn("Sub", s2.Subjectivity.cast("float"))
    result = s3.groupBy("Target").agg(f.count("Target").alias("Target Count"), f.avg("Sub").alias("Sub Average")) \
        .orderBy("Sub Average", ascending=True)
    result.show()


df = pfizer_df.na.drop()
df = df.withColumn("subjectivity_level",
                   f.when((df.Subjectivity >= 0.00000) & (df.Subjectivity <= 0.33333), "objective")
                   .when((df.Subjectivity >= 0.33333) & (df.Subjectivity <= 0.66666), "half_objective")
                   .when((df.Subjectivity >= 0.66666) & (df.Subjectivity <= 1), "subjective")
                   .otherwise(":/"))
df = df.withColumn("polarity_level",
                   f.when((df.Polarity >= -1) & (df.Polarity <= -0.33333), "hate")
                   .when((df.Polarity >= -0.33333) & (df.Polarity <= 0.33333), "neutral")
                   .when((df.Polarity >= 0.33333) & (df.Polarity <= 1), "love")
                   .otherwise(":/"))
q1 = df.select("*").filter((df.subjectivity_level == "objective") & (df.polarity_level == "hate")) \
    .groupBy("polarity_level").count()
q2 = df.select("*").filter((df.subjectivity_level == "objective") & (df.polarity_level == "neutral")) \
    .groupBy("polarity_level").count()
q3 = df.select("*").filter((df.subjectivity_level == "objective") & (df.polarity_level == "love")) \
    .groupBy("polarity_level").count()
q4 = df.select("*").filter((df.polarity_level == "neutral") & (df.subjectivity_level == "objective")) \
    .groupBy("subjectivity_level").count()
q5 = df.select("*").filter((df.polarity_level == "neutral") & (df.subjectivity_level == "half_objective")) \
    .groupBy("subjectivity_level").count()
q6 = df.select("*").filter((df.polarity_level == "neutral") & (df.subjectivity_level == "subjective")) \
    .groupBy("subjectivity_level").count()
