# Tasks - ML Phase Week 1 Day 3

**Theme:** baselines and error analysis - the two things I failed to explain yesterday.
**Data:** `xauusd_m5_et.csv`
**Time:** 60-75 min. If it runs longer, stop and tell me.

Yesterday you built a model with MAE 14.89 and had no way of knowing whether that was
good. Today you get the tools to answer that.

**Reuse your dataframe from yesterday.** Do not rebuild it. Same `eu_*` / `us_*` naming,
same features, same 80/20 chronological split.

---

## Concept 1 - A baseline is not a model

A baseline is a rule so simple it needs no training. You write down what it would have
predicted, then measure how wrong it was - exactly like a model.

Why it matters: MAE 14.89 means nothing on its own. If guessing gives 18, your model
earned its place. If guessing gives 12, your model is worse than nothing.

**Worked example** - "always predict the training mean":

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

# one number, repeated for every test row
pred = np.full(len(y_test), y_train.mean())

print(mean_absolute_error(y_test, pred), r2_score(y_test, pred))
```

That is the whole idea. No `.fit()`, no learning - just a constant.

When the rule is a column you already have, it is even shorter:

```python
pred = X_test['us_atr14']          # "tomorrow looks like the last 14 days"
print(mean_absolute_error(y_test, pred))
```

---

## Task 1 - Four baselines (15 min)

`prev_day` and `atr14` are **columns you already have** - use them directly as predictions,
one value per test row. Only `train_mean` and `train_median` are single numbers repeated.

Build one table with these five rows, sorted by MAE:

| name | prediction |
|---|---|
| `train_mean` | `np.full(len(y_test), y_train.mean())` |
| `train_median` | same, with median |
| `prev_day` | `X_test['prev_us_range']` |
| `atr14` | `X_test['us_atr14']` |
| `my_model` | yesterday's `y_pred` |

Columns: MAE, RMSE, R2. Then add `vs_best_baseline` = MAE minus the best *baseline* MAE
(excluding your model).

**In a comment:**
- Which baseline is hardest to beat, and why is that one - not the mean - the honest benchmark?
- `train_mean` will have a negative R2. What does a negative R2 actually mean?


from sklearn.metrics import mean_absolute_percentage_error

train_mean = y_train.mean()
train_median = y_train.median()
prev_day = X_test['prev_us_range']
atr14 = X_test['us_atr14']
my_model = y_pred

pred_mean = np.full(len(y_test), train_mean)
pred_median = np.full(len(y_test), train_median)

rows = []
for name, prediction in [
    ('train_mean', pred_mean),
    ('train_median', pred_median),
    ('prev_day', prev_day),
    ('atr14', atr14),
    ('my_model', my_model)
]:
    rows.append({
        'name': name,
        'MAE': mean_absolute_error(y_test, prediction),
        'R2': r2_score(y_test, prediction),
        'RMSE': root_mean_squared_error(y_test, prediction),
        'MAPE': mean_absolute_percentage_error(y_test, prediction)
    }
    )

rows_df = pd.DataFrame(rows)
rows_df

#I've also added MAPE so it's a bit clearer for me.
#It's difficult to say, which will be the hardest baseline to beat
#negative r2 score signifies a VERY BAD performance of the model, not sure how to interpret it here in this context, but it feels like my model performs a lot well, 
#and it's able to explain 47% of the variance, if I'm not mistaken. It's not perfect, I'd rather see numbers like 70 here honestly, but it was a quickly trained model

#model wins in every single case now, it looks like it.
#I guess atr14 is the best to compare with, as it seems to be the closest to the model's current performance + it trims itself to the current market performance
#I'm thinking if we could somehow use rolling atr14 as the baseline comparator, but wondering if that's possible.



---

## Concept 2 - Average error hides where the model fails

MAE is one number for the whole test set. A model can be excellent on quiet days and
useless on violent ones and still show a decent average - and violent days are exactly
the ones that cost money.

The fix: bucket the **actual** values, then compute the error inside each bucket.

**Worked example:**

```python
res = pd.DataFrame({'actual': y_test, 'pred': y_pred})
res['bucket'] = pd.qcut(res['actual'], 5, labels=['Q1','Q2','Q3','Q4','Q5'])

