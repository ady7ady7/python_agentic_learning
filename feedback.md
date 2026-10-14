# Feedback - Current Session

<!-- Drafted by Claude from Adrian's own comments during the session - correct or add. -->

**Date:** 2026-10-14
**Session:** ML Phase - Week 8 Day 3 (7 realized_power-family features, found 4-5 with a real if small effect)
**Score:** ~90% - all 7 formulas correctly translated to code, one real implementation bug caught and fixed same-session
**Difficulty:** 6/10 (Adrian's own rating - heaviest math day in the project so far)
**Time:** ~2h

---

**Context:** Adrian did independent overnight research, bringing back a well-organized
family of 13 candidate features, all variants/companions of Tuesday's strongest feature
(`realized_power`). Today built the 7 that work directly from OHLC without long lookback
windows: Efficiency Ratio, Concentration, signed semivariance asymmetry (SJV), Relative RP,
Center of Mass, Wick-to-Close ratio, Wick Rejection Asymmetry.

---

**What actually happened:**

- **Tasks 1-3 (feature construction):** all 7 formulas correctly implemented, matching the
  concept explanations given. Correctly flagged upfront that this batch was unusually
  math-heavy and used LLM assistance for Center of Mass specifically (the hardest, most
  unfamiliar formula of the seven) - an honest, reasonable call, not a shortcut taken
  silently.

- **Real bug, caught and fixed same-session:** the first `center_of_mass` implementation
  rolled over raw `close` prices instead of absolute 1-bar returns - computing a completely
  different (and conceptually meaningless for this purpose) quantity than intended. Caught
  through the review process, fixed to `close.pct_change().abs()` as the input series, and
  re-screened - revised result p=0.018, d=-0.089 (a real but small effect, now actually
  measuring what the feature was meant to measure).

- **Task 4 (screening):** ran Mann-Whitney + Cohen's d across all 7. Results: `sjv_10`
  (d=0.160) and `efficiency_ratio_10` (d=0.159) are the strongest of today's batch,
  `wtc_10` (d=-0.145) and the corrected `center_of_mass` (d=-0.089) show weaker but real
  effects, `wra_10`/`relative_rp` are borderline (p>0.1), and `concentration_10` looks
  genuinely dead (p=0.966, d≈-0.015). None individually beats `realized_power`'s own d=0.250,
  as expected for companion/derived features. Correctly interpreted this as still useful -
  several independently-reasoned small effects stacking in a nonlinear model (RF/XGBoost)
  is a real mechanism, not wishful thinking, since they're not random variants but each
  targeting a genuinely different aspect of the same underlying phenomenon.

---

**Real outcome:** the feature set for tomorrow's modeling now has ~10-11 features (Tuesday's
batch + today's 7, several with real if modest individual effects) - a substantially richer,
more theoretically-grounded set than Friday's weak 4-feature baseline.

**Reinforce next:** when implementing a formula from a written spec, double-check which
exact series feeds into a rolling/apply operation - today's bug (raw price instead of
absolute returns) passed silently because the code ran without error and produced a
plausible-looking (if conceptually wrong) number.

**Carries forward:** RF vs XGBoost comparison on the full, enriched feature set - the
remaining features from Adrian's research list (jump-share/bipower variation, multi-scale
L1 variance ratio, clustering - needing 20-50+ bar windows; gap-share and volume-based ones
needing separate judgment calls) stay deferred for later in the week/project.
