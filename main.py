# =========================
# IMPORT LIBRARIES
# =========================
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from sklearn.model_selection import train_test_split

# =========================
# IMPORT CUSTOM FUNCTIONS
# =========================
from src.data_loader import load_data
from src.preprocessing import clean_data, select_features
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import predict
from src.utils import save_model, save_report

# =========================
# AUTO CREATE FOLDERS
# =========================
os.makedirs("outputs/graphs", exist_ok=True)
os.makedirs("outputs/models", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

# =========================
# LOAD DATA
# =========================
df = load_data("data/raw/global air pollution dataset.csv")

# CLEAN DATA
df = clean_data(df)

# =========================
# STATIC GRAPH
# =========================
def save_histogram(df):
    df.hist(figsize=(10, 8))
    plt.title("Feature Distribution")
    plt.savefig("outputs/graphs/histogram.png")
    plt.close()

save_histogram(df)

# =========================
# ANIMATED GRAPH 1 - CO AQI
# =========================
def animated_co_aqi(df):
    fig, ax = plt.subplots()
    x, y = [], []

    def update(frame):
        if frame < len(df):
            x.append(frame)
            y.append(df['CO AQI Value'].iloc[frame])

            ax.clear()
            ax.plot(x, y)
            ax.set_title("CO AQI Animated Trend")
            ax.set_xlabel("Index")
            ax.set_ylabel("CO AQI Value")

    ani = animation.FuncAnimation(fig, update, frames=50)
    ani.save("outputs/graphs/co_aqi_animation.gif", writer="pillow")
    plt.close()

animated_co_aqi(df)

# =========================
# ANIMATED GRAPH 2 - PM2.5
# =========================
def animated_pm25(df):
    fig, ax = plt.subplots()
    x, y = [], []

    def update(frame):
        if frame < len(df):
            x.append(frame)
            y.append(df['PM2.5 AQI Value'].iloc[frame])

            ax.clear()
            ax.plot(x, y, color='red')
            ax.set_title("PM2.5 Animated Trend")
            ax.set_xlabel("Index")
            ax.set_ylabel("PM2.5 AQI Value")

    ani = animation.FuncAnimation(fig, update, frames=50)
    ani.save("outputs/graphs/pm25_animation.gif", writer="pillow")
    plt.close()

animated_pm25(df)

# =========================
# FEATURES
# =========================
X, y = select_features(df)

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TRAIN MODEL
# =========================
model = train_model(X_train, y_train)

# =========================
# EVALUATE MODEL
# =========================
accuracy = evaluate_model(model, X_test, y_test)
print("Model Accuracy:", accuracy)

# =========================
# SAVE REPORT
# =========================
save_report(
    f"Model Accuracy: {accuracy}",
    "outputs/reports/report.txt"
)

# =========================
# SAVE MODEL
# =========================
save_model(model, "outputs/models/air_pollution_model.pkl")

# =========================
# PREDICTION
# =========================
new_data = pd.DataFrame({
    'CO AQI Value': [25],
    'Ozone AQI Value': [30],
    'NO2 AQI Value': [15],
    'PM2.5 AQI Value': [40]
})

result = predict(model, new_data)
print("Predicted AQI Category:", result[0])

print("Training Complete")