Pandas Essentials for Data Manipulation

### Series vs DataFrame

```python
"""Understanding Series and DataFrame."""

import pandas as pd

# SERIES - 1D labeled array (like a column)
prices = pd.Series([100, 101, 102, 103], name='close')
print(prices)
# 0    100
# 1    101
# 2    102
# 3    103
# Name: close, dtype: int64

# DATAFRAME - 2D table (like a spreadsheet)
data = pd.DataFrame({
    'ticker': ['EURUSD', 'EURUSD', 'EURUSD'],
    'close': [1.0850, 1.0860, 1.0855],
    'volume': [1000, 1500, 1200]
})

print(data)
#    ticker   close  volume
# 0  EURUSD  1.0850    1000
# 1  EURUSD  1.0860    1500
# 2  EURUSD  1.0855    1200
```

---

### Essential DataFrame Operations

#### 1. Accessing Columns

```python
"""Accessing DataFrame columns."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD'],
    'open': [1.08, 1.25],
    'close': [1.09, 1.26]
})

# Get a column as Series
close_series = df['close']  # Returns Series
print(type(close_series))  # <class 'pandas.core.series.Series'>

# Multiple columns (returns DataFrame)
subset = df[['ticker', 'close']]  # Note: double brackets [[]]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

---

#### 2. Checking for Missing Values (NaN)

```python
"""Handling NaN values properly."""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD', 'USDJPY'],
    'close': [1.08, np.nan, 110.5],
    'volume': [1000, 1500, np.nan]
})

# Check which cells are NaN (returns DataFrame of True/False)
print(df.isna())
#    ticker  close  volume
# 0   False  False   False
# 1   False   True   False
# 2   False  False    True

# Count NaN per column (returns Series)
nan_counts = df.isna().sum()
print(nan_counts)
# ticker    0
# close     1
# volume    1
# dtype: int64

# Check if ANY column has NaN values
has_nan = (df.isna().sum() > 0).any()
print(has_nan)  # True

# Total NaN in entire DataFrame
total_nan = df.isna().sum().sum()
print(total_nan)  # 2
```

**Key Pattern:**
```python
# CORRECT way to check if DataFrame has NaN:
if df.isna().sum().sum() > 0:
    print("DataFrame has missing values")

# OR check per column:
if (df.isna().sum() > 0).any():
    print("At least one column has NaN")
```

---

#### 3. Filtering Rows (Boolean Indexing)

```python
"""Filtering DataFrame rows."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'EURUSD', 'EURUSD'],
    'close': [1.08, 1.09, 1.10],
    'volume': [1000, 1500, 800]
})

# Filter rows where close > 1.08
high_prices = df[df['close'] > 1.08]
print(high_prices)
#    ticker  close  volume
# 1  EURUSD   1.09    1500
# 2  EURUSD   1.10     800

# Multiple conditions (use & for AND, | for OR, parentheses required!)
filtered = df[(df['close'] > 1.08) & (df['volume'] > 1000)]
print(filtered)
#    ticker  close  volume
# 1  EURUSD   1.09    1500
```

**PCAP Trap:** Forgetting parentheses in multiple conditions
```python
# WRONG (SyntaxError or wrong results):
df[df['close'] > 1.08 & df['volume'] > 1000]

# CORRECT:
df[(df['close'] > 1.08) & (df['volume'] > 1000)]
```

---

#### 4. Iterating Over Rows

```python
"""Iterating over DataFrame rows (use sparingly!)."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD'],
    'close': [1.08, 1.25]
})

# iterrows() - returns (index, Series)
for index, row in df.iterrows():
    print(f"Row {index}: {row['ticker']} closed at {row['close']}")
# Row 0: EURUSD closed at 1.08
# Row 1: GBPUSD closed at 1.25

# WARNING: iterrows() is SLOW for large DataFrames
# For production, use vectorized operations when possible
```

---

#### 5. Adding/Modifying Columns

```python
"""Creating and modifying columns."""

import pandas as pd

df = pd.DataFrame({
    'open': [1.08, 1.09],
    'close': [1.09, 1.10]
})

# Add new column
df['change'] = df['close'] - df['open']

print(df)
#    open  close  change
# 0  1.08   1.09    0.01
# 1  1.09   1.10    0.01

# Conditional column
df['direction'] = df['change'].apply(lambda x: 'UP' if x > 0 else 'DOWN')
```

---

### Advanced Filtering & Optimization Patterns

#### Efficient Filtering with Aggregation

When you need to filter rows and calculate statistics, avoid wrapping Series in lists or using NumPy unnecessarily. Pandas Series methods are optimized and cleaner.

**INEFFICIENT Approach:**
```python
"""Avoid wrapping Series in lists with NumPy."""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'open': [100, 102, 101, 103],
    'close': [101, 101, 102, 105]
})

# BAD: Wrapping filtered Series in list, then using NumPy
bullish_closes = df['close'][df['close'] > df['open']]
avg_bullish = np.mean([bullish_closes])  # Unnecessary list wrapping
```

**EFFICIENT Approach 1: Filter First, Then Aggregate**
```python
"""Clean and readable: filter, then use Series methods."""

