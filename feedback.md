# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-19
**Session:** ML Phase - Week 9 Day 1 (leak persisted after the "obvious" fix - found the real, deeper mechanism)
**Score:** ~85% - correct mechanics throughout, a genuinely sharp diagnostic push that found the actual root cause
**Difficulty:** 4-5/10 (Adrian's own rating)
**Time:** ~1h

---

**What actually happened, task by task:**

- **Task 0 (confirm the leak):** correctly computed the correlation between
  `realized_power` and `target_volatility_rose` (-0.37) - correctly recognized this is
  still a strong relationship (stronger than any legitimate effect found this month, where
  Cohen's d topped out around 0.25) even though the raw correlation number alone looked
  smaller than expected at first glance.

- **Task 1 (remove leaking features, re-screen) - the real finding:** removed
  `realized_power`/`volatility_ratio`/`relative_rp` and re-ran the screen. The table came
  back numerically IDENTICAL to Friday's leaked version for every remaining feature
  (`atr14` d=-0.39, `wtc_10` d=0.57, etc.) - a strong, if initially unflagged, signal that
  the remaining features carry the same problem independently of the three removed ones.

- **Task 2 (re-fit):** correctly executed the full discipline checklist again. Result: gap
  between train (0.56) and test (0.77-0.80) AUC persisted essentially unchanged - correctly
  flagged as "still weird" rather than accepted at face value, even without yet knowing why.

- **Task 3 + follow-up discussion - the real diagnostic work:** pushed back hard and
  correctly on an early hypothesis that `atr14` must be dropped simply for being
  conceptually "about volatility," rightly pointing out that volatility autocorrelation is
  real and well-established and it would be absurd to ban using past volatility to predict
  future volatility. This forced a sharper diagnosis: verified directly
  (`all_targets_df[['et_time','atr14','realized_power']]`) that `atr14` and
  `realized_power` move together IN THE SAME ROW, confirming both are measured at the exact
  same moment as the target's own reference point (`rp_at_event`) - the actual problem is
  not "using volatility as a feature" (legitimate) but "the feature and the target's
  reference point occupy the identical moment in time" (a structural leak, not a temporal
  one - `shift(1)` alone would not fix this, since no future data is involved, just a
  shared anchor point). Correctly rejected a proposed fix (lagging `rp_at_event`) as
  insufficient on its own, and independently proposed the right general-purpose structure:
  a clean observation window -> gap -> prediction window, with features built entirely from
  the first and the target entirely from the third, so no feature can mathematically share
  a timestamp with the target's anchor by construction.

---

**Real outcome:** a genuinely deeper, better understanding of WHY the leak persisted after
the "obvious" fix - this is a more subtle and more generally useful lesson than Friday's
original leak (shared raw material was easy to spot; shared TIMING of an otherwise-unrelated
feature and a target's reference point is a much easier mistake to make unknowingly).

**Reinforce next:** the distinction between temporal leakage (using future data - what
`shift`/time-splits guard against) and structural/reference-point leakage (a feature and a
target's own anchor measured at the identical moment, regardless of whether anything
"future" is touched) - this is a new, more general pattern worth remembering explicitly,
since it will recur any time a target is defined relative to a feature's own value.

**Carries forward, agreed plan:** rebuild the target using a clean three-window structure
(observation window for features -> gap -> prediction window for the target, no overlap).
Additionally, Adrian wants to move away from arbitrary bar-count windows (10/20 bars) toward
windows anchored to real market structure (session opens/specific times of day with known
liquidity patterns) for testing volatility predictability - a more principled choice than
round numbers picked for convenience.
