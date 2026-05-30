import json

def code(src):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}

def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}

cells = []

# ── PIPELINE ──────────────────────────────────────────────────────────────────
cells.append(code(
"""import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

sns.set_theme(style='whitegrid')

# load price history
data_folder = '../data/'
for file in os.listdir(data_folder):
    if 'price_history_full' in file:
        df = pd.read_csv(data_folder + file)

launch_ref = pd.read_csv('../data/official_launch_prices.csv')
df = df.merge(launch_ref, on='submodel_name')
df['official_premiere_date'] = pd.to_datetime(df['official_premiere_date'])
df['datetime'] = pd.to_datetime(df['datetime'])
df['days_since_launch'] = (df['datetime'] - df['official_premiere_date']).dt.days
df = df[df['days_since_launch'] > 0]
df['NEW'] = df['new_price'] * 100
df = df.drop('new_price', axis=1)
df['price_pct_of_launch'] = round(df['NEW'] / df['official_launch_price'] * 100, 1)
df['days_rounded'] = (df['days_since_launch'] / 7).round() * 7
df['tier'] = df.apply(lambda row: row['submodel_name'].replace(row['generation_name'], '').strip(), axis=1)
df['tier'] = df['tier'].replace('', 'Base')

# load monthly sold
ms_df = pd.read_csv('../data/monthly_sold_full.csv')
ms_df = ms_df.merge(launch_ref, on='submodel_name', how='left')
ms_df['official_premiere_date'] = pd.to_datetime(ms_df['official_premiere_date'])
ms_df['datetime'] = pd.to_datetime(ms_df['datetime'])
del ms_df['premiere_date']
ms_df['days_since_launch'] = (ms_df['datetime'] - ms_df['official_premiere_date']).dt.days
ms_df['days_rounded'] = (ms_df['days_since_launch'] / 7).round() * 7
ms_df = ms_df[ms_df['days_since_launch'] >= 0]
ms_df['tier'] = ms_df.apply(lambda row: row['submodel_name'].replace(row['generation_name'], '').strip(), axis=1)
ms_df['tier'] = ms_df['tier'].replace('', 'Base')

# price decay dataframes
base_apple_df = df[(df['tier'] == 'Base') & (df['brand'] == 'Apple') & (df['generation_name'] != 'iPhone 17')]
base_apple_decay_df = base_apple_df.groupby(['generation_name', 'product_grade', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()

base_samsung_df = df[(df['tier'] == 'Base') & (df['brand'] == 'Samsung')]
base_samsung_decay_df = base_samsung_df.groupby(['generation_name', 'product_grade', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()

base_google_df = df[(df['tier'] == 'Base') & (df['brand'] == 'Google')]
base_google_decay_df = base_google_df.groupby(['generation_name', 'product_grade', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()

base_combined_df = df[df['tier'] == 'Base']
all_brands_decay_df = base_combined_df.groupby(['brand', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()

grouped_generation_decay_df = df.groupby(['submodel_name', 'generation_name', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()
iphone13_decay_df = grouped_generation_decay_df[grouped_generation_decay_df['generation_name'] == 'iPhone 13']

# 1-year retention
yearly_change_df = df[(df['days_rounded'] > 330) & (df['days_rounded'] < 380)]
retention_1yr_df = yearly_change_df.groupby('generation_name').agg(
    price_retention=('price_pct_of_launch', 'mean'),
    brand=('brand', 'first')
).reset_index().sort_values('price_retention', ascending=False)

brand_retention = retention_1yr_df.groupby('brand')['price_retention'].mean()
apple_retention = brand_retention['Apple']
samsung_retention = brand_retention['Samsung']
google_retention = brand_retention['Google']

grade_means = df[(df['tier'] == 'Base') & (df['brand'] == 'Apple')].groupby('product_grade')['price_pct_of_launch'].mean()
renewed_premium_premium = grade_means['Renewed Premium'] - grade_means['Renewed']

# sales rank dataframes
apple_base_rank_df = ms_df[(ms_df['tier'] == 'Base') & (ms_df['brand'] == 'Apple') & (ms_df['monthly_sold'] >= 0)]
apple_base_rank_df = apple_base_rank_df.groupby(['generation_name', 'days_rounded'])['monthly_sold'].mean().reset_index()

iphone13_rank_df = ms_df[ms_df['generation_name'] == 'iPhone 13']
iphone13_rank_df = iphone13_rank_df.groupby(['submodel_name', 'days_rounded'])['monthly_sold'].mean().reset_index()

rank_dates_gen_df = (ms_df.set_index('datetime')
    .groupby(['generation_name', 'brand', 'tier'])
    .resample('W')['monthly_sold'].mean().reset_index())
rank_dates_gen_df['monthly_sold'] = rank_dates_gen_df.groupby('generation_name')['monthly_sold'].ffill()
apple_base_rank_dates_df = rank_dates_gen_df[
    (rank_dates_gen_df['tier'] == 'Base') &
    (rank_dates_gen_df['brand'] == 'Apple') &
    (rank_dates_gen_df['monthly_sold'] >= 0)
]

rank_dates_sub_df = (ms_df.set_index('datetime')
    .groupby(['submodel_name', 'brand', 'generation_name'])
    .resample('W')['monthly_sold'].mean().reset_index())
rank_dates_sub_df['monthly_sold'] = rank_dates_sub_df.groupby('generation_name')['monthly_sold'].ffill()
iphone13_rank_dates_df = rank_dates_sub_df[rank_dates_sub_df['generation_name'] == 'iPhone 13']
"""))

