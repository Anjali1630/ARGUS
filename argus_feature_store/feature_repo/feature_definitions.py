from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64

user = Entity(
    name="user_id",
    join_keys=["user_id"]
)

transactions_source = FileSource(
    path="data/transactions.parquet",
    event_timestamp_column="event_timestamp",
)

user_tx_features = FeatureView(
    name="user_tx_features",
    entities=[user],
    ttl=timedelta(minutes=10),
    schema=[
        Field(name="tx_count_10m", dtype=Int64),
    ],
    online=True,
    source=transactions_source,
)
