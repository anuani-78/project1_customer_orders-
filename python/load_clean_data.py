import pandas as pd
import psycopg2

# Step 1: Read CSVs
customers_df = pd.read_csv('../data/customers.csv')
orders_df = pd.read_csv('../data/orders.csv')

# Step 2: Drop Duplicates
customers_df = customers_df.drop_duplicates()
orders_df = orders_df.drop_duplicates()

# Step 3: Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="data_engineer_practice",  # change if your DB name is different
    user="postgres",                    # your PostgreSQL username
    password="your_password"            # your PostgreSQL password
)
cur = conn.cursor()

# Step 4: Insert Customers
for _, row in customers_df.iterrows():
    cur.execute(
        "INSERT INTO customers (customer_id, customer_name) VALUES (%s, %s) ON CONFLICT (customer_id) DO NOTHING",
        (row['customer_id'], row['customer_name'])
    )

# Step 5: Insert Orders
for _, row in orders_df.iterrows():
    cur.execute(
        "INSERT INTO orders (order_id, customer_id, order_date) VALUES (%s, %s, %s) ON CONFLICT (order_id) DO NOTHING",
        (row['order_id'], row['customer_id'], row['order_date'])
    )

# Finalize
conn.commit()
cur.close()
conn.close()

print("✅ Data cleaned and loaded into PostgreSQL!")
