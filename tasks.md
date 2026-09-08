# Tasks - ML Phase Week 3 Day 2

**Time:** target 60-75 min.

**Where we are:** `project4_trend_regime/h1_with_regime.csv` and `m15_with_regime.csv` exist,
built by `01_regime_labeling.py`. H1 regime label looks solid on visual inspection over
1500 bars - dominant strong_bear/strong_bull blocks in real trends, range_recross in
consolidation. Columns: `open/high/low/close`, `ema144_high/low`, `ema33_high/low`,
`atr14`, `bars_since_recross`, `regime` (5 categories), plus on H1 only:
`m15_regime_at_close`, `mtf_aligned_bull`, `mtf_aligned_bear`.

Today: get hands-on with this dataframe yourself - load it, look at it, verify a few things
independently rather than taking my regime logic on faith. No target, no model yet.

---

## Task 1 - Load and orient yourself (10 min)

- 1a. Load `h1_with_regime.csv` with `et_time` as a datetime index.
- 1b. Print `.info()` and `.describe()` - anything look off (nulls, weird ranges)?
- 1c. Print `regime.value_counts(normalize=True)` yourself and compare against what the
     script printed yesterday. Do the numbers match your own read of the chart?

**In a comment:** how many total rows, and what date range does this cover?

h1_df.info()

start, end = h1_df['et_time'].min(), h1_df['et_time'].max()
print(start, end)

#30500 rows, no nulls
#it covers 5+ years of data, from 2021-01-04 00:00:00 to 2026-07-17 14:00:00


print(h1_df['regime'].value_counts())
'''
regime
strong_bull         12609
strong_bear          8607
range_recross        7442
retracement_bull      974
retracement_bear      889
Name: count, dtype: int64
'''

#This looks quite optimistic, as it seems like trends occupy the most time, but there are also range_recross periods
#that surely could wipe out any account if not taken seriously




---

## Task 2 - Regime duration (20 min)

You said "the important thing is red dominates in a downtrend" - let's check that with
numbers, not just eyeballing.

For each *contiguous block* of the same regime (e.g. 40 consecutive `strong_bear` bars in a
row counts as one block, not 40), compute how many bars it lasted.

Hint for finding contiguous blocks without a loop:
```python
block_id = (h1["regime"] != h1["regime"].shift(1)).cumsum()
block_lengths = h1.groupby(block_id)["regime"].agg(["first", "size"])
```
`block_id` increases by 1 every time the regime changes, so rows with the same `block_id`
are one uninterrupted run of the same label. `.groupby(block_id)` then collapses each run
into one row: `first` is the regime name, `size` is how many bars it lasted.

- 2a. Build `block_lengths` as above.
- 2b. Group by regime name (`first`) and get mean/median/max block length for each of the
     5 categories.
- 2c. What fraction of `strong_bear` blocks last more than 10 bars? More than 50?

**In a comment:** does this match the visual impression - are strong trend blocks
meaningfully longer-lived than range_recross blocks, or surprisingly similar?


h1_df['block_id'] = (h1_df['regime'] != h1_df['regime'].shift(1)).cumsum()
block_lengths = h1_df.groupby(['block_id'])['regime'].agg(['first', 'size'])
print(block_lengths.head(50))
mean_block_lengths = block_lengths.groupby('first').agg(
    avg_block_length = ('size', 'mean'),
    median_block_length = ('size', 'median'),
    min_block_length = ('size', 'min'),
    max_block_length = ('size', 'max'),
)

longer_than_10 = block_lengths[(block_lengths['first'] == 'strong_bear') & (block_lengths['size'] >= 10)].count() / block_lengths[block_lengths['first'] == 'strong_bear'].count() * 100
print(longer_than_10) #55% of the strong bear trends out of all bears are longer than 10 hours long

