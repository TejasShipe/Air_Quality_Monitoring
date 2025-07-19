# src/forecasting.py
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Dummy training function (replace with real model & dataset)
def train_model():
    # Simulated data: [PM2.5, PM10, CO2, NO2]
    X = np.array([
        [50, 80, 400, 30],
        [80, 120, 420, 40],
        [100, 160, 450, 50],
        [130, 200, 480, 60]
    ])
    y = np.array([90, 120, 160, 200])  # Simulated AQI

    model = LinearRegression()
    model.fit(X, y)

    # Save model
    joblib.dump(model, 'src/aqi_model.pkl')
    print("✅ AQI prediction model trained and saved.")

def predict_aqi(pm25, pm10, co2, no2):
    model = joblib.load('src/aqi_model.pkl')
    input_features = np.array([[pm25, pm10, co2, no2]])
    predicted_aqi = model.predict(input_features)
    return round(predicted_aqi[0], 2)
