from kafka import KafkaProducer
import time
import json

# Kafka producer'ı başlatıyoruz
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker adresi
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Veriyi JSON formatına serileştiriyoruz
)

while True:
    # Mevcut zamanı alıyoruz
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    
    # Kafka topic'ine gönderiyoruz
    producer.send('time-topic', {'time': current_time})
    print(f"Sent: {current_time}")
    
    # 1 saniye bekliyoruz
    time.sleep(1)
