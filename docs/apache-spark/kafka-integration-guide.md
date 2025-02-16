# "Structured Streaming + Kafka Entegrasyon Kılavuzu (Kafka broker sürümü 0.10.0 veya daha yeni)"

Kafka'dan veri okumak ve Kafka'ya veri yazmak için Structured Streaming entegrasyonu.  

## Bağlantı (Linking)  

Scala/Java uygulamaları için, eğer SBT/Maven proje tanımları kullanıyorsanız, uygulamanızı aşağıdaki bileşenle bağlayın:  

```
groupId = org.apache.spark
artifactId = spark-sql-kafka-0-10_2.12
version = 3.5.4
```

Lütfen unutmayın: Kafka mesaj başlıkları (headers) özelliğini kullanmak istiyorsanız, Kafka istemci (client) sürümünüzün en az **0.11.0.0** veya daha yeni bir sürüm olması gerekmektedir.  

Python uygulamaları için, uygulamanızı dağıtırken yukarıda belirtilen kütüphaneyi ve bağımlılıklarını eklemeniz gerekir. Bununla ilgili detaylar için aşağıdaki **Dağıtım (Deploying)** bölümüne bakabilirsiniz.  

`spark-shell` üzerinde denemeler yapmak için, `spark-shell`'i başlatırken yukarıda belirtilen kütüphaneyi ve bağımlılıklarını eklemeniz gerekir. Ayrıca, daha fazla bilgi için **Dağıtım (Deploying)** bölümüne göz atabilirsiniz.

## Kafka'dan Veri Okuma

### Akış Sorguları için Bir Kafka Kaynağı Oluşturma

```Py
# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Subscribe to 1 topic, with headers
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .option("includeHeaders", "true") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "headers")

# Subscribe to multiple topics
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1,topic2") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Subscribe to a pattern
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribePattern", "topic.*") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
```

**Toplu Sorgular için Bir Kafka Kaynağı Oluşturma**  

Eğer toplu (batch) işlemeye daha uygun bir kullanım senaryonuz varsa, belirli bir offset aralığı için bir Dataset/DataFrame oluşturabilirsiniz.

```Py
# Subscribe to 1 topic defaults to the earliest and latest offsets
df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Subscribe to multiple topics, specifying explicit Kafka offsets
df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1,topic2") \
  .option("startingOffsets", """{"topic1":{"0":23,"1":-2},"topic2":{"0":-2}}""") \
  .option("endingOffsets", """{"topic1":{"0":50,"1":-1},"topic2":{"0":-1}}""") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Subscribe to a pattern, at the earliest and latest offsets
df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribePattern", "topic.*") \
  .option("startingOffsets", "earliest") \
  .option("endingOffsets", "latest") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
```

Kaynaktaki her satır aşağıdaki şemaya sahiptir:

| Sütun           | Tür      |  
|----------------|---------|  
| **key**        | binary  |  
| **value**      | binary  |  
| **topic**      | string  |  
| **partition**  | int     |  
| **offset**     | long    |  
| **timestamp**  | timestamp |  
| **timestampType** | int  |  
| **headers (isteğe bağlı)** | array |

Kafka kaynağı için hem toplu (batch) hem de akış (streaming) sorgularında aşağıdaki seçeneklerin ayarlanması gerekmektedir. 

| Seçenek                     | Değer                         | Anlamı  |  
|-----------------------------|------------------------------|---------|  
| **assign**                  | JSON string `{"topicA":[0,1],"topicB":[2,4]}` | Tüketilecek belirli **TopicPartition**'lar. Kafka kaynağı için yalnızca **"assign"**, **"subscribe"** veya **"subscribePattern"** seçeneklerinden biri belirtilebilir. |  
| **subscribe**               | Virgülle ayrılmış konu listesi | Abone olunacak konu (topic) listesi. Kafka kaynağı için yalnızca **"assign"**, **"subscribe"** veya **"subscribePattern"** seçeneklerinden biri belirtilebilir. |  
| **subscribePattern**        | Java regex string            | Abone olunacak konu(lar) için kullanılan desen. Kafka kaynağı için yalnızca **"assign"**, **"subscribe"** veya **"subscribePattern"** seçeneklerinden biri belirtilebilir. |  
| **kafka.bootstrap.servers** | Virgülle ayrılmış `host:port` listesi | Kafka **"bootstrap.servers"** yapılandırması. |

