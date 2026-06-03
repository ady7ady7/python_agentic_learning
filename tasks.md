# Tasks — Week 5 Day 3

## Pro Fold note + dollar decay + tier aggregation

---

### Task 1 — Pro Fold: add markdown note to flagship chart [1 pt]

Below the flagship launch price chart, add a markdown cell:

Explain in 1-2 sentences that Pixel Pro Fold is excluded because it's a foldable
device in a separate category, and that including it would place Google's ceiling
above Samsung Ultra for 2024 ($1,899 vs $1,299).



That's my whole write-up for that in the relevant markdown cell:

Below is a comparison of the official launch prices across all brands. The first chart focuses on base models (e.g., iPhone 15, Samsung Galaxy S22, Google Pixel 6), while the second highlights flagship submodels (iPhone Pro Max, Samsung Galaxy Ultra, Google Pixel Pro).

IMPORTANT NOTE: In Google's line, there is also the Pro Fold/Fold XL (it also takes #1 position in the chart above) which appeared for the first time in 2023, and is currently the most expensive version of Google Pixel Pro phone, but it is best understood as a premium form alternative rather than the absolute hardware pinnacle. While its $1,799 price tag reflects the complex engineering, flexible display, and R&D of a foldable, it actually compromises on traditional flagship metrics. Essentially, you are paying a massive premium for a versatile, pocketable tablet, but if your goal is the absolute best camera and performance hardware Google offers, the traditional Pixel Pro remains the true flagship.

Unlike Google’s Fold, the iPhone Pro Max and Samsung Galaxy Ultra are the undisputed, absolute hardware flagships of their respective brands with the best cameras, maximum efficiency and the largest batteries.


---

### Task 2 — Verify NEW units, build dollar decay charts [4 pts]

First, run this and check if the numbers look like phone prices in USD:
```python
df[df['submodel_name'] == 'iPhone 13']['NEW'].describe()
```
iPhone 13 Renewed should be roughly $400-700. Report what you see.

Then build dollar decay charts — one per brand:
- Groupby `submodel_name + days_rounded` → mean `NEW` (or `NEW/100` if needed)
- Filter each brand to the tiers that matter:
  - Apple: Base + Pro Max only (others too cluttered)
  - Samsung: Base + Ultra only (or closest equivalent)
  - Google: Base + Pro only
- Seaborn lineplot, x = days_rounded, y = mean price in USD, hue = submodel_name
- Add hlines at $500 and $300 as reference points
- Title per chart: "Price in USD over time — [Brand] submodels"

Observation after each chart: which submodel loses the most dollars?
At what point does the Pro Max become cheaper than the base model was at launch?


1. 
df[df['submodel_name'] == 'iPhone 13']['NEW'].describe()

count    49842.000000
mean       431.615981
std        126.293766
min        110.880000
25%        333.630000
50%        398.980000
75%        505.030000
max       1499.970000
Name: NEW, dtype: float64

I'd say it looks quite plausible.

We surely need this, but also for brands and I'm gonna do it the next time I think.


---

### Task 3 — Tier aggregation: decay and sales rank [4 pts]

**Part A — Price decay by tier (all brands combined)**

Filter `df` to tiers that appear across multiple brands: Base, Pro, Pro Max.
Groupby `tier + days_rounded` → mean `price_pct_of_launch`.
Seaborn lineplot: x = days_rounded, y = price_pct_of_launch, hue = tier.
Title: "Price decay by tier — all brands"

Does Pro Max consistently retain more value than Base?
Is there a clear tier hierarchy?

**Part B — Sales rank by tier**

Same but for `ms_df`: groupby `tier + days_rounded` → mean `monthly_sold`.
Filter to tiers with enough data (check value_counts first).
Seaborn lineplot, invert y-axis.
Title: "Sales rank by tier over lifecycle"

Do higher tiers sell worse (higher rank number) early but recover later?


#tier aggregation for price decay
all_brands_tier_price_decay_df = df.groupby(['brand', 'tier', 'days_rounded'])['price_pct_of_launch'].mean().reset_index()
apple_tier_price_decay_df = all_brands_tier_price_decay_df[all_brands_tier_price_decay_df['brand'] == 'Apple']
samsung_tier_price_decay_df = all_brands_tier_price_decay_df[all_brands_tier_price_decay_df['brand'] == 'Samsung']
google_tier_price_decay_df = all_brands_tier_price_decay_df[all_brands_tier_price_decay_df['brand'] == 'Google']



plt.subplots(figsize = (12, 6))
all_brands_submodels_price_chart = sns.lineplot(
    all_brands_tier_price_decay_df,
    x = 'days_rounded',
    y = 'price_pct_of_launch',
    hue = 'tier',
    marker = 'o'
)
plt.show()

#Apple
plt.subplots(figsize = (12, 6))
pd_submodels_1 = sns.lineplot(
    apple_tier_price_decay_df,
    x = 'days_rounded',
    y = 'price_pct_of_launch',
    hue = 'tier'
)
plt.show()


#Samsung
plt.subplots(figsize = (12, 6))
pd_submodels_1b = sns.lineplot(
    samsung_tier_price_decay_df,
    x = 'days_rounded',
    y = 'price_pct_of_launch',
    hue = 'tier'
)
plt.show()

#Google
plt.subplots(figsize = (12, 6))
pd_submodels_1c = sns.lineplot(
    google_tier_price_decay_df,
    x = 'days_rounded',
    y = 'price_pct_of_launch',
    hue = 'tier'
)
plt.show()



By looking at these charts:

Contrary to expectations, the standard iPhone Base models exhibit the highest price stability across generations. While the Pro Max performs exceptionally well in specific intervals, the Base model consistently retains a higher percentage of its launch value over the long term.

Samsung displays distinct phases of price retention:
The FE (Fan Edition) and Base models lead in value retention during the first year.
Around day 500, they get the Ultra tier starts getting in and slowly overtakes the lineup to claim the highest value retention before data tracking concludes (at around 1500 day mark).

The final hierarchy, not including the Ultra (not enough data yet) stabilizing in the later stages shows FE > Base > +.

Google’s lineup shows the sharpest polarization between tiers:
The budget-friendly Pixel 'a' series is the clear leader, consistently holding its value better than both the Base and Pro models.
Conversely, the Pro Fold, which I mentioned above, experiences the most severe and rapid depreciation in the entire dataset, failing to sustain its premium launch value over time.



It already feels like I've done enough for today.
The next goal will be to integrate it so that it makes perfect sense in our data order + also analyze the monthly sales in the same way and do the same.


---

**Total: 9 pts**