# ── TITLE ─────────────────────────────────────────────────────────────────────
cells.append(md(
"""# Amazon Renewed Phone Price Analysis

This project looks at how the prices of refurbished smartphones decay after launch on Amazon US,
using historical price data from the Keepa API. The dataset covers Apple, Samsung and Google
across 63 submodels and roughly 878,000 weekly price records from 2019 to 2026.

The central question is pretty simple — once a phone hits the secondary market, how fast does
it lose value, and does it depend on the brand, the model tier, or the time of year?"""))

cells.append(md(
"""**a few notes on the data and methodology**

All prices here are for Renewed (refurbished) listings, not factory new. Apple phones on Amazon US
are exclusively sold by Renewed sellers, so for iPhones this dataset essentially captures the
full secondary market. Samsung and Google have both New and Renewed listings; where relevant,
the analysis separates them.

Launch prices were sourced manually from official press releases and represent the mean across
storage tiers — for example, iPhone 16 Pro ranged from $999 to $1,499 depending on storage,
so the reference price used here is $1,224. Carrier-locked variants were excluded since their
pricing dynamics differ slightly from unlocked units. Models launched very recently like the
iPhone 17 were also left out of decay charts due to not having enough price history to show
anythng meaningful yet."""))

# ── KPI ───────────────────────────────────────────────────────────────────────
cells.append(md("---\n# at a glance"))

cells.append(code(
"""kpi_data = [
    ['Price records', '878,267'],
    ['Brands', '3 (Apple, Samsung, Google)'],
    ['Generations tracked', str(df['generation_name'].nunique())],
    ['Years of data', '2019 - 2026'],
    ['Apple 1yr price retention', f'{round(apple_retention, 1)}%'],
    ['Samsung 1yr price retention', f'{round(samsung_retention, 1)}%'],
    ['Google 1yr price retention', f'{round(google_retention, 1)}%'],
    ['Renewed Premium premium', f'+{round(renewed_premium_premium, 1)} pp vs Renewed'],
]

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
table = ax.table(
    cellText=kpi_data,
    colLabels=['Metric', 'Value'],
    cellLoc='left',
    loc='center',
    colWidths=[0.45, 0.45]
)
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2.2)

for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#cccccc')
    if row == 0:
        cell.set_facecolor('#2c3e50')
        cell.set_text_props(color='white', fontweight='bold')
    elif row % 2 == 0:
        cell.set_facecolor('#f2f2f2')
    else:
        cell.set_facecolor('white')

plt.title('project overview', fontsize=14, pad=20)
plt.tight_layout()
plt.show()
"""))

# ── PRICE DECAY ───────────────────────────────────────────────────────────────
cells.append(md(
"""---\n# price decay analysis

Each chart below shows price as a percentage of the official launch price over time.
100% means the phone is still at its launch price on the Renewed market, 50% means it's
lost half its value. The x-axis shows days since launch so models can be compared at the
same point in their lifecycle regardless of when they were released."""))

cells.append(md("**all brands — base models combined**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_1d = sns.lineplot(data=all_brands_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='brand', ax=ax)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price decay — all base models by brand')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
plt.tight_layout()
plt.show()
"""))

cells.append(md(
"""Apple phones are the last to hit the 50% mark, getting there at around 900 days after launch.
Samsung reaches it at roughly 500 days, Google at around 420 days. Apple also has the highest
price floor, stabilising at 26-28% of launch price after about 2000 days — Samsung bottoms out
around 16-17% and Google around 20%."""))

cells.append(md(
"""**Apple — base models by generation**

iPhones on Amazon are sold as Renewed or Renewed Premium only. Solid lines are standard Renewed,
dashed lines are Renewed Premium. iPhone 17 is excluded — too little data at this point."""))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_1 = sns.lineplot(data=base_apple_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='generation_name', style='product_grade', ax=ax)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price decay — base iPhone models')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()
"""))

