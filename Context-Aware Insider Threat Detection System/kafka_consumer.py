from kafka import KafkaConsumer
import json

# Kafka consumer
consumer = KafkaConsumer('user_activity',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Process messages in real-time
for message in consumer:
    activity = message.value
    print(f"Received: {activity}")