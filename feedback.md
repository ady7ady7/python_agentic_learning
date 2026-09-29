# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-29
**Session:** ML Phase - Week 6 Day 2 (fair XGBoost tuning, B2 revisited)
**Score:** ~80% - a genuinely useful negative result, framed by Adrian as less successful than it was
**Difficulty:** 3-4/10 (Adrian's own rating)
**Time:** ~1h

---

**What actually happened, task by task:**

- **Warm-up:** correct, both methods (list comprehension + boolean-mask `.sum()`) agreed
  (1831). Found the double-check step "kinda weird" - flagged as worth keeping anyway: this
  cross-check is exactly what PROVES a filter condition is right rather than just believed
  to be right, not a redundant step even when it feels obvious in hindsight.

- **Task 0 (B2, second pass):** closer than the first attempt but still leaned on "more room
  to pick evidence" phrasing rather than "measurement precision." Worked through a coin-flip
  analogy (10 flips can easily show 70% heads on a fair coin by pure noise; 10,000 flips
  reliably lands near the true 50% - the coin's fairness never changes, only how precisely
  the MEASUREMENT reflects it). Adrian's own restatement afterward was noticeably closer
  ("at large numbers, reality reveals itself") - correctly self-aware that his math
  background is a genuine gap here, not something to force-fix in one sitting. Deliberately
  not drilled further today per the "repeat across different contexts, not in a loop" rule -
  will resurface naturally next time a stats test comes up.

- **Task 1 (fair XGBoost tuning):** properly executed - bounded parameter grid from the
  start (no repeat of the too-wide-grid mistake), `TimeSeriesSplit`, correct
  `response_method='predict_proba'` scorer, evaluated on real test set rather than trusting
  `.best_score_`. Result: test AUC 0.754 (essentially tied with RF's 0.758), train AUC 0.889
  (gap ~0.135, versus RF's near-zero gap) - a real, still-present overfitting tendency even
  after fair tuning.

- **Task 2 (feature importance comparison):** correctly found `atr_zscore_in_block` still
  gets diluted in XGBoost (0.143, not the top feature) even under proper tuning, unlike RF
  where it stays dominant (0.365). Read this as "today's tuning effort didn't give much" -
  reframed together: this is actually the valuable result of the day. Yesterday's RF-vs-
  XGBoost hypothesis was based on an UNFAIR comparison (tuned RF vs untuned XGBoost); today
  gives a FAIR comparison and the same qualitative pattern holds (RF exploits one dominant
  feature better, XGBoost's sequential correction dilutes it) - upgrading the conclusion from
  "plausible guess" to "tested and confirmed," which is real progress even though the
  practical choice of model (RF) didn't change.

---

**Process note, communicated directly this session:** Adrian described today as "not a
massive success" / "didn't move forward" - pushed back on gently: a well-designed experiment
that confirms a hypothesis with a fair test is a genuine result, not a null outcome, even
when the headline number (test AUC) barely moved. Worth remembering this framing distinction
for future sessions where a fair re-test just confirms yesterday's guess.

**Reinforce next:** B2's mechanical explanation - visibly closer today, not yet fully
internalized in his own words. Let it resurface naturally in a different stats context
rather than re-drilling it directly.

**Carries forward:** RF remains the better-suited model for this specific feature set
(one dominant feature, several weak ones) - now backed by a fair, controlled comparison
rather than an unfair one. No open model-comparison threads remain for this project unless
new features change the picture.
