# Tasks - ML Phase Week 3 Day 4

**Time:** target 75-90 min.

**Where we are:** `project4_trend_regime/m15_pullback_events.csv` - 5,522 pullback events.
Yesterday we confirmed (Mann-Whitney, full data, p=2.56e-08) that EU pullbacks (hour 3-4 ET)
are statistically deeper than RTH ones (hour 10-11 ET). You also noticed something in the
boxplot: hours 6-7 and 16-19 ET looked unusually active.

Today: (1) a short, rigorous check on that hour pattern - is it real or did you eyeball
noise? (2) start of feature building for a model, now that we trust the target.

---

## Task 1 - Is the 6-7 / 16-19 pattern real? (25 min)

Yesterday's test compared exactly two groups (EU vs RTH). Today you're comparing across
all 24 hours at once, which changes what test is appropriate.

### Why not just run Mann-Whitney 24 times

You could compare hour 6 vs "everything else", then hour 7 vs "everything else", etc. But
running many tests on the same data inflates your false-positive rate: at a 5% significance
threshold, testing 24 independent hours means you'd expect ~1 to look "significant" by pure
chance even if none of them mean anything. This is the multiple comparisons problem.

### Kruskal-Wallis: the >2-group version of Mann-Whitney

`scipy.stats.kruskal` asks one combined question first: **"do these 24 groups all come from
the same distribution, or does at least one differ?"** It's the non-parametric equivalent of
a one-way ANOVA (which compares means across >2 groups and assumes normality - not
appropriate here, same reasoning as Mann-Whitney vs t-test).

- **H0:** all 24 hourly groups of `depth_atr` come from the same distribution (hour has no
  effect on pullback depth).
- **H1:** at least one hour's distribution differs from the others.

It does NOT tell you *which* hour differs, or by how much - only whether hour matters at
all, as a single yes/no gate before you go hunting for specific hours.

- 1a. Filter to `status == 'resumed'` (as before). Group `depth_atr` by hour (0-23).
- 1b. Run `scipy.stats.kruskal(*groups)` - unpack each hour's `depth_atr` values as a
     separate argument. Report the p-value.
- 1c. If (and only if) H0 is rejected, compute the median `depth_atr` for every hour and
     rank them - do hours 6, 7, 16, 17, 18, 19 actually stand out as a cluster, or was that
     an artifact of how the boxplot happened to look?

**In a comment:** based on the Kruskal-Wallis result and the per-hour medians, do you still
believe there's a real 6-7/16-19 effect, or does it look more like noise now that you're
looking at ranked medians instead of a visual impression?


from scipy.stats import kruskal
'''
- **H0:** all 24 hourly groups of `depth_atr` come from the same distribution (hour has no
  effect on pullback depth).
- **H1:** at least one hour's distribution differs from the others.
'''
pullback_df.head()

grouped_by_hour = pullback_df.groupby('hour')['depth_atr'].agg(
     mean_atr = ('mean')
).reset_index()
grouped_by_hour.head(15)

groups = []
for i in (pullback_df['hour'].unique()):
     groups.append(pullback_df['depth_atr'][pullback_df['hour'] == i])
     
results = kruskal(*groups)
print(results) #p_value = 4.337509543465713e-28, very close to 0


grouped_by_hour_median = pullback_df.groupby('hour')['depth_atr'].agg(
     median_atr = ('mean')
).reset_index().sort_values(by = 'median_atr', ascending = False)
grouped_by_hour_median.head(15)

'''
hour	median_atr
16	16	2.223377
23	23	2.114033
18	18	2.071305
6	6	2.024532
17	17	1.897854
19	19	1.789194
7	7	1.745000
20	20	1.742685
2	2	1.731529
4	4	1.710913
0	0	1.708876
22	22	1.625740
5	5	1.620733
1	1	1.606385
12	12	1.580137'''


#16-20 + 6-7 are relatively high, with 16 being visibly high above the rest
#There could be a real effect, but I'm unsure whether I'd be interested in trading during these hours anyway.

