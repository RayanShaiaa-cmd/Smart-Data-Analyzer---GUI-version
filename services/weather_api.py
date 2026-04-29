import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_current_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    res = requests.get(url, params=params)
    data = res.json()

    return {
        "city": data.get("name", "unknown"),
        "temp": data["main"]["temp"],
        "temp min": data["main"]["temp_min"],
        "temp max": data["main"]["temp_max"],
        "wind speed": data["wind"]["speed"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "pressure": data["main"]["pressure"],
        "sea level": data["main"].get("sea_level", 0),
        "date": datetime.now().strftime("%Y-%m-%d")
    }


def get_forecast(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto"
    }

    res = requests.get(url, params=params)
    data = res.json()["daily"]

    return data