cells.append(md(
"""Renewed Premium consistently sits above the standard Renewed curve for the same generation.
The gap appears early and stays fairly stable throughout the lifecycle, which suggests buyers
pay a persistent condition premium regardless of how old the phone gets. The exact difference
varies by generation but averages around [TODO: fill renewed_premium_premium value] percentage points."""))

cells.append(md("**Samsung — base models by generation**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_1b = sns.lineplot(data=base_samsung_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='generation_name', ax=ax)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price decay — base Samsung models')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()
"""))

cells.append(md("**Google Pixel — base models by generation**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_1c = sns.lineplot(data=base_google_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='generation_name', ax=ax)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price decay — base Google Pixel models')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()
"""))

cells.append(md(
"""**within a generation — iPhone 13 submodels**

All tiers normalised to 100% at their own first recorded price, so you can compare decay
shape directly without the different launch prices distorting the picture."""))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_2 = sns.lineplot(data=iphone13_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='submodel_name', ax=ax)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price decay — iPhone 13 submodels')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
plt.tight_layout()
plt.show()
"""))

cells.append(md("[TODO: observation about which submodel holds value best within iPhone 13]"))

# ── BRAND COMPARISON ──────────────────────────────────────────────────────────
cells.append(md(
"""---\n# brand comparison at one year post-launch

Instead of looking at the full decay curve, this takes a snapshot at around 365 days after
launch and lines up all generations side by side. It's a cleaner way to answer which phones
hold their value best in the first year."""))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(14, 6))
order = retention_1yr_df['generation_name'].tolist()
pd_chart_7 = sns.barplot(data=retention_1yr_df, x='generation_name', y='price_retention',
    hue='brand', order=order, ax=ax)
ax.axhline(75, color='lightgray', linestyle='--', linewidth=1)
ax.axhline(50, color='lightgray', linestyle='--', linewidth=1)
ax.set_title('Price retention at ~1 year post-launch')
ax.set_xlabel('Generation')
ax.set_ylabel('Price retention (%)')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
"""))

cells.append(md(
"""iPhones dominate the top of the chart. The Pixel 5 stands out as an anomaly among Google phones —
it launched at a low price ($699) and Google discontinued it earlier than expected, which constrained
supply and kept its secondary market value unusually stable. Other Pixel models, which launched at
higher prices and remained available for longer, didn't benefit from that same scarcity effect."""))

# ── PRICE DISTRIBUTION ────────────────────────────────────────────────────────
cells.append(md(
"""---\n# price distribution across the full lifecycle

The decay curves show averages. This boxplot shows the full spread of weekly prices across
the entire recorded lifecycle for each brand — median, quartiles, and outliers. It gives
a sense of how much variation there is within each brand, not just where the average lands."""))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(8, 6))
pd_chart_8 = sns.boxplot(data=all_brands_decay_df, x='brand', y='price_pct_of_launch',
    hue='brand', ax=ax)
ax.set_title('Price distribution across full lifecycle by brand')
ax.set_xlabel('Brand')
ax.set_ylabel('Price as % of launch price')
plt.tight_layout()
plt.show()
"""))

cells.append(md("[TODO: observation about spread and median differences between brands]"))

# ── SALES RANK ────────────────────────────────────────────────────────────────
cells.append(md(
"""---\n# sales rank analysis

Amazon's monthly_sold metric is a rank position, not a unit count — lower means the product
is selling more. Keepa only started tracking this consistently from late 2023, so there's
roughly 1.5 years of data to work with. Limited, but enough to see some lifecycle patterns."""))

cells.append(md("**sales rank over the product lifecycle — base iPhones**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
ms_chart_3 = sns.lineplot(data=apple_base_rank_df, x='days_rounded', y='monthly_sold',
    hue='generation_name', ax=ax)
ax.invert_yaxis()
ax.set_title('Sales rank over time — base iPhones by generation (lower = more sold)')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Monthly sales rank')
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.show()
"""))

cells.append(md("[TODO: observation about lifecycle deterioration and any exceptions]"))

