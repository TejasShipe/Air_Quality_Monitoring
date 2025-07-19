# src/user_input.py
def get_user_data():
    print("🔵 Enter today's air quality details:")
    location = input("Location: ")
    date = input("Date (YYYY-MM-DD): ")
    pm25 = float(input("PM2.5 level: "))
    pm10 = float(input("PM10 level: "))
    co2 = float(input("CO2 level: "))
    no2 = float(input("NO2 level: "))
    complaint = input("Any complaints/comments about air today? ")

    return {
        'location': location,
        'date': date,
        'pm25': pm25,
        'pm10': pm10,
        'co2': co2,
        'no2': no2,
        'complaint': complaint
    }
