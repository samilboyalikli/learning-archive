"""
SIMPLE ANALYSIS ON THE VACCINE PFIZER DATASET

TEXT:
Description: The content of the tweet in textual form.
Type: String.
Purpose: Provides the actual content of each tweet.
This column can be used for various natural language processing (NLP) tasks such as sentiment analysis,
keyword extraction, and topic modeling.

SUBJECTIVITY:
Description: A score between 0 and 1 that represents the degree of subjectivity in the tweet.
A score of 0 means the tweet is objective, while a score of 1 indicates it is highly subjective.
Type: Float (range: 0 to 1).
Purpose: Indicates how much of the tweet is based on personal opinion versus factual information.
This can be useful for identifying tweets that are more opinion-driven.

POLARITY:
Description: A sentiment polarity score, ranging from -1 (extremely negative) to 1 (extremely positive).
Type: Float (range: -1 to 1).
Purpose: Used to determine the emotional tone of the tweet, whether it is negative, neutral, or positive.
This column is key for sentiment analysis tasks.

TARGET:
Description: A binary variable indicating the overall sentiment of the tweet towards the Pfizer vaccine.
A value of 0 indicates a negative sentiment, and a value of 1 indicates a positive sentiment.
Type: Integer (0 or 1).
Purpose: Serves as the target label for machine learning models. It helps to classify the sentiment of the tweets as
positive or negative.
"""

# TODO
#   1. (checked) tweet sayısı bulunacak.
#   2. (checked) pozitif/negatif tweet sayısı bulunacak.
#   3. (checked) "pfizer" kelimesini içeren tweetler bulunup görüntülenecek.
#   4. (checked) en uzun tweet bulunacak.
#   5. (checked) en çok geçen kelime bulunacak.
#   6. (checked) konu dağılımı analiz edilecek.
#   7. subjectivity/polarity arasındaki ilişki analiz edilecek.

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


def subjectivity_polarity():
    """
    This dataset will be show some relationship between subjectivity and polarity.

    1. Subjectivity: A score between 0 and 1 that represents the degree of subjectivity in the tweet.
        1.1.    Objective: Score between 0.00000 and 0.33333. \n
        1.2.    Half-Objective: Score between 0.33333 and 0.66666. \n
        1.3.    Subjective: Score between 0.66666 and 1. \n
    2. Polarity: A sentiment polarity score, ranging from -1 (extremely negative) to 1 (extremely positive).
        2.1.    Hate: Score between -1 and -0.33333. \n
        2.2.    Neutral: Score between -0.33333 and 0.33333. \n
        2.3.    Love: Score between 0.33333 and 1. \n

    TODO
        1. (checked) Determining the "objective" range for the Subjectivity column. (oc)
        2. (checked) Determining the "half-objective" range for the Subjectivity column. (hoc)
        3. (checked) Determining the "subjective" range for the Subjectivity column. (sc)
        4. (checked) Determining the "hate" range for the Polarity column. (hc)
        5. (checked) Determining the "neutral" range for the Polarity column. (nc)
        6. (checked) Determining the "love" range for the Polarity column. (lc)
        7. Average of hc according to oc
        8. Average of nc according to oc
        9. Average of lc according to oc
        10. Average of oc according to nc
        11. Average of hoc according to nc
        12. Average of sc according to nc
    """
    df = pfizer_df.na.drop()
    oc = df.select("*").filter((df.Subjectivity >= 0.00000) & (df.Subjectivity <= 0.33333))
    hoc = df.select("*").filter((df.Subjectivity >= 0.33333) & (df.Subjectivity <= 0.66666))
    sc = df.select("*").filter((df.Subjectivity >= 0.66666) & (df.Subjectivity <= 1))
    hc = df.select("*").filter((df.Polarity >= -1) & (df.Polarity <= -0.33333))
    nc = df.select("*").filter((df.Polarity >= -0.33333) & (df.Polarity <= 0.33333))
    lc = df.select("*").filter((df.Polarity >= 0.33333) & (df.Polarity <= 1))

# q1 = pfizer_df.select("Subjectivity").filter((pfizer_df.Subjectivity >= 0.0000) & (pfizer_df.Subjectivity <= 0.33333)) \
#               .count()
# q1s1 = pfizer_df \
#     .select("Polarity", "Subjectivity").filter((pfizer_df.Polarity.isNotNull()) & (pfizer_df.Subjectivity.isNotNull()))\
#     .count()
#
# q2 = pfizer_df.select("Polarity").filter((pfizer_df.Polarity >= -0.33333) & (pfizer_df.Polarity <= 0.33333)).count()
# print("Subjectivity Range: ", q1, " ", "Polarity Range: ", q2)
