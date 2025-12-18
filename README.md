# NetSuite Operational KPI Automation

Automated generation of operational KPIs from NetSuite-like ERP data using Python, designed to support management decision-making without direct ERP access.

---

## Business Context

In many organizations, operations and management teams need quick visibility into sales performance, customer behavior, and product profitability without logging into the ERP system every day.

This project simulates a real-world NetSuite environment by using exported ERP-style data and automating the calculation of key operational KPIs commonly used by finance, operations, and analytics teams.

---

## Data Sources

The project uses **simulated NetSuite exports** based on real ERP structures:

- **Transactions**  
  Sales transactions including date, customer, item, quantity, amount, status, and location.

- **Customers**  
  Customer master data including category, status, and sales representative.

- **Inventory**  
  Item master data including item type and base price.

All datasets were cleaned, standardized, and stored as processed CSV files to simulate a real ERP analytics pipeline.

---

## KPIs Generated

The following KPIs were calculated to reflect common operational and financial insights:

- **Monthly Revenue**  
  Tracks revenue trends over time to support performance monitoring.

- **Revenue by Customer Category**  
  Identifies which customer segments contribute most to total revenue.

- **Top Customers by Revenue**  
  Highlights key accounts driving business results.

- **Top Items by Revenue**  
Highlights key items driving business results.

- **Item-Level Performance and Margins**  
  Combines sales data with inventory base prices to calculate:
  - Total revenue per item  
  - Total cost  
  - Gross margin  

These KPIs help identify profitable products and potential pricing or cost issues.

---

## Project Structure

netsuite-operational-kpi-automation/
│
├── data/
│   ├── raw/          # Simulated NetSuite exports
│   └── processed/    # Cleaned and standardized datasets
│
├── scripts/
│
├── outputs/
│   ├── kpis/             # KPI CSV outputs
│   └── visualizations/   # Charts and plots
│
├── requirements.txt
└── README.md