"""
Run this script to generate sample data for testing.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(start_date, num_days):
    dates = [(start_date + timedelta(days=x)).strftime('%d/%m/%y') for x in range(num_days)]
    data = {
        "Date": dates,
        "Laptops": np.random.randint(0, 50, num_days),
        "LCDs": np.random.randint(0, 50, num_days),
        "LEDs": np.random.randint(0, 50, num_days),
        "PCs": np.random.randint(0, 50, num_days),
        "Mouses": np.random.randint(0, 50, num_days),
        "Keyboards": np.random.randint(0, 50, num_days),
        "GPUs": np.random.randint(0, 50, num_days),
        "Speakers": np.random.randint(0, 50, num_days),
        "Microphones": np.random.randint(0, 50, num_days),
        "Cables": np.random.randint(0, 50, num_days),
    }
    return pd.DataFrame(data)

start_date = datetime(2024, 7, 1)
num_days = 31

for i in range(3):
    shop_data = generate_data(start_date, num_days)
    shop_data.to_csv(f'shop{i}.csv', index=False)

print("CSV files created successfully!")

