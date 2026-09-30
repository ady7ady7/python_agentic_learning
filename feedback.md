# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-09-30
**Session:** ML Phase - Week 6 Day 3 (new direction: mean-reversion toolkit - ADF, Hurst, half-life)
**Score:** ~85% - two tasks fully correct, one with a single, understandable input-series mixup, felt much harder than it was
**Difficulty:** 8-9/10 (Adrian's own rating - felt "steamrolled" by the material)
**Time:** not tracked precisely today

---

**Context:** pivoted from the pullback resumed/recrossed classifier (RF confirmed as the
better model for that feature set) toward mean-reversion research, per Adrian's own
direction. A short research pass beforehand established the standard toolkit (ADF, Hurst
Exponent, half-life via AR(1)) and one important finding - Hurst needs hundreds of
observations per window to be reliable, ruling out computing it per pullback-block and
requiring a new, separate rolling-window pipeline on the continuous M15 series. A second
thread (gamma-exposure proxies) was researched and explicitly deferred to tomorrow at
Adrian's request - today's material alone was already dense.

---

**What actually happened, task by task:**

- **Task 1 (ADF test) - fully correct:** built `deviation = close - close.rolling(200).mean()`,
  ran `adfuller()`, correctly extracted the p-value from its awkward multi-value return tuple
  (a real source of the task's felt difficulty - the function's raw output is genuinely
  unfriendly to read), and correctly interpreted p=0.0 as rejecting the random-walk null
  hypothesis - real evidence of mean-reversion around the 200-bar rolling mean.

- **Task 2 (Hurst Exponent) - one clear, fixable issue, not a conceptual error:** used a
  found library (`hurst.compute_Hc`) rather than hand-rolling the variance-scaling method as
  suggested - a reasonable, pragmatic choice given the material's density. The real issue:
  ran it on raw `close` price (H=0.63, reads as trending) rather than on the `deviation`
  series used in Tasks 1 and 3. This isn't wrong so much as answering a DIFFERENT question -
  raw XAUUSD price trends upward over years (so H>0.5 there is expected and unsurprising),
  while Tasks 1 and 3 both ask whether deviation FROM a local rolling mean reverts, which is
  a separate and compatible question (a market can have both a long-run trend and
  short-run local mean-reversion). Correctly sensed something might be off
  ("I could've done something wrong") without being able to pinpoint it alone - a fair
  outcome given how much new material landed in one day.

- **Task 3 (half-life via AR(1)) - fully correct, undersold by Adrian's own assessment:**
  correctly implemented the OLS regression of the differenced deviation on its lagged level,
  correctly extracted the half-life formula, got half_life=93.4 bars. Said "I have no idea,
  I'm not a data scientist yet" - but the implementation and number were both right; what was
  missing was the LAST interpretive step (comparing 93.4 bars against the 5-60 bar tradeable
  range from the research), which we did together afterward: at 200-bar window, reversion is
  real (per Task 1) but too slow to be practically tradeable - a genuine, useful, negative-
  leaning finding, not a failure to understand the material.

---

**Real takeaway to correct Adrian's own harsh self-assessment:** 2 of 3 tasks were fully
correct including interpretation, and the third had correct mechanics with one specific,
nameable input-series mixup - not "steamrolled by the concepts." The FEELING of being
overwhelmed was real and valid (this was genuinely dense, multi-layered statistical material
delivered in one sitting, worse than the track's usual 3-4 tasks/session pacing, and used an
LLM assist which is fine but understandably didn't build the same confidence as working it
out directly) - but the actual output quality doesn't match "tragedy," and it's worth saying
that plainly so the difficulty rating reflects the experience of the day, not a mistaken
belief that the work itself was bad.

**Reinforce next:** always double-check WHICH series (raw price vs. a deviation/derived
series) a statistical test is actually being run on - today's one real slip. Also: this kind
of dense, multi-concept statistical day should probably be split across two sessions in the
future rather than delivered in one 3-task block, given how it landed.

**Carries forward:** Task 4 (session-aware realized volatility + two honestly-labeled
"gamma-like" proxies) explicitly deferred to tomorrow, unstarted. Mean-reversion verdict so
far: real at a 200-bar window (ADF confirms), but likely too slow to trade (half-life 93 bars
vs. 5-60 bar tradeable range) - worth testing a SHORTER rolling window next, where reversion
might be faster and closer to tradeable, once Hurst is corrected to run on deviation.
