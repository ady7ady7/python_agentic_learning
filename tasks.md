# Tasks - ML Phase Week 7 Day 4

**Time:** target 75-90 min.

**Where we are:** Yesterday's multi-horizon test flipped the hypothesis - extreme-high
z-score episodes show trend CONTINUATION (deviation grows monotonically to N=100), while
extreme-low episodes deepen then partially reverse by N=100 (weaker, delayed, asymmetric).
Full writeup in `project4_trend_regime/mean_reversion_findings.md`. Today: define an actual
binary classification target from this, mirroring the pullback project's resumed/recrossed
design exactly - continuation vs. no-continuation, not reversion.

---

## Warm-up (10 min) - repetition: dict comprehension, fresh column

Straight repeat, no escalation.

```python
m15 = pd.read_csv('./project4_trend_regime/m15_with_regime.csv', parse_dates=['et_time'])
```

**Your turn:** build a dict comprehension mapping each `regime` value to the fraction of its
rows where `atr14` is above the overall 75th percentile of `atr14` (same inline-boolean-then
-mean shape, different threshold - a percentile instead of median/mean this time).

---

## Task 1 - Define the continuation target (30 min)

**The goal in plain words:** for each episode (first bar of a continuous extreme run, same
definition as yesterday), does price make a NEW, MORE EXTREME high/low within N bars - i.e.
does the move continue further - or does it fail to extend and instead pull back? This
mirrors `resumed` (new extreme reached) vs `recrossed` (reverted without extending) from the
pullback project exactly, just applied to z-score episodes instead of EMA-channel pullbacks.

- 1a. Rebuild `deviation_30`, `z_score_30`, and the episode flags
     (`new_high_episode`/`new_low_episode`) fresh, self-contained - same code as the last two
     days, don't assume leftover notebook state.
- 1b. For each HIGH episode: record `ref_close` (the close price at the episode's first
     bar). Over the next N bars (try N=20 first, matching earlier tests), check if ANY later
     close exceeds `ref_close` (a new, more extreme high - continuation) BEFORE any close
     drops back to `close.rolling(30).mean()` taken at the episode bar (a reversion/failure
     to continue). Mirror this with lows for LOW episodes (new lower low = continuation,
     touching the rolling mean first = failure).
- 1c. Build `target_continued` (1 if continuation happened first, 0 if reversion/mean-touch
     happened first, within the N-bar window). Rows where NEITHER happens within N bars are
     ambiguous - drop them for now (same "can't resolve within the window" logic as
     `unfinished` events in the pullback project).

**In a comment:** what fraction of episodes show continuation vs. reversion-first vs.
ambiguous/dropped? Does the high/low asymmetry found yesterday show up here too (e.g. high
episodes continuing more often than low episodes)?





m15_df = pd.read_csv('project4_trend_regime/m15_with_regime.csv')
m15_df['deviation_30'] = m15_df['close'] - m15_df['close'].rolling(30).mean()
m15_df['z_score_30'] = m15_df['deviation_30'] / m15_df['deviation_30'].rolling(30).std()

is_extreme_high = m15_df['z_score_30'] > 2.5
is_extreme_low = m15_df['z_score_30'] < -2.5
m15_df['new_high_episode'] = is_extreme_high & ~is_extreme_high.shift(1, fill_value=False)
m15_df['new_low_episode'] = is_extreme_low & ~is_extreme_low.shift(1, fill_value=False)

m15_df['ref_close'] = m15_df.apply(lambda x: x['close'] if x['new_high_episode'] == 1 or x['new_low_episode'] == 1 else np.nan, axis = 1)
m15_df['ref_close'] = m15_df['ref_close'].ffill()
m15_df = m15_df.dropna()
m15_df = m15_df.reset_index(drop=True)


def check_continuation_high(df, event_idx, n_bars=20):
    ref_close = df['close'].iloc[event_idx]
    ref_mean = df['close'].rolling(30).mean().iloc[event_idx]
    
    for k in range(1, n_bars + 1):
        future_idx = event_idx + k
        if future_idx >= len(df):
            return None  
        future_close = df['close'].iloc[future_idx]
        if future_close > ref_close:
            return 1  
        if future_close <= ref_mean:
            return 0 
    return None


