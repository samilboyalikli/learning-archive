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
***
**Programlama Modeli**  

Structured Streaming’in temel fikri, **canlı veri akışını sürekli olarak eklenen bir tablo gibi ele almaktır**. Bu yaklaşım, **toplu işleme modeline çok benzeyen yeni bir akış işleme modeli** ortaya çıkarır. Akış hesaplamanızı, **statik bir tablo üzerinde çalıştırılan standart bir toplu sorgu gibi ifade edersiniz** ve **Spark, bunu sınırsız bir giriş tablosu üzerinde artımlı bir sorgu olarak çalıştırır**. Şimdi, bu modeli daha ayrıntılı bir şekilde inceleyelim.

![Unbounded Table](./images/ss1.png "Unbounded Table")

**Giriş tablosu** üzerindeki bir sorgu, **"Sonuç Tablosu"nu** oluşturur. Her **tetikleme aralığında** (örneğin, **her 1 saniyede bir**), **Giriş Tablosu'na yeni satırlar eklenir** ve bu da **Sonuç Tablosu'nun güncellenmesine neden olur**. **Sonuç Tablosu güncellendiğinde**, değişen sonuç satırlarını **harici bir hedefe (sink) yazmak isteriz**.

![Programming Model](./images/ss2.png "Programming Model")

**"Çıktı"**, dış depolamaya yazılan veriyi ifade eder. Çıktı, **farklı modlarda** tanımlanabilir:  

- **Complete Mode (Tam Mod)** – **Güncellenmiş Sonuç Tablosu'nun tamamı** dış depolamaya yazılır. **Tüm tablonun nasıl yazılacağına** karar vermek, **depolama bağlayıcısına** bağlıdır.  
- **Append Mode (Ekleme Modu)** – **Son tetikleme işleminden bu yana Sonuç Tablosu'na eklenen yeni satırlar** dış depolamaya yazılır. **Mevcut satırların değişmediği** sorgular için uygundur.  
- **Update Mode (Güncelleme Modu)** – **Son tetikleme işleminden bu yana değişen satırlar** dış depolamaya yazılır (**Spark 2.1.1 sürümünden itibaren** mevcuttur). **Tam Mod’dan farkı**, yalnızca **son değişen satırları** dışa aktarmasıdır. **Eğer sorguda bir toplama (aggregation) işlemi yoksa**, **Ekleme Modu’na eşdeğer olur**.  

Her modun **yalnızca belirli türdeki sorgular için geçerli olduğunu** unutmayın. Bu konuyu ilerleyen bölümlerde ayrıntılı olarak ele alacağız.  

Bu modelin kullanımını açıklamak için yukarıdaki **Hızlı Örnek (Quick Example)** bağlamında inceleyelim: İlk **lines DataFrame**, **giriş tablosunu** temsil eder. Nihai **wordCounts DataFrame**, **sonuç tablosudur**. **Streaming lines DataFrame üzerinde çalıştırılan sorgu**, **statik bir DataFrame üzerinde çalıştırılan sorguyla tamamen aynıdır**. Ancak, **bu sorgu çalıştırıldığında**, Spark: **Sürekli olarak socket bağlantısından yeni verileri kontrol eder**. **Yeni veri geldikçe**, **önceki sayımları yeni verilerle birleştiren bir "artımlı" sorgu çalıştırır**. Böylece **güncellenmiş kelime sayımları hesaplanır**. Aşağıda bu sürecin nasıl çalıştığını görebilirsiniz:

![Model of Quick Example](./images/ss3.png "Model of Quick Example")

Structured Streaming’in **tüm tabloyu materyalize etmediğini** unutmayın. Bunun yerine: **En son kullanılabilir veriyi** akış veri kaynağından okur. **Sonucu güncellemek için** veriyi **artımlı (incremental) olarak işler**. **Kaynak veriyi işledikten sonra atar**. **Sonucu güncellemek için gerekli olan minimum ara durumu (örneğin, önceki örnekteki ara sayımlar) saklar**.  

