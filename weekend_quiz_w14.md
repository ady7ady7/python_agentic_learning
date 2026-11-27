# Weekend Quiz - Week 14

No notes, no running code. 2-4 sentences per answer is enough.

---

**Q1.** `mlflow.sklearn.log_model(model, name='xauusd_range_multiplier')` - does this create a new
version of the registered model `xauusd_range_multiplier`? What does `name` mean here, and which
call actually creates a version?



**Q2.** You wrote `register_model(f'runs/{run_id}/model', NAME)` (no colon). It didn't crash. What
happened, and how would you notice in the UI?



**Q3.** The whole registered model got deleted in the UI, champion included. The production run
still exists. List the steps to bring the champion back. Why is it possible at all?



**Q4.** Champion MAE 0.3020, challenger MAE 0.3016, both on the same 281 fair rows, period-to-period
noise about 0.023. What does `should_promote(..., margin=0.02)` return, and why is that the right
answer?



**Q5.** Why does `retrain.py` log a run even when the challenger loses?



**Q6.** `log_metrics({'test_mae': 0.30, 'first_date': '2025-06-17'})` crashes. Why, and where does
`first_date` belong instead?



**Q7.** `def get_history(symbol, start, end=dt.date.today())` - the function runs inside a server
that has been up since Monday. On Thursday you call `get_history('XAU/USD', '2026-11-20')`.
Which `end` does it use, and what's the fix?



**Q8.** You compare two data feeds and the 8:15-9:00 power differs by about 0.2 in log terms. Is
that "small"? What do you compare it against to decide?
