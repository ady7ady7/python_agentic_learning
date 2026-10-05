# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-05
**Session:** ML Phase - Week 7 Day 1 (resolving the momentum/reversion contradiction - drift removal, threshold sweep, formal test)
**Score:** ~95% - resolved a real open question definitively, with an unprompted, well-chosen extra tool (Cohen's d)
**Difficulty:** 6/10 (Adrian's own rating)
**Time:** ~80 min

---

**What actually happened, task by task:**

- **Task 1 (drift removal):** correctly rebuilt the comparison using
  `future_deviation_20 = close.shift(-20) - close.rolling(30).mean()` instead of the raw
  `close.shift(-20) - close`. Result flipped the sign completely from Friday: z<-2 now shows
  mean=-14.82 (down) and z>2 shows mean=+14.02 (up) - the OPPOSITE of Friday's apparent
  momentum pattern, and exactly the direction true mean-reversion predicts. Confirmed the
  drift hypothesis from Friday was correct - it was the real cause of the earlier
  contradiction, not a genuine momentum effect in the data.

- **Task 2 (threshold sweep):** built a thorough table (went beyond the ask - added
  quantiles alongside mean/median) across thresholds 1.5-3.5. Found a clean, monotonic
  relationship: the reversion effect strengthens as the threshold gets more extreme
  (below-threshold mean: -13.2 at 1.5 -> -21.2 at 3.5; above-threshold mean: +12.4 -> +15.9) -
  exactly the "edge lives further in the tails" hypothesis floated after Friday's session,
  now confirmed with real numbers.

- **Task 3 (formal test) - correct instinct, strong unprompted extension:** ran
  Mann-Whitney at three threshold pairs (2.5/3/3.5), got p=0.0 everywhere, and correctly
  recognized on his own that "everything is statistically viable" doesn't tell you effect
  STRENGTH, especially at this sample size (same lesson as the significance-vs-effect-size
  work from Week 5/6). Independently fetched and implemented a proper Cohen's d function
  (pooled std, ddof=1 - mechanically correct) without being asked. Results: d=0.71-0.75 for
  the above-threshold groups, d=-0.80 to -0.92 for below-threshold groups - medium-to-large
  effect sizes, genuinely strong for financial data (where effects are typically much
  smaller, 0.05-0.15). Also noticed and flagged the below/above asymmetry without being
  prompted.

---

**Real verdict for this project, now settled:** after removing gold's long-term drift
contamination, XAUUSD M15 shows a real, large-effect-size mean-reversion signal at extreme
z-score thresholds (2.5+), resolving Friday's apparent momentum contradiction. This closes
the open question cleanly and gives the project a solid, verified foundation to build an
actual feature/target/model on top of - the next natural step.

**Reinforce next:** none new - this session demonstrated exactly the "verify before
modeling" and "significance vs effect size" disciplines from recent weeks being applied
proactively and correctly in a brand new context, unprompted. A strong sign these habits are
becoming automatic rather than something that needs re-teaching each time.

**Carries forward:** with the mean-reversion signal confirmed, next step is converting this
into an actual classification/regression target and building features/model around it - the
same ML learning workflow already used successfully for the pullback project.

**Post-session discussion, corrected to the right scope:** Adrian initially asked what this
would mean for a trader testing a strategy - he then explicitly corrected this himself:
this repo's purpose is learning pandas/stats/ML on real data, NOT building or validating
tradeable strategies ("to nie jest nasza działka... jesli jakaś idea faktycznie jest
ciekawa, to ja już sobie na własną rękę w ramach innych projektów też mogę to badać").
Saved as a standing scope boundary in memory (ml-learning-phase.md). Reframed the same
underlying curiosity in ML/stats terms instead: (1) the natural next step is defining an
actual classification/regression TARGET from the confirmed reversion signal (e.g. "does
price revert by X within N bars after an extreme z-score event" as a binary label, mirroring
the P(resumed)/P(recrossed) target design from the pullback project), (2) checking whether
the effect is stable across time (sub-period comparisons) as a FEATURE-ENGINEERING/
data-quality question - does a "time since last regime change" or similar context feature
matter - not as a strategy-robustness question, (3) the below/above asymmetry as a question
about whether `direction` needs to be a feature in any model built on this, same as it was
for the pullback project.
