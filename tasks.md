# Tasks — Week 6 Day 1

## Finish + polish 07_final_project_adjusted_sns.ipynb

---

### Task 1 — Fix base_apple_df variable collision [bug]

In the pipeline cell, `base_apple_df` is defined twice:
- First for price decay: `df[(df['tier'] == 'Base') & (df['brand'] == 'Apple') & (df['generation_name'] != 'iPhone 17')]`
- Then overwritten for sales: `submodel_ms_df[(submodel_ms_df['brand'] == 'Apple') & (submodel_ms_df['tier'] == 'Base')]`

The price decay charts downstream use `base_apple_df` and will silently use the wrong data on re-run.
Fix: rename the sales version to `apple_base_ms_df` and update the chart cell that references it.

Done and tested, it works properly now.

---

### Task 2 — Fix stale methodology note (cell-2)

Currently says:
- "Monthly_sold shows a sales rank rather than the number of goods sold"
- "Actual sales volume data was omitted..."

Both are now wrong. Update to reflect the actual approach: Keepa sales estimate brackets summed per month, used as a relative indicator, not omitted.


Fixed that, thanks.

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

That doesn't work - the day window is a bit too long for some of the most interesting examples.
Instead of that, I'd like to annotate my price decay for tiers in a proper way and add relevant observations there.

I want to add 1yr/2yr, maybe even 3 year shades (that get a bit darker as we go further in time) on the chart, annotate them properly and add annotations for respective tier pricing after a given period of time.
That should be enough to back up some of my findings later.

For now I've deleted the whole retention_2yr_df section + charts after testing them out - it's not the right path.
---

### Task 4 — Update Key findings section

Add two missing bullets:
- iPhone 13 Pro Max as the undisputed secondary market king — late-lifecycle buyers chase it specifically because price has dropped enough to make the top-tier hardware accessible
- Q4 and Prime Day seasonality — all brands spike in Q4, Google and Apple also spike in July 2025, consistent with Prime Day

I've added some findings that make sense, you're wrong with the 13 Pro Max as well.

# Key findings

- **All brands' sales spike in Q4** and there are few factors or events that could affect that. For iPhones, end of September usually signifies the launch of a new generation, and then there's Black Friday (November) and Christmas (December).
- **Apple retains value best.** At the one-year mark, iPhones hold significantly more of their
  launch price than Samsung or Google. The 50% barrier comes around 900 days for Apple vs
  roughly 500 days for Samsung and 420 for Google. This tendency continues throughout the lifecycle.

- **iPhone 13 as the undisputed secondary market king**. Our data shows that this is the best selling iPhone generation on the secondary market at this moment in time. This could be due to the fact that it offers a perfect balance of reasonable pricing and great hardware.
 
- **Renewed Premium holds its value better than standard Renewed.** For iPhones the gap
  averages around 10.3 percentage points and stays fairly stable
  throughout the lifecycle. It's not just a launch-window premium.

- **The Pixel 5 is an anomaly.** For some reason it outperforms every other Google model at the one-year mark.
  It could be due to the fact that low launch price plus early discontinuation created supply constraints that kept its
  secondary market value elevated longer than expected, but this is just a speculation at this point.

- **Budget-conscious buyers drive the secondary market for older generations.** In the iPhone 13 lineup, the base model and the Mini show significantly higher sales and volatility than the premium Pro Max. This suggests that when looking at older generations, buyers are heavily driven by price and affordability rather than chasing top-tier flagship capabilities.

These are the current findings.

---

**Total: 4 tasks**
