# Tasks - ML Phase Week 2 Day 3

**Time:** target 60-75 min.

Yesterday your q90 model covered 88.3% of test days. Good number. But it came from **one**
train/test split - one slice of history. Today you find out whether that number is real or
whether you got lucky with where the split happened to fall.

---

## Warm-up - coverage from memory (5 min)

Write this without looking it up:

#Start 13:08

> Given `y_test` (true values) and `pred_q90` (the q90 model's predictions), compute what
> share of test days had their actual value stay at or below the prediction.

One line. Then write a second line that does the same for q80.

Not scored - just checking whether yesterday stuck.



q90_coverage = (y_test <= pred_q90).mean()
q80_coverage = (y_test <= pred_q80).mean()


---

## Concept - one split tells you one thing

Here is what you have been doing all week:

```
[========== train 80% ==========][== test 20% ==]
 2021 ---------------------------> 2025 ------> 2026
```

You train once, test once, get one number. The problem: that number describes how the model
performed **on one specific stretch of 2025-2026**. If that stretch happened to be calm, or
happened to be violent, your result is coloured by it.

Walk-forward validation fixes this by repeating the exercise across the whole history:

```
[== train ==][test]
      [== train ==][test]
            [== train ==][test]
                  [== train ==][test]
```

The training window slides forward. Each time: fit on the window, predict the stretch
immediately after it, record the result, move on. Nothing ever trains on data that comes
after what it is tested on - the chronological rule still holds, just repeated.

Instead of one number you get several - one per fold (a fold is simply one train-then-test
cycle). And a spread of numbers tells you something a single number cannot:

- **q90 coverage = 88%, 89%, 87%, 90%** - the model is reliable, this is a real property
- **q90 coverage = 71%, 95%, 62%, 99%** - the average is still ~82%, but the model is
  unstable and the average is misleading

That second case is exactly what a single split would hide.

**Worked example - the loop structure:**

```python
train_size = 600      # how many days to train on
test_size  = 125      # how many days to predict, then move forward

results = []
start = train_size

while start + test_size <= len(df):
    train = df.iloc[start - train_size : start]      # the window before
    test  = df.iloc[start : start + test_size]       # the stretch right after

    model = QuantileRegressor(quantile=0.9, alpha=0, solver='highs')
    model.fit(train[features], train['us_range'])
    pred = model.predict(test[features])

    results.append({
        'test_start': test.index.min(),
        'coverage':   (test['us_range'] <= pred).mean(),
    })

    start += test_size        # slide the window forward by one test block

folds = pd.DataFrame(results)
```

Read the slicing carefully, because it is the part that trips people up:

- `df.iloc[start - train_size : start]` - the 600 rows **ending** at `start`
- `df.iloc[start : start + test_size]` - the 125 rows **beginning** at `start`

They touch but never overlap. `start += test_size` then moves everything forward by 125
days and the whole thing repeats.

---

## Task 1 - Walk-forward on q90 (25 min)

**What we are predicting:** `us_range` - the high minus low of the US session
(10:00-16:00 ET), in points.

**When:** at 10:00 ET. Features may use this morning's EU session and previous days,
nothing from the US session itself.

**Features - the same six as yesterday:**

```python
features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
```

Your dataframe needs to be sorted by date for any of this to be meaningful - check that
first with `df.index.is_monotonic_increasing` (or sort by `trade_date` if it is a column).

- 1a. Run the walk-forward loop with `train_size=600`, `test_size=125`, for q90.
- 1b. Print the resulting table: one row per fold, showing the test period start and the
     coverage achieved.
- 1c. Print the mean coverage across folds, and the min and max.

**In comments:**
- How many folds did you get?
- Is the coverage stable across folds, or does it swing? Quote the worst fold.
- Yesterday's single split gave 88.3%. How does that compare to the average here?

from sklearn.linear_model import QuantileRegressor

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14', 'eu_atr14', 'prev_us_range', 'eu_range_norm']

train_size = 300
test_size = 300

results = []
start = train_size
while start + test_size <= len(df):
     train = df.iloc[start - train_size : start]
     test = df.iloc[start : start + test_size]
     
     model = QuantileRegressor(quantile = 0.9, alpha = 0, solver = 'highs')
     model.fit(train[features], train['us_range'])
     pred = model.predict(test[features])
     
     results.append({
          'test_start': train.index.min(),
          'coverage': (test['us_range'] <= pred).mean()
     })
     
     start += test_size


folds = pd.DataFrame(results)

folds.head()

print(f'Mean coverage = {folds['coverage'].mean():.3f}, min coverage = {folds['coverage'].min():.3f}, max coverage = {folds['coverage'].max():.3f}')

#I've went for 300/300 instead, as it's the window that used to work best on my previous ML model tests.


Mean coverage = 0.904, min coverage = 0.870, max coverage = 0.923
3 folds here, I think it's alright and the expected coverage is achieved in all three windows. What do you think?

I'd say even the worst split with 0.87 coverage is acceptable, especially that the rest coverages are better with 0.92 scores - it could be worth the effort and it makes logical sense to me. Of course it could prove me wrong with more examples, but it simply seems to make sense to retrain the algo and test on data that's most relevant (it's simply not too far ahead), as long as the windows are long enough to make proper training. I'd say 300 days is probably enough, hopefully!


---

## Task 2 - All three quantiles, and the ordinary model (20 min)

- 2a. Extend the loop so each fold fits **four** models: q50, q80, q90, and an ordinary
     `LinearRegression`. Record coverage for each.
- 2b. Produce a summary table: one row per model, showing mean coverage, min, max, and the
     target it was aiming for (0.5 / 0.8 / 0.9 / and for the ordinary model, whatever it
     turns out to be).

**In comments:**
- Which of the four is most stable across folds? Which is least?
- Does any model systematically miss its target, rather than just varying around it?

Interesting task to practice Python a bit :))

