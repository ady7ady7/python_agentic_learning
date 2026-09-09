# Tasks - ML Phase Week 3 Day 3

**Time:** target 75-90 min.

**Where we are:** `project4_trend_regime/m15_pullback_events.csv` exists - 5,522 pullback
events, built on M15 candles with H1 as the regime context. Columns: `direction` (bull/bear),
`ref_time`, `ref_price`, `ref_atr`, `depth_price`, `depth_atr`, `duration_minutes`, `status`
(resumed/recrossed/unfinished), `same_candle_pullback`.

We already found one real insight together: EU session pullbacks (03-05 ET) are meaningfully
deeper than RTH ones (10-12 ET) - medians 0.96 vs 0.75 ATR. Today you build on that with your
own analysis, statistics, and baselines - this is the part that's supposed to be yours.

---

## Task 1 - Load, filter, orient (10 min)

- 1a. Load the CSV, parse `ref_time` as datetime.
- 1b. Filter to `status == 'resumed'` only - this is the target we care about (recrossed
     and unfinished are different phenomena, not the pullback distribution itself).
- 1c. Print `.describe()` on `depth_atr` and `duration_minutes` for this filtered set.

**In a comment:** how many resumed events are you left with, and does the distribution
shape (mean vs median, skew) look like what you'd expect for something bounded at zero?

A question to ask here - does depth_price mean the difference between the high and the low of the pullback? We've started a lot lower in terms of prices, so this could be a bit misleading compared to the ATR, but whatever. The values look as follows:

Name: duration_minutes, dtype: float64
                         ref_time    ref_price      ref_atr  depth_price  \
count                        5278  5278.000000  5278.000000  5278.000000   
mean   2023-12-27 01:34:45.619553  2621.358610     4.758877     7.126762   
min           2021-01-04 14:00:00  1617.748000     0.487974     0.000000   
25%           2022-08-26 13:03:45  1843.448250     2.227819     1.707000   
50%           2024-02-22 18:15:00  2068.518000     3.424564     3.540000   
75%           2025-04-30 20:45:00  3288.272500     5.577013     7.570000   
max           2026-07-17 06:45:00  5495.785000    55.445449   233.727000   
std                           NaN   985.806401     4.504206    12.183361   

         depth_atr  duration_minutes  
count  5278.000000       5278.000000  
mean      1.611313        267.771883  
min       0.000000         15.000000  
25%       0.554021         15.000000  
50%       0.959917         15.000000  
75%       1.760733         75.000000  
max      22.858904      15390.000000  
std       2.056793       1010.355440  


There are 5278 events still in the DF with some nice differences and things tht we could probably visualize to see how these differ by duration minutes vs atr (size).


---

## Task 2 - Is EU vs RTH statistically real, or noise? (25 min)

We found EU median 0.96 vs RTH median 0.75 - a ~30% difference. A difference in two medians
you compute from a sample is not proof of anything by itself - with enough noise, two
random subsets of the SAME data will almost always show slightly different medians. The
question a statistical test answers is: **how surprising is a gap this large if there were
actually no real difference between EU and RTH?** If it's very surprising (a small
p-value), you have evidence the gap is real. If it's not surprising at all (large p-value),
the gap you saw could easily be random noise and you should not build anything on it.

### Why normaltest first

Which test is "correct" depends on the shape of the data. A t-test compares means and
assumes each group is roughly normally distributed (bell-shaped, symmetric). We already
saw in Task 1 that `depth_atr` is bounded at zero and right-skewed (a long tail of deep
pullbacks, a hard floor at zero) - that is NOT what a t-test expects, and running one
anyway risks a wrong p-value.

`scipy.stats.normaltest` tests exactly this:
- **H0 (null hypothesis):** the data comes from a normal distribution.
- **H1 (alternative):** it does not.
- **p < 0.05** → reject H0, the data is not normal (this is what we expect here).

### Why Mann-Whitney U, specifically

If the data isn't normal, you don't fix it by fudging a t-test - you switch to a test that
doesn't require normality at all. Mann-Whitney U works by RANKING every value from both
groups together (smallest = rank 1, next = rank 2, ...) and checking whether one group's
ranks tend to be systematically higher or lower than the other's - not by comparing means.
That makes it robust to skew and outliers, at the cost of only telling you about the
overall *tendency* (are EU values typically larger?), not the exact size of the difference
in the original units.

