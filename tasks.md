# Tasks — ML Phase Week 1 Day 2

**Theme:** designing a prediction problem that is actually solvable.
**Data:** `xauusd_m5_et.csv`
**Time:** 60–90 min

Yesterday's task 5 was unsolvable and you caught it: with the full daily OHLC in the features,
predicting `bullish` is reading the answer. Today we fix that properly.

The fix has three parts, and they are the foundation of every honest model:
1. **Split the day** — an observation window you can see, a target window you cannot
2. **Features from the past only** — everything known at the cut-off, nothing after
3. **Validation that respects time** — no training on the future

Target for today: **range of the afternoon session** — your own suggestion, and the right one.
Range is a volatility question, and volatility clusters. Direction does not.

---

## Task 1 — Split the trading day (15 min)

Build a daily DataFrame where each row splits the session in two:

**Morning window (observation): 03:00–09:55 ET**
- `am_open`, `am_high`, `am_low`, `am_close`, `am_bars`

**Afternoon window (target): 10:00–16:00 ET**
- `pm_high`, `pm_low`

Then:
- `pm_range` = `pm_high` − `pm_low`   ← **this is the target**

Keep only days where both windows have bars.

**In a comment:** what is the exact moment in the day at which a prediction would be made,
and how do you know none of your features come from after it?

df = pd.read_csv('xauusd_m5_et.csv')
print(df.head())

df['et_time'] = pd.to_datetime(df['et_time'])
df['trade_date'] = pd.to_datetime(df['trade_date'])

eu_session = df[(df['et_time'].dt.hour >= 3) & (df['et_time'].dt.hour <= 9)]
eu_session = eu_session.groupby(['trade_date']).agg(
    eu_open = ('open', 'first'),
    eu_high = ('high', 'max'),
    eu_low = ('low', 'min'),
    eu_close = ('close', 'last'),
    eu_bars = ('et_time', 'count')
).reset_index()
eu_session.head()

us_session = df[(df['et_time'].dt.hour >= 10) & (df['et_time'].dt.hour <= 15)]
us_session = us_session.groupby(['trade_date']).agg(
    us_open = ('open', 'first'),
    us_high = ('high', 'max'),
    us_low = ('low', 'min'),
    us_close = ('close', 'last'),
    us_bars = ('et_time', 'count')
).reset_index()
us_session.head()

us_session['us_range'] = us_session['us_high'] - us_session['us_low']
eu_session['eu_range'] = eu_session['eu_high'] - eu_session['eu_low']

df = us_session.merge(eu_session, on = 'trade_date')
df = df[(df['us_bars'] >= 0) & (df['eu_bars'] >= 0)]
df.head()

I've sligthly changed the naming to a more convenient eu/us names :)).

Obviously the prediction would be made at the us open and we'd have to eliminate all the us data to eliminate data leakage. We'd target the us_range I guess.


---

## Task 2 — Features, all from before 10:00 (25 min)

Build these on the daily frame. Every one must be knowable at 10:00 ET.

**From this morning:**
- 2a. `am_range` = am_high − am_low
- 2b. `am_return_pct` = open-to-close of the morning, in percent
- 2c. `am_close_loc` = where am_close sits inside the morning range, 0.0 to 1.0
- 2d. `am_bar_rng_mean` = mean of (high − low) across the morning's 5-min bars

**From previous days:**
- 2e. `pm_atr14` = mean `pm_range` over the previous 14 days
- 2f. `am_atr14` = mean `am_range` over the previous 14 days
- 2g. `prev_pm_range` = yesterday's `pm_range`

**Normalised:**
- 2h. `am_range_norm` = `am_range` / `am_atr14`

Drop rows with NaN. Print the shape and the correlation of each feature with `pm_range`.

**In a comment:** 2d requires going back to the 5-minute data after you have already
aggregated to daily. Explain how you did it, and why `am_range` alone does not capture
the same thing.


df['eu_return_pct'] = (df['eu_close'] - df['eu_open']) / df['eu_open'] * 100
df['eu_close_loc'] = (df['eu_close'] - df['eu_low']) / (df['eu_high'] - df['eu_low'])
#To achieve this step, I actualy had to modify the earlier step, as the current aggrgation is on daily level
#This is how I've done it 