Bu model, **diğer birçok akış işleme motorundan önemli ölçüde farklıdır**. **Çoğu akış işleme sistemi**, **kullanıcının kendisinin sürekli agregasyonları yönetmesini gerektirir**. Bu durum, **hata toleransı (fault-tolerance)** ve **veri tutarlılığı (at-least-once, at-most-once, exactly-once gibi)** konularında **kullanıcının sorumluluk almasını gerektirir**. **Structured Streaming modeli** ise **yeni veri geldiğinde Sonuç Tablosu’nu güncelleme işini Spark’a bırakır**. **Böylece kullanıcılar, hata toleransı ve veri tutarlılığı gibi konularla uğraşmak zorunda kalmaz**. Bir örnek olarak, bu modelin **olay zamanı (event-time) tabanlı işlemeyi ve geç gelen verileri** nasıl ele aldığını inceleyelim.

### **Olay Zamanı (Event-time) ve Geç Gelen Verileri Yönetme**  

Olay zamanı (event-time), verinin içinde gömülü olan zamandır. Birçok uygulamada, bu olay zamanı üzerinden işlem yapmak isteyebilirsiniz. Örneğin: IoT cihazlarının her dakika ürettiği olayların sayısını hesaplamak istiyorsanız, Verinin Spark’a ulaştığı zaman yerine, verinin üretildiği zamanı (yani olay zamanı) kullanmak istersiniz. Bu olay zamanı, Structured Streaming modelinde doğal bir şekilde ifade edilir: -Cihazlardan gelen her olay, tabloda bir satırdır. -Olay zamanı, satırdaki bir sütun değeridir. -Bu, pencere tabanlı (window-based) agregasyonların doğrudan event-time sütununda bir gruplama ve toplama türü olarak çalışmasını sağlar. -Her zaman penceresi bir grup olur. -Her satır birden fazla pencereye/gruba ait olabilir. -Bu sayede, event-time penceresi tabanlı agregasyon sorguları, -Hem statik bir veri kümesinde (örneğin, toplanmış cihaz olay günlükleri üzerinde) -Hem de bir veri akışında tutarlı bir şekilde tanımlanabilir. Böylece, kullanıcıların hayatını önemli ölçüde kolaylaştırır.  

Bu model, olay zamanına göre beklenenden daha geç gelen verileri doğal bir şekilde ele alır. Spark, Sonuç Tablosu’nu güncellediği için, geç gelen veriler geldiğinde eski agregasyonları güncelleme ve ara durumun boyutunu sınırlamak için eski agregasyonları temizleme yetkisine sahiptir. Spark 2.1 ile birlikte, geç gelen veriler için eşik belirlemeye olanak tanıyan watermarking desteği eklenmiştir. Bu mekanizma, kullanıcının belirlediği bir eşik süresine göre eski durumları temizleyerek, sistemin bellek kullanımını optimize etmesini sağlar. Bu konular, ilerleyen bölümlerde "Window Operations" başlığı altında daha ayrıntılı olarak açıklanmaktadır.

### **Hata Toleransı (Fault Tolerance) Semantiği**  

Baştan sona tam olarak bir kez işleme (end-to-end exactly-once semantics) sağlamak, Structured Streaming’in tasarımındaki temel hedeflerden biridir. Bunu başarmak için: Structured Streaming’in veri kaynakları (sources), veri çıkış noktaları (sinks) ve yürütme motoru (execution engine) güvenilir şekilde tasarlanmıştır. İşlemin tam ilerleme durumu takip edilir, böylece herhangi bir hata durumunda sistem kendini yeniden başlatabilir ve/veya işlemi yeniden gerçekleştirebilir.