### Aşağıdaki yapılandırmalar isteğe bağlıdır:

| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **startingTimestamp** | Zaman damgası string (örn. `"1000"`) | Yok (bir sonraki tercih `startingOffsetsByTimestamp`) | Streaming ve Batch | Bir sorgu başlatıldığında, tüm abone olunan bölümler (partitions) için başlangıç zaman damgasını belirten bir string. Aşağıdaki zaman damgası kaydırma seçeneklerine bakınız. Eğer Kafka belirtilen zaman damgasına karşılık gelen offset’i döndürmezse, `startingOffsetsByTimestampStrategy` seçeneğinin değerine göre hareket edilir. |
| **Not 1** | `startingTimestamp`, `startingOffsetsByTimestamp` ve `startingOffsets` seçeneklerine göre önceliklidir. |
| **Not 2** | Streaming sorgular için, bu sadece yeni bir sorgu başlatıldığında geçerlidir. Sorgunun devam ettirilmesi durumunda kaldığı yerden devam eder. Sorgu sırasında yeni keşfedilen bölümler en erken noktadan başlar. |
| **startingOffsetsByTimestamp** | JSON string (örn. `{ "topicA": { "0": 1000, "1": 1000 }, "topicB": { "0": 2000, "1": 2000 } }`) | Yok (bir sonraki tercih `startingOffsets`) | Streaming ve Batch | Bir sorgu başlatıldığında, her bir `TopicPartition` için başlangıç zaman damgasını belirten bir JSON string. Aşağıdaki zaman damgası kaydırma seçeneklerine bakınız. Eğer Kafka belirtilen zaman damgasına karşılık gelen offset’i döndürmezse, `startingOffsetsByTimestampStrategy` seçeneğinin değerine göre hareket edilir. |
| **Not 1** | `startingOffsetsByTimestamp`, `startingOffsets` seçeneğine göre önceliklidir. |
| **Not 2** | Streaming sorgular için, bu sadece yeni bir sorgu başlatıldığında geçerlidir. Sorgunun devam ettirilmesi durumunda kaldığı yerden devam eder. Sorgu sırasında yeni keşfedilen bölümler en erken noktadan başlar. |
| **startingOffsets** | `"earliest"`, `"latest"` (yalnızca streaming için) veya JSON string (örn. `{ "topicA": { "0": 23, "1": -1 }, "topicB": { "0": -2 } }`) | Streaming için `"latest"`, Batch için `"earliest"` | Streaming ve Batch | Bir sorgu başlatıldığında başlangıç noktası: `"earliest"` en erken offset’ten başlar, `"latest"` en son offset’ten başlar veya her `TopicPartition` için başlangıç offset’ini belirten bir JSON string kullanılabilir. JSON içinde `-2` en erken offset’i, `-1` en son offset’i ifade eder. |
| **Not** | Batch sorgular için `"latest"` (dolaylı olarak veya JSON içinde `-1` kullanılarak) izin verilmez. Streaming sorgular için, bu sadece yeni bir sorgu başlatıldığında geçerlidir. Sorgunun devam ettirilmesi durumunda kaldığı yerden devam eder. Sorgu sırasında yeni keşfedilen bölümler en erken noktadan başlar. |
| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **endingTimestamp** | Zaman damgası string (örn. `"1000"`) | Yok (bir sonraki tercih `endingOffsetsByTimestamp`) | Batch sorgu | Bir batch sorgusunun bittiği zamanı belirten bir string. Tüm abone olunan bölümler (partitions) için bitiş zaman damgasını belirten bir JSON string. Aşağıdaki zaman damgası kaydırma seçeneklerine bakınız. Eğer Kafka belirtilen zaman damgasına karşılık gelen offset’i döndürmezse, offset en son (`latest`) olarak ayarlanır. |
| **Not** | `endingTimestamp`, `endingOffsetsByTimestamp` ve `endingOffsets` seçeneklerine göre önceliklidir. |
| **endingOffsetsByTimestamp** | JSON string (örn. `{ "topicA": { "0": 1000, "1": 1000 }, "topicB": { "0": 2000, "1": 2000 } }`) | Yok (bir sonraki tercih `endingOffsets`) | Batch sorgu | Bir batch sorgusunun bittiği noktayı belirten bir JSON string. Her `TopicPartition` için bitiş zaman damgasını belirtir. Aşağıdaki zaman damgası kaydırma seçeneklerine bakınız. Eğer Kafka belirtilen zaman damgasına karşılık gelen offset’i döndürmezse, offset en son (`latest`) olarak ayarlanır. |
| **Not** | `endingOffsetsByTimestamp`, `endingOffsets` seçeneğine göre önceliklidir. |
| **endingOffsets** | `"latest"` veya JSON string (örn. `{ "topicA": { "0": 23, "1": -1 }, "topicB": { "0": -1 } }`) | `"latest"` | Batch sorgu | Bir batch sorgusunun bittiği noktayı belirler. `"latest"` en son offset’i ifade eder. Alternatif olarak her `TopicPartition` için bitiş offset’ini belirten bir JSON string kullanılabilir. JSON içinde `-1`, en son offset’i (`latest`) ifade eder. `-2` (en erken) offset olarak kullanılamaz. |
| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **failOnDataLoss** | `true` veya `false` | `true` | Streaming ve batch | Veri kaybı olasılığı olduğunda (örneğin, topic'ler silindiğinde veya offset'ler aralık dışı kaldığında) sorgunun hata verip vermeyeceğini belirler. Bu, bazen yanlış bir alarm olabilir. Beklediğiniz gibi çalışmadığında bu özelliği devre dışı bırakabilirsiniz. |
| **kafkaConsumer.pollTimeoutMs** | `long` | `120000` (ms) | Streaming ve batch | Executor’ların Kafka’dan veri çekmesi için milisaniye cinsinden zaman aşımı süresi. Belirtilmediğinde, `spark.network.timeout` değerine geri döner. |
| **fetchOffset.numRetries** | `int` | `3` | Streaming ve batch | Kafka offset'lerini alırken pes etmeden önce yapılacak yeniden deneme sayısı. |
| **fetchOffset.retryIntervalMs** | `long` | `10` (ms) | Streaming ve batch | Kafka offset’lerini almayı tekrar denemeden önce beklenmesi gereken süre (milisaniye cinsinden). |
| **maxOffsetsPerTrigger** | `long` | Yok | Streaming sorgu | Her tetikleme aralığında işlenecek maksimum offset sayısına getirilen hız limiti. Belirtilen toplam offset sayısı, farklı hacimlerdeki `topicPartitions` arasında orantılı olarak bölünür. |
| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **minOffsetsPerTrigger** | `long` | Yok | Streaming sorgu | Her tetikleme aralığında işlenecek minimum offset sayısı. Belirtilen toplam offset sayısı, farklı hacimlerdeki `topicPartitions` arasında orantılı olarak bölünür. **Not:** Eğer `maxTriggerDelay` süresi aşılırsa, mevcut offset sayısı `minOffsetsPerTrigger` değerine ulaşmasa bile tetikleme gerçekleşir. |
| **maxTriggerDelay** | Zaman birimiyle birlikte | `15m` (15 dakika) | Streaming sorgu | İki tetikleme arasında, kaynakta veri bulunduğu sürece, tetiklemenin en fazla ne kadar geciktirilebileceğini belirler. Bu seçenek yalnızca `minOffsetsPerTrigger` ayarlanmışsa geçerlidir. |
| **minPartitions** | `int` | Yok | Streaming ve batch | Kafka’dan okunacak minimum bölüm (partition) sayısı. Varsayılan olarak, Spark, Kafka `topicPartitions` ile birebir eşleşen Spark bölümlerine (partitions) sahiptir. Eğer bu değeri `topicPartitions` sayısından büyük bir değere ayarlarsanız, Spark büyük Kafka bölümlerini daha küçük parçalara böler. **Not:** Bu yapılandırma yalnızca bir ipucu (hint) niteliğindedir; Spark görevlerinin sayısı yaklaşık olarak `minPartitions` kadar olur. Ancak, yuvarlama hatalarına veya veri almayan Kafka bölümlerine bağlı olarak bu sayı daha az veya daha fazla olabilir. |
İşte çevirisi:
| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **groupIdPrefix** | `string` | `spark-kafka-source` | Streaming ve batch | Yapılandırılmış akış sorguları tarafından üretilen tüketici grup tanımlayıcılarının (group.id) öneki. Eğer "kafka.group.id" ayarlanmışsa, bu seçenek göz ardı edilecektir. |
| **kafka.group.id** | `string` | Yok | Streaming ve batch | Kafka’dan veri okurken Kafka tüketicisi için kullanılacak Kafka grup id’si. Bu seçeneği dikkatli kullanın. Varsayılan olarak, her sorgu veri okumak için benzersiz bir grup id’si oluşturur. Bu, her Kafka kaynağının, başka bir tüketiciden etkileşim görmeden kendi grup id’sine sahip olmasını sağlar ve bu sayede abonelik yaptığı tüm `topic`lerin bölümlerini (partitions) okuyabilir. Bazı senaryolarda (örneğin, Kafka grup tabanlı yetkilendirme), veri okumak için belirli bir yetkilendirilmiş grup id’si kullanmak isteyebilirsiniz. Grup id’sini isteğe bağlı olarak ayarlayabilirsiniz. Ancak, bunu aşırı dikkatli yapın çünkü beklenmeyen davranışlara yol açabilir. Aynı grup id’sine sahip eşzamanlı çalışan sorgular (hem batch hem de streaming) veya kaynaklar birbirleriyle çakışabilir ve her sorgunun yalnızca verilerin bir kısmını okumasına neden olabilir. Bu durum, sorgular hızlı bir şekilde başlatıldığında veya yeniden başlatıldığında da meydana gelebilir. Bu tür sorunları en aza indirmek için Kafka tüketici oturum zaman aşımını ("kafka.session.timeout.ms" seçeneğini ayarlayarak) çok küçük bir değere ayarlayın. Bu ayar yapıldığında, "groupIdPrefix" seçeneği göz ardı edilecektir. |
| Seçenek | Değer | Varsayılan | Sorgu Türü | Anlamı |
|---------|-------|-----------|------------|--------|
| **includeHeaders** | `boolean` | `false` | Streaming ve batch | Kafka başlıklarının (headers) satırlara dahil edilip edilmeyeceğini belirler. |
| **startingOffsetsByTimestampStrategy** | `"error"` veya `"latest"` | `"error"` | Streaming ve batch | Belirtilen başlangıç zaman damgasına göre (global veya her bir bölüm için) başlangıç ofseti Kafka'nın döndürdüğü ofsetle eşleşmediğinde kullanılacak strateji. İşte strateji adı ve ilgili açıklamalar: |
|         |  |           |            | **"error"**: Sorguyu başarısız kılar ve kullanıcıların manuel adımlar gerektiren geçici çözümlerle ilgilenmesini sağlar. |
|         |  |           |            | **"latest"**: Bu bölümler için en son ofseti atar, böylece Spark daha ileri mikro-batch’lerde bu bölümlerden daha yeni kayıtları okuyabilir. |