# eu_session = df[(df['et_time'].dt.hour >= 3) & (df['et_time'].dt.hour <= 9)]
# eu_session['candle_range'] = eu_session['high'] - eu_session['low']
# eu_session = eu_session.groupby(['trade_date']).agg(
#     eu_open = ('open', 'first'),
#     eu_high = ('high', 'max'),
#     eu_low = ('low', 'min'),
#     eu_close = ('close', 'last'),
#     eu_bars = ('et_time', 'count'),
#     eu_bar_rng_mean = ('candle_range', 'mean')
# ).reset_index()
# eu_session.head()


df['us_atr14'] = df['us_range'].shift(1).rolling(14).mean()
df['eu_atr14'] = df['eu_range'].shift(1).rolling(14).mean()
df['prev_us_range'] = df['us_range'].shift(1)
df['eu_range_norm'] = df['eu_range'] / df['eu_atr14']

df = df.dropna()
df.head()
df.shape

test_df = df.copy().drop(columns = ['us_open', 'us_high', 'us_low', 'us_close', 'us_bars', 'us_bar_rng_mean'])

# I wasn't sure which correlation to use here
print('KENDALL')
kendall = test_df.corr('kendall')
display(kendall)

print('PEARSON')
pearson = test_df.corr('pearson')
display(pearson)

print('SPEARMAN')
spearman = test_df.corr('spearman')
display(spearman)




I've identified that 2d requires to go back - it wasn't a big deal, I've just pasted that in the comment so you can see :))

Shape:
(1398, 21)

