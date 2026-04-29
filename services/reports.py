import streamlit as st
import pandas as pd
import plotly.express as px


def show_today_report(df, city):
    if df.empty:
        st.warning("No data available")
        return

    today = df.iloc[-1]

    st.subheader(f"🌍 Weather Today - {city}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", today["temp"])
    col2.metric("Humidity", today["humidity"])
    col3.metric("Wind Speed", today["wind speed"])

    fig = px.bar(
        x=["Temp", "Min", "Max"],
        y=[today["temp"], today["temp min"], today["temp max"]],
        title="Temperature Overview"
    )
    st.plotly_chart(fig)


def show_day_report(df, date):
    data = df[df["date"] == date]

    if data.empty:
        st.warning("No data for this date")
        return

    st.dataframe(data)


def show_history_report(df):
    if df.empty:
        st.warning("No data available")
        return

    df["date"] = pd.to_datetime(df["date"])

    fig = px.line(df, x="date", y="temp", title="Temperature Over Time")
    st.plotly_chart(fig)

    fig2 = px.line(df, x="date", y="humidity", title="Humidity Trend")
    st.plotly_chart(fig2)


def show_forecast_report(data):
    st.subheader("📈 Forecast")

    df = pd.DataFrame({
        "date": data["time"],
        "max": data["temperature_2m_max"],
        "min": data["temperature_2m_min"]
    })

    fig = px.line(df, x="date", y=["max", "min"])
    st.plotly_chart(fig)