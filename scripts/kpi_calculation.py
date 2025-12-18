import pandas as pd

# Load clean datasets
transactions = pd.read_csv("data/processed/transactions_clean.csv")
inventory = pd.read_csv("data/processed/inventory_clean.csv")
customers = pd.read_csv("data/processed/customers_clean.csv")

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

category_df = transactions.merge(
    customers,
    on="customer_name",
    how="left"
)

revenue_by_category = (
    category_df
    .groupby("customer_category")["amount"]
    .sum()
    .reset_index()
    .sort_values(by="amount", ascending=False)
)

item_sales = transactions.groupby("item_name").agg(
    total_revenue=("amount", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

item_sales = item_sales.merge(
    inventory[["item_name", "base_price"]],
    on="item_name",
    how="left"
)

item_sales["total_cost"] = item_sales["base_price"] * item_sales["total_quantity"]
item_sales["gross_margin"] = (
    (item_sales["total_revenue"] - item_sales["total_cost"]) / item_sales["total_revenue"]
)

# save KPIs
monthly_revenue.to_csv("outputs/kpis/kpi_monthly_revenue.csv", index=False)
revenue_by_customer.to_csv("outputs/kpis/kpi_revenue_by_customer.csv", index=False)
revenue_by_item.to_csv("outputs/kpis/kpi_revenue_by_item.csv", index=False)
atv_df.to_csv("outputs/kpis/kpi_average_transaction_value.csv", index=False)
revenue_by_category.to_csv("outputs/kpis/kpi_revenue_by_customer_category.csv", index=False)
item_sales.to_csv("outputs/kpis/kpi_item_gross_margin.csv", index=False)