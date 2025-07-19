# src/visualization.py
import mysql.connector
import pandas as pd
import plotly.express as px

def plot_aqi_trends():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sqlrunner_00',
        database='smart_airquality_db'
    )
    query = "SELECT date, location, (pm25 + pm10 + co2 + no2)/4 as aqi FROM air_quality"
    df = pd.read_sql(query, conn)
    df['date'] = pd.to_datetime(df['date'])

    fig = px.line(df, x='date', y='aqi', color='location', title='Air Quality Index Trend')
    fig.show()
    conn.close()

if __name__ == "__main__":
    plot_aqi_trends()


# import mysql.connector
# import pandas as pd
# import plotly.express as px

# def plot_aqi_trends():
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='Sqlrunner_00',
#         database='air_quality_db'
#     )

#     query = """
#     SELECT date, location, (pm25 + pm10 + co2 + no2)/4 AS aqi FROM air_quality
#     """
#     df = pd.read_sql(query, conn)

#     # ✅ Convert date column to datetime
#     df['date'] = pd.to_datetime(df['date'])

#     # ✅ Optional: round to nearest minute (or hour, if data is dense)
#     df['date'] = df['date'].dt.floor('min')  # or 'H' for hour

#     # ✅ Optional: group and average AQI for each time/location
#     df = df.groupby(['date', 'location'])['aqi'].mean().reset_index()

#     # ✅ Plot the cleaned data
#     fig = px.line(df, x='date', y='aqi', color='location', title='Air Quality Index Trend')
#     fig.show()

#     conn.close()

# if __name__ == "__main__":
#     plot_aqi_trends()
