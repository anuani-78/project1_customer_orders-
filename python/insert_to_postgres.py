import pandas as pd
import psycopg2

# Load clean CSVs
customers = pd.read_csv('../data/customers_clean.csv')
orders = pd.read_csv('../data/orders_clean.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="project1_customer_orders",
    user="anuani-78",
    password="Repeat"
)

cur = conn.cursor()

# Insert data into customers
for _, row in customers.iterrows():
    cur.execute(
        "INSERT INTO customers (customer_id, customer_name) VALUES (%s, %s)",
        (int(row['customer_id']), row['customer_name'])
    )

# Insert data into orders
for _, row in orders.iterrows():
    cur.execute(
        "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)",
        (int(row['order_id']), int(row['customer_id']), row['order_date'])
    )

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully!")
