# Tasks - ML Phase Week 2 Day 5

**Time:** target 60-75 min.

Quiz is separate and waits for the weekend. This is extra practice: you have a walk-forward
loop (D3) and a `forecast_range()` function (D4), but you have never run them together. A
model isn't "done" until you know it beats a naive baseline *consistently*, not just on
average - today you check that properly, for real.





---

## Warm-up - baseline vs model, from memory (5 min)

Write one line: given `y_test` and `pred` (a model's predictions) and a naive baseline
`naive_pred` (e.g. yesterday's value repeated), how do you compare their MAE to see if the
model is actually earning its keep? Not scored.

Start 19:52

comparison_df = pd.DataFrame({'actual': y_test, 'pred': pred, 'baseline': naive_pred})
comparison_df['absolute_diff'] = abs(comparison_df['actual'] - comparison_df['pred'])
comparison_df['naive_diff'] = abs(comparison_df['actual'] - comparison_df['naive_pred'])

comparison_df = comparison_df.groupby('absolute_diff').agg(
    mae = ('absolute_diff', 'mean'),
    naive_mae = ('naive_diff', 'mean'),
).reset_index()




---

## Task 1 - Walk-forward coverage for q80, model vs naive (25 min)

**What we are predicting:** `us_range` at 10:00 ET, using this morning's EU session and
previous days only - same as all week.

```python
features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
```

**The naive baseline for this task:** `prev_us_range` (yesterday's range) treated as an
80th-percentile guess. It's a real thing someone might actually do without a model - "today
will probably be like yesterday, plus some room."

- 1a. Run the walk-forward loop (`train_size=300`, `test_size=300` or whatever you prefer -
     your call, justify it in a comment like you did on D3) fitting `QuantileRegressor(
     quantile=0.8, alpha=0, solver='highs')` on each training window.
- 1b. In the same loop, for each fold also compute coverage using `prev_us_range` directly
     as the "prediction" (no model - just that column, scaled up by 1.3x to give it a fair
     shot at 80%: `naive_pred = test['prev_us_range'] * 1.3`).
- 1c. Build a table: one row per fold, two coverage columns (`model_coverage`,
     `naive_coverage`).

**In a comment:** does the model beat the naive baseline in every fold, most folds, or is it
close? What would it mean if the naive baseline won even one fold?

---


from sklearn.linear_model import QuantileRegressor

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
filtered_df = df[features]

train_size = 300
test_size = 300


start = train_size
results = []

while start + test_size <= len(df):
    train = df.iloc[start - train_size : start]
    test = df.iloc[start : start + test_size]
    
    model = QuantileRegressor(quantile = 0.8, alpha = 0, solver = 'highs')
    model.fit(train[features], train['us_range'])
    pred = model.predict(test[features])
    
    results.append(
        {
            'window_start': train.index.min(),
            'model_prediction': (pred <= test['us_range']).mean(),
            'naive_coverage': ((test['prev_us_range'] * 1.3) <= test['us_range']).mean()
        }
    )
    
    start += test_size
    

folds = pd.DataFrame(results)
folds.head()

    
Weird, but the coverages suck here

	window_start	model_prediction	naive_coverage
0	15	0.233333	0.320000
1	315	0.203333	0.313333
2	615	0.173333	0.310000





## Task 2 - Extend forecast_range() to both sessions (20 min)

Wednesday's function only predicted `us_range`. Today, predict `eu_range` for tomorrow
morning too - using only what's known at the US close (16:00 ET) today: today's full EU+US
data and history, nothing from tomorrow.

```python
features_eu = ['prev_eu_range', 'prev_us_range', 'eu_atr14', 'us_atr14']
```

(`prev_eu_range` and `prev_us_range` here mean *today's* completed sessions - they become
"previous" once tomorrow starts. You already built lagged versions like this in Week 1.)

- 2a. Fit q50/q80/q90 `QuantileRegressor` models for `eu_range` on the full dataset (no
     split - like Task 1 on D4).
- 2b. Write a function `forecast_both(row, us_models, eu_models)` that returns a dict with
     six keys: `us_q50`, `us_q80`, `us_q90`, `eu_q50`, `eu_q80`, `eu_q90`.
- 2c. Run it on the last available row and print the result next to what actually happened
     the next morning (if you have that data) or just print the six numbers with a note on
     what each represents.

**In a comment:** which of the six numbers would matter most to you if you were deciding
position size before the EU session opens, and why?

from sklearn.linear_model import QuantileRegressor

features_eu = ['prev_eu_range', 'prev_us_range', 'eu_atr14', 'us_atr14']
features_us = ['eu_range', 'eu_bar_rng_mean', 'us_atr14', 'eu_atr14', 'prev_us_range', 'eu_range_norm']


eu_q50_model = QuantileRegressor(quantile = 0.5, alpha = 0, solver = 'highs')
eu_q50_model.fit(df[features_eu], df['eu_range'])

eu_q80_model = QuantileRegressor(quantile = 0.8, alpha = 0, solver = 'highs')
eu_q80_model.fit(df[features_eu], df['eu_range'])

eu_q90_model = QuantileRegressor(quantile = 0.9, alpha = 0, solver = 'highs')
eu_q90_model.fit(df[features_eu], df['eu_range'])


from typing import Dict


def forecast_both(row,
                  us_models,
                  eu_models):
    
    features_us = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
    features_eu = ['prev_eu_range', 'prev_us_range', 'eu_atr14', 'us_atr14']
    
    row_us = row[features_us]
    row_eu = row[features_eu]
    
    return {
        'us_q50': us_models[0].predict(row_us),
        'us_q80': us_models[1].predict(row_us),
        'us_q90': us_models[2].predict(row_us),
        'eu_q50': eu_models[0].predict(row_eu),
        'eu_q80': eu_models[1].predict(row_eu),
        'eu_q90': eu_models[2].predict(row_eu),
    }
    
    
xd = pd.DataFrame(forecast_both(row = df.iloc[[-1]],
                   us_models = [q50_model, q80_model, q90_model],
                   eu_models = [eu_q50_model, eu_q80_model, eu_q90_model]))
xd.head()


	us_q50	us_q80	us_q90	eu_q50	eu_q80	eu_q90
0	31.919022	45.169257	58.449321	55.244878	75.330539	91.297397



Obviously I would look at eu_q80 most likely, as it should hold in 4 out of 5 days. eu_q50 is a bit too dangerous, and q90 might be an overkill. US qs are irrelevant at that time yet.




---

## Task 3 - Reality check (10 min)

- 3a. Pick any 3 of the six predictions from Task 2 and sanity-check them against the
     historical `atr14` for that session (e.g. is `us_q90` in a plausible range compared to
     `us_atr14`, or wildly off?).

**In a comment:** if one of the three looked implausible, what would you check first -
feature order, a data leak, or something else? You don't need it to actually be wrong, just
say what your first move would be.


historical_atr14 = df.iloc[-1]['us_atr14']
print(historical_atr14)
#35.10521428571422
'''
	us_q50	us_q80	us_q90	eu_q50	eu_q80	eu_q90
0	31.919022	45.169257	58.449321	55.244878	75.330539	91.297397
'''

'''
By looking at the us_qXX I can clearly see the percentages look very plausible - 
q50 would indeed be a dangerous stop to set and could get taken out
q80 seems a lot safer as it's about 30% above the atr14
q90 protects us even more, but it could be an overkill, as it only adds +10pp safety for 13 points more, not a deal I'd take here
'''

If data looked implausible - I'd first check data leak, then the features.

---

**Total: warm-up + 3 tasks.** Take the quiz separately whenever suits you this weekend.
