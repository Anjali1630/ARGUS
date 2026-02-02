import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import pickle

np.random.seed(100)

data = pd.DataFrame({
    "amount": np.random.randint(10, 100000, 1000),
    "tx_count_10m": np.random.randint(1, 50, 1000),
    "avg_amount_24h": np.random.randint(100, 50000, 1000),
    "is_fraud": np.random.choice([0, 1], size=1000, p=[0.85, 0.15])
})

X = data[["amount", "tx_count_10m", "avg_amount_24h"]]
y = data["is_fraud"]

model = XGBClassifier(max_depth=5, n_estimators=200)
model.fit(X, y)

with open("model_v2.pkl", "wb") as f:
    pickle.dump(model, f)

print("Shadow model V2 saved successfully")
