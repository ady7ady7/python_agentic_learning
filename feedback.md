# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-10
**Session:** ML Phase - Week 3 Day 4 (Kruskal-Wallis hour check, feature table, baseline)
**Score:** pending (see notes below - one real bug, rest solid)
**Difficulty:** 5/10
**Time:** 60 min

---

**Adrian's own summary:** felt shaky overall - unsure about Kruskal-Wallis interpretation
without a post-hoc test, found the groupby/aggregation part fiddly, and wasn't confident
the baseline calculation was methodologically correct or told him anything concrete beyond
"a number".

---

**What actually happened, task by task:**

- **Task 1 (Kruskal-Wallis):** correctly ran `kruskal(*groups)`, correctly read p=4.34e-28
  as "reject H0, at least one hour differs" - this interpretation was right, the uncertainty
  was really about "what next" (post-hoc), which is a legitimate stopping point since no
  post-hoc test was assigned today. One real bug: the per-hour ranking table was built with
  `.agg(median_atr=('mean'))` - the column was named `median_atr` but the aggregation
  function was actually `'mean'`, so the "hour 16 stands out" observation was based on
  means, not medians, and means are pulled around by the same fat right tail we already
  knew about (max depth_atr ≈ 22.9). Re-verified with the real median: hour 16 does not
  stand out as sharply once outliers stop dominating. Adrian's separate instinct - that
  after-hours/pre-market ATR spikes may reflect thin order books rather than real volume -
  was sound reasoning independent of the bug.

- **Task 2 (feature table):** direction encoding, hour, ref_atr, same_candle_pullback all
  reasonable. `prior_pullback_depth` used a plain `shift(1)` across the whole table rather
  than tracking block boundaries (there was no `block_id` column available at the time) -
  a deliberate, acknowledged shortcut rather than an oversight. Checked the actual damage
  together: 4.3% of resumed rows would have been given a prior-pullback value copied in
  from an unrelated, earlier trend block; where both methods produced a value they always
  agreed (0% disagreement) - so the shortcut's cost was bounded and specific (false
  positives on block boundaries), not silent corruption throughout.
  Also independently concluded, before seeing any model result, that predicting an exact
  depth_atr value looks harder than even direction prediction (which has already proven
  weak in past weeks) - and proposed instead modeling P(resumed) vs P(recrossed) as a
  function of depth/context, which mirrors the approach already validated with real signal
  in regimatic-ml's insights_korekty.md (§4, stop-survival tables). This became today's
  plan change for tomorrow.

- **Task 3 (baseline):** MAE calculation was mechanically correct (predict train median/mean,
  score against test via mean_absolute_error). The uncertainty ("does this actually tell me
  something") was resolved together: MAE≈1.0 ATR isn't inherently good or bad - it's only
  meaningful next to the day-3 EU/RTH baselines (also ≈1.0), which makes it a same-magnitude
  sanity check rather than a new result, and sets the bar any future model has to clear.

---

**Housekeeping done after the session (Claude's work, not scored):** added `block_id` to
`03_pullback_target_m15.py` (increments per directional block, not per reference point) and
recomputed `prior_pullback_depth` as `groupby('block_id')['depth_atr'].shift(1)` instead of
a plain shift - closes the gap Adrian flagged, confirmed empirically (4.3% of rows affected,
now fixed by construction). `m15_pullback_events.csv` regenerated with both new columns.

---

**Plan change for next session:** move from regression (predict exact depth_atr) to
conditional classification (P(resumed) vs P(recrossed) given depth reached / hour /
direction), following the stop-survival table pattern from regimatic-ml.

**Reinforce next:** double-checking that an aggregation's column name matches its actual
function (`.agg(name=('function'))` naming vs reality) - the Task 1 bug pattern.
