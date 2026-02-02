import csv
from datetime import datetime

def log_prediction(user_id, tx_count, v1, v2):
    with open("shadow_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), user_id, tx_count, v1, v2])
