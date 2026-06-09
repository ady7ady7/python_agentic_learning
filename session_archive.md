# Session Archive

<!-- One entry per session, newest on top. Appended automatically at end of each session. -->
<!-- Format: date | score | difficulty | 5–10 lines max per entry -->

---
## 2026-06-08 | Week 6 Day 1 | Score: N/A | Difficulty: 4/10
**Covered:** Polish and bug-fixing session on 07_final_project_adjusted_sns.ipynb. Fixed base_apple_df variable collision, corrected stale methodology note (sales data now correctly described as lower-bound indicator, not omitted), updated key findings with iPhone 13 secondary market king finding and Q4/Prime Day seasonality. Corrected Pro Max claim — data shows Base + Mini lead iPhone 13 sales, not Pro Max. Rejected tier retention barplot in favour of planned annotated shaded bands on tier decay charts.
**Problems / gaps:** Shaded band annotations on tier decay charts not yet implemented. Polish notebook (06_final_project_pl.ipynb) still not synced with all changes from Weeks 5–6.
**Reinforce next:** Implement axvspan shaded year bands on tier decay charts, then assess if project is ready to wrap or needs further polish.

---
## 2026-06-05 | Week 5 Day 5 | Score: N/A | Difficulty: 8/10
**Covered:** Major discovery: `monthly_sold` is Keepa's sales estimate buckets (50 = at least 50 units sold), not a sales rank — and existing `mean()` aggregation was methodologically wrong due to varying ASIN counts per submodel. Decision: keep `06_final_project_sns.ipynb` for price decay, rebuild sales section from scratch in `07_final_project_adjusted_sns.ipynb`. New pipeline: `resample('ME').last()` per ASIN + `sum()` across variants, aggregated to `month_year`. Built brand / brand+tier / submodel DataFrames, rebuilt all sales charts, wrote observations for iPhone 11/13/15 submodels. Sales section now has correct methodology and honest framing.
**Problems / gaps:** `base_apple_df` variable collision in pipeline (overwritten by sales version). Stale methodology note in cell-2 still references old incorrect framing. 1yr/2yr retention by tier not yet built. Key findings missing iPhone 13 Pro Max and seasonality bullets.
**Reinforce next:** Fix bug, update methodology note, add tier retention charts, update key findings. Session ran very long (~2+ hrs) due to unexpected methodological rebuild.

---
## 2026-06-03 | Week 5 Day 3 | Score: N/A | Difficulty: N/A
**Covered:** Tier decay charts built for all brands + per brand (Apple/Samsung/Google). Key finding: Apple Base outperforms Pro Max in long-term % retention; Samsung FE leads early; Google 'a' series is the strongest value holder. Base and flagship launch price charts over time. Pro Fold excluded from flagship chart with detailed analytical note. NEW column confirmed as USD. Full notebook reorder planned.
**Problems / gaps:** USD decay charts not yet built. Sales rank by tier not done. Debug cell still in notebook. Notebook order needs restructuring.
**Reinforce next:** Remove debug cell, reorder notebook per agreed structure, add USD decay charts, add sales rank by tier, update Polish notebook.

---
## 2026-06-02 | Week 5 Day 2 | Score: N/A | Difficulty: N/A
**Covered:** Annotation practice on 2 charts. All-brands decay chart: shaded first-year band, crossing-point annotations for all 3 brands. 1-year retention barplot: Pixel 5 anomaly annotated. Discussed line highlighting and circle annotations. Base vs flagship launch price scatter+line charts built. Pro Fold inclusion question raised.
**Problems / gaps:** Pro Fold decision deferred. Highlighting individual lines / circle annotations not yet implemented.
**Reinforce next:** Pro Fold decision, USD charts, tier aggregation for sales rank.

---
## 2026-06-01 | Week 5 Day 1 | Score: N/A | Difficulty: N/A
**Covered:** Launch price barplot added (sorted by value, brand colored) — iPhones not always most expensive, some Samsung models overlap. Identified that NEW column may be in cents not USD — needs verification before dollar charts. Decided to add USD price alongside % in existing aggregations rather than separate charts.
**Problems / gaps:** Tasks 2-3 (dollar decay charts) not done — price unit verification needed first. Polish notebook not updated yet.
**Reinforce next:** Verify NEW column units, add price_usd to existing aggregations, build dollar decay charts for all 3 brands, update Polish notebook.

