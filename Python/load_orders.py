import pandas as pd
import psycopg2

# Load the cleaned orders CSV
df = pd.read_csv('../data/orders.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="project1_customer_orders",
    user="anuani-78",
    password="Repeat"   # 🔁 Replace with your actual password
)

cur = conn.cursor()

# Insert orders into the 'orders' table
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)",
        (row['order_id'], row['customer_id'], row['order_date'])
    )

conn.commit()
cur.close()
conn.close()

print("Orders loaded.")
