import pandas as pd

transactions = pd.read_csv("data/raw/transactions.csv", sep=";")
customers = pd.read_csv("data/raw/customers.csv", sep=";")
inventory = pd.read_csv("data/raw/inventory.csv", sep=";")

print("=== TRANSACTIONS ===")
print(transactions.info())
print(transactions.head())

print("\n=== CUSTOMERS ===")
print(customers.info())
print(customers.head())

print("\n=== INVENTORY ===")
print(inventory.info())
print(inventory.head())