---
## 2026-05-31 | Week 4 Day 7 | Score: N/A | Difficulty: N/A
**Covered:** Final polish on 06_final_project_sns.ipynb — Prime Day vlines added, iPhone 15 sales comparison added, all TODO placeholders filled with real observations, prose polished throughout. Polish version 06_final_project_pl.ipynb created with natural Polish prose. GitHub notebook rendering issue identified (nbconvert error) — PNG outputs confirmed present, likely GitHub-side transient issue. Planned next additions: $ price charts per submodel, launch price barplot year-over-year.
**Problems / gaps:** GitHub notebook rendering unreliable — not a file issue. build_final_notebook_sns.py lost (not committed). translate_to_polish.py not committed (file not found at commit time).
**Reinforce next:** $ price analysis (NEW / 100 per submodel), launch price barplot by year, README-based portfolio repo if GitHub rendering remains broken.

---
## 2026-05-30 | Week 4 Day 6 | Score: N/A | Difficulty: N/A
**Covered:** Created 05_final_project.ipynb — clean consolidated notebook with full pipeline cell, proper section flow, human-sounding prose, [TODO] placeholders for remaining observations. All charts included in logical order. build_final_notebook.py script created as reproducible generator. All DataFrames renamed systematically. vlines solved with invisible scatter traces for legend entries. Confirmed notebook runs without errors.
**Problems / gaps:** KPI board aesthetics still improvable. A few [TODO] placeholders remain for numeric values and observations. Plotly charts won't render statically on GitHub.
**Reinforce next:** Fill in [TODO] placeholders, polish KPI board, add any final observations. Project ready to share.

---
## 2026-05-29 | Week 4 Day 5 | Score: N/A | Difficulty: N/A
**Covered:** Axis labels added to all charts. Vline overlap on ms_chart_5/6 partially improved — decided to try facet_col by year and annotation box approaches tomorrow. pd_chart_1 split into Apple/Samsung/Google/combined versions. pd_chart_1b/1c reveal Samsung is New-only, Google is mixed. Combined brand decay chart added. pd_chart_8 (best time to buy barplot) identified as analytically weak — to be replaced with price distribution boxplot + KDE per brand. Pixel 5 outlier documented (Issue 15) — low launch price + early discontinuation = scarcity effect. Documented Issues 13-15 in case_study_issues.md.
**Problems / gaps:** vline overlap not fully solved. pd_chart_8 dropped as concept. KPI board still aesthetically poor.
**Reinforce next:** Final session — facet vline chart, boxplot + KDE for price distribution, KPI board polish, written conclusions scaffolded, notebook structure finalized.

---
## 2026-05-28 | Week 4 Day 4 | Score: N/A | Difficulty: N/A
**Covered:** Brand comparison at 1 year — iPhones retain value most, Pixel 5 outlier flagged as potentially sparse data. Best time to buy chart — steepest weekly price drop per generation (diff per ASIN, groupby generation+days_rounded, idxmin). KPI board with go.Indicator in 2×4 subplot grid — fixed add_trace row/col positioning, shortened titles with <br> splits. Learned go vs px distinction.
**Problems / gaps:** go.Indicator cluttering without row/col args — fixed. date_range tuple not accepted as value — used scalar (6 years) instead. Best time to buy chart has outliers (Pixel 10 far out) — boxplot per brand suggested as improvement.
**Reinforce next:** Final session tomorrow — polish charts, add written conclusions, consolidate into deliverable notebook. Consider boxplot for best-time-to-buy per brand.

---
## 2026-05-27 | Week 4 Day 3 | Score: N/A | Difficulty: N/A
**Covered:** Charts 3-6 built (monthly_sold by tier/generation, days_since_launch + real datetime). Resample+ffill applied to datetime charts to fix artifacts. Vlines working with pd.Timestamp * 1000 fix. monthly_sold data only starts late 2023 — limitation noted. Product grade split on Chart 1: Renewed vs Renewed Premium — Premium clearly more stable and expensive. No New iPhones on Amazon US confirmed. Planned next additions: brand comparison at 1-year lifecycle stage, best-time-to-buy inflection analysis, KPI board with go.Indicator cards.
**Problems / gaps:** monthly_sold coverage too short for meaningful seasonal analysis on real dates. vline annotation positioning needs refinement.
**Reinforce next:** Brand comparison bar chart at 365 days. Price inflection/best-time-to-buy. KPI board with Plotly go.Indicator.

