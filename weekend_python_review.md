# Weekend Python Review — Core Skills Refresh
**Estimated time: 40–60 minutes**
**Format: Code from scratch, no hints, no looking things up.**
Write all solutions in a single .py file or notebook. Run each task to verify it works.
Assessment happens after you're done — paste your solutions and I'll score + give feedback.

---

## Task 1 — Comprehensions (10 min)

You have a list of trades:

```python
trades = [
    {'symbol': 'AAPL', 'side': 'buy', 'qty': 100, 'price': 182.5},
    {'symbol': 'TSLA', 'side': 'sell', 'qty': 50, 'price': 245.0},
    {'symbol': 'NVDA', 'side': 'buy', 'qty': 200, 'price': 610.0},
    {'symbol': 'AAPL', 'side': 'sell', 'qty': 80, 'price': 190.0},
    {'symbol': 'MSFT', 'side': 'buy', 'qty': 30, 'price': 415.0},
    {'symbol': 'TSLA', 'side': 'buy', 'qty': 120, 'price': 238.0},
]
```

Using comprehensions (no loops), produce:

1a. A list of gross values (`qty * price`) for buy trades only.

1b. A dict mapping each symbol to its total qty traded (both sides combined).
    Expected: `{'AAPL': 180, 'TSLA': 170, 'NVDA': 200, 'MSFT': 30}`

1c. A set of symbols where at least one trade has gross value above 50,000.



gross_values =  [trade['qty'] * trade['price'] for trade in trades]
print(gross_values)


symbol_qty = {trade['symbol'] : (trade['qty'] * trade['price']) for trade in trades}
print(symbol_qty)

high_value_symbols = list(set([trade['symbol'] for trade in trades if trade['qty'] * trade['price'] >= 50000]))
print(high_value_symbols)


---

## Task 2 — Functions + edge cases (10 min)

Write a function `weighted_avg_price(trades, symbol)` that:
- Takes the trades list above and a symbol string
- Returns the weighted average price for that symbol across all trades (weighted by qty)
- Raises a `ValueError` with a descriptive message if the symbol doesn't exist in the list
- Returns a float rounded to 2 decimal places

Example: `weighted_avg_price(trades, 'AAPL')` → `(100*182.5 + 80*190.0) / (100+80)` → `185.83`

Then write a second function `top_n_by_value(trades, n)` that returns the top n trades by gross value as a list of dicts, sorted descending. Handle the case where n exceeds the number of trades gracefully.


from typing import List

def weighted_avg_price(trades: List[dict], symbol: str) -> float:
    filtered_trades = [trade for trade in trades if trade['symbol'] == symbol]
    
    
    vwap_sums = [(trade['price'] * trade['qty']) for trade in filtered_trades]
    vwap_qties = sum([(trade['qty']) for trade in filtered_trades])
    
    vwap = round(sum(vwap_sums) / vwap_qties, 2)
    return vwap




def top_n_by_value(trades: List[dict], n: int):
    try:
    
        sorted_trades = sorted(trades, 
                               key = lambda trade: trade['qty'] * trade['price'],
                               reverse = True)
        return sorted_trades[:n]
    except IndexError:
        print(f'Please make sure your desired n trades is shorter than {len(trades)}')


print(top_n_by_value(trades, 15))


I've added the unexpected exception



---

## Task 3 — Class (15 min)

Write a `Portfolio` class that:

- `__init__` takes an owner name (string) and initialises an empty list of positions
- `add_position(symbol, qty, avg_price)` adds a position dict to the list
- `remove_position(symbol)` removes the position by symbol — raises `KeyError` if not found
- `total_value(current_prices: dict)` takes a dict of `{symbol: current_price}` and returns the total portfolio value as a float
- `__repr__` returns something like `Portfolio(owner='Adrian', positions=3)`
- `__len__` returns the number of positions

Bonus: add a `most_valuable(current_prices)` method that returns the symbol with the highest current value.



