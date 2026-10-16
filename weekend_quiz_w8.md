# Weekend Quiz - Week 8

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.

---

## Part A - Research-grounded feature engineering

**A1.** You find a strong single feature (like `realized_power` this week) and want to
build 5-10 variants/companions of it based on literature. A colleague says "just try random
combinations and see which ones work." What's the risk in that approach versus what you
actually did this week, and why does it matter even if both approaches might find the same
"winning" features?

**A2.** New scenario: you screen 15 candidate features with Mann-Whitney + Cohen's d against
a target with only 4 features currently in your model. Two features come back with p>0.1.
Should you drop them before modeling? What changes about your answer if you had 150
candidate features instead of 15?

---

## Part B - Overfitting discipline, applied correctly

**B1.** You tune a RandomForest with `RandomizedSearchCV` and get train AUC=0.56, test
AUC=0.54 - a small, healthy-looking gap. A colleague says "great, no overfitting, ship it."
What does the SMALL gap actually tell you, and what does it NOT tell you about whether the
model is useful?

**B2.** New scenario: you tune a model and get train AUC=0.60, test AUC=0.78 - test is
HIGHER than train. A colleague says "even better than we hoped!" What's your immediate
reaction, and why is this pattern often more suspicious than the reverse (train >> test)?

---

## Part C - The realized_power leak (this week's real mistake)

**C1.** You build a target: "does feature X rise in the next 20 bars compared to now?" You
then include X itself as a feature in your model, along with two other features that are
mathematically derived from X (like a ratio of X at two different windows). Explain in
plain words why this is a leak, even though X's value at the CURRENT bar is technically
"available" at prediction time (not future information in the usual sense).

**C2.** How is this leak similar to, and different from, `same_candle_pullback` (the
earlier project's leak, where a feature was structurally impossible for one target class)?
Name the one key difference in mechanism.

**C3.** A colleague says "if a feature causes a leak, just remove that one feature and
you're done." Based on this week, why might that not be enough - what else needs checking?

---

## Part D - Judgement

**D1.** After a full week of disciplined feature engineering, a target (direction/
continuation) that looked promising turns out to be fundamentally unpredictable from your
feature set, confirmed with zero overfitting and proper tuning. A colleague says "the whole
week was wasted - nothing to show for it." What would you say back, concretely?

**D2.** You pivot from predicting direction to predicting volatility, reasoning that
volatility clustering is a more established phenomenon in the literature than return
predictability. Is this a sound methodological move, or is it "shopping for a target until
something works" (the same risk as shopping for features)? What's the actual difference
between the two, if any?

---

**8 questions total.** Answer in the same file, under each question, then let me know when
done.
