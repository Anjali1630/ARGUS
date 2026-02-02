from fastapi import FastAPI
import pickle
import numpy as np
from feast import FeatureStore
from shadow_logger import log_prediction
from kafka_producer import send_to_kafka   # NEW

app = FastAPI()
store = FeatureStore(repo_path="argus_feature_store/feature_repo")

with open("model_v1.pkl", "rb") as f:
    model_v1 = pickle.load(f)

with open("model_v2.pkl", "rb") as f:
    model_v2 = pickle.load(f)

@app.get("/")
def home():
    return {"message": "ARGUS running in Shadow Mode 👁️"}

@app.post("/predict")
def predict(user_id: str, amount: int):
    features = store.get_online_features(
        features=["user_tx_features:tx_count_10m"],
        entity_rows=[{"user_id": user_id}]
    ).to_dict()

    tx_count_10m = features["tx_count_10m"][0]
    avg_amount_24h = amount

    data = np.array([[amount, tx_count_10m, avg_amount_24h]])

    pred_v1 = int(model_v1.predict(data)[0])
    pred_v2 = int(model_v2.predict(data)[0])

    # Shadow CSV logging
    log_prediction(user_id, tx_count_10m, pred_v1, pred_v2)

    # Kafka streaming (NEW)
    event = {
        "user_id": user_id,
        "tx_count_10m": tx_count_10m,
        "champion_v1": pred_v1,
        "shadow_v2": pred_v2
    }
    send_to_kafka(event)

    return event