PEARSON
trade_date	us_range	eu_open	eu_high	eu_low	eu_close	eu_bars	eu_bar_rng_mean	eu_range	eu_return_pct	eu_close_loc	us_atr14	eu_atr14	prev_us_range	eu_range_norm
trade_date	1.000000	0.470916	0.896163	0.895887	0.897784	0.897015	0.031534	0.595916	0.514031	-0.013320	0.065402	0.605483	0.701980	0.471469	0.015329
us_range	0.470916	1.000000	0.627686	0.629467	0.620284	0.623238	0.017349	0.806164	0.700206	-0.130696	0.011537	0.665781	0.654070	0.705924	0.231724
eu_open	0.896163	0.627686	1.000000	0.999867	0.999739	0.999642	0.029472	0.753142	0.646075	-0.052677	0.064990	0.794289	0.866332	0.618631	0.037331
eu_high	0.895887	0.629467	0.999867	1.000000	0.999723	0.999801	0.029451	0.756857	0.650974	-0.041674	0.070425	0.796033	0.867901	0.621964	0.041969
eu_low	0.897784	0.620284	0.999739	0.999723	1.000000	0.999885	0.029465	0.744094	0.632921	-0.036504	0.071997	0.791966	0.865021	0.613759	0.024197
eu_close	0.897015	0.623238	0.999642	0.999801	0.999885	1.000000	0.029520	0.748644	0.639227	-0.027828	0.080912	0.793990	0.866751	0.616666	0.030218
eu_bars	0.031534	0.017349	0.029472	0.029451	0.029465	0.029520	1.000000	0.015895	0.018479	0.000676	0.017056	0.011884	0.011181	0.002257	0.026564
eu_bar_rng_mean	0.595916	0.806164	0.753142	0.756857	0.744094	0.748644	0.015895	1.000000	0.897428	-0.146992	-0.002178	0.778862	0.790651	0.817300	0.325137
eu_range	0.514031	0.700206	0.646075	0.650974	0.632921	0.639227	0.018479	0.897428	1.000000	-0.193436	-0.005457	0.642204	0.650068	0.663866	0.599935
eu_return_pct	-0.013320	-0.130696	-0.052677	-0.041674	-0.036504	-0.027828	0.000676	-0.146992	-0.193436	1.000000	0.725000	-0.036875	-0.023406	-0.075123	-0.175177
eu_close_loc	0.065402	0.011537	0.064990	0.070425	0.071997	0.080912	0.017056	-0.002178	-0.005457	0.725000	1.000000	0.043978	0.046156	0.021387	-0.015094
us_atr14	0.605483	0.665781	0.794289	0.796033	0.791966	0.793990	0.011884	0.778862	0.642204	-0.036875	0.043978	1.000000	0.951555	0.720655	-0.009320
eu_atr14	0.701980	0.654070	0.866332	0.867901	0.865021	0.866751	0.011181	0.790651	0.650068	-0.023406	0.046156	0.951555	1.000000	0.681583	-0.054092
prev_us_range	0.471469	0.705924	0.618631	0.621964	0.613759	0.616666	0.002257	0.817300	0.663866	-0.075123	0.021387	0.720655	0.681583	1.000000	0.162625
eu_range_norm	0.015329	0.231724	0.037331	0.041969	0.024197	0.030218	0.026564	0.325137	0.599935	-0.175177	-0.015094	-0.009320	-0.054092	0.162625	1.000000
SPEARMAN
trade_date	us_range	eu_open	eu_high	eu_low	eu_close	eu_bars	eu_bar_rng_mean	eu_range	eu_return_pct	eu_close_loc	us_atr14	eu_atr14	prev_us_range	eu_range_norm
trade_date	1.000000	0.596678	0.953507	0.952756	0.954726	0.953696	0.031526	0.735753	0.641887	0.016979	0.066768	0.725915	0.807676	0.596759	-0.007450
us_range	0.596678	1.000000	0.647944	0.651239	0.644280	0.647385	0.044137	0.733739	0.655513	0.000002	0.059240	0.703668	0.666839	0.610558	0.130694
eu_open	0.953507	0.647944	1.000000	0.999552	0.999484	0.998983	0.049131	0.784907	0.678039	-0.003566	0.064503	0.792801	0.854732	0.647332	0.003129
eu_high	0.952756	0.651239	0.999552	1.000000	0.999467	0.999565	0.049384	0.788964	0.686623	0.014317	0.075850	0.794653	0.856122	0.648534	0.013436
eu_low	0.954726	0.644280	0.999484	0.999467	1.000000	0.999570	0.048792	0.777906	0.668587	0.015696	0.075471	0.790965	0.853369	0.643384	-0.008445
eu_close	0.953696	0.647385	0.998983	0.999565	0.999570	1.000000	0.049300	0.782974	0.677925	0.031930	0.094128	0.793357	0.854681	0.646003	0.002755
eu_bars	0.031526	0.044137	0.049131	0.049384	0.048792	0.049300	1.000000	0.027379	0.038636	0.000381	0.015869	0.007913	0.002412	-0.018239	0.041852
eu_bar_rng_mean	0.735753	0.733739	0.784907	0.788964	0.777906	0.782974	0.027379	1.000000	0.870535	-0.032544	0.061654	0.815903	0.853116	0.723720	0.254835
eu_range	0.641887	0.655513	0.678039	0.686623	0.668587	0.677925	0.038636	0.870535	1.000000	0.008623	0.087490	0.660901	0.688379	0.607711	0.580792
eu_return_pct	0.016979	0.000002	-0.003566	0.014317	0.015696	0.031930	0.000381	-0.032544	0.008623	1.000000	0.826082	0.003411	0.000668	-0.017229	-0.004262
eu_close_loc	0.066768	0.059240	0.064503	0.075850	0.075471	0.094128	0.015869	0.061654	0.087490	0.826082	1.000000	0.075171	0.066970	0.058825	0.038733
us_atr14	0.725915	0.703668	0.792801	0.794653	0.790965	0.793357	0.007913	0.815903	0.660901	0.003411	0.075171	1.000000	0.877290	0.755386	-0.045667
eu_atr14	0.807676	0.666839	0.854732	0.856122	0.853369	0.854681	0.002412	0.853116	0.688379	0.000668	0.066970	0.877290	1.000000	0.684258	-0.102810
prev_us_range	0.596759	0.610558	0.647332	0.648534	0.643384	0.646003	-0.018239	0.723720	0.607711	-0.017229	0.058825	0.755386	0.684258	1.000000	0.052787
eu_range_norm	-0.007450	0.130694	0.003129	0.013436	-0.008445	0.002755	0.041852	0.254835	0.580792	-0.004262	0.038733	-0.045667	-0.102810	0.052787	1.000000