#16-20 are aftermarket hours, which could be volatile due to a hollow orderbook
#6-7 is the same case, but the opposite, it's early pre-market, during EU session, yet before the US opens.

#The ATR can be higher, but it's always relative to the recent price action and it doesn't necessarily mean there's volume behind
#In other words, I'm not particularly interested in those periods, but maybe it's worth to check it... Idk.


---

## Task 2 - First feature table for the depth model (30 min)

Time to build the X you'll eventually feed a model. Every feature here must be something
you'd actually know **at `ref_time`** - the moment the peak/trough was just established -
since that's when you'd want a depth prediction.

Build a new dataframe, one row per event (reuse the `resumed`-filtered set), with:

- `direction` (already have it) - encode as 0/1 (bear=0, bull=1) or keep as category, your
     choice, but note which you picked and why it matters for the model type you'd use later.
- `hour` (already have it, from `ref_time`).
- `ref_atr` (already have it) - this is the volatility level at the moment of reference.
- `is_same_candle_pullback` (already have it) - though think about whether this belongs as
     a *feature* (known before the fact) or is actually closer to a description of the
     outcome. Write down your reasoning either way.
- A new one: `prior_pullback_depth` - for events happening within the same underlying trend
     block, what was the depth of the *previous* pullback? (If you're not sure how to find
     "the previous one in the same trend", that's fine - describe the problem in a comment
     instead of guessing at code, and we'll solve it together next session.)

**In a comment:** which of these features do you expect to actually predict depth, and
which do you expect to be close to useless? You don't need to be right - the point is
committing to a guess before any model tells you the answer.


from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()
pullback_df['direction_int'] = encoder.fit_transform(pullback_df[['direction']]).astype(int)
pullback_df['prior_pullback_depth'] = pullback_df['depth_atr'].shift(1)

#I frankly think predicting depth of a pullback will be veery difficult.
#IMO it should be easier to predict the chances a given pullback will result in a resume or recross on certain ATR levels


pullback_df.head()
#all features for your refernece
'''direction	ref_time	ref_price	ref_atr	depth_price	depth_atr	duration_minutes	status	same_candle_pullback	hour	minute	direction_int	prior_pullback_depth
0	bull	2021-01-04 14:00:00-05:00	1942.610	2.983302	1.790	0.600006	30.0	resumed	False	14	0	1	NaN
1	bull	2021-01-04 14:30:00-05:00	1942.740	2.605102	0.662	0.254117	15.0	resumed	True	14	30	1	0.600006
2	bull	2021-01-04 14:45:00-05:00	1944.135	2.532022	3.117	1.231032	150.0	resumed	False	14	45	1	0.254117
'''


---

## Task 3 - Baseline once more, on the real feature set (15 min)

- 3a. Chronological 80/20 split on this new feature table.
- 3b. Report train-set median/mean `depth_atr` and the resulting MAE on test - same
     calculation as Day 3, just now living alongside the actual features you'll model with.

**In a comment:** has anything changed from yesterday's baseline numbers, and should it
have?


train = pullback_df[:math.floor(0.8 * len(pullback_df))]
test = pullback_df[math.floor(0.8 * len(pullback_df)):]

train_median = train['depth_atr'].median()
train_mean = train['depth_atr'].mean()

baseline_mae = mean_absolute_error(np.full(len(test), train_mean), test['depth_atr'])
baseline_mae_median = mean_absolute_error(np.full(len(test), train_median), test['depth_atr'])
print(baseline_mae, baseline_mae_median)

#1.2215080988640952 1.004526664451128

#I'm not exactly what does this data suggest, 1 ATR baseline doesn't look a very big error TBH
#The baseline is perhaps already very informative, or it trims dow and flattens bigger retracements into very small baseline
---

**Total: 3 tasks.** Task 2's `prior_pullback_depth` may not fully solve today - that's fine,
flag where you get stuck rather than forcing something fragile.
