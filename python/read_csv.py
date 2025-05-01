import pandas as pd

# Load CSVs
customers = pd.read_csv('../data/customers.csv').drop_duplicates()
orders = pd.read_csv('../data/orders.csv').drop_duplicates()

# Save clean files
customers.to_csv('../data/customers_clean.csv', index=False)
orders.to_csv('../data/orders_clean.csv', index=False)