---

## Task 3 — Look at the data before modelling (20 min)

Visualisation and statistics come first. A model trained on a relationship you have not
looked at is a guess with extra steps.

**3a. Distribution of the target.** Histogram of `pm_range`. Is it symmetric or skewed?
Add vertical lines for mean and median.

**3b. Does the morning actually relate to the afternoon?** Scatter of `am_range` (x) vs
`pm_range` (y). Then set both axes to log scale. In a comment: did that make the
relationship easier or harder to read, and why?

**3c. Correlation heatmap.** `sns.heatmap` of the correlation matrix for all your features
plus `pm_range`, with values annotated. Which feature relates most strongly to the target?

**3d. Volatility clustering, visually.** Line plot of `pm_range` across the full period.
In a comment: do quiet and violent stretches cluster together, or alternate randomly?
This is the entire premise of today's task — check whether it actually holds.

**3e. Quintile table.** Bucket `am_range` into 5 quantiles with `pd.qcut`. Per bucket print
mean and median `pm_range`, plus the count. Is the progression monotonic?

**In a comment:** based on 3a-3e alone, before fitting anything — do you expect a model to
work here? Yes or no, and name the evidence.

The distribution is certainly NOT symmetric, it's skewed to the right.


mean_us_range = df['us_range'].mean()
median_us_range = df['us_range'].median()

histplot = sns.histplot(
    df['us_range']
)


histplot.axvline(
    x = mean_us_range,
    color = 'r'
)
histplot.axvline(
    x = median_us_range,
    color = 'yellow'
)
plt.show()


eu_vs_us_scatterplot = sns.scatterplot(
    df,
    x = 'eu_range',
    y = 'us_range'
)
plt.show()



eu_vs_us_scatterplot = sns.scatterplot(
    df,
    x = 'eu_range',
    y = 'us_range'
)
eu_vs_us_scatterplot.set_xscale('log'),
eu_vs_us_scatterplot.set_yscale('log')
plt.show()
#QUITE HONESTLY, IT MAKES the results look much more distributed in the center of the chart,
#but it's completely useless as human brain cannot understand it properly - perhaps algos do, not sure


corr_heatmap = sns.heatmap(
    test_df.select_dtypes(include = 'number')
)
plt.show()

#no visible correlations, I've used test_df with data leakage features cut out alreaydy

plt.figure(figsize = (20, 10)) #increased the size to see more
us_range_lineplot = sns.lineplot(
    x = df[:1000]['trade_date'], #I also limited the visualization scope as it was very difficult to observe anything while looking at the full history
    y = df[:1000]['us_range']
)
plt.show()
#volatility seems to cluster and have a wave structure, but high-volatility periods seem to be less popular as well


volatility_buckets = pd.qcut(df['eu_range'], 5)
print(volatility_buckets.head())



---

## Task 4 — Is the relationship statistically real? (15 min)

A visible pattern and a statistically supported one are different claims.

**4a.** Test whether `pm_range` is normally distributed (`scipy.stats.normaltest`).
State the null hypothesis in your own words and what the p-value means here.

**4b.** Split days into two groups: `am_range` above vs below its median. Test whether
`pm_range` differs between the groups. Pick the correct test based on 4a and justify it.

**4c.** Report the correlation between `am_range` and `pm_range` two ways: Pearson and
Spearman. Explain why the two numbers differ.

**In a comment:** if 4b came back with p = 0.30, would you still build the model? What would
that tell you that the scatter plot did not?


from scipy.stats import normaltest, mannwhitneyu
import scikit_posthocs as sp

#H0: It's a normal distribution
#H1: It's NOT a normal distribution
us_range_distribution = normaltest(df['us_range'].sample(200))
print(us_range_distribution[1])
#close to 0, H0 rejected, not a normal distribution
#In that case, we'd use a nonparametric test - MannWhitney U, Kruskal Wallis

