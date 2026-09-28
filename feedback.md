# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-28
**Session:** ML Phase - Week 6 Day 1 (consolidated RF pipeline, first XGBoost attempt)
**Score:** ~85% - one concept not yet landed (B2), one fair pushback on an unscaffolded question, strong independent synthesis at the end
**Difficulty:** 5/10 (Adrian's own rating)
**Time:** ~1h30

---

**What actually happened, task by task:**

- **Warm-up:** correct, clean per-direction inline median comparison, matches the intended
  pattern exactly.

- **Task 0 (B2 quiz fix):** first restatement still framed it as "more room/chances to find
  differences" - the same imprecise mental model as the original quiz answer, not yet fully
  replaced by the "precision of measurement via 1/sqrt(n) shrinking standard error" framing.
  Worked through with a concrete example (a fixed true difference of 1 unit, same at any n;
  only the noise around measuring it shrinks) - not confirmed fixed by end of session, worth
  a very quick recheck next time it comes up rather than a full task.

- **Task 1 (consolidated RF pipeline):** clean reproduction of Friday's known-good bounded
  RandomForest config. Result: test AUC 0.758, train AUC 0.733 (test slightly ABOVE train,
  a healthy sign, no overfitting), `atr_zscore_in_block` still dominant (0.365 importance).
  Minor process note (not a real error): left a stale inline comment with an old printed
  value next to a `print()` statement, which looked like a data inconsistency until clarified
  - worth clearing stale comments when reusing code blocks across tasks.

- **Task 2 (XGBoost) - fair, justified pushback on scope:** the closing question asked him to
  reason about why a lower learning_rate + more trees INCREASED overfitting rather than
  reducing it, without ever having been taught the underlying mechanism
  (total fitting capacity ~ n_estimators * learning_rate) - a real violation of this track's
  own "new technique = worked example first" rule, and Adrian correctly called it out rather
  than guessing blindly. Explained directly instead: n_estimators tripled (100->300) while
  learning_rate only halved (0.1->0.05), so total capacity rose, not fell. Results: XGBoost
  underperformed the tuned RF on both metrics (test AUC 0.70-0.71 vs RF's 0.758, train/test
  gap 0.20-0.24 vs RF's near-zero) with default-ish, untuned settings.

- **Independent synthesis (strong, unprompted):** correctly connected the RF-vs-XGBoost
  architecture difference (parallel independent trees vs. sequential error-correcting trees)
  to WHY XGBoost's feature importances were far more spread out than RF's (each new tree
  hunts for remaining error once earlier trees "used up" the dominant feature's signal).
  Proposed a broader hypothesis (RF better exploits one standout feature among weak ones;
  XGBoost favors environments with several genuinely strong features) - a reasonable,
  well-reasoned idea, refined together: true specifically for TODAY'S small dataset with
  UNTUNED XGBoost params, not a safe general claim about the algorithm, since XGBoost often
  outperforms RF on single-dominant-feature problems once properly tuned (RF's own first
  attempt last week was just as badly overfit before tuning fixed it).

---

**Reinforce next:** B2's mechanical explanation (standard error shrinking via 1/sqrt(n)) -
still not fully replacing the "more room to differ" framing after one pass. Also: a reminder
to myself/going forward - don't ask a "why did X happen" question about a mechanism that
hasn't been taught yet; teach it first, consistent with this track's own standing rule.

**Carries forward:** XGBoost has not been given a fair, tuned shot yet (only default-ish
params tried) - if returning to model comparison, tune it properly (RandomizedSearchCV +
early_stopping) before drawing conclusions about it versus RandomForest.
