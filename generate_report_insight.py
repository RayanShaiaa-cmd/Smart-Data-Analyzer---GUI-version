import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

features = [
    "temp",
    "temp min",
    "temp max",
    "wind speed",
    "humidity",
    "pressure",
    "sea level",
]


def generate_report(df):
    data = df.iloc[0]
    print("🌏 WEATHER REPORT")
    print("-" * 20)
    print(f"City : {data['city']}")
    print(f"Date : {data['date']}")
    print(f"Temperature : {data['temp']}")
    print(f"Min temp : {data['temp min']}")
    print(f"Max temp : {data['temp max']}")
    print(f"Humidity : {data['humidity']}")
    print(f"Wind Speed : {data['wind speed']}")
    print(f"Pressure : {float(data['pressure'])}")
    print(f"Weather : {data['describtion']}")

    values = [data[f] for f in features]

    # For Normalization
    values[5] = values[5] / 10
    values[6] = values[5] / 10

    # Visualization
    plt.figure(figsize=(10, 7))
    plt.bar(features, values)
    plt.title(f"Weather Report - {data['city']} {data['date']}")
    plt.xticks(rotation=45)
    plt.ylabel("Values")
    plt.show()

    angles = np.linspace(0, 2 * np.pi, len(features), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    plt.polar(angles, values)
    plt.fill(angles, values, alpha=0.3)
    plt.xticks(angles[:-1], features)
    plt.title("Weather Radar Chart")
    plt.show()


def generate_report_previous_data(data):
    data["date"] = pd.to_datetime(data["date"])
    data = data.sort_values("date")

    plt.figure(figsize=(10, 5))
    plt.plot(data["date"], data["temp"], marker="o")

    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(data["date"], data["humidity"], label="Humidity")
    plt.plot(data["date"], data["wind speed"], label="Wind Speed")
    plt.xlabel("Date")
    plt.title("Humidity & Wind Speed Trends")
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(data["date"].astype(str), data["temp"])
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.title("Temperature Comparison By Day")
    plt.show()

    print(data[["temp", "humidity", "wind speed"]].corr())
    print(f"Max Temp : {data['temp max'].max()}")
    print(f"Min Temp : {data['temp min'].min()}")
    print(f"Average Temperature : {data['temp'].mean()}")

def generate_future_report(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["max_temperature"], label="Max Temperature")
    plt.plot(df["time"], df["min_temperature"], label="Min Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Max and Min Temperatures")
    plt.legend()
    plt.savefig("Daily Max and Min Temperatures.png")
    plt.show()