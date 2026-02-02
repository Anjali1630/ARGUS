import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

np.random.seed(42)

data = pd.DataFrame({
    "amount": np.random.randint(10, 100000, 1000),
    "tx_count_10min": np.random.randint(1, 50, 1000),
    "avg_amount_24h": np.random.randint(100, 50000, 1000),
    "is_fraud": np.random.choice([0, 1], size=1000, p=[0.9, 0.1])
})

X = data[["amount", "tx_count_10min", "avg_amount_24h"]]
y = data["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as fraud_model.pkl")
