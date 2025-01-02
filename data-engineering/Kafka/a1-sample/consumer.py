from kafka import KafkaConsumer
import json

# Kafka consumer'ı başlatıyoruz
consumer = KafkaConsumer(
    'time-topic',  # Hangi topic'ten veri alacağız
    bootstrap_servers='localhost:9092',  # Kafka broker adresi
    group_id='time-consumer-group',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # JSON verisini deserialize ediyoruz
)

for message in consumer:
    print(f"Received: {message.value['time']}")