high_event_positions = m15_df.index[m15_df['new_high_episode']].tolist()

results = []
for pos in high_event_positions:
    outcome = check_continuation_high(m15_df, pos, n_bars=20)
    results.append({'event_idx': pos, 'target_continued': outcome})

high_targets_df = pd.DataFrame(results)
print(len(high_targets_df))
high_targets_df = high_targets_df.dropna()
print(len(high_targets_df))
print(high_targets_df['target_continued'].value_counts())

# 2198
# 2113
# target_continued
# 1.0    1860
# 0.0     253
# Name: count, dtype: int64




def check_continuation_low(df, event_idx, n_bars=20):
    ref_close = df['close'].iloc[event_idx]
    ref_mean = df['close'].rolling(30).mean().iloc[event_idx]
    
    for k in range(1, n_bars + 1):
        future_idx = event_idx + k
        if future_idx >= len(df):
            return None  
        future_close = df['close'].iloc[future_idx]
        if future_close < ref_close:
            return 1  
        if future_close >= ref_mean:
            return 0 
    return None


low_event_positions = m15_df.index[m15_df['new_low_episode']].tolist()

results = []
for pos in low_event_positions:
    outcome = check_continuation_low(m15_df, pos, n_bars=20)
    results.append({'event_idx': pos, 'target_continued': outcome})

low_targets_df = pd.DataFrame(results)
print(len(low_targets_df))
low_targets_df = low_targets_df.dropna()
print(len(low_targets_df))
print(low_targets_df['target_continued'].value_counts())

# 1953
# 1867
# target_continued
# 1.0    1586
# 0.0     281
# Name: count, dtype: int64




---

## Task 2 - First feature table (25 min)

Same mechanical-feature approach as the pullback project.

- 2a. For each resolved episode (continuation or reversion-first, not ambiguous), build:
     `direction` (1 for high episodes, 0 for low - the asymmetry from yesterday suggests this
     matters a lot here), `hour` (from `et_time`), `atr14` (volatility context),
     `abs_z_score` (how extreme the triggering deviation was).
- 2b. Quick sanity check: group by `direction` and compute `target_continued.mean()` - does
     this match yesterday's finding (high episodes continuing more, given they showed
     monotonic growth vs. low episodes' partial reversal)?

**In a comment:** does this numeric check from 2b match your expectation from yesterday's
multi-horizon table, or is there a surprise?



high_targets_df['direction'] = 1
low_targets_df['direction'] = 0

all_targets_df = pd.concat([high_targets_df, low_targets_df], ignore_index=True)


m15_df['abs_z_score'] = m15_df['z_score_30'].abs()
m15_df['hour'] = pd.to_datetime(m15_df['et_time']).dt.hour

feature_cols = ['hour', 'atr14', 'abs_z_score', 'et_time']
all_targets_df = all_targets_df.merge(
    m15_df[feature_cols],
    left_on='event_idx',
    right_index=True
)

all_targets_df.head()
print(all_targets_df['target_continued'].mean())
0.8658291457286432



---

## Task 3 - Time-aware split + baseline (20 min)

- 3a. Sort by the episode's `et_time`, time-aware 80/20 split (no shuffling).
- 3b. Compute the "always predict the majority class" baseline accuracy on test - is this
     target closer to balanced (50/50-ish, given continuation and reversion are both common
     outcomes) or imbalanced like the pullback project's resumed/recrossed (95/5)?

**In a comment:** given the class balance here, does this feel like a genuinely different
(and in some ways easier/more interesting) ML problem than the pullback classifier's extreme
imbalance - why or why not?



all_targets_df = all_targets_df.sort_values(by = 'et_time')

train = all_targets_df[:int(0.8*(len(all_targets_df)))]
test = all_targets_df[int(0.8*(len(all_targets_df))):]


all_targets_df['target_continued'].value_counts()
print(534 / (534 + 3446)) #13.4% reversed / 83.6% continued

#It feels similar, but 83.6 - 13.4 is not as drastic difference as in returned/recrossed


---

**Total: 3 tasks + warm-up, ~75 min.** Defining the problem properly, same as Week 4 Day 1
for the pullback project - no model fitting until tomorrow.
