# Project 1 — Amazon Phone Price Analysis

Portfolio analysis of iPhone / Samsung / Google Pixel price decay on Amazon after launch.
Data source: Keepa API export (19 ASINs, renewed/refurbished listings, Amazon US).

## Structure
```
notebooks/   — Jupyter notebooks (01_exploration, 02_cleaning, 03_analysis, 04_viz)
data/        — raw Keepa CSV exports (gitignored)
```

## Data — Keepa API quirks

1. ### Timestamps: `listedSince`, `trackingSince`
Raw values are integers — they look like Unix timestamps but they are not.
Keepa uses its own epoch: **minutes elapsed since 2011-01-01 00:00 UTC**.

Conversion:
```python
KEEPA_EPOCH = pd.Timestamp("2011-01-01")
meta["listed_since"] = KEEPA_EPOCH + pd.to_timedelta(meta["listedSince"], unit="min")
```

Applying standard Unix conversion (seconds since 1970-01-01) produces nonsensical dates in the 1970s — this is the trap. Always check the Keepa API docs before assuming timestamp format.

2. ### `listedSince` vs `trackingSince` gap
`listedSince` is when the product appeared on Amazon. `trackingSince` is when Keepa started collecting data — always later, sometimes by weeks or months.
Price history before `trackingSince` does not exist. For price decay analysis anchored to launch date, this gap must be accounted for — products with a large gap have incomplete early-price data and may skew decay curves.

Observed gaps (from exploration): range from -55 to +101 days.
- Large positive gap (e.g. Samsung S22+ 101d, iPhone 13 63d): significant missing early-price window.
- Negative gap (e.g. Pixel 9a -55d, Galaxy S25 FE -42d): Keepa tracked the listing before it went live — pre-release tracking. `listedSince` here likely reflects first availability, not first appearance in Keepa.

3. ### Prices
Raw price columns were supposed to be integers, which should be divided by 100 to get the real price, but it doesn't seem like it.

4. `monthly_sold`
This is **sales rank position**, not unit count. Lower value = more sold.
Cannot be used as absolute volume, only useful for relative comparisons.
I chose not to use it for now.

5. NaN values after I resampled data to show min prices for each week for each model.

It seems like there are some missing price points, and the granularity of our data is not perfect.
There are exactly 72 missing price points from 3062 rows, totaling to about 2.5% of values missing.
It's not that big of a deal and it shouldn't affect the results much. 

I was thinking about using mean of the prev/next rows to deal with that, but then I thought a NaN value
could as well the price is not changing, so I decided to use ffill carefully (to make sure it's taken from the same asin)


