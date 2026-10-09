# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-09
**Session:** ML Phase - Week 7 Day 5 (first classifier on the continuation target, week wrap-up)
**Score:** ~90% - correct, honest execution throughout, model itself turned out weak (a real result, not an error)
**Difficulty:** 4/10 (today specifically), 6/10 for the week overall (Adrian's own ratings)
**Time:** ~45 min

---

**What actually happened, task by task:**

- **Warm-up:** correct, mirrored Thursday's pattern on the opposite tail cleanly.

- **Task 1 (baseline logistic regression):** correctly fit on train, correctly used
  `predict_proba` (not `.predict()`) for ROC AUC - test AUC 0.561, essentially barely above
  a coin flip, honestly reported as "absolutely useless" rather than dressed up. Correctly
  reasoned about the direction of a 0.56 AUC's practical meaning relative to the 83.6/13.4
  base rate. Coefficient table correctly built and read: `direction` clearly dominant (0.303),
  `atr14` secondary (0.104), `hour`/`abs_z_score` negligible - consistent with the known
  high/low asymmetry from earlier this week.

- **Task 2 (precision/recall on minority class) - real, correctly diagnosed finding:**
  default-threshold model got precision=0.0, recall=0.0 on the reversed class - correctly
  self-diagnosed as "model is unable to predict ANY reversed instance" (confirmed by checking
  there genuinely were 83 reversed instances in test, ruling out a data/split bug).
  Independently went further than asked and tried `class_weight='balanced')` as a next step -
  AUC unchanged (0.561, same weak signal) but precision/recall moved to 0.114/0.061 - still
  weak, correctly read as "a bit better, yet still worse than baseline."

- **Task 3 (week wrap-up):** honest, clear-eyed self-assessment. Named the episode-vs-row
  distinction as the most valuable concept from the week. Explicitly flagged not fully
  grasping the drift-removal fix (addressed in-session afterward with a concrete numeric
  walkthrough - gold drifting $1/bar means raw future-return always carries that +$20 over
  20 bars regardless of any real reversion/continuation behavior, while measuring against
  the rolling mean nets that shared drift out) and confirmed it landed as a real, standard
  technique (detrending / Bollinger-Bands-style residual, not an ad-hoc trick) once explained
  that way. Also candidly named the stateful-function work from Thursday as something that
  needs real, repeated practice while tired, not just conceptual understanding.

---

**Real outcome:** the model itself is weak (AUC ~0.56, can't usefully separate the minority
class even with class_weight) - a genuine, honestly-reached result, not a bug. Given the
high/low asymmetry dominates the one useful coefficient, the four mechanical features tried
today may simply not carry enough signal for this specific target - consistent with the
broader pattern seen in the pullback project too.

**Reinforce next:** drift-removal/detrending logic - landed today with a concrete worked
example, but given his own math-gap self-assessment, this is worth a light re-touch in a
different context later this month (he explicitly values repetition across contexts, not a
single explanation).

**Carries forward, Adrian's explicit ask:** wants a genuinely useful/successful model result
at some point, not just "learned the ML flow" - flagged as aspirational, with appropriate
honesty that market data may or may not cooperate. Also: continue the already-flagged need
for deliberate practice on iterative/stateful functions and vectorized-pandas alternatives.
