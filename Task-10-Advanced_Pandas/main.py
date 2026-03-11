import pandas as pd
import random

random.seed(42)

# Define data parameters
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

# Generate 200 sales transactions
data = {
    'transaction_id': range(1001, 1201),
    'region': [random.choice(regions) for _ in range(200)],
    'category': [random.choice(categories) for _ in range(200)],
    'salesperson': [random.choice(salespersons) for _ in range(200)],
    'sales_amount': [round(random.uniform(50, 5000), 2) for _ in range(200)],
    'customer_id': [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data)
print(df.head(10))
print(f"\nDataset shape: {df.shape}")

# Task 1: Basic Grouping and Single Aggregations

# 1.1 Calculate total sales amount for each region using groupby() and sum()
total_sales_amount = df.groupby('region')['sales_amount'].sum().sort_values(ascending=False).reset_index()
print("Total sales amount for each region\n", total_sales_amount)

# 1.2 Count the number of transactions for each product category using groupby() and count()
number_of_transactions=df.groupby('category')['transaction_id'].count().reset_index()
print("number of transactions for each product category \n:",number_of_transactions)

# 1.3 Calculate the average sales amount per salesperson using groupby() and mean()
average_sales_amount_per_salesperson = df. groupby('salesperson')['sales_amount'].mean().reset_index()
print("Average sales amount per salesperson \n", average_sales_amount_per_salesperson)



#Task 2: Multi-Column Grouping and Multiple Aggregations
# 2.1 Group by both region AND category to calculate total sales for each combination using:
combained_total_sales = df.groupby(['region', 'category'])['sales_amount'].sum().sort_values(ascending=False)
print("Total sales by region and category: \n", combained_total_sales)

# 2.2 For each salesperson, calculate three metrics simultaneously using the agg() method
three_matrics = df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).sort_values(by='sum',ascending=False).reset_index()
print("Three matrics: \n", three_matrics)

max_total_revenue = combained_total_sales.idxmax()
min_total_revenue = combained_total_sales.idxmin()
print(f"Max total revenue: {max_total_revenue}, Min total revenue: {min_total_revenue}")


# Task 3: Custom Aggregation and Complete Sales Report
# Define a custom aggregation function that calculates the sales range (max - min) for each group

def sales_range(x):
    return max(x) - min(x)
region_sales = df.groupby('region')['sales_amount'].agg(['sum', 'mean', 'min', 'max', sales_range])

print("Region sales: \n", region_sales)

final_summary_report = df.groupby('region').agg({
    'sales_amount': ['sum', 'mean'],
    'customer_id': 'count'
}).reset_index()

print(final_summary_report)

