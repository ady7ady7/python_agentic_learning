# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-02
**Session:** ML Phase - Week 6 Day 5 (half-life window table, z-score feature, first predictive check)
**Score:** ~88% - strong, independent work throughout, one real open question surfaced at the end
**Difficulty:** 5/10 (Adrian's own rating)
**Time:** ~1h15

---

**What actually happened, task by task:**

- **Warm-up:** correct, simple plain-mean variant of the dict comprehension pattern - fine.

- **Task 1 (half-life across window sizes):** well-executed table-building, including a
  smart choice to batch all rolling-window columns before a single `dropna()` rather than
  dropping NaNs per-window (avoiding unnecessary row loss) - a real, independently-reasoned
  efficiency improvement, not something asked for. Correctly read the monotonic
  window-to-half-life relationship (8.7 bars at window=20 up to 93.4 at window=200). Asked
  what the 22-33 bar half-life numbers mean practically - resolved together: at M15, ~22
  bars is ~5.5 hours, meaning a reversion-based holding horizon should be measured in hours,
  not days (too slow) or minutes (too fast for the effect to materialize).

- **Task 2 (z-score feature):** thorough, went beyond the ask - computed `.describe()`,
  correctly read the distribution as roughly centered and symmetric, plotted a histogram,
  and UNPROMPTED ran `scipy.stats.normaltest` to formally check normality rather than relying
  on the "looks bell-shaped" visual impression - found p≈1.3e-111, correctly concluding the
  distribution is NOT formally normal despite looking like it (fat tails, typical of
  financial data) - a genuinely sharp, self-directed verification instinct. Also explored
  percentile thresholds (1%/5%/95%/99%) to judge signal frequency at different z cutoffs
  before committing to one.

- **Task 3 (does z-score predict reversion?) - real open finding, not yet resolved:**
  correctly built the forward-looking `future_return_20` target and split by z-score group.
  BUT the actual numbers point the OPPOSITE direction from mean-reversion: `z < -2`
  (unusually low price) showed mean future_return = -0.226 (continuing down), while `z > 2`
  (unusually high price) showed mean future_return = +1.008 (continuing up) - this reads as
  MOMENTUM, not reversion, directly in tension with Task 1's ADF/half-life findings
  supporting reversion. Adrian's own interpretation ("some evidence of mean-reversion in
  there") doesn't match the sign of these numbers - flagged together as the real open
  question, not yet resolved with a formal test. Adrian explicitly asked how to check this
  "czarno na białym" (in black and white) without being biased by eyeballing - correctly
  identifying that visual histogram comparison isn't rigorous enough and a formal test
  (Mann-Whitney, same tool from Week 3/5) is the right next move - deferred to tomorrow with
  a fresh mind rather than rushed today.

---

**Reinforce next:** none new - today showed strong independent statistical instincts
(normaltest, percentile exploration, catching his own interpretation might not match the
numbers). The open item is a real analysis question, not a skill gap.

**Carries forward (priority for tomorrow):** resolve the Task 3 contradiction properly -
run Mann-Whitney comparing future_return_20 between the z<-2 and z>2 groups (and against the
normal-range group) to get a real p-value and effect size, rather than relying on
`.describe()` and histogram comparison. If momentum is confirmed over reversion at this
horizon (N=20 bars forward), that's a genuinely important pivot for this entire research
direction - worth treating as a serious finding, not a bug to explain away.
