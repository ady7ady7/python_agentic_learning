# Project 1 — Amazon Phone Price Analysis

Portfolio analysis of iPhone / Samsung / Google Pixel price decay on Amazon after launch.
Data source: Keepa API export (19 ASINs, renewed/refurbished listings, Amazon US).

## Structure
```
notebooks/   — Jupyter notebooks (01_exploration, 02_cleaning, 03_analysis, 04_viz)
data/        — raw Keepa CSV exports (gitignored)
```

## Data — Keepa API quirks

### Timestamps: `listedSince`, `trackingSince`
Raw values are integers — they look like Unix timestamps but they are not.
Keepa uses its own epoch: **minutes elapsed since 2011-01-01 00:00 UTC**.

Conversion:
```python
KEEPA_EPOCH = pd.Timestamp("2011-01-01")
meta["listed_since"] = KEEPA_EPOCH + pd.to_timedelta(meta["listedSince"], unit="min")
```

Applying standard Unix conversion (seconds since 1970-01-01) produces nonsensical dates in the 1970s — this is the trap. Always check the Keepa API docs before assuming timestamp format.

### `listedSince` vs `trackingSince` gap
`listedSince` is when the product appeared on Amazon. `trackingSince` is when Keepa started collecting data — always later, sometimes by weeks or months.
Price history before `trackingSince` does not exist. For price decay analysis anchored to launch date, this gap must be accounted for — products with a large gap have incomplete early-price data and may skew decay curves.

Observed gaps (from exploration): range from -55 to +101 days.
- Large positive gap (e.g. Samsung S22+ 101d, iPhone 13 63d): significant missing early-price window.
- Negative gap (e.g. Pixel 9a -55d, Galaxy S25 FE -42d): Keepa tracked the listing before it went live — pre-release tracking. `listedSince` here likely reflects first availability, not first appearance in Keepa.

### Prices
Raw price columns are integers — divide by 100 to get USD.
Example: `34999` → `$349.99`

### `monthly_sold`
This is **sales rank position**, not unit count. Lower value = more sold.
Cannot be used as absolute volume — only useful for relative comparisons.
