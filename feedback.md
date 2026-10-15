# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-15
**Session:** ML Phase - Week 8 Day 4 (RF vs XGBoost on the full ~18-feature set, honest weak result)
**Score:** ~90% - flawless overfitting discipline, one real interpretive slip caught and corrected
**Difficulty:** 5/10 (Adrian's own rating)
**Time:** ~60 min (focused)

---

**What actually happened, task by task:**

- **Task 1 (feature table + split):** clean, all ~18 features confirmed present with zero
  NaNs, time-aware split done correctly.

- **Task 2 (RandomForest):** bounded grid, `RandomizedSearchCV` + `TimeSeriesSplit`, correct
  train vs test AUC comparison. Result: train=0.560, test=0.541 - tiny gap (~0.02), textbook
  healthy generalization, but test AUC is actually BELOW Friday's weak 4-feature baseline
  (0.561). Correctly flagged the surprise rather than hiding it.

- **Task 3 (XGBoost):** same discipline, same grid shape validated in Week 6. Result:
  train=0.560, test=0.550 - again a tiny gap, again roughly at/below the Friday baseline.
  One interpretive slip here, corrected: read AUC≈0.55 as "55% chance of catching reversals
  instead of 13%" - this conflates AUC (a ranking metric: given one random continuation and
  one random reversal, how often the model scores them in the right relative order) with a
  practical detection rate. AUC near 0.5 means close to NO real ranking power, regardless of
  which class you frame the question around - corrected in-session.

- **Task 4 (feature importances):** correctly observed no dominant feature in either model
  (all in the 0.02-0.10 range) and correctly concluded there's no principled cutoff for
  trimming anything - an honest "difficult to make a decision" rather than forcing a
  narrative onto noisy importances.

---

**Real outcome - a genuine, well-earned negative result:** a full week of research-grounded
feature engineering (14 new features, each individually screened, several with real if
modest univariate effects) plus two properly-tuned models produced essentially the SAME
weak result as Friday's thin 4-feature baseline. This is strong evidence the bottleneck is
the TARGET (predicting direction/continuation at this M15 horizon from OHLC-derived
features), not insufficient features or poor tuning - Adrian reached this same conclusion
independently, citing parallel research he's doing elsewhere pointing the same direction.

**Reinforce next:** AUC's precise meaning (ranking/ordering probability between a random
positive and random negative pair) vs. informal "percent chance of catching X" language -
this is a recurring soft spot worth a clean restatement next time AUC comes up in a new
context, though the instinct to flag the surprising result himself was the important part
and that worked well.

**Carries forward, agreed plan:** rather than closing out the continuation-target thread
entirely, try pivoting to a DIFFERENT target on the same rich feature set - predicting
volatility (does realized volatility rise or fall after an extreme event) instead of
direction/continuation. Adrian's own instinct, grounded in literature from this week
(volatility clustering/persistence is a much stronger, better-established property than
return/direction predictability) - a reasonable next experiment before concluding the whole
feature set is unusable.
