# Tasks — Week 11 Day 4

---

## Task 1 — Project intro with goals

- [ ] Add new markdown cell right after cell-0 (title)
- [ ] Write: what we are analyzing (XAUUSD m5, London session features as predictors of NY session direction)
- [ ] Write: hypothesis (do London session features have predictive power over NY session direction)
- [ ] Write: what we want to achieve (binary classifier — bullish/bearish NY session, XGBoost)
- [ ] Write: why this data (Dukascopy, 5 years, ET timezone justification)

## Task 2 — Minor fixes to existing cells

- [ ] cell-37: remove Warsaw reference ("3:00 ET is 8:00/9:00 Warsaw time") — unprofessional in a portfolio piece
- [ ] cell-56: rewrite "Important note" — remove apologetic tone, replace with a proper transition: EDA showed no clear signal in simple features, which motivated deeper feature engineering
- [ ] cell-65: remove "Kasia claimed" — replace with a factual justification for XGBoost (strong on tabular data with non-linear relationships)
- [ ] cell-68: remove "which perhaps should be done earlier" — self-deprecating, not portfolio material

## Task 3 — EDA → ML transition section

- [ ] Add new markdown cell before current "## ML Intro" (cell-64)
- [ ] Write: why these 11 specific features (what each encodes, rationale)
- [ ] Write: why NY OHLC columns are excluded from X (data leakage — not available at prediction time)
- [ ] Write: why time-based split instead of random (time series — future cannot train on past)

## Task 4 — Hyperparameter tuning rationale

- [ ] cell-70: explain why the grid was extended with gamma, min_child_weight, reg_lambda, colsample_bytree
- [ ] Write: default model overfit (train 1.0 / test 0.48) required regularization parameters, not just subsample/depth

## Task 5 — Final conclusion

- [ ] Review cell-72: does it close the project properly
- [ ] Add sentence tying Mann-Whitney to model result: no statistical signal in features → no prediction in model — consistent conclusion
- [ ] Optional: add "future work" — COT data, DXY correlation, Random Forest as sanity-check baseline

---

**Total: 5 tasks, markdown only, zero new code**
