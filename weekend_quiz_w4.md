# Weekend Quiz - Week 4

No notes, no running code. Answer from memory. New format this week, per your request:
mostly transfer questions ("would this work in a new/hypothetical situation") rather than
"what happened this week" recall.

---

## Part A - Imbalanced classes (new scenario)

You're building a classifier to flag fraudulent credit card transactions. In your training
data, 0.3% of transactions are fraud (even more imbalanced than this week's 4.4%).

**A1.** Would you expect `class_weight='balanced'` to behave similarly to what you saw this
week (mild correction, or the extreme swing you actually got)? Why?

**A2.** You train a model and get AUC = 0.95 - very high. Based on what you learned Friday,
what's the FIRST thing you'd want to check before trusting that this model is actually
useful for catching fraud? (Not "is the code right" - a specific thing about the data/features.)

**A3.** Someone on your team says "let's just use accuracy to compare our two candidate
models." Give them a one-sentence reason why that's a bad idea here, using a concrete number
(doesn't have to be exact - illustrate the point).

---

## Part B - Time-aware evaluation (new scenario)

You're now predicting next-week retail sales using 3 years of weekly historical data.

**B1.** Would a random 80/20 `train_test_split(shuffle=True)` be appropriate here? If not,
what would you do instead, and why does it matter for THIS kind of data specifically (not
just "because we did it that way on the pullback data")?

**B2.** Suppose your time-aware split gives you a suspiciously perfect result (test MAE
close to zero). Name one concrete way a time-aware split can still leak future information
into training, even though train is entirely before test in time.

---

## Part C - Reading model output

**C1.** A logistic regression model gives you `model.coef_` = [0.02, -3.1, 0.15] for
features [temperature, is_weekend, price]. Without knowing anything else about the
business problem - what does the -3.1 tell you, and what does it NOT tell you? (Hint:
think about what you learned distinguishing "strong coefficient" from "leaking feature.")

**C2.** You compute precision=0.9, recall=0.2 for a rare event you're trying to detect.
In plain words, describe a real situation where this specific combination (high precision,
low recall) would be the WRONG tradeoff for the business problem - i.e., where you'd
actually want the opposite balance instead.

---

## Part D - Judgement

**D1.** A colleague built a churn-prediction model and says "AUC is 0.91, ship it." Ask them
one sharp follow-up question, based on this week's experience, before agreeing.

**D2.** You're asked to predict whether a rare mechanical failure will happen in the next
24 hours from sensor data (failures: ~1% of readings). Given everything this week covered -
would you reach for class_weight, threshold tuning, more/better features, or a different
target definition FIRST? Defend your ordering in 2-3 sentences - there's no single right
answer, the reasoning is what's graded.

---

**7 questions total.** Answer in the same file, under each question, then let me know when
done.
