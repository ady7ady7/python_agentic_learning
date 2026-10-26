# Weekend Quiz - Week 9

No notes, no running code. Answer from memory. Same transfer-question format as recent
weeks - judging whether an approach generalizes to a new scenario, not recall of what
happened.

---

## Part A - Structural leakage (Day 1's real finding)

#Start 11:34

**A1.** You're predicting next-week revenue for a store. One of your features is "average
daily foot traffic THIS week," and your target is "total revenue THIS week." A colleague
says "that's fine, foot traffic this week is available before we know this week's revenue."
Using Day 1's distinction, explain what's actually wrong here and why "available before the
target" isn't the same as "safe to use."

WTF - it's actually a form of data leakage, as week revenue depends on foot traffic, yet you can't have the FULL foot traffic BEFORE the week ends, so it doesn't make sense. You can only make predicitons with data you have available, and this wouldn't be realistic.


**A2.** New scenario: you're predicting whether a patient's recovery will be "fast" or
"slow," and one feature is "doctor's initial severity rating," recorded at the SAME visit
where the recovery-speed label was later assigned by the same doctor based on that visit.
Is this the same leakage mechanism as Day 1's, a different one, or not a leak at all?
Justify your answer.


This is basically a doctor's subjective opinion on patient's health in two forms. Plus we'd have to assume that doctor's opinions are always unbiased and basically perfect - it doesn't make sense. The severity should always be rated on unarbitrary, quantitative metrics that are unaffected by anyone's opinion. I assume we'd have some thresholds for what 'fast' and 'slow' means in quantitative sense, as right now it's put in a very weird way. Anyway, I wouldn't trust that, as people have their biases and their judgment can vary depending on many factors. Perhaps I'm wrong and we should test it before criticizing, but that's my initial, intuitive approach.

---

## Part B - Window design (Day 2-4's core theme)

**B1.** You're told to predict tomorrow's weather using today's weather, with "a few hours"
gap between the data you observe and what you're predicting. A colleague suggests just
picking round numbers (observe 9am-12pm, predict 3pm-6pm) "because round numbers are easier
to code." What's the actual principled alternative this month's project used instead, and
why does it matter for whether the result means anything real?

I'd put dollars against peanuts that a professional wouldn't suggest that, as that's just dumb XD. Quite frankly, as for prediction windows, I'd simply test different alternatives, yet it probably makes sense to check one window after another (e.g. 3 hours as an observation window and then the next 3 hours as the target), but I'm totally sure that there are different phenomena around the globe that would use entirely different windows, and some even could have breaks between them and the predictions would be more effective (it's possible). Yet, it's all a matter of testing and I wouldn't reject that scenario just by looking at it from now.



**B2.** New scenario: you're asked to predict a website's server load in the next hour
based on the last 10 minutes of traffic. Based on what this month found about SHORT vs LONG
gaps between observation and prediction windows, would you expect this to be an easier or
harder prediction problem than one with a 3-hour gap, and why?

Your assumption again is based on a naive thought that gaps between windows work hte same in every single situation and context. I have no fucking idea quite frankly, and it would probably also depend. It makes sense to expect higher traffic at certain situations, yet this is a very specific question at an unexplored problem. My normal expectation would be it would be harder to predict something with a 3-hour gap, as maybe the website load is somewhat autocorrelated (especially in some contexts high load could slow down the website or make it crash, so that some people would have to wait and the high load would continue, but it's a naive scenario that is not guaranteed to happen.), but we really have to explore something to make such assumptions imo.


**B3.** Day 3 found that going from 2 features to ~10 features did NOT improve the result -
it slightly diluted it. A colleague says "that proves more features always hurts." What's
wrong with that generalization, based on what the feature_importances_ table actually
showed?

Nah, if we had many GREAT features with great effect strength, it would certainly improve the predictions. Yet, we had only few (1 was exceptionally strong) that gave cool results. I guess it's a matter of exploring a given topic from every angle and maybe you'd be able to find more features that were great and were not an effect of noise etc.

---

## Part C - Reading regression results correctly

**C1.** New scenario: you compare two models on two different targets. Model A gets test
R²=0.60 on Target A. Model B gets test R²=0.25 on Target B. A colleague says "Model A is
clearly better - it explains more variance." What question would you ask BEFORE agreeing,
based on Day 3's correction about R² and target variance?

I'd check whether we're not leaking data somewhere, and I'd also compare the train R2 in both cases + maybe look at more metrics like MAE.

**C2.** You fit a regression and get: train MAE=0.25, test MAE=0.30, train R²=0.70, test
R²=0.35. Is this gap pattern (train better than test on both metrics) something to worry
about, panic about, or expect? How does this differ from the inverted pattern (test better
than train) seen with the leaked classifier earlier this project?

Higher test MAE is a bit alarming,- it's not that big, yet I'd still check if there's no leakage. However, the train R2 s much higher than test R2; I'm actually doubting this would be a real scenario, as in most cases both metrics show the same pattern (here it's contradicting) yet I'd check for leaks for sure.

---

## Part D - MLflow and production thinking (Day 5)

**D1.** A colleague says "we already write results in markdown files after every session,
so MLflow doesn't add anything new." Based on what Day 5 actually showed had NO value in a
single logged run, and what DID show value, explain where you'd push back on this claim and
where you'd actually agree with it.

MLflow adds a lot - I've watched a guide about it after we've finished the session - it basically allows to hold and save different experiment results, save different models and version them, so you could have test vs production model, and basically many many other features, with model wrapping and implementation as one of the core functionalities. You can basically wrap your model and make it work outside of your Jupyter, link it with some industry tools or infrastructure like dedicated GUI/web/Spark/Databricks etc., and basically make somebody who doesn't understand the model use it and get useful results



**D2.** New scenario: a colleague trains a model in a Jupyter notebook, gets a good result,
and says "great, it's done, we can use it in production whenever we need it." What's
missing from "the model exists and works in my notebook" that Day 5's `load_model`/
`predict` round-trip was specifically there to prove?


I've kinda explained it above - Well, you could use a model in Jupyter, train it every time and run the whole data preparation loop etc., but it's frantic and pointless. Instead you could wrap the TRAINED model, so you don't have to train it every single time (especially if your datasets are huge), and simply run it elsewhere (like through API request) and feed it with just a single row of data it needs, which makes things MUCH MUCH smoother and easier to use.


**D3.** Your `predict_volatility(model, observation_features: dict) -> float` function was
deliberately NOT written as `predict_volatility(model, dataframe_row)`. Why does a `dict in,
float out` shape matter more once you imagine a FastAPI endpoint calling this function than
it would inside your own notebook?


I didn't use FastAPI yet, so this question is a bit weird, yet I remember you saying that it could crash on DF rows, so this is a decision dictated by infrastructure and experience

---

**11 questions total.** Answer in the same file, under each question, then let me know when
done.
