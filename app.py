import streamlit as st
from datetime import datetime, timedelta

from services.weather_api import get_current_weather, get_forecast
from services.data_handler import save_weather_data, load_city_data
from services.reports import (
    show_today_report,
    show_day_report,
    show_history_report,
    show_forecast_report
)

st.set_page_config(page_title="Weather AI Dashboard", layout="wide")

st.title("🌤 Weather AI Dashboard")

city = st.text_input("Enter City", "Sana'a")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Today's Report",
        "Specific Day",
        "History Analysis",
        "Forecast"
    ]
)

# ---------------- SAVE BUTTON ----------------
if st.button("💾 Save Today's Data"):
    data = get_current_weather(city)
    save_weather_data(city, data)
    st.success("Weather data saved successfully!")

# ---------------- MENU ----------------
df = load_city_data(city)

if menu == "Today's Report":
    show_today_report(df, city)

elif menu == "Specific Day":
    date = st.date_input("Select Date")
    show_day_report(df, str(date))

elif menu == "History Analysis":
    show_history_report(df)

elif menu == "Forecast":
    lat = st.number_input("Latitude", value=48.85)
    lon = st.number_input("Longitude", value=2.35)

    forecast = get_forecast(lat, lon)
    show_forecast_report(forecast)