Tüm akış kaynakları (streaming sources), veri akışındaki okuma konumunu takip etmek için offset mekanizmasına sahiptir. Bu offsetler, Kafka’daki offset’lere veya Kinesis’teki sıra numaralarına benzer. İşlem motoru (execution engine), her tetikleme (trigger) sırasında işlenen verinin offset aralığını kaydetmek için Checkpointing (kontrol noktası alma) ve Write-ahead logs (ileri yazımlı günlükleme) kullanır. Akış çıkış noktaları (streaming sinks), yeniden işleme senaryolarına karşı idempotent olacak şekilde tasarlanmıştır. Yani, aynı veri tekrar işlense bile sonuç değişmez. Bu üç mekanizma sayesinde: Tekrar oynatılabilir kaynaklar (replayable sources) ve idempotent çıkış noktaları (sinks) birlikte çalışarak, Structured Streaming, herhangi bir hata durumunda "end-to-end exactly-once" semantiğini garanti edebilir.

# API Kullanarak Datasets ve DataFrames  

Spark 2.0'dan itibaren, DataFrame'ler ve Dataset'ler hem statik, sınırlı veriyi hem de akışkan, sınırsız veriyi temsil edebilir. Statik Dataset'ler/DataFrame'ler ile benzer şekilde, akış kaynaklarından akışkan DataFrame'ler/Dataset'ler oluşturmak için ortak giriş noktası olan SparkSession'ı (Scala/Java/Python/R dokümantasyonu) kullanabilir ve bunlar üzerinde statik DataFrame'ler/Dataset'ler ile aynı işlemleri uygulayabilirsiniz. Eğer Dataset'ler/DataFrame'ler ile daha önce çalışmadıysanız, öncelikle DataFrame/Dataset Programlama Kılavuzu'nu incelemeniz şiddetle tavsiye edilir.

### **Akışkan DataFrame'ler ve Akışkan Dataset'ler Oluşturma**  

Akışkan DataFrame'ler, `SparkSession.readStream()` tarafından döndürülen `DataStreamReader` arayüzü (Scala/Java/Python dokümantasyonu) aracılığıyla oluşturulabilir. R dilinde ise `read.stream()` metodu kullanılır. Statik DataFrame oluşturmak için kullanılan `read` arayüzüne benzer şekilde, veri kaynağının detaylarını – veri formatı, şema, seçenekler vb. – belirtebilirsiniz.

**Girdi Kaynakları**  

Birkaç yerleşik veri kaynağı bulunmaktadır:  

- **Dosya kaynağı** – Bir dizine yazılan dosyaları veri akışı olarak okur. Dosyalar, değiştirilme zamanına göre işlenir. Eğer `latestFirst` ayarlanmışsa, işlem sırası tersine çevrilir. Desteklenen dosya formatları şunlardır: **text, CSV, JSON, ORC, Parquet**. Daha güncel bir liste ve her dosya formatı için desteklenen seçenekler için **DataStreamReader** arayüzü dokümantasyonuna bakabilirsiniz. Unutmayın, dosyalar belirtilen dizine atomik olarak yerleştirilmelidir; çoğu dosya sisteminde bu, dosya taşıma işlemleriyle sağlanabilir.  

- **Kafka kaynağı** – Kafka'dan veri okur. Kafka broker sürümü 0.10.0 veya üstü ile uyumludur. Daha fazla bilgi için **Kafka Entegrasyon Kılavuzu**'na bakabilirsiniz.  

- **Soket kaynağı (test amaçlı)** – Bir soket bağlantısından UTF-8 metin verisi okur. Dinleme yapan sunucu soketi driver'da bulunur. Bu, uçtan uca hata toleransı garantisi sunmadığı için yalnızca test amaçlı kullanılmalıdır.  

- **Rate kaynağı (test amaçlı)** – Belirtilen hızda saniyede belirli sayıda satır üreten bir veri kaynağıdır. Her çıktıda bir zaman damgası (timestamp) ve bir değer (value) bulunur. **timestamp** → Mesajın gönderildiği zamanı içeren **Timestamp** türünde bir değerdir. **value** → **Long** türünde bir değer olup, **0'dan başlayarak mesaj sayısını** ifade eder. Bu kaynak, test ve performans kıyaslamaları (benchmarking) için tasarlanmıştır.  

