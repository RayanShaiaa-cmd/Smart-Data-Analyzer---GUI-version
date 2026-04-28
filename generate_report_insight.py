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
    values[5] = values[5]/10
    values[6] = values[5]/10

    # Visualization
    plt.figure(figsize=(10, 7))
    plt.bar(features, values)
    plt.title(f"Weather Report - {data['city']} {data['date']}")
    plt.xticks(rotation=45)
    plt.ylabel("Values")
    plt.show()

    angles = np.linspace(0, 2*np.pi, len(features), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    plt.polar(angles, values)
    plt.fill(angles, values, alpha=0.3)
    plt.xticks(angles[:-1], features)
    plt.title("Weather Radar Chart")
    plt.show()