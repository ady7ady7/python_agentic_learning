# Tasks — Final Day

## Fill TODOs + export PNGs + build portfolio repo

---

### Task 1 — Fill all [TODO] placeholders in 06_final_project_sns.ipynb [2 pts]

Run the notebook, look at the charts, and fill in these placeholders with real observations:

1. After pd_chart_1 (Apple decay + Renewed vs Renewed Premium):
   Replace `[TODO: fill renewed_premium_premium value]` with the actual number.
   Print `round(renewed_premium_premium, 1)` to get it.

2. After pd_chart_2 (iPhone 13 submodels):
   Replace `[TODO: observation about which submodel holds value best within iPhone 13]`
   with 2-3 sentences based on what the chart shows.

3. After pd_chart_8 (boxplot):
   Replace `[TODO: observation about spread and median differences between brands]`
   with 2-3 sentences.

4. After ms_chart_3 (sales rank lifecycle):
   Replace `[TODO: observation about lifecycle deterioration and any exceptions]`
   with 2-3 sentences.

5. After ms_chart_5 (real dates):
   Replace `[TODO: seasonal observation]` with 1-2 sentences.

6. In key findings:
   Replace `[TODO: renewed_premium_premium]` with the actual number.

---

### Task 2 — Add savefig calls to build script, regenerate, run and save [3 pts]

In `build_final_notebook_sns.py`, add a `plt.savefig()` call after each `plt.show()`
for every chart. Create a `charts/` folder in `project1_phones_sales_analytics/`.

Convention: `plt.savefig('../charts/{chart_name}.png', dpi=150, bbox_inches='tight')`

Charts to export:
- `kpi_table.png`
- `pd_chart_1d.png` (all brands combined)
- `pd_chart_1.png` (Apple)
- `pd_chart_1b.png` (Samsung)
- `pd_chart_1c.png` (Google)
- `pd_chart_2.png` (iPhone 13 submodels)
- `pd_chart_7.png` (1-year retention)
- `pd_chart_8.png` (boxplot)
- `ms_chart_3.png` (sales rank lifecycle)
- `ms_chart_4.png` (iPhone 13 rank by submodel)
- `ms_chart_5.png` (real dates + vlines)
- `ms_chart_6.png` (iPhone 13 real dates)

After adding savefig calls: regenerate notebook, run all cells, save, commit.

---

### Task 3 — Create new portfolio repo structure [3 pts]

Create a new folder `products_prices_historical_analysis_portfolio/` alongside the existing repo
(or initialise a new git repo — your call on whether it's a subfolder or separate).

Structure:
```
README.md
analysis.ipynb          ← copy of 06_final_project_sns.ipynb
case_study_issues.md    ← copy from project1_phones_sales_analytics/
charts/                 ← all PNG exports from Task 2
data/                   ← gitignored
```

The README.md should mirror the notebook structure exactly — same sections, same prose,
with `![](charts/chart_name.png)` in place of each code cell output.
I'll draft the README content once the PNGs are confirmed exported and look good.

---

### Task 4 — Final commit and push [2 pts]

Commit everything in both repos:
- `python_agentic_learning`: final session archive, tasks cleared
- Portfolio repo: initial commit with full content

---

**Total: 10 pts**
