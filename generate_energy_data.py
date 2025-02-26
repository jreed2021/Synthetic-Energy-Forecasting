import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the synthetic dataset
days = 365  # One year of data
data_points_per_day = 24  # Hourly data points
total_points = days * data_points_per_day  # Total number of points

# Generate time index (hourly intervals)
time_index = pd.date_range(start='2025-01-01', periods=total_points, freq='H')

# Create seasonal patterns
yearly_pattern = np.sin(2 * np.pi * (time_index.dayofyear / 365.25))  # Annual seasonality
daily_pattern = np.sin(2 * np.pi * (time_index.hour / 24))  # Daily seasonality

# Add randomness/noise
random_noise = np.random.normal(scale=5, size=total_points)

# Combine all components to create synthetic energy consumption data
energy_consumption = 100 + (20 * yearly_pattern) + (10 * daily_pattern) + random_noise

# Create a DataFrame
df = pd.DataFrame({'Timestamp': time_index, 'Energy_Consumption': energy_consumption})

# Save dataset to CSV file
csv_filename = "synthetic_energy_consumption.csv"
df.to_csv(csv_filename, index=False)

# Display sample plot for first 7 days
plt.figure(figsize=(12, 5))
df.set_index('Timestamp')['2025-01-01':'2025-01-07'].plot()
plt.title('Synthetic Energy Consumption Data (First Week of 2025)')
plt.xlabel('Time')
plt.ylabel('Energy Consumption (kWh)')
plt.grid()
plt.show()

print(f"Dataset saved as: {csv_filename}")
