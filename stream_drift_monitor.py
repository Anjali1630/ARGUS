from kafka import KafkaConsumer
import json
from collections import deque
from drift_detector import detect_drift
import subprocess

consumer = KafkaConsumer(
    "argus-transactions",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("ARGUS Drift Monitor is watching the stream... 👁️")

buffer = deque(maxlen=100)

for message in consumer:
    event = message.value
    buffer.append(event["tx_count_10m"])
    print("Stream:", event)

    if len(buffer) == 100:
        drift, score = detect_drift()
        print("Drift check:", drift, "Score:", score)

        if drift:
            print(" DRIFT DETECTED! Retraining model...")
            subprocess.run(["python", "auto_retrain.py"])
