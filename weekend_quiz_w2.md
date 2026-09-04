# Weekend Quiz - Week 2 (Quantile Regression & Walk-Forward)

No notes, no code execution. Write from memory - if you're unsure, say so rather than
guessing. Partial answers are fine; blank answers with "don't know" are more useful to me
than confident wrong ones.

---

## Part A - Concepts

**A1.** In your own words: what does `QuantileRegressor(quantile=0.9)` actually predict,
and how is that different from what `LinearRegression` predicts?

**A2.** What is "coverage" and how do you compute it in one line, given `y_test` (actual
values) and `pred` (a model's predictions)? Break down what the line does, don't just
state it.

**A3.** You fit `QuantileRegressor(quantile=0.9)` with the default `alpha` and get
predictions that barely change from day to day - almost a flat line. What's the likely
cause, and what parameter fixes it?

**A4.** Why is `us_range <= 54.1%` an expected, correct result for an ordinary
`LinearRegression` model - not a bug? (This came up directly this week.)

**A5.** You want to place a stop-loss and you have three models available: q50, q80, q90.
Which one do you pick and why? What are you trading off by picking a higher quantile
instead of a lower one?

---

## Part B - Walk-forward validation

**B1.** Why does a single train/test split not tell you whether a model is reliable? What
specifically can walk-forward validation catch that a single split cannot?

**B2.** Write the walk-forward loop skeleton from memory - the actual `while` loop, the
slicing, and how `start` moves forward. You don't need the model-fitting details, just the
loop structure that makes it walk-forward and not a single split.

**B3.** In a walk-forward loop with `train_size=300` and `test_size=125`, what determines
how many folds you get from a dataset of, say, 1600 rows? Roughly how many folds would that
give you?

**B4.** You ran walk-forward on q90 and got coverage of 0.88, 0.89, 0.87, 0.90 across four
folds. A colleague ran it with only one split and also got 0.88. Are these two results
telling you the same thing? Explain the difference.

---

## Part C - Code from memory

**C1.** Write the code to fit a `QuantileRegressor` for the 80th percentile with
regularisation switched off, on `X_train` / `y_train`, then compute its coverage on the
test set.

**C2.** You have a fitted model and want to predict on a *single* day's data taken from a
dataframe `X` (the last row). Write the code to correctly extract that row and get a
prediction out of it - including why a plain `X.iloc[-1]` would not work directly.

**C3.** Write the code to pick 5 truly random row indices from a dataframe with `n` rows
(no repeats, no bias toward the first few rows), without relying on a fixed number like 6.

---

## Part D - Judgement

**D1.** You built `forecast_range()` and tested it by passing today's features as a plain
Python list of numbers instead of a properly-shaped, named DataFrame row. It ran without
error and gave a number. What's actually wrong with this, and what failure mode does it
open up that a crash would not?

**D2.** Someone tells you: "I trained my quantile models on a train/test split, confirmed
q90 covers 90% of test days, so now I'm confident in predictions from the same models going
forward." What is missing from their reasoning, based on this week's work?

**D3.** Your q90 model has mean coverage 0.90 across walk-forward folds, but the worst fold
is 0.62 and the best is 0.99. Is this model trustworthy? What would you want to know before
answering?

---

**When done, paste your answers and I will score them.**
