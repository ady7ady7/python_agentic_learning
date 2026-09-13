# Weekend Quiz - Week 3

No notes, no code execution. Answer from memory - if unsure, say so rather than guessing.
Focus this week: trend regime definition, pullback-depth target, statistics
(normaltest/Mann-Whitney/Kruskal-Wallis), baselines, stop-survival tables.

---

#Start 12:17

## Part A - Regime definition

**A1.** Describe, in your own words, what `bull_separated` and `bear_separated` mean and
why the definition uses whole EMA channels (high/low pairs) rather than comparing two
single EMA values.

It means the ema channels do not touch or cross each other, so that the closer channel is fully separated from the latter channel - it's simple as that, no need to say more. Channel gives more balanced approach and allows to avoid some fake signals.



**A2.** Early in the week, a version of the regime label used `sign(EMA33_mid - EMA144_mid)`
computed fresh on every candle. What went wrong with that approach, and what was the fix?

What the fuck is that question about? Should I remember every single issue? XD
I guess it causes more fake signals than the channel approach.



**A3.** Why does `retracement_bull` include the case where price sits *inside* the EMA144
channel (between EMA144_low and EMA144_high), not just below it?

Because the trigger included one ema, not both.
Another stupid question - how does that supposed to help me learn useful concepts in my case? It's a memory question about this week's tasks rather than something that makes sense.


---

## Part B - The pullback target

**B1.** State the three possible outcomes (`status` values) for a pullback event, and in
one sentence each, what each one means.

Again... stupid memory question.
I think it was resumed/recrossed/ongoing (or something equivalent)

resumed - price went back to the extreme
recrossed - the trend failed and the emas recrossed
ongoing - not decided YET


**B2.** Why is `depth_price` measured differently for `recrossed` events (depth at the
moment of the recross) versus `resumed`/`unfinished` events (deepest point reached)?


- because we want to have a real perspective on levels which can cause recross, what's the point in measuring an extreme if it turns into an opposite trend, if it's not a pullback anymore?


**B3.** What does `ref_atr` need to be read from, exactly, and why would reading it from a
later candle be a problem?

- We need to have a repetitive angle on every single situation like that, the pullback time can vary, the ATR will also vary every single time, so the measuring way varies with that. But if we use the set method with the same reference time (the extreme), it gives much more repetitiveness.


**B4.** `same_candle_pullback` flags events resolved on the very next candle after the
reference point. What was the actual bug this flag helped catch, and what would have
happened to the reported depth if it hadn't been fixed?


A lot of "pullbacks" were in-candle minimal, even very tiny moves that wouldn't be available to trade realistically, considering the costs etc. That skewed the results deeply and would greatly undermine observations and lower the median/avg pullback levels. It was simply noise, a lot of noise.

---

## Part C - Statistics

**C1.** You compare two groups with `normaltest` and get p < 0.05 for both. What does that
tell you, and which test do you use next: a t-test or Mann-Whitney U? Why?

It means values in the groups don't have normal distirbutions and they must be compared with Mann-Whitney U, because that's a non-parametric statistical test to see if there are statistically meaningful differences between them. Otherwise we'd use a t-test.



**C2.** What specifically does Mann-Whitney U compare between the two groups - describe the
mechanism, not just "it's non-parametric."


It compares whether their values are different in a statistically meaningful way, besides just noise and randomness etc. p < 0.05 means that they're statistically meanignful differences.


**C3.** Why is testing 24 hourly groups with one Kruskal-Wallis test better than running 24
separate two-group tests (e.g. hour 6 vs everything else, hour 7 vs everything else, ...)?

It's one operation, much cleaner + Kruskal-Wallis only shows IF there's any scenario where 1 group differst from another in a statistically meaningful way, it doesn't show the magnitude or anything like that. If we want to know more, we'd have to run a posthoc test e.g. Dunn.

**C4.** Kruskal-Wallis gives p < 0.05 across 24 hourly groups. What can you conclude, and
what can you NOT conclude from this result alone?

I already covered it above - there's at least ONE situation where two groups differ from each other in a meaningful way, nothing else and nothing more.


**C5.** True or false, and explain: "subsampling to 200 rows before a statistical test is
fine as long as the test result is still significant."

False, but I don't remember why exaclty - please remind me, as I want to know and remember such things.

---

## Part D - Baselines and the stop table

**D1.** You compute MAE = 1.0 for "always predict the median depth_atr." Is 1.0 a good or
bad result? What do you need to know before answering?

That really depends, we'd need to know the magnitude of ATRs etc. If that's like 50 and we're only away 1.0 with the prediction or statistical average, that would be great. Totally different if ATRs range around 0.5-1.5 etc.

**D2.** The stop-survival table says "2.0 ATR survives 80% of the time" - but this number is
computed only on `status == 'resumed'` events. Explain precisely why including `recrossed`
events would change this number, and in which direction.


It would certainly lower the number, as we can easily assume all recrossed events go way below 2.0 ATR.



**D3.** Someone says: "the survival table proves a 2.0 ATR stop will make you profitable 80%
of the time." What is wrong with this claim?

False, already explained above, as it's only a part of real scenarios, false assumption. It's fair to say that based on our research, 2.0 ATR stop should make you survive 80% of the 'resumed' scenarios, nothing more.

---

## Part E - Judgement

**E1.** Midweek, the plan changed from "predict exact depth_atr with regression" to
"predict P(resumed) vs P(recrossed) given depth reached." What was the reasoning behind
this change, and what evidence (from this project or the sister repo) supported it?

Again - retarded question about memory from this weeks tasks, but alright. I've already tested and determined that predicting the exact ranges and prices on the market is probably impossible, at least in this scope, so it doesn't make any sense.



**E2.** Name one real bug found this week that would NOT have thrown an error or crashed -
it would have just silently produced a plausible-looking wrong number. What made it
findable?


That would definitely be using only resumed scenarios and omitting all the others and assume that's how the market works, but you'd have to be retarded to believe that frankly. Ther ecould be other scenarios, but that's 100% that case you've just mentioned.


Finish 12:34

---

**When done, paste your answers and I will score them.**
