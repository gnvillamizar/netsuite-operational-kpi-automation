import pandas as pd

transactions = pd.read_csv("data/processed/transactions_clean.csv")
customers = pd.read_csv("data/processed/customers_clean.csv")
inventory = pd.read_csv("data/processed/inventory_clean.csv")

print("=== TRANSACTIONS ===")
print(transactions.info())
print(transactions.head())

print("\n=== CUSTOMERS ===")
print(customers.info())
print(customers.head())

print("\n=== INVENTORY ===")
print(inventory.info())
print(inventory.head())
