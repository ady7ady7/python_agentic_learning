# Tasks - ML Phase Week 2 Day 2

**Time:** target 60-75 min.

Yesterday the quantile models came out wrong - q90 covered 70% of days instead of 90%.
The cause was in the features, not the method. Today we fix it and finish the topic with
something you could actually use.

---

## Warm-up - the bucket table from memory (5 min)

Write this without looking anything up. Fourth time this week, so it should start flowing:

> Given `y_test` (the true values) and `y_pred` (the model's predictions), produce a table
> that splits the test set into 5 equal-sized groups by actual value, and shows per group:
> mean actual, mean predicted, MAE, bias, and how many rows.

One hint, because you have hit this twice: `y_test` is a Series (a single column), so you
cannot add columns to it. Build a DataFrame first with both actual and predicted side by
side, then work on that.

Not scored. Check against your notes afterwards and see what slipped.

#Start 12:35

quantiles_df = pd.DataFrame({'actual': y_test, 'pred': y_pred})
quantiles_df['bias'] = quantiles_df['pred'] - quantiles_df['actual']
quantiles_df['abs_diff'] = abs(quantiles_df['pred'] - quantiles_df['actual'])
quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

grouped_buckets = quantiles_df.groupby('bucket').agg(
  mean_actual = ('actual', 'mean'),
  mean_pred = ('pred', 'mean'),
  mae = ('abs_diff', 'mean'),
  bias = ('bias', 'mean'),
  n = ('bucket', 'count')
).reset_index()


	bucket	mean_actual	mean_pred	mae	bias	n
0	Q1	10.411860	30.851140	20.439280	-20.439280	57
1	Q2	20.875929	45.611391	24.776548	-24.735463	56
2	Q3	30.554877	52.902009	22.515949	-22.347132	57
3	Q4	44.240911	65.436249	22.921935	-21.195338	56
4	Q5	95.244018	82.311158	31.398622	12.932859	57


---

## Why yesterday's coverage was wrong

You built the feature list like this:

```python
X = df.drop(columns=['trade_date', 'us_open', 'us_high', 'us_low', 'us_close',
                     'us_bars', 'us_bar_rng_mean', 'us_range', 'us_range_norm'])
```

That correctly removed everything from the US session. But it left in `eu_open`, `eu_high`,
`eu_low`, `eu_close` - the raw morning **price levels**.

Those are numbers like 1850 in 2021 and 4100 in 2026. Gold roughly doubled across your
dataset. So the model trained on price levels around 2000 and was then asked to predict on
levels around 4000 - values it had never seen. It extrapolates badly, and every prediction
comes out too low. That is why all three coverages landed under target.

The fix: **use only features that do not drift with the price level.** A range in points, a
ratio, a location within a range - these mean the same thing in 2021 and 2026. A raw price
does not.

I checked this on your data with the clean feature set:

```
q50 -> 50.9%    q80 -> 77.4%    q90 -> 88.3%
```

Which is where they belong.

---

## Task 1 - Rerun the quantiles on clean features (20 min)

**What we are predicting:** `us_range` - how far price travels during the US session
(10:00-16:00 ET), measured as high minus low.

**When we are predicting it:** at 10:00 ET, the moment the US session opens. So we may use
anything from this morning's EU session (03:00-09:55 ET) and anything from previous days,
but nothing from the US session itself.

**Use exactly these six features:**

```python
X = ['eu_range',          # today's morning high - low, in points
     'eu_bar_rng_mean',   # mean high-low of the morning's 5-min bars
     'us_atr14',          # mean us_range over the previous 14 days
     'eu_atr14',          # mean eu_range over the previous 14 days
     'prev_us_range',     # yesterday's us_range
     'eu_range_norm']     # eu_range divided by eu_atr14
```

Note what is absent: no `eu_open`, `eu_high`, `eu_low`, `eu_close`. Every feature above is
either a distance or a ratio, so none of them grows just because gold got more expensive.

- 1a. Chronological 80/20 split (`shuffle=False`), same as before.
- 1b. Fit `QuantileRegressor(quantile=q, alpha=0, solver='highs')` for q = 0.5, 0.8, 0.9.
     (`alpha=0` switches off regularisation; `solver='highs'` is the faster solver.)
- 1c. For each, compute coverage on the test set: `(y_test <= pred).mean()`.
- 1d. Fit an ordinary `LinearRegression` on the same features and compute its coverage too.

**In comments:**
- Do the three coverages now land near 0.5 / 0.8 / 0.9?
- The ordinary model's coverage will be near 50%. Explain why that is exactly what it should
  be, given what ordinary regression is trying to predict.



from sklearn.model_selection import train_test_split
from sklearn.linear_model import QuantileRegressor, LinearRegression

X = df[['eu_range', 'eu_bar_rng_mean', 'us_atr14', 'eu_atr14', 'prev_us_range', 'eu_range_norm']]
y = df['us_range']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    shuffle = False
)

