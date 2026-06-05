# Tasks — Week 6 Day 1

## Finish + polish 07_final_project_adjusted_sns.ipynb

---

### Task 1 — Fix base_apple_df variable collision [bug]

In the pipeline cell, `base_apple_df` is defined twice:
- First for price decay: `df[(df['tier'] == 'Base') & (df['brand'] == 'Apple') & (df['generation_name'] != 'iPhone 17')]`
- Then overwritten for sales: `submodel_ms_df[(submodel_ms_df['brand'] == 'Apple') & (submodel_ms_df['tier'] == 'Base')]`

The price decay charts downstream use `base_apple_df` and will silently use the wrong data on re-run.
Fix: rename the sales version to `apple_base_ms_df` and update the chart cell that references it.

---

### Task 2 — Fix stale methodology note (cell-2)

Currently says:
- "Monthly_sold shows a sales rank rather than the number of goods sold"
- "Actual sales volume data was omitted..."

Both are now wrong. Update to reflect the actual approach: Keepa sales estimate brackets summed per month, used as a relative indicator, not omitted.

---

### Task 3 — Add 1yr and 2yr price retention by tier

New barplots showing price retention at ~1 year and ~2 years, broken down by tier per brand.
Directly backs up the sales findings (e.g. iPhone 13 Pro Max holding value better at 2yr = explains late-lifecycle buyer preference for it).

Pattern:
```python
retention_1yr_df  # already exists (days_rounded 330–380)
retention_2yr_df = df[(df['days_rounded'] > 700) & (df['days_rounded'] < 750)]
```
Then groupby `['generation_name', 'tier']`, barplot `hue='tier'`, one chart per brand.
Place in Section 5 (Price decay by tier) or as a bridge into the sales section.

---

### Task 4 — Update Key findings section

Add two missing bullets:
- iPhone 13 Pro Max as the undisputed secondary market king — late-lifecycle buyers chase it specifically because price has dropped enough to make the top-tier hardware accessible
- Q4 and Prime Day seasonality — all brands spike in Q4, Google and Apple also spike in July 2025, consistent with Prime Day

---

**Total: 4 tasks**
