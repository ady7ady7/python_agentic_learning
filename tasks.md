# Tasks - ML Phase Week 2 Day 1

**Theme:** the Q5 problem. You have raised it three times unprompted - today it gets solved.
**Data:** `xauusd_m5_et.csv`
**Time:** target 60 min.

Quiz result: 62%. Leakage 92%, code recall 25%. So today starts with a five-minute drill,
then moves to the one thing you keep asking about.


#Start 13:00

---

## Warm-up - code from memory (5 min, no notes)

Write these three from memory first. Then check against your week-1 files and note what
you got wrong. This is not scored - it is calibration.

1. A baseline predicting the training median, with its MAE.
2. The bucket table: `mean_actual`, `mean_pred`, `mae`, `bias`, `n` per quantile.
3. WAPE for train and test.

Do not skip this because it feels trivial. The quiz says it is not yet automatic.


1. 

from sklearn.metrics import mean_absolute_error

mean_training = np.full(len(y_test), y_train.median())
train_mae = mean_absolute_error(y_test, mean_training)

2. 
#struggle here

y_pred = model.predict(X_test)
mean_actual = np.full(len(y_test), y_test.mean())
mean_pred = np.full(len(y_test), y_pred.mean())

quantiles_df = pd.DataFrame({'actual': y_test, 'pred': y_pred})
quantiles_df['mae'] = abs(quantiles_df['mean_actual'] - quantiles_df['mean_pred'])
quantiles_df['bias'] = quantiles_df['mean_actual'] - quantiles_df['mean_pred']

quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
quantiles_df = quantiles_df.groupby('bucket').agg(
     mean_actual = ('actual', 'mean'),
     mean_pred = ('pred', 'mean'),
     mae = ('mae', 'mean'),
     bias = ('bias', 'mean'),
     n = ('bucket', 'count')
).reset_index()


test_mae = mean_absolute_error(y_test, y_pred)

train_wape = train_mae / y_train.mean() * 100
test_wape = test_mae / y_test.mean() * 100 #mock here

#finished this part at 13:33

---

## Concept - your model cannot predict Q5, and that is not a bug

Every day this week the same pattern appeared:

```
Q1  bias +11.5    model over-predicts quiet days
Q5  bias -44.1    model under-predicts violent days
```

Linear regression minimises **squared error**, which means it fits a line through the
middle of the cloud. On a right-skewed target it cannot pass through both the bulk and the
tail, so it lands near the mean and misses both ends. This is called **regression toward
the mean** and it is a property of the method, not a mistake in your code.

You asked: *"if we could identify Q5 earlier, we'd have very good predictive power."*

That instinct has a name. The technique is **quantile regression**, and instead of
predicting the average outcome it predicts a chosen percentile.

**Ordinary regression** answers: *what is the expected range today?*
**Quantile regression** answers: *what range will not be exceeded on 90% of days like today?*

For stop placement, the second question is the useful one.

**Worked example:**

```python
from sklearn.linear_model import QuantileRegressor

# alpha=0 disables the regularisation; quantile=0.9 asks for the 90th percentile
q90 = QuantileRegressor(quantile=0.9, alpha=0)
q90.fit(X_train, y_train)
pred_q90 = q90.predict(X_test)

# how often did reality stay below the prediction?
coverage = (y_test <= pred_q90).mean()
print(f"{coverage:.1%} - should land near 90%")
```

`coverage` is the metric that matters here, not MAE. A q90 model that covers 89% of days is
working correctly even if its MAE looks worse than the ordinary model's.

---

## Task 1 - Three quantiles (25 min)

Use the **`us_range` setup from Day 3** - predicting the afternoon from the morning.

- 1a. Fit three `QuantileRegressor` models: quantile 0.5, 0.8, 0.9. Same X, same split.
- 1b. For each, compute coverage on the test set: `(y_test <= pred).mean()`.
- 1c. Put the three coverages in a table next to their target quantiles.
- 1d. Also fit an ordinary `LinearRegression` and compute its coverage.

**In comments:**
- Are the coverages close to 0.5 / 0.8 / 0.9? If one is badly off, which and by how much?
- What is the ordinary model's coverage, and why is it near 50% rather than 90%?

Note: `QuantileRegressor` is slow on larger data. If it takes more than a minute, reduce
to `alpha=0` and fewer features, or say so and I will switch you to a faster approach.




from sklearn.linear_model import QuantileRegressor


eu_session.head()
eu_session.columns

df.head()
df = df.dropna()

y = df['us_range']
X = df.drop(columns = ['trade_date', 'us_open', 'us_high', 'us_low', 'us_close', 'us_bars',
       'us_bar_rng_mean', 'us_range', 'us_range_norm'])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    shuffle = False
)


q90_model = QuantileRegressor(quantile = 0.9)
q90_model.fit(X_train, y_train)
pred_q90 = q90_model.predict(X_test)

coverage_90 = (y_test <= pred_q90).mean()
print(f'{coverage_90} should land near 90%')


