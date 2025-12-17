import pandas as pd

transactions = pd.read_csv("data/raw/transactions.csv", sep=";")
customers = pd.read_csv("data/raw/customers.csv", sep=";")
inventory = pd.read_csv("data/raw/inventory.csv", sep=";")

transactions = transactions.rename(columns={
    "date": "transaction_date",
    "Document Number": "transaction_id",
    "Name": "customer_name",
    "Item": "item_name",
    "Sum of Quantity": "quantity",
    "Sum of Amount": "amount",
    "Status": "transaction_status",
    "Location": "location"
})

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"], dayfirst=True)
transactions["transaction_id"] = transactions["transaction_id"].astype(str)
transactions["customer_name"] = transactions["customer_name"].astype(str)
transactions["item_name"] = transactions["item_name"].astype(str)
transactions["quantity"] = transactions["quantity"].astype(int)
transactions["amount"] = transactions["amount"].astype(float)
transactions["transaction_status"] = transactions["transaction_status"].astype(str)
transactions["location"] = transactions["location"].astype(str)

customers = customers.rename(columns={
    "ID interno": "customer_id",
    "NOMBRE": "customer_name",
    "Categoria": "customer_category",
    "Estado": "customer_status",
    "Representante de ventas": "sales_rep"
})

customers["customer_id"] = customers["customer_id"].astype(str)
customers["customer_name"] = customers["customer_name"].astype(str)
customers["customer_category"] = customers["customer_category"].astype(str)
customers["customer_status"] = customers["customer_status"].astype(str)
customers["sales_rep"] = customers["sales_rep"].astype(str)

inventory = inventory.rename(columns={
    "ID interno": "item_id",
    "Nombre para mostrar": "item_name",
    "Subtipo": "item_type",
    "Precio base": "base_price"
})

inventory["item_id"] = inventory["item_id"].astype(str)
inventory["item_name"] = inventory["item_name"].astype(str)
inventory["item_type"] = inventory["item_type"].astype(str)
inventory["base_price"] = inventory["base_price"].astype(float)

inventory = inventory[["item_id", "item_name", "item_type", "base_price"]]

transactions.to_csv("data/processed/transactions_clean.csv", index=False)
customers.to_csv("data/processed/customers_clean.csv", index=False)
inventory.to_csv("data/processed/inventory_clean.csv", index=False)