**Genel Bakış**  

Structured Streaming, Spark SQL motoru üzerine inşa edilmiş, ölçeklenebilir ve hata toleranslı bir akış işleme motorudur. Akış hesaplamanızı, statik veriler üzerinde yapılan toplu işlemlerle aynı şekilde ifade edebilirsiniz. Spark SQL motoru, bu işlemi artımlı ve sürekli olarak çalıştırır ve akış verileri gelmeye devam ettikçe nihai sonucu günceller. Akış toplamaları, olay zamanı pencereleri, akıştan toplu işleme katılmalar gibi işlemleri ifade etmek için Scala, Java, Python veya R'deki Dataset/DataFrame API'lerini kullanabilirsiniz. Bu hesaplama, optimize edilmiş aynı Spark SQL motoru üzerinde çalıştırılır. Son olarak, sistem, uçtan uca **tam olarak bir kez (exactly-once)** hata toleransı garantilerini sağlamak için **checkpointing** (kontrol noktaları) ve **Write-Ahead Logs (WAL)** mekanizmalarını kullanır. Kısacası, Structured Streaming, kullanıcıların akış işlemlerinin detaylarını düşünmesine gerek kalmadan, hızlı, ölçeklenebilir ve hata toleranslı bir **uçtan uca tam olarak bir kez işleme (exactly-once processing)** sunar.  

Dahili olarak, varsayılan olarak, Structured Streaming sorguları **mikro-batch işleme motoru** kullanılarak işlenir. Bu yöntem, veri akışlarını küçük toplu iş yükleri serisi halinde işleyerek **100 milisaniye kadar düşük uçtan uca gecikme süresi** ve **tam olarak bir kez hata toleransı** sağlar. Ancak, Spark 2.3 sürümünden itibaren, **Sürekli İşleme (Continuous Processing)** adı verilen yeni bir **düşük gecikmeli işleme modu** tanıtılmıştır. Bu mod, **1 milisaniye kadar düşük uçtan uca gecikme süresi** sağlayabilir ancak **en az bir kez işleme (at-least-once processing)** garantisi sunar. Dataset/DataFrame işlemlerini değiştirmeden, uygulamanızın gereksinimlerine bağlı olarak uygun işleme modunu seçebilirsiniz.  

Bu kılavuzda, programlama modelini ve API'leri adım adım ele alacağız. Öncelikle varsayılan mikro-batch işleme modelini kullanarak temel kavramları açıklayacağız, ardından Sürekli İşleme modelini tartışacağız. Öncelikle, **Structured Streaming** ile **bir akış kelime sayımı sorgusunun** basit bir örneğiyle başlayalım.
***
**Hızlı Örnek**  

Diyelim ki, bir **TCP soketi** üzerinden gelen metin verisinin **anlık kelime sayımını** tutmak istiyorsunuz. Bunu **Structured Streaming** kullanarak nasıl ifade edebileceğinizi görelim. Bu kodun **Scala, Java, Python ve R** dillerindeki tam halini görebilirsiniz. Ayrıca, Spark’ı indirerek örneği doğrudan çalıştırabilirsiniz.  

Her durumda, örneği adım adım inceleyelim ve nasıl çalıştığını anlayalım. İlk olarak, gerekli sınıfları içe aktarmamız ve **Spark ile ilgili tüm işlemlerin başlangıç noktası olan yerel bir SparkSession oluşturmamız** gerekiyor.

```Py
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()
```
Şimdi, **localhost:9999** üzerinde dinleyen bir sunucudan alınan metin verilerini temsil eden bir **akış DataFrame’i** oluşturalım ve bu **DataFrame’i kelime sayılarını hesaplayacak şekilde dönüştürelim.**

```Py
# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words.groupBy("word").count()
```
Bu **lines DataFrame’i**, akış halinde gelen metin verilerini içeren **sınırsız bir tabloyu** temsil eder. Bu tablo, **"value"** adında tek bir string sütunu içerir ve akış verisindeki her satır, tablodaki bir satıra karşılık gelir. **Dikkat edilmesi gereken nokta:** Şu anda herhangi bir veri alınmıyor. Çünkü henüz işlemi başlatmadık, sadece dönüşüm adımlarını tanımlıyoruz. Sonraki adımda, iki **yerleşik SQL fonksiyonunu** kullandık:  -**split**: Her satırı kelimelere ayırmak için. -**explode**: Kelimeleri ayrı satırlar hâline getirmek için. Ayrıca, **alias** fonksiyonunu kullanarak yeni oluşturulan sütunun adını **"word"** olarak belirledik. Son olarak, **wordCounts DataFrame’i** oluşturduk. Bu DataFrame, veri kümesindeki **benzersiz kelimelere göre gruplama** yaparak **her birinin kaç kez geçtiğini** hesaplar. **Bu, akış verisinden elde edilen kelime sayılarını temsil eden bir akış DataFrame’idir.**  

Artık, akış verileri üzerinde sorgumuzu kurduk. Şimdi tek yapmamız gereken, **gerçekten veri alımını başlatmak** ve kelime sayılarını hesaplamak. Bunu yapmak için:  -**outputMode("complete")** belirterek **tam sonuç kümesini** her güncellemede **konsola yazdırılacak** şekilde ayarlıyoruz.  -**start()** fonksiyonunu çağırarak **akış hesaplamasını başlatıyoruz.**

```Py
 # Start running the query that prints the running counts to the console
query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```
Bu kod çalıştırıldıktan sonra, **akış hesaplaması arka planda başlatılmış olacak**. **Query** nesnesi, bu aktif akış sorgusuna bir referans sağlar ve **query çalışırken işlemin sonlanmasını önlemek için** `awaitTermination()` fonksiyonunu kullanarak sorgunun bitmesini beklemeye karar verdik.  

Bu örnek kodu **gerçekten çalıştırmak** için iki seçeneğiniz var: Birisi **kodu kendi Spark uygulamanızda derleyerek çalıştırabilirsiniz.** Veya **Spark’ı indirdikten sonra doğrudan örneği çalıştırabilirsiniz.** Biz ikinci yöntemi gösteriyoruz. Öncelikle, **Netcat**'i (çoğu Unix benzeri sistemde bulunan küçük bir yardımcı program) **bir veri sunucusu olarak çalıştırmanız gerekecek**. Bunun için şu komutu kullanabilirsiniz:

`$ nc -lk 9999`

Daha sonra, **farklı bir terminalde** aşağıdaki komutu kullanarak örneği başlatabilirsiniz:

```
$ ./bin/spark-submit examples/src/main/python/sql/streaming/structured_network_wordcount.py localhost 9999
```
Bundan sonra, **Netcat sunucusunun çalıştığı terminale yazdığınız her satır sayılacak ve her saniye ekrana yazdırılacaktır.** Çıktı aşağıdakine benzer şekilde görünecektir:

```
# TERMINAL 1:
# Running Netcat

$ nc -lk 9999
apache spark
apache hadoop
```
```
# TERMINAL 2: RUNNING structured_network_wordcount.py

$ ./bin/spark-submit examples/src/main/python/sql/streaming/structured_network_wordcount.py localhost 9999

-------------------------------------------
Batch: 0
-------------------------------------------
+------+-----+
| value|count|
+------+-----+
|apache|    1|
| spark|    1|
+------+-----+

-------------------------------------------
Batch: 1
-------------------------------------------
+------+-----+
| value|count|
+------+-----+
|apache|    2|
| spark|    1|
|hadoop|    1|
+------+-----+
...
```
