# Weekend Quiz - Week 4

No notes, no running code. Answer from memory. New format this week, per your request:
mostly transfer questions ("would this work in a new/hypothetical situation") rather than
"what happened this week" recall.

---

#Start 11:50

## Part A - Imbalanced classes (new scenario)

You're building a classifier to flag fraudulent credit card transactions. In your training
data, 0.3% of transactions are fraud (even more imbalanced than this week's 4.4%).

**A1.** Would you expect `class_weight='balanced'` to behave similarly to what you saw this
week (mild correction, or the extreme swing you actually got)? Why?

I'd expect an extreme swing, as the penalty for not recognizing 'fraud' would be so high, that we'd get a lot of false positives to avoid that penalty from the model's side. We'd probably get all of the frauds amongst the class labeled as positive, but we'd get a lot of false positives there as well.

**A2.** You train a model and get AUC = 0.95 - very high. Based on what you learned Friday,
what's the FIRST thing you'd want to check before trusting that this model is actually
useful for catching fraud? (Not "is the code right" - a specific thing about the data/features.)


I'd set whether data we get is really available before + check if features we use really make a differenc - if not, it's time to look somewhere else.


**A3.** Someone on your team says "let's just use accuracy to compare our two candidate
models." Give them a one-sentence reason why that's a bad idea here, using a concrete number
(doesn't have to be exact - illustrate the point).


If we're working on frauds that are within 0.3% of all transactions, it's a total disaster as even with 99% accuracy, we would be very far from truth. What matters here is the ability to detect positive cases that are actually positive and avoid false positives as much as possible - as that would cause disruptions we don't want. Every fraud detected is a success and being able to blanace the number of frauds detected with avoiding false positives as much as possible is the key - accuracy does not capture that at all. We'd need to look at precision (how many positives we've labeled as positive are actually positive)/recall scores (how many positives out of all actual positives we've labeled as positive).

---

## Part B - Time-aware evaluation (new scenario)

You're now predicting next-week retail sales using 3 years of weekly historical data.

**B1.** Would a random 80/20 `train_test_split(shuffle=True)` be appropriate here? If not,
what would you do instead, and why does it matter for THIS kind of data specifically (not
just "because we did it that way on the pullback data")?

Shuffle=True is a huge issue, as weekly retail sales may be directly autocorrelated (it's often observed with time series), so it should come in the original order!


**B2.** Suppose your time-aware split gives you a suspiciously perfect result (test MAE
close to zero). Name one concrete way a time-aware split can still leak future information
into training, even though train is entirely before test in time.

Idk - I thought about data changing over time, but it isn't an example of data leak.
Perhaps the features somehow reveal the future for each day, which causes a data leak in every single day and in consequence a data leak in whole dataset.


---

## Part C - Reading model output

**C1.** A logistic regression model gives you `model.coef_` = [0.02, -3.1, 0.15] for
features [temperature, is_weekend, price]. Without knowing anything else about the
business problem - what does the -3.1 tell you, and what does it NOT tell you? (Hint:
think about what you learned distinguishing "strong coefficient" from "leaking feature.")

I'm not sure.



**C2.** You compute precision=0.9, recall=0.2 for a rare event you're trying to detect.
In plain words, describe a real situation where this specific combination (high precision,
low recall) would be the WRONG tradeoff for the business problem - i.e., where you'd
actually want the opposite balance instead.

I imagine detecting cancer (and healthcare in general) would be the kind of a problem where you want high recall for a cost of some false positives and it would make sense. Same for situations which could lead to costly machine stopping/disruptions etc. Perhaps the cost of pre-servicing and leading to some unnecessary repairs would be less costly than actually ignoring the issue until the machine breaks.


---

## Part D - Judgement

**D1.** A colleague built a churn-prediction model and says "AUC is 0.91, ship it." Ask them
one sharp follow-up question, based on this week's experience, before agreeing.

What's the precision/recall score?



**D2.** You're asked to predict whether a rare mechanical failure will happen in the next
24 hours from sensor data (failures: ~1% of readings). Given everything this week covered -
would you reach for class_weight, threshold tuning, more/better features, or a different
target definition FIRST? Defend your ordering in 2-3 sentences - there's no single right
answer, the reasoning is what's graded.

I'd prboably go for threshold tuning and measure the results, while simultaneously looking for better features (trimming the usesless ones, researching for more useful ones - it's always a good deal if a model doesn't work properly).


#FINISH 12:03

---

**7 questions total.** Answer in the same file, under each question, then let me know when
done.
