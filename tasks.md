# Tasks - ML Phase Week 3 Day 5

**Time:** target 45-60 min - short session, Friday wrap-up.

**Where we are:** `project4_trend_regime/m15_pullback_events.csv` now has `block_id` and a
correctly-computed `prior_pullback_depth`. Yesterday you proposed switching from "predict
exact depth_atr" to "predict P(resumed) vs P(recrossed) given how deep the pullback has
already gone" - this mirrors the stop-survival table from regimatic-ml's
insights_korekty.md (§4), which found real signal there on a different instrument (NDX).

Today: build the same kind of table on our XAUUSD data, and see if the pattern shows up
here too. This is the last task of the week - short and concrete.

---

## Task 1 - The stop-survival table (35 min)

The question: **"if you set a stop at X ATR beyond the reference point, what fraction of
pullbacks stay within it (i.e. the trend resumes before price goes that deep)?"**

A pullback "surviving" a stop of X ATR means: its `depth_atr` never exceeded X before the
trend resumed. For `status == 'recrossed'` events, the trend never resumed at all - so by
definition, a stop couldn't have "survived" them in the same sense (there's a separate
question buried here, see the comment prompt below).

- 1a. Filter to `status == 'resumed'` only for now (recrossed handled separately below).
- 1b. For a range of stop levels - try `[0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0]` (in ATR
     units, matching `depth_atr`) - compute what fraction of resumed events had
     `depth_atr <= X`. This is "the stop would have survived."
- 1c. Put this in a table: one row per stop level, one column for the survival fraction.
     Compare it to regimatic-ml's numbers for reference (not to match exactly - different
     instrument - but to see if the *shape* is similar): their 1.0 ATR stop survived 19%,
     2.0 ATR survived 53%, 5.0 ATR survived 82%.

**In a comment before building this:** `recrossed` events are excluded from the survival
fractions here, same as regimatic-ml did. Why does dropping them make the "survival" number
optimistic rather than neutral? (Hint: think about what a recrossed event actually
represents for someone who set a stop at, say, 3 ATR and the trend never came back.)


#W3 D5 T11
#start 11:33

#I've reloaded the file to go back from getting the filtered pullbacks only
pullback_df = pd.read_csv('project4_trend_regime/m15_pullback_events.csv')

#converting ref time to datetime + filtering to resumed pullbacks only, also turning it into America/Ny Time to make sure it's ET time
pullback_df['ref_time'] = pd.to_datetime(pullback_df['ref_time']).dt.tz_localize('America/New_York')
pullback_df['hour'] = pullback_df['ref_time'].dt.hour
pullback_df['minute'] = pullback_df['ref_time'].dt.minute

pullback_df['status'].value_counts()
#5278 resumed
#243 recrossed (only about 5%)


pullback_df = pullback_df[pullback_df['status'] == 'resumed']

#how many % of the time the pullback depth is less than or equal toa  given ATR level
atr_range = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0]
survival_rates = {
     'atr': atr_range, 
     'survival_rate': [
          (pullback_df['depth_atr'] <= i).sum() / len(pullback_df) for i in atr_range
          ]
     }

survival_df = pd.DataFrame(survival_rates)
survival_df.head(15)


'''	
     atr	survival_rate
0	0.5	0.213338
1	1.0	0.520652
2	1.5	0.692497
3	2.0	0.791967
4	3.0	0.878742
5	4.0	0.919667
6	5.0	0.941266
7	8.0	0.975748

'''

#Below there are values from regimatic-ml for reference from NQ - remember in this repo I work with gold
#How many of pullbacks WILL not reach a given ATR level and the trend will resume if we set a stop at that level?
'''

| Level | All | Bull | Bear |
|---|---|---|---|
| 1.0 ATR | 19 % | 21 % | 15 % |
| 1.5 ATR | 40 % | 41 % | 36 % |
| **2.0 ATR** | **53 %** | 54 % | 51 % |
| 2.5 ATR | 62 % | 63 % | 60 % |
| 3.0 ATR | 69 % | 70 % | 68 % |
| 4.0 ATR | 77 % | 77 % | 76 % |
| **5.0 ATR** | **82 %** | 82 % | 82 % |
| 6.0 ATR | 86 % | 86 % | 86 % |
| 8.0 ATR | 90 % | 90 % | 91 % |
| 10.0 ATR | 93 % | 92 % | 94 % |

'''






---

## Task 2 - Does EU vs RTH change the safe stop level? (15 min)

You already proved statistically (Day 3) that EU pullbacks run deeper than RTH ones. That
should show up directly in this table.

- 2a. Rebuild the same survival table from Task 1, split into EU-hour (3-4) and RTH-hour
     (10-11) subsets.
- 2b. For a fixed target survival rate (pick 80%), what stop level (in ATR) does each
     session need to hit it?

**In a comment:** does this match what you'd expect given Wednesday's statistical result,
and would this change how you'd size a stop differently for a EU-session vs RTH-session
trade?





pullback_df.head()
eu_pullbacks = pullback_df[(pullback_df['hour'] >= 3) & (pullback_df['hour'] <= 4)] #3:00 et - 5:00 et (10:00 EU - 12:00 EU)
rth_pullbacks = pullback_df[(pullback_df['hour'] >= 10) & (pullback_df['hour'] <= 11)] #10:00 ET - 12:00 ET (16:00 EU - 18:00 EU)

atr_range = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0]
survival_rates_eu = {
     'atr_range': atr_range,
     'survival_rate': [
          (eu_pullbacks['depth_atr'] <= i).sum() / len(eu_pullbacks) for i in atr_range
          ]
}

survival_df_eu = pd.DataFrame(survival_rates_eu)


survival_rates_rth = {
     'atr_range': atr_range,
     'survival_rate': [
          (rth_pullbacks['depth_atr'] <= i).sum() / len(rth_pullbacks) for i in atr_range
          ]
}

survival_df_rth = pd.DataFrame(survival_rates_rth)

display(survival_df_eu.head(15))
display(survival_df_rth.head(15))

'''
EU SURVIVAL RATES: 

atr_range	survival_rate
0	0.5	0.184579
1	1.0	0.535047
2	1.5	0.693925
3	2.0	0.801402
4	3.0	0.890187
5	4.0	0.925234
6	5.0	0.946262
7	8.0	0.974299
'''


'''
RTH SURVIVAL RATES

atr_range	survival_rate
0	0.5	0.314700
1	1.0	0.670807
2	1.5	0.809524
3	2.0	0.881988
4	3.0	0.939959
5	4.0	0.958592
6	5.0	0.973085
7	8.0	0.995859
'''


#To survive 80% of the time, EU needs a stop of 2.0 ATR, and RTH 1.5, so EU is more volatile (IN TERMS OF ATR!) and needs a bigger stop in terms of ATR.
#The findings match my expectations from Wednesday

#So sure, it could affect the sizing, but in the end, the RTH stop could still be bigger in points,
#as it will be certainly more volatile in terms of points, but it's interesting to see that in terms of ATR, the EU session is more volatile




---

**Total: 2 tasks.** Short Friday session - this closes out the week with one concrete,
checkable result. Weekend quiz comes separately once this is done.
