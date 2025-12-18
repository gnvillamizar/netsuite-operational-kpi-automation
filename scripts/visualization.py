import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load KPI data
monthly_revenue = pd.read_csv("outputs/kpis/kpi_monthly_revenue.csv")
top_customers = pd.read_csv("outputs/kpis/kpi_revenue_by_customer.csv").head(10)
atv = pd.read_csv("outputs/kpis/kpi_average_transaction_value.csv")
top_items = pd.read_csv("outputs/kpis/kpi_revenue_by_item.csv").head(5)
cat_revenue = pd.read_csv("outputs/kpis/kpi_revenue_by_customer_category.csv")
item_gross_margin = pd.read_csv("outputs/kpis/kpi_item_gross_margin.csv")

# Formatter for thousands
def thousands_formatter(x, pos):
    return f'{int(x):,}'

# Extract average transaction value
atv_value = atv["average_transaction_value"].iloc[0]

# Plot Monthly Revenue
monthly_revenue["month"] = monthly_revenue["month"].astype(str)
plt.figure(figsize=(10, 6))
plt.bar(monthly_revenue["month"], monthly_revenue["monthly_revenue"])
plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.axhline(
    y=atv_value,
    linestyle='--',
    color='red',
    label="Average Transaction Value (Global)"
)
plt.title("Monthly Revenue vs Average Transaction Value")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/visualizations/monthly_revenue_vs_atv.png")
plt.close()

# Plot Top 10 Customers by Revenue
plt.figure(figsize=(10, 6))
plt.barh(top_customers["customer_name"], top_customers["total_revenue"])
plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.axvline(
    x=atv_value,
    linestyle='--',
    color='red',
    label="Average Transaction Value (Global)"
)
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Customer")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/visualizations/top_customers_vs_atv.png")
plt.close()

#Plot Top 5 Items by Revenue
plt.figure(figsize=(10, 6))
plt.barh(top_items["item_name"], top_items["total_revenue"])
plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.axvline(
    x=atv_value,
    linestyle='--',
    color='red',
    label="Average Transaction Value (Global)"
)
plt.title("Top 5 Items by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Item")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/visualizations/top_items_vs_atv.png")
plt.close()

# Plot Revenue by Customer Category
plt.figure(figsize=(10, 6))
plt.barh(cat_revenue["customer_category"], cat_revenue["amount"])
plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.axvline(
    x=atv_value,
    linestyle='--',
    color='red',
    label="Average Transaction Value (Global)"
)
plt.title("Revenue by Customer Category")
plt.xlabel("Customer Category")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/visualizations/revenue_by_customer_category.png")
plt.close()

# Plot Item Gross Margin
plt.figure(figsize=(10, 6))
plt.bar(item_gross_margin["item_name"], item_gross_margin["gross_margin"])
plt.title("Item Gross Margin (%)")
plt.xlabel("Item")
plt.ylabel("Gross Margin (%)")
plt.xticks(rotation=45, ha='right')
max_margin = item_gross_margin["gross_margin"].max()
if max_margin == 0:
    plt.ylim(0, 1)
else:
    plt.ylim(0, max_margin * 1.2)
plt.tight_layout()

plt.savefig("outputs/visualizations/item_gross_margin.png")
plt.close()