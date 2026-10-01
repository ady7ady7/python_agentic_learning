# Tasks - ML Phase Week 6 Day 4

**Time:** target 60-75 min - deliberately lighter than yesterday, per yesterday's own
feedback that the material was too dense for one sitting.

**Where we are:** Yesterday's verdict: ADF confirms mean-reversion exists around a 200-bar
rolling mean (p=0.0), but half-life (93.4 bars) is too slow to be practically tradeable (vs.
the 5-60 bar range research suggests). Hurst was computed on the wrong series (raw `close`
instead of `deviation`) - today fixes that, then tests whether a SHORTER rolling window shows
faster, more tradeable reversion. Only 2 tasks today, no new statistical concepts - this is a
correction + a parameter variation, not new material.

---

## Warm-up (10 min) - repetition: dict comprehension, fresh column

Straight repeat, no escalation.

```python
m15 = pd.read_csv('./project4_trend_regime/m15_with_regime.csv', parse_dates=['et_time'])
```

**Your turn:** build a dict comprehension mapping each `regime` value to the fraction of its
rows where `close < ema144_low` (mirror of yesterday's warm-up, opposite side).


regime_below_ema144_low = {
    regime : (m15_df.loc[m15_df['regime'] == regime, 'close'] < m15_df.loc[m15_df['regime'] == regime, 'ema144_low']).mean()
    for regime in m15_df['regime'].unique()
}
print(regime_below_ema144_low)

'''
{'strong_bull': np.float64(0.0), 
'retracement_bull': np.float64(0.3782569631626235), 
'range_recross': np.float64(0.37778868874090893), 
'strong_bear': np.float64(1.0), 
'retracement_bear': np.float64(0.0)}
'''

---

## Task 1 - Fix Hurst: run it on deviation, not raw price (25 min)

Same code as yesterday, one change: feed it the right series.

**Concept - why `kind` matters to this library:** `compute_Hc` needs to know what shape of
number stream it's getting, because its internal math (building cumulative sums to measure
range/dispersion at different lags) differs depending on that. The library offers three
options: `'price'` assumes a POSITIVE, typically-trending level (like a raw close price) and
internally converts it to returns before analysis; `'change'` assumes you're ALREADY handing
it a series of changes/deviations, so it skips that conversion step; `'random_walk'` is for a
series you already know behaves like cumulative noise. Yesterday's `deviation` series
(close minus its own rolling mean) is centered around zero and can go negative - it's not a
price level anymore, it already IS a kind of "change" series relative to the mean, so
`'change'` is the correct choice, not `'price'` (which would wrongly try to treat negative
deviation values as if they were prices).

- 1a. Rebuild `deviation = close - close.rolling(200).mean()` (same as Task 1 from
     yesterday). Run `compute_Hc(deviation, kind='change', simplified=True)`.
- 1b. Print H. Does this new H (on deviation) come out closer to or below 0.5, unlike
     yesterday's 0.63 on raw price?

**In a comment:** now that Hurst is measuring the same thing as Task 1/3 from yesterday
(deviation from a 200-bar mean, not raw price trend) - do all three tools (ADF, Hurst,
half-life) now agree with each other? If Hurst still doesn't cleanly support mean-reversion
even on the right series, is that a contradiction, or could the different tools just be
sensitive to different things (ADF: does it revert at all; Hurst: how persistent/anti-
persistent the whole series is; half-life: how fast)?

m15_df.head()
#deviation is already there
H, c, data = compute_Hc(series = m15_df['deviation'], kind = 'change', simplified = True)
print(H) #0.522782653194648
#It's definitely closer than yesterday, not sure whether 0.52 is a signifier of a strong mean reverting data, but it's definitely closer.





---

## Task 2 - Try a shorter window: does speed improve? (25 min)

Yesterday's 93-bar half-life was measured on a 200-bar rolling mean. A shorter mean might
track price more closely, producing smaller, faster-reverting deviations - worth testing
directly rather than assuming.

**Reminder - the half-life function, self-contained (same as yesterday's Task 3):**

```python
import numpy as np
import statsmodels.api as sm

def calculate_half_life(time_series):
    y = np.asarray(time_series)
    dy = np.diff(y)              # change from one bar to the next
    y_lag = y[:-1]                # the series one step behind dy

    X = sm.add_constant(y_lag)    # adds an intercept column so OLS can fit a + b*y_lag
    model = sm.OLS(dy, X)
    res = model.fit()

    lam = res.params[1]           # the slope on y_lag - how strongly today's level predicts tomorrow's change
    half_life = -np.log(2) / lam  # bars needed for the deviation to shrink halfway back to zero
    return half_life
```

- 2a. Rebuild `deviation_50 = close - close.rolling(50).mean()` (quarter of yesterday's
     window). Run `calculate_half_life(deviation_50)` (drop any NaNs first).
- 2b. Re-run ADF (`adfuller(deviation_50.dropna())`) too - still p≈0, or does a shorter
     window change that picture at all?

**In a comment - updated verdict:** compare the 50-bar window's half-life to yesterday's
200-bar result (93.4 bars). Is reversion meaningfully faster at this shorter window - closer
to the 5-60 bar tradeable range - or does it stay similarly slow regardless of window choice?



#m15_df['deviation_50'] = m15_df['close'] - m15_df['close'].rolling(50).mean() 
# - executed above in the same cell where I calculate deviation, so I don't delete another 49 rows

half_life_value = calculate_half_life(m15_df['deviation_50'])
adfuller_value = adfuller(m15_df['deviation_50'])

print(half_life_value) #22.17001591847692
print(adfuller_value) #(np.float64(-34.09721333869626), 0.0, 71, 121746, {'1%': np.float64(-3.430403713780186), '5%': np.float64(-2.8615637406960395), '10%': np.float64(-2.5667826363336177)}, np.float64(690650.5356657901))


#Quite honestly, I'm not sure - half life's value i 22, and I can't say anything about adfuller score, as I don't understand how itw orks.



---

**Total: 2 tasks + warm-up, ~60 min.** Lighter day - a correction and one parameter
variation, consolidating yesterday's findings rather than adding new statistical machinery.
Task 4 from yesterday (session-aware volatility + gamma-like proxies) stays deferred -
pick it up once this verdict is settled, not today.
