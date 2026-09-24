# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-24
**Session:** ML Phase - Week 5 Day 4 (RandomizedSearchCV, TimeSeriesSplit, fixing overfitting)
**Score:** ~85% - real multi-step scorer bug, self-diagnosed and resolved with guidance
**Difficulty:** 5/10 (Adrian's own rating)
**Time:** ~1h

---

**What actually happened, task by task:**

- **Warm-up:** correct on the first try, no issues.

- **Task 1 (why CV before tuning):** correctly explained why tuning against the test set
  directly is a form of leakage even without future data being involved. Built and inspected
  `TimeSeriesSplit` output correctly to see its shape before using it for real.

- **Task 2 (RandomizedSearchCV) - real bug, multi-step, self-diagnosed:** first attempt used
  `make_scorer(roc_auc_score)` with no probability handling - defaults to scoring on
  `.predict()` output (binary), the SAME class of mistake flagged twice before this month
  (Week 4 Day 4, Week 5 Day 1), this time hidden inside a search tool rather than a direct
  call. Got `best_score_` = nan and suspiciously poor params - correctly went to sklearn docs
  independently rather than accepting the bad result, found and tried `make_scorer(...,
  needs_proba=True)`. That parameter is deprecated in the installed sklearn version and
  raised once `error_score='raise'` was added to reveal what a silent nan was hiding -
  resolved by switching to the current API, `make_scorer(roc_auc_score,
  response_method='predict_proba')`. End state: tuned RF found `max_depth=3,
  min_samples_leaf=10, n_estimators=200`, test AUC = 0.730 (vs yesterday's overfit default RF
  at 0.633, and logistic regression's 0.735 - now essentially tied).

- **Task 3 (overfitting gap, post-tuning):** initially compared a train-AUC number (0.9999)
  computed BEFORE the scorer fix against test AUC computed after - a within-session
  apples-to-oranges mixup, clarified once asked which model was actually being evaluated;
  Adrian correctly explained the timeline himself once prompted. Once both numbers came from
  the same (correctly-tuned) model: train AUC 0.736 vs test AUC 0.730 - gap collapsed from
  0.367 (yesterday's overfit default) to ~0.006. Directly demonstrates the mechanism Adrian
  asked about yesterday: an unconstrained tree memorizes training noise, a shallow
  (max_depth=3) one generalizes.

---

**Real takeaway, stated explicitly by Adrian:** wants to genuinely master handling
overfitting in tree-based models (RF, XGBoost) rather than just knowing the term - today
gave him a concrete before/after (gap 0.367 -> ~0.006) tied to one specific lever
(max_depth), which is a solid first real data point toward that goal.

**Reinforce next:** `make_scorer` needs explicit probability handling
(`response_method='predict_proba'`, not the deprecated `needs_proba`) whenever the
underlying metric (like ROC AUC) needs probabilities - this is now the third occurrence of
the general predict-vs-predict_proba confusion, this time one layer deeper inside a
search/scoring wrapper rather than a direct metric call. Also: double-check which model
object a metric is being computed against mid-session, especially after refitting with new
parameters under the same variable name.

**Open question carried to tomorrow:** now that tuned RandomForest (0.730) and logistic
regression (0.735) are essentially tied on this dataset, is RandomForest still worth pursuing
here, or does this confirm the Week 5 Day 1 finding that the FEATURE SET has a low ceiling
regardless of algorithm choice? Also: revisit the new CV-portfolio-project discussion
(paused this week, no domain/dataset landed yet).