median_eu_range = df['eu_range'].median()
below_median_eu_range = df['us_range'][df['eu_range'] <= median_eu_range].sample(200)
above_median_eu_range = df['us_range'][df['eu_range'] >= median_eu_range].sample(200)

mw_test = mannwhitneyu(below_median_eu_range, 
                       above_median_eu_range
                       )

display(mw_test[1])
#picking samples instead of full DFs

#H0: There's no meaningful difference between the groups
#H1: There's a meaningful difference between the groups.
sp.posthoc_dunn(
    [below_median_eu_range, above_median_eu_range]
)


'''
3.380588784020326e-77
np.float64(5.2039612781732755e-21)
1	2
1	1.000000e+00	5.182604e-21
2	5.182604e-21	1.000000e+00
'''

#The p-values are below 0, there seems to be a statistically meaningfull difference between the two groups


I'm honestly not so sure about this section..



---

## Task 5 — Baselines before any model (15 min)

You cannot judge a model without knowing what costs nothing.

Split the data chronologically, 80/20. On the **test** set only, compute MAE and R² for:

- 5a. Always predict the training-set **mean** of `pm_range`
- 5b. Always predict the training-set **median**
- 5c. Predict `prev_pm_range` (yesterday's value)
- 5d. Predict `pm_atr14` (the 14-day rolling mean)

Print all four in one table, sorted by MAE.

**In a comment:** which baseline is hardest to beat, and why is that one the honest
benchmark rather than the mean?


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

X = test_df.drop(columns = ['us_range'])
y = test_df['us_range']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    shuffle = False
)

#I don't know what do you mean here - how AM I SUPPOSED to compute mae and R2 without training a model DUDE? This task is either very unclear or completely nonsense, I'm not sure which option.





---

## Task 6 — First real model (20 min)

- 6a. Fit a `LinearRegression` on the training set, predict on test.
- 6b. Report MAE, RMSE, R² on test — and the same three on train.
- 6c. Compare against the best baseline from Task 5. Better or worse, and by how much?
- 6d. Plot predicted vs actual as a scatter, with a diagonal reference line.

**In comments:**
- Does linear regression need feature scaling here? Answer yes or no and justify it.
- What does the train-vs-test gap tell you?
- If the model beats the mean baseline but loses to `pm_atr14`, what is your verdict?



from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

model = LinearRegression()
model.fit(X_train, y_train)

train_y_pred = model.predict(X_train)
train_mae = mean_absolute_error(y_train, train_y_pred)
train_r2 = r2_score(y_train, train_y_pred)
train_rmse = root_mean_squared_error(y_train, train_y_pred)

y_pred = model.predict(X_test)
test_mae = mean_absolute_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)
test_rmse = root_mean_squared_error(y_test, y_pred)

print(f'Train values: MAE: {train_mae}, R2 {train_r2}, RMSE {train_rmse}')
print(f'Test values: MAE: {test_mae}, R2 {test_r2}, RMSE {test_rmse}')


Train values: MAE: 4.026452759244498, R2 0.3344725256666109, RMSE 6.254345342145135
Test values: MAE: 14.993502938684792, R2 0.4709428259030948, RMSE 27.80561074625558




---

## Task 7 — Where does it fail? (15 min)

Using the test-set predictions from Task 6:

- 7a. Split the actual `pm_range` into 5 quantile buckets.
- 7b. For each bucket: mean actual, mean predicted, MAE.
- 7c. State in one sentence where the model is weakest.

**In a comment:** is the error evenly spread, or concentrated? What would that mean for
someone using this to size a position?

Again I give up here, not sure exactly how to do it here....


---

**Total: 7 tasks.** Sections 3-4 are the pre-modelling checks - do not skip them to get to the model. Paste solutions and comment answers when done.

Pandas methods you will likely need today — worth knowing cold:
`.mean()` on a 0/1 column, `pd.qcut`, `.merge()`, `.between()`, `sns.heatmap`,
`scipy.stats.normaltest`, `mannwhitneyu`, `pearsonr` / `spearmanr`, `sns.heatmap`,
`scipy.stats.normaltest`, `scipy.stats.mannwhitneyu`, `scipy.stats.pearsonr` / `spearmanr`
