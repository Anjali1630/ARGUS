import pandas as pd
import numpy as np

def detect_drift(log_file="shadow_log.csv"):
    df = pd.read_csv(log_file, header=None)
    df.columns = ["time", "user_id", "tx_count", "v1_pred", "v2_pred"]

    recent_tx = df["tx_count"].tail(50)
    historical_tx = df["tx_count"].head(50)

    recent_mean = recent_tx.mean()
    historical_mean = historical_tx.mean()

    drift_score = abs(recent_mean - historical_mean)

    if drift_score > 5:
        return True, drift_score
    else:
        return False, drift_score
