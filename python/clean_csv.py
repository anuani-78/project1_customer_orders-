import pandas as pd

# Read raw CSVs
customers = pd.read_csv('../data/customers.csv')
orders = pd.read_csv('../data/orders.csv')

# Remove duplicates
customers_clean = customers.drop_duplicates()
orders_clean = orders.drop_duplicates()

# Save to new clean files
customers_clean.to_csv('../data/customers_clean.csv', index=False)
orders_clean.to_csv('../data/orders_clean.csv', index=False)

print("CSV files cleaned and saved.")
