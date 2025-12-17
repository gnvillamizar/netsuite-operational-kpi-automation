import pandas as pd

transactions = pd.read_csv("data/processed/transactions_clean.csv")
inventory = pd.read_csv("data/processed/inventory_clean.csv")

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
transactions["month"] = transactions["transaction_date"].dt.to_period("M")

monthly_revenue = (
    transactions
    .groupby("month")["amount"]
    .sum()
    .reset_index()
    .rename(columns={"amount": "monthly_revenue"})
)

revenue_by_customer = (
    transactions
    .groupby("customer_name")["amount"]
    .sum()
    .reset_index()
    .rename(columns={"amount": "total_revenue"})
    .sort_values(by="total_revenue", ascending=False)
)

revenue_by_item = (
    transactions
    .groupby("item_name")["amount"]
    .sum()
    .reset_index()
    .rename(columns={"amount": "total_revenue"})
    .sort_values(by="total_revenue", ascending=False)
)

average_transaction_value = transactions["amount"].mean()
atv_df = pd.DataFrame({
    "average_transaction_value": [average_transaction_value]
})

inventory_prices = inventory[["item_name", "base_price"]]
monthly_revenue.to_csv("outputs/kpis/kpi_monthly_revenue.csv", index=False)
revenue_by_customer.to_csv("outputs/kpis/kpi_revenue_by_customer.csv", index=False)
revenue_by_item.to_csv("outputs/kpis/kpi_revenue_by_item.csv", index=False)
atv_df.to_csv("outputs/kpis/kpi_average_transaction_value.csv", index=False)
inventory_prices.to_csv("outputs/kpis/kpi_inventory_base_prices.csv", index=False)