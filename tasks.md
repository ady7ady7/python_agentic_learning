# Tasks — Week 5 Day 4

## Reorder + USD charts + sales rank by tier

---

### Task 1 — Remove debug cell and reorder notebook [3 pts]

1. Delete the `df[df['submodel_name'] == 'iPhone 13']['NEW'].describe()` cell (currently Cell 9)

2. Reorder cells in Jupyter to match this structure:
```
1.  Title + methodology
2.  KPI board
3.  Official launch prices (section header)
     — Barplot sorted by value
     — Base models over time
     — Flagship models over time + Pro Fold note
4.  Price decay analysis — % of launch (section header)
     — All brands combined (annotated)
     — Apple by generation (Renewed vs Premium)
     — Samsung by generation
     — Google by generation
     — iPhone 13 submodels
5.  Price decay by tier (section header)
     — All brands combined by tier
     — Apple tiers
     — Samsung tiers
     — Google tiers
6.  Dollar price decay — USD (section header)  ← NEW, built in Task 2
7.  Brand comparison at 1 year (annotated barplot)
8.  Price distribution (boxplot)
9.  Sales rank analysis (section header)
     — Base iPhones lifecycle
     — iPhone 13 + 16 submodels
     — Real dates with vlines
     — Sales rank by tier  ← NEW, built in Task 3
10. Key findings
```

Add a short markdown section header before each numbered section if not already there.


#I've ordered everything as you wanted - now I'm creating the dollar price decay, and then I will also add the sales rank by tier :)).

---

### Task 2 — USD price decay charts [3 pts]

Groupby `submodel_name + days_rounded` → mean `NEW` (already in USD).
Build one chart per brand, filtered to Base + top tier only:
- Apple: `tier` in `['Base', 'Pro Max']`, exclude iPhone 17
- Samsung: `tier` in `['Base', 'Ultra']` — where Ultra doesn't exist use `'+'`
- Google: `tier` in `['Base', 'Pro']`

Seaborn lineplot per brand, hue = submodel_name.
Add hlines at 500 and 300.
Titles: "Price in USD over time — Apple", "...Samsung", "...Google"

One markdown observation per chart: at what point does the Pro Max/Ultra/Pro
become cheaper in dollars than the base model was at launch?



Few things here.
First of all, this whole step was very long and took me about 2 hrs or maybe even more, I'm not sure, but we're ending today's session with that as I could've overestimated my capabilities for today :D.

Nevertheless, it's a lot of very important work, and I've also included Samsung Edge and Google Pro Fold as both were very interesting phenomena to cover.
Currently I've decided we're putting these things into 4 separate cells

intro md + 1 chart + markdown for all brands means

3 charts + 1 markdown for all brand-specific submodels price action, so this is how it all looks like:


md1:
## Price decay in USD

While looking at percentage drops is important, analyzing price decay in raw USD is vital. It provides a clear, real-world benchmark of what each brand or tier actually costs over time.

Below are the price decay charts in USD. First, you will see the average prices for all brands and tiers combined. After that, the charts break down the price decay for base and flagship models for each specific brand (Google chart also includes Pro Fold as an interesting phenomenon). Please note that these figures show the average price across all generations, storage options and colors, so actual prices may vary depending on the exact version.

chart1:

dollar_all_brands_price_decay_df = df.groupby(['brand', 'submodel_name', 'days_rounded', 'tier'])['NEW'].mean().reset_index()