from sklearn.linear_model import QuantileRegressor, LinearRegression

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14', 'eu_atr14', 'prev_us_range', 'eu_range_norm']
quantiles = [50, 80, 90]

train_size = 300
test_size = 300

results = []
start = train_size
while start + test_size <= len(df):
     train = df.iloc[start - train_size : start]
     test = df.iloc[start : start + test_size]
     
     lin_reg = LinearRegression()
     lin_reg.fit(train[features], train['us_range'])
     lin_reg_pred = lin_reg.predict(test[features])
     results.append({
     'model': 'linreg',
     'test_start': test.index.min(),
     'coverage': (test['us_range'] <= lin_reg_pred).mean()
     })
     
     for q in quantiles:
          name = f'q{q}'
          quantile_parameter = q/100
          model = QuantileRegressor(quantile = quantile_parameter, alpha = 0, solver = 'highs')
          model.fit(train[features], train['us_range'])
          pred = model.predict(test[features])
     
          results.append({
               'model': name,
               'test_start': train.index.min(),
               'coverage': (test['us_range'] <= pred).mean()
          })
     
     start += test_size


folds = pd.DataFrame(results)

folds.head(15)



	model	test_start	coverage
0	linreg	15	0.620000
1	q50	15	0.480000
2	q80	15	0.766667
3	q90	15	0.923333
4	linreg	315	0.660000
5	q50	315	0.496667
6	q80	315	0.796667
7	q90	315	0.870000
8	linreg	615	0.623333
9	q50	615	0.483333
10	q80	615	0.826667
11	q90	615	0.920000


And the summary:

model_summary = folds.groupby('model').agg(
     mean_coverage = ('coverage', 'mean'),
     min_coverage = ('coverage', 'min'),
     max_coverage = ('coverage', 'max'),
).reset_index()

model_summary.head()

As for "target", that doesn't make any sense - it's obvious that q50 aimed for around 50%, q80 for 80%, 90 for 90% etc, it's kinda self-explanatoy and clearly visible, skipped that to avoid useless code.


model	mean_coverage	min_coverage	max_coverage
0	linreg	0.634444	0.620000	0.660000
1	q50	0.486667	0.480000	0.496667
2	q80	0.796667	0.766667	0.826667
3	q90	0.904444	0.870000	0.923333


---

## Task 3 - Plot it (15 min)

- 3a. Line plot: x = fold test start date, y = coverage, one line per model (q50, q80, q90).
- 3b. Add three horizontal reference lines at 0.5, 0.8 and 0.9 so you can see at a glance
     whether each model tracks its own target.

**In a comment:** looking at the chart, is there a period where all three models degrade at
once? If yes, what might have been happening in the market then - and check it against your
data rather than guessing (`us_range` mean per year would tell you something).



import matplotlib.pyplot as plt
import seaborn as sns

folds.head()

plt.figure(figsize = (16, 10))
lp = sns.lineplot(
    folds,
    x = 'test_start',
    y = 'coverage',
    hue = 'model'
)
lp.axhline(y = 0.5, color = 'red')
lp.axhline(y = 0.8, color = 'red')
lp.axhline(y = 0.9, color = 'red')
plt.show()


#I wouldn't say all models degrade at once, the results are mixed + overall close to their expected coverage, while linear regression's coverage sits around 60-62% mark.


#Finish 14:28


---

**Total: warm-up + 3 tasks.**

The loop in Task 1 is the only genuinely new thing today. If the slicing does not make
sense, stop and ask rather than fighting it.
