# Tasks - ML Phase Week 1 Day 4

**Theme:** reinforcement. No new concepts today - the same four ideas, applied again.
**Data:** `xauusd_m5_et.csv`
**Time:** target 60 min. If you pass 75, stop and tell me.

You said the concepts need repetition to stick. So today you use baselines, buckets,
bias-vs-MAE and WAPE again - on a **different target**, so it is practice rather than
copy-paste.

**New target: `eu_range`** - the morning session range, predicted from *yesterday's* data.
Same dataframe, same features, one change: you now forecast the morning instead of the
afternoon, using only what closed before today started.

---

## Reminder 1 - MAE is per row, then averaged

Yesterday you wrote:

```python
mae = abs(mean_actual - mean_pred)     # this is bias, not MAE
```

The difference matters: if a bucket has errors of +20 and -20, the difference of means is
0 while the true MAE is 20. Compute the error **per row first**, then group:

```python
res['abs_error'] = (res['actual'] - res['pred']).abs()   # per row
res['error']     = res['pred'] - res['actual']           # per row, keeps sign

res.groupby('bucket', observed=True).agg(
    mae  = ('abs_error', 'mean'),
    bias = ('error', 'mean'),
)
```

`bias` is a real term - mean error. It tells you the *direction* of the mistake.
`mae` tells you the *size*. You need both.

---

## Reminder 2 - WAPE, one more time

You have two error numbers from different periods and want to know which is worse.
You cannot compare them directly if the scales differ.

```
train MAE  4.06   with typical values around 11
test  MAE 14.89   with typical values around 40
```

Divide each by what it is predicting:

```python
4.06 / 11.06 * 100 = 36.7%
14.89 / 40.32 * 100 = 36.9%
```

Same accuracy. The MAE jump was scale, not failure.

**Rule:** whenever you compare error across sets with different scales, convert to percent
first. That is all WAPE is.

---

## Task 1 - Build the new target (15 min)

Predict `eu_range` using only data available **before today's morning session opens**.

Features - all lagged by one day:
- `prev_eu_range`, `prev_us_range`
- `eu_atr14`, `us_atr14`  (you already have these, they are already shift-based)
- `prev_eu_close_loc`, `prev_eu_return_pct`

Same 80/20 chronological split.

**In a comment:** which of your existing features would leak here, and why? Name at least
two and say exactly what they reveal.



df['prev_eu_range'] = df['eu_range'].shift(1)
df['prev_eu_close_loc'] = (df['eu_close'].shift(1) - df['eu_low'].shift(1)) / (df['eu_high'].shift(1) - df['eu_low'].shift(1))
df['prev_eu_return_pct'] = (df['eu_close'].shift(1) - df['eu_open'].shift(1)) / df['eu_open'].shift(1) * 100
df.head()
filtered_df = df.drop(columns = ['trade_date', 'us_open', 'us_high', 'us_low', 'us_close', 'us_bars', 
                                 'us_bar_rng_mean', 'us_range', 'eu_open', 'eu_high', 
                                 'eu_low', 'eu_close', 'eu_bar_rng_mean', 'eu_bars',
                                 'eu_return_pct', 'eu_close_loc', 'eu_range_norm', 'us_range_norm'])

filtered_df = filtered_df.dropna()
filtered_df.head()

X = filtered_df.drop(columns = ['eu_range'])
y = filtered_df['eu_range']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    shuffle = False
)

X.head()
#Currently no features leak, I've dropped all the leakages in filtered_df, it's self-explanatory


---

## Task 2 - Baselines, then the model (20 min)

- 2a. Four baselines on the test set: `train_mean`, `train_median`, `prev_eu_range`, `eu_atr14`.
     One table, MAE + R2, sorted by MAE.
- 2b. Fit `LinearRegression`. Add it to the table.
- 2c. WAPE for train and test.

**In comments:**
- Which baseline won this time? Same as yesterday or different?
- Does your model beat it? By how much, in percent?
- Compare the train/test WAPE gap here against yesterday's 36.7 / 36.9. Wider or narrower,
  and what would explain it?



