# Tasks — ML Phase Week 1 Day 2

**Theme:** designing a prediction problem that is actually solvable.
**Data:** `xauusd_m5_et.csv`
**Time:** 60–90 min

Yesterday's task 5 was unsolvable and you caught it: with the full daily OHLC in the features,
predicting `bullish` is reading the answer. Today we fix that properly.

The fix has three parts, and they are the foundation of every honest model:
1. **Split the day** — an observation window you can see, a target window you cannot
2. **Features from the past only** — everything known at the cut-off, nothing after
3. **Validation that respects time** — no training on the future

Target for today: **range of the afternoon session** — your own suggestion, and the right one.
Range is a volatility question, and volatility clusters. Direction does not.

---

## Task 1 — Split the trading day (15 min)

Build a daily DataFrame where each row splits the session in two:

**Morning window (observation): 03:00–09:55 ET**
- `am_open`, `am_high`, `am_low`, `am_close`, `am_bars`

**Afternoon window (target): 10:00–16:00 ET**
- `pm_high`, `pm_low`

Then:
- `pm_range` = `pm_high` − `pm_low`   ← **this is the target**

Keep only days where both windows have bars.

**In a comment:** what is the exact moment in the day at which a prediction would be made,
and how do you know none of your features come from after it?

---

## Task 2 — Features, all from before 10:00 (25 min)

Build these on the daily frame. Every one must be knowable at 10:00 ET.

**From this morning:**
- 2a. `am_range` = am_high − am_low
- 2b. `am_return_pct` = open-to-close of the morning, in percent
- 2c. `am_close_loc` = where am_close sits inside the morning range, 0.0 to 1.0
- 2d. `am_bar_rng_mean` = mean of (high − low) across the morning's 5-min bars

**From previous days:**
- 2e. `pm_atr14` = mean `pm_range` over the previous 14 days
- 2f. `am_atr14` = mean `am_range` over the previous 14 days
- 2g. `prev_pm_range` = yesterday's `pm_range`

**Normalised:**
- 2h. `am_range_norm` = `am_range` / `am_atr14`

Drop rows with NaN. Print the shape and the correlation of each feature with `pm_range`.

**In a comment:** 2d requires going back to the 5-minute data after you have already
aggregated to daily. Explain how you did it, and why `am_range` alone does not capture
the same thing.

---

## Task 3 — Look at the data before modelling (20 min)

Visualisation and statistics come first. A model trained on a relationship you have not
looked at is a guess with extra steps.

**3a. Distribution of the target.** Histogram of `pm_range`. Is it symmetric or skewed?
Add vertical lines for mean and median.

**3b. Does the morning actually relate to the afternoon?** Scatter of `am_range` (x) vs
`pm_range` (y). Then set both axes to log scale. In a comment: did that make the
relationship easier or harder to read, and why?

**3c. Correlation heatmap.** `sns.heatmap` of the correlation matrix for all your features
plus `pm_range`, with values annotated. Which feature relates most strongly to the target?

**3d. Volatility clustering, visually.** Line plot of `pm_range` across the full period.
In a comment: do quiet and violent stretches cluster together, or alternate randomly?
This is the entire premise of today's task — check whether it actually holds.

**3e. Quintile table.** Bucket `am_range` into 5 quantiles with `pd.qcut`. Per bucket print
mean and median `pm_range`, plus the count. Is the progression monotonic?

**In a comment:** based on 3a-3e alone, before fitting anything — do you expect a model to
work here? Yes or no, and name the evidence.

---

## Task 4 — Is the relationship statistically real? (15 min)

A visible pattern and a statistically supported one are different claims.

**4a.** Test whether `pm_range` is normally distributed (`scipy.stats.normaltest`).
State the null hypothesis in your own words and what the p-value means here.

**4b.** Split days into two groups: `am_range` above vs below its median. Test whether
`pm_range` differs between the groups. Pick the correct test based on 4a and justify it.

**4c.** Report the correlation between `am_range` and `pm_range` two ways: Pearson and
Spearman. Explain why the two numbers differ.

**In a comment:** if 4b came back with p = 0.30, would you still build the model? What would
that tell you that the scatter plot did not?

---

## Task 5 — Baselines before any model (15 min)

You cannot judge a model without knowing what costs nothing.

Split the data chronologically, 80/20. On the **test** set only, compute MAE and R² for:

- 5a. Always predict the training-set **mean** of `pm_range`
- 5b. Always predict the training-set **median**
- 5c. Predict `prev_pm_range` (yesterday's value)
- 5d. Predict `pm_atr14` (the 14-day rolling mean)

Print all four in one table, sorted by MAE.

**In a comment:** which baseline is hardest to beat, and why is that one the honest
benchmark rather than the mean?

---

## Task 6 — First real model (20 min)

- 6a. Fit a `LinearRegression` on the training set, predict on test.
- 6b. Report MAE, RMSE, R² on test — and the same three on train.
- 6c. Compare against the best baseline from Task 5. Better or worse, and by how much?
- 6d. Plot predicted vs actual as a scatter, with a diagonal reference line.

**In comments:**
- Does linear regression need feature scaling here? Answer yes or no and justify it.
- What does the train-vs-test gap tell you?
- If the model beats the mean baseline but loses to `pm_atr14`, what is your verdict?

---

## Task 7 — Where does it fail? (15 min)

Using the test-set predictions from Task 6:

- 7a. Split the actual `pm_range` into 5 quantile buckets.
- 7b. For each bucket: mean actual, mean predicted, MAE.
- 7c. State in one sentence where the model is weakest.

**In a comment:** is the error evenly spread, or concentrated? What would that mean for
someone using this to size a position?

---

**Total: 7 tasks.** Sections 3-4 are the pre-modelling checks - do not skip them to get to the model. Paste solutions and comment answers when done.

Pandas methods you will likely need today — worth knowing cold:
`.mean()` on a 0/1 column, `pd.qcut`, `.merge()`, `.between()`, `sns.heatmap`,
`scipy.stats.normaltest`, `mannwhitneyu`, `pearsonr` / `spearmanr`, `sns.heatmap`,
`scipy.stats.normaltest`, `scipy.stats.mannwhitneyu`, `scipy.stats.pearsonr` / `spearmanr`
