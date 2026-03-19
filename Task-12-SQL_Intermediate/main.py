import pandas as pd
import sqlite3

customers_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/customers.csv"
orders_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/orders.csv"

customers_df = pd.read_csv(customers_url)
orders_df = pd.read_csv(orders_url)

conn = sqlite3.connect(":memory:")
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# Task 1 — Aggregation and Grouping
query = """
SELECT 
    CustomerID,
    COUNT(OrderID) AS order_count,
    SUM(Freight) AS total_freight,
    AVG(Freight) AS avg_freight
FROM orders
GROUP BY CustomerID
ORDER BY total_freight DESC
LIMIT 10;
"""

# Task 2 — WHERE vs. HAVING
query1 = """
SELECT 
    CustomerID,
    COUNT(OrderID) AS high_freight_orders
FROM orders
WHERE Freight > 50
GROUP BY CustomerID
ORDER BY high_freight_orders DESC
LIMIT 10;

"""
query2 = """

SELECT 
    CustomerID,
    SUM(Freight) AS total_freight
FROM orders
GROUP BY CustomerID
HAVING SUM(Freight) > 500
ORDER BY total_freight DESC;

"""


result = pd.read_sql_query(query, conn)
result1 = pd.read_sql_query(query1, conn)
result2 = pd.read_sql_query(query2, conn)
print(result, result1, result2)

# Task 3 — JOIN and Aggregation

query3 = """
SELECT 
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID) AS order_count,
    SUM(o.Freight) AS total_freight
FROM customers c
INNER JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country
ORDER BY total_freight DESC;

"""

query4='''SELECT 
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID) AS order_count,
    SUM(o.Freight) AS total_freight
FROM customers c
LEFT JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country;
'''
result3 = pd.read_sql_query(query, conn)
print(result3)
