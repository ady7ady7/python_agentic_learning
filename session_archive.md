# Session Archive

<!-- One entry per session, newest on top. Appended automatically at end of each session. -->
<!-- Format: date | score | difficulty | 5–10 lines max per entry -->

---
## 2026-05-12 | Week 2 Day 2 | Score: 14/15 | Difficulty: 5/10
**Covered:** Fixed pipeline bugs from Day 1 (resample without groupby, ffill syntax). Meta columns preserved via post-resample merge. days_since_launch recalculated after resample. Price decay curves for iPhone 13 and all iPhones (days_since_launch as x-axis). Decay summary table: first/last price, total_drop_pct, max_weekly_drop using diff().abs(). Added agg + diff patterns to pandas_concepts.md.
**Problems / gaps:** transform vs agg distinction still causing confusion under pressure. groupby().first() vs groupby().transform('first') mix-up.
**Reinforce next:** groupby agg vs transform — more reps. Keep cleaning up pipeline design (meta conversion once, not twice).

---
## 2026-05-11 | Week 2 Day 1 | Score: 2/4 (partial) | Difficulty: 7/10
**Covered:** Started 03_analysis.ipynb. Attempted full pipeline with meta preserved through resample. Pipeline ran but produced ~283 rows instead of ~3000 — two bugs identified: resample without groupby (collapsed all ASINs into one), and incorrect ffill syntax. Meta preservation through resample not solved.
**Problems / gaps:** `resample` without `groupby('asin')` prefix — critical mistake. ffill argument syntax wrong. Short session due to time constraints.
**Reinforce next:** Fix the two pipeline bugs. Solve meta column preservation through resample. Resume Parts 2 and 3.

---
## 2026-05-08 | Week 1 Day 5 | Score: 9.5/12 | Difficulty: 7/10 | Quiz: 7.5/9
**Covered:** Full clean pipeline from scratch (load → merge → days_since_launch → outlier removal → resample). Resampled multi-iPhone Plotly chart on cleaned data. Seaborn boxplot with sort by median. Brand comparison chart (Apple + Samsung S20 FE + S21). Week 1 quiz completed.
**Problems / gaps:** ffill missing after resample (holes in charts). Task 4 skipped — meta columns dropped before task required them (task ordering issue). `ignore_index` behavior reversed in quiz. `agg` vs `transform` distinction not fully articulated.
**Reinforce next:** Keep meta columns through pipeline from the start. ffill after resample. `agg` vs `transform` distinction. `ignore_index=True` behavior.

---
## 2026-05-07 | Week 1 Day 4 | Score: 13.5/15 | Difficulty: 5/10
**Covered:** Full resample pipeline from scratch (AMAZON column) — ffill scope correct this time. New notebook 02_cleaning.ipynb: days_since_launch column, negative days filter, outlier detection with groupby + transform + 3×median threshold (709 outliers removed). Multi-model Plotly line chart for all iPhones. Added groupby + transform to pandas_concepts.md.
**Problems / gaps:** `> 0` instead of `>= 0` in days filter (dropped 4 extra rows). No resample before final chart — plotted raw event data. Concept check question poorly worded by Claude ("no groupby" when "no merge" was meant).
**Reinforce next:** Resample before visualization. Precision in filter conditions (> vs >=).

---
## 2026-05-06 | Week 1 Day 3 | Score: 13.5/15 | Difficulty: 5/10
**Covered:** Reinforced resample pipeline (USED prices), merge on asin to add brand/model/listed_since to price DataFrame, first Plotly line chart (iPhone 13 weekly NEW prices). Confirmed downtrend in price over time visually.
**Problems / gaps:** ffill applied without groupby scope again (same mistake as Day 2 — needs more reps). set_index placement initially forgotten.
**Reinforce next:** ffill scope, set_index placement. Writing pandas_concepts entries independently.

---
## 2026-05-05 | Week 1 Day 2 | Score: N/A | Difficulty: 6/10
**Covered:** Data moved to `project1_phones_sales_analytics/data/` (gitignored). `data_schema_examples.md` created. `learning_materials/pandas_concepts.md` created with ToC + 5 concepts. Combined all 19 `_price_history.csv` files into one DataFrame (170k rows). Resampled NEW prices to weekly min per ASIN using `groupby + resample + reset_index + ffill`. Discussed event-based data structure, why ffill beats interpolation for price data, multi-index behavior after resample.
**Problems / gaps:** `resample` pattern non-obvious — especially multi-index output, `reset_index` placement, and `ffill` scope. Combining groupby + resample + ffill in one pipeline tripped Adrian up.
**Reinforce next:** Drill resample + reset_index + ffill pattern with coding tasks (not verbal Q&A). Design tasks.md with scoring. Concept checks as small code exercises.

---
## 2026-05-04 | Week 1 Day 1 | Score: N/A | Difficulty: 3/10
**Covered:** Repo structure setup (tasks/feedback/session_archive in root, CLAUDE.md updated). venv created in repo root with pandas/jupyterlab/seaborn/plotly. JupyterLab kernel configured in VS Code. Started 01_exploration.ipynb: loaded all_products_meta.csv, converted Keepa minute timestamps to datetime, computed tracking_gap_days (range -55 to +101 days, notable anomalies for newest models). Loaded iPhone 13 price_history, inspected event-based structure and non-null counts per price column — NEW dominates across all three brands.
**Problems / gaps:** Too much copy-paste from Claude — not enough active coding by Adrian. Scaffolding approach not applied yet.
**Reinforce next:** Scaffolded learning from Day 2: explain pattern → Adrian writes code → correct. Use English throughout.