q50_model = QuantileRegressor(quantile = 0.5)
q50_model.fit(X_train, y_train)
q50_pred = q50_model.predict(X_test)
q50_coverage = (y_test <= q50_pred).mean()

q80_model = QuantileRegressor(quantile = 0.8)
q80_model.fit(X_train, y_train)
q80_pred = q80_model.predict(X_test)
q80_coverage = (y_test <= q80_pred).mean()

q90_model = QuantileRegressor(quantile = 0.9)
q90_model.fit(X_train, y_train)
q90_pred = q90_model.predict(X_test)
q90_coverage = (y_test <= q90_pred).mean()


print(f'Q50 coverage: {q50_coverage}, Q80 coverage {q80_coverage}, Q90 coverage {q90_coverage}')

linear_reg_model = LinearRegression()
linear_reg_model.fit(X_train, y_train)
lin_pred = linear_reg_model.predict(X_test)

lin_pred_q50_coverage = (lin_pred <= q50_pred).mean()
lin_pred_q80_coverage = (lin_pred <= q80_pred).mean()
lin_pred_q90_coverage = (lin_pred <= q90_pred).mean()
print(f'Lin Q50 coverage: {lin_pred_q50_coverage}, Lin Q80 coverage {lin_pred_q80_coverage}, Lin  Q90 coverage {lin_pred_q90_coverage}')


Q50 coverage: 0.10247349823321555, Q80 coverage 0.2332155477031802, Q90 coverage 0.27208480565371024
Lin Q50 coverage: 0.01060070671378092, Lin Q80 coverage 0.15547703180212014, Lin  Q90 coverage 0.2508833922261484

Quite frankly, I'm not sure whether this is what you expected for the Linear Regression coverage - we never tested that.

