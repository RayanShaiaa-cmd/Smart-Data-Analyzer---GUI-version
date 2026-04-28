import dotenv as env
import os
from datetime import datetime, timedelta
from DateValidator import get_valid_date
import requests as req
import pandas as pd
import generate_report_insight as gri
import matplotlib.pyplot as plt


# for download the privates variables
env.load_dotenv()

API_key = os.environ.get("API_KEY", "No API_KEY")
city = input("Enter the city to know its status : ")


# Handling Files
if not os.path.exists("data"):
    os.mkdir("data")
    print('Create Folder "data" for storing weather`s data')

data = pd.read_csv(f"data/{city}.csv")


# UI Layer
while True:
    print("Choose a number from these option :")
    print(
        f"--------------{city}------------- \n"
        "1.Display information of this day \n"
        "2.Display information of specefic day \n"
        "3.Display information of previous days \n"
        "4.Display prediction information for future days \n"
        "5.Save today`s information for this country \n"
        "6.Exit"
    )

    choice = input("Enter : ").strip()

    if choice == "1":
        current_date = datetime.strftime(datetime.now(), "%Y-%m-%d")

        result = data[data["date"] == current_date]

        if result.empty:
            print("Please, save the data first.")
        else:
            gri.generate_report(result)

    elif choice == "2":
        user_date = input("Enter date by format (yyyy-mm-dd) : ")

        result = data[data["date"] == user_date]

        if result.empty:
            print(f"Please, we don`t find the data of {user_date}")
        else:
            gri.generate_report(result)

    elif choice == "3":
        gri.generate_report_previous_data(data)

    elif choice == "4":
        # APIs Codes
        latitude = float(input("Enter latitude : "))  # 48.85
        longitude = float(input("Enter longitude : "))  # 2.35

        today = datetime.now()
        week_ago = today - timedelta(days=7)

        start_date = week_ago.strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"

        response = req.get(url)

        data = response.json()
        daily_data = data["daily"]

        # ---------------------------------------------
        # Analitics code

        df = pd.DataFrame(
            {
                "time": daily_data["time"],
                "max_temperature": daily_data["temperature_2m_max"],
                "min_temperature": daily_data["temperature_2m_min"],
            }
        )

        df["time"] = pd.to_datetime(df["time"])

        gri.generate_future_report(df)

    elif choice == "5":
        # To make APIs connection
        params = {"q": city, "appid": API_key, "units": "metric"}

        URL = "https://api.openweathermap.org/data/2.5/weather"

        session = req.Session()

        response = session.get(URL, params=params, timeout=5)
        data = response.json()

        session.close()

        # for Handling Nulls and repear information in correct format
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

        if os.path.exists(f"data/{city}.csv"):
            data = pd.read_csv(f"data/{city}.csv")
            if df["date"].values[0] in data["date"].values:
                print("the weather`s information of this date is already exists !!")
            else:
                df.to_csv(f"data/{city}.csv", header=False, mode="a")
                print("Done, Added today`s information succusfully")
        else:
            df.to_csv(f"data/{city}.csv")
            print("Done, Create weather.csv file and added first row")

    elif choice == "6":
        print("program is exiting ...")
        break

    else:
        print("Invalid input, please enter from one of these option !!")
