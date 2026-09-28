# Weekend Quiz - Week 5

No notes, no running code. Answer from memory. Same transfer-question format as last week -
judging whether an approach generalizes to a new scenario, not recall of what happened.


#Start 13:24
---

## Part A - Leakage and honest baselines

You're handed a dataset for predicting whether a customer will cancel a subscription next
month. A colleague's model gets AUC = 0.93 using a feature called `days_since_last_login`.

**A1.** Before trusting this feature, what's the FIRST thing you'd check about it, given
what you found with `same_candle_pullback` this month? What would make you suspicious it's a
structural leak rather than genuine signal?

The 'days_since_last_login' could already be a form of leak, as some of these customers will be alreeady people who cancelled subscription will have high days_since_last_login number (it contains the information you need in many cases). It's not 100% sure, but it's possible.


**A2.** Same dataset - someone scaled all numeric features (mean/std normalization) using
statistics computed on the full dataset BEFORE splitting train/test. Explain concretely why
this is a leak, even if train is entirely time-ordered before test.


Because the scaling takes plaes on full dataset, it uses data that wouldn't normally be available and averages train data based on test data as well - it's as simple as that.

---

## Part B - Significance vs effect size

**B1.** You run a Mann-Whitney test comparing conversion rate between two website designs,
with 2 million visitors per group. You get p = 0.0001. A colleague says "huge win, ship
design B." What's your one-sentence pushback, and what number would you ask for next?


It doesn't show which conversion rate is higher, it just shows there's a meaningful difference between the two website designs - nothing about the effect size or strength, pure bullshit. That MW results would essentially mean that some effect IS THERE, and would incite me to do more research to get the proper answers.


**B2.** In your own words: what's the actual mechanical reason a huge sample size makes it
easier to get a tiny p-value even for a practically meaningless difference?

As the dataset's size increases, it builds up more and more range, giving it more chances to actually differ meaningfully from the other set, due to the larger number of samples.



---

## Part C - Model tuning and overfitting

**C1.** A colleague tunes a `RandomForestClassifier` with `RandomizedSearchCV` and reports
"cross-validated AUC = 0.89, best model found." They deploy it. Based on what you learned
this week, what's the one thing you'd want to see before trusting that number - and why isn't
"we used RandomizedSearchCV" enough on its own to rule out overfitting?


I'd check the RandomizedSearch's parameter grid used, as it doesn't protect from overfitting by default - if the parameter values are too big, the overfitting might be an issue anyway, as RSCV automatically picks the best params by score, despite of overfitting (it doesn't check it in any way).


**C2.** Two random forests get nearly the same test AUC (0.75 vs 0.76), but Model A has
train AUC = 0.99 and Model B has train AUC = 0.77. Which would you actually deploy, and why -
answer in terms of what you'd expect from each model on data six months from now, not just
today's test set.

Model B, as it's obviously better suited for predictions, there's practically no overfitting issue. The first model works just a tiny bit better, yet it's adjusted to fit train data almost perfectly, and maybe the test data was also similar to the train data, so it performs relatively well, but as it starts to differ from the train data, the AUC will fall slightly.

**C3.** New scenario: you're tuning a `RandomForestClassifier` and your `param_distributions`
grid includes `max_depth` values from 2 up to 50. Is this grid itself a risk, independent of
whatever `RandomizedSearchCV` picks? Explain why or why not.


I've already kinda explained it in C1, but it could also create another issues, besides just overfitting:
1. It might be difficult to even have 50 depth for simple mechanical reasons, as there might not be neough data, or we'd need absurdly high numbers of rows to make this make sense, AND NOT BE OVERFITTED (practically impossible).
2. Calculating that could also be an issue, but it's RandomizedSearch - we could simply pick a few random iterations, not check the whole grid.

---

## Part D - Reading model output correctly

**D1.** You compute `roc_auc_score(y_test, model.predict(X_test))` and get 0.58. A teammate
computes `roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])` on the SAME model and
gets 0.81. Both ran without errors. Which number is right, and what's actually going on?

The second one is right, as it checks the actual score for predictions on one group (exactly what it is for). The first one makes no sense, as there are two numbers (for both classes predicted), it's skewed and it works as a mean of two scores, practically false.

**D2.** A `RandomForestClassifier`'s `feature_importances_` shows one feature at 0.41 and the
rest below 0.05 each. A colleague says "let's just drop everything except that one feature."
Give one reason this could be a bad idea, and one reason it might actually be fine - i.e.
what would you check before deciding either way?


1. First of all, one would definitley check whether thsi is not some sort of data leakage, whether direct or indirect.

2. Yes, trimming bad features COULD be a very good idea, as then the model would focus more on features that really make the difference in predictions, instead of forcing the features that don't do much and it could improve the score probably. However, it's not always the case, it really depends on the differences, the threshold we set, the number of features etc. In this case, I'd probably still leave at least 2-3 "bad features" to balance it out a bit. Still that's a strong signal to explore data more and engineer more features.


#finish 13:48

---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