res.groupby('bucket', observed=True).apply(
    lambda g: pd.Series({
        'mean_actual': g['actual'].mean(),
        'mean_pred':   g['pred'].mean(),
        'mae':         (g['actual'] - g['pred']).abs().mean(),
        'n':           len(g),
    })
)
```

Note `pd.qcut` on its own only labels rows - the grouping is what produces the answer.
That was the missing half yesterday.


quantiles_df = pd.DataFrame({'actual': y_test, 'pred': y_pred})
quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

error_quantiles_df = quantiles_df.groupby('bucket').agg(
    mean_actual = ('actual', 'mean'),
    mean_pred = ('pred', 'mean'),
    n = ('bucket', 'count')
)

error_quantiles_df['mae'] = abs(error_quantiles_df['mean_actual'].abs() - error_quantiles_df['mean_pred'].abs())
error_quantiles_df.head()


#Seems that Q5 predictions are the absolute killer, which ruin our stats.
#If we'd be able to identify Q5 somehow earlier, we'd have a very good predictive power - at least that's what I think instinctively


I've done it slightly different, imo it's clearer.
Anyway, I don't feel comfrotable with the qcut, but I kinda get the idea, or start getting it.
Makes a lot of sense





---

## Task 2 - Where does the model fail? (20 min)

- 2a. Build that table for your model's test predictions.
- 2b. Add a column `bias` = `mean_pred` - `mean_actual`. Positive means over-prediction.
- 2c. Do the same for the `atr14` baseline, so you can compare per bucket.

**In comments:**
- Is the error evenly spread across buckets, or concentrated? Where exactly?
- Look at `bias` in Q1 and Q5. Is there a pattern, and can you explain why it happens?
- Someone sizes a position using this model. Which bucket should worry them most?




quantiles_df = pd.DataFrame({'actual': y_test, 'pred': y_pred})
quantiles_df['bucket'] = pd.qcut(quantiles_df['actual'], 5, labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

error_quantiles_df = quantiles_df.groupby('bucket').agg(
    mean_actual = ('actual', 'mean'),
    mean_pred = ('pred', 'mean'),
    n = ('bucket', 'count')
)

error_quantiles_df['mae'] = abs(error_quantiles_df['mean_actual'].abs() - error_quantiles_df['mean_pred'].abs())
error_quantiles_df.head()

#Seems that Q5 predictions are the absolute killer, which ruin our stats.
#If we'd be able to identify Q5 somehow earlier, we'd have a very good predictive power - at least that's what I think instinctively


atr_df = pd.DataFrame({'atr': atr14, 'actual': y_test, 'pred': y_pred})
atr_df['bucket'] = pd.qcut(atr_df['atr'], 5, labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

error_atr_df = atr_df.groupby('bucket').agg(
    mean_atr = ('atr', 'mean'),
    mean_actual = ('actual', 'mean'),
    mean_pred = ('pred', 'mean'),
    n = ('bucket', 'count')
)

error_atr_df['mae'] = abs(error_atr_df['mean_pred'] - error_atr_df['mean_atr'])
error_atr_df.head()

#Similar situation here, the high ATR periods seem to be very difficult to predict.
#I reckon it's because the data's mostly trained on lower ATR periods (80% of data is in the Q1-Q4 region, which is quite obvious), and it's hard to predict the outliers


And the results:

#1:

mean_actual	mean_pred	n	mae
bucket				
Q1	10.411860	17.047310	57	6.635451
Q2	20.875929	28.233644	56	7.357715
Q3	30.554877	33.827112	57	3.272235
Q4	44.240911	42.289685	56	1.951226
Q5	95.244018	58.922296	57	36.321721


#2

mean_atr	mean_actual	mean_pred	n	mae
bucket					
Q1	13.204783	13.820298	15.283551	57	2.078767
Q2	25.038389	33.555982	27.256233	56	2.217844
Q3	34.996737	33.989333	33.307234	57	1.689503
Q4	44.471879	44.299054	38.251973	56	6.219906
Q5	81.618137	75.886404	66.133072	57	15.485064


---

## Concept 3 - Metrics can disagree, and that tells you something

Yesterday your numbers were:

```
train:  MAE  4.06   R2 0.323
test:   MAE 14.89   R2 0.490
```

MAE got 3.7x worse on test, but R2 got **better**. That looks impossible.

It is not. R2 measures error relative to the variance *of that particular set*. Between
train and test, gold went from ~2094 to ~4194 and the mean `us_range` went from 11.1 to
40.3. Everything got bigger - the errors and the variance both.

So: **MAE is in points and comparable across sets. R2 is relative and is not.**

---

## Task 3 - Diagnose the regime shift (15 min)

- 3a. Print mean and std of `us_range` separately for train and test.
- 3b. Same for `eu_close` (the price level).
- 3c. Line plot of `us_range` over the whole period, with a vertical line at the split point.
- 3d. Compute the model's MAE **as a percentage of the mean actual** in each set:
     `MAE / y.mean() * 100`.

**In a comment:** after 3d, is the model actually 3.7x worse on test, or was that an
artefact of scale? What does this suggest about predicting a raw price range across years?


y_train.head()
y_test.head()


train_mean, train_std = (y_train.mean(), y_train.std())
print(f'Train values: {train_mean}, {train_std}')

test_mean, test_std = (y_test.mean(), y_test.std())
print(f'Test values: {test_mean}, {test_std}')

Train values: 11.05777856510186, 7.669927953779707
Test values: 40.31998586572436, 38.29568113706263



train_euc_mean, train_euc_std = (X_train['eu_close'].mean(), X_train['eu_close'].std())
print(f'Train EU close values: {train_euc_mean}, {train_euc_std}')

test_euc_mean, test_euc_std = (X_test['eu_close'].mean(), X_test['eu_close'].std())
print(f'Test EU close values: {test_euc_mean}, {test_euc_std}')

Train EU close values: 2093.67947741364, 419.61857079851376
Test EU close values: 4194.185148409893, 569.2810482847498


df.head()
split_point = df['trade_date'][int(round(0.8*len(df)))]
print(split_point)

plt.figure(figsize=(20, 10))
lineplot = sns.lineplot(
     df,
     x = 'trade_date',
     y = 'us_range'
)
plt.axvline(
     x = split_point,
     color = 'yellow'
)
plt.show()




#WAPE - ważona średnia, która dużo lepiej radzi sobie na prawoskośnych rozkłądach.

train_pct = train_mae / y_train.mean() * 100
test_pct  = test_mae  / y_test.mean()  * 100
print(f'train WAPE: {train_pct:.1f}%   test WAPE: {test_pct:.1f}%')


#I don't understand it for shit yet, I just kinda copied this from you, being honest here.
I only know it handles right skewed distirbutions better, but that's about it, IDK why and I wouldn't know how to use it and why..



---

## Task 4 - One fix, measured (15 min)

If the problem is scale, model a scale-free target instead.

- 4a. Build `us_range_norm` = `us_range` / `us_atr14`. This is "today's range relative to
     recent days" - roughly 1.0 on a typical day.
- 4b. Retrain the same `LinearRegression` on this new target. Same features, same split.
- 4c. Report train and test MAE and R2.
- 4d. Compare train-vs-test on the normalised target against yesterday's raw-target run.

**In a comment:** did normalising the target reduce the train/test gap? If yes, what does
that confirm? If no, what else could explain it?


df.head()
df['us_range_norm'] = df['us_range'] / df['us_atr14']

y = df['us_range_norm']
X = df.drop(columns = ['trade_date', 'us_open', 'us_high', 'us_low', 'us_close', 'us_bars', 'us_bar_rng_mean', 'us_range', 'us_range_norm'])


X_train, X_test, y_train, y_test = train_test_split(
     X,
     y,
     test_size = 0.2,
     shuffle = False
)
model = LinearRegression()
model.fit(X_train, y_train)



train_pred = model.predict(X_train)
train_mae = mean_absolute_error(y_train, train_pred)
train_r2 = r2_score(y_train, train_pred)
train_rmse = root_mean_squared_error(y_train, train_pred)
train_mape = mean_absolute_percentage_error(y_train, train_pred)
print(f'Train metrics: MAE: {train_mae}, R2_SCORE: {train_r2}, RMSE: {train_rmse}, train_mape {train_mape}')


test_pred = model.predict(X_test)
test_mae = mean_absolute_error(y_test, test_pred)
test_r2 = r2_score(y_test, test_pred)
test_rmse = root_mean_squared_error(y_test, test_pred)
test_mape = mean_absolute_percentage_error(y_test, test_pred)
print(f'Test metrics: MAE: {test_mae}, R2_SCORE: {test_r2}, RMSE: {test_rmse}, train_mape {test_mape}')

'''Yesterday's metrics with absolute us_range

Train values: MAE: 4.026452759244498, R2 0.3344725256666109, RMSE 6.254345342145135
Test values: MAE: 14.993502938684792, R2 0.4709428259030948, RMSE 27.80561074625558
'''

Todays results:

Train metrics: MAE: 0.38918616685539076, R2_SCORE: 0.0825434706588205, RMSE: 0.6432873326399401, train_mape 0.4271305702463293
Test metrics: MAE: 0.6506124472685888, R2_SCORE: -1.039789597984146, RMSE: 0.9953337405214719, train_mape 0.8526300387331389


It doesn't seem like we've achieved better results with this approach - perhaps normalizing that creates an effect of the outliers from the Q5 greatly increase the mean/median values, which maybe brings data closer to the Q5 data, but at the same time make it perform slightly worse on the most majority of data (Q1-Q4). That's my speculation. I've seen that this dataset has a very big right skew, which means some outliers are really extremely big.





---

**Total: 4 tasks.** Paste solutions and comment answers when done.

Stop and tell me if anything is unclear rather than fighting it for an hour - that is a
defect in my task, not in you.