q80_model = QuantileRegressor(quantile = 0.8)
q80_model.fit(X_train, y_train)
pred_q80 = q80_model.predict(X_test)

coverage_80 = (y_test <= pred_q80).mean()
print(f'{coverage_80} should land near 80%')



q50_model = QuantileRegressor(quantile = 0.5)
q50_model.fit(X_train, y_train)
pred_q50 = q50_model.predict(X_test)

coverage_50 = (y_test <= pred_q50).mean()
print(f'{coverage_50} should land near 50%')


0.7031802120141343 should land near 90%
0.607773851590106 should land near 80%
0.3745583038869258 should land near 50%

#Not entirely sure how to interpret it, but it looks like the coverage is highest for the 90%, as it's 70% if I'm interpreting it properly. 

#But in this context, your suggestion doesn't make sense :)), as it's quite the opposite in this case.






---

## Task 2 - Does it fix Q5? (20 min)

- 2a. Build the bucket table again, this time with four prediction columns:
     ordinary, q50, q80, q90 - showing `mean_actual` and each model's mean prediction.
- 2b. For the Q5 bucket specifically: what does each model predict, against a mean actual
     of roughly 95?
- 2c. Compute MAE for each of the four, on the whole test set.

**In comments:**
- q90 will have the worst MAE. Explain why that is expected and not a failure.
- For someone placing a stop, which of the four numbers do they want, and why?
- Yesterday you said "it would be nice if we could mitigate Q5". Did this mitigate it?




quantiles_df = pd.DataFrame({'ordinary': y_test, 'q50': pred_q50, 'q80': pred_q80, 'q90': pred_q90})
qs = ['q50', 'q80', 'q90']
for q in qs:
    q_name_mae = f'{q}_mae'
    q_name_bias = f'{q}_bias'
    quantiles_df[q_name_mae] = abs(quantiles_df['ordinary'] - quantiles_df[q])
    quantiles_df[q_name_bias] = quantiles_df['ordinary'] - quantiles_df[q]

quantiles_df['bucket'] = pd.qcut(quantiles_df['ordinary'], 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
quantiles_df.head()

bucket_means = quantiles_df.groupby('bucket').agg(
    mean_actual = ('ordinary', 'mean'),
    q50_mean = ('q50', 'mean'),
    q50_mae = ('q50_mae', 'mean'),
    q50_bias = ('q50_bias', 'mean'),
    q80_mean = ('q80', 'mean'),
    q80_mae = ('q80_mae', 'mean'),
    q80_bias = ('q80_bias', 'mean'),
    q90_mean = ('q90', 'mean'),
    q90_mae = ('q90_mae', 'mean'),
    q90_bias = ('q90_bias', 'mean')
).reset_index()

bucket_means.head()

#As for the questions, I'll simply paste the results here


'''bucket	mean_actual	q50_mean	q50_mae	q50_bias	q80_mean	q80_mae	q80_bias	q90_mean	q90_mae	q90_bias
0	Q1	26.590864	18.601414	7.989450	7.989450	27.597410	2.194519	-1.006546	33.297246	6.706382	-6.706382
1	Q2	38.697974	22.848840	15.849134	15.849134	33.020842	5.758531	5.677132	39.210786	3.036578	-0.512812
2	Q3	51.301863	25.983851	25.318012	25.318012	36.932946	14.368916	14.368916	43.476422	7.899598	7.825441
3	Q4	61.933715	26.877338	35.056377	35.056377	37.494363	24.439352	24.439352	44.088573	17.845142	17.845142
4	Q5	98.404797	31.776297	66.628499	66.628499	41.824093	56.580703	56.580703	48.809575	49.595222	49.595222'''

#Q90 seems to work the best - it is some indicator, but I'm not sure wheteher I'm interpreting this correctly.



---

## Task 3 - The practical output (10 min)

Print a small table for the last 10 test days:

```
date        actual   q50    q80    q90    within_q80?
```

**In a comment:** if you traded off `q80`, how many of those 10 days would have had the
range exceed your estimate? Is that roughly what you would expect?


small_df = df[['trade_date', 'us_range']].tail(10)
small_df['q50'] = pred_q50.mean()
small_df['q80'] = pred_q80.mean()
small_df['q90'] = pred_q90.mean()
small_df['within_q80'] = small_df['us_range'] <= small_df['q80']
small_df['within_q90'] = small_df['us_range'] <= small_df['q90']

exceeded_q80 = small_df['within_q80'].mean()
print(exceeded_q80)
exceeded_q90 = small_df['within_q90'].mean()
print(exceeded_q90)

#60% are within q80, 70% within q90


small_df.head(10)


#Yeah, probably that's around what I expected.
#It would maybe make sense to incrase this a bit, maybe q95 makes more sense.


#Finish 14:53, but quite frankly, I stopped a few times - 90 minutes is a realistic benchmark for today.

---

**Total: warm-up + 3 tasks.**

Say so if `QuantileRegressor` is too slow or the API fights you - there is a faster route
via `GradientBoostingRegressor(loss='quantile')` and I will switch if needed.