import pandas as pd

df = pd.DataFrame({
    'open': [100, 102, 101, 103],
    'close': [101, 101, 102, 105]
})

# GOOD: Filter to bullish candles, then use .mean()
bullish_data = df[df['close'] > df['open']]
avg_bullish_close = bullish_data['close'].mean()

print(avg_bullish_close)  # Direct Series method, no NumPy needed
```

**EFFICIENT Approach 2: Use `.loc[]` for Filtered Column Access**
```python
"""Most concise: filter rows and access column in one step."""

import pandas as pd

df = pd.DataFrame({
    'open': [100, 102, 101, 103],
    'close': [101, 101, 102, 105],
    'volume': [1000, 1500, 1200, 1800]
})

# BEST: Use .loc[row_filter, column] for direct access
avg_bullish_close = df.loc[df['close'] > df['open'], 'close'].mean()
max_bullish_volume = df.loc[df['close'] > df['open'], 'volume'].max()

print(f"Avg Bullish Close: {avg_bullish_close}")
print(f"Max Bullish Volume: {max_bullish_volume}")
```

**Why This Matters:**
- **Performance:** Pandas Series methods (`.mean()`, `.max()`, `.sum()`) are vectorized C code - much faster than Python loops or unnecessary conversions
- **Readability:** `df.loc[condition, column].mean()` is clearer than wrapping in lists
- **Memory:** Avoids creating intermediate lists

#### Top-N Selection with `.nlargest()` and `.nsmallest()`

```python
"""Efficient top-N selection."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD'],
    'volume': [1000, 1500, 1200, 1800]
})

# Get top 3 by volume
top_3 = df.nlargest(3, 'volume')
print(top_3)
#    ticker  volume
# 3  AUDUSD    1800
# 1  GBPUSD    1500
# 2  USDJPY    1200

# Get bottom 2 by volume
bottom_2 = df.nsmallest(2, 'volume')
```

**Note:** `.nlargest()` and `.nsmallest()` are more efficient than sorting the entire DataFrame when you only need a few rows.

#### Conditional Column Creation with `.apply()` vs Vectorized Operations

```python
"""Creating columns: vectorized vs apply()."""

import pandas as pd

df = pd.DataFrame({
    'open': [100, 102, 101, 103],
    'close': [101, 101, 102, 105]
})

# APPROACH 1: Vectorized (FASTEST for simple conditions)
df['direction_vec'] = 'bearish'  # Default value
df.loc[df['close'] > df['open'], 'direction_vec'] = 'bullish'

# APPROACH 2: .apply() (better for complex logic)
df['direction_apply'] = df.apply(
    lambda row: 'bullish' if row['close'] > row['open'] else 'bearish',
    axis=1
)

# APPROACH 3: .iterrows() (SLOWEST - avoid for large DataFrames)
directions = []
for idx, row in df.iterrows():
    directions.append('bullish' if row['close'] > row['open'] else 'bearish')
df['direction_iter'] = directions
```

**Performance Ranking:**
1. **Vectorized operations** (`.loc[]`, boolean indexing) - fastest
2. **`.apply()`** - moderate, good for complex row-wise logic
3. **`.iterrows()`** - slowest, avoid in production for large data

---

### Common Pandas Gotchas

**1. `.any()` returns boolean, not numeric**
```python
import pandas as pd

s = pd.Series([0, 5, 0])

# WRONG:
if s.any() > 0:  # .any() is True/False, comparing bool > 0 is weird
    pass

# CORRECT:
if s.any():  # Just check the boolean directly
    pass

# OR check if values > 0:
if (s > 0).any():  # Check if ANY value is > 0
    pass
```

**2. Series arithmetic is element-wise**
```python
s = pd.Series([1, 2, 3])
result = s + 10  # Series([11, 12, 13])
```

**3. Column names must exist**
```python
df = pd.DataFrame({'a': [1, 2]})
print(df['b'])  # KeyError: 'b'
```

---

## Quick Reference Card

`

### Pandas Operations
```python
import pandas as pd

# Load CSV
df = pd.read_csv('file.csv')

# Check columns
df.columns  # Index(['col1', 'col2', ...])

# Access columns
df['col1']        # Series
df[['col1', 'col2']]  # DataFrame

# Check NaN
df.isna()         # DataFrame of True/False
df.isna().sum()   # Count per column
df.isna().sum().sum()  # Total NaN count

# Filter rows
df[df['col'] > 10]
df[(df['col'] > 10) & (df['col'] < 20)]  # Multiple conditions need ()

# Iterate
for idx, row in df.iterrows():
    print(row['col'])
```

---

## Exam Tips

**Pandas:**
- `.any()` returns boolean
- `.sum()` on boolean Series counts True values
- Multiple conditions need parentheses: `(condition1) & (condition2)`
- Use `&` for AND, `|` for OR (not `and`/`or`)
- `.isna()` returns DataFrame, `.isna().sum()` returns Series

---