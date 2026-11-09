# Tasks - ML Phase Week 12 Day 2 - swap the production model

**Time:** ~45 min. No new theory - plumbing only. Goal: `/predict/live` serves the new
linear model (8 features, correct ET clock) with the new range constants.

**Facts you need:**
- New MLflow run: `d068c9f054b04563b8c0e8765ffef091` (`w12d1_linreg_final_v2`; the other run
  with the same name, `56c6...`, is an earlier duplicate)
- `k_p75 = 2138.64`, `k_p90 = 3063.55` (old: 2079.53 / 2961.72)
- Model features, exact names:
  `log_power_obs, log_atr14_obs, center_of_mass_mean_observation, log_parkinson_obs,
  log_har_d, is_cpi, is_nfp, is_thursday`
- `macro_releases.csv` now has NFP/CPI dates to Dec 2027

---

## Step 1 - `predict_volatility_multiplier.py`
- New `RUN_ID` and k constants.
- In `predict_volatility()`: `row = pd.DataFrame([observation_features])[model.feature_names_in_]`
  - sklearn needs the same column names in the same order as at `fit`; `feature_names_in_` is
  that list, stored in the model. Extra keys in the dict are ignored this way.
- Optional: `RUN_ID = os.getenv('RUN_ID', '<default>')` - future swaps = change a Render env var.

## Step 2 - `live_data.py`
- `outputsize` 100 -> 500 (`log_har_d` needs yesterday's window; on Monday, Friday's).
- Per bar: `parkinson_volatility = np.log(high / low) ** 2 / (4 * np.log(2))`.
  In the observation aggregation: `parkinson_obs = ('parkinson_volatility', 'sum')`.
- Logs: `log_power_obs`, `log_atr14_obs`, `log_parkinson_obs`.
- `log_har_d`: rows with `hour == current_hour`, `minute >= 15`, `trade_date < current_date`;
  `prev_date` = max of their `trade_date`; log of the sum of `abs_ret_1bar` on `prev_date`.
- Flags: `is_nfp` / `is_cpi` = today in the CSV dates, `is_thursday` = `weekday() == 3` -
  all three ONLY when `current_hour == 8` (releases are at 8:30; the model learned them for
  the 8:15-9:00 window), otherwise 0.
- Keep `realized_power_observation` in the returned dict - `api.py` needs it.

## Step 3 - `api.py`
- `ObservationFeatures` (POST `/predict`) -> the 8 new fields.

## Step 4 - test
- `uvicorn api:app --reload`, open `/predict/live`. No NaN / inf, range in a sane number of points.

## Step 5 - deploy repo / Render
- Copy code + `macro_releases.csv` + `mlflow.db` + `mlruns/`, redeploy.
