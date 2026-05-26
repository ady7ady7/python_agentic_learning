# Case Study — Data Issues & Solutions

A log of real problems encountered during analysis and how they were resolved.
Useful as portfolio evidence of analytical thinking and problem-solving.

---

## Issue 1 — Plotly multi-line chart "shadow" artifacts

When plotting price decay curves with color by brand, Plotly rendered filled shadow areas
between lines instead of clean separate lines. The cause was that different phone models
within a brand had price data recorded at different `days_since_launch` values — uneven
gaps across models. Plotly interpolates between misaligned x-axis points and fills the
area as a side effect.

Fix: round `days_since_launch` to the nearest 7 (weekly grid) before aggregating by brand.
This aligns all models to the same x-axis positions.

```python
df["days_rounded"] = (df["days_since_launch"] / 7).round() * 7
brand_decay = df.groupby(["brand", "days_rounded"])["price_pct_of_launch"].mean().reset_index()
```

Unique x-axis values dropped from ~1069 to ~334. Shadows gone, chart clean.

---

## Issue 2 — Keepa timestamp format

`listedSince` and `trackingSince` columns look like Unix timestamps but produce dates in
the 1970s when treated as such. Keepa uses its own epoch: minutes elapsed since
2011-01-01 00:00 UTC, not seconds since 1970-01-01.

```python
KEEPA_EPOCH = pd.Timestamp("2011-01-01")
df["listed_since"] = KEEPA_EPOCH + pd.to_timedelta(df["listedSince"], unit="min")
```

---

## Issue 3 — Tracking gap between listedSince and trackingSince

For some products, Keepa started tracking weeks or months after the product was listed on
Amazon, meaning early price history is missing. The observed range was -55 to +101 days.
A positive gap means the early-price window is missing (e.g. Samsung S22+ 101 days,
iPhone 13 63 days). A negative gap means Keepa was tracking before the product went live.

Price decay curves anchored to launch date are incomplete for models with large positive
gaps. Samsung S22+ is the most affected in this dataset.

---

## Issue 4 — Event-based price history structure

Each row in `_price_history.csv` records only one changed value — all other columns are
NaN. It can't be read as a standard time series directly. The fix is to filter to rows
where the target column is not null, resample to weekly minimum per ASIN, then
forward-fill gaps within each ASIN.

```python
df = df[df["NEW"].notna()]
df = df.set_index("datetime")
df = df.groupby("asin").resample("W")["NEW"].min().reset_index()
df["NEW"] = df.groupby("asin")["NEW"].ffill()
```

ffill rather than interpolation because prices move in discrete jumps. A missing week
most likely means the price didn't change, not that it was mid-transition.

---

## Issue 5 — Initial dataset contained only 19 probe ASINs

The first CSV export contained only 19 ASINs — one per submodel. When seasonal analysis
was attempted in Week 3, it produced only 12 rows across 3 brands, which is worthless
for any interpretation.

The harvester uses a `probe_asin` per submodel to fetch all variants from the Keepa API.
The export was built from those probe ASINs only, not the full `keepa.products` table
which had 893 ASINs across 60 submodels.

Fix: re-exported directly from PostgreSQL with a full JOIN across
`keepa.generations → keepa.submodels → keepa.products → keepa.price_history`.
Carrier-locked variants excluded (Verizon, AT&T, T-Mobile, Cricket, Tracfone, Boost Mobile)
— 15k rows out of 893k lost (1.7%), acceptable for cleaner data.

```python
df = pd.read_sql(price_query, engine, params={"carrier_grades": CARRIER_GRADES})
```

Dataset grew from 19 ASINs / ~170k rows to 893 ASINs / 878k rows. Seasonal analysis
expanded from 12 to 36 rows with full 12-month coverage per brand.

---

## Issue 6 — dt.month extracted from wrong column in seasonal analysis

The seasonal MoM analysis grouped by month, but month was computed from `listed_since`
(a fixed date per ASIN — the Amazon listing date) instead of `datetime` (the actual
price observation date). Every row for a given ASIN got the same month, so the groupby
was measuring which month phones were listed, not when prices actually moved.

```python
df['month'] = df['datetime'].dt.month  # not df['listed_since'].dt.month
```

Caught and fixed within the same session.

---

## Issue 7 — agg('first') unreliable as a launch price proxy

Using `groupby('model').agg('first')` on `new_price` to estimate launch price produced
apparent drops of 40–60% within the first 90 days for several models (iPhone 11 Pro,
iPhone 12 Pro Max, Pixel 6 Pro, Galaxy S21 FE, others). These numbers looked suspicious.

