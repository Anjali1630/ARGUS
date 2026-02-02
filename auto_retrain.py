from drift_detector import detect_drift
import subprocess

drift, score = detect_drift()

if drift:
    print(" Drift detected! Score:", score)
    print("Triggering retraining...")

    subprocess.run(["python", "train_model_v2.py"])

    print(" New model trained and saved (model_v2.pkl)")
else:
    print(" No drift. Model is still valid.")
