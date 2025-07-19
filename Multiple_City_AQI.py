from datetime import datetime, timedelta
from src.api_fetcher import get_realtime_aqi
from src.insert_to_db import insert_data
import random

cities = ["Bhiwandi","Kalyan","Mumbai","Thane","Delhi","Ahmedabad","Rajasthan","Assam","Chennai","Bangalore"] # Add/remove cities as needed

def vary(value, percent=10):
    variation = value * (percent / 100)
    return round(random.uniform(value - variation, value + variation), 2)

for city in cities:
    print(f"🌍 Fetching base AQI data for {city}...")
    base_data = get_realtime_aqi(city)

    if not isinstance(base_data, dict):
        print(f"❌ Skipping {city} due to error: {base_data}")
        continue

    print(f"📊 Inserting 30 days of varied AQI data for {city}...")
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
        print(f"✅ Inserted {city} - {date}: PM2.5={record['pm25']}, PM10={record['pm10']}")
