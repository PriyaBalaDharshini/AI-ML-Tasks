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

plt.figure()

plt.boxplot(df["delivery_days"].dropna())
#plt.xlim(0, 10000)
plt.title("Distribution of Delivery Days")
plt.xlabel("Delivery Days")
plt.ylabel("Days")

plt.show()