class Portfolio():
    
    def __init__(self, owner_name: str):
        self.owner_name = owner_name,
        self.positions_list = []
        
    def __repr__(self):
        return f'Portfolio(owner = {self.owner_name}, positions = {len(self.positions_list)})'
    
    def __len__(self):
        return len(self.positions_list)
        
    def add_position(self, symbol, qty, avg_price):
        '''A method used to add positions'''
        self.positions_list.append({'symbol': symbol, 'qty': qty, 'avg_price': avg_price})
    
    def remove_position(self, symbol):
        '''A method used to remove positions'''
        list_of_positions_to_remove = [position for position in self.positions_list if position['symbol'] == symbol]
        
        try:
            self.positions_list.remove(list_of_positions_to_remove)
        except KeyError as e:
            print(f'There are no positions for {symbol}')
    
    def total_value(self, current_prices: dict):
        '''A method used to calculate the total value of our portfolio, we need a dict of symbol + current_price for that e.g.
        
        {symbol: current_price}
        '''
        total_porfolio_value = sum([position['qty'] * current_prices['current_price'] for position in self.positions_list if position['symbol'] == current_prices['symbol']])
        return total_porfolio_value
        


---

## Task 4 — Generator (10 min)

Write a generator function `drawdown_periods(prices)` that:
- Takes a list of prices (floats)
- Yields the percentage drawdown at each point from the running peak
- Drawdown = `(current - peak) / peak * 100` — will be 0 or negative

Example input: `[100, 105, 102, 98, 110, 107]`
Expected yields: `0.0, 0.0, -2.86, -6.67, 0.0, -2.73`

Then write a regular function `max_drawdown(prices)` that uses the generator to find the worst (most negative) drawdown value.

from typing import List

def drawdown_periods(prices: List[float]):
    peak = 0
    for price in prices:
        if price > peak:
            peak = price
        yield (price - peak) / peak * 100


xd = [100, 105, 102, 98, 110, 107]

print(list(drawdown_periods(xd)))


#That was difficult,  I needed the LLM help a bit

def max_drawdown(prices):
    dd_list = list(drawdown_periods(prices))
    return min(dd_list)

print(max_drawdown(xd))

That was easy after I've got the generator down


---

## Task 5 — Decorator (10 min)

Write a decorator `validate_positive` that:
- Wraps any function
- Before the function runs, checks all numeric arguments (positional and keyword)
- Raises a `ValueError` if any numeric argument is zero or negative
- Lets non-numeric arguments pass through unchecked

Apply it to a simple function `calc_position_size(capital, risk_pct, stop_distance)` that returns `(capital * risk_pct / 100) / stop_distance`.

Test that:
- Normal call works: `calc_position_size(10000, 1.5, 2.0)` → `75.0`
- `calc_position_size(10000, 1.5, -2.0)` raises `ValueError`
- `calc_position_size(10000, 0, 2.0)` raises `ValueError`

from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f'All numeric values must be positive, got {arg} instead')
        for key, val in kwargs.items():
            if isinstance(val, (int, float)) and val <= 0:
                raise ValueError(f'Argument {key} should have only positive arguments, got {val}')
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def calc_position_size(capital: float, risk_pct: float, stop_distance: float):
    return (capital * risk_pct / 100 / stop_distance)


$ python practice.py
75.0
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_agentic_learning\practice.py", line 1038, in <module>
    print(calc_position_size(10000, 1.5, -2.0))
          ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_agentic_learning\practice.py", line 1025, in wrapper
    raise ValueError(f'All numeric values must be positive, got {arg} instead')
ValueError: All numeric values must be positive, got -2.0 instead
(venv) 
HARDPC@DESKTOP-5F8NBD1 MINGW64 ~/Desktop/AL/projekty/python_agentic_learning (main)
$ python practice.py
75.0
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_agentic_learning\practice.py", line 1039, in <module>
    print(calc_position_size(10000, 0, 2.0))
          ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_agentic_learning\practice.py", line 1025, in wrapper
    raise ValueError(f'All numeric values must be positive, got {arg} instead')
ValueError: All numeric values must be positive, got 0 instead
(venv) 


Decorators are also very difficult for me at this point.

---

## Scoring (after submission)
| Task | Points |
|------|--------|
| 1 — Comprehensions | 15 |
| 2 — Functions | 20 |
| 3 — Class | 25 |
| 4 — Generator | 20 |
| 5 — Decorator | 20 |
| **Total** | **100** |

Partial credit given. Style counts — Pythonic solutions score higher than technically-correct-but-verbose ones.
