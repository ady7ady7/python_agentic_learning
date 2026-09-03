# Tasks - ML Phase Week 2 Day 4

**Time:** target 60-75 min.

This week's goal was to answer your own question from week 1: "if we could identify Q5
earlier, we'd have good predictive power." You now have quantile regression, and you have
proven with walk-forward testing that its coverage holds up over time, not just on one
lucky split.

Today you turn that into something usable - a small function that takes today's morning
data and gives back three numbers you could actually act on. No new statistics today,
just packaging what you already built.

---

## Warm-up - walk-forward loop from memory (5 min)

Write the skeleton from memory, not the fitted numbers - just the shape:

> You have `train_size` and `test_size`. Starting from `start = train_size`, in a loop:
> slice out a training window ending at `start`, slice out a test window beginning at
> `start`, fit a model on the training window, predict on the test window, record the
> result, then move `start` forward by `test_size`. Stop when there is no room left for a
> full test window.

Write it as actual code, `while` loop and all. Not scored - the point is checking whether
the shape of walk-forward has stuck, separately from remembering what QuantileRegressor
does.

#Start 12:06


train_size = 300
test_size = 300

features = ['X', 'Y', 'Z']
results = []

start = train_size
while start + test_size <= len(df):
     train = df.iloc[start - train_size : start]
     test = df.iloc[start : start + test_size]

     model = QuantileRegressor(quantile = 0.8, alpha = 0, solver = 'highs')
     model.fit(train[features], train['desired_target'])
     pred = model.predict(test[features])

     results.append(
          {
          'train_start': train.index.min(),
          'prediction' pred
          }
     )
     start += train_size

results = pd.Dataframe(results)

---

## Task 1 - Refit on the full dataset (15 min)

Every model this week was trained on some window and tested on a later one - which means
none of them has ever seen the most recent data. Before building something usable, that
changes.

**What we are predicting:** `us_range` - the high minus low of the US session
(10:00-16:00 ET), in points, at the moment the US session opens (10:00 ET). Features come
from this morning's EU session (03:00-09:55 ET) and from previous days - nothing from the
US session itself, since it has not happened yet at prediction time.

**Features:**

```python
features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
```

- 1a. Fit three `QuantileRegressor` models (quantile 0.5, 0.8, 0.9, `alpha=0`,
     `solver='highs'`) on your **entire** dataframe - no train/test split this time.
- 1b. This is a different thing from what you have done all week, so name it in a comment:
     what can this final model tell you that a train/test split cannot, and what can it
     **not** tell you that a train/test split could? (You already have the answer to the
     second half from Monday to Wednesday.)



from sklearn.linear_model import QuantileRegressor

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']
quantiles = [50, 80, 90]
filtered_df = df[features]


#first approach, I kinda wanted to use classes here as I thought it could be appropriate and I idn't use OOP for a long time, but it's just for testing purpsoes 
class QuantileModel():
    def __init__(self, model_name, quantile):
        self.name = model_name
        self.quantile_parameter = quantile
        self.model = None
        self.predictions = []

    def create_model(self):
        self.model = QuantileRegressor(quantile = self.quantile_parameter, alpha = 0, solver = 'highs')
    
    def train_model(self, train_x, train_target):
        self.model.fit(train_x, train_target)
    
    def model_predict(self, test_x):
        pred = self.model.predict(test_x)
        self.predictions.append(pred)
        return self.predictions
    

for q in quantiles:
    q_parameter = q / 100
    model_name = f'q{q}_model'
    model = QuantileModel(model_name, q_parameter)
    model.create_model()
    model.train_model(filtered_df, df['us_range'])
    pred = model.model_predict(filtered_df)
    
    print(pred)
    
#in this case training the models only takes 6 lines, so perhaps it's more practical :D
q50_model = QuantileRegressor(quantile = 0.5, alpha = 0, solver = 'highs')
q50_model.fit(filtered_df, df['us_range'])

q80_model = QuantileRegressor(quantile = 0.8, alpha = 0, solver = 'highs')
q80_model.fit(filtered_df, df['us_range'])

q90_model = QuantileRegressor(quantile = 0.9, alpha = 0, solver = 'highs')
q90_model.fit(filtered_df, df['us_range'])
    
    
    

Frankly I'm unsure what's the point.
I mean, yeah, we could do the testing beforehand using train-test splits to get the idea how the model works, AND THEN retrain the model on the whole dataset, as we already know what to expect, to predict new data. Is that the logic behind it?

We obviously can't test it as we don't have more data, but if we assume it gets the results as in the past, then we've already tested it.




---

## Task 2 - A function that returns three numbers (25 min)

Wrap the three fitted models into one function.

```python
def forecast_range(today_features, q50_model, q80_model, q90_model):
    """
    today_features: a single row of feature values (one day), same columns as
                     used for training - shape (1, 6), not a plain list.
    Returns a dict with the three quantile predictions.
    """
    return {
        'q50': q50_model.predict(today_features)[0],
        'q80': q80_model.predict(today_features)[0],
        'q90': q90_model.predict(today_features)[0],
    }
```

The `[0]` matters: `.predict()` always returns an array, even for one row, so you pull out
the single number inside it.