longer_than_10 = block_lengths[(block_lengths['first'] == 'strong_bull') & (block_lengths['size'] >= 10)].count() / block_lengths[block_lengths['first'] == 'strong_bull'].count() * 100
print(longer_than_10) #60% of the strong bull trends out of all bulls are longer than 10 hours long

longer_than_10 = block_lengths[(block_lengths['first'] == 'range_recross') & (block_lengths['size'] >= 10)].count() / block_lengths[block_lengths['first'] == 'range_recross'].count() * 100
print(longer_than_10) #84% of the range_RECROSS regime occurences out of all range recrosses are longer than 10 hours long


'''                  avg_block_length  median_block_length  min_block_length  \
first                                                                       
range_recross            30.500000                 23.0                 1   
retracement_bear          4.233333                  3.0                 1   
retracement_bull          3.959350                  3.0                 1   
strong_bear              36.625532                 14.0                 1   
strong_bull              47.224719                 18.0                 1   

                  max_block_length  
first                               
range_recross                  153  
retracement_bear                18  
retracement_bull                20  
strong_bear                    320  
strong_bull                    375  
'''
#Not sure what to think here, but there are some trends that definitely last, and the tendency is towards the bullish dominance (47 vs 36 bull vs bear mean).
#Range_recross periods are also long, the mean is lower than the  strong_bear and bull.

#However, we can also see that most of the trend are not that long with 14-18 median block lengths
#The mean is elevated by the extreme outliers that can last 200+, and the median for range_recross is 23 hours.

#This suggests that these periods definitively need patience to hold trades
#I'd also like to check how these numbers look after we filter out the night/Asian time range.





---

## Task 3 - Look at the data yourself (20 min)

Pick any 2-3 stretches of the chart that interest you (open the PNG, note some dates) and
pull the actual rows for those dates - the same way we diagnosed the July 2nd flicker
yesterday.

- 3a. For one stretch you'd call a "clean strong trend", print the regime column for that
     window - is it mostly one label, or mixed?
- 3b. For one stretch that looks like consolidation/chop on the chart, do the same - is it
     mostly `range_recross`, or does the model disagree with your eye?
- 3c. If you find a spot where you disagree with the label, write down exactly which
     candle and why - don't fix the code, just flag it as a note.

**In a comment:** based on this, do you trust this regime label enough to build a target on
top of it next session, or is there something that still bothers you?


I've decided to portray all 3 regimes on different charts to see if there are any visible differences:

check_df = h1_df[(h1_df['regime'] == 'strong_bear')].copy()
linep = sns.lineplot(
    check_df,
    x = 'et_time',
    y = 'close'
    )
plt.show()


check_df = h1_df[(h1_df['regime'] == 'strong_bull')].copy()
linep = sns.lineplot(
    check_df,
    x = 'et_time',
    y = 'close'
    )
plt.show()


check_df = h1_df[(h1_df['regime'] == 'range_recross')].copy()
linep = sns.lineplot(
    check_df,
    x = 'et_time',
    y = 'close'
    )
plt.show()


#There are subtle nuances between the three charts and you can clearly see the price movement is different and definitely bearish/bullish/range, which looks like we have filtered out at least a fraction of unvaforable trading conditions with this simple differentiation. And I must add that bullish is a way more upwards than the bearish is downwards - in other wards, the bearish chart overall looks a bit similar to the range_recross regime chart, which is interesting.

Overall I'd say we're unable to create perfect distinction, but it's probably as good as we can get with minimum effort for getting favorable trading conditions, and I'd stick with that without looking for more nuanced differentation for convenience. And most definitely there are more and less trending periods, but overall it looks promising from this point of view. And it could maybe give some actually useful edge in the logn term.



I don't see a reason to go deeply into specific trends, as every trend willl look a bit different, depending on the context. Building observations on the basis of single trends doesn't make sense IMHO.


---

**Total: 3 tasks.** No coding of new logic today - this is about you owning the data before
we build the pullback target on top of it.
