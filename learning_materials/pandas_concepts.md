# Pandas Concepts Reference

A practical reference built session by session. Each entry is written as a real task or question,
not a method name. Use the ToC to find what you need, then go to the section for the pattern.

---

## Table of Contents

- [How do I load a CSV file into a DataFrame and get a first look at the data?](#1-loading-and-inspecting-data) — `read_csv`, `head`, `info`, `shape` — line 30
- [How do I convert raw integer timestamps to real human-readable dates?](#2-converting-timestamps) — `pd.to_timedelta` + epoch offset — line 65
- [How do I calculate a new column based on the difference between two datetime columns?](#3-datetime-arithmetic) — datetime subtraction + `.dt.days` — line 95
- [How do I load multiple CSV files matching a pattern into one combined DataFrame?](#4-loading-multiple-csvs) — `os.listdir` + loop + `pd.concat` — line 122
- [How do I get the lowest price per week per group (e.g. per ASIN) from an irregular time series?](#5-groupby-resample-aggregation) — `groupby` + `resample` + `reset_index` + `ffill` — line 155
- [How do I combine two DataFrames on a shared column to add metadata to a time series?](#6-merging-dataframes) — `df.merge` — line 169
- [How do I add a column with a per-group statistic (e.g. median per ASIN) aligned to the full DataFrame?](#7-groupby-transform) — `groupby` + `transform` — line 200
- [How do I compute multiple aggregations at once per group (e.g. min, max, first, last price per month)?](#8-groupby-agg) — `groupby` + `agg` with named aggregations — line 248
- [How do I calculate week-over-week price changes and find the largest single-period move?](#9-diff-and-abs) — `diff` + `abs` + `groupby` — line 285
- [How do I aggregate a metric across two grouping columns (e.g. mean price per brand per week)?](#10-groupby-multiple-keys) — `groupby([col1, col2])` + `mean` — line 320
- [How do I sort a Seaborn chart's x-axis by a computed statistic (e.g. median value)?](#11-seaborn-order-by-statistic) — compute stat + sort + pass to `order=` — line 348
- [How do I group a numeric column into fixed-width buckets (e.g. every 50 days)?](#12-pd-cut-binning) — `pd.cut` — line 385
- [How do I regularize irregular time series data to fixed intervals to eliminate chart artifacts?](#13-regularize-time-series) — round to nearest N + groupby mean — line 415

---

## 1. Loading and Inspecting Data

**What it does:** Reads a CSV from disk into a DataFrame. Inspection methods give you a quick structural overview — shape, column types, null counts.

**Pattern:**
```python
df = pd.read_csv("path/to/file.csv")

df.shape        # (rows, columns)
df.head()       # first 5 rows
df.info()       # column names, dtypes, non-null counts
df.describe()   # basic stats for numeric columns
```

**Example:**
```
Input: CSV with 19 rows, columns: asin, brand, model, listedSince

df.shape   → (19, 4)
df.head()  → first 5 rows of the table
df.info()  → asin        19 non-null  object
             brand       19 non-null  object
             listedSince 19 non-null  int64
```

**Gotchas:**
- `df.info()` shows non-null counts — use it to spot missing data at a glance before doing anything else.
- `df.describe()` only covers numeric columns by default; pass `include="all"` to include strings.

---

## 2. Converting Timestamps

**What it does:** Converts integer timestamps in a non-standard format (e.g. Keepa minutes since 2011-01-01) into proper `datetime` objects you can work with.

**Pattern:**
```python
EPOCH = pd.Timestamp("2011-01-01")
df["date_col"] = EPOCH + pd.to_timedelta(df["raw_int_col"], unit="min")
```

**Example:**
```
Input:  listedSince = 4,706,827  (minutes since 2011-01-01)

EPOCH + pd.to_timedelta(4_706_827, unit="min")
→ 2019-10-28 07:07:00
```

**Gotchas:**
- Keepa uses **minutes since 2011-01-01**, not Unix seconds since 1970-01-01. Applying standard Unix conversion produces dates in the 1970s — always check API docs before assuming timestamp format.
- `unit="min"` for minutes, `unit="s"` for seconds, `unit="ms"` for milliseconds.

---

## 3. Datetime Arithmetic

**What it does:** Subtracts two datetime columns to get a duration, then extracts it as an integer number of days (or other units).

**Pattern:**
```python
df["gap_days"] = (df["end_date_col"] - df["start_date_col"]).dt.days
```

**Example:**
```
Input:
  listed_since    = 2021-11-11
  tracking_since  = 2022-01-13

(tracking_since - listed_since).dt.days → 63
```

**Gotchas:**
- Subtraction of two datetime columns gives a `Timedelta` Series, not an integer. You need `.dt.days` to extract the numeric value.
- Negative values are valid — they mean tracking started before the listed date (e.g. pre-release Keepa tracking).

---

## 4. Loading Multiple CSVs into One DataFrame

**What it does:** Iterates over files in a folder, filters by name pattern, loads each into a DataFrame, and stacks them all vertically into one combined DataFrame.

**Pattern:**
```python
import os
import pandas as pd

dfs = []
for file in os.listdir("path/to/folder"):
    if "pattern" in file:
        dfs.append(pd.read_csv(os.path.join("path/to/folder", file)))

df = pd.concat(dfs, ignore_index=True)
```

**Example:**
```
Files in folder:
  B09LNW3CY2_price_history.csv   (18174 rows)
  B08PP5MSVB_price_history.csv   (9103 rows)
  ...19 files total

pd.concat(dfs)  →  DataFrame with 170608 rows, all ASINs combined
```

**Gotchas:**
- Use a list + single `pd.concat` at the end, not `pd.concat` inside the loop. Concatenating inside a loop rebuilds the entire DataFrame on every iteration — slow on large data.
- `ignore_index=True` resets the index to 0…n. Without it you get duplicate index values from each file.
- `os.listdir` gives no guaranteed order — if order matters, sort the list first.

---

## 5. Groupby + Resample: Lowest Value per Week per Group

**What it does:** Takes an irregular time series (event-based, not one row per day), groups by a category (e.g. ASIN), then buckets into weekly intervals and aggregates. Forward-fills weeks with no events.

**Pattern:**
```python
# Step 1 — filter to rows where the target column has a value
df = df[df["value_col"].notna()]

# Step 2 — datetime index required for resample
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.set_index("datetime")

# Step 3 — group by category, resample weekly, aggregate
df = df.groupby("group_col").resample("W")["value_col"].min().reset_index()

# Step 4 — forward fill empty weeks within each group
df["value_col"] = df.groupby("group_col")["value_col"].ffill()
```

**Example:**
```
Input: 170608 rows, event-based, NEW column has 51588 non-null values across 19 ASINs

After filter + resample("W").min():  3062 rows  (one per ASIN per week)
After ffill:                         3062 rows, 0 NaN in NEW
```

**Gotchas:**
- `resample` requires a datetime **index**, not a regular column — `set_index` first.
- `groupby("asin").resample("W")["col"].min()` produces a **multi-level index** (asin + datetime). Call `reset_index()` immediately after to get a flat DataFrame with regular columns.
- `df.groupby("asin").ffill()` drops the groupby key column from output — instead use `df["col"] = df.groupby("asin")["col"].ffill()` to fill in place and keep all columns.
- `ffill()` carries the last known value forward — correct for price data (price didn't change, just no event recorded). Don't use interpolation — prices are discrete jumps, not gradients.

---

## 6. Merging DataFrames on a Shared Column

**What it does:** Combines two DataFrames horizontally by matching rows on a shared key column — like a SQL JOIN. Used to enrich a time series with metadata (e.g. adding brand/model to price rows).

**Pattern:**
```python
merged = df.merge(meta_df, on="key_col")
# default is inner join — only keeps rows where key exists in both DataFrames
```

**Example:**
```
prices (3062 rows):         meta (19 rows):
  asin   datetime   NEW       asin        brand   model
  B09... 2022-01-10 729.99    B09...      Apple   iPhone 13
  B09... 2022-01-17 729.99    B07...      Apple   iPhone 11
  ...                         ...

merged = prices.merge(meta, on="asin")

Result (3062 rows):
  asin   datetime   NEW    brand  model      listed_since
  B09... 2022-01-10 729.99 Apple  iPhone 13  2021-11-11
  B09... 2022-01-17 729.99 Apple  iPhone 13  2021-11-11
```

**Gotchas:**
- Default join is **inner** — rows with a key that exists in only one DataFrame are dropped silently. If you lose rows unexpectedly, check for key mismatches with `df["asin"].isin(meta["asin"]).all()`.
- If the meta DataFrame has duplicate keys, every match multiplies — a 3062-row DataFrame merged against meta with 2 rows per ASIN would produce 6124 rows. Always verify `merged.shape[0] == original.shape[0]` after merging one-to-many.
- Use `how="left"` to keep all rows from the left DataFrame even if no match exists in the right.

## 7. Groupby + Transform: Per-Group Statistics Aligned to Full DataFrame

**What it does:** Computes a statistic (e.g. median, mean) per group and returns a Series with the same length as the original DataFrame — so you can assign it directly as a new column. Unlike `groupby().agg()`, it doesn't collapse rows.

**Pattern:**
```python
df["col_median"] = df.groupby("group_col")["value_col"].transform("median")
```

**Example:**
```
Input:
  asin        NEW
  B09...      729.99
  B09...      699.99
  B07...      649.99
  B07...      629.99

df["median"] = df.groupby("asin")["NEW"].transform("median")

Result:
  asin        NEW     median
  B09...      729.99  714.99   ← median of B09... rows only
  B09...      699.99  714.99
  B07...      649.99  639.99   ← median of B07... rows only
  B07...      629.99  639.99
```

**Gotchas:**
- `transform` returns a Series aligned to the original index — this is what makes it assignable as a new column. `agg` returns one row per group, which can't be assigned directly.
- Common aggregation strings: `"median"`, `"mean"`, `"std"`, `"max"`, `"min"`, `"first"`, `"last"`.
- Use case: outlier detection — `df["is_outlier"] = df["NEW"] > df.groupby("asin")["NEW"].transform("median") * 3`.

---

## 8. Groupby + Agg: Multiple Aggregations Per Group

**What it does:** Computes several statistics at once per group and collapses to one row per group. Unlike `transform`, the result is a summary DataFrame — not aligned to the original.

**Pattern:**
```python
summary = df.groupby("group_col")["value_col"].agg(
    first_price="first",
    last_price="last",
    min_price="min",
    max_price="max"
).reset_index()
```

**Example:**
```
Input: all_iphones_df grouped by model, monthly

summary = all_iphones_df.groupby(["model", "month"])["NEW"].agg(
    min_price="min",
    max_price="max",
    first_price="first",
    last_price="last"
).reset_index()

Result: one row per model per month, with 4 price stats columns
```

**Gotchas:**
- `agg` collapses rows — result has one row per group, not one row per original row. Use `transform` if you need the result aligned back to the full DataFrame.
- Named aggregations syntax: `output_col_name="aggregation_string"` — clean and readable.
- `"first"` / `"last"` depend on row order — sort by the relevant column first if order matters.
- To aggregate multiple columns at once: `df.groupby("group")[["col1", "col2"]].agg(...)`.

---

## 9. Week-over-Week Changes: diff + abs

**What it does:** Computes the difference between consecutive rows (e.g. price change from one week to the next). Combined with `groupby` to stay within each group, and `abs()` to get magnitude regardless of direction.

**Pattern:**
```python
# Week-over-week change within each group
df["weekly_change"] = df.groupby("group_col")["value_col"].diff()

# Largest absolute change per group
df["weekly_change_abs"] = df.groupby("group_col")["value_col"].diff().abs()
summary["max_move"] = df.groupby("group_col")["weekly_change_abs"].max()
```

**Example:**
```
Input: iPhone 13 weekly NEW prices
  week 1: 729.99
  week 2: 699.99
  week 3: 729.99

diff()     → NaN, -30.0, +30.0
diff().abs()→ NaN, 30.0, 30.0
max()      → 30.0  (largest single-week move)
```

**Gotchas:**
- First row in each group is always NaN after `diff()` — no previous row to compare against.
- `diff()` gives signed values (negative = drop, positive = rise). Use `.abs()` if you want magnitude only.
- Always apply within `groupby` — without it, `diff()` bleeds across group boundaries (last row of one ASIN compared to first row of next).

---

## 10. Groupby on Multiple Keys: Aggregate Across Two Dimensions

**What it does:** Groups by two columns simultaneously and computes a statistic per unique combination. Used when you want e.g. mean price per brand per time period — one row per brand+period pair.

**Pattern:**
```python
result = df.groupby(["group_col1", "group_col2"])["value_col"].mean().reset_index()
```

**Example:**
```
Input: df with columns brand, days_since_launch, price_pct_of_launch (one row per model per week)

brand_decay = df.groupby(["brand", "days_since_launch"])["price_pct_of_launch"].mean().reset_index()

Result: one row per brand per days_since_launch value
  brand    days_since_launch  price_pct_of_launch
  Apple    6                  100.0
  Apple    13                 98.9
  Samsung  7                  99.1
  ...
```

**Gotchas:**
- When passing to `px.line`, always use the DataFrame + column name syntax: `px.line(df, x="col1", y="col2", color="col3")` — not `px.line(x=df["col1"], ...)`. The second form loses grouping context and causes visual artifacts (shadows, incorrect lines).
- Irregular spacing in the grouped result (not every day_since_launch appears for every brand) can cause jagged lines in Plotly. Resampling to regular intervals before grouping fixes this.

---

## 11. Seaborn: Sort Chart Axis by a Computed Statistic

**What it does:** Controls the order of categories on a Seaborn chart axis by computing a statistic (e.g. median) per category, sorting it, and passing the sorted list to the `order` parameter.

**Pattern:**
```python
# Step 1 — compute the statistic per category
order_df = df.groupby("category_col")["value_col"].median().reset_index()

# Step 2 — sort by statistic
order_df = order_df.sort_values("value_col", ascending=False)

# Step 3 — pass sorted category list to order=
sns.boxplot(df, x="category_col", y="value_col", order=order_df["category_col"])
```

**Example:**
```
Brands sorted by median price_pct_of_launch (descending):
  Apple    72.3
  Google   58.1
  Samsung  54.7

sns.boxplot(selected_df, x="brand", y="price_pct_of_launch", order=["Apple", "Google", "Samsung"])
→ Apple on left (highest retention), Samsung on right
```

**Gotchas:**
- Without `order=`, Seaborn sorts categories alphabetically — rarely what you want for analytical charts.
- `order` takes a list or Series of category values, not a DataFrame — pass `order_df["category_col"]`, not `order_df`.
- Add title with `ax.set_title("...")` where `ax` is the return value of `sns.boxplot(...)`.

---

## 12. Binning a Numeric Column into Fixed-Width Buckets

**What it does:** Splits a continuous numeric column into discrete intervals (bins) of fixed width. Each value gets assigned to a bucket label like `(0, 50]`, `(50, 100]` etc. Useful for grouping time or price ranges for aggregation or visualization.

**Pattern:**
```python
df["bucket_col"] = pd.cut(df["numeric_col"], bins=range(start, stop, step))

# Then group by the bucket
summary = df.groupby("bucket_col")["value_col"].mean().reset_index()
```

**Example:**
```
Input: days_since_launch values: 6, 13, 62, 110, 355 ...

df["days_bucket"] = pd.cut(df["days_since_launch"], bins=range(0, 2400, 50))

Result:
  days_since_launch   days_bucket
  6                   (0, 50]
  13                  (0, 50]
  62                  (50, 100]
  110                 (100, 150]
  355                 (350, 400]
```

**Gotchas:**
- Values outside the bin range become NaN — make sure `stop` covers your max value.
- `pd.cut` produces an ordered Categorical dtype — Seaborn respects this order automatically, so you don't need to pass `order=` manually.
- Each bin is left-open, right-closed by default: `(0, 50]` includes 50 but not 0.
- Use `pd.cut` for equal-width bins. Use `pd.qcut` for equal-frequency bins (same number of rows per bucket).

---

## 13. Regularizing Irregular Time Series to Fixed Intervals

**What it does:** When different groups (e.g. ASINs) have price data recorded at slightly different days, rounding to the nearest fixed interval (e.g. 7 days) aligns them to the same x-axis points. This eliminates visual artifacts (shadows, jagged interpolation) in line charts.

**Pattern:**
```python
# Round to nearest N days
df["days_rounded"] = (df["days_since_launch"] / N).round() * N

# Then aggregate per group + rounded interval
result = df.groupby(["group_col", "days_rounded"])["value_col"].mean().reset_index()
```

**Example:**
```
Before rounding: days_since_launch has 1069 unique values (irregular gaps per ASIN)
After rounding to 7: days_rounded has 334 unique values (aligned to weekly grid)

→ All brands now have data at the same x positions
→ px.line connects clean dots, no interpolation artifacts
```

**Gotchas:**
- Rounding merges nearby data points into one bucket — you lose some granularity but gain visual clarity. For analysis this trade-off is almost always worth it.
- Always aggregate (mean/median) after rounding — don't just rename the column, or you'll have duplicate x values per group.
- This is a lightweight alternative to `resample` when you don't need the full time-series machinery.

