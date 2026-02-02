import pandas as pd
from datetime import datetime, timedelta, timezone

users = ["user_1", "user_2", "user_3"]

rows = []
now = datetime.now(timezone.utc)

for i in range(100):
    rows.append({
        "user_id": users[i % 3],
        "event_timestamp": now - timedelta(minutes=i),
        "tx_count_10m": (i % 20) + 1
    })

df = pd.DataFrame(rows)
df.to_parquet("transactions.parquet", index=False)

print("transactions.parquet created with UTC timestamps!")
