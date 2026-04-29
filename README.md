# 🌦️ Weather AI Dashboard (Streamlit)

## 📌 Overview

A modern **Python-based Weather Analytics Dashboard** built with Streamlit that collects, stores, analyzes, and visualizes weather data for any city.

The system integrates real-time APIs and provides an **interactive web interface** for exploring current, historical, and forecasted weather insights.

---

## 🚀 Key Features

### 🌍 Real-Time Weather Monitoring

* Current temperature (min / max)
* Humidity, wind speed, pressure
* Weather description
* One-click data saving

---

### 📊 Historical Data Analytics

* Time-series analysis:

  * Temperature trends
  * Humidity trends
  * Wind speed trends
* Correlation analysis between features
* Interactive visualizations using Plotly

---

### 📈 Forecast Visualization

* Integrated with Open-Meteo API
* Displays:

  * Daily max temperature
  * Daily min temperature
* Clean interactive line charts

---

### 💾 Data Persistence

* Stores data per city in CSV format
* Prevents duplicate entries
* Enables long-term tracking

---

### 🖥️ Interactive Web Interface

* Built with Streamlit
* Sidebar navigation
* Dynamic dashboard updates
* No command-line interaction required

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** – UI dashboard
* **pandas** – data processing
* **plotly** – interactive visualization
* **requests** – API integration
* **python-dotenv** – environment variables

**APIs:**

* OpenWeatherMap (real-time data)
* Open-Meteo (forecast data)

---

## 📂 Project Structure

```id="1aqhcc"
weather-ai-dashboard/
│
├── app.py
│
├── services/
│   ├── weather_api.py
│   ├── data_handler.py
│   └── reports.py
│
├── data/
├── requirements.txt
├── .env.example
├── README.md
```

---

## ⚙️ Installation

```bash id="8b8q5r"
git clone https://github.com/RayanShaiaa-cmd/Smart-Data-Analyzer---GUI-version.git
cd Smart-Data-Analyzer---GUI-version
pip install -r requirements.txt
```

---
## 🔑 Environment Setup

Create a `.env` file:

```bash
API_KEY=your_openweathermap_api_key
```

### 🔐 How to get your API Key

1. Go to **https://openweathermap.org/**
2. Create a free account (Sign Up)
3. After logging in, enter Your name in a navigation bar
4. Enter My API Keys
5. Enter generate api key
5. Copy the key which you created it and paste it into your `.env` file

> ⏱️ Note: The API key may take a few minutes to activate after creation.

---

## ▶️ Run the Application

```bash id="vszkq9"
```
at the terminal inside the folder of the program

---

## 📊 Dashboard Modules

### 1. Today’s Report

* Live weather metrics
* Quick visual summary

### 2. Historical Search

* Retrieve weather data by date
* Structured table display

### 3. Analytics Dashboard

* Temperature trends
* Humidity & wind comparisons
* Statistical insights

### 4. Forecast Analysis

* Future temperature trends
* Interactive line charts

---

## ⚠️ Limitations

* Uses CSV instead of a database
* Requires valid API key
* Basic error handling for API failures

---

## 🔧 Future Improvements

* Integrate Machine Learning forecasting
* Replace CSV with PostgreSQL
* Deploy to Streamlit Cloud
* Add authentication system
* Multi-city comparison dashboard

---

## 👨‍💻 Author

**Rayan Shaiaa**
AI & Data Science Student

---

## ⭐ Project Value

This project demonstrates:

* API integration in real-world applications
* Data processing and storage design
* Interactive dashboard development
* Time-series data analysis
* Clean modular architecture

---