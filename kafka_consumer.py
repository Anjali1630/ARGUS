from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "argus-transactions",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening to ARGUS stream...")

for message in consumer:
    print("Received:", message.value)
