import pandas as pd
import psycopg2

df = pd.read_csv('../data/customers_clean.csv')

conn = psycopg2.connect(
    host="localhost",
    database="project1_customer_orders-",
    user="anuani-78",
    password="Repeat"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("INSERT INTO customers (customer_id, customer_name) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                (row['customer_id'], row['customer_name']))

conn.commit()
cur.close()
conn.close()
print("Customers loaded.")