---
## 2026-05-26 | Week 4 Day 2 | Score: N/A | Difficulty: 4-7/10
**Covered:** Pipeline cleanup (removed _x/_y duplicate columns). Created official_launch_prices.csv (63 submodels, real premiere dates, mean prices across storage tiers). Merged into pipeline — price_pct_of_launch now anchored to real launch prices, days_since_launch to real premiere dates. Charts 1 & 2 rebuilt — curves now start near 100%. ms_df aligned to same pipeline (official premiere dates, tier column). Documented Issues 10-12 in case_study_issues.md (Keepa premiere_date unreliable, storage price variation, unstable recent models).
**Problems / gaps:** iPhone 17 and other recent models spike above 150% — excluded from analysis, threshold ~10 weekly observations. Dataset not designed for this analysis — required significant external data sourcing to make it work.
**Reinforce next:** High-volume session. Charts 3-6 (monthly_sold). Product grade split (Renewed vs New vs Renewed Premium). Make charts interactive and polished. Push toward final deliverable.

---
## 2026-05-25 | Week 4 Day 1 | Score: N/A | Difficulty: 5/10
**Covered:** Created 04_interactive_charts.ipynb. Tier extraction implemented and verified (12 tiers: Base, Pro, Pro Max, Ultra, FE, Mini, Plus, +, a, Pro Fold, Edge, Pro XL). Charts 1 & 2 built. Discovered first_price was grouped by model not submodel — fixed to groupby('submodel_name'). Discovered tracking gap causes Pro/Pro Max to start mid-decay (iPhone 13 Pro gap = 212 days, Pro Max = 163 days). Documented as Issue 9 in case_study_issues.md. Chart plan saved to memory.
**Problems / gaps:** price_pct_of_launch normalization was wrong scope — fixed. Tracking gap cannot be filled, must be annotated/acknowledged.
**Reinforce next:** Annotate charts with actual first recorded day per submodel. Verify Charts 1 & 2 look correct after fix. Move to Charts 3-6 (monthly_sold).

---
## 2026-05-22 | Week 3 Day 5 | Score: N/A | Difficulty: 5/10
**Covered:** Updated case_study_issues.md with Issues 5-8 (probe ASIN gap, wrong dt.month column, agg('first') tracking gap problem, monthly_sold granularity). Apple price decay by generation chart built. Apple monthly_sold by submodel chart attempted — still cluttered. Designed full 6-chart interactive plan: tier-based filtering (submodel tier extracted from name by stripping generation_name prefix), per-generation submodel comparison, both relative (days_since_launch) and absolute (real datetime with event markers) views for price decay and sales rank.
**Problems / gaps:** Tasks 3 & 4 skipped — correctly identified as premature before chart approach was properly designed. monthly_sold still not clean enough for a final chart.
**Reinforce next:** Implement 6-chart plan. Start with tier extraction (`str.replace` + strip), verify with value_counts. Build Charts 1 & 2 (price decay) first, then 3-6 (monthly_sold). Event markers for BF/Christmas/launch on datetime charts.

---
## 2026-05-21 | Week 3 Day 4 | Score: N/A | Difficulty: 5/10
**Covered:** Launch price by submodel (Seaborn barplot, chronological order) — uptrend visible, likely inflation; Google launches cheaper than Apple. Price decay velocity in first 90 days — large apparent drops (40-60%) flagged as possibly artifact of tracking gap (first recorded price ≠ true launch price). monthly_sold per submodel chart built but unreadable — too many lines, needs filtering or small multiples.
**Problems / gaps:** `agg('first')` on NEW price not reliable as launch price proxy due to tracking gap. Task 3 visualization still not solved — brand aggregation too coarse, submodel too granular. Project alignment feeling loose.
**Reinforce next:** Fix monthly_sold chart: filter to one brand or top N models. Tighten project direction — each session should add one clear, defensible finding. Document tracking gap caveat in writeup.

---
## 2026-05-20 | Week 3 Day 3 | Score: N/A | Difficulty: 4/10
**Covered:** Written interpretation of seasonal chart (Oct/Nov Apple dip = new iPhone launch pressure + Black Friday; December reclaim across all brands). First look at monthly_sold_full.csv (18,489 rows; Apple 180 ASINs, Samsung 99, Google 83). Brand-level monthly_sold chart built but identified as misleading — aggregating across generations at different ages flattens signal into noise.
**Problems / gaps:** monthly_sold brand aggregation not meaningful — need per-generation view. Seasonal writeup unit phrasing needs tightening ("below 1.5%" should reference percentage points, not percent). Task 3 didn't yield useful insights in current form.
**Reinforce next:** Redesign monthly_sold chart: one line per generation_name, days_since_launch on x. Exploratory angle — extract more phenomena from limited columns (price decay shape, launch price comparison, rank velocity). Make the research "sexy" — don't assume, let data show.

