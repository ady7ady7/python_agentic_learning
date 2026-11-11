# Tasks - Interview Prep Day 1 - "Walk me through a Python script that pulls data from a REST API"

**Time:** ~50 min, evening session. One new concept (retry with backoff), the rest is turning
work you already did into an interview answer.

**Why this question first:** it's the one you can answer best - Twelve Data -> features ->
FastAPI -> hourly cron -> database -> frontend, now on Google Cloud Run. The interviewer
will dig into the "production" parts: what happens when the API fails, how it runs without
you, how you know the data is right. Tonight you make sure each of those has a concrete answer.

---

## Warm-up (5 min) - comprehension on API-shaped data

Twelve Data returns bars like this (newest first, prices as strings):

```python
values = [
    {'datetime': '2026-11-10 08:10:00', 'close': '4075.78'},
    {'datetime': '2026-11-10 08:05:00', 'close': '4074.10'},
    {'datetime': '2026-11-10 08:00:00', 'close': '4076.55'},
]
```

- W1 (no-brainer). List of closes as floats: `[4075.78, 4074.10, 4076.55]`.
- W2. ONE dict `{datetime: close_as_float}`. Reminder: outer `{}` + `key: value`, no inner `{}`.
- W3. Same dict, but sorted oldest first - `sorted(values, key=lambda v: v['datetime'])` in the
  `for` part.

---

## Task 1 - Retry with backoff in `get_recent_bars` (20 min)

**Concept - which failures are worth retrying.** An API call can fail in two kinds of ways:

- **Temporary** - the server is busy or the network blinked: HTTP 429 (too many requests),
  500/502/503/504 (server-side trouble), timeouts, connection errors. Trying again a bit later
  often works. This is exactly what hit your Worker this week (429 from in front of Render).
- **Permanent** - your request is wrong: 400 (bad parameters), 401/403 (bad key). Retrying
  just repeats the same error, so fail at once with a clear message.

**Backoff** = wait longer after each failed attempt (2 s, 4 s, 8 s...), so you don't hammer a
server that's already struggling. "Exponential" = the wait doubles each time.

```python
import time
import requests

RETRYABLE = {429, 500, 502, 503, 504}

def get_with_retry(url, params, max_attempts=4):
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, params=params, timeout=10)  # timeout: never hang forever
        except (requests.ConnectionError, requests.Timeout) as e:
            if attempt == max_attempts:
                raise RuntimeError(f'Network error after {max_attempts} attempts: {e}')
        else:
            if response.status_code not in RETRYABLE:
                return response                     # success, or a permanent error - caller decides
            if attempt == max_attempts:
                return response                     # out of attempts, hand back the last answer
        time.sleep(2 ** attempt)                    # 2, 4, 8 s
```

Read it step by step before using it:
- `try / except / else`: `except` runs when `requests.get` raised (no response at all),
  `else` runs when it didn't (we got a response, maybe an error code).
- `2 ** attempt` - 2 to the power of the attempt number: 2, 4, 8 seconds.

- 1a. In this repo's `live_data.py`, make `get_recent_bars` use it (keep your existing checks -
  `status_code != 200` and `status == 'error'` - they now run on the response it returns).
- 1b. Test the permanent path: call it with a wrong API key. It must fail at once (no waiting).
- 1c. **In a comment, one sentence each:** why is 401 not retried, and why is 429 retried?

Twelve Data detail worth knowing: when you hit their limit they often reply with HTTP 200
and `{"status": "error", "code": 429}` in the body - so your `status == 'error'` check is the
one that catches it, not the status code. (Retrying that case is optional.)



import requests
import os
from dotenv import load_dotenv
import pandas as pd
import time

retried = {429, 500, 502, 503, 504}
API_KEY = os.getenv('TWELVEDATA_API_KEY')

def get_candle_data(url, params, max_attempts = 4):
  '''
  Function used to fetch candle data with HTTP request
  '''
  load_dotenv()
  for attempt in range(1, max_attempts + 1):
    try:
      response = requests.get(
        url = url,
        params = {
          **params,
          'apikey': API_KEY}
      , timeout = 10)
      if attempt == max_attempts:
        print(f'Max attempts reached, data fetch failed')
        break
    except response.status_code not in (retried):
      print(f'Request error {response.status_code}: {response.reason}')
      break
    except response.status_code in retried:
      time.sleep(2 ** attempt)
    else:
      data = response.json()
      data = pd.DataFrame(data['values'])
      return data
      
  
  
  
xd = get_candle_data(url = 'https://api.twelvedata.com/time_series',
                     params = {
                       'symbol': 'AAPL',
                       'interval': '5min'
                     })
print(xd)










---

## Task 2 - Your answer, in English, in `interview_prep.md` (25 min)

Write it as **STAR** (Situation, Task, Action, Result), ~2 minutes spoken (~250 words). Use
your own words - I'll polish the English after, not the content.

