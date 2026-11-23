# Weekend Quiz - Week 13

No notes, no running code. 2-4 sentences per answer is enough.

---

**Q1.** Production loads `models:/xauusd_range_multiplier@champion`. You train a better
model on Monday. List the steps to put it live. Which file in the code do you edit?


There are multiple options, one is simply giving the new model alias 'champion' through mlflow client:

client = MlflowClient()
client.set_registered_model_alias(NAME, 'champion', model_name)

I could also set a strict model run id in predict_volatility_multiplier, and it would work as well. So I either work in predict_volatility_multiplier, or retrain the model and give the new model the champion label :)).



**Q2.** On Tuesday the new model turns out bad. How do you go back to the old one, and how
long does it take?

It takes a minute, I simply switch the aliases, giving the old one the @champion alias. It's as simple as that.



**Q3.** In your own words: what's the difference between a run and a registered model
version? Why don't we just load runs directly in production?

A run is a test of a given model, which can go both ways, positive or negative, so it isn't the case that there's a point to register every run. We only register models and versions that bring us improvements or interesting results.

Loading models is a lot more convenient as you can simply replace the @champion model every single time and you don't have to change anything else, look for versions etc., especially taht they consist of multiple alphanumerical characters, and could be difficult to memorize. This is simply a way more convenient way to operate - just work with models/experiments on MLFlow, continue tests and only replace the champion model when the challenger really gets better.



**Q4.** A table has a column `har_m` (average of the last 22 days, so the first 22 rows are
NaN) that the model doesn't use. You call `table.dropna()`. What happens to your data, and
what should you write instead?


If we don't use that column at all, it would be wise to do table = table.drop(columns = ['har_m]), way better than deleting 22 rows of our data.



**Q5.** You compare a new model with the old one. The new one is tested on rows from
2025-06-11, the old one on rows from 2025-06-17. Why is this comparison worthless, even if
the new model's MAE is lower?


This is a literal data leakage, it could be big or not, depedning on the total number of rows. In our case, it didn't alter the results much, but it still did. We should only test on data that wasn't previously available to the model. It's unfair and the model would get advantage of that, simple as that.


**Q6.** Why did we split `train_and_evaluate` into `split_table` + `score`, instead of
keeping one function that does everything?


Because sometimes you'd simply want to test an existing model instead of training it, and it's simply more convenient. Sometimes you'd like to split data without trainin it etc. Now we have 3 options that we can easily use, and it isn't complicated at all, neither code wise, nor complicated to understand.



**Q7.** `sizes = pd.Series(['2', '5', '1'])`. What does `sizes.sum()` return, and what type is
it? What is the fix?



251 - it occurs because we're using strings here, and instead of summing the numbers properly, the code sums them as strings, so '2 + 5 + 1' = '251'. A simple fix would be to use astype(float) or float(), or int() here.