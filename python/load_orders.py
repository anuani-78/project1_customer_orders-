import pandas as pd
import psycopg2

df = pd.read_csv('../data/orders_clean.csv')

conn = psycopg2.connect(
    host="localhost",
    database="project1_customer_orders-",
    user="anuani-78",
    password="Repeat"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;",
                (row['order_id'], row['customer_id'], row['order_date']))

conn.commit()
cur.close()
conn.close()
print("Orders loaded.")
