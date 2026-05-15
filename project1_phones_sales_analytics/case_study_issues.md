# Case Study — Data Issues & Solutions

A log of real problems encountered during analysis and how they were resolved.
Useful as portfolio evidence of analytical thinking and problem-solving.

---

## Issue 1 — Plotly multi-line chart "shadow" artifacts

**Problem:** When plotting price decay curves with color by brand, Plotly rendered filled
shadow areas between lines instead of clean separate lines.

**Root cause:** Different phone models within a brand had price data recorded at different
`days_since_launch` values — uneven gaps across models. Plotly interpolates between
misaligned x-axis points and renders filled areas as a side effect.

**Solution:** Round `days_since_launch` to the nearest 7 (weekly grid) before aggregating
by brand. This aligns all models to the same x-axis positions.

```python
df["days_rounded"] = (df["days_since_launch"] / 7).round() * 7
brand_decay = df.groupby(["brand", "days_rounded"])["price_pct_of_launch"].mean().reset_index()
```

**Result:** Unique x-axis values reduced from ~1069 → ~334. Shadows eliminated, chart clean.

---

## Issue 2 — Keepa timestamp format

**Problem:** `listedSince` and `trackingSince` columns appear to be integers — look like
Unix timestamps but produce dates in the 1970s when treated as such.

**Root cause:** Keepa uses its own epoch: minutes elapsed since 2011-01-01 00:00 UTC,
not seconds since 1970-01-01 (Unix standard).

**Solution:**
```python
KEEPA_EPOCH = pd.Timestamp("2011-01-01")
df["listed_since"] = KEEPA_EPOCH + pd.to_timedelta(df["listedSince"], unit="min")
```

---

## Issue 3 — Tracking gap between listedSince and trackingSince

**Problem:** For some products, Keepa started tracking weeks or months after the product
was listed on Amazon. This means early price history is missing.

**Observed range:** -55 to +101 days gap.
- Positive gap: missing early-price window (e.g. Samsung S22+ 101 days, iPhone 13 63 days)
- Negative gap: pre-release tracking — Keepa tracked before product went live

**Impact:** Price decay curves anchored to launch date may be incomplete for products
with large positive gaps. Samsung S22+ is most affected.

---

## Issue 4 — Event-based price history structure

**Problem:** Each row in `_price_history.csv` records only one changed value — all other
columns are NaN. Cannot be read as a standard time series directly.

**Solution:** Filter to rows where the target column (`NEW`) is not null, resample to
weekly minimum per ASIN, then forward-fill gaps within each ASIN.

```python
df = df[df["NEW"].notna()]
df = df.set_index("datetime")
df = df.groupby("asin").resample("W")["NEW"].min().reset_index()
df["NEW"] = df.groupby("asin")["NEW"].ffill()
```

**Why ffill and not interpolation:** Prices are discrete jumps, not gradients.
A missing week most likely means the price didn't change, not that it was mid-transition.