rows = []
for name, prediction in [
     ('train_mean', np.full(len(y_test), y_train.mean())),
     ('train_median', np.full(len(y_test), y_train.median())),
     ('prev_eu_range', X_test['prev_eu_range']),
     ('eu_atr14', X_test['eu_atr14'])
]:
     rows.append(
          {
          'name': name,
          'MAE': mean_absolute_error(y_test, prediction),
          'R2': r2_score(y_test, prediction),
          }
     )

rows = pd.DataFrame(rows)
rows.head()

#It's similar, it seems like eu_atr14 is a pretty solid metric as a baseline, it self adjusts itself to the current market dynamics


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
model_mae = mean_absolute_error(y_test, y_pred)
model_r2 = r2_score(y_test, y_pred)

rows.loc[len(rows)] = ({
     'name': 'model_predictions',
     'MAE': model_mae,
     'R2': model_r2
})

rows.head()

'''	name	MAE	R2
0	train_mean	39.893995	-0.691469
1	train_median	42.069544	-0.780908
2	prev_eu_range	27.668226	-0.080938
3	eu_atr14	23.976252	0.159418
4	model_predictions	21.242674	0.309893'''

#It seems like we're getting very close to the eu_ATR14 IN TERMS of MAE, but still perform about 2pp better + 0.15pp better in terms of predictions in the current state.
#Not bad I think.



train_wape = 39.89 / y_train.mean() * 100
test_wape = 21.24 / y_test.mean() * 100 #I manually took the MAE values here for convenience, since I didn't create variables for them - IMO it's not a big deal
print(train_wape, test_wape)

#190.92927338459194 35.25731791180053

Wider, train_wape is very high, which is a bit weird TBH.
Test_wape looks more legitimate.

---

## Task 3 - Buckets and bias (20 min)

- 3a. Bucket the test set by actual `eu_range` into 5 quantiles.
- 3b. Per bucket: `mean_actual`, `mean_pred`, `mae`, `bias`, `n` - using the per-row method above.
- 3c. Plot `bias` per bucket as a bar chart, with a horizontal line at zero.

**In comments:**
- Yesterday the bias went from +6.6 in Q1 to -36.3 in Q5. Does the same pattern appear here?
- Why does a linear model do this? Answer in one sentence.
- If you were sizing a position off this model, which bucket is dangerous and why?



quantiles_df = pd.DataFrame({'actual': y_test, 'pred': y_pred})
quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

quantiles_df['abs_error'] = abs(quantiles_df['actual'] - quantiles_df['pred'])
quantiles_df['error'] = quantiles_df['actual'] - quantiles_df['pred']
quantiles_df.head()

quantiles_diff = quantiles_df.groupby('bucket').agg(
    mean_actual = ('actual', 'mean'),
    mean_pred = ('pred', 'mean'),
    mae = ('abs_error', 'mean'),
    bias = ('error', 'mean')
).reset_index()

quantiles_diff.head()


plt.figure(figsize = (16, 9))
error_chart = sns.barplot(
    quantiles_diff,
    x = 'bucket',
    y = 'mae'
)
error_chart.set_title('MAE by EU range buckets for the model test results')
error_chart.axhline(color = 'r')
plt.show()



#For you convenience, the results from the table as well:
'''
	bucket	mean_actual	mean_pred	mae	bias
0	Q1	22.949193	34.458395	11.961866	-11.509202
1	Q2	38.296304	42.357092	11.151325	-4.060789
2	Q3	48.676439	55.593989	14.356647	-6.917550
3	Q4	65.064625	62.780759	16.480208	2.283866
4	Q5	125.927070	81.818032	52.002728	44.109038'''

#Yes, seems like the same pattern appears here, the bias goes up highly in the Q5
#It makes sense to happen in a highly skewed dataset to the right - the outliers, which all naturally #occupy Q5 lift up the MAE BY A LOT - these can be highly impactful news days, or simply very high #volatility days, which naturally occured from time to time during those 5-6 years of analyzed data

#Q5 is dangerous obviously - it would be nice if we could somehow mitigate its effects

---

**Total: 3 tasks.**

If any of this feels like busywork rather than practice, say so and I will cut it.
