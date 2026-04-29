# 🌦️ Weather AI Dashboard (Streamlit)

## 📌 Overview

This project is a **modern Python + Streamlit Weather Analytics System** that collects, stores, analyzes, and visualizes weather data for any city.

It integrates real-time APIs and provides a full interactive dashboard instead of a CLI system.

It supports:

* Real-time weather tracking
* Historical weather analysis
* Interactive dashboards
* Forecast visualization
* CSV-based data persistence

---

## 🚀 Features

### 1. 🌍 Live Weather Dashboard

* Displays real-time weather data:
  * Temperature (current / min / max)
  * Humidity
  * Wind speed
  * Pressure
  * Weather description
* One-click **Save Weather Data**

---

### 2. 📊 Historical Data Analysis

* Time-series visualization of:
  * Temperature trends
  * Humidity trends
  * Wind speed trends
* Correlation analysis between weather features
* Clean interactive charts using Plotly

---

### 3. 📈 Forecast Visualization

* Uses Open-Meteo API
* Displays:
  * Max temperature trend
  * Min temperature trend
* Interactive line charts

---

### 4. 💾 Data Persistence System

* Stores weather data in CSV files per city
* Prevents duplicate daily entries
* Enables long-term historical tracking

---

### 5. 🖥️ Streamlit Web Interface

* Sidebar navigation system
* Simple city input system
* Real-time dashboard updates
* No terminal usage required

---

## 🧠 Tech Stack

* Python
* Streamlit → UI Dashboard
* pandas → Data processing
* plotly → Visualization
* requests → API calls
* python-dotenv → Environment variables
* OpenWeatherMap API → Live weather
* Open-Meteo API → Forecast data

---

## 📂 Project Structure

weather-ai-dashboard/
│
├── app.py # Streamlit main application
│
├── services/
│ ├── weather_api.py # API integration layer
│ ├── data_handler.py # CSV data storage system
│ └── reports.py # Visualization & analytics
│
├── data/
│ └── (city CSV files)
│
├── requirements.txt
├── .env
├── README.md


---

## ⚙️ Installation

```bash
git clone https://github.com/RayanShaiaa-cmd/Smart-Data-Analyzer---GUI-version.git
cd Smart-Data-Analyzer---GUI-version
code . (write it in terminal to open the program in vs code)
pip install -r requirements.txt


🔑 Environment Setup
Create a .env file:
API_KEY=your_openweathermap_api_key

▶️ Run the Project
streamlit run app.py


##📊 Dashboard Modules
1. Today's Report
Live weather metrics
Quick visual summary
2. Specific Day Search
Retrieve historical weather by date
Display structured table
3. History Analytics
Temperature over time
Humidity trends
Wind speed comparison
Statistical insights
4. Forecast Analysis
Future temperature prediction
Line chart visualization


##📈 Example Output
Interactive dashboard
Line charts (temperature trends)
Bar charts (weather comparison)
Forecast curves

##⚠️ Known Issues
No cloud database (CSV only)
Requires valid API key
Limited error handling for API failures

##🔧 Future Improvements
Add Machine Learning forecasting model
Replace CSV with PostgreSQL database
Add authentication system
Deploy to Streamlit Cloud
Build mobile-friendly UI
Add multi-city comparison dashboard

##👨‍💻 Author

Rayan Shaiaa
AI & Data Science Student | Machine Learning Enthusiast

##⭐ Why This Project Matters

This project demonstrates:

Real-world API integration
Data engineering pipeline design
Interactive dashboard development
Time-series data analysis
Clean modular Python architecture
Portfolio-ready AI/ML engineering project