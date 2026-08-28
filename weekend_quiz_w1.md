# Weekend Quiz - ML Phase Week 1

**Take it Saturday or Sunday, whenever suits you.**
**No notes, no looking things up, no running code.** Write answers from memory.
Where a question asks for code, write it as you would type it - small syntax slips do not
matter, the structure does.

If you do not know something, write "don't know" rather than guessing. That is more useful
to me than a plausible-sounding wrong answer.

---

## Part A - Concepts (answer in your own words)

**A1.** What is a baseline, and why is `train_mean` a bad benchmark compared to `atr14`?

**A2.** R2 comes back as -0.69. Say precisely what that means. Not "bad" - what specifically?

**A3.** Two models on the same data:
```
Model X:  bias = +0.2   MAE = 25
Model Y:  bias = -18    MAE = 19
```
Describe what each one is doing wrong. Which would you rather deploy for position sizing,
and why?

**A4.** You have MAE 4.1 on train and MAE 15.0 on test. Name two completely different
explanations for this gap, and say how you would tell them apart.

**A5.** Why does a linear regression systematically over-predict the smallest values and
under-predict the largest ones?

---

## Part B - Leakage (the important part)

**B1.** You are predicting `eu_range` (03:00-09:55 ET) using yesterday's data only.
For each feature below: safe or leaking? If leaking, say exactly what it reveals.

```
a)  eu_close_loc          - where today's EU close sits in today's EU range
b)  prev_us_range         - yesterday's US session range
c)  eu_atr14              - 14-day mean of eu_range, shifted by 1
d)  eu_bar_rng_mean       - mean 5-min bar range across today's EU session
e)  gap = eu_open - prev_us_close
```

**B2.** This line appeared in your code on Day 1:

```python
daily['atr14'] = daily['day_range'].rolling(14).mean()
```

What is wrong with it, and what does the fix look like?

**B3.** A model scores 0.995 accuracy. Before looking at anything else, what is your first
hypothesis and what would you check first?

---

## Part C - Code from memory

**C1.** Write the code for a baseline that predicts the training median for every test row,
and reports its MAE.

**C2.** Write the code that produces this table - MAE and bias per quantile bucket of the
actual values:

```
bucket  mean_actual  mean_pred    mae   bias    n
Q1            22.9       34.5   12.0  +11.5   56
...
```

**C3.** Write the two lines that convert MAE into a scale-free percentage, for train and
test.

---

## Part D - Judgement

**D1.** Your model: MAE 21.2, R2 0.31. Best baseline: MAE 24.0, R2 0.16.
Is this model worth using? Argue either way, but commit to an answer.

**D2.** You normalise your target by dividing by ATR14, retrain, and R2 drops to -1.04.
Give two possible explanations and say which you would investigate first.

**D3.** Bucket analysis shows MAE of 12 in Q1 and 52 in Q5. Someone wants to use this model
to set stop distances. What do you tell them?

---

**When done, paste your answers and I will score them.**
