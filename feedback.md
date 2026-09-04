# Feedback - Current Session

<!-- Drafted by Claude - correct, add or delete anything that does not match. -->

**Date:** 2026-09-04
**Session:** ML Phase - Week 2 Day 5 (walk-forward + naive baseline, two-session forecast function)
**Score:** pending (Task 1 diagnosis carries to Monday)
**Difficulty:** 5/10
**Time:** ~75 min

---

**What went well:**

- Task 2: correctly diagnosed and fixed the row-shape bug from scratch - `df.iloc[-1]`
  returns a Series, models need 2D input, so `df.iloc[[-1]]` (double brackets at the row-slice
  step) was the fix, then plain single-bracket column selection on the resulting DataFrame
  row (`row[features_us]`). Understood *why*, not just applied the fix.
- Task 2 output (`eu_q50/q80/q90`, `us_q50/q80/q90`) reasoned through clearly: picked
  `eu_q80` as the number that matters for pre-EU-session sizing, explained why q50 is too
  aggressive and q90 likely overkill for the extra safety margin it buys.
- Task 3: sanity-checked predictions against `us_atr14`, judged q80 vs q90 in terms of
  "safety bought per point of range given up" rather than just eyeballing the numbers.
  Correct first move stated for an implausible result: check for a data leak, then the
  features.

---

**Open problem - carries to Monday:**

- Task 1 walk-forward loop: mechanically correct (`test['us_range']` as the reference,
  `start += test_size`), but `model_coverage` and `naive_coverage` both came out far below
  target (~17-23% instead of ~80% for a quantile=0.8 model). Model coverage was *lower*
  than the naive baseline in every fold, which is the actual anomaly worth chasing, not just
  the miss from 80%. Suspected cause: train/test regime mismatch (same class of issue as
  the raw-price-drift bug from D2), not yet confirmed - agreed to check
  `train['us_range'].describe()` vs `test['us_range'].describe()` per fold on Monday.

---

**What to reinforce next:**

- Task 1 diagnosis (Monday)
- Otherwise: this session's real content was integrating two things built separately this
  week (walk-forward loop, forecast function) - worth continuing to combine older material
  rather than only introducing new topics

---

**Anything else:**

