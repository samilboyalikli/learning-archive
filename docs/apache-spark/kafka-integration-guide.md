# "Structured Streaming + Kafka Entegrasyon Kılavuzu (Kafka broker sürümü 0.10.0 veya daha yeni)"

Kafka'dan veri okumak ve Kafka'ya veri yazmak için Structured Streaming entegrasyonu.  

### Bağlantı (Linking)  

Scala/Java uygulamaları için, eğer SBT/Maven proje tanımları kullanıyorsanız, uygulamanızı aşağıdaki bileşenle bağlayın:  

```
groupId = org.apache.spark
artifactId = spark-sql-kafka-0-10_2.12
version = 3.5.4
```

Lütfen unutmayın: Kafka mesaj başlıkları (headers) özelliğini kullanmak istiyorsanız, Kafka istemci (client) sürümünüzün en az **0.11.0.0** veya daha yeni bir sürüm olması gerekmektedir.  

Python uygulamaları için, uygulamanızı dağıtırken yukarıda belirtilen kütüphaneyi ve bağımlılıklarını eklemeniz gerekir. Bununla ilgili detaylar için aşağıdaki **Dağıtım (Deploying)** bölümüne bakabilirsiniz.  

`spark-shell` üzerinde denemeler yapmak için, `spark-shell`'i başlatırken yukarıda belirtilen kütüphaneyi ve bağımlılıklarını eklemeniz gerekir. Ayrıca, daha fazla bilgi için **Dağıtım (Deploying)** bölümüne göz atabilirsiniz.