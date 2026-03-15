# E-Commerce Sales Analysis

**Author:** Taimoor Ali  
**Background:** BS Mathematics, University of Jhang  
**Tools:** Python, Pandas, Matplotlib, Seaborn

---

## Overview

Exploratory data analysis (EDA) of a US retail superstore dataset containing
9,994 orders across 3 product categories, 49 states, and 4 years of sales data.

The goal was to uncover actionable business insights from raw sales data — including
which categories and regions drive the most revenue, how sales trend over time,
and whether discount strategies are hurting overall profitability.

---

## Key Findings

1. **Technology is the top-selling category** — generating the highest total revenue,
   though Furniture and Office Supplies follow closely.

2. **Sales peak strongly in Q4 (Oct–Dec)** — consistent across all years in the
   dataset, suggesting seasonal demand tied to the holiday period.

3. **California, New York, and Texas are the top 3 states** by sales volume —
   together accounting for a significant share of total revenue.

4. **High discounts consistently destroy profit margins** — orders with discounts
   above 40% are almost always loss-making. This is the most important business
   insight in the dataset: the company is likely over-discounting.

---

## Charts Produced

| File | Description |
|------|-------------|
| `chart1_category_sales.png` | Horizontal bar chart — total sales by product category |
| `chart2_monthly_trend.png` | Line chart — monthly sales trend over 4 years |
| `chart3_top_states.png` | Bar chart — top 10 US states by total sales |
| `chart4_profit_discount.png` | Scatter plot — profit vs discount rate (with break-even line) |

---

## How to Run

1. Clone this repository
2. Download the dataset from Kaggle:  
   https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
3. Place `Sample - Superstore.csv` in the project folder
4. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
5. Run the analysis:
   ```bash
   python analysis.py
   ```
   Or open `ecommerce_sales_analysis.ipynb` in Jupyter Notebook.

---

## Dataset

- **Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Rows:** 9,994 orders
- **Columns:** 21 (Order ID, Order Date, Category, Sales, Profit, Discount, Region, State, etc.)
- **Time period:** 2014–2017

---

## Skills Demonstrated

- Data loading and inspection with **Pandas**
- Data cleaning: handling dates, duplicates, missing values
- Groupby aggregations and time-series analysis
- Data visualisation with **Matplotlib** and **Seaborn**
- Communicating findings in plain language

---

*This project was built as part of my preparation for an MS in Data Science & AI.*  
*Contact: taimoorali5588@gmail.com*
