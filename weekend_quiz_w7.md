# Weekend Quiz - Week 7

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.

---

## Part A - Drift and detrending

You're analyzing Bitcoin price (which has drifted upward massively over most of its
history) to check whether it "reverts" after unusually sharp 1-hour rallies.

**A1.** You compute `future_return_N = close.shift(-N) - close` and find positive future
returns after sharp rallies. A colleague says "see, momentum confirmed." What's the FIRST
thing you'd check before agreeing, given what happened with gold this month?

**A2.** Explain in your own words (not a formula) why measuring price relative to its OWN
rolling mean, rather than relative to today's raw price, removes the effect of a long-term
upward drift from a reversion/continuation comparison.

---

## Part B - Defining events correctly

**B1.** New scenario: you're studying whether a stock's RSI staying above 70 for multiple
consecutive days predicts a pullback. You count every day with RSI>70 as a separate "event"
and average the next-5-day return across all of them. What's the methodological problem
with this, based on what you learned testing z-score extremes this month?

**B2.** You fix B1 by only counting the FIRST day RSI crosses above 70 in each continuous
run. Write (in plain words, not code) what boolean logic identifies that first day, given a
column `is_extreme` that's True/False per row.

---

## Part C - The continuation target

**C1.** You're asked to build a target: "after an extreme event, does the move extend
further, or does it pull back first?" Within a fixed N-bar window, three outcomes are
possible: extends, pulls back, or neither happens. How did this project handle the "neither"
case, and why not just force it into one of the other two categories?

**C2.** A colleague suggests always using N=20 bars for this kind of target "since that's
standard." What's wrong with picking one horizon without checking others first, based on
what actually happened this month when 20 bars was the only horizon tested?

**C3.** Your first baseline classifier on a real continuation target gets ROC AUC = 0.56,
barely above a coin flip, even after trying `class_weight='balanced'`. A colleague says
"that means the whole project failed." How would you respond, given this month's experience?

---

## Part D - Judgement

**D1.** You've just discovered that two different, both-methodologically-sound analyses of
the same underlying question gave opposite conclusions (one said reversion, one said
continuation). What does this situation actually tell you about the data, and what should
you NOT conclude from it?

**D2.** A dataset shows 83.6% of events "continue" and 13.4% "reverse" - noticeably less
extreme than a 95/5 split you worked with earlier. Does this milder imbalance mean class-
imbalance techniques (class_weight, threshold tuning) are definitely unnecessary here, or is
there still a reason to check? Justify briefly.

---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
