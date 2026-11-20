# Weekend Quiz - Week 13

No notes, no running code. 2-4 sentences per answer is enough.

---

**Q1.** Production loads `models:/xauusd_range_multiplier@champion`. You train a better
model on Monday. List the steps to put it live. Which file in the code do you edit?



**Q2.** On Tuesday the new model turns out bad. How do you go back to the old one, and how
long does it take?



**Q3.** In your own words: what's the difference between a run and a registered model
version? Why don't we just load runs directly in production?



**Q4.** A table has a column `har_m` (average of the last 22 days, so the first 22 rows are
NaN) that the model doesn't use. You call `table.dropna()`. What happens to your data, and
what should you write instead?



**Q5.** You compare a new model with the old one. The new one is tested on rows from
2025-06-11, the old one on rows from 2025-06-17. Why is this comparison worthless, even if
the new model's MAE is lower?



**Q6.** Why did we split `train_and_evaluate` into `split_table` + `score`, instead of
keeping one function that does everything?



**Q7.** `sizes = pd.Series(['2', '5', '1'])`. What does `sizes.sum()` return, and what type is
it? What is the fix?
