import joblib

# SAVE MODEL
def save_model(model, path):
    joblib.dump(model, path)
    print("Model Saved")

# SAVE REPORT
def save_report(text, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
    print("Report Saved")