The cause is the tracking gap from Issue 3 — the first price Keepa recorded is often
weeks or months after actual launch. If early-market prices were elevated and then
normalized, `agg('first')` captures an inflated starting point, making the drop look
steeper than it was. The first-90-days decay velocity analysis is unreliable for models
with large tracking gaps and should be treated as a lower bound, not as true launch price.

---

## Issue 8 — monthly_sold chart unreadable at both brand and submodel level

Aggregating `monthly_sold` by brand over time gives a flat, featureless chart — too much
averaging across models at wildly different lifecycle stages. Going the other direction
and plotting by submodel gives 60+ colored lines that are completely unreadable.

The underlying issue is that `monthly_sold` is a sales rank snapshot, not a unit count.
Ranks are only comparable within a group at similar ages. Mixing a phone at day 10
post-launch with one at day 800 in the same mean distorts everything. The next attempt
is filtering to a single brand with enough data coverage and plotting one line per
generation — results pending.

---

## Issue 9 — Tracking gap causes submodel price curves to start mid-decay

When computing `price_pct_of_launch` per submodel, higher-tier models (Pro, Pro Max, Ultra)
frequently have tracking gaps of 100-200+ days. This means their first recorded price is
already well into the decay curve, not at launch. The result: Pro/Pro Max lines appear to
start at 50% or lower on the chart, which looks like a data error but is actually a
coverage gap.

Confirmed for iPhone 13 submodels:

| Submodel | First recorded | Premiere | Gap (days) |
|---|---|---|---|
| iPhone 13 Mini | 2021-12-12 | 2021-11-10 | 31 |
| iPhone 13 | 2022-03-06 | 2021-11-11 | 114 |
| iPhone 13 Pro Max | 2022-04-24 | 2021-11-11 | 163 |
| iPhone 13 Pro | 2022-06-12 | 2021-11-11 | 212 |

The fix for `price_pct_of_launch` is to group by `submodel_name` instead of `model`
so each submodel normalizes against its own first recorded price, not the base model's.
The ultimate fix — implemented in Week 4 — was to source official launch prices externally
(see Issue 10) and use `official_premiere_date` as the day 0 anchor, making the tracking
gap a display issue rather than a normalization error.

---

## Issue 10 — Using Keepa's premiere_date and first recorded price as launch anchors

`premiere_date` in the database reflects when Keepa first associated a product with a
generation, not the actual public launch date. Similarly, the first recorded price is
whatever Keepa captured when it started tracking — often weeks or months after the real
launch, and at a price level that may already reflect post-launch normalization.

This made `price_pct_of_launch` unreliable: curves were anchored to arbitrary start points,
some models appeared to begin at 50-60% of their own "launch price", and
`days_since_launch` was measured from the wrong origin.

Fix: compiled a reference table (`official_launch_prices.csv`) with real premiere dates
and official retail prices per submodel, sourced from Apple/Samsung/Google press releases.
These replace Keepa's premiere_date and first_price in all decay calculations:

```python
launch_ref = pd.read_csv('../data/official_launch_prices.csv')
df = df.merge(launch_ref, on='submodel_name', how='left')
df['days_since_launch'] = (df['datetime'] - df['official_premiere_date']).dt.days
df['price_pct_of_launch'] = round(df['NEW'] / df['official_launch_price'] * 100, 1)
```

Result: decay curves now correctly start near 100% for most submodels. The remaining
gap (curves starting at e.g. 80% rather than 100%) reflects real Renewed market pricing
at the time Keepa first recorded the product — not a data error.

---

## Issue 11 — Launch price varies by storage size; mean used as proxy

Official retail prices differ significantly by storage tier. For example, iPhone 16 Pro
ranged from $999 (128GB) to $1,499 (1TB). Since the dataset mixes storage sizes within
each submodel and the analysis aggregates across all variants, using a single storage
tier's price as the launch anchor would skew results depending on which variant happened
to be tracked first.

Approach: use the mean of all official storage-tier prices per submodel as
`official_launch_price`. For iPhone 16 Pro: ($999 + $1,099 + $1,299 + $1,499) / 4 = $1,224.

This is a conscious simplification. It slightly underrepresents premium configurations
and overrepresents base configurations, but is more representative than picking any single
tier. The limitation is noted in the methodology.

---

## Issue 12 — Very recently launched models produce unstable decay curves

Models launched within the last few months (e.g. iPhone 17, Galaxy S25 Edge) have very
few price observations. Random outliers or a single elevated early price can spike
`price_pct_of_launch` well above 100% or produce erratic curves with large swings.

These models should either be excluded from decay analysis or clearly flagged as
"insufficient data" in the visualization. A practical threshold: exclude submodels with
fewer than ~10 weekly price observations after resampling.
