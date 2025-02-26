# Energy Consumption Forecasting 📊

## 📌 Project Overview
This project simulates and forecasts energy consumption using synthetic time-series data. The dataset includes **hourly energy consumption** values over one year, generated with **seasonal and daily trends**. The goal is to analyze trends and develop machine learning models to predict future energy demand.

## 🔍 Dataset
- **File:** `synthetic_energy_consumption.csv`
- **Columns:** 
  - `Timestamp`: Time index (hourly data)
  - `Energy_Consumption`: Simulated energy consumption in kWh

## 📊 Exploratory Data Analysis (EDA)
Key insights from the data:
- **Mean Consumption**: ~100 kWh
- **Seasonality Observed**: Higher energy usage in **winter**, lower in **summer**
- **Daily Trends**: Consumption peaks at specific hours
- **Fluctuations**: Standard deviation ~16.5 kWh

### 🖼 Visualizations:
1. **Full Year Trend:**
   - Shows **seasonal energy consumption** changes.
2. **Daily Averages:**
   - Highlights **short-term variations**.

## 🚀 Next Steps: Forecasting Models
This repository will be updated with forecasting models such as:
- **ARIMA/SARIMA** (Traditional time-series model)
- **Facebook Prophet** (Seasonal forecasting)
- **LSTM Neural Network** (Deep learning)

## 🛠 Setup & Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/energy_forecasting_project.git
cd energy_forecasting_project

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
