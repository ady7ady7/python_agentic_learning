# Weekend Quiz - Week 5

No notes, no running code. Answer from memory. Same transfer-question format as last week -
judging whether an approach generalizes to a new scenario, not recall of what happened.

---

## Part A - Leakage and honest baselines

You're handed a dataset for predicting whether a customer will cancel a subscription next
month. A colleague's model gets AUC = 0.93 using a feature called `days_since_last_login`.

**A1.** Before trusting this feature, what's the FIRST thing you'd check about it, given
what you found with `same_candle_pullback` this month? What would make you suspicious it's a
structural leak rather than genuine signal?

**A2.** Same dataset - someone scaled all numeric features (mean/std normalization) using
statistics computed on the full dataset BEFORE splitting train/test. Explain concretely why
this is a leak, even if train is entirely time-ordered before test.

---

## Part B - Significance vs effect size

**B1.** You run a Mann-Whitney test comparing conversion rate between two website designs,
with 2 million visitors per group. You get p = 0.0001. A colleague says "huge win, ship
design B." What's your one-sentence pushback, and what number would you ask for next?

**B2.** In your own words: what's the actual mechanical reason a huge sample size makes it
easier to get a tiny p-value even for a practically meaningless difference?

---

## Part C - Model tuning and overfitting

**C1.** A colleague tunes a `RandomForestClassifier` with `RandomizedSearchCV` and reports
"cross-validated AUC = 0.89, best model found." They deploy it. Based on what you learned
this week, what's the one thing you'd want to see before trusting that number - and why isn't
"we used RandomizedSearchCV" enough on its own to rule out overfitting?

**C2.** Two random forests get nearly the same test AUC (0.75 vs 0.76), but Model A has
train AUC = 0.99 and Model B has train AUC = 0.77. Which would you actually deploy, and why -
answer in terms of what you'd expect from each model on data six months from now, not just
today's test set.

**C3.** New scenario: you're tuning a `RandomForestClassifier` and your `param_distributions`
grid includes `max_depth` values from 2 up to 50. Is this grid itself a risk, independent of
whatever `RandomizedSearchCV` picks? Explain why or why not.

---

## Part D - Reading model output correctly

**D1.** You compute `roc_auc_score(y_test, model.predict(X_test))` and get 0.58. A teammate
computes `roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])` on the SAME model and
gets 0.81. Both ran without errors. Which number is right, and what's actually going on?

**D2.** A `RandomForestClassifier`'s `feature_importances_` shows one feature at 0.41 and the
rest below 0.05 each. A colleague says "let's just drop everything except that one feature."
Give one reason this could be a bad idea, and one reason it might actually be fine - i.e.
what would you check before deciding either way?

---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
