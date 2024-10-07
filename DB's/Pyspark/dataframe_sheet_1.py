import findspark
from pyspark.sql import SparkSession

findspark.init()
spark = SparkSession.builder.master("local[*]").getOrCreate()
spark.conf.set("spark.sql.repl.eagerEval.enabled", True)

titanic_df = spark.read.csv("train.csv", header=True, inferSchema=True)
# spark'ın read fonksiyonunu kullanarak csv dosyasını okumayı başlatıyoruz.
# buradaki dataları "titanic_df" olarak tanımlıyoruz.

"""
Böylece bir DataFrame oluşturmuş olduk. 
Aşağıda bu DataFrame'e hangi fonksiyonları uygulayabileceğimiz yer alacak.
"""

titanic_df.printSchema()
"""printSchema() -> table'ın şemasını gösterir"""
# output:
# root
# |-- PassengerId: integer (nullable = true)
# |-- Survived: integer (nullable = true)
# |-- Pclass: integer (nullable = true)
# |-- Name: string (nullable = true)
# |-- Sex: string (nullable = true)
# |-- Age: double (nullable = true)
# |-- SibSp: integer (nullable = true)
# |-- Parch: integer (nullable = true)
# |-- Ticket: string (nullable = true)
# |-- Fare: double (nullable = true)
# |-- Cabin: string (nullable = true)
# |-- Embarked: string (nullable = true)

titanic_df.limit(5)
"""limit() -> table'ın ilk 5 datasını getirecektir."""

titanic_df.select()
"""select() -> SQL'deki SELECT komutuna benzer eylemleri yapmamıza olanak tanır."""

titanic_df.select('PassengerId', 'Survived').limit(5)
# PassengerId ve Survived columnlarının ilk 5 satırını getirir.

titanic_df.where()
"""where() -> SQL'deki WHERE komutuna benzer eylemleri yapmamıza olanak tanır."""

titanic_df.where((titanic_df.Age > 25) & (titanic_df.Survived == 1)).limit(5)
# titanic_df table'ındaki Age sütununda 25 değerinde büyük ve
# titanic_df table'ındaki Survived sütununda 1'e eşit dataların
# ilk 5'ini getirir.

titanic_df.agg()
"""agg() -> SQL'deki aggregat fonksiyonlarına benzer eylemleri yapmamıza olanak tanır."""

titanic_df.agg({'Fare': 'avg'})
# Fare column'unun Average değerini getirir.

titanic_df.groupBy()
"""groupBy() -> SQL'deki GROUP BY komutuna benzer eylemleri yapmamıza olanak tanır."""

titanic_df.orderBy()
"""orderBy() -> SQL'deki ORDER BY komutuna benzer eylemleri yapmamıza olanak tanır."""

titanic_df.groupBy('Pclass').agg({'Fare': 'avg'}).orderBy('Pclass', ascending=False)
# titanic_df table'ındaki Pclass sütunundaki dataları grupluyoruz.
# Ardından bunların Fare değerlerinin ortalamalarını alıyoruz.
# Ardından bunları Pclass sütununa göre düzenliyoruz.
# Bu output DESC olarak çıkacak.

titanic_df.filter(titanic_df.Age > 25)
"""filter() -> DataFrame'deki belli şartlara uyan dataları filtreler"""

titanic_df.filter(titanic_df.Age > 25).agg({'Fare': 'avg'})
# titanic_df table'ındaki bazı dataları filtreleyip onların üzerinde işlem yapıyoruz.
# titanic_df table'ındaki Age sütunundaki 25 değerinden büyük dataları filtreliyoruz.
# filtrelediğimiz dataların Fare değerlerinin ortalamasını alıyoruz.

titanic_df.createOrReplaceTempView("Titanic")
"""createOrReplaceTempView() -> bu fonksiyon table'ı SQL komutlarına açar."""

spark.sql('select * from Titanic')
"""sql() -> table sql komutlarına hazır hale gelince bu fonksiyonla dümdüz SQL sorguları yazabiliyoruz."""

from pyspark.sql.types import IntegerType
"""bir sütunun veri tipini integer olarak tanımlamak için import ediyoruz"""

from pyspark.sql.functions import udf
"""udf - user defined function anlamına gelir. pythonda yazılmış fonksiyonları DataFrame'de kullanmamızı sağlar"""


def round_float_down(x):
    """round float_down adında bir fonksiyon oluşturuyoruz.
    bu fonksiyon girilen değeri bir tamsayıya dönüştürüyor."""
    return int(x)


round_float_down_udf = udf(round_float_down, IntegerType())
"""BURAYI ANLAMADIM"""

titanic_df.select('PassengerId', 'Fare', round_float_down_udf('Fare').alias('Fare Rounded Down')).limit(5)

spark.stop()
"""stop() -> spark session'ı durdurur."""
