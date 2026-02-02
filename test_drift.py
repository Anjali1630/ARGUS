from drift_detector import detect_drift

drift, score = detect_drift()

print("Drift Detected:", drift)
print("Drift Score:", score)