apple_dollar_price_decay_df = dollar_all_brands_price_decay_df[(dollar_all_brands_price_decay_df['brand'] == 'Apple') & ((dollar_all_brands_price_decay_df['tier'] == 'Base') | (dollar_all_brands_price_decay_df['tier'] == 'Pro Max'))]
samsung_dollar_price_decay_df = dollar_all_brands_price_decay_df[(dollar_all_brands_price_decay_df['brand'] == 'Samsung') & ((dollar_all_brands_price_decay_df['tier'] == 'Base') | (dollar_all_brands_price_decay_df['tier'] == 'Ultra') | (dollar_all_brands_price_decay_df['tier'] == 'Edge'))]
google_dollar_price_decay_df = dollar_all_brands_price_decay_df[(dollar_all_brands_price_decay_df['brand'] == 'Google') & ((dollar_all_brands_price_decay_df['tier'] == 'Base') | (dollar_all_brands_price_decay_df['tier'] == 'Pro') | (dollar_all_brands_price_decay_df['tier'] == 'Pro Fold'))]

plt.subplots(figsize = (14, 6))
pd_dollar_chart1 = sns.lineplot(
    data = dollar_all_brands_price_decay_df,
    x = 'days_rounded',
    y = 'NEW',
    hue = 'brand'
)
plt.axhline(1000, color='red', linestyle='dotted', linewidth=2)
plt.axhline(500, color='red', linestyle='dotted', linewidth=2)
plt.title('Price decay in USD across all brands (mean)')
plt.xlabel('Time in days since launch (relative)')
plt.ylabel('Price in USD')
plt.legend(loc = 'upper right', fontsize = 14)
plt.tight_layout()

md2 + intro to the brand tier comparisons:
The above analysis expands on what we know about the price action of these brands.

Looking at the overall brand averages, Apple smartphones maintain a constant premium of about 200–400 USD over the competition throughout their entire lifecycle. At certain points, some iPhones can be as much as 100% more expensive than their direct competitors. Eventually, the average floor price for an iPhone stabilizes around 200-300 USD.

Google and Samsung both start at an average launch baseline of 700-800 USD. However, Samsung holds its value slightly better after the first year, maintaining a steady 100 USD premium over Google on average throughout the most of the lifecycle from that point. Samsung's floor price settles near 200 USD around 1,500 days after launch, while Google drops a bit lower to about 150-180 USD in the same timeframe.

Naturally, these brand-level charts use broad averages across all models and submodels, meaning they show general trends rather than exact calculations for a specific phone. It's also worth checking how the tiers perform within the brands.

----------------------------------------------------

#### Brand tier comparisons

charts2:

plt.subplots(figsize = (14, 6))
pd_dollar_chart1a = sns.lineplot(
    data = apple_dollar_price_decay_df,
    x = 'days_rounded',
    y = 'NEW',
    hue = 'tier'
)
plt.axhline(1000, color='red', linestyle='dotted', linewidth=2)
plt.axhline(500, color='red', linestyle='dotted', linewidth=2)
plt.title('Price decay in USD across iPhone tiers (mean) - the base model vs Pro Max')
plt.xlabel('Time in days since launch (relative)')
plt.ylabel('Price in USD')
plt.legend(loc = 'upper right', fontsize = 14)
plt.tight_layout()
plt.show()




plt.subplots(figsize = (14, 6))
pd_dollar_chart1b = sns.lineplot(
    data = samsung_dollar_price_decay_df,
    x = 'days_rounded',
    y = 'NEW',
    hue = 'tier'
)
plt.axhline(1000, color='red', linestyle='dotted', linewidth=2)
plt.axhline(500, color='red', linestyle='dotted', linewidth=2)
plt.title('Price decay in USD across Samsung tiers (mean) - the base model vs Ultra and the Edge phenomenon')
plt.xlabel('Time in days since launch (relative)')
plt.ylabel('Price in USD')
plt.legend(loc = 'upper right', fontsize = 14)
plt.tight_layout()
plt.show()





plt.subplots(figsize = (14, 6))
pd_dollar_chart1c = sns.lineplot(
    data = google_dollar_price_decay_df,
    x = 'days_rounded',
    y = 'NEW',
    hue = 'tier'
)
plt.axhline(1000, color='red', linestyle='dotted', linewidth=2)
plt.axhline(500, color='red', linestyle='dotted', linewidth=2)
plt.title('Price decay in USD across Google tiers (mean) - the base model vs Pro and the Pro Fold phenomenon')
plt.xlabel('Time in days since launch (relative)')
plt.ylabel('Price in USD')
plt.legend(loc = 'upper right', fontsize = 14)
plt.tight_layout()
plt.show()