- **Mikro-Toplu Rate kaynağı (test amaçlı)** – Her mikro-toplu işlem (micro-batch) için belirlenen sayıda satır üreten bir veri kaynağıdır. Her çıktıda bir zaman damgası (timestamp) ve bir değer (value) bulunur. **timestamp** → Mesajın gönderildiği zamanı içeren **Timestamp** türünde bir değerdir. **value** → Long türünde bir değer olup, 0'dan başlayarak mesaj sayısını ifade eder. Rate kaynağından farklı olarak, bu kaynak her mikro-toplu işlemde (micro-batch) tutarlı bir giriş verisi seti sağlar. Örneğin: Batch 0 → 0 - 999, Batch 1 → 1000 - 1999 ve bu şekilde devam eder... Aynı mantık, oluşturulan zaman değerleri için de geçerlidir. Bu kaynak da test ve performans kıyaslamaları (benchmarking) için tasarlanmıştır.

Bazı kaynaklar, hata toleranslı değildir çünkü bir hata sonrası checkpoint edilmiş offset'ler kullanılarak verinin yeniden oynatılacağını garanti etmezler. Hata toleransı kavramlarıyla ilgili önceki bölüme göz atabilirsiniz. Aşağıda, Spark'taki tüm veri kaynaklarının detayları verilmiştir.