- **H0:** EU and RTH `depth_atr` come from the same distribution (no systematic
  tendency for one to be larger).
- **H1:** they don't - one tends to be larger than the other.

- 2a. Build the two groups: EU (hour between 3 and 5), RTH (hour between 10 and 12), same
     as before.
- 2b. Run `scipy.stats.normaltest` on `depth_atr` for the full resumed set - confirm it's
     non-normal (state the p-value).
- 2c. Run `scipy.stats.mannwhitneyu` comparing EU vs RTH `depth_atr` (use
     `alternative='two-sided'` since you're asking "are they different", not "is EU
     specifically larger").
- 2d. Report the p-value.

**In a comment, write out before you run anything:**
- What exactly is H0 here, in terms of THIS data (not the generic template above)?
- What would a p-value of 0.30 mean for the EU-vs-RTH claim - would you still trust the
  30% gap you found earlier? Answer this before you see your actual result.

**Then after running:** state the conclusion in plain terms - what does your actual
p-value tell you about whether EU and RTH pullbacks are really different?



from scipy.stats import normaltest, mannwhitneyu

#2a - adding hr/min for convenience
pullback_df['hour'] = pullback_df['ref_time'].dt.hour
pullback_df['minute'] = pullback_df['ref_time'].dt.minute

eu_pullbacks = pullback_df[(pullback_df['hour'] >= 3) & (pullback_df['hour'] <= 4)] #3:00 et - 5:00 et (10:00 EU - 12:00 EU)
eu_pullbacks = pullback_df[(pullback_df['hour'] >= 3) & (pullback_df['hour'] <= 4)]
eu_pullbacks.head(15) 

rth_pullbacks = pullback_df[(pullback_df['hour'] >= 10) & (pullback_df['hour'] <= 11)] #10:00 ET - 12:00 ET (16:00 EU - 18:00 EU)
rth_pullbacks.head(15) 

#2B testing whether depth atr on the whole dataset has a normal distribution
normaltest_results = normaltest(pullback_df['depth_atr'])
print(normaltest_results) 
#NormaltestResult(statistic=np.float64(182.06953704951587), pvalue=np.float64(2.9114032894630856e-40))
#p_value = 1.7076775229562615e-46 # H0 rejected (Data does not come from a normal distribution)

#now it's time to compare rth vs eu sets, whether they're meaningfully statistically different from each other
#H0: There are no differences between the datasets
#H1: The datasets are meaningfully different
comparison_test_results = mannwhitneyu(rth_pullbacks['depth_atr'], eu_pullbacks['depth_atr'], alternative='two-sided')
print(comparison_test_results)
#MannwhitneyuResult(statistic=np.float64(16799.5), pvalue=np.float64(0.005643195590467532))
#Again, p_value is way below 0.05, H0 rejected, the two datasets have meaningful statistical differences


'''- What would a p-value of 0.30 mean for the EU-vs-RTH claim - would you still trust the
  30% gap you found earlier? Answer this before you see your actual result.'''
  
#It would mean the datasets are similar to each other, and I wouldn't trust that gap :)), but it's not the case.
#We can see clear differences between the RTH vs EU and it makes sense as well, as RTH is the EU/US overlapping period,
# which could be more volatile overall, but also more ordered in terms of following a given direction more decisively
#but this is just my pure speculation, that doesn't make any sens without proof, and the reason doesn't even matter as well







---

## Task 3 - Baseline: how good is "always predict the median"? (20 min)

Before any model, establish what a trivial guess costs you - same principle as every
previous ML session.

- 3a. Split chronologically 80/20 by `ref_time` (sort first!).
- 3b. On the test set, compute MAE for: (i) always predict the training-set median
     `depth_atr`, (ii) always predict the training-set mean.
- 3c. Compute the same baselines separately for EU-hour and RTH-hour events in the test
     set - does a session-aware baseline (train-set EU median for EU events, train-set RTH
     median for RTH events) beat the single overall median?

**In a comment:** if a future model can't beat the session-aware baseline from 3c, is it
worth using?



import math
from sklearn.metrics import mean_absolute_error

pullback_df = pullback_df.sort_values(by = 'ref_time')
print(len(pullback_df))
train_set = pullback_df[:math.floor(0.8 * len(pullback_df))]
test_set = pullback_df[math.floor(0.8 * len(pullback_df)):]

median_baseline = np.full(len(test_set), train_set['depth_atr'].median())
mean_baseline = np.full(len(test_set), train_set['depth_atr'].mean())

test_baseline_mae_median = mean_absolute_error(test_set['depth_atr'], median_baseline)
test_baseline_mae_mean = mean_absolute_error(test_set['depth_atr'], mean_baseline)
print(test_baseline_mae_median, test_baseline_mae_mean)#1.004526664451128 1.2215080988640952



eu_train_set = eu_pullbacks[:math.floor(0.8 * len(eu_pullbacks))]
eu_test_set = eu_pullbacks[math.floor(0.8 * len(eu_pullbacks)):]

median_eu_baseline = np.full(len(eu_test_set), eu_train_set['depth_atr'].median())
mean_eu_baseline = np.full(len(eu_test_set), eu_train_set['depth_atr'].mean())

test_baseline_mae_median_eu = mean_absolute_error(eu_test_set['depth_atr'], median_eu_baseline)
test_baseline_mae_mean_eu = mean_absolute_error(eu_test_set['depth_atr'], mean_eu_baseline)

print(F'Eu baselines: MAE median: {test_baseline_mae_median_eu}, MAE mean: {test_baseline_mae_mean_eu}')
#Eu baselines: MAE median: 0.9029923329570835, MAE mean: 1.0331881627738368


rth_train_set = rth_pullbacks[:math.floor(0.8 * len(rth_pullbacks))]
rth_test_set = rth_pullbacks[math.floor(0.8 * len(rth_pullbacks)):]

median_rth_baseline = np.full(len(rth_test_set), rth_train_set['depth_atr'].median())
mean_rth_baseline = np.full(len(rth_test_set), rth_train_set['depth_atr'].mean())

test_baseline_mae_median_rth = mean_absolute_error(rth_test_set['depth_atr'], median_rth_baseline)
test_baseline_mae_mean_rth = mean_absolute_error(rth_test_set['depth_atr'], mean_rth_baseline)

print(F'RTH baselines: MAE median: {test_baseline_mae_median_rth}, MAE mean: {test_baseline_mae_mean_rth}')
#RTH baselines: MAE median: 0.8467832584731276, MAE mean: 0.8873829123913888


#If a model can't beat the baseline, it doesn't make sense to use it at all :)).






---

## Task 4 - Visualize the shape (15 min)

- 4a. Histogram of `depth_atr` (resumed only) - do the same skewed shape we've seen before.
- 4b. Same histogram, split by EU/RTH/other with `hue`, to see the shift visually alongside
     the statistical test.
- 4c. Box plot of `depth_atr` by hour of day (0-23) - is EU/RTH the whole story, or is there
     more structure across the full 24 hours?

**In a comment:** does the box plot suggest any other hour worth investigating beyond
EU/RTH, or does the pattern look like it's really just those two windows?


plt.figure(figsize = (20, 10))
histo_chart = sns.histplot(
     pullback_df['depth_atr']
)
plt.show()
#the left side looks a bit like a bell curve, but it has a huge tail to the right side, some extreme outrliers

#the issue with split by EU/RTH other will be a bit counterintuitive here, since I'm not naming EU/RTH as the whole EU/RTH session,
# but rather the windows that I usually like to trade in during these EU/RTH sessions
#For that reason I decided to do separate hisplots for EU/RTH pullbacks from the previously selected windows


plt.figure(figsize = (10, 8))
eu_pb_chart = sns.histplot(
     eu_pullbacks['depth_atr']
)
plt.show()

plt.figure(figsize = (10, 8))
rth_pb_chart = sns.histplot(
     rth_pullbacks['depth_atr']
)
plt.show()

#quite frankly all the charts look very similar, a bit bell-curve like structure on the left and a huge tail to the right, caused by the outliers


#and the boxplot you've asked for

plt.figure(figsize = (10, 8))
depth_atr_by_hour = sns.boxplot(
     pullback_df,
     x = 'hour',
     y = 'depth_atr'
     )
plt.show()

#by looking at the boxplot, I'm wondering whether I'm seeing the ET hours or hours in my local EU time,
#as the 6-7 window + 16-19 windows seem to be quite active





---

**Total: 4 tasks.** This is your session - own the numbers, don't just confirm what we
already suspect.
