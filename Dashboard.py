import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from datetime import datetime

# ---------- DB Connection ----------
def fetch_data(city=None):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sqlrunner_00',  # Change this
        database='smart_airquality_db'
    )
    query = "SELECT * FROM air_quality"
    if city:
        query += f" WHERE location = '{city}'"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ---------- AQI Level Helper ----------
def get_aqi_level(aqi):
    if aqi <= 50:
        return "🟢 Good"
    elif aqi <= 100:
        return "🟡 Moderate"
    elif aqi <= 150:
        return "🟠 Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "🔴 Unhealthy"
    elif aqi <= 300:
        return "🟣 Very Unhealthy"
    else:
        return "🟥 Hazardous"

# ---------- UI ----------
st.set_page_config(page_title="AQI Dashboard", layout="wide")
st.title("🌍 Air Quality Monitoring Dashboard")

# ---------- Sidebar Filters ----------
df_all = fetch_data()
cities = df_all["location"].unique().tolist()
selected_city = st.sidebar.selectbox("Select City", cities)

df = fetch_data(selected_city)
df['date'] = pd.to_datetime(df['date'])

# ---------- AQI Calculation ----------
df["aqi"] = df[["pm25", "pm10", "co2", "no2"]].mean(axis=1)
latest_row = df.sort_values("date", ascending=False).iloc[0]
current_aqi = round(latest_row["aqi"], 2)
aqi_level = get_aqi_level(current_aqi)

# ---------- Display AQI Box ----------
st.metric(f"📍 Current AQI in {selected_city}", f"{current_aqi}", help=aqi_level)

st.markdown(f"**Air Quality Status**: {aqi_level}")

# ---------- Line Chart ----------
st.subheader("📈 AQI Over Time")
fig = px.line(df, x='date', y='aqi', title='AQI Trend', markers=True)
st.plotly_chart(fig, use_container_width=True)

# ---------- Bar Chart of Pollutants ----------
st.subheader("🔬 Latest Pollutant Levels")
pollutants = {
    "PM2.5": latest_row["pm25"],
    "PM10": latest_row["pm10"],
    "CO₂": latest_row["co2"],
    "NO₂": latest_row["no2"],
}
pollutant_df = pd.DataFrame(pollutants.items(), columns=["Pollutant", "Level"])
fig_bar = px.bar(pollutant_df, x="Pollutant", y="Level", color="Pollutant", title="Current Pollutant Levels")
st.plotly_chart(fig_bar, use_container_width=True)

# ---------- Raw Data ----------
with st.expander("📄 View Raw Data"):
    st.dataframe(df.sort_values("date", ascending=False))
