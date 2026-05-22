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
