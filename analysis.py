# =============================================================================
#  E-Commerce Sales Analysis
#  Author  : Taimoor Ali
#  Dataset : Superstore Sales Dataset (Kaggle)
#  Tools   : Python, Pandas, Matplotlib, Seaborn
# =============================================================================
#
#  HOW TO RUN:
#  1. Download dataset from Kaggle:
#     https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
#  2. Save the CSV file as "Sample - Superstore.csv" in the same folder as this script
#  3. Open terminal in that folder and run:
#       python analysis.py
#  4. Four chart images will be saved in the same folder
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from matplotlib.lines import Line2D

# ── Style ──────────────────────────────────────────────────────────────────────
sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.family'] = 'DejaVu Sans'

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 1 — LOAD DATA
# ══════════════════════════════════════════════════════════════════════════════
print('Loading data...')
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print(f'  Loaded {df.shape[0]:,} rows and {df.shape[1]} columns')
print(f'  Columns: {df.columns.tolist()}\n')

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 2 — EXPLORE DATA
# ══════════════════════════════════════════════════════════════════════════════
print('--- Basic Data Info ---')
print(df.info())
print('\n--- Basic Statistics ---')
print(df.describe())

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 3 — CLEAN DATA
# ══════════════════════════════════════════════════════════════════════════════
print('\nCleaning data...')

# Check missing values
missing = df.isnull().sum()
print(f'  Missing values:\n{missing[missing > 0]}')

# Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
print(f'  Duplicates removed: {before - len(df)}')

# Extract time columns
df['Year']  = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.to_period('M')

print(f'  Final shape: {df.shape}')
print('  Data is clean!\n')

# ══════════════════════════════════════════════════════════════════════════════
#  STEP 4 — VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════════

# ── Chart 1: Sales by Category ────────────────────────────────────────────────
print('Building Chart 1: Sales by Category...')
category_sales = df.groupby('Category')['Sales'].sum().sort_values()

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#4C9BE8', '#6B5EA8', '#E87B4C']
category_sales.plot(kind='barh', ax=ax, color=colors, edgecolor='none')

ax.set_title('Total Sales by Product Category', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Total Sales (USD)', fontsize=11)
ax.set_ylabel('')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

for i, v in enumerate(category_sales):
    ax.text(v + 5000, i, f'${v:,.0f}', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('chart1_category_sales.png', dpi=150, bbox_inches='tight')
plt.close()
print('  Saved: chart1_category_sales.png')


# ── Chart 2: Monthly Sales Trend ──────────────────────────────────────────────
print('Building Chart 2: Monthly Sales Trend...')
monthly = df.groupby('Month')['Sales'].sum()
monthly.index = monthly.index.astype(str)

fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(monthly.index, monthly.values, color='#4C9BE8', linewidth=2,
        marker='o', markersize=4, markerfacecolor='white', markeredgewidth=1.5)
ax.fill_between(monthly.index, monthly.values, alpha=0.12, color='#4C9BE8')

ax.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Sales (USD)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_xticks(range(0, len(monthly), 3))
ax.set_xticklabels(monthly.index[::3], rotation=45, ha='right', fontsize=9)

plt.tight_layout()
plt.savefig('chart2_monthly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print('  Saved: chart2_monthly_trend.png')


# ── Chart 3: Top 10 States by Sales ───────────────────────────────────────────
print('Building Chart 3: Top 10 States by Sales...')
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(top_states.index, top_states.values,
              color='#6B5EA8', edgecolor='none', width=0.6)

ax.set_title('Top 10 States by Total Sales', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Total Sales (USD)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_xticklabels(top_states.index, rotation=30, ha='right', fontsize=10)

for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, h + 2000,
            f'${h:,.0f}', ha='center', va='bottom', fontsize=8.5)

plt.tight_layout()
plt.savefig('chart3_top_states.png', dpi=150, bbox_inches='tight')
plt.close()
print('  Saved: chart3_top_states.png')


#  Chart 4: Profit vs Discount 
print('Building Chart 4: Profit vs Discount...')
fig, ax = plt.subplots(figsize=(8, 6))

colors_scatter = df['Profit'].apply(lambda x: '#4C9BE8' if x >= 0 else '#E84C4C')
ax.scatter(df['Discount'], df['Profit'], alpha=0.25, c=colors_scatter,
           s=18, edgecolors='none')
ax.axhline(y=0, color='#555', linestyle='--', linewidth=1, label='Break-even line')

ax.set_title('Profit vs Discount Rate\nDo Higher Discounts Hurt Profit?',
             fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Discount Rate (0 = no discount, 1 = 100% off)', fontsize=11)
ax.set_ylabel('Profit (USD)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#4C9BE8',
           markersize=8, label='Profitable order'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#E84C4C',
           markersize=8, label='Loss-making order'),
    Line2D([0], [0], color='#555', linestyle='--', label='Break-even')
]
ax.legend(handles=legend_elements, fontsize=10)

plt.tight_layout()
plt.savefig('chart4_profit_discount.png', dpi=150, bbox_inches='tight')
plt.close()
print('  Saved: chart4_profit_discount.png')


#  STEP 5 — PRINT KEY FINDINGS

print('\n' + '='*60)
print('KEY FINDINGS')
print('='*60)
print(f'  Total orders analysed : {len(df):,}')
print(f'  Total revenue         : ${df["Sales"].sum():,.0f}')
print(f'  Total profit          : ${df["Profit"].sum():,.0f}')
print(f'  Top category          : {category_sales.idxmax()}')
print(f'  Top state             : {top_states.idxmax()}')
print(f'  Orders at a loss      : {(df["Profit"] < 0).sum():,} ({(df["Profit"] < 0).mean()*100:.1f}%)')
print('='*60)
print('\nAll 4 charts saved successfully!')