And also it's difficult for me to interpret these results. How should they be interpreted? It doesn't look like 0.5, 0.8, 0.9 :((. 


However, AS i used your settings with alpha =0 and solver = 'highs', the results look as follows:

Q50 coverage: 0.508833922261484, Q80 coverage 0.773851590106007, Q90 coverage 0.8833922261484098
Lin Q50 coverage: 0.09187279151943463, Lin Q80 coverage 1.0, Lin  Q90 coverage 1.0

Isn't it some kind of error or overfitting or something?
And do I correctly understand that we're able to quite precisely determine which quantile will the given target belong to BEFOREHAND, or am I wrong? How to interpret the results? It's really interesting for me, could be very useful etc, if this actually works properly and if I know how to use it.


---

## Task 2 - Compare the four models properly (20 min)

Yesterday this table was built without `y_test` in it, so it measured how far the quantile
models sat from the ordinary model rather than from reality. Today reality goes in first.

Build a DataFrame with **five columns**: `actual`, `ordinary`, `q50`, `q80`, `q90`.
`actual` is `y_test`. The rest are the four prediction vectors (a vector here just means the
list of predictions, one per test row).

- 2a. Bucket by `actual` into 5 quantiles.
- 2b. Per bucket show: `mean_actual`, and the mean prediction of each of the four models.
- 2c. Across the whole test set, MAE of each of the four models against `actual`.

**In comments:**
- In the Q5 bucket (the most violent days), what does each model predict against the true
  mean? Which comes closest?
- q90 will have the worst overall MAE. Why is that expected rather than a failure?
- If you are setting a stop, which of the four numbers do you want and why?



quantiles_df = pd.DataFrame({'actual': y_test, 'ordinary': y_pred, 'q50': q50_pred, 'q80': q80_pred, 'q90': q90_pred})
quantiles_df['abs_diff_model'] = abs(quantiles_df['actual'] - quantiles_df['ordinary'])
quantiles_df['abs_diff_q50'] = abs(quantiles_df['actual'] - quantiles_df['q50'])
quantiles_df['abs_diff_q80'] = abs(quantiles_df['actual'] - quantiles_df['q80'])
quantiles_df['abs_diff_q90'] = abs(quantiles_df['actual'] - quantiles_df['q90'])
quantiles_df['bias_diff'] = quantiles_df['actual'] - quantiles_df['ordinary']
quantiles_df['bias_diff_q50'] = quantiles_df['actual'] - quantiles_df['q50']
quantiles_df['bias_diff_q80'] = quantiles_df['actual'] - quantiles_df['q80']
quantiles_df['bias_diff_q90'] = quantiles_df['actual'] - quantiles_df['q90']


quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
results_df = quantiles_df.groupby('bucket').agg(
    mean_actual = ('actual', 'mean'),
    mean_pred = ('ordinary', 'mean'),
    model_mae = ('abs_diff_model', 'mean'),
    model_bias = ('bias_diff', 'mean'),
    q50_mean = ('q50', 'mean'),
    q50_mae = ('abs_diff_q50', 'mean'),
    q50_bias = ('bias_diff_q50', 'mean'),
    q80_mean = ('q80', 'mean'),
    q80_mae = ('abs_diff_q80', 'mean'),
    q80_bias = ('bias_diff_q80', 'mean'),
    q90_mean = ('q90', 'mean'),
    q90_mae = ('abs_diff_q90', 'mean'),
    q90_bias = ('bias_diff_q90', 'mean'),
).reset_index()

results_df.head()



1. In the q5 in this configuration, the q90 model comes the closest with the bias it's only -1.8 on average. The rest of the models could be described as fairly ineffective in terms of MAE - it's higher than in other Qs systematically. The linear regression is not that far from the actual results here with 30 MAE/12 bias, but it's relative - I'm unsure whether this would be useful. Overal this model is not very effective with 20MAE/-20 bias in every other Q, but it's my opinion only.

2. The MAE in q90 is the highest since there are extreme outliers which make the precise results very difficult.

3. All numbers are kinda useful. MAE shows the mean absolute error, which is kind of the trust range, or the error margin that should be added. Bias shows the average error with its direction, so that how I should correct the predictions. If I could predict the quantile, that would also be useful in terms of determining the magnitude of possible stop loss and the possible magnitude of error. Knowing the prediction averages vs actual averages is also useful to see how these values interact, and I'd also like to know the local values (like atr14, which kinda self-adjusts itself.)

---

## Task 3 - The usable output (15 min)

Print the last 15 test days as a table:

```
date        actual    q50     q80     q90    within_q80   within_q90
```

Careful here - yesterday this went wrong. `pred_q80` is a list with one prediction per test
row, so to get the last 15 you slice it: `pred_q80[-15:]`. Using `.mean()` would collapse
all of them into one number and every row would show the same value.

- 3a. Build the table.
- 3b. Count how many of the 15 days stayed within q80, and within q90.

**In a comment:** if you had used q80 as your stop distance on those 15 days, how many times
would the range have blown through it? Is that in line with what q80 promises?


test_df = pd.DataFrame(
    {'date': df['trade_date'][-15:],
     'actual': y_test[-15:],
     'q50': q50_pred[-15:],
     'q80': q80_pred[-15:],
     'q90': q90_pred[-15:]
    }
    )

test_df['within_q50'] = test_df['actual'] <= test_df['q50']
test_df['within_q80'] = test_df['actual'] <= test_df['q80']
test_df['within_q90'] = test_df['actual'] <= test_df['q90']

w50_count = test_df['within_q50'].mean()
w80_count = test_df['within_q80'].mean()
w90_count = test_df['within_q90'].mean()
print(F'Within q50: {w50_count}, Within q80: {w80_count}, within q90: {w90_count}')

test_df.head()

I've extended it to q50 as well and to answer your question with data:

Within q50: 0.6, Within q80: 0.8, within q90: 0.8666666666666667




#Finish 13:31




---

**Total: warm-up + 3 tasks.**

Tell me immediately if anything is unclear rather than working around it.
