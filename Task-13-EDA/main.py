import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(50)
n = 200

data = {
    "order_id": np.arange(1001, 1001 + n),
    "city": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Chennai"], size=n),
    "category": np.random.choice(
        ["Electronics", "Clothing", "Groceries", "Furniture"], size=n
    ),
    "order_value": np.random.randint(200, 5000, size=n).astype(float),
    "delivery_days": np.random.randint(1, 15, size=n).astype(float),
    "rating": np.random.choice([1, 2, 3, 4, 5, None], size=n),
}
missing_indices_order = np.random.choice(n, size=15, replace=False)
missing_indices_delivery = np.random.choice(n, size=10, replace=False)
data["order_value"][missing_indices_order] = np.nan
data["delivery_days"][missing_indices_delivery] = np.nan

data["order_value"][5] = 95000
data["order_value"][88] = 87000

df = pd.DataFrame(data)

# Task 1 — Inspect & Handle Missing Values
print("Shape: \n", df.shape)
print("Date Type: \n", df.dtypes)
print("Missing values: \n", df.isnull().sum())
missing_count = df.isnull().sum()
missing_percent = (missing_count/len(df))*100
print("Missing percent: \n", missing_percent.round(2))


# Task 2 — Summarize & Visualize
print("Summary: \n", df.describe())
"""
Order value column has the heighest mean value. 
order value column has the heighest value gap b/w 75% and max
"""

