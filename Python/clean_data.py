import pandas as pd

# Load raw CSV files
customers = pd.read_csv('../data/customers.csv')
orders = pd.read_csv('../data/orders.csv')

# Remove duplicates
customers_clean = customers.drop_duplicates()
orders_clean = orders.drop_duplicates()

# Save cleaned versions
customers_clean.to_csv('../data/customers_clean.csv', index=False)
orders_clean.to_csv('../data/orders_clean.csv', index=False)

print("✅ Data cleaned and saved as customers_clean.csv and orders_clean.csv")
print(f"🧹 Removed {len(orders) - len(orders_clean)} duplicate orders")
print(f"🧹 Removed {len(customers) - len(customers_clean)} duplicate customers")
