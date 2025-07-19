import requests

API_KEY = "c8e802fe93289ff61c5701f74168a6dd"  # Replace with your real API key

def get_realtime_aqi(city):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_resp = requests.get(geo_url).json()

    if not geo_resp or len(geo_resp) == 0:
        return f"❌ City '{city}' not found or API limit reached"

    try:
        lat = geo_resp[0]['lat']
        lon = geo_resp[0]['lon']
    except (KeyError, IndexError):
        return f"❌ Invalid location data received for '{city}'"

    aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(aqi_url)
    data = response.json()

    if "list" not in data:
        return "❌ AQI data not found in API response"

    components = data['list'][0]['components']
    aqi = data['list'][0]['main']['aqi']  # AQI scale (1-5)

    result = {
        "pm2_5": components["pm2_5"],
        "pm10": components["pm10"],
        "co": components["co"],
        "no2": components["no2"],
        "aqi_index": aqi
    }

    return result
