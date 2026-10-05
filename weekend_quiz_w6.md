# Weekend Quiz - Week 6

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.

#start 12:01

---

## Part A - Fair model comparison

You're comparing a tuned `RandomForestClassifier` against an `XGBClassifier` on a new
dataset (customer churn). The RF was tuned with `RandomizedSearchCV` over a bounded grid;
the XGBoost was fit once with library defaults.

**A1.** Before concluding "RF wins," what's wrong with this comparison, based on what you
did in Week 6 Day 1 vs Day 2?


Both models should receive either the same tuning OR simply the best possible tuning for their needs. Otherwise it's not a fair comparison.


**A2.** You give XGBoost a fair, bounded-grid tuning pass too, and it still loses to RF on
test AUC - but XGBoost's feature importances are much more evenly spread across features
than RF's. What does that spread pattern suggest about the architectural difference between
the two algorithms (not just "XGBoost is worse here")?


It shows that XGB's probably way more balanced in terms of increasing or decreasing features' weights, which probably suggests that it could do better when the features are more balanced (which was not the case in my particular feature set). RF on the other hand was very straight forward in assigning futures' importance and it seemed to reflect the reality better, as I was able to test the features with visuals/statistic tests before - it pretty much acted as it knew some features are close to useless and their importances need to be put down. It seems like RF is a good choice to distinguish between good/bad features, especially if the feature set is not as good, but I might be wrong. I didn't test multiple different scenarios, just used my dataset with some features.

These algorithms are just different, I wouldn't say one is better than the other.


---

## Part B - Mean-reversion toolkit, new instrument

You're now asked to check for mean-reversion in a completely different instrument - say,
a tech stock's price relative to its own 50-day moving average.

**B1.** You run the Hurst Exponent on the RAW stock price (not a deviation series) over 10
years and get H=0.68. A colleague says "clearly trending, no mean-reversion here, stop
looking." What's wrong with using this single number to shut down the investigation (think
about what question that H value actually answers.

We're looking at a raw value on an asset that's probably trending long-term, instead of checking how it really moves from the standard error over time (which would really measure what we want to know). The results would be skewed indead, and even as we look at deviations, we'd probably be better testing a few windows.


**B2.** You then correctly compute deviation = price - rolling(50).mean(), run ADF on it,
and get p=0.001 (reject random walk). Half-life comes out to 140 days. Is this a usable,
tradeable mean-reversion signal? Justify using the standard tradeable range from this
month's research.

I don't think it's usable, 140 days to come back 50% is probably not the best signal to trade. It's not 100% sure by all means, as we'd have to test a specified strategy on a specified asset to make sure, but in most cases, itw ould be useless.


**B3.** New scenario: a colleague argues "if ADF rejects random walk, that alone proves
mean-reversion is profitable to trade." What's missing from that argument - name the ONE
additional thing (beyond statistical existence) that determines whether something is
actually a good trade.

That would be a very naive approach - we'd have to check a few things:
- whether the signals are even tradable, and the move sizes are enough to cover the costs/fees + slippage
- possible SL/TP scenarios and outcomes
- we'd have to check how often these esignals are available
- we'd have to check IF THE SIGNALS are actually distinguishable from fake signals/non signals in reality, as it's easy to ANALYZE past, but we'd have to only take measures that would normally be available to us at the time of taking a given trade in the past. Is it a workable, tradable strategy?
- and maybe more factors, depending on our current portfolio, strategies etc.


---

## Part C - The momentum/reversion contradiction (this week's real open question)

**C1.** You compute `future_return_N = close.shift(-N) - close` and split rows by whether
`z < -2` or `z > 2` (z-score of deviation from a rolling mean). The z<-2 group shows NEGATIVE
average future returns and the z>2 group shows POSITIVE average future returns - the
opposite of what mean-reversion would predict. Before concluding "this market has momentum,
not reversion," what's one concrete confound you'd want to rule out first (think about what
else was happening to the instrument's price over the whole sample period)?

I'd like to check whether this is just a standard drift on a given market, or something beyond that, that's actually usable/tradable.


**C2.** Suppose after removing that confound, the pattern still doesn't clearly support
reversion at z=±2, but DOES show up clearly at z=±3.5 (more extreme). What would that tell
you about where any real edge in this data might actually live?

That shows there might be some signals after extreme moves, near 3-4 std. Whether it makes sense or not, would require careful consideration of many factors + backtesting etc. I guess there are some strategies that use extreme deviations and are profitable, just an educated guess. I don't think a strategy has to trade every day to be profitable, and in most cases it would be the oppsoite.

---

## Part D - Judgement

**D1.** A colleague wants to test 15 different z-score thresholds (±1.0 through ±4.0 in
steps of 0.2) against future returns and will "just use whichever threshold gives the best
result." What's the statistical risk in that approach, and how does it connect to something
you learned about parameter grids earlier this month?


It's connected with data mining issue that might show good results in a single grid just by randomness, which wouldn't work in the real life.That's obviously a risk, and yet I think we still have to test thresholds and just look at some range on that grid instead of just one set of parameters. E..g imo if the range of parameters around 3.0, 3.5, 4.0 z-score would yield similar (positive) results, that would suggest it's probably not a coincidence and an issue of randomness/data mining, but rather a viable, possible signal for further checks.


**D2.** You're told "not a model yet - just the first honest look" before any ML is built on
top of a new feature. Why does that ordering (verify the raw relationship BEFORE fitting a
model) matter, using one concrete failure mode that skipping it could cause?


From my experience, features that don't show any relationships or strong effect with the target without any model, are not magically turned into something useful as we create ML model and use these features to train it. I'd say it's the opposite, e.g. they can dilute the real results given by features that actually matter.


#finish 12:25


---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