| **Kaynak** | **Seçenekler** | **Hata Toleransı** | **Notlar** |
|------------|--------------|----------------|---------|
| **Dosya Kaynağı (File source)** | **path**: Girdi dizininin yolu, tüm dosya formatları için ortak.  <br> **maxFilesPerTrigger**: Her tetiklemede işlenecek maksimum yeni dosya sayısı (varsayılan: sınırsız). <br> **latestFirst**: Büyük bir dosya birikimi varsa, en yeni dosyaları önce işlemek için kullanılır (varsayılan: false). <br> **fileNameOnly**: Yeni dosyaların sadece dosya adına göre kontrol edilip edilmeyeceğini belirler (varsayılan: false). <br> **maxFileAge**: Bir dosyanın dizinde ne kadar süreyle geçerli kabul edileceğini belirler (varsayılan: 1 hafta). <br> **cleanSource**: İşlenen dosyaların temizlenmesini sağlar. Seçenekler: "archive", "delete", "off" (varsayılan: "off").  | **Evet** | Küresel (glob) yolları destekler ancak virgülle ayrılmış birden fazla yol/glob desteklemez. |
| **Soket Kaynağı (Socket Source)** | **host**: Bağlanılacak ana makine (zorunlu). <br> **port**: Bağlanılacak port (zorunlu). | **Hayır** | |
| **Oran Kaynağı (Rate Source)** | **rowsPerSecond**: Saniyede kaç satır üretileceği (varsayılan: 1, örn. 100). <br> **rampUpTime**: Belirtilen hız olan *rowsPerSecond* değerine ne kadar sürede ulaşılacağı (varsayılan: 0 saniye). <br> **numPartitions**: Üretilen satırların kaç bölüme ayrılacağı (varsayılan: Spark'ın varsayılan paralelliği). | **Evet** | Kaynak, belirtilen satır hızına ulaşmaya çalışır ancak sistem kaynak kısıtlamalarına bağlı olarak hız değişebilir. |
| **Mikro-Batch Oran Kaynağı (Rate Per Micro-Batch Source)** | **rowsPerBatch**: Her mikro-batch için kaç satır üretileceği. <br> **numPartitions**: Üretilen satırların kaç bölüme ayrılacağı (varsayılan: Spark'ın varsayılan paralelliği). <br> **startTimestamp**: Üretilen zamanın başlangıç değeri (varsayılan: 0). <br> **advanceMillisPerBatch**: Her mikro-batch’te zamanın ne kadar ileri alınacağı (varsayılan: 1000ms). | **Evet** | |
| **Kafka Kaynağı (Kafka Source)** | Ayrıntılar için [Kafka Entegrasyon Rehberi](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html)ne bakın. | **Evet** | |
---
  
İşte bazı örnekler.
```Py
spark = SparkSession. ...

# Read text from socket
socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

socketDF.isStreaming()    # Returns True for DataFrames that have streaming sources

socketDF.printSchema()

# Read all the csv files written atomically in a directory
userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark \
    .readStream \
    .option("sep", ";") \
    .schema(userSchema) \
    .csv("/path/to/directory")  # Equivalent to format("csv").load("/path/to/directory")
```

Bu örnekler, türü belirtilmemiş (untyped) akışkan (streaming) DataFrame'ler oluşturur. Bu, DataFrame'in şemasının derleme (compile) zamanında kontrol edilmediği, yalnızca sorgu çalıştırıldığında çalışma (runtime) zamanında kontrol edildiği anlamına gelir. map, flatMap gibi bazı işlemler derleme zamanında tür bilgisine ihtiyaç duyar. Bu işlemleri gerçekleştirebilmek için, türü belirtilmemiş (untyped) akışkan DataFrame’leri, statik DataFrame’lerde kullanılan aynı yöntemlerle, türü belirtilmiş (typed) akışkan Dataset’lere dönüştürebilirsiniz. Daha fazla ayrıntı için **SQL Programlama Rehberi**'ne bakabilirsiniz. Ek olarak, desteklenen akışkan veri kaynakları hakkında daha fazla ayrıntı belgenin ilerleyen bölümlerinde ele alınmaktadır.  
 
Spark 3.1 sürümünden itibaren, `DataStreamReader.table()` yöntemiyle tablolar üzerinden de akışkan DataFrame’ler oluşturabilirsiniz. Daha fazla bilgi için Streaming Table API’lerine göz atabilirsiniz.  

### **Akışkan DataFrame/Dataset'lerde Şema Çıkarımı ve Bölümlendirme (Partition)**  

Varsayılan olarak, dosya tabanlı kaynaklardan yapılan Structured Streaming işlemlerinde, şemanın otomatik olarak çıkarılması yerine açıkça belirtilmesi gerekmektedir. Bu kısıtlama, sorgunun tutarlı bir şema ile çalışmasını garanti altına almak için uygulanmıştır, hatta bir hata durumunda bile aynı şema korunur. Ancak, geçici (ad-hoc) kullanım durumları için `spark.sql.streaming.schemaInference` ayarını true yaparak şema çıkarımını tekrar etkinleştirebilirsiniz.

Eğer dizin yapısı `/key=value/` formatında isimlendirilmiş alt dizinler içeriyorsa, bölüm keşfi (partition discovery) otomatik olarak gerçekleşir ve Spark bu dizinleri tarayarak içeriğe erişir. Kullanıcı tarafından sağlanan şema içerisinde bu bölüm sütunları (partition columns) yer alıyorsa, Spark okunan dosyanın yolu üzerinden bu değerleri otomatik olarak dolduracaktır. Ancak, bölümleme şemasını oluşturan dizinler sorgu başladığında mevcut olmalı ve sorgu süresince değişmemelidir. Örneğin, `/data/year=2015/` dizini mevcutken `/data/year=2016/` eklemek geçerlidir, ancak bölümleme sütununu değiştirmek (örn. `/data/date=2016-04-17/` şeklinde bir dizin oluşturmak) geçersizdir.

## **Akışkan (Streaming) DataFrame/Dataset Üzerinde İşlemler**  

Akışkan DataFrame/Dataset'ler üzerinde çeşitli işlemler uygulayabilirsiniz. SQL benzeri, şemasız işlemler (örneğin: `select`, `where`, `groupBy`) ile; RDD benzeri, türü belirli işlemler (örneğin: `map`, `filter`, `flatMap`) yapabilirsiniz. Daha fazla ayrıntı için SQL programlama kılavuzuna göz atabilirsiniz. Şimdi, kullanabileceğiniz birkaç temel işlem örneğine bakalım.  

### **Temel İşlemler - Seçim (Selection), Yansıtma (Projection), ve Kümeleme (Aggregation)**  

DataFrame/Dataset üzerindeki en yaygın işlemlerin çoğu akışkan veriler için desteklenmektedir. Ancak, desteklenmeyen bazı işlemler de bulunmaktadır; bunlar bu bölümün ilerleyen kısımlarında açıklanacaktır.

```Py
df = ...  # streaming DataFrame with IOT device data with schema { device: string, deviceType: string, signal: double, time: DateType }

# Select the devices which have signal more than 10
df.select("device").where("signal > 10")

# Running count of the number of updates for each device type
df.groupBy("deviceType").count()
```

Bir akışkan (streaming) DataFrame/Dataset'i geçici bir görünüm (temporary view) olarak kaydedebilir ve ardından üzerinde SQL komutları çalıştırabilirsiniz.

```Py
df.createOrReplaceTempView("updates")
spark.sql("select count(*) from updates")  # returns another streaming DF
```

Bir DataFrame/Dataset'in akış verisi içerip içermediğini df.isStreaming kullanarak belirleyebilirsiniz.

```Py
df.isStreaming()
```

Bir sorgunun planını kontrol etmek isteyebilirsiniz, çünkü Spark, akış veri kümesine karşı SQL ifadesini işlerken durumsal işlemler ekleyebilir. Sorgu planına durumsal işlemler eklendiğinde, sorgunuzu durumsal işlemleri göz önünde bulundurarak değerlendirmeniz gerekebilir (örn. çıktı modu, watermark, durum deposu boyutunun yönetimi vb.).

#### Olay Zamanına Göre Pencere İşlemleri

Kaynaklanan olay-zamanına (event-time) göre kayan pencere (sliding window) üzerinden yapılan toplu işlemler, **Structured Streaming** ile oldukça basittir ve gruplandırılmış toplu işlemlere oldukça benzer. Gruplandırılmış bir toplu işlemde, kullanıcı tarafından belirtilen gruplama sütunundaki her benzersiz değer için toplu veriler (örn. sayaçlar) tutulur. Pencere tabanlı toplu işlemlerde ise, bir satırın olay zamanı hangi pencereye denk geliyorsa, o pencere için toplu veriler saklanır. Bunu bir örnekle daha iyi anlayalım.  

Örneğin, önceki hızlı örneğimizi biraz değiştirip, veri akışının artık her satırla birlikte o satırın oluşturulma zamanını da içerdiğini düşünelim. Kelimeleri saymak yerine, 10 dakikalık pencerelerde, her 5 dakikada bir güncellenen kelime sayımlarını almak istiyoruz. Yani, 12:00 - 12:10, 12:05 - 12:15, 12:10 - 12:20 gibi 10 dakikalık pencerelerdeki kelime sayımlarını hesaplayacağız. Burada 12:00 - 12:10, 12:00'dan sonra ve 12:10'dan önce gelen verileri içerir. Şimdi, 12:07’de alınan bir kelimeyi düşünelim. Bu kelimenin hem 12:00 - 12:10 hem de 12:05 - 12:15 pencerelerine dahil edilmesi gerekir, çünkü her ikisinin de zaman aralığına uymaktadır. Böylece, kelime sayıları hem gruplama anahtarına (kelimenin kendisi) hem de pencereye (olay zamanına göre hesaplanan) göre indekslenir.  

Sonuç tabloları şu şekilde görünecektir.

!["A Result Table"](./images/ss4.png "A Result Table")

Bu pencereleme işlemi gruplamaya benzediğinden, kod içinde `groupBy()` ve `window()` işlemlerini kullanarak pencere tabanlı toplu işlemleri ifade edebilirsiniz. Aşağıdaki örneklerin tam kodunu Scala/Java/Python dillerinde bulabilirsiniz.

```Py
words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }

# Group the data by window and word and compute the count of each group
windowedCounts = words.groupBy(
    window(words.timestamp, "10 minutes", "5 minutes"),
    words.word
).count()
```

