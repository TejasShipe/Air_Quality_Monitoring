# src/forecasting.py
import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',  # Replace with your actual password
        database='air_quality_db'
    )
    query = "SELECT pm25, pm10, co2, no2, (pm25 + pm10 + co2 + no2)/4 as aqi FROM air_quality"
    df = pd.read_sql(query, conn)
    conn.close()

    # Split into features and target
    X = df[['pm25', 'pm10', 'co2', 'no2']]
    y = df['aqi']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def predict_aqi(pm25, pm10, co2, no2):
    model = train_model()
    prediction = model.predict([[pm25, pm10, co2, no2]])
    return round(prediction[0], 2)

if __name__ == "__main__":
    # Example prediction
    predicted_aqi = predict_aqi(90, 120, 85, 80)
    print(f"🔮 Predicted AQI: {predicted_aqi}")
