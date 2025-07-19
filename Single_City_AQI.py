from datetime import datetime, timedelta
from src.api_fetcher import get_realtime_aqi
from src.insert_to_db import insert_data
import random

city = "Bhiwandi"  # 🔁 Change city if needed

print(f"📊 Simulating AQI data with variations for {city} (Last 30 days)...")

# Fetch base data from API once
base_data = get_realtime_aqi(city)

if not isinstance(base_data, dict):
    print("❌ Failed to fetch AQI data:", base_data)
    exit()

# Helper to add realistic random variation
def vary(value, percent=10):
    variation = value * (percent / 100)
    return round(random.uniform(value - variation, value + variation), 2)

# Insert varied data for last 30 days
for i in range(30):
    date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
    
    record = {
        "date": date,
        "location": city,
        "pm25": vary(base_data["pm2_5"], 15),
        "pm10": vary(base_data["pm10"], 15),
        "co2": vary(base_data["co"], 10),
        "no2": vary(base_data["no2"], 10)
    }
    
    insert_data(record)
    print(f"✅ Inserted data for {date}: PM2.5={record['pm25']}, PM10={record['pm10']}")
