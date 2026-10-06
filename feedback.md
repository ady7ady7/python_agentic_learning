# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-06
**Session:** ML Phase - Week 7 Day 2 (defining the mean-reversion target) - real, negative-leaning finding
**Score:** not scored in the usual sense - this session caught a genuine methodological issue and produced an important negative result
**Difficulty:** not rated - ran long on Task 1 alone (~70 min) due to a real design flaw caught mid-stream
**Time:** ~70 min (Task 1 only; Tasks 2-3 deferred)

---

**What actually happened:**

Before writing any target-building code, Adrian pushed back hard on interpreting his own
numbers rather than accepting them at face value - exactly the right instinct. First attempt
computed `future_deviation_20` per-ROW for all `|z_score| > 2.5` rows and found the average
deviation GREW rather than shrank (e.g. extreme-high: +14.18 at the event bar -> +15.24 at
+20 bars) - looked like anti-reversion. Correctly suspected his own interpretation might be
wrong before concluding anything, and asked for help auditing it rather than assuming the
data was broken or that reversion doesn't exist.

**Real issue identified together:** `z_score > 2.5` can stay true for several consecutive
bars during an extended extreme move - counting every one of those bars as a separate "event"
averages the START of a move together with its MIDDLE, which structurally cannot show
reversion (the middle of an ongoing move hasn't reverted by definition). Fixed by building
proper episodes: flag only the FIRST bar of each continuous run above/below threshold
(`is_extreme & ~is_extreme.shift(1, fill_value=False)`), mirroring the `block_id` pattern
from the pullback project.

**One real bug along the way, self-corrected with guidance:** first attempt at the episode
flag used `.apply(lambda x: ...)` with a reference to the full column's `.shift()` inside the
lambda - a lambda applied to a single Series only receives one scalar value per call, so
referencing the whole column inside it doesn't do what was intended, compounded by an
operator-precedence bug (`x == 1 & (...)` binds as `x == (1 & (...))`, not `(x == 1) & (...)`
- the same `&`/`==` precedence trap as previous sessions). Resolved by switching to a fully
vectorized boolean expression instead of `.apply()`/lambda - the correct, idiomatic pandas
pattern for this kind of row-vs-previous-row comparison.

**After the fix - the real finding:** even with proper episode-based events (one row per
genuine first-crossing, not per bar), the pattern PERSISTED: deviation at the 20-bar mark was
STILL larger in magnitude than at the event bar (high: 11.65 -> 12.54, low: -13.43 -> -14.60).
This is a genuine, methodologically sound negative result for THIS specific horizon (20
bars) - not an artifact of the row-vs-episode counting issue, which has now been ruled out.

---

**Correctly NOT a defeat, and Adrian treated it as such:** rather than conclude "mean-
reversion doesn't exist" from one horizon, proposed testing several forward horizons (5, 10,
20, 50, 100 bars) before drawing a final conclusion - the 20-bar choice was always somewhat
arbitrary, not an established fact. Agreed to defer Tasks 2-3 (feature table, baseline split)
until the target itself is on solid ground - correctly refusing to build further structure on
an unresolved foundation.

**Reinforce next:** `.apply()` + lambda referencing the full column (not just the scalar
passed in) is a real recurring gap - vectorized boolean comparisons
(`series & ~series.shift(1)`) should be the default reach for "is this different from the
previous row" logic, not `.apply()`. Also: `&`/`==` operator precedence - still needs
parentheses around each condition every time.

**Carries forward (priority for tomorrow):** build the same episode-based reversion check
across multiple forward horizons (5, 10, 20, 50, 100 bars) in one table, before deciding
whether to pursue this mean-reversion thread further or pivot direction. This is explicitly
NOT yet a "mean-reversion doesn't exist" conclusion - it's "doesn't show up cleanly at 20
bars with this episode definition," which is a narrower, more honest claim.