- **S:** what you wanted (hourly gold volatility forecast, live, without you running anything)
- **T:** what the script had to do (pull fresh 5-min bars, compute features, predict, store)
- **A:** the concrete things you did - pick 4-5:
  - `requests` to Twelve Data, error checks on status code AND the error field in the JSON
  - sorting (API returns newest first), dropping the still-forming candle, timezone to New York
  - features -> model -> FastAPI endpoint, protected with an API key
  - scheduled: Cloudflare Worker cron every hour at :15, results stored in a D1 database
  - the 429 incident: diagnosed it from logs, added retries, moved the backend to Cloud Run
- **R:** what it does now (runs every hour on its own, stores prediction + what actually
  happened, a public page shows the hit rate)

Then 3 follow-ups they're likely to ask - 2-3 sentences each:
1. "What happens when the API fails?"
2. "How do you know the data is correct?" (hint: you have a great story - the clock bug)
3. "How would you scale this to 100 instruments?" (hint: API rate limits, one call per
   symbol per hour, store raw bars once instead of re-fetching)


S - First I tried to create an ML model for direction prediction, and I tried multiple models, a lot of features and basically I thought I exhausted all possibilities with no effects at all, as the effects were close to a coin flip. I tested volatility target instead and it turned out to be much more predictable, and the research confirmed that, so I moved into volatility prediction target instead. After weeks of testing different features I finally created a model that seemed to be viable, but my main goal was to implement it in production, so that it would create predictions live.

T - It needs to fetch live market data and work in the same way as my ML tests, but in live environment. So fetched data needs to be prepared and the features need to be calculated - it needs the same amount of data as there was used for calculations during the training so the effects are the same. We need to handle timezones and stuff like that, so everything works in the same way, replicated from the ML model. The calls need to be automated, so that we only see the results and use them, and also every non-technical person could use these.


A - First, I needed to wrap the model with MLflow first, so that it could be used anywhere without retraining it every single time in my Jupyter Notebook - MLflow allows that, and it allowed me to save the model in mlruns folder - every model has its path and mlflow wraps it in a way that's replicable eveyrwhere. I don't know the details, not sure I know them. I know it allows for versioning and experiments as well.

Then I had to prepare an endpoint iwth FastAPI (Claude helped with that, as I don't see a reason to memorise everything by heart). What it does, is that after it's called, it sends a request for data from Twelvedata's API(using the API Key provided in .env), it gets data and transforms it, prepares features and final data structure following my functions, and then sends the prepared features data to the ML model in backend and gets the prediction(s). The predictions are then sent back, saved in a DB on backend and shown in frontend.

The requests are automated with a cron job hosted on Cloudflare worker, as backend in Render had issues with accepting Cloudflare requests, and Cloudflare worker sends sends the requests to the backend (currently in Google Cloud Run) and gets the results back to the frontend

R - It works every hour within a specified window (Mon-Fri, 3:15 ET - 15:15 ET), the requests are sent from Cloudflare worker to the backend, and then shown on the frontend, also saved on local backend DB so that we will get more data to analyze, as I can easily say this is an experiment.


1. Since I'm observing the site, I'm monitoring how it works. If it fails, our data doesn't get deleted or anything, the frontend should still be running, but obviously we can the logs in few places:
- Cloudflare worker, as there could be issues with Cloudflare - backend communication - this already happened before and it seemed like Render backedn was blocking CLoudflare's IP addresses, as reqeusts from my PC reached their destination without any issues
- backend failed requests - for whatever reason, Twelvedata could restrict our requests - if we corssed the rate limits or whatever - that shouldn't happen as I'm way below the daily 800 requests and 8 requests per minute, and I obiously took it into account when creating this pipeline

I have the logs, and I would act accordingly - I already had to move the backend to Google Cloud.

- I've tested data, as I've used my Jupyter Notebook first and basically run this whole pipeline on my own and I had to check how the data looks like to design how features are calculated next. If nothing changes, everything should be correct. But obviously we could add checks and standard try-except blocks for the features itself.

If I'm expecting the features to range in a certain window, I could filter these out in pandas or whatever.
By design I'm calling the API after a given threshold, after the candle is closed, so it should be finished. I cannot predict everything, but I think I'm prepared quite well and the results show that, as ihe inner band held the hour's full range in 61% of 44 scored hours, the outer band in 84%, and it was with the worse RF model - now I'm using LinearRegression, which is a lot better.


- First of all, we could simply buy the paid API, as I'm using a free tier. With that, there wouldn't be a problem with calling this as many times as we'd like. Every other symbol could have a separate page on the frontend, with a separate endpoint - that wouldn't change much, the requests would probably need just a tiny symbol change in every case, at least withg the current approch.

If needed, we could use our own stored data.



---

**Total: warm-up + 2 tasks, ~50 min.** Next sessions: SQL on a columnar database (BigQuery,
with your NQ data), then automating a data feed into a BI dashboard, then the ad tech question
and a mock interview.