---
## 2026-05-19 | Week 3 Day 2 | Score: N/A | Difficulty: 5/10
**Covered:** Rebuilt pipeline on full Postgres export (878k rows → 105k after resample, 893 ASINs). Exported all_asins_meta.csv. Renamed probe_asins_meta.csv. Recomputed price_pct_of_launch and regularized decay chart — chart described as "making much more sense." Re-ran seasonal analysis with correct groupby('asin').diff() scoping. Fixed dt.month bug (was extracting from listed_since instead of datetime). Final seasonal result: 36 rows, full 12-month coverage, Oct/Nov showing strongest negative diffs for Apple — consistent with new iPhone launch + Black Friday pressure.
**Problems / gaps:** dt.month extracted from wrong column (listed_since vs datetime) — caught and fixed same session. NEW * 100 workaround needed (export had new_price already divided, pipeline expected raw). backup_df = df without .copy() — same reference bug pattern.
**Reinforce next:** Correct interpretation of MoM price_diff values (units = percentage points, not dollars). Seasonal chart analysis and written interpretation. Keep drilling column scoping hygiene.

---
## 2026-05-18 | Week 3 Day 1 | Score: N/A | Difficulty: 5/10
**Covered:** Seasonal analysis design — MoM price diff (groupby asin + diff()) vs raw price_pct_of_launch. Adrian correctly identified age/season confound before being prompted. Seaborn lineplot syntax correct on first try. Identified .shift(1) scoping bug (crosses ASIN boundaries — same pattern as ffill scope). Seasonal result only 12 rows — data too sparse. Root cause confirmed: CSV export used 19 probe ASINs only, not full Postgres catalog (60 submodels, 19,565 price records). Full schema mapped (keepa.generations → submodels → products → price_history).
**Problems / gaps:** .shift(1) instead of groupby('asin').diff() — recurring scoping pattern. Seasonal analysis not completed due to data gap.
**Reinforce next:** Groupby scoping for any per-group operation (diff, ffill, transform). Tomorrow: discuss product_grade filter implications, export full dataset from Postgres, rebuild pipeline.

---
## 2026-05-15 | Week 2 Day 5 | Score: 9/10 | Difficulty: 5/10
**Covered:** pd.cut binning (50-day buckets), Seaborn barplot with hue by brand. Regularized x-axis by rounding days_since_launch to nearest 7 — eliminated Plotly shadow artifacts. Rebuilt clean brand decay chart. Added pd.cut and regularization patterns to pandas_concepts.md and important_info.md.
**Problems / gaps:** Seaborn order= passed unnecessarily (pd.cut Categorical handles it automatically). Q4 groupby syntax slightly off. Week 2 quiz coding tasks too close to session work — will recalibrate for Week 3.
**Reinforce next:** Complex groupby/agg syntax needs more reps. Week 3: seasonal analysis (Black Friday/Christmas WoW price effect), sales volume comparison if feasible.

---
## 2026-05-14 | Week 2 Day 4 | Score: 14/15 | Difficulty: 8/10
**Covered:** Brand-level aggregation: groupby(brand + days_since_launch) → mean price_pct_of_launch → one line per brand. Plotly brand decay chart with hline at 50%. Seaborn boxplot sorted by median per brand. Written analysis: Apple retains value best, decay shape, data quality concerns.
**Problems / gaps:** Multi-key groupby and Seaborn order pattern still unintuitive — required LLM assistance. px.line Series syntax causing visual artifacts (fixed to DataFrame syntax). Decay curve shape question answered descriptively, not analytically.
**Reinforce next:** Multi-key groupby and Seaborn order with more reps. Both patterns now in pandas_concepts.md.

---
## 2026-05-13 | Week 2 Day 3 | Score: 13/15 | Difficulty: 5/10
**Covered:** agg vs transform reinforced with targeted tasks. Brand comparison decay table. Normalized decay chart (price_pct_of_launch vs days_since_launch, color by brand). Key insight: one line per model is too cluttered — need brand-level aggregation for clean comparison (Day 4 task).
**Problems / gaps:** Task 4/5 used wrong df due to ambiguous task wording (Claude's fault — will specify df explicitly going forward). filtered_df overwritten immediately after creation.
**Reinforce next:** Brand-level aggregation: groupby(brand + days_since_launch) → mean price_pct_of_launch → one line per brand. Specify exact df in every task.

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

