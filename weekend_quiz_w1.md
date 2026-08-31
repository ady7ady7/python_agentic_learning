# Weekend Quiz - ML Phase Week 1

**Take it Saturday or Sunday, whenever suits you.**
**No notes, no looking things up, no running code.** Write answers from memory.
Where a question asks for code, write it as you would type it - small syntax slips do not
matter, the structure does.

If you do not know something, write "don't know" rather than guessing. That is more useful
to me than a plausible-sounding wrong answer.

---

#Start 14:27

## Part A - Concepts (answer in your own words)

**A1.** What is a baseline, and why is `train_mean` a bad benchmark compared to `atr14`?

Baseline is the raw % of occurences we'd get if we simply took raw data and checked the results with simple statistics/observations. It's necessary to be able to properly see how the ML model really performs - are we getting better results than we'd get if we didn't even use ML?

As for train_mean, IT REALLY depends, as IT'S NOT ALWAYS the case. You're asking me that question in our context, where the train mean is potent to many outliers (some very extreme) + the data's spanned over 6 years and the magnitude's changed, so it's not really showing the current state of things.

And in this context, the atr14 is a self-adjusting metric, which seems to reflect the local volatility quite well.


**A2.** R2 comes back as -0.69. Say precisely what that means. Not "bad" - what specifically?

That means the results do not cover the current variance and they're unreliable. 0.69 would mean they cover 69% of all the possible results, while -69% essentially means they're not trustworthy.



**A3.** Two models on the same data:
```
Model X:  bias = +0.2   MAE = 25
Model Y:  bias = -18    MAE = 19
```
Describe what each one is doing wrong. Which would you rather deploy for position sizing,
and why?


Bias shows the difference between the actual value and the predicted value, it's essentially MAE, but MAE shows ABSOLTUE difference, and bias keeps the direction.

For that reason, I'd stick with MAE for position sizing, as there, we're looking at the magnitude of possible move to not get stopped out, the direction is not that important, as you never knwo the direction anyway. I'd go for model Y then, the bias is worse, but the MAE is closer to the original, more useful model.


**A4.** You have MAE 4.1 on train and MAE 15.0 on test. Name two completely different
explanations for this gap, and say how you would tell them apart.

- data leakage and wrong ML setup - check if model received any data that normally wouldn't be available
- overfitting in terms of data behaviors change over time - e.g. if we use time series data and train data on 6 years of data, the first 4 years could be relatively lwo volatility (these would be used for the training), and then the volatility could increase. And even if we process data properly, it will not be perfroming well, as model received different magnitude of data for training. You can simply check mean baselines, medians etc., and do EDA on train/test sets to check if datasets differ in a meaningful way.


**A5.** Why does a linear regression systematically over-predict the smallest values and
under-predict the largest ones?

It's simply well adjusted to properly perform within the most majority of examples from the dataset, which makes it perfect to predict values within the 0.05 - 0.9 percentile (something like it), but then if there are extreme outliers, it's obviously not adjusted for them. It's like it was trained on some data, which had a certain magnitude and number of occurences. It's either we're able to properly perform most of the values and we accept the fact, that we can't perfeclty predict the extremes, or we aim to predict the extremes, but then we fail at the majority, as our training is highly overshot.

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


a) absolute leak, we wouldn't have that available
b) safe
c) safe
d) leak
e) safe (assuming we predict after eu opens, but that makes sense)

```

**B2.** This line appeared in your code on Day 1:

```python
daily['atr14'] = daily['day_range'].rolling(14).mean()
```

What is wrong with it, and what does the fix look like?

It includes today's range (that nroamlly wouldn't be available ) = data leak
To fix it, you'd simple add .shift(1) to use atr14 based on the previous days, not including today


**B3.** A model scores 0.995 accuracy. Before looking at anything else, what is your first
hypothesis and what would you check first?

A) it's most likely data leakage, as the scenario is nearly unrealistic. I'd check if it has any data that reveals the results and wouldn't normally be available in a real scenario.


---

## Part C - Code from memory

**C1.** Write the code for a baseline that predicts the training median for every test row,
and reports its MAE.

from sklearn.metrics import mean_absolute_error

mean_pred = np.full(len(y_test), y_train.median())
mean_actual = np.full(len(y_test), y_test.median())

train_mae = mean_absolute_error(y_test, mean_pred)
test_mae = mean_absolute_error(y_test, mean_actual)



**C2.** Write the code that produces this table - MAE and bias per quantile bucket of the
actual values:

y_test['bucket'] = pd.qcut(y_test, 5, ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

----

I don't know tbh


```
bucket  mean_actual  mean_pred    mae   bias    n
Q1            22.9       34.5   12.0  +11.5   56
...
```

**C3.** Write the two lines that convert MAE into a scale-free percentage, for train and
test.

Same as above.

---

## Part D - Judgement

**D1.** Your model: MAE 21.2, R2 0.31. Best baseline: MAE 24.0, R2 0.16.
Is this model worth using? Argue either way, but commit to an answer.

It could be useful, as it covers move variance than the baseline + the MAE's also closer to the real values. I'd consider using it, but I'd still probably aim to improve it somehow, maybe also check the results on different Qs and check if I'm somehow able to predict which Q is going to appear, so that I could avoid the extreme values that skew the results.


**D2.** You normalise your target by dividing by ATR14, retrain, and R2 drops to -1.04.
Give two possible explanations and say which you would investigate first.


No idea tbh.


**D3.** Bucket analysis shows MAE of 12 in Q1 and 52 in Q5. Someone wants to use this model
to set stop distances. What do you tell them?


I'd preferably just want to avoid EXTREME CONDITIONS, if possible, knowing that MAE in Q5 also isn't very relevant, as it's driven by extreme outliers. One would definitley want to use the model in lower Qs, if it would somehow be psosible to identify them earlier by any other features/conditions. Difficult to say.

#Finish 14:57

---

**When done, paste your answers and I will score them.**