md3 with extensive description/observations:

## Apple - premium and strong retention
At launch, the Pro Max carries a massive premium over the Base model, exceeding 600 USD (roughly a 75% markup). However, this gap shrinks rapidly. In the first year, the Pro Max loses about 40% of its launch price on the second market, going below the 1000 USD mark, while the Base model proves much more stable, losing only 20%. This cuts the initial Pro Max price premium in half to around 300 USD.

This 250–300 USD tier premium remains steady for the first three years. By day 1600, the Pro Max sits at 400 USD compared to the Base at 300 USD. Eventually, after 2000 days, the Pro Max hits a solid price floor of 280 USD, while the Base model bottoms out near 200 USD.


## Samsung - the Edge anomaly and strong Ultra performance

Within the Samsung ecosystem, the Edge submodel stands out with an aggressive price decay. Starting at around 950 USD, right between the Base and Flagship tiers, it plummets to match the Base model at 600 USD in just 150-180 days. This rapid drop is most likely tied to the hardware and repair risks mentioned earlier.

Meanwhile, renewed Ultra models enter the market at roughly 1150 USD, holding a 400-500 USD premium over the Base model. Ultra falls below 1000 USD within months, settling at 800-850 USD after one year. Interestingly, its premium decays slower and holds well over time compared to corresponding iPhones (which are also more expensive), maintaining a stable 200-300 USD gap. Near day 1400, the Ultra remains strong at 350 USD, with an expected floor of 200-250 USD past the 2000-day mark. As for the Base Samsung, it stabilizes around 150-180 USD, performing only slightly below the Base iPhone over the long term.

## Google - the Pro Fold crash and small tier differences

Despite entering the market at the highest price point in the dataset (1700 USD), the Pro Fold suffers the fastest decay in the entire dataset. It plummets to 1000 USD within 6 months. After brief fluctuations, it breaks below 1000 USD at the one-year mark and hits the 700-800 USD range by day 500, losing over 50% of its value in record time.

Unlike Apple and Samsung, Google's Pro and Base models are remarkably close to each other, with an initial premium of just 200-250 USD. This gap narrows even more to under 100 USD after year one. Both tiers experience a massive first-year drop: the Base model falls from 800 USD to 500 USD, and the Pro version drops from 1000 USD to nearly match it shortly after.

The Base version hits an initial floor of 200 USD at year 2, dips to 150–180 USD by year 4, and shows a surprising late-lifecycle uptrend back to 200 USD near day 2000. The Pro model follows a similar path, hitting a 300 USD floor at year 2, dipping to 250 USD at year 4, and fluctuating down to 200 USD around day 1500–1600, leaving it just 20–40 USD pricier than the Base model.



I'm wondering if these are put appropriately in this order and so that these are not split into 3 separate charts + 3 separate markdowns respectively for each brand, but perhaps this order shows the differences in a clearer way. State your opinion on that.

In the later stages I might decide to add some annotations or markings here and there and we will also have to recheck our key findings in the end of the analysis as we're done with everything, but I'm very happy about today's performance and progress.


---

### Task 3 — Sales rank by tier [2 pts]

Using `ms_df`, check tier coverage first:
```python
ms_df['tier'].value_counts()
```

Groupby `tier + days_rounded` → mean `monthly_sold`.
Filter to tiers with enough data (>200 rows).
Seaborn lineplot, invert y-axis, hue = tier.
Title: "Sales rank by tier over lifecycle (lower = more sold)"

Do higher tiers start with worse rank (less popular early) and improve later?
Any tier that bucks expectations?

---

**Total: 8 pts**
