# Data Schema & Examples

All raw data lives in `data/` (gitignored). This file documents structure and real examples for each file type.

---

## 1. `all_products_meta.csv` — one row per ASIN

| Column | Type | Description |
|---|---|---|
| asin | string | Amazon product ID |
| title | string | Full product title |
| brand | string | Apple / Samsung / Google |
| model | string | e.g. iPhone 13, Galaxy S22+ |
| manufacturer | string | Usually same as brand |
| productGroup | string | e.g. Wireless |
| binding | string | e.g. Electronics |
| color | string | e.g. Black, Midnight |
| size | string | Storage size e.g. 128GB |
| monthlySold | int | Sales rank bucket (NOT units sold) |
| listedSince | int | **Keepa minutes since 2011-01-01** — convert before use |
| trackingSince | int | **Keepa minutes since 2011-01-01** — when Keepa started tracking |
| rootCategory | int | Keepa category ID |
| parentAsin | string | Parent ASIN (often null — not useful for analysis) |

**Example row:**
```
asin:         B09LNW3CY2
title:        Apple iPhone 13, 128GB, Midnight - Unlocked (Renewed)
brand:        Apple
model:        iPhone 13
color:        Midnight
size:         128GB
listedSince:  5808056  →  2021-11-11 after conversion
trackingSince:5808056  →  2022-01-13 after conversion
```

---

## 2. `{ASIN}_price_history.csv` — event-based price snapshots

Each row records a **change** in one value. All other columns are NaN for that row.

| Column | Type | Description |
|---|---|---|
| datetime | string | Timestamp of the change event |
| asin | string | Amazon product ID |
| AMAZON | float | Amazon direct price (almost always null for Renewed) |
| NEW | float | New/Renewed seller price — **main column for analysis** |
| USED | float | Used seller price |
| SALES | float | Sales rank at that moment |
| LISTPRICE | float | Manufacturer list price (rarely populated) |
| REFURBISHED | float | Refurbished seller price |
| COUNT_NEW | float | Number of new offers |
| COUNT_USED | float | Number of used offers |
| COUNT_REFURBISHED | float | Number of refurbished offers |
| EBAY_NEW_SHIPPING | float | eBay new price incl. shipping |
| EBAY_USED_SHIPPING | float | eBay used price incl. shipping |

**Key quirk — event-based structure:**
```
datetime              NEW     SALES   COUNT_NEW
2022-01-13 20:40:00   729.99  NaN     NaN        ← only NEW changed
2022-01-15 22:28:00   NaN     NaN     -1.0       ← only COUNT_NEW changed
2022-02-07 15:44:00   NaN     352330  NaN        ← only SALES changed
```
To get a continuous price series you must resample/forward-fill.

**Non-null counts for iPhone 13 (B09LNW3CY2), 18174 total rows:**
```
NEW:         6483  ← dominant price column
USED:        3367
AMAZON:      3233
REFURBISHED: 1274
LISTPRICE:     54
```
Same pattern holds for Samsung and Google — NEW dominates.

---

## 3. `{ASIN}_monthly_sold.csv` — sales rank snapshots

| Column | Type | Description |
|---|---|---|
| asin | string | Amazon product ID |
| datetime | string | Timestamp of snapshot |
| monthly_sold | int | Sales rank position (lower = more sold, NOT unit count) |

**Example rows:**
```
asin        datetime              monthly_sold
B09LNW3CY2  2023-10-20 11:28:00  1000
B09LNW3CY2  2023-11-02 08:28:00   500
```

---

## 4. `{ASIN}_stats.csv` — aggregate statistics, one row per ASIN

Wide format. Contains rolling averages over 30 / 90 / 180 / 365 days for all price types, plus current and interval-start values.

**Key columns:**
```
avg30_NEW, avg90_NEW, avg180_NEW, avg365_NEW   — rolling avg NEW price
current_NEW                                    — most recent NEW price
salesRankDrops30/90/180/365                    — proxy for sales velocity
totalOfferCount                                — total active offers
```

**Note:** All price values here are already in USD (not raw Keepa integers) — the harvester script divided by 100 on export.
