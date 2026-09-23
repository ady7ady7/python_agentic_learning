# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-23
**Session:** ML Phase - Week 5 Day 3 (Cohen's d, RandomForestClassifier, overfitting check)
**Score:** ~95% - one small formula slip, immediately self-flagged as suspicious
**Difficulty:** 5/10 (Adrian's own rating - "nic szczególnie trudnego, fajne i przydatne")
**Time:** ~1h10

---

**What actually happened, task by task:**

- **Warm-up (group-vs-group Mann-Whitney, no worked example):** clean, correct setup on the
  first try (`direction` bull vs bear on `ref_atr`), including writing out which two things
  were being compared before running the test - exactly the forcing-function habit intended.
  Adrian noted this pattern (and the general "which two groups" setup) is worth periodically
  repeating with other test variants to keep it locked in - a good self-directed instinct.

- **Task 1 (Cohen's d) - small bug, self-flagged:** first formula had a parenthesization slip
  - `np.sqrt(a**2 + b**2) / 2` instead of `np.sqrt((a**2 + b**2) / 2)` (dividing by 2 outside
  vs. inside the square root - mathematically different operations). Got d = -0.51, then
  correctly sensed the number didn't sit right against yesterday's "weak effect" conclusion
  and asked about it rather than accepting it. After correcting to the proper pooled-std
  formula, got d = -0.36 (small-to-medium effect) - consistent with yesterday's finding.
  Also explicitly said he won't memorize the formula by heart but knows Cohen's d exists and
  where to look it up - a reasonable, honest scope for this tool at his current stage.

- **Task 2 (RandomForestClassifier):** correct implementation. Got a genuinely interesting,
  correctly-interpreted result: default RF scored WORSE on AUC (0.633) than yesterday's
  logistic regression (0.735), despite feature importances looking more "balanced" across
  features than the logistic coefficients - correctly reasoned through this apparent
  contradiction rather than assuming a coding error, flagging it as an open, real finding.

- **Task 3 (overfitting check):** correctly computed train AUC = 1.0 vs test AUC = 0.633 -
  a textbook overfitting signature, correctly diagnosed. Asked a mature methodological
  question about whether hyperparameter tuning should be done manually (building intuition)
  or via search (RandomizedSearchCV/GridSearchCV) - flagged as a good topic for a future
  session rather than resolved today.

---

**Reinforce next:** none newly flagged - this session's slip (parenthesization in a formula)
is a one-off arithmetic error, not a conceptual gap, and was caught by Adrian's own number
sense before correction was needed.

**Carries to next session:** RandomForest is currently underperforming logistic regression
due to overfitting (train AUC 1.0) - natural next step is hyperparameter tuning
(`max_depth`, `min_samples_leaf`, etc.), ideally via a proper search method per Adrian's own
question today, rather than manual guessing.
