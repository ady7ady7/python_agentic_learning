# Weekend Quiz - Week 7

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.

---

## Part A - Drift and detrending

#start 13:07

You're analyzing Bitcoin price (which has drifted upward massively over most of its
history) to check whether it "reverts" after unusually sharp 1-hour rallies.

**A1.** You compute `future_return_N = close.shift(-N) - close` and find positive future
returns after sharp rallies. A colleague says "see, momentum confirmed." What's the FIRST
thing you'd check before agreeing, given what happened with gold this month?


I'd check whether it's not just a natural drift, it would be worth to compare the price reaction vs mean price, or deviation first.



**A2.** Explain in your own words (not a formula) why measuring price relative to its OWN
rolling mean, rather than relative to today's raw price, removes the effect of a long-term
upward drift from a reversion/continuation comparison.


Mean already covers general price's tendency to move in a certain direction - so it should take the drift away and show how the price reacted in a particular moment. Of course, if there's a drift, why shouldn't we follow it anyway, if it makes money. It's just that one wants to find BETTER spots to take risk etc.


---

## Part B - Defining events correctly

**B1.** New scenario: you're studying whether a stock's RSI staying above 70 for multiple
consecutive days predicts a pullback. You count every day with RSI>70 as a separate "event"
and average the next-5-day return across all of them. What's the methodological problem
with this, based on what you learned testing z-score extremes this month?

I'm mistaking one single event for a number of events (as every candle with RSI above 70 is interpreted as a different event). That's a real issue.


**B2.** You fix B1 by only counting the FIRST day RSI crosses above 70 in each continuous
run. Write (in plain words, not code) what boolean logic identifies that first day, given a
column `is_extreme` that's True/False per row.

First occurence of each cross below 70 can have an assigned ID, which is then kept for eveyr other candle until the price recrosses the RSI70. That mitigates the issue to some extent. Thre would be of course situations, where price crosses RSI70, goes back a little bit, and then recrosses it etc., but one must know that we won't be able to cover every single event with 100% accuracy, and there are perhaps compromises to be made. Of course, some metalabeling etc. could be done, if the project's resources allowed that and if that made a huge difference - always an option to consider.

---

## Part C - The continuation target

**C1.** You're asked to build a target: "after an extreme event, does the move extend
further, or does it pull back first?" Within a fixed N-bar window, three outcomes are
possible: extends, pulls back, or neither happens. How did this project handle the "neither"
case, and why not just force it into one of the other two categories?


I think we've deleted all the flat events - there weren't many of these, like 1-3% if I remember correctly, so doing that shouldn't pose a threat to our observations integrity etc. Keeping them could skew the results of other categories though - I'm not 100% certain that was the absolute best solution, but it works quite well.


**C2.** A colleague suggests always using N=20 bars for this kind of target "since that's
standard." What's wrong with picking one horizon without checking others first, based on
what actually happened this month when 20 bars was the only horizon tested?

The answer is as simple as "you never know anything before you've tested it, never trust your intuition before you've checked it". Nothing more to add - how is one supposed to know what is the best N, unless it's properly tested?


**C3.** Your first baseline classifier on a real continuation target gets ROC AUC = 0.56,
barely above a coin flip, even after trying `class_weight='balanced'`. A colleague says
"that means the whole project failed." How would you respond, given this month's experience?

First of all, I'd make sure all reasonable options and solutions were exhausted before accepting such an extreme thesis. Obviously, we don't want to do excessive data mining and looking for effects that are not there, but we want to objectively assess data and make sound, unbiased decisions. If that was done and there is no effect, well maybe that colleague was right - accepting "failure" is totally fine, as we reject an area that won't bring us anythign valuable and we can spend our resources on build elsewhere, where it actually matters and gives meaningful results.

---

## Part D - Judgement

**D1.** You've just discovered that two different, both-methodologically-sound analyses of
the same underlying question gave opposite conclusions (one said reversion, one said
continuation). What does this situation actually tell you about the data, and what should
you NOT conclude from it?

There are many options:
- perhaps our analysis was sound, yet performed at a different time horizon - both conclusions could make sense on the same dataset, if we adopted different scopes/contexts
- perhaps analysis only seemed sound, but in some way it was done differently and we need to check our methodology once again
- I wouldn't draw any major conclusions before properly checking data + methodologies used for drawing both conclusions - opposite conclusions clearly show that there's some discrepacny that needs to be cleared and addressed, so we understand why that's the case.
No clear decisions before that.


**D2.** A dataset shows 83.6% of events "continue" and 13.4% "reverse" - noticeably less
extreme than a 95/5 split you worked with earlier. Does this milder imbalance mean class-
imbalance techniques (class_weight, threshold tuning) are definitely unnecessary here, or is
there still a reason to check? Justify briefly.

There's always a reason to check, as there is that "magical point/threshold", where the magic starts to work perfectly fine, as it should. How am I supposed to know it won't work this time? As a general rule of thumb, I shouldn't make any assumptions, before I test something - it's a good practice and a way to spend some more time doing work, but also reaping the results and avoiding bullshit based on bias.

#finish 13:26

---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
