# Weekend Quiz - Week 2 (Quantile Regression & Walk-Forward)

No notes, no code execution. Write from memory - if you're unsure, say so rather than
guessing. Partial answers are fine; blank answers with "don't know" are more useful to me
than confident wrong ones.


#Start 16:08

---

## Part A - Concepts

**A1.** In your own words: what does `QuantileRegressor(quantile=0.9)` actually predict,
and how is that different from what `LinearRegression` predicts?


It predicts the 90th percentile of a given data, a boundary which shouldn't be crossed in 9 out of 10 days, if we're looking at the trading days. LinearRegression aims to predict the precise predicted value instead.

**A2.** What is "coverage" and how do you compute it in one line, given `y_test` (actual
values) and `pred` (a model's predictions)? Break down what the line does, don't just
state it.

Coverage is the number or percentage of entries that fall within a certain threshold - in terms of assessing ML models and specifically QuantileRegressor, it portrays how many % of real data are actually below the predicted value, or in other words, how often can we expect that the prediction will be lower than the actual value.

coverage = (y_test <= pred).mean()


**A3.** You fit `QuantileRegressor(quantile=0.9)` with the default `alpha` and get
predictions that barely change from day to day - almost a flat line. What's the likely
cause, and what parameter fixes it?

Default alpha (1) causes the model to flatten the results to the lowest values, which means we will cross the predicted threshold very often. To fix it, one should simply use alpha = 0 and solver = 'highs' to make more balanced predictions.


**A4.** Why is `us_range <= 54.1%` an expected, correct result for an ordinary
`LinearRegression` model - not a bug? (This came up directly this week.)

The LinearRegression performs quite well in predicting the values from the middle of the curve, while having issues with getting the lower/higher values properly. This is not a bug.


**A5.** You want to place a stop-loss and you have three models available: q50, q80, q90.
Which one do you pick and why? What are you trading off by picking a higher quantile
instead of a lower one?

q80, it's probably the best idea as it should survive 4 out of 5 days - q90 will not add much safety, it will protect me from 1 more SL out of 10 entries, and yet it will cost much more eveyr time the SL is hit, lowering the R:R metric, whcih is also very important.

---

## Part B - Walk-forward validation

**B1.** Why does a single train/test split not tell you whether a model is reliable? What
specifically can walk-forward validation catch that a single split cannot?


Data can change over time in very different scopes like the daily range, volume, the magnitude of prices in general (e.g. American ES index was probably like 300-500 pts in 1990s and now it's above 7500), which could affect the results. Walk-forward testing allows us to train the model on a set interval and then test it on data that's right after the training period, which definitely makes more sense.


**B2.** Write the walk-forward loop skeleton from memory - the actual `while` loop, the
slicing, and how `start` moves forward. You don't need the model-fitting details, just the
loop structure that makes it walk-forward and not a single split.

train_size = 300
test_size = 300
start = train_size

results = []
while start + test_size <= len(df):
    train = df.iloc[start - train_size : start]
    test = df.iloc[start : start + test_size]
    model = MockModel()
    model.fit(train[features], train['target'])
    pred = model.predict(test[features])

    results.append(
        {
            'train_start': train.index.min(),
            'predictionts': pred
        }
    )
    start += test_size


**B3.** In a walk-forward loop with `train_size=300` and `test_size=125`, what determines
how many folds you get from a dataset of, say, 1600 rows? Roughly how many folds would that
give you?

The test size mostly, as we move by the length of the test_size every time.
It would give around 10 folds in total.





**B4.** You ran walk-forward on q90 and got coverage of 0.88, 0.89, 0.87, 0.90 across four
folds. A colleague ran it with only one split and also got 0.88. Are these two results
telling you the same thing? Explain the difference.

It's really difficult to say without looking at specific data etc., and it's difficult to say how the models really perform, but it seems like it. However, in the first case we've checked and verified how the model performs on different periods that could differ from each other and it also gives a better idea on how the model performs, how low/high it could go more realistically. In the second case, if we didn't test it in any other way, we're only looking at one split, which could perform entirely different the next time we use it. The first approach is simply safer.


---

## Part C - Code from memory

**C1.** Write the code to fit a `QuantileRegressor` for the 80th percentile with
regularisation switched off, on `X_train` / `y_train`, then compute its coverage on the
test set.


from sklearn.linear_model import QuantileRegressor

model = QuantileRegressor(quantile = 0.8, alpha = 0, solver = 'highs')
model.fit(X_train, y_train)
pred = model.predict(X_test)
coverage = (pred <= y_test).mean()


**C2.** You have a fitted model and want to predict on a *single* day's data taken from a
dataframe `X` (the last row). Write the code to correctly extract that row and get a
prediction out of it - including why a plain `X.iloc[-1]` would not work directly.


row = X.iloc[[-1]] #it requires a Pandas DF not a series, 2-d instead of 1-d structure
prediction = model.predict(row)


**C3.** Write the code to pick 5 truly random row indices from a dataframe with `n` rows
(no repeats, no bias toward the first few rows), without relying on a fixed number like 6.

import random
list = random.sample([i for range(len(df)), 5])




---

## Part D - Judgement

**D1.** You built `forecast_range()` and tested it by passing today's features as a plain
Python list of numbers instead of a properly-shaped, named DataFrame row. It ran without
error and gave a number. What's actually wrong with this, and what failure mode does it
open up that a crash would not?

It could mess up the order of columns and therefore use one feature instead of another, totally messing up the results.


**D2.** Someone tells you: "I trained my quantile models on a train/test split, confirmed
q90 covers 90% of test days, so now I'm confident in predictions from the same models going
forward." What is missing from their reasoning, based on this week's work?

The market could still have a very unusual week caused by whatever, the coverage could be relaated to the big scheme of things etc. And also there could be issues within the whhole training/testing procedure, difficult to say.


**D3.** Your q90 model has mean coverage 0.90 across walk-forward folds, but the worst fold
is 0.62 and the best is 0.99. Is this model trustworthy? What would you want to know before
answering?


There are better and worse periods, as for every model, but overall even the worst fold gives over 60%+ coverage, which is really nice IMO. I'd say it's trustworthy, but I'd probably also see the coverages across all folds to be more informed before making decisions based on model's predictions.

Finisz 16:40

---

**When done, paste your answers and I will score them.**
