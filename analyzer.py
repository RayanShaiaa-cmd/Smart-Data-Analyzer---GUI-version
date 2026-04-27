import dotenv as env
import os
from datetime import datetime
from DateValidator import get_valid_date
import requests as req
import pandas as pd


#for download the privates variables
env.load_dotenv()

API_key = os.environ.get("API_KEY", "No API_KEY")
city = input("Enter the city to shos its status : ")

start_date = get_valid_date("Enter The start date : ")
end_date = get_valid_date("Enter the end date : ")

if start_date > end_date:
    print("The start and end date has been exchange")
    start_date, end_date = end_date, start_date

params = {"q": city, "appid": API_key, "start_date": start_date, "end_date": end_date}

URL = "https://api.openweathermap.org/data/2.5/weather"

session = req.Session()

response = session.get(URL, params=params)
data = response.json()

record = {
    "city": data.get("name", "unknown"),
    "temp": data.get("main", "unknown").get("temp"),
    "temp min": data.get("main", "unknown").get("temp_min"),
    "temp max": data.get("main", "unknown").get("temp_max"),
    "wind speed": data.get("wind", "unknown").get("speed"),
    "humidity": data.get("main", "unknown").get("humidity"),
    "describtion": data.get("weather", "unknown")[0].get("description"),
    "sea level": data.get("main", "unknown").get("sea_level"),
    "pressure": data.get("main", "unknown").get("pressure"),
    "date": datetime.strftime(datetime.now(), "%Y-%m-%d"),
}

df = pd.DataFrame([record])
