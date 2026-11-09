# Weekend Quiz - Week 11

No notes, no running code. Answer from memory. Transfer questions - new scenarios, same
ideas as this week's benchmark arc.

---

## Part A - Measuring a model honestly

**A1.** A colleague shows you a model for daily ad clicks with test MAE = 120 clicks and says
"that's good". What ONE extra number do you need before you can judge it, how do you compute
it, and what would "skill = 0.05" tell you?



**A2.** A random forest gives a feature an impurity importance of 0.02 (out of 1.00). Your
teammate wants to delete it. Name the two checks from this week that test whether a feature
is really useless, and say what each one actually measures (in what units).



**A3.** Model A: train MAE 0.22, test MAE 0.34. Model B: train MAE 0.33, test MAE 0.31.
Which one do you ship and why? What is happening with A?



---

## Part B - Building features without cheating

**B1.** You build "average sales over the last 7 days" with `sales.rolling(7).mean()` and
use it to predict today's sales. What's wrong, and what is the one-word fix?



**B2.** You add a 30-day lag feature, run `.dropna()`, split 80/20 again, and the new model
beats yesterday's MAE by 0.01. Why can't you claim the new feature caused that improvement
yet? What row must be in the same table?



---

## Part C - Trusting the data

**C1.** You get an hourly electricity-usage file labelled "Europe/Warsaw time". Without
asking anyone, how could you check from the data itself whether the timestamps are really
local time? (Hint: what happens at a known moment every day / every year?)



**C2.** Your macro-release flags showed "no effect at all" on gold volatility. Name two
possible explanations - one about the market, one about your data - and how you'd tell
them apart.
