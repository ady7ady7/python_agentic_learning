# Weekend Quiz - Week 8

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.


#Start 13:28

---

## Part A - Research-grounded feature engineering

**A1.** You find a strong single feature (like `realized_power` this week) and want to
build 5-10 variants/companions of it based on literature. A colleague says "just try random
combinations and see which ones work." What's the risk in that approach versus what you
actually did this week, and why does it matter even if both approaches might find the same
"winning" features?


WDYM - random combinations, like totally random features or what? Literature-based approach generally allows us to quickly check whether there are already explored directions, which can save us a lot of time - it makes sense to use what humanity already developed and maybe build on it, rather than randomly look for some b, as it can take much longer, especially that I'm not a PhD in maths/statistics. While surely I guess that we'll have to explore and think to develop features for the most effective models, as nothing really valuable is published, or what was really valuable was published and exhausted over time, checking out research papers and literature makes a lot of sense to see what potential directions or approaches we could take or dig in.


**A2.** New scenario: you screen 15 candidate features with Mann-Whitney + Cohen's d against
a target with only 4 features currently in your model. Two features come back with p>0.1.
Should you drop them before modeling? What changes about your answer if you had 150
candidate features instead of 15?


I wouldn't be so sure about dropping these features, as they can have real effect when combined with another feature or a set of features - you never know. It's a preliminary check + effect's strenght check, but it isn't 1:1 as decisive as modeling and checking how it really works.


---

## Part B - Overfitting discipline, applied correctly

**B1.** You tune a RandomForest with `RandomizedSearchCV` and get train AUC=0.56, test
AUC=0.54 - a small, healthy-looking gap. A colleague says "great, no overfitting, ship it."
What does the SMALL gap actually tell you, and what does it NOT tell you about whether the
model is useful?

It shows me how well we've done the procedure - there's no big difference between the effects of model working on train vs test data, which is a living proof that I've properly prepared data and trained the model. Also, still it doesn't mean the model is strong and/or worth using - and here it's not, as 0.56/0.54 AUC is mostly a coinflip +4-6pp (MIGHT BE USEFUL in some cases, maybe it's not entirely useless, I guess it depends on the context).



**B2.** New scenario: you tune a model and get train AUC=0.60, test AUC=0.78 - test is
HIGHER than train. A colleague says "even better than we hoped!" What's your immediate
reaction, and why is this pattern often more suspicious than the reverse (train >> test)?

It suggests we might have data leakage, and perhaps model is good at predicting the target as it receives the target in a different form, or some target-made proxy etc. I'd check that, as it's definitely suspicious.


---

## Part C - The realized_power leak (this week's real mistake)

**C1.** You build a target: "does feature X rise in the next 20 bars compared to now?" You
then include X itself as a feature in your model, along with two other features that are
mathematically derived from X (like a ratio of X at two different windows). Explain in
plain words why this is a leak, even though X's value at the CURRENT bar is technically
"available" at prediction time (not future information in the usual sense).

It's a leak if the target itself was used to calculate that particular value or if you used values that aren't normally available, it's as simple as that.


**C2.** How is this leak similar to, and different from, `same_candle_pullback` (the
earlier project's leak, where a feature was structurally impossible for one target class)?
Name the one key difference in mechanism.

Well, similar in a sense that it affects the final verdict and normally you wouldn't be able to use that information. E.g. if it's a same candle pullback, you can't decide if it actually is a same candle pullback BEFORE the candle closes - so you can't play it, even if it was XD. It doesn't make sense to use normally.

And here it's a different form of a leak, where you use numbers that direct contain information about target and calculate other numbers from them - you basically use data you wouldn't normally have available.


**C3.** A colleague says "if a feature causes a leak, just remove that one feature and
you're done." Based on this week, why might that not be enough - what else needs checking?

Provided we remove all forms of leak, it should work - one just have to make sure, if that's the case. And here we've used similar data to calculate few features, so more careful checks are needed. WE must make sure that we only use data that would normally be available to us, as otherwise it doesn't make any sense.



---

## Part D - Judgement

**D1.** After a full week of disciplined feature engineering, a target (direction/
continuation) that looked promising turns out to be fundamentally unpredictable from your
feature set, confirmed with zero overfitting and proper tuning. A colleague says "the whole
week was wasted - nothing to show for it." What would you say back, concretely?



Nah, that's bullshit, as it's a learning process and useful examples to deal with data leakage/overfitting, I'd say it was useful MLOps from the model creation, feature engineering POV.


**D2.** You pivot from predicting direction to predicting volatility, reasoning that
volatility clustering is a more established phenomenon in the literature than return
predictability. Is this a sound methodological move, or is it "shopping for a target until
something works" (the same risk as shopping for features)? What's the actual difference
between the two, if any?


It makes sense to follow a direction which seems to be more promising and has research-proven success rate, and it was done after actually failing with return predictability measured from two different angles.


Finish 13:42
---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