- 2a. Take the **last row** of your dataframe (today's actual morning data) and pass its
     features through the function. `X.iloc[[-1]]` gets you the last row **as a DataFrame**
     (not a Series) - the double brackets are what keep the two-dimensional shape the model
     expects.
- 2b. Print the three numbers next to the actual `us_range` that happened that day.
- 2c. Also run the function on 5 other random days from your data and build a small table:
     date, actual, q50, q80, q90.

**In a comment:** for those 5 days, how many times did the actual value exceed q80? Roughly
what would you expect, and does it match?


#The task took a bit longer than expected, as I had to import the latest data :)).
For that reason I first did a mock test with some random numbers, as the data was importing, to not waste time.



def forecast_range(today_features, q50_model, q80_model, q90_model):
    """
    today_features: a single row of feature values (one day), same columns as
                     used for training - shape (1, 6), not a plain list.
    Returns a dict with the three quantile predictions.
    """
    return {
        'q50': q50_model.predict(today_features)[0],
        'q80': q80_model.predict(today_features)[0],
        'q90': q90_model.predict(today_features)[0],
    }
    

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']

today_features = [[30, 5, 42, 24, 66, 1.3]]
xd = forecast_range(today_features, q50_model, q80_model, q90_model)

#first test with simple randomly added numbers, then I reimported the latest market data, and had to adapt the import to the non-SQL structure, went without problems :))
df = pd.read_csv('xauusd_m5_latest.csv')


df['et_time'] = pd.to_datetime(df['timestamp'], unit = 's', utc = True).map(lambda x: x.tz_convert('America/New_York'))
df['trade_date'] = pd.to_datetime(df['et_time']).dt.date

eu_session = df[(df['et_time'].dt.hour >= 3) & (df['et_time'].dt.hour <= 9)]
eu_session['candle_range'] = eu_session['high'] - eu_session['low']
eu_session = eu_session.groupby(['trade_date']).agg(
    eu_open = ('open', 'first'),
    eu_high = ('high', 'max'),
    eu_low = ('low', 'min'),
    eu_close = ('close', 'last'),
    eu_bars = ('et_time', 'count'),
    eu_bar_rng_mean = ('candle_range', 'mean')
).reset_index()
eu_session.head()

us_session = df[(df['et_time'].dt.hour >= 10) & (df['et_time'].dt.hour <= 15)]
us_session['candle_range'] = us_session['high'] - us_session['low']
us_session = us_session.groupby(['trade_date']).agg(
    us_open = ('open', 'first'),
    us_high = ('high', 'max'),
    us_low = ('low', 'min'),
    us_close = ('close', 'last'),
    us_bars = ('et_time', 'count'),
    us_bar_rng_mean = ('candle_range', 'mean')
).reset_index()
us_session.head()

us_session['us_range'] = us_session['us_high'] - us_session['us_low']
eu_session['eu_range'] = eu_session['eu_high'] - eu_session['eu_low']

df = us_session.merge(eu_session, on = 'trade_date')
df = df[(df['us_bars'] >= 0) & (df['eu_bars'] >= 0)]


df['eu_return_pct'] = (df['eu_close'] - df['eu_open']) / df['eu_open'] * 100
df['eu_close_loc'] = (df['eu_close'] - df['eu_low']) / (df['eu_high'] - df['eu_low'])
df['us_atr14'] = df['us_range'].shift(1).rolling(14).mean()
df['eu_atr14'] = df['eu_range'].shift(1).rolling(14).mean()
df['prev_us_range'] = df['us_range'].shift(1)
df['eu_range_norm'] = df['eu_range'] / df['eu_atr14']

df = df.dropna()



def forecast_range(today_features, q50_model, q80_model, q90_model):
    """
    today_features: a single row of feature values (one day), same columns as
                     used for training - shape (1, 6), not a plain list.
    Returns a dict with the three quantile predictions.
    """
    return {
        'q50': q50_model.predict(today_features)[0],
        'q80': q80_model.predict(today_features)[0],
        'q90': q90_model.predict(today_features)[0],
    }
    

features = ['eu_range', 'eu_bar_rng_mean', 'us_atr14',
            'eu_atr14', 'prev_us_range', 'eu_range_norm']

today_features = [[30, 5, 42, 24, 66, 1.3]]
xd = forecast_range(today_features, q50_model, q80_model, q90_model)


import random
results = []
random_list = [random.randint(1, 6) for i in range(5)]
filtered_df = df.iloc[random_list]

for i in range(len(filtered_df)):
    pred = forecast_range(filtered_df[features].iloc[[i]], q50_model, q80_model, q90_model)
    results.append(
    {
    'date': filtered_df['trade_date'].iloc[i],
    'actual': filtered_df['us_range'].iloc[i],
    'q50': pred['q50'],
    'q80': pred['q80'],
    'q90': pred['q90']
    }
    )

final_table = pd.DataFrame(results)
final_table.head()

date	actual	q50	q80	q90
0	2026-09-01	52.83	46.191558	68.728874	88.109602
1	2026-08-31	37.64	41.604968	68.599222	114.191962
2	2026-09-01	52.83	46.191558	68.728874	88.109602
3	2026-08-28	185.63	31.092429	45.761808	64.531458
4	2026-08-31	37.64	41.604968	68.599222	114.191962


---

## Task 3 - One paragraph, plain language (10 min)

No code. Write 4-6 sentences, as if explaining this to someone who trades but has never
heard of quantile regression, answering:

- What does this model actually tell you before the US session opens?
- Why would you use q80 rather than an ordinary "expected range" prediction to size a stop?
- What is this model **not** able to tell you? (You have hit this limit twice this week -
  name it.)


It tells me the us range boundaries that won't be crossed in 50% (1 out of 2 days), 80% (4 out of 5 days) and 90% (9 out of 10 days). By using that it allows me to set a predicted range for the SL that shouldn't be crossed within 4 out of 5 days, if we're using the q80 model prediction. It's better than expected range prediction, as these expected range predictions have errors anyway, and it's a prediction that really stays uncrossed in the expected number of occurences.

It's not able to tell me the exact range the market is going to reach, or the actual direction it;s going to go.


---

**Total: warm-up + 3 tasks.**

This closes the quantile regression topic. Tomorrow is the week wrap-up and the weekend
quiz.
