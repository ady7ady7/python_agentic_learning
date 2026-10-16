# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-16
**Session:** ML Phase - Week 8 Day 5 (volatility target pivot - strong results, but a real leak needs fixing Monday)
**Score:** ~80% - clean mechanics throughout, but the suspiciously strong Task 3 result is leakage, correctly self-flagged ("OR THERE IS A TRAP") though not yet fixed
**Difficulty:** 5-6/10 (Adrian's own rating)
**Time:** ~1h10 (started late, stayed focused)

---

**What actually happened, task by task:**

- **Task 1 (volatility target):** correctly built `target_vol_rose` from comparing
  `realized_power` at the event vs. 20 bars later. Class balance came out 44.5%/55.5% -
  genuinely much more balanced than `target_continued`'s 83.6/13.4, as hoped.

- **Task 2 (univariate screen):** ran the Mann-Whitney + Cohen's d screen across all 18
  features. Results looked dramatically stronger than any direction-target screen this
  project (`realized_power` d=-0.82, `relative_rp` d=-0.85, `volatility_ratio` d=-0.81 -
  versus a max of d≈0.16 for the continuation target). Adrian noted the jump in effect
  sizes but did not yet connect it to a methodological cause.

- **Task 3 (modeling) - the real issue:** RF test AUC=0.80, XGBoost test AUC=0.77 - both
  dramatically higher than yesterday's ~0.54-0.55, AND both showing test AUC far ABOVE
  train AUC (0.56) - an inverted, highly unusual pattern that is itself a red flag (normal
  overfitting shows the opposite: train >> test). Adrian correctly sensed something was off
  ("the results are weird... OR THERE IS A TRAP") without pinning down the exact mechanism.

---

**Root cause identified (not yet fixed - deferred to next week per Adrian's explicit
end-of-week call):** `realized_power` was used simultaneously as (a) the raw material the
TARGET is defined from (`target_vol_rose` = whether `realized_power` is higher 20 bars
later than at the event) and (b) a FEATURE fed directly into the model. Worse,
`volatility_ratio` and `relative_rp` are both themselves built as ratios/transformations of
`realized_power` - so three of the "features" are mathematically entangled with the
target's own construction, not independent signal. This explains both the implausibly
large Cohen's d values in Task 2's screen and the inverted train/test AUC pattern in Task
3 - this is leakage, not a genuine breakthrough. Adrian was told the fix (drop
`realized_power`/`volatility_ratio`/`relative_rp` from the feature list, keep them only in
the target's own construction, then re-screen and re-fit) but explicitly chose to leave it
for next week rather than fix it tonight (Friday, late) - a reasonable call on timing, not
a disagreement about the diagnosis.

---

**Reinforce next:** whenever a target is built from the same underlying quantity used as a
feature (realized_power here), that feature - and anything DERIVED from it - must be
excluded from the model's inputs. This is the same leakage family as `same_candle_pullback`
from the earlier pullback-classifier project, just appearing in a different construction
pattern (shared raw material between target and feature, not a structurally-impossible
value). Also: an inverted train/test AUC gap (test > train) is itself a diagnostic red flag
worth checking immediately, not just a pleasant surprise.

**Carries forward, explicit next step:** Monday - drop `realized_power`,
`volatility_ratio`, `relative_rp` from the feature list for the volatility target, re-run
the Task 2 screen and Task 3 models on the cleaned set, and see what (if anything) survives
as a genuine effect. Also noted from the week-wrap-up comment: Adrian wants to start
building toward genuinely deployable/effective models rather than endless target
exploration, and separately raised interest in unsupervised approaches (k-means on trend
features) and breakout-validity classification with metalabeling as possible future
directions - flagged as his own ideas to revisit, not committed to yet.
