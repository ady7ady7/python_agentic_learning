# Weekend Quiz - Week 3

No notes, no code execution. Answer from memory - if unsure, say so rather than guessing.
Focus this week: trend regime definition, pullback-depth target, statistics
(normaltest/Mann-Whitney/Kruskal-Wallis), baselines, stop-survival tables.

---

## Part A - Regime definition

**A1.** Describe, in your own words, what `bull_separated` and `bear_separated` mean and
why the definition uses whole EMA channels (high/low pairs) rather than comparing two
single EMA values.

**A2.** Early in the week, a version of the regime label used `sign(EMA33_mid - EMA144_mid)`
computed fresh on every candle. What went wrong with that approach, and what was the fix?

**A3.** Why does `retracement_bull` include the case where price sits *inside* the EMA144
channel (between EMA144_low and EMA144_high), not just below it?

---

## Part B - The pullback target

**B1.** State the three possible outcomes (`status` values) for a pullback event, and in
one sentence each, what each one means.

**B2.** Why is `depth_price` measured differently for `recrossed` events (depth at the
moment of the recross) versus `resumed`/`unfinished` events (deepest point reached)?

**B3.** What does `ref_atr` need to be read from, exactly, and why would reading it from a
later candle be a problem?

**B4.** `same_candle_pullback` flags events resolved on the very next candle after the
reference point. What was the actual bug this flag helped catch, and what would have
happened to the reported depth if it hadn't been fixed?

---

## Part C - Statistics

**C1.** You compare two groups with `normaltest` and get p < 0.05 for both. What does that
tell you, and which test do you use next: a t-test or Mann-Whitney U? Why?

**C2.** What specifically does Mann-Whitney U compare between the two groups - describe the
mechanism, not just "it's non-parametric."

**C3.** Why is testing 24 hourly groups with one Kruskal-Wallis test better than running 24
separate two-group tests (e.g. hour 6 vs everything else, hour 7 vs everything else, ...)?

**C4.** Kruskal-Wallis gives p < 0.05 across 24 hourly groups. What can you conclude, and
what can you NOT conclude from this result alone?

**C5.** True or false, and explain: "subsampling to 200 rows before a statistical test is
fine as long as the test result is still significant."

---

## Part D - Baselines and the stop table

**D1.** You compute MAE = 1.0 for "always predict the median depth_atr." Is 1.0 a good or
bad result? What do you need to know before answering?

**D2.** The stop-survival table says "2.0 ATR survives 80% of the time" - but this number is
computed only on `status == 'resumed'` events. Explain precisely why including `recrossed`
events would change this number, and in which direction.

**D3.** Someone says: "the survival table proves a 2.0 ATR stop will make you profitable 80%
of the time." What is wrong with this claim?

---

## Part E - Judgement

**E1.** Midweek, the plan changed from "predict exact depth_atr with regression" to
"predict P(resumed) vs P(recrossed) given depth reached." What was the reasoning behind
this change, and what evidence (from this project or the sister repo) supported it?

**E2.** Name one real bug found this week that would NOT have thrown an error or crashed -
it would have just silently produced a plausible-looking wrong number. What made it
findable?

---

**When done, paste your answers and I will score them.**
