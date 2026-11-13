# Weekend Quiz - Week 11

No notes, no running code. Answer from memory. Transfer questions - new scenarios, same
ideas as this week's benchmark arc.

---

## Part A - Measuring a model honestly

**A1.** A colleague shows you a model for daily ad clicks with test MAE = 120 clicks and says
"that's good". What ONE extra number do you need before you can judge it, how do you compute
it, and what would "skill = 0.05" tell you?


I'd actually need to see some kind of baseline for comparison basically to see, if it makes sense. Perhaps it would be wise to also compare iwth other types of models to see how they perform. Skill = 0.05 tells me it removes just 5% of the error from a naive baseline, which doesn't seem like a super amazing model at first sight.



**A2.** A random forest gives a feature an impurity importance of 0.02 (out of 1.00). Your
teammate wants to delete it. Name the two checks from this week that test whether a feature
is really useless, and say what each one actually measures (in what units).

Even if it's only 0.02 importance, we have to remember that it still might be useful and give some advantage over not having it, so I wouldn't opt for deleting it just like that.

We should use permutation importatnce + ablation. THe first one checks how features perform when their order is shifted, and it gives more honest results as for importance in general. Ablation shows how the features set performs without this feature, and we can check all features like that and simply compare the results. If they are worse, it would obviously be a good reason to delete the feature. If not, and even if the improvement is minor/marginal, but it is there I'd still consider keeping the feature. That really depends.



**A3.** Model A: train MAE 0.22, test MAE 0.34. Model B: train MAE 0.33, test MAE 0.31.
Which one do you ship and why? What is happening with A?

A seems more reasonable - perhaps the overfitting issue could be improved a bit, yet in B the test result is BETTER than the actual train result, which might suggest some kind of data leakage or underfitting of some sort. This is a bit weird, but A gives a standard train-test MAE gap and it feels just like an honest model. B's result is suspicious and it suggests that something could be done wrong there and it needs checks.


---

## Part B - Building features without cheating

**B1.** You build "average sales over the last 7 days" with `sales.rolling(7).mean()` and
use it to predict today's sales. What's wrong, and what is the one-word fix?

That's a prime example of data leakage, as that result includes the current day. One should use .shift(1) to avoid that and only count all the days before that day, to avoid using information that wouldn't normally be available to us.



**B2.** You add a 30-day lag feature, run `.dropna()`, split 80/20 again, and the new model
beats yesterday's MAE by 0.01. Why can't you claim the new feature caused that improvement
yet? What row must be in the same table?


The split takes away some rows and the 30-day lag feature calculations are now false compared to the real data. It changes the calculation maths basically.



---

## Part C - Trusting the data

**C1.** You get an hourly electricity-usage file labelled "Europe/Warsaw time". Without
asking anyone, how could you check from the data itself whether the timestamps are really
local time? (Hint: what happens at a known moment every day / every year?)


We can compare that with DST and check how these hours change with that - it gives a clear indication whether it works as we intended.



**C2.** Your macro-release flags showed "no effect at all" on gold volatility. Name two
possible explanations - one about the market, one about your data - and how you'd tell
them apart.



1. There is no real effect of macro-release on volatility - that's one possibility
2. We've measured data in a wrong way - there's always a risk of that and one could be comparing times with DST to check if there are any discrepancies. In this case, one could also do a simply hourly volatility check on macro-release days to see if there aren't any hours with increased volatility, and whether we didn't take wrong hour for our calculations.