cells.append(md("**sales rank within a generation — iPhone 13 submodels**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(12, 6))
ms_chart_4 = sns.lineplot(data=iphone13_rank_df, x='days_rounded', y='monthly_sold',
    hue='submodel_name', ax=ax)
ax.invert_yaxis()
ax.set_title('Sales rank over time — iPhone 13 submodels (lower = more sold)')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Monthly sales rank')
plt.tight_layout()
plt.show()
"""))

cells.append(md(
"""The Pro Max appears to be the most popular submodel in the iPhone 13 lineup. A bit counterintuitive
at first — you'd expect the cheaper base model to sell more — but at this stage of the lifecycle
the Pro Max is deeply discounted from its $1,099 launch price and still offers the best hardware
of the generation. Buyers looking for a budget flagship will often go for the top tier once the
price is right."""))

cells.append(md(
"""**sales rank on real calendar dates — base iPhones**

Using actual dates rather than days since launch makes it possible to spot seasonal patterns.
Gray dotted lines mark the September iPhone launch window, orange is Black Friday, red is Christmas.
Data starts from late 2023, so there are only two seasonal cycles visible."""))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(14, 6))
ms_chart_5 = sns.lineplot(data=apple_base_rank_dates_df, x='datetime', y='monthly_sold',
    hue='generation_name', ax=ax)
ax.invert_yaxis()

launch_line = ax.axvline(pd.Timestamp('2023-09-15'), color='gray', linestyle='--', linewidth=1.5, alpha=0.6, label='iPhone Launch (Sep)')
bf_line = ax.axvline(pd.Timestamp('2023-11-25'), color='orange', linestyle='--', linewidth=1.5, alpha=0.6, label='Black Friday (Nov)')
xmas_line = ax.axvline(pd.Timestamp('2023-12-20'), color='red', linestyle='--', linewidth=1.5, alpha=0.6, label='Christmas (Dec)')
for year in range(2024, 2026):
    ax.axvline(pd.Timestamp(f'{year}-09-15'), color='gray', linestyle='--', linewidth=1.5, alpha=0.6)
    ax.axvline(pd.Timestamp(f'{year}-11-25'), color='orange', linestyle='--', linewidth=1.5, alpha=0.6)
    ax.axvline(pd.Timestamp(f'{year}-12-20'), color='red', linestyle='--', linewidth=1.5, alpha=0.6)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=labels, bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.set_title('Sales rank over time — base iPhones (real dates)')
ax.set_xlabel('Date')
ax.set_ylabel('Monthly sales rank')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""))

cells.append(md("[TODO: seasonal observation — any visible uptick in sales around BF/Christmas?]"))

cells.append(md("**iPhone 13 submodels on real calendar dates**"))

cells.append(code(
"""fig, ax = plt.subplots(figsize=(14, 6))
ms_chart_6 = sns.lineplot(data=iphone13_rank_dates_df, x='datetime', y='monthly_sold',
    hue='submodel_name', ax=ax)
ax.invert_yaxis()

ax.axvline(pd.Timestamp('2023-09-15'), color='gray', linestyle='--', linewidth=1.5, alpha=0.6, label='iPhone Launch (Sep)')
ax.axvline(pd.Timestamp('2023-11-25'), color='orange', linestyle='--', linewidth=1.5, alpha=0.6, label='Black Friday (Nov)')
ax.axvline(pd.Timestamp('2023-12-20'), color='red', linestyle='--', linewidth=1.5, alpha=0.6, label='Christmas (Dec)')
for year in range(2024, 2026):
    ax.axvline(pd.Timestamp(f'{year}-09-15'), color='gray', linestyle='--', linewidth=1.5, alpha=0.6)
    ax.axvline(pd.Timestamp(f'{year}-11-25'), color='orange', linestyle='--', linewidth=1.5, alpha=0.6)
    ax.axvline(pd.Timestamp(f'{year}-12-20'), color='red', linestyle='--', linewidth=1.5, alpha=0.6)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=labels, bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.set_title('Sales rank over time — iPhone 13 submodels (real dates)')
ax.set_xlabel('Date')
ax.set_ylabel('Monthly sales rank')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""))

# ── KEY FINDINGS ──────────────────────────────────────────────────────────────
cells.append(md(
"""---\n# key findings

- **Apple retains value best.** At the one-year mark, iPhones hold significantly more of their
  launch price than Samsung or Google. The 50% barrier comes around 900 days for Apple vs
  roughly 500 days for Samsung and 420 for Google.

- **Renewed Premium holds its value better than standard Renewed.** For iPhones the gap
  averages around [TODO: renewed_premium_premium] percentage points and stays fairly stable
  throughout the lifecycle — it's not just a launch-window premium.

- **The Pixel 5 is an anomaly.** It outperforms every other Google model at the one-year mark.
  Low launch price plus early discontinuation created supply constraints that kept its
  secondary market value elevated longer than expected.

- **Older flagships attract buyers looking for the best hardware at a discount.** The iPhone 13
  Pro Max shows stronger sales rank than cheaper submodels of the same generation, suggesting
  people actively seek out the top tier once the price drops to a reasonable level.

- **Seasonal sales data is limited.** The monthly_sold metric only covers from late 2023,
  making it hard to draw firm conclusions about Black Friday or Christmas effects. There are
  hints of demand improvement around the holiday window but more history is needed to say
  anything with confidence."""))

nb_out = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.12.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

out_path = "notebooks/06_final_project_sns.ipynb"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(nb_out, f, indent=1, ensure_ascii=False)

print(f"Written: {out_path}")
print(f"Cells: {len(cells)}")
