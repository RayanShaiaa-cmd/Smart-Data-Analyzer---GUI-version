import os
import pandas as pd


def save_weather_data(city, record):
    if not os.path.exists("data"):
        os.mkdir("data")

    file_path = f"data/{city}.csv"
    df = pd.DataFrame([record])

    if os.path.exists(file_path):
        existing = pd.read_csv(file_path)

        if record["date"] in existing["date"].values:
            return

        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)


def load_city_data(city):
    file_path = f"data/{city}.csv"

    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    return pd.DataFrame()