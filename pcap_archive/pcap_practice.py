
#This file will be used for me to test the code and complete the tasks - but it will not be checked by the agent,
#it's just for me


#Week1 Day1 Task1

'''tasks_files/math_utils.py'''

# '''Mock file for practicing imports with some basic functions'''

# def add(a, b):
#     '''add nums and receive the result'''
#     return a + b

# def multiply(a, b):
#     '''multiply nums and receive the result'''
#     return a * b

# pi = 3.14159 #module-level ocnstant

# '''tasks_files/test_imports.py'''

# import math_utils

# #task1
# x1 = math_utils.add(3, 5)
# print(x1)


#W1 D1 Task2
# import sys
# print(sys.path[0]) #current dir

# num = 0
# for path in sys.path:
#     num += 1
#     print(f'{num}: {path}')

# sys.path.append(r'C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\tasks_files\secret')

# mock_var = 3
# import hidden
# from hidden import * #If we use the wildcard import, we would also import the value of the mock_var in there
# from hidden import mock_var #also works if we would like to import a single variable for whatever reason

# num = 0
# for path in sys.path:
#     num += 1
#     print(f'{num}: {path}')

# print(mock_var)

#W1 D1 Task3
# You're given this broken package structure:

# ```
# broken_pkg/
# ├── __init__.py
# ├── engine.py
# └── utils.py
# ```

# **engine.py:**
# ```python
# from broken_pkg.utils import helper

# def start():
#     return helper()
# ```

# **utils.py:**
# ```python
# from broken_pkg.engine import start

# def helper():
#     return "Engine started: " + start()

# **Task:**
# 1. Predict what error occurs when you run `from broken_pkg import engine`
# 2. Fix the circular dependency WITHOUT changing the function behavior
# 3. Explain your solution in a comment

#We'd get an error, as the engine.py depends on broken_pkg, and we're trying to import what's already in there, and we're trying to select the general scope from the specific file of this very scope, which is erratic. Same for utils.py.
# 
# **engine.py:**
# ```python
# from utils import helper

# def start():
#     return helper()

# **utils.py:**
# ```python
# from engine import start

# def helper():
#     return "Engine started: " + start()

#We simply import the respective modules from the current folder we're in, no need to do circular imports here
#Python automatically checks the current directory first when importing modules


#W1 D1 Task 5

# '''Module used to check dependencies''' 
# /algo_backtest/check_dependencies.py

# def check_deps():
#     try:
#         import pandas as pd
#         import numpy as np
        
#     except ImportError as e:
#         print(f'Import error: {str(e)}')
#     except ModuleNotFoundError as e:
#         print(f'Module not found: {str(e)}')
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
        
#     else:
#         print('Imports succeeded!')
#         print(f'Pandas version: {pd.__version__}')
#         print(f'Numpy version: {np.__version__}')


#W1 D2 T1

# s = "PCAP Exam"
# ```

# Predict the output of each expression (write answers in `practice.py`, paste here):

# 1. `s[100:]`
# 2. `s[-100:]`
# 3. `s[5:3]`
# 4. `s[::-1]`
# 5. `s[::2]`
# 6. `s[-4:-1]`

# **Question:** Why does `s[100:]` return an empty string instead of raising an `IndexError`?
#As slicing never returns an index error.

#empty string
#PCAP Exam
#empty string
#maxE PACP
#PA xm
#Exa

#W1 D2 T2
# print(s.find('E'))
# print(s.index('e'))

# s = "   ,  TEST, TEXT ,SUPER TEXT,    "

# strip = s.strip()
# print(strip)

# lstrip = s.lstrip()
# print(lstrip)

# rstrip = s.rstrip()
# print(rstrip)

# split_no_arg = s.split()
# print(split_no_arg)

# split_arg = s.split(' ')
# print(split_arg)

#W1 D2 T3

# def safe_divide(a: float, b: float) -> float:
    
#     try:
#         result = a / b
    
#     except ZeroDivisionError as e:
#         print(f'Cannot divide by zero! {str(e)}')
#     except TypeError as e:
#         print(f'Wrong data type, use float (e.g. 0.64, 6.4, 64.4). {str(e)}')
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
        
#     else:
#         print('Operation successful')
#         return result
    
#     finally:
#         print('Operation complete')
    

# print(safe_divide(5, 0))
# print(safe_divide(40, 25))

#W1 D2 T4 - REFACTOR/DEBUG

# def process_data(value):
#     try:
#         result = int(value) / 10
#         return result
    
#     except ValueError:
#         print("Invalid number format")
#         return None
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         return None
#     except Exception as e:
#         print(f"Generic error: {e}")
#         return None

#the exception handling instances were put in the wrong order, from general to specific, and it would always end up with a basic Exception handling

#W1 D1 T5

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     print(data.head())
#     print(f"Loaded {len(data)} rows")
    

#/algo_backtest/data/data_loader.py
#     '''
# Data loading module for AlgoBacktest
# '''


# from typing import Optional
# import pandas as pd


# class DataLoader:
#     '''
#     Class used to load and validate data
    
#     Attributes:
#         file_path: path to the csv file with trading data
    
#     '''

#     def __init__(self, file_path: str) -> None:
#         '''Initialize the DataLoader class with file path'''
#         print('DataLoader initialized.')
#         self.filepath = file_path
    
    
#     def load_data(self) -> Optional[pd.DataFrame]:
#         '''
#         Load CSV data with error handling.

#         Returns:
#             DataFrame with columns: timestamp, ticker, open, high, low, close, volume (and DF index)
#             Returns None if file not found.

#         Raises:
#             ValueError: If CSV format is invalid or missing required columns.
#             FileNotFoundError: If file is missing or file name is wrong.
#             Pandas Parser Error: If there are any issues with data parsing.
#         '''
        
#         try:
#             data = pd.read_csv(self.filepath)
#             data.columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
            
        
#         except FileNotFoundError as e:
#             print(f'File not found: {str(e)}')
#             return None
#         except ValueError as e:
#             print(f'Value Error! {str(e)}')
#         except pd.errors.ParserError as e:
#             print(f'Pandas Parser Error: {str(e)}')
#             return None
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')
            
        
#         else:
#             print('Data loading succeeded')
#             return data
        
#         finally:
#             print('Data loading operation ended.')
        
        
#W1 D1 T6

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     print(data.head())
#     print(f"Loaded {len(data)} rows")
    
# x = loader.validate_data(data)
# print(x)


#     def validate_data(self, df: pd.DataFrame) -> bool:
#         '''
#         Docstring for validate_data

#         :param df: Description
#         :type df: pd.DataFrame
#         :return: Description
#         :rtype: bool
#         '''

#         req_columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
#         #ohlc_columns = ['open', 'high', 'low', 'close']


#         missing_columns = set(df.columns) - set(df.columns)
#         if missing_columns:
#             print(f'Missing columns: {missing_columns}')
#             is_valid = False
    
#         nan_values = df[req_columns].isna().sum()
#         if nan_values.any():
#             print(f'Missing values found: {nan_values}')
#             is_valid = False

#         invalid_rows = df[df['high'] < df['low']]
#         if not invalid_rows.empty:
#             print(f'Found {len(invalid_rows)} invalid rows: {invalid_rows}')
#             is_valid = False

#         return is_valiD


        
#W1 D1 T7


# Write a function `read_config(file_path: str) -> dict` that:

# **Handles these edge cases:**
# 1. File doesn't exist (return empty dict)
# 2. File exists but is empty (return empty dict)
# 3. File has permission error (print error, return empty dict)
# 4. File contains valid data (return parsed dict - assume each line is `key=value`)

# def read_config(file_path: str) -> dict:
#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
            
#             if not content.strip(): #the file is empty
#                 return {}
            
#             config = {}
#             for line in content.strip().split('\n'):
#                 key, value = line.split('=', 1)
#                 config[key] = value

#             return config
#     except FileNotFoundError:
#         print(f'File not found - either it does not exist or the file name is wrong!')
#         return {}
#     except PermissionError as e:
#         print(f'Permission error: {str(e)}')

        
#W1 D2 Bonus Task

# def format_trade_summary(ticker: str, price: float, volume: int, side: str) -> str:
#     '''
#     Function used to return the trade in nice format
    
#     args:
#     ticker: str, 
#     price: float, 
#     volume: int, 
#     side: str
    
#     Returns:
#     A nicely formatted trade string, example:
#     "EURUSD: BUY @ 103.25 | Vol: 25,000"
#     '''
    
#     print(f'{ticker}: {side.upper()} @ {price:.2f} | Vol: {volume}')
    
# format_trade_summary('GBPUSD', 120.64, 100, 'buy')


#W1 D3 T1

# class Counter:
#     def __init__(self, start):
#         self.value = start

#     def increment(self):
#         self.value += 1

#     def get_value(self):
#         return self.value

# c1 = Counter(10)
# c2 = Counter(20)

# c1.increment()
# c1.increment()
# c2.increment()

# print(c1.get_value())
# print(c2.get_value())

# **Your answer:**
# - Line 1 output: `12`
# - Line 2 output: `21`

# **Explain:** Why do `c1` and `c2` have different values even though they're both `Counter` objects?

# **Answer here:**

# They are different objects, the Counter is only a blueprint for creating them. 
# C1 starts with 10 as a starting value and c2 with 20, and the number only gets incremented 
# as we call the increment() method (not function, as it's a class - method) only for the given object.


#W1 D3 T2

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name):
#         self.name = name

# dog1 = Dog("Buddy")
# dog2 = Dog("Max")

# print(dog1.name)
# print(dog2.name)
# print(dog1.species)
# print(dog2.species)

# Dog.species = "Canis lupus"

# print(dog1.species)
# print(dog2.species)


# **Your predictions:**
# 1. `dog1.name` → `Buddy`
# 2. `dog2.name` → `Max`
# 3. `dog1.species` (first time) → `Canis familiaris`
# 4. `dog2.species` (first time) → `Canis familiaris`
# 5. `dog1.species` (after change) → 'Canis lupus`
# 6. `dog2.species` (after change) → Canis lupus`

# **Question:** What's the difference between `self.name` and `species` in this class?

# **Answer here:**
# Self.name is an attribute of a given class object - dog1/dog2.
# If we create a dog1 as an instance of the Dog class, chosen self.name 
# will only reference to this particular object, instance.

# Species, however, is a class attribute of class Dog, 
# and it relates to the whole class, including all of the instances of it.

#W1 D3 T3

# class BankAccount:
    
#     """
#     Represents a simple bank account.

#     Attributes:
#         owner: Account owner's name.
#         balance: Current account balance.
#     """
    
    
#     def __init__(self, owner: str, balance: float = 0.0):
#         """Constructor used to initialize account with owner and optional starting balance."""
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount: float) -> None:
#         '''
#         Method used to deposit a given amount in the account
#         Only accepts positive amount values
#         '''
        
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f'Only positive amounts accepted for deposit!')
    
#     def withdraw(self, amount: float) -> bool:
#         '''
#         Method used to withdraw a given amount from the account
#         Only accepts withdraw if:
        
#         1. The withdrawn amount is above 0.
#         2. There is a sufficient balance in the account.
        
#         Returns True if the withdraw is successful, otherwise it returns False.
#         '''
        
#         if amount < 0:
#             print('Cannot withdraw NEGATIVE amounts!')
#             return False
#         elif self.balance < amount:
#             print(f'Cannot withdraw ${amount:.2f} as the current balance is below that amount!')
#             return False
#         else:
#             self.balance -= amount
#             print(f'${amount} withdrawn successfully.')
#             return True
    
#     def get_balance(self) -> float:
#         '''
#         Checks the current balance of the account
#         '''
        
#         return self.balance


# account = BankAccount("Alice", 100.0)
# account.deposit(50.0)
# print(account.get_balance())  # Should print 150.0
# account.withdraw(30.0)
# print(account.get_balance())  # Should print 120.0
# account.withdraw(200.0)       # Should fail (insufficient funds)
# print(account.get_balance())  # Should still be 120.0


#W1 D3 T4 - find the bug

# class TodoList:
#     tasks = []

#     def __init__(self, owner):
#         self.owner = owner

#     def add_task(self, task):
#         self.tasks.append(task)

#     def get_tasks(self):
#         return self.tasks

# alice_todos = TodoList("Alice")
# bob_todos = TodoList("Bob")

# alice_todos.add_task("Buy groceries")
# bob_todos.add_task("Walk dog")

# print(f"Alice's tasks: {alice_todos.get_tasks()}")
# print(f"Bob's tasks: {bob_todos.get_tasks()}")

# Bug: All of the instances - alice and bob todos will share the same list of tasks, 
# as they used class attribute tasks, 
# which is shared across all of the class instances.

#FIX:

# class TodoList:
    
#     def __init__(self, owner: str):
#         self.owner = owner
#         self.tasks = [] #instead of using list as a default argument, we initiate it here

#     def add_task(self, task):
#         self.tasks.append(task)

#     def get_tasks(self):
#         return self.tasks

# alice_todos = TodoList("Alice")
# bob_todos = TodoList("Bob")

# alice_todos.add_task("Buy groceries")
# bob_todos.add_task("Walk dog")

# print(f"Alice's tasks: {alice_todos.get_tasks()}")
# print(f"Bob's tasks: {bob_todos.get_tasks()}")

#W1 D3 T5 - I created algo_backtest/engine/position.py

# from algo_backtest.engine.position import Position

# long_pos = Position('FDAX', 'buy', 25100, 10, 25050, 25350)
# print(long_pos.calculate_pnl(25250.0))  # 1000.0
# print(long_pos.should_close(25090.0))  # True (hit SL)

# short_pos = Position("GBPUSD", 'SELL', entry_price=120.0, quantity=-500, stop_loss=121.0, take_profit=118.0)
# print(short_pos.calculate_pnl(119.0))  # 500.0
# print(short_pos.should_close(117.5))  # True (hit TP)


#W1 D3 T6 - fixes in ago_backtest/data/data_loader - 
#added context manager to load_data() - with open() as f: pd.read_csv(f),
#added missing return statement in ValueError + logic error in validate_data for missing cols

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     is_valid = loader.validate_data(data)
#     print(f"Data valid: {is_valid}")  # Should print True


#W1 D3 T7


# What is the output of this code?
#
# class Test:
#     value = 10

#     def __init__(self):
#         self.value = 20

# obj = Test()
# print(obj.value)
# print(Test.value)
# ```

# **Choices:**
# A) `20` then `20`
# B) `10` then `10`
# C) `20` then `10`
# D) `10` then `20`

# **Your answer with explanation:**
#A,
# In the first print we print the attribute value of the object, 
# which is self.value, 20;
# In the second print however we print the class attribute, 
# is shared across all the class instances, and it's 10.

# What happens when you run this code?

# class Person:
#     def __init__(self, name):
#         self.name = name
#         return self

# p = Person("Alice")
# ```

# **Choices:**
# A) Works fine, `p.name` is `"Alice"`
# B) `TypeError: __init__() should return None`
# C) `AttributeError: 'NoneType' object has no attribute 'name'`
# D) `NameError: self is not defined`

# **Your answer with explanation:**
# B, init should return None!


#W1 D3 T8
#Enhance the `OHLCCandle` class from the lesson with new methods.

# class OHLCCandle:
#     """Represents a single OHLC candle."""

#     def __init__(self, timestamp: str, ticker: str, open_price: float,
#                  high: float, low: float, close: float, volume: int) -> None:
#         self.timestamp = timestamp
#         self.ticker = ticker
#         self.open = open_price
#         self.high = high
#         self.low = low
#         self.close = close
#         self.volume = volume

#     def is_bullish(self) -> bool:
#         """Check if candle closed higher than it opened."""
#         return self.close > self.open

#     def get_body_size(self) -> float:
#         """Calculate candle body size."""
#         return abs(self.close - self.open)

#     def get_range(self) -> float:
#         """Calculate candle range (high - low)."""
#         return self.high - self.low
    
#     def is_doji(self, threshold: float = 0.1) -> bool:
#         if abs(self.close - self.open) / (self.high - self.low) < threshold:
#             return True
#         elif self.high - self.low == 0:
#             return True
#         else:
#             return False
#     def get_upper_wick(self) -> float:
#         max_price = max(self.open, self.close)
#         return self.high - max_price
    
#     def get_lower_wick(self) -> float:
#         min_price = min(self.open, self.close)
#         return min_price - self.low
    

# candle = OHLCCandle(
#     timestamp="2024-01-01 09:00:00",
#     ticker="EURUSD",
#     open_price=100.5,
#     high=101.0,
#     low=100.0,
#     close=100.6,
#     volume=5000
# )

# print(f"Is doji? {candle.is_doji()}")  # Should be False (body is significant)
# print(f"Upper wick: {candle.get_upper_wick():.2f}")  # 101.0 - 100.6 = 0.40
# print(f"Lower wick: {candle.get_lower_wick():.2f}")  # 100.5 - 100.0 = 0.50

#W1 D3 Bonus task
#Employee class that assigns unique IDs to each employee using a class attribute counter

# class Employee:
#     """
#     Employee with auto-incrementing ID.

#     Class Attributes:
#         total_employees: Counter for total employees created.

#     Instance Attributes:
#         name: Employee name.
#         employee_id: Unique ID assigned automatically.
#     """

#     total_employees = 0

#     def __init__(self, name: str):
#         Employee.total_employees += 1
#         self.name = name
#         self.employee_id = Employee.total_employees

# emp1 = Employee("Alice")
# emp2 = Employee("Bob")
# emp3 = Employee("Charlie")

# print(emp1.employee_id)  # 1
# print(emp2.employee_id)  # 2
# print(emp3.employee_id)  # 3
# print(Employee.total_employees)  # 3


#W1 D4 T1
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"Product(name={self.name!r}, price={self.price})"

#     def __str__(self):
#         return f"{self.name}: ${self.price:.2f}"

# product = Product("Laptop", 999.99)

# print(str(product)) #`Laptop: $999.99`
# print(repr(product)) #`Product(name = 'Laptop'), price = 999.99`
# print(product)       #`Laptop: $999.99`

#W1 D4 T2
# class Counter:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"Counter: {self.value}"

# counter = Counter(10)
# result = str(counter)
# print(f"Result: {result}")


#W1 D4 T3 - updates of __repr__ and __str__ in algo_backtest/engine/position.py
# from algo_backtest.engine.position import Position

# pos = Position("EURUSD", "BUY", 1.0850, 10000, stop_loss=1.0800, take_profit=1.0950)
# print(repr(pos))  # Should show Position(ticker='EURUSD', ...)
# print(str(pos))   # Should show BUY 10000 EURUSD @ 1.0850 [SL=1.0800, TP=1.0950]
# print(pos)        # Should use __str__

# pos_no_sl = Position("GBPUSD", "SELL", 1.2500, 5000)
# print(pos_no_sl)  # Should show SELL 5000 GBPUSD @ 1.2500 [No SL, No TP]


#W1 D4 T4 - checking for NaN values in Pandas


# df = pd.DataFrame({
#     'ticker': ['EURUSD', 'GBPUSD', 'USDJPY'],
#     'open': [1.08, 1.25, np.nan],
#     'close': [1.09, np.nan, 110.5],
#     'volume': [1000, 1500, 2000]
# })

# check_nan1 = df.isna().sum().sum() #returns a total sum of NaNs in our DF
# print(check_nan1)

# check_nan2 = df.isna().sum() #returns a nice breakthrough of all columns and the number of NaNs in each
# print(check_nan2)

# check_nan3 = df.isna().any().any() #returns True
# print(check_nan3)

#W1 D4 T5 - Pandas practice

# df = pd.DataFrame({
#     'timestamp': ['2024-01-01 09:00', '2024-01-01 09:01', '2024-01-01 09:02', '2024-01-01 09:03'],
#     'ticker': ['EURUSD', 'EURUSD', 'EURUSD', 'EURUSD'],
#     'open': [1.0800, 1.0820, 1.0850, 1.0830],
#     'high': [1.0850, 1.0870, 1.0900, 1.0880],
#     'low': [1.0790, 1.0810, 1.0840, 1.0820],
#     'close': [1.0820, 1.0850, 1.0830, 1.0850],
#     'volume': [1000, 1500, 2000, 1200]
# })

# # 1. Filter rows where `close > open` (bullish candles)
# # 2. Filter rows where `volume > 1200` AND `close > 1.0840`
# # 3. Get the `high` values (as a Series) where `close > open`
# # 4. Count how many candles are bullish (close > open)

# bullish_candles = df[df['close'] > df['open']]
# filtered_rows = df[(df['volume'] > 1200) & (df['close'] > 1.0840)]
# high_series = pd.Series(df['high'][df['close'] > df['open']])
# bullish_candles_count = len(df[df['close'] > df['open']])
# print(bullish_candles_count)

#W1 D4 T6 - creating Trade Class in algo_backtest/engine/trade.py
# from algo_backtest.engine.trade import Trade

# # Winning BUY trade
# trade1 = Trade(
#     ticker="EURUSD",
#     side="BUY",
#     entry_price=1.0800,
#     exit_price=1.0850,
#     quantity=10000,
#     entry_time="2024-01-01 09:00",
#     exit_time="2024-01-01 09:30",
#     exit_reason="TP"
# )

# print(trade1)
# # Expected: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $50.00

# # Losing SELL trade
# trade2 = Trade(
#     ticker="GBPUSD",
#     side="SELL",
#     entry_price=1.2500,
#     exit_price=1.2550,
#     quantity=5000,
#     entry_time="2024-01-01 10:00",
#     exit_time="2024-01-01 10:15",
#     exit_reason="SL"
# )

# print(trade2)
# Expected: [LOSS] SELL 5000 GBPUSD: 1.2500 -> 1.2550 (SL) | P&L: $-25.00


#W1 D4 T7

# df = pd.DataFrame({'a': [1, 2, 3]})
# #result = df['a'] > 2 and df['a'] < 5 #ERROR, ValueError - doesn't work like that with Series

# result = df[(df['a'] > 2) & (df['a'] < 5)] #correct application
# print(result)

#W1 D4 T8 - modifying algo_backtest/data/data_loader.py - classmethod

# from algo_backtest.engine.trade import Trade

# trade1 = Trade("EURUSD", "BUY", 1.08, 1.09, 10000, "2024-01-01 09:00", "2024-01-01 09:30", "TP")
# trade2 = Trade("GBPUSD", "SELL", 1.25, 1.26, 5000, "2024-01-01 10:00", "2024-01-01 10:15", "SL")
# trade3 = Trade("USDJPY", "BUY", 110.00, 110.50, 2000, "2024-01-01 11:00", "2024-01-01 11:45", "TP")

# trades = [trade1, trade2, trade3]
# win_rate = Trade.calculate_win_rate(trades)
# print(f"Win rate: {win_rate:.1f}%")  # Expected: 66.7%
# print(trades)

#W1 D5 T1

# **Answer these short questions to test your Week 1 retention:**

# 1. What's the difference between `import math` and `from math import sqrt`?
# 2. What does `"PCAP"[10:20]` return? (No IndexError!)
# 3. In exception handling, why must specific exceptions come before general ones?
# 4. What's the difference between an instance attribute and a class attribute?
# 5. When does Python call `__repr__` vs `__str__`?
# 6. What operator do you use for multiple conditions in Pandas filtering? (`and`/`or` or `&`/`|`?)

# **Your answers:**

# 1. Two differences - in the first example we import all the relevant functions from math that are set to be imported there by default if we use this general import (this is also the best practice, as we're not occupying the namespace), but to use them we have to call math.module_name; In the second example we only import the sqrt function and we can call it by naming it sqrt. It's not the best practice as we're also occupying the namespace and may cause naming conflicts, especially if our codebase is large and we import a lot of functions like that.
# 2. Empty string
# 3. Because otherwise we would always catch the general exception catch, and it would block the other exception handling cases (so effectively, they would be pointless)
# 4. Instance attribute is tied to a given instance of a class, while a class attribute is shared among all instances of a given class.
# 5. It calls __str__ by default if it's available and if we do print(class_name); __repr__ would be called instead if __str__ is not available. We can also simply explicitly call both methods as in print(repr(class_name)) or print(str(class_name))
# 6. For single elements comparison, we use and/or operators, and for series we use & / | instead, so in this case the answer is `&`/`|`.


#W1 D5 T2- updated algo_backtest/main.py to import data_loader and trade 
# and do a mock backtest of 3 manually added trades

#W1 D5 T3


# class Portfolio:
#     total_portfolios = 0

#     def __init__(self, name):
#         self.name = name
#         Portfolio.total_portfolios += 1

#     def __str__(self):
#         return f"Portfolio: {self.name}"

#     def __repr__(self):
#         return f"Portfolio({self.name!r})"

# p1 = Portfolio("Tech Stocks")
# p2 = Portfolio("Bonds")

# print(p1)
# print(repr(p2))
# print(f"Total: {Portfolio.total_portfolios}")

# portfolios = [p1, p2]
# print(portfolios)

# **Your predictions:**
# - Line 1 (`print(p1)`): `Portfolio: Tech Stocks`
# - Line 2 (`print(repr(p2))`): `Portfolio('Bonds')`
# - Line 3 (`print(f"Total: ...")`): `Total: 2`
# - Line 4 (`print(portfolios)`): `[Portfolio('Tech Stocks'), Portfolio('Bonds')]`

#W1 D5 T4

# from typing import Optional, List
# from algo_backtest.data.data_loader import DataLoader
# from algo_backtest.engine.trade import Trade


# def safe_backtest_runner(filepath: str) -> Optional[List[Trade]]:
#     """
#     Safely run backtest with error handling.

#     Args:
#         filepath: Path to OHLC data CSV.

#     Returns:
#         List of Trade objects if successful, None if any error occurs.

#     Error Handling:
#         - FileNotFoundError: Data file missing
#         - ValueError: Invalid data format
#         - KeyError: Missing required columns
#         - Exception: Catch-all for unexpected errors
#     """

#     try:
        
#         trades = []
#         loader = DataLoader(filepath)
#         data = loader.load_data()
#         x = loader.validate_data(data)
        
#         if x:
#             trade1 = Trade(data.iloc[0]['ticker'],     #ticker
#                            'BUY',                      #side     
#                            data.iloc[15]['open'],      #entry_price
#                            data.iloc[34]['close'],     #exit_price
#                            15000,                      #quantity
#                            data.iloc[15]['timestamp'], #entry_time
#                            data.iloc[35]['timestamp'], #exit_time
#                            '')                         #reason (nie wrzucam nic na razie)
            
            
#             trade2 = Trade(data.iloc[0]['ticker'],     #jw.
#                            'SELL',
#                            data.iloc[18]['open'],
#                            data.iloc[27]['close'],
#                            15000,
#                            data.iloc[18]['timestamp'],
#                            data.iloc[28]['timestamp'],
#                            '')
#             trades = [trade1, trade2]

#     except FileNotFoundError as e:
#         print(f'File not found: {str(e)}')
#         return None

#     except ValueError as e:
#         print(f'Wrong value: {str(e)}')
#         return None

#     except KeyError as e:
#         print(f'Key not found: {str(e)}')
#         return None
    
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
#         return None
    
#     else:
#         print('Trades added successfully, returning the list of trades.')
#         return trades

#     finally:
#        print('Operation finished')

# # Test 1: Valid file
# result = safe_backtest_runner('ohlc_mock_data.csv')
# print(f"Valid file: {result is not None}")  # Should be True

# # Test 2: Missing file
# result = safe_backtest_runner('nonexistent.csv')
# print(f"Missing file: {result is None}")  # Should be True


#W1 D5 T5
# data = pd.read_csv('ohlc_mock_data.csv')

# import numpy as np
# # Question 1: What's the average close price for bullish candles only?
# # Your code here
# avg_bullish_close = np.mean([data['close'][data['close'] > data['open']]])
# print(avg_bullish_close)
# # Question 2: Find the candle with the highest volume
# # Return the entire row as a Series
# # Your code here
# highest_vol = np.max([data['volume']])
# highest_vol_candle = data[data['volume'] == highest_vol]
# print(highest_vol_candle)
# # Question 3: Calculate the total volume for candles where close > 100.5
# # Your code here

# total_vol_candles = sum(data['volume'][data['close'] > 100.5])
# print(total_vol_candles)

# # Question 4: Create a new column 'candle_type' with values 'bullish' or 'bearish'
# # based on close vs open
# # Your code here
# for index, row in data.iterrows():
#     row['candle_type'] = 'bullish' if row['close'] > row['open'] else 'bearish'
#     print(row)
# #Here we iterate, creating a copy of each row, so we don't add anything to the original df

# data['candle_type'] = data.apply(lambda row: 'bullish' if row['open'] > row['close'] else 'bearish',
#                                          axis = 1)
# print(data)

# # Question 5: Get all candles where high is in the top 10 highest values
# # Hint: Use .nlargest()
# # Your code here
# top_10_highs = data.nlargest(10, 'high')
# print(top_10_highs)


#W1 D5 T6 - created algo_backtest/engine/position_manager to manage multiple positions

# from algo_backtest.engine.position_manager import PositionManager
# from algo_backtest.engine.position import Position

# manager = PositionManager()

# # Add positions
# pos1 = Position("EURUSD", "BUY", 1.0800, 10000, stop_loss=1.0750, take_profit=1.0900)
# pos2 = Position("GBPUSD", "SELL", 1.2500, 5000, stop_loss=1.2550, take_profit=1.2450)

# manager.add_position(pos1)
# manager.add_position(pos2)

# print(manager)  # PositionManager: 2 open positions

# # Check P&L at current price
# current_price = 1.0850
# total_pnl = manager.get_total_pnl(current_price)
# print(total_pnl)

# # Check for triggered positions
# closed = manager.close_triggered_positions(1.0900)
# print(f"Closed {len(closed)} positions")
# print(manager)  # Should show 1 open position now

#W1 D5 T8 - Bug hunter 

#I'm leaving the original version in its oriignal form 

# """Broken trading simulator - find all bugs!"""

# class trade:
#     def __init__(self, Ticker, side, entry, exit, qty):
#         self.ticker = Ticker
#         self.Side = side
#         self.entry = entry
#         self.exit = exit
#         self.qty = qty

#     def __str__(self):
#         print(f"{self.Side} {self.ticker}")

#     def calc_pnl(self):
#         if self.Side == "BUY":
#             return (self.exit - self.entry) * self.qty
#         else:
#             return (self.entry - self.exit) * self.qty

# trades = []

# import pandas as pd
# df = pd.read_csv("data.csv")

# for i in range(len(df)):
#     row = df.iloc[i]
#     t = trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
#     trades.append(t)

# total = 0
# for t in trades:
#     total = total + t.calc_pnl()

# print(f"Total PNL: {total}")

#**List of all issues I found:**

# 1. uncapitalized class name - trade
# 2. capitalized parameter name - Ticker
# 3. capitalized self.Side 
# 4. it would be nice to also add .upper to side to account for potential case issues
# 5. weird __str__ representation with unclear information (missing data) AND an error - it uses print instead of return
# 6. wrong place to import pandas module
# 7. general lack of exception handling
# 8. wrong total_pnl calculation

#Fixed version:

# '''
# Fixed trade simulator
# '''

# import pandas as pd

# class Trade:
#     def __init__(self, ticker, side, entry, exit, qty):
#         '''init constructor for the Trade class'''
#         self.ticker = ticker
#         self.side = side.upper()
#         self.entry = entry
#         self.exit = exit
#         self.qty = qty
        
#     def __str__(self):
#         '''A clear representation of a class if anybody decides to use print(Trade)'''
#         return f"{self.side} {self.qty} {self.ticker} @ {self.entry}, EXIT @ {self.exit}"
    
#     def calc_pnl(self):
#         '''Method used to calculate profit of a given position
        
#         Returns the pnl value, depending on the side (buy or sell)
#         '''
#         if self.qty < 0 or self.entry < 0 or self.exit < 0:
#             print(f'Wrong value, it should be above 0!')
#             return None
        
#         if self.side == "BUY":
#             return (self.exit - self.entry) * self.qty
#         else:
#             return (self.entry - self.exit) * self.qty
    

# trades = []
# filepath = 'ohlc_mock_data.csv'

# df = pd.read_csv(filepath)

# for i in range(len(df)):
#     row = df.iloc[i]
#     t = Trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
#     trades.append(t)

# total = 0
# for t in trades:
#     total += t.calc_pnl()

# print(f"Total PNL: {total}")


# class Test:
#     items = []

#Start 11:32
#W2 D1 T1

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof"

# d = Dog("Buddy")
# print(d.name)
# print(d.speak())


#W2 D1 T2 - a child class SavingsAccount adding to the class we created last week


# class BankAccount:
    
#     """
#     Represents a simple bank account.

#     Attributes:
#         owner: Account owner's name.
#         balance: Current account balance.
#     """
    
    
#     def __init__(self, owner: str, balance: float = 0.0):
#         """Constructor used to initialize account with owner and optional starting balance."""
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount: float) -> None:
#         '''
#         Method used to deposit a given amount in the account
#         Only accepts positive amount values
#         '''
        
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f'Only positive amounts accepted for deposit!')
    
#     def withdraw(self, amount: float) -> bool:
#         '''
#         Method used to withdraw a given amount from the account
#         Only accepts withdraw if:
        
#         1. The withdrawn amount is above 0.
#         2. There is a sufficient balance in the account.
        
#         Returns True if the withdraw is successful, otherwise it returns False.
#         '''
        
#         if amount < 0:
#             print('Cannot withdraw NEGATIVE amounts!')
#             return False
#         elif self.balance < amount:
#             print(f'Cannot withdraw ${amount:.2f} as the current balance is below that amount!')
#             return False
#         else:
#             self.balance -= amount
#             print(f'${amount} withdrawn successfully.')
#             return True
    
#     def get_balance(self) -> float:
#         '''
#         Checks the current balance of the account
#         '''
        
#         return self.balance
    
    
    
# class SavingsAccount(BankAccount):
        
#     '''A child class of BankAccount with added interest_rate
#     and add_interest method that allows for interest compounding'''
    
#     def __init__(self, owner: str, balance: float, interest_rate: float):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#         self.balance = balance
    
#     def __str__(self):
#         return f'SavingsAccount(balance = ${super().get_balance()}, rate = {self.interest_rate}%)'
        
#     def add_interest(self):
#         '''Compounds the interest based on set interest_rate'''
#         self.balance += self.interest_rate * self.balance
#         return self.balance
        
        
# savings = SavingsAccount(owner="Alice", balance=1000.0, interest_rate=0.05)
# print(savings)  # SavingsAccount(balance=$1000.00, rate=5.0%)
# savings.add_interest()
# print(savings.get_balance())  # 1050.0
# savings.add_interest()
# print(savings.get_balance())


#W2 D1 T3

# class Strategy:
#     '''A strategy class used to generate trades based on set signals + child classes with specific strategies'''
#     def __init__(self, name: str):
#         self.name = name
        
#     def generate_signal(self, price: float) -> str:
#         return 'HOLD'
    
# class LevelCrossStrategy(Strategy):
#     def __init__(self, level: float):
#         super().__init__('Level Cross')
#         self.level = level
        
#     def generate_signal(self, price: float) -> str:
        
#         if price > self.level:
#             return 'BUY'
#         elif price < self.level:
#             return 'SELL'
#         else:
#             return 'HOLD'
        
# strategy = LevelCrossStrategy(100.0)
# print(strategy.generate_signal(105))  # "BUY"
# print(strategy.generate_signal(95))   # "SELL"
# print(strategy.generate_signal(100))  # "HOLD"


#W2 D1 T4 - bug hunting

#original
# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def __init__(self, brand, year, doors):
#         self.doors = doors

# car = Car("Toyota", 2023, 4)
# print(car.brand)  # What happens here?

#Bug - brand, year in child class should be plugged from the parent class with super()
#Fix:

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def __init__(self, brand, year, doors):
#         super().__init__(brand, year)
#         self.doors = doors
        

# car = Car("Toyota", 2023, 4)
# print(car.brand)


#W2 D1 T5

# class Animal:
#     pass

# class Mammal(Animal):
#     pass

# class Dog(Mammal):
#     pass

# dog = Dog()

# print(isinstance(dog, Dog))           # A  -> True
# print(isinstance(dog, Mammal))        # B -> True
# print(isinstance(dog, Animal))        # C -> True
# print(isinstance(dog, object))        # D (TRICKY!) -> True

# print(issubclass(Dog, Mammal))        # E -> True
# print(issubclass(Dog, Animal))        # F -> False
# print(issubclass(Dog, Dog))           # G (TRICKY!) -> True
# print(issubclass(Animal, Dog))        # H -> False


#W2 D1 T6 - abstract base class - `algo_backtest/strategies/base_strategy.py`


# '''Abstract Method Class - base strategy'''

# from abc import ABC, abstractmethod

# class BaseStrategy(ABC):
#     '''A class with abstract method used to generate trading signal'''
#     def __init__(self, name: str):
#         self.name = name
        
#     @abstractmethod
#     def generate_signal(self, price: float) -> str:
#         pass
    
#     def get_name(self) -> str:
#         '''inherited method to fetch a given strategy name'''
#         return self.name


#import also added to strategies/init.py
# from .base_strategy import BaseStrategy

# __all__ = ['BaseStrategy']


#W1 D1 T8 - code review/issue detection

#original:
# class strategy:
#     def init(self, name):
#         name = name

#     def signal(self, price):
#         return HOLD

# class MovingAverageStrategy(strategy):
#     def init(self, ma_period):
#         self.ma_period = ma_period

#     def signal(self, price):
#         result = super().signal(price)
#         if price > 100:
#             return "buy"
#         return result

# strat = MovingAverageStrategy(20)
# print(strat.name)


#ISSUES:\
# 1. Uncapitalized class name
# 2. Lack of floor symbols __ next to init
# 3. name in init has local scope instead of being self.name
# 4. HOLD in signal in parent class will trigger a TypeError, as it's not defined in anyway, and it's not a string either
# 5. lack of super() to get the parent class parameters in init
# 6. with current logic in signal in both classes, we only get to have a 'buy' or 'hold' signal (from the parent class), and no sell at all
# 7. the class is called without a name
# 8. Lack of type hints

#fixed version:

# class Strategy:
#     '''a base strategy for creating strategies'''
#     def __init__(self, name: str):
#         self.name = name

#     def signal(self):
#         pass

# class MovingAverageStrategy(Strategy):
#     '''a child-class of strategy class with its separate signal generating logic'''
#     def __init__(self, name: str, ma_period: float):
#         super().__init__(name)
#         self.ma_period = ma_period

#     '''Signal class used to generate signals for the moving average strategy (mock, as you can see :))'''
#     def signal(self, price: float):
#         if price > 100:
#             return 'Buy'
#         elif price < 100:
#             return 'Hold'
        
# strat = MovingAverageStrategy('Strategy1', 20)
# print(strat.name)

#finish 12:38

#W2 D2 T2 - creating a mock strategy inherited from BaseStrategy (w/ abstract method for generate_signal in BaseStrategy)

# from .base_strategy import BaseStrategy

# class LevelCrossStrategy(BaseStrategy):
#     '''
#     A strategy based on crossing certain levels
#     '''
    
#     def __init__(self, level: float):
#         '''Initializing the class with defined level'''
#         super().__init__('Level Cross Strategy')
#         self.level = level
        
    
#     def generate_signal(self, price: float) -> str:
#         '''
#         Method used to generate signal based on a price you pass - this is a mock method mainly used to practice.
        
#         It's an instance of a method that inherits abstract method from BaseStrategy (so it's mandatory).
#         Signals for real strategies most likely will be more robust.
#         '''
#         if price > self.level:
#             return 'BUY'
#         elif price < self.level:
#             return 'SELL'
#         elif price == self.level:
#             return 'HOLD'
    
    
#     def get_level(self) -> float:
#         '''Method used to return the set level'''
#         return self.level

#W2 D2 T3 - Another mock strategy built with BaseStrategy inheritance

# from .base_strategy import BaseStrategy
# from typing import List

# class MovingAverageStrategy(BaseStrategy):
    
#     def __init__(self, ma_period: int):
#         '''Initialization of the class, inheriting the base init from the BaseStrategy and extending it'''
#         super().__init__(f'MovingAverage Strategy - ma {ma_period}')
#         self.ma_period = ma_period
#         self.price_history: List[float] = []
    
#     def add_price(self, price: float):
#         '''Method used to add a price to the self.price_history list'''
#         self.price_history.append(price)
#         if len(self.price_history) > self.ma_period:
#             self.price_history.remove([0])
            
#     def generate_signal(self, price: float) -> str:
#         '''Method used to check whether the list has enough entries to be able to calculate the MA properly'''
#         if len(self.price_history) < self.ma_period:
#             print(f'Not enough data entries to properly count ma {self.ma_period}. Currently we only have {len(self.price_history)} entries.')
#             return 'HOLD'
        
#         else:
#             ma_value = sum(self.price_history) / self.ma_period
#             if price > ma_value:
#                 return 'BUY'
#             else:
#                 return 'SELL'        


#W2 D2 T4 - testing the strategies with a function

# from algo_backtest.strategies import MovingAverageStrategy, LevelCrossStrategy

# '''Test script used to check if our strategies work properly'''

# def test_strategy(strategy, prices: list[float]) -> None:
#     """Test a strategy with a list of prices.

#     Args:
#         strategy: Any strategy that has generate_signal method
#         prices: List of prices to test
#     """
#     print(f"\nTesting: {strategy.get_name()}")
#     for price in prices:
#         signal = strategy.generate_signal(price)
#         print(f"  Price {price}: {signal}")


# strat1 = MovingAverageStrategy(5)
# strat2 = LevelCrossStrategy(100.5)

# strat1.add_price(430)
# strat1.add_price(230)
# strat1.add_price(450)
# strat1.add_price(470)
# strat1.add_price(490)
# strat1.add_price(530)
# test_strategy(strat1, [430, 450, 520, 550, 570, 460, 430, 320])
# test_strategy(strat2, [120, 105, 90, 20])


#W2 D2 T5


# from algo_backtest.strategies import BaseStrategy, LevelCrossStrategy, MovingAverageStrategy

# def analyze_strategy(strategy: BaseStrategy) -> str:
#     """Analyze a strategy and return description based on its type.

#     Args:
#         strategy: Any strategy instance

#     Returns:
#         Description string
#     """
    
#     if isinstance(strategy, LevelCrossStrategy):
#         return f"{strategy.name} with level={strategy.level}"
#     elif isinstance(strategy, MovingAverageStrategy):
#         return f"{strategy.name} with period={strategy.ma_period}"
#     else:
#         return strategy.name

# # Test cases
# strat1 = LevelCrossStrategy(100.0)
# strat2 = MovingAverageStrategy(5)

# print(analyze_strategy(strat1))
# # Expected: "Level Cross Strategy with level=100.0"

# print(analyze_strategy(strat2))


#W2 D2 T8 - Bug bounty

#THE BUGGY ORIGINAL:
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "Starting vehicle"

# class Car(Vehicle):
#     def start(self):
#         return f"Starting {self.brand} car"

# class Motorcycle(Vehicle):
#     pass

# def start_all_vehicles(vehicles):
#     for v in vehicles:
#         print(v.start())

# vehicles = [
#     Car("Toyota"),
#     Motorcycle("Harley"),
#     Vehicle("Generic")
# ]

# start_all_vehicles(vehicles)


#issues:
#1. Lack of docstrings/typehints
#2. Car has a missing init and it doesn't use super() - perhaps it's okay as the code still works, but it just looks weird to me
#3. The Motorcycle class is empty, so what's the point of even having it there when it does nothing different compared to the parent class?
#4. As a consequence of the above, the start_all_vehicles will not be able to work properly and list all the vehicles.

#fix

# class Vehicle:
#     '''Parent class used to start a vehicle'''
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "Starting vehicle"

# class Car(Vehicle):
#     '''A polimorphic variant of a Vehicle that is designed specifically for cars'''
#     def __init__(self, brand: str, doors: int):
#         super().__init__(brand)
#         self.doors = doors
    
#     def start(self):
#         return f"Starting {self.brand} car with {self.doors} doors"

# class Motorcycle(Vehicle):
#     '''A polimorphic variant of a Vehicle extended specifically for motorcycles'''
#     def __init__(self, brand, horsepower: int):
#         super().__init__(brand)
#         self.horsepower = horsepower
        
#     def start(self):
#         return f'Starting a {self.brand} motorcycle with {self.horsepower} horsepower'

# def start_all_vehicles(vehicles):
#     for v in vehicles:
#         print(v.start())

# vehicles = [
#     Car("Toyota", 4),
#     Motorcycle("Harley", 50),
#     Vehicle("Generic")
# ]

# start_all_vehicles(vehicles)


#W2 D3 T1 -> MRO predictions

# class Animal:
#     def speak(self):
#         return "generic sound"

# class Mammal(Animal):
#     def speak(self):
#         return "mammal sound"

# class Bird(Animal):
#     def speak(self):
#         return "chirp"

# class Bat(Mammal, Bird):
#     pass

# class Platypus(Bird, Mammal):
#     pass

# bat = Bat()
# platypus = Platypus()

# print(bat.speak()) # -> 'mammal sound'
# print(platypus.speak()) # -> 'chirp'
# print(Bat.__mro__) # Mammal -> Bird -> Animal

#W2 D3 T4

# class LoggerMixin:
    
#     def __init__(self):
#         self.class_name = None
    
#     def log(self, message: str):
#         print(f'{self.class_name} message: {message}')
    


# class Trade(LoggerMixin):
    
#     def __init__(self):
#         super().__init__()
#         self.class_name = 'Trade Class'
        

# x = Trade()
# x.log('Test Xd')

#W2 D3 T5 - error prediction


# Case A -> Error, B is inherited from A, and it doesn't make sense to later make A inherited from B 
# class A:
#     pass

# class B(A):
#     pass

# class C(A, B):
#     pass

# # Case B -> No error, everything's fine here and we kind of 'appoint' the inheritance structure in Z class
# class X:
#     pass

# class Y:
#     pass

# class Z(X, Y):
#     pass

# # Case C -> No error, It's a proper structure of inheritance -> It doesn't change much, but it works.
# class P:
#     pass

# class Q(P):
#     pass

# class R(Q):
#     pass

# class S(R, Q):
#     pass


#W2 D3 T8 - # Identifying issues

# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

# class UserManager(Database):  # IS-A relationship
#     def __init__(self, connection_string):
#         super().__init__(connection_string)

#     def get_user(self, user_id):
#         return self.query(f"SELECT * FROM users WHERE id={user_id}")

# class ProductManager(Database):  # IS-A relationship
#     def __init__(self, connection_string):
#         super().__init__(connection_string)

#     def get_product(self, product_id):
#         return self.query(f"SELECT * FROM products WHERE id={product_id}")
#
#Issues:
#1. UserManager shouldn't be a subclass of Database - it could use Database method's instead (connect + query), but it's not an extended Database version, but rather it uses 2 methods from the Database.
#2. Same for ProductManager, there's no need to inherit Database class, but rather simply use the query method.
#3. And as for both - for these two subclasses, we could simply write two extra methods to the Database method and it would be much more nice and neat, if it's only about changing the product_id or user_id. It's just weird to invent a new class for that.


#Option 1 - IMHO very clear and not overengineered
# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

#     def get_user(self, user_id):
#         return (f"SELECT * FROM users WHERE id={user_id}")
    
#     def get_product(self, product_id):
#         return (f"SELECT * FROM products WHERE id={product_id}")


# #Option 2 - A bit more tricky but with perhaps clearer structure if we're planning to extend the new classes much further

# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

# class UserManager():  # IS-A relationship
#     def __init__(self, connection_string):
#         self.connection = Database(connection_string)

#     def get_user(self, user_id):
#         return self.connection.query(f"SELECT * FROM users WHERE id={user_id}")

# class ProductManager():  # IS-A relationship
#     def __init__(self, connection_string):
#         self.connection = Database(connection_string)

#     def get_product(self, product_id):
#         return self.connection.query(f"SELECT * FROM products WHERE id={product_id}")


#W2 D4 T1
# def process_data(value):
#     try:
#         result = 10 / value
#         data = [1, 2, 3]
#         print(data[value])
#     except ZeroDivisionError:
#         return "Zero error"
#     except IndexError:
#         return "Index error"
#     except Exception as e:
#         return f"Other: {e}"
#     else:
#         return "Success"
#     finally:
#         print("Cleanup")

# print(process_data(0))
# print(process_data(5))
# print(process_data(2))


# Output prediction:
#Zero error -> Cleanup
#Index error -> Cleanup
#Success -> Cleanup

# The exception order is arranged well, from specific to general.
# The else block only executes if we don't get any errors, and the finally block always executes.

#W2 D4 T2 - classmethod in position.py for calculating position size

#     @classmethod
#     def calculate_position_size(self,
#                                 account_balance: float,
#                                 position_type: str,
#                                 risk_percent: float, 
#                                 entry_price: float, 
#                                 stop_loss_price: float) -> float:
#         '''
#         A class method used to calculate the position size based on a set risk %,
#         with given position type and entry + stop loss
        
#         For now it uses a stop loss price - at some point I might decide to use distance instead - depends on our needs
#         '''
#         try:
#             usd_risk = account_balance * (risk_percent / 100)
            
#             if position_type.upper() == 'BUY':
#                 distance = abs(entry_price - stop_loss_price)
#             else:
#                 distance = abs(entry_price + stop_loss_price)
            
#             if distance != 0:
#                 position_size = usd_risk / distance
#                 return position_size
#             else:
#                 print('The stop loss is set at the entry price, returning 0')
#                 return 0
            
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')


# from algo_backtest.engine.position_manager import Position

# size = Position.calculate_position_size(10000, 'buy', 0.5, 50.0, 48.0)
# print(size)

#W4 D4 T3 - Output prediction - list comprehensions review

# prices = [100, 105, 98, 102, 110, 95]
# # A
# result_a = [p for p in prices if p > 100]
# # B
# result_b = [p * 2 if p > 100 else p for p in prices]
# # C
# result_c = [p for p in prices if p > 100 if p < 110]

# print(result_a) #-> [105, 102, 110] 
# print(result_b) #-> [100, 210, 98, 204, 220, 95]
# print(result_c) #-> [105, 102]

#W4 D4 T5 - bug fix

# def add_trade(trade, portfolio=[]): #This is the issue - mutable default parameter
#     portfolio.append(trade)
#     return portfolio

# result1 = add_trade("AAPL")
# result2 = add_trade("GOOGL")
# result3 = add_trade("MSFT", [])

# print(result1) 'AAPL'
# print(result2) 'AAPL, GOOGL'
# print(result3) 'MSFT'

#FIX:

# def add_trade(trade, portfolio = None): #This is the issue - mutable default parameter
    
#     if portfolio is None:
#         portfolio = []
#     portfolio.append(trade)
#     return portfolio

# result1 = add_trade("AAPL")
# result2 = add_trade("GOOGL")
# result3 = add_trade("MSFT", [])

# print(result1) #'AAPL'
# print(result2) #'AAPL, GOOGL'
# print(result3) #'MSFT'


#W2 D4 T8 - Code Review / Code Fix

# class RiskCalculator:
#     def __init__(self, account_balance):
#         self.account_balance = account_balance

#     def calculate_position_size(self, risk_percent, entry, stop_loss):
#         risk_dollars = self.account_balance * risk_percent  # Bug 1
#         distance = entry - stop_loss  # Bug 2
#         position_size = risk_dollars / distance  # Bug 3
#         return position_size

#     def get_risk_amount(risk_percent):  # Bug 4
#         return self.account_balance * (risk_percent / 100)

# # Test
# calc = RiskCalculator(10000)
# size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
# print(size)

# 1. No type hints/ docstrings
# 2. Lack of self in get_risk_amount method
# 3. That really depends on how we ask and present our data, but risk_percent and multiplying it by our acc balance like that might be tricky.
#If somebody gives the percent value like 5, we'd get our balance by 5 instead of 5% of our balance. But this depends, as we could also state percents as 0.05.
# 4. I've chosen more descriptive variants for entry and stop_loss



# class RiskCalculator:
#     '''Class used to calculate risk - both position size and the risk amount'''
    
    
    
    
#     def __init__(self, account_balance: float):
#         self.account_balance = account_balance
        
#     def calculate_position_size(self, 
#                                 risk_percent: float, 
#                                 entry_price: float, 
#                                 stop_loss_price: float) -> float:
        
#         '''Method used to calculate position size - check args, as this is IMPORTANT:
        
#         risk_percent - GIVE THE ACTUAL PERCENT VALUE here (e.g. 0.5 for 0.5%, 5 for 5%, 20 for 20%)
#         entry - provide the entry price e.g. 2053.43
#         stop_loss_price - as above,

        
#         '''
        
#         risk_dollars = self.account_balance * (risk_percent / 100)
#         distance = abs(entry_price - stop_loss_price)  #More descriptive variant + abs for both BUY/SELL
#         position_size = risk_dollars / distance  #This should be correct now if we assume that above is correct
#         return position_size

#     def get_risk_amount(self, risk_percent):
#         '''Get the risk amount per position'''
#         return self.account_balance * (risk_percent / 100)

# # Test
# calc = RiskCalculator(10000)
# size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
# print(size)

#W2 D5 T2 - Output prediction

# class Vehicle:
#     wheels = 4

#     def __init__(self, brand):
#         self.brand = brand

#     def describe(self):
#         return f"{self.brand} with {self.wheels} wheels"

# class Motorcycle(Vehicle):
#     wheels = 2

# class Car(Vehicle):
#     def __init__(self, brand, doors):
#         super().__init__(brand)
#         self.doors = doors

#     def describe(self):
#         return f"{super().describe()}, {self.doors} doors"

# # What prints?
# m = Motorcycle("Honda")
# c = Car("Toyota", 4)

# print(m.describe()) #-> Honda with 2 wheels
# print(c.describe()) #-> Toyota with 4 wheels, 4 doors
# print(m.wheels, c.wheels) #-> 2 4


#W2 D5 T3 - Predict the output
# def risky_operation(x):
#     try:
#         if x == 0:
#             raise ValueError("Zero not allowed")
#         result = 10 / x
#     except ValueError as e:
#         print(f"Caught: {e}")
#         return -1
#     except ZeroDivisionError:
#         print("Division by zero!")
#         return -2
#     else:
#         print(f"Success: {result}")
#         return result
#     finally:
#         print("Cleanup done")

# print(risky_operation(0))
# print("---")
# print(risky_operation(2))

# #1 - Caught: Zero not allowed. Cleanup done. -1
# #2 - Success: 5.0 Cleanup done. 5.0


#W2 D5 T4 - Output prediction

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

#     @staticmethod
#     def validate(value):
#         return value > 0

# print(Counter.get_count()) #0
# c1 = Counter() #2
# c2 = Counter() #2
# print(Counter.get_count()) #2
# print(c1.get_count()) #5
# print(Counter.validate(-5))#False
# print(c2.validate(10)) #True

'''

When we create actual class objects, the count value is increased with init.
As classmethod doesn't include actually creating any object, it doesn't use the init - it doesn't increase the count value, but it's obviously able to fetch it, and since it's a shared class attribute, we get the last value.

When creating a new class object (as c1, c2), we increase that count value by 1, as it's a shared class attribute.

'''

#W2 D5 T5

# from algo_backtest.engine.position import Position

# position_size = Position.calculate_position_size(10000, 2, 100, 95)
# print(position_size)
# position = Position('DAX', 'Buy', 25100, position_size, 24900, 25300)
# print(str(position))


#W2 D5 T7 - Bug fix

# class Strategy:
#     active_count = 0

#     def __init__(self, name):
#         self.name = name
#         active_count += 1  # Bug 1

#     @classmethod
#     def get_active(self):  # Bug 2
#         return cls.active_count

#     @staticmethod
#     def validate_name(name):
#         return len(name) > 0 and self.name.isalpha()  # Bug 3

#     def describe():  # Bug 4
#         return f"Strategy: {self.name}"
    
# #1. We will not increase active_count as it's in local scope
# #2 Class method CANNOT use self, it uses cls instead
# #3 static_method DOES NOT have access to class attributes, it's a self standing function only with its own attributes
# #4 Lack of self in describe method
# #5 - lack of docs/typehints - not a bug, but a bad practice

#FIXED VERSION BELOW:

# class Strategy:
#     '''Mock docstring'''
#     active_count = 0

#     def __init__(self, name: str):
#         self.name = name
#         Strategy.active_count += 1

#     @classmethod
#     def get_active(cls) -> int:  
#         '''Returns count of active strategies'''
#         return cls.active_count

#     @staticmethod
#     def validate_name(name) -> bool:
#         '''A standalone method/function that allows to validate any name'''
#         return len(name) > 0 and name.isalpha()

#     def describe(self) -> str:  
#         '''Returns the name of a given strategy'''
#         return f"Strategy: {self.name}"



#W3 D1 T2 - Output prediction

# class Secret:
#     def __init__(self):
#         self._protected = "visible"
#         self.__private = "hidden"

#     def reveal(self):
#         return self.__private

# s = Secret()
# print(s._protected) #visible
# print(s.reveal()) #hidden
# print(hasattr(s, '__private')) #False
# print(hasattr(s, '_Secret__private')) #True

#W3 D1 T3 - Output prediction

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius

#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32

# t = Temperature(25) 
# print(t.celsius) #25
# print(t.fahrenheit) # 77
# t.celsius = 30  # What happens here? Error - there's no such attribute as 'celsius' in the Temperature class.

#W3 D1 T4 - Code impl

# Create a `Price` class that:
# 1. Has a protected `_value` attribute
# 2. Has a `value` property (getter)
# 3. Has a `value` setter that validates: value must be >= 0
# 4. Raises `ValueError` with message "Price cannot be negative" if validation fails

# class Price:
#     '''A mock docstring of a mock class used for practice'''
    
#     def __init__(self, value: float):
#         self._value = value
    
#     @property
#     def value(self) -> float:
#         return self._value
    
#     @value.setter
#     def value(self, value: float) -> None:
#         if value >= 0:
#             self._value = value
#         else:
#             raise ValueError('Price cannot be negative!')


# # Test it:
# p = Price(100)
# print(p.value)      # Should print: 100
# p.value = 150       # Should work
# print(p.value)      # Should print: 150
# p.value = -10       # Should raise ValueError
#works.



#W3 D1 T5 -  modifying Trade class in algo_backtest/engine/trade.py - protected attributes, pnl as a property, is_winner property

# In practice.py - paste your test code and output
# from algo_backtest.engine.trade import Trade

# # Create a winning BUY trade
# t1 = Trade("AAPL", "buy", 100.0, 110.0, 10)
# print(t1)           # Should show: BUY AAPL: +100.00 (WIN)
# print(t1.pnl)       # Should show: 100.0
# print(t1.is_winner) # Should show: True

# # Create a losing SELL trade
# t2 = Trade("TSLA", "sell", 200.0, 220.0, 5)
# print(t2)           # Should show: SELL TSLA: -100.00 (LOSS)


#Updated Trade class pasted here as well:

# """Trade management for completed positions."""
# from typing import Optional

# class Trade:
#     '''
#     Represents a completed trade
    
#     Attributes:
#         ticker: Trading symbol.
#         side: 'BUY' or 'SELL'.
#         entry_price: Entry price.
#         exit_price: Exit price.
#         quantity: Number of units.
#         entry_time: Entry timestamp (string or datetime).
#         exit_time: Exit timestamp (string or datetime).
#         pnl: Profit/Loss (calculated automatically).
#         exit_reason: 'SL', 'TP', or 'MANUAL'.
#     '''
    
#     def __init__(self,
#                  ticker: str,
#                  side: str,
#                  entry_price: float,
#                  exit_price: float,
#                  quantity: float,
#                  entry_time: Optional[str] = None,
#                  exit_time: Optional[str] = None,
#                  exit_reason: Optional[str] = None
#                  ):
        
#         """Initialize a completed trade and calculate P&L."""
        
#         self._ticker = ticker
#         self._side = side.upper()
#         self._entry_price = entry_price
#         self._exit_price = exit_price
#         self._quantity = quantity
#         self._entry_time = entry_time
#         self._exit_time = exit_time
        
#         if exit_reason is not None:
#             self._exit_reason = exit_reason.upper()
#         else:
#             self._exit_reason = ''

#         #Properties - is_winner + pnl
#         self.__pnl: Optional[float] = None
#         self.__is_winner: Optional[bool] = None
        
#     def __str__(self):
#         """
#         User-friendly representation.

#         Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
#         Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
#         """
        
#         if self.is_winner == True:
#             result = '[WIN]'
#         else:
#             result = '[LOSS]'
        
#         return (f'''{result} {self._side} {self._quantity} {self._ticker}: 
#                 {self._entry_price} -> {self._exit_price} {self._exit_reason}
#                 | P&L: ${self.pnl:.2f}''')
    
#     def __repr__(self):
        
        
#         return (f'Trade(ticker = {self._ticker!r}, side = {self._side!r},'
#                 f'entry_price = {self._entry_price}, exit_price = {self._exit_price}'
#                 f'quantity = {self._quantity}, pnl = {self.pnl:.2f}, exit_reason = {self._exit_reason!r}'
#         )
    
    
#     @property
#     def pnl(self) -> float:
#         '''
#         Calculate profit/loss based on side.

#         Returns:
#             P&L in currency units.
#         '''
#         if self._side != 'BUY' and self._side != 'SELL':
#             print('Incorrect side, it should be either BUY or SELL (case insensitive)')
#             return None
#         elif self._exit_price < 0 or self._entry_price < 0:
#             print('Incorrect exit price or entry price, it should be above 0!')
#             return None
        
#         if self._side == 'BUY':
#             self.__pnl = (self._exit_price - self._entry_price) * self._quantity
#             return self.__pnl
#         elif self._side == 'SELL':
#             self.__pnl = (self._entry_price - self._exit_price) * self._quantity
#             return self.__pnl
        
#     @property 
#     def is_winner(self) -> bool:
#         """A property created to check if trade was profitable."""
#         if self.pnl > 0:
#             self.__is_winner = True
#         else:
#             self.__is_winner = False
            
#         return self.__is_winner
        
    
#     @classmethod
#     def calculate_win_rate(cls, trades: list['Trade']) -> float:
#         """
#         Calculate win rate from list of trades.

#         Args:
#             trades: List of Trade objects.

#         Returns:
#             Win rate as percentage (0-100).
#             Returns 0 if no trades.
#         """

#         if trades is not None:
#             trades_profits = [trade.pnl() for trade in trades]
#             winners = [profit for profit in trades_profits if profit > 0]
#             print(trades_profits)
#             return (len(winners) / len(trades_profits)) * 100
            
#         else:
#             return 0


#W3 D1 T6 - Property output prediction

# class Counter:
#     def __init__(self):
#         self._count = 0

#     @property
#     def count(self):
#         self._count += 1
#         return self._count

# c = Counter()
# print(c.count) #1
# print(c.count) #2
# print(c.count) #3


#W3 D1 T8 - it was supposed to be just a script to integrate Position with Trade,
#As a result of a natural flow I quickly moved to an idea of creating another class

# from typing import Optional
# from algo_backtest.engine.position import Position
# from algo_backtest.engine.trade import Trade


# class PositionTrade:
#     '''My practice class which integrates both Position and Trade classes
    
#        Mainly done for practice purposes for now, but we will see.
#     '''
    
#     def __init__(self,
#     acc_size: float,
#     risk_percent: float,
#     entry_price: float,
#     asset_name: str,
#     position_side: str,
#     sl: Optional[float] = None,
#     tp: Optional[float] = None,
#     ):
#         self.acc_size = acc_size
#         self.risk_percent = risk_percent
#         self.entry_price = entry_price
#         self.asset_name = asset_name
#         self.position_side = position_side
        
#         self.sl = sl
#         self.tp = tp
        
#         self.position = None
#         self.trade = None
        

#     def create_trade(self):
        
#         '''A method used to integrate the Position class and create an instance of an active position'''

#         try:
#             self.position_size = Position.calculate_position_size(self.acc_size, self.risk_percent, self.entry_price, self.sl)
#             self.position = Position(self.asset_name, self.position_side, self.entry_price, self.position_size, self.sl, self.tp)
            
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')
            
#     def check_trade(self, price):
        
#         '''A method used to check if the position should close and IF IT SHOULD, we integrate the Trade class'''
        
#         if self.position is not None and price > 0:
#             check, reason = self.position.should_close(price)
#             if check is True:
#                 print('Time to close the position!')
#                 self.trade = Trade(self.asset_name, self.position_side, self.entry_price, price, self.position_size, None, None, reason)
                
#                 print(self.trade)
#                 print(self.position)
#             else:
#                 print('Position still open')
#         else:
#             print('There is no position or the given price is below 0')
            
            

# x = PositionTrade(10000, 2, 50, 'DAX', 'Buy', 48, 55)
# x.create_trade()
# x.check_trade(55)


#W3 D2 T2 - random testing

# import random

# random.seed(100)
# a = random.randint(1, 10)

# random.seed(100)
# b = random.randint(1, 10)

# random.seed(200)
# c = random.randint(1, 10)

# print(a == b) #True
# print(a == c) #False


#W3 D2 T3

# class Percentage:
#     def __init__(self, value):
#         self._value = value
    
#     @property
#     def value(self):
#         return self._value
    
#     @value.setter
#     def value(self, setter):
#         if setter in range(0, 101):
#             self._value = setter
#         else:
#             raise ValueError('Percentage must be between 0 and 100!')
    
#     @property
#     def as_decimal(self):
#         return self._value / 100
    
# p = Percentage(50)
# print(p.value)      # 50
# print(p.as_decimal) # 0.5
# p.value = 75
# print(p.value)      # 75
# p.value = 150  

#W3 D2 T4 - before the attribute was unprotected and caused RecursionError

# class BadExample:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, new_value):
#         self._value = new_value

# obj = BadExample(10)


#W3 D2 T5 - updating the Trade class - added tp/sl as optional init values + risk_reward_ratio and return_percent as properties
# from algo_backtest.engine.trade import Trade

# trade = Trade(
#     ticker="EURUSD",
#     side="BUY",
#     entry_price=1.1000,
#     exit_price=1.1050,
#     quantity=10000,
#     stop_loss=1.0950,
#     take_profit=1.1100
# )
# print(f"P&L: ${trade.pnl:.2f}")
# print(f"Return: {trade.return_percent:.2f}%")
# print(f"R:R Ratio: {trade.risk_reward_ratio:.2f}")



#W3 D2 T6

# import random
# random.seed(42)
# result = random.choice(['A', 'B', 'C'])
# print(result)

# picks = [random.choice(items) for _ in range(3)]

# picks = random.sample(items, 3)

# import random
# prices = [random.randrange(0, 400) for i in range(10)]
# print(prices)
# sample = random.sample(prices, 3)
# print(sample)


# class Example:
#     def __init__(self):
#         self.__data = [1, 2, 3]

#     @property
#     def data(self):
#         return self.__data

# e = Example()
# e.data.append(4)
# print(len(e.data))

#W3 D2 T8 - Risk Validator class

# from typing import Tuple

# class RiskValidator:
    
#     def __init__(self, max_risk_percent: float, max_position_size: float):
        
#         self.__max_risk_percent = max_risk_percent
#         self.__max_position_size = max_position_size
        
#     @property
#     def max_risk_percent(self) -> float:
#         '''Property max_risk_percent with validation'''
#         if self.__max_risk_percent < 0.1 or self.__max_risk_percent > 10:
#             raise ValueError('Max risk percent should be between 0.1 and 10.0!')
#         else:
#             return self.__max_risk_percent

#     @property
#     def max_position_size(self) -> float:
#         '''Property max_position_size with validation'''
#         if self.__max_position_size < 0:
#             raise ValueError('Max position size should be above 0!')
#         else:
#             return self.__max_position_size
        
#     def validate_position(self, position) -> Tuple[bool, str]:
#         if position.quantity > self.__max_position_size:
#             return (False, 'Position size exceeds maximum')
#         else:
#             return (True, 'Position valid!')
        

# validator = RiskValidator(max_risk_percent=2.0, max_position_size=100.0)
# print(validator.max_risk_percent)  # 2.0


# from algo_backtest.engine.position import Position

# large_position = Position(
#     ticker="AAPL",
#     side="BUY",
#     quantity=150.0,
#     entry_price=150.0
# )


# valid, message = validator.validate_position(large_position)
# print(f"Valid: {valid}, Message: {message}")


#W3 D2 T9 - Random trade generator

# import random
# from typing import List
# from algo_backtest.engine.trade import Trade

# def generate_random_trades(n: int, tickers: List[str]) -> List[Trade]:
#     '''A function used to generate a number of random trades
    
#     Args: 
#     n - the number of trades you want to generate
#     tickers - the list of tickers you want to use in the generator
    
#     Returns:
#     - a list of generated trades
#     '''
    
#     trades = []
    
#     for i in range(n):
#         ticker = random.choice(tickers)
#         side = random.choice(['BUY', 'SELL'])
#         entry_price = random.uniform(120.0, 200.0)
#         exit_price = entry_price * random.uniform(0.95, 1.05)
#         quantity = random.randint(1, 100)
        
#         trade = Trade(ticker, side, entry_price, exit_price, quantity)
#         trades.append(trade)
        
#     return trades


# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
# trades = generate_random_trades(5, tickers)
# for trade in trades:
#     print(trade)

#W3 D3 T1

# try:
#     x = int("abc")
# except Exception as e:
#     print(type(e).__name__)
    
#W3 D3 T2

# class BankAccount:
#     def __init__(self, owner: str, initial_balance: float = 0.0):
#         self.__owner = owner
#         self.initial_balance = initial_balance
#         self.__balance = self.initial_balance
        
#     def __str__(self):
#         return f'{__class__.__name__}(owner = {self.__owner}, balance = {self.__balance})'
        
#     @property
#     def owner(self) -> str:
#         return self.__owner
    
#     @property
#     def balance(self) -> float:
#         if self.initial_balance < 0:
#             raise ValueError('Initial balance cannot be below 0!')
#         else:
#             return self.__balance
        
#     def deposit(self, amount: float):
#         self.__balance += amount
    
#     def withdraw(self, amount: float):
#         if amount > self.__balance:
#             print(f'The current balance is lower than the amount you want to withdraw!')
#             return False
#         else:
#             self.__balance -= amount
#             print(f'Successfully withdrawn ${amount:.2f} from the account.')
#             return True
    
    
    
# acc = BankAccount("Alice", 100.0)
# print(acc.owner)          # Alice
# print(acc.balance)        # 100.0
# acc.deposit(50.0)
# print(acc.balance)        # 150.0
# success = acc.withdraw(200.0)
# print(success)            # False (insufficient funds)
# print(acc.balance)        # 150.0 (unchanged)
# acc.owner = "Bob"         # AttributeError (read-only)
# print(acc)


#W3 D3 T3

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         '''Simplified string representation if anybody wants to print a class instance'''
#         return f'{__class__.__name__} at ({self.x}, {self.y})'
    
#     def __repr__(self) -> str:
#         '''Unambigous representation for devs'''
#         return f'{__class__.__name__!r}(x = {self.x}, y = {self.y})'
    
    

# p = Point(3, 5)
# print(p)           # Which method? str
# print([p])         # Which method?
# print(f"{p}")      # Which method?
# print(f"{p!r}")    # Which method? -> repr

#W3 D3 T4

# from typing import List
# from algo_backtest.engine.trade import Trade

# class TradeManager:
#     '''Mock class used to manage trades with the Trade class, we can calculate the win rate, total pnl etc.
#        Requires Trade class import from algo_backtest/engine/trade.py'''
    
#     def __init__(self):
#         self._trades = []
#         self.__total_pnl: float = 0.0
#         self.__win_rate: float = 0.0
#         self.__trade_count: int = 0
        
#         self.winning_trades = 0
        
#     def __len__(self):
#         '''Length dunder method'''
#         return len(self._trades)

#     def __iter__(self):
#         '''Iter dunder method, making the objects in the TradeManager iterable'''
#         return iter(self._trades)
    
#     @property 
#     def trade_count(self):
#         return self.__trade_count
    
#     @property
#     def total_pnl(self):
#         return self.__total_pnl
    
#     @property
#     def win_rate(self):
#         self.__win_rate = (self.winning_trades / self.__trade_count * 100)
#         return self.__win_rate
        
    
#     def add_trade(self, trade: Trade) -> None:
#         '''A method used to add trades created with a Trade class'''
#         self._trades.append(trade)
#         self.__trade_count += 1
#         self.__total_pnl += trade.pnl
#         if trade.pnl > 0:
#             self.winning_trades += 1
        
#     def remove_trade(self, ticker: str) -> bool:
#         '''A method used to remove trades and return a T/F'''
#         for trade in self._trades:
#             if trade.ticker == ticker:
#                 self._trades.remove(trade)
#                 return True
#         print('Did not find a trade with requested ticker')
#         return False

#     def get_trades_by_side(self, side: str) -> List[Trade]:
#         '''Gets all of the trades that are either 'BUY' or 'SELL' '''
#         filtered_trades = []
        
#         for trade in self._trades:
#             if trade.side == side:
#                 filtered_trades.append(trade)
        
#         return filtered_trades



# manager = TradeManager()
# manager.add_trade(Trade("AAPL", "BUY", 100, 110, 10))   # +100 PnL
# manager.add_trade(Trade("GOOGL", "SELL", 200, 190, 5))  # +50 PnL
# manager.add_trade(Trade("MSFT", "BUY", 50, 45, 20))     # -100 PnL

# print(f"Total P&L: ${manager.total_pnl:.2f}")  # $50.00
# print(f"Win Rate: {manager.win_rate:.1f}%")    # 66.7%
# print(f"Trade Count: {manager.trade_count}")   # 3
# print(f"Length: {len(manager)}")               # 3

# for trade in manager:
#     print(trade)

#W3 D3 T5
# class A:
#     def __init__(self):
#         self.x = 1

# class B(A):
#     def __init__(self):
#         self.y = 2

# b = B()
# print(hasattr(b, 'x'), hasattr(b, 'y'))


# class MyClass:
#     @property
#     def value(self):
#         return self._value

# obj = MyClass()
# print(obj.value) #Attribute Error - object has no attribute '_value'

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1
#         self.id = Counter.count

# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(c1.id, c2.id, c3.id)

#W3 D3 T6 - Debugging

#Original:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self._price = price

#     @property
#     def price(self):
#         return self.price  # Bug 1

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self._price = value
#         # Bug 2: What if value <= 0?

#     def apply_discount(self, percent):
#         self._price = self._price * (1 - percent)  # Bug 3

#     def __str__(self)
#         return f"Product: {self.name}, ${self._price}"  # Bug 4
    
    
    # 1. Wrong property name
    # 2. We aren't properly handling negative values here, which should be the msot logical step
    # 3. Whatever number we put as percent here (if it's an integer), we'd end up with a negative number most likely
    # 4. Lack of :
    
    #Fixed version:
    
    
# class Product:
#     '''Mock class for exercise purpose'''
#     def __init__(self, name: str, price: float):
#         self.name = name
#         self._price = price
    
#     def __str__(self):
#         return f'Product: {self.name}, ${self._price}'    
    
#     @property
#     def price(self):
#         if self._price < 0:
#             raise ValueError('Price cannot be negative!')
#         else:
#             return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be negative!')
#         else:
#             self._price = value
            
#     def apply_discount(self, percent):
#         self._price = self._price * (1 - percent / 100)


#W3 D3 T7 - dunder methods hash + eq added to  algo_backtest/engine/position.py

# from algo_backtest.engine.position import Position

# p1 = Position("AAPL", "BUY", 100.0, 10)
# p2 = Position("AAPL", "BUY", 100.0, 10)
# p3 = Position("AAPL", "SELL", 100.0, 10)

# print(p1 == p2)  # True
# print(p1 == p3)  # False

# # Can use in set
# positions = {p1, p2, p3}
# print(len(positions))  # 2 (p1 and p2 are duplicates)
# print(positions)

#W3 D3 T8 - Mutable def argument trap

# def add_item(item, items=[]):
#     items.append(item)
#     return items

# print(add_item("a"))
# print(add_item("b"))
# print(add_item("c"))

#Q1 Base Output:
#[a], [a, b], [a, b, c]

#Fixed version:
# from typing import List

# def add_item(item: str, items: List = None) -> List:
    
#     if items is None:
#         items = []
#     items.append(item)
#     return items

# print(add_item("a"))
# print(add_item("b"))
# print(add_item("c"))

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr)

#W3 D4 T1


# class Parent:
#     def __init__(self):
#         self.x = 1
#         print("Parent __init__ ran")

# class Child(Parent):
#     def __init__(self):
#         super().__init__() #WITHOUT THIS LINE WE'D GET AN ATTRIBUTE ERROR - parent's init doesn't RUN AUTOMATICALLY
#         self.y = 2
#         print("Child __init__ ran")
        

# c = Child()
# # Output: "Child __init__ ran"  (Parent never ran!)

# print(c.y)  # 2 - works
# print(c.x)  # AttributeError: 'Child' has no attribute 'x'



### Example 3: NO `__init__` in Child -> The INIT inheritance is automatic!

# class Parent:
#     def __init__(self):
#         self.x = 1
#         print("Parent __init__ ran")

# class Child(Parent):
#     pass  # No __init__ defined

# c = Child()
# # Output: "Parent __init__ ran"  (Automatically uses Parent's!)

# print(c.x)  # 1 - works!


#W4 D4 T2 - creating child class for the Base class Account:


# class Account:
#     def __init__(self, owner: str, balance: float = 0.0):
#         self._owner = owner
#         self._balance = balance

#     @property
#     def balance(self) -> float:
#         return self._balance

#     def deposit(self, amount: float) -> None:
#         if amount > 0:
#             self._balance += amount



# class MarginAccount(Account):
#     '''A child class with margin and buying power added'''

#     def __init__(self, owner: str, balance: float, leverage: float):
#         super().__init__(owner, balance)
#         self._leverage = leverage
#         self._buying_power = 0.0
        
#     def __str__(self):
#         return f'{__class__.__name__}(owner = {self._owner}, balance = {self._balance}, leverage = {self._leverage})'
    
#     @property
#     def buying_power(self) -> float:
#         '''A property that calculates the current buying power'''
#         self._buying_power = self._leverage * self._balance
#         return self._buying_power
    
#     @property
#     def leverage(self) -> float:
#         '''A property that describes leverage (read-only)'''
#         return self._leverage


# acc = MarginAccount("Alice", 1000.0, leverage=2.0)
# print(acc.balance)       # 1000.0
# print(acc.leverage)      # 2.0
# print(acc.buying_power)  # 2000.0
# acc.deposit(500)
# print(acc.buying_power)  # 3000.0
# print(acc)               # MarginAccount(owner='Alice', balance=1500.00, leverage=2.0)


#W4 D4 T4 - price generator function

# import random

# def price_generator(start_price: float, num_ticks: int, volatility: int = 5):
#     """
#     Generate simulated price ticks.

#     Args:
#         start_price: Starting price
#         num_ticks: Number of price updates to generate
#         volatility: Max percentage change per tick (1 = 1%)

#     Yields:
#         float: Next price value
#     """

#     prices = []
#     for i in range(num_ticks):
#         price = start_price * (1 - (random.uniform(-volatility, volatility) / 100))
#         prices.append(price)
    
#     return prices


# prices = price_generator(100, 10, 5)
# print(prices)

# class Parent:
#     class_var = "parent"

# class Child(Parent):
#     pass

# Child.class_var = "child"
# print(Parent.class_var, Child.class_var)


#W3 D4 T6  - DEBUGGING

# class Vehicle:
#     def __init__(self, brand: str, year: int):
#         self.brand = brand
#         self.year = year

#     def info(self) -> str:
#         return f"{self.year} {self.brand}"

# class Car(Vehicle):
#     def __init__(self, brand: str, year: int, doors: int):
#         super().__init__(brand, year)
#         self.doors = doors

#     def info(self) -> str:
#         return f"{super().info()} with {self.doors} doors"

# car = Car("Toyota", 2020, 4)
# print(car.info())  # Expected: "2020 Toyota with 4 doors"

# #The child class has init, so it won't automatically inherit the attributes from the parent class,
# #yet it doesn't use the super().__init__() so it won't actually be able to ge the brand, and year attributes.

#W3 D5 T1

# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))

# def simple():
#     yield 1

# g = simple()
# next(g)
# next(g)  # What happens here?



#W3 D5 T2

# def countdown(n):
#     for num in range(n, 0, -1): #I assume we want to include 1
#         yield num

# # Test it:
# for num in countdown(5):
#     print(num)


#W3 D5 T3
# A) Convert this list comprehension to a generator expression
# squares_list = [x**2 for x in range(10)]

# # Your generator expression (hint: change [ ] to ( ))
# squares_gen = (x ** 2 for x in range (10))

# # B) Convert this filtered list comprehension to a generator expression
# evens_list = [x for x in range(20) if x % 2 == 0]

# # Your generator expression:
# evens_gen = (x for x in range (20) if x % 2 == 0)

# # C) Predict the output:
# gen = (x * 2 for x in [1, 2, 3])
# print(next(gen)) # 2
# print(next(gen)) # 4
# print(list(gen))  # What remains? [6]


#W3 D5 T4

# import random

# def price_ticks(start_price: float, num_ticks: int):
#     """
#     Generate simulated price movements.

#     Each tick moves the price by -1% to +1% randomly.

#     Args:
#         start_price: Starting price
#         num_ticks: Number of prices to generate

#     Yields:
#         float: Each new price (rounded to 2 decimals)
#     """

#     for num in range(num_ticks):
#         exit_price = round(random.uniform(start_price * 0.99, start_price * 1.01), 2)
#         yield exit_price

# # Test:
# random.seed(42)  # For reproducible results
# for price in price_ticks(100.0, 5):
#     print(f"${price:.2f}")

#W3 D5 T5


# class Portfolio:
#     """
#     A portfolio that holds cash and tracks transactions.

#     Requirements:
#     1. __init__(self, initial_cash: float) - store as _cash (protected)
#     2. cash property (read-only) - returns current cash
#     3. _transactions list (protected) - stores all deposit/withdrawal amounts
#     4. deposit(amount) - adds to cash, appends amount to transactions
#     5. withdraw(amount) - subtracts from cash (raise ValueError if insufficient), appends negative amount
#     6. __len__ - returns number of transactions
#     7. __iter__ - iterates over transactions
#     8. __str__ - returns "Portfolio: $X.XX (N transactions)"
#     """

#     def __init__(self, initial_cash: float):
#         self._cash = initial_cash
#         self._transactions_list = []
        
#     def __str__(self) -> str:
#         return f'{__class__.__name__}: ${self._cash:.2f}, ({len(self._transactions_list)} transactions)'
        
#     def __len__(self) -> int:
#         '''Dunder method that allows to check the current length of the transactions list'''
#         return len(self._transactions_list)
    
#     def __iter__(self) -> iter:
#         '''Dunder method that allows us to iterate over transactions'''
#         return iter(self._transactions_list)
        
#     @property
#     def cash(self) -> float:
#         '''A read-only property which returns the current amount of cash'''
#         return self._cash
    
    
#     def deposit(self, amount):
#         '''A method used to deposit any positive amount into our account'''
#         if amount < 0:
#             raise ValueError('The deposited amount has to be above 0!')
#         else:
#             self._cash += amount
#             self._transactions_list.append(('deposit', amount))
    
#     def withdraw(self, amount):
#         '''A method used to withdraw funds if there is a sufficient amount available'''
#         if amount > self._cash:
#             raise ValueError('Deposit impossible, not enough funds')
#         else:
#             self._cash -= amount
#             self._transactions_list.append(('withdraw', -amount))
    
    

# # Test:
# p = Portfolio(1000.0)
# p.deposit(500.0)
# p.withdraw(200.0)
# print(p)              # Portfolio: $1300.00 (2 transactions)
# print(len(p))         # 2
# for t in p:
#     print(t)          # Should print: 500.0, then -200.0


#W3 D5 T6

# gen = (x for x in [1, 2, 3])
# list(gen)  # Consumes it
# for item in gen:
#     print(item) #Prints nothing, empty loop

# def gen():
#     yield 1
#     return "done"
#     yield 2

# g = gen()
# print(next(g))
# print(next(g)) -> Stop iteration error


#W3 D5 T7 - error fix

# def even_numbers(limit):
#     """Generate even numbers from 0 up to (not including) limit."""
#     n = 0
#     while n < limit:
#         if n % 2 == 0:
#             return n  # BUG - IT WILL STOP THE LOOP
#         n += 1
        
        

# def even_numbers(limit):
#     """Generate even numbers from 0 up to (not including) limit."""
#     n = 0
#     while n < limit:
#         if n % 2 == 0:
#             yield n  # BUG - IT WILL STOP THE LOOP
#         n += 1
        
# for num in even_numbers(10):
#     print(num)
# # Should print: 0, 2, 4, 6, 8



#W3 D5 T8

# import random

# class SimpleTradeManager:
#     """Simplified version for this exercise."""

#     def __init__(self):
#         self._trades = []  # List of (ticker, pnl) tuples

#     def add_trade(self, ticker: str, pnl: float):
#         self._trades.append((ticker, pnl))

#     def profitable_trades(self):
#         """
#         Generator that yields only profitable trades.

#         Yields:
#             tuple: (ticker, pnl) where pnl > 0
#         """
        
#         profitable_trades = ((trade[0], trade[1]) for trade in self._trades if trade[1] > 0)
#         return profitable_trades
        

# # Test:
# tm = SimpleTradeManager()
# tm.add_trade("AAPL", 100.0)
# tm.add_trade("GOOGL", -50.0)
# tm.add_trade("MSFT", 200.0)
# tm.add_trade("TSLA", -75.0)

# print("Profitable trades:")
# for ticker, pnl in tm.profitable_trades():
#     print(f"  {ticker}: ${pnl}")



#Start 12:30
#W4 D1 T1

# def count():
#     n = 0
#     while True:
#         yield n
#         n += 1

# c = count()
# print(next(c), next(c), next(c))


# try:
#     x = int("abc")
# except ValueError:
#     print("V", end=" ")
# except TypeError:
#     print("T", end=" ")
# else:
#     print("E", end=" ")
# finally:
#     print("F")

# import sys

# print(sys.argv[0])

# class A:
#     def method(self):
#         return "instance"

#     @classmethod
#     def method(cls):
#         return "class"

# a = A()
# print(a.method())


# class A:
#     def __init__(self):
#         self._x = 0

#     @property
#     def x(self):
#         return self._x

# a = A()
# a.x = 10
# print(a.x) #AttributeError - brak settera


# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# print(issubclass(C, A)) #True 


# gen = (i for i in range(3))  # [0, 1, 2]
# for _ in range(2):
#     print(next(gen), end=" ")  # Prints: 0 1 
# for x in gen:
#     print(x, end=" ")          # Prints: 2 (only one left!)


#W4 D1 T2

# classify = lambda x: 'positive' if x > 0 else 'zero' if x == 0 else 'negative'

# print(classify(5))   # "positive"
# print(classify(-3))  # "negative"
# print(classify(0))   # "zero"

#W4 D1 T3
# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x ** 2, numbers)
# print(result)
# print(list(result))


# celsius = [0, 10, 20, 30, 40]
# # Formula: F = C * 9/5 + 32

# fahrenheit = list(map(lambda x: x * (9/5) + 32, celsius))
# print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]



# a = [1, 2, 3]
# b = [10, 20, 30]
# result = list(map(lambda x, y: x + y, a, b))
# print(result)

#W4 D1 T4 - filter practice


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))


# words = ["hi", "hello", "bye", "goodbye", "ok", "python"]
# long_words = list(filter(lambda x: len(x) > 3, words))
# print(long_words)  # ['hello', 'goodbye', 'python']


# items = [0, 1, "", "hello", None, 42, [], [1, 2]]
# truthy = list(filter(None, items))
# print(truthy)



#W4 D1 T5 - lambda sorting


# pairs = [(1, 'c'), (2, 'a'), (3, 'b')]
# pairs.sort(key = lambda x: x[1])
# print(pairs)  # [(2, 'a'), (3, 'b'), (1, 'c')]


# products = [
#     {'name': 'Apple', 'price': 1.50},
#     {'name': 'Banana', 'price': 0.75},
#     {'name': 'Cherry', 'price': 2.00}
# ]
# products.sort(key = lambda x: x['price'])
# print([p['name'] for p in products])  # ['Banana', 'Apple', 'Cherry']


# words = ["python", "java", "c", "javascript"]
# words.sort(key = lambda x: len(x))
# print(words)  # ['c', 'java', 'python', 'javascript']


#W4 D1 T6 - lambda filtering

# trades = [
#     ("AAPL", 150.0, "BUY"),
#     ("GOOGL", -50.0, "SELL"),
#     ("MSFT", 200.0, "BUY"),
#     ("TSLA", -100.0, "BUY"),
#     ("AMZN", 75.0, "SELL"),
#     ("META", -25.0, "SELL"),
# ]

# # 1. Filter profitable trades (pnl > 0)
# profitable = list(filter(lambda x: x[1] > 0, trades))
# print("Profitable:", profitable)

# # 2. Filter BUY trades only
# buys = list(filter(lambda x: x[2] == 'BUY', trades))
# print("BUY trades:", buys)

# # 3. Filter profitable BUY trades (combine conditions)
# profitable_buys = list(filter(lambda x: x[2] == 'BUY' and x[1] > 0, trades))
# print("Profitable BUYs:", profitable_buys)

#W4 D1 T7
# result = list(filter(lambda x: x, [0, 1, 2, '', 'a']))
# print(result)

#W4 D1 T8
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Step 1: Filter to keep only even numbers
# # Step 2: Square each remaining number
# # Result should be: [4, 16, 36, 64, 100]

# even_nums = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_nums)
# squared = list(map(lambda x : x ** 2, even_nums))
# print(squared)

# #Bonus - the same thing using list comprehensions

# squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
# print(squared_evens)

#finish 13:51


#9:53
#W4 D2 T1

# def outer():
#     message = "Hello"
#     def inner():
#         return message
#     return inner

# greet = outer()
# print(greet())

#W4 D2 T2


# def make_counter(start=0):
#     """
#     Create a counter that remembers its count.

#     Args:
#         start: Initial count value (default 0)

#     Returns:
#         A function that increments and returns the count
#     """
#     # Your code here
    
#     counter = start

#     def increase_counter():
#         nonlocal counter 
#         counter += 1
#         return counter
    
#     return increase_counter

# # Test:
# counter_a = make_counter(0)
# counter_b = make_counter(100)

# print(counter_a())  # 1
# print(counter_a())  # 2
# print(counter_a())  # 3

# print(counter_b())  # 101
# print(counter_b())  # 102


#W4 D2 T3

# x = 10

# def outer():
#     x = 20

#     def inner():
#         nonlocal x
#         x = 30

#     inner()
#     print("outer x:", x)

# outer()
# print("global x:", x)


#30, 10


#W4 D2 T4 - Late Binding Trap
    
# functions = []
# for i in range(3):
#     functions.append(lambda: i)

# print(functions[0]())
# print(functions[1]())
# print(functions[2]())
# print(functions)
#We'd get 2 as an output in every single case

# functions = []
# functions = [i for i in range(3)]

# print(functions[0])
# print(functions[1])
# print(functions[2]())
# print(functions)


#W4 D2 T5

# def make_price_validator(min_price: float, max_price: float):
#     """
#     Create a price validator function.

#     Args:
#         min_price: Minimum acceptable price
#         max_price: Maximum acceptable price

#     Returns:
#         A function that takes a price and returns (is_valid, message)
#     """

#     min_price = min_price
#     max_price = max_price
    
#     def validate_price(price):
#         nonlocal min_price
#         nonlocal max_price
        
#         if price > min_price and price < max_price:
#             print(f'Price {price:.2f} is valid')
#             return True
#         else:
#             print(f'Price {price:.2f} is invalid!')
#             return False
        
#     return validate_price
    
    
# # Test:
# validate_stock = make_price_validator(0.01, 10000.0)
# validate_crypto = make_price_validator(0.0001, 100000.0)

# print(validate_stock(150.50))     # (True, "Price 150.5 is valid")
# print(validate_stock(-5.0))       # (False, "Price -5.0 below minimum 0.01")
# print(validate_stock(50000.0))    # (False, "Price 50000.0 above maximum 10000.0")

# print(validate_crypto(0.00001))   # (False, "Price 1e-05 below minimum 0.0001")
# print(validate_crypto(45000.0))   # (True, "Price 45000.0 is valid")


#W4 D2 T7

# def make_trade_logger(prefix: str):
#     """
#     Create a trade logger with a specific prefix.

#     The logger should also track the total number of trades logged.

#     Args:
#         prefix: String prefix for log messages (e.g., "INFO", "TRADE")

#     Returns:
#         A tuple of (log_trade, get_count) functions
#     """
#     # Your code here
#     prefix = prefix
#     trades = []
    
#     def add_trade(ticker: str, side: str, price: float):
#         nonlocal prefix
#         trades.append([prefix, ticker, side, price])
#         print(f'[{prefix}] {ticker} {side} @ ${price:.2f}')
           
#     def get_count():
#         return len(trades)
    
#     return add_trade, get_count
    
# # Test:
# log_trade, get_count = make_trade_logger("TRADE")

# log_trade("AAPL", "BUY", 150.0)   # [TRADE] AAPL BUY @ $150.00
# log_trade("GOOGL", "SELL", 2800.0) # [TRADE] GOOGL SELL @ $2800.00
# log_trade("MSFT", "BUY", 300.0)   # [TRADE] MSFT BUY @ $300.00

# print(f"Total trades: {get_count()}")  # Total trades: 3

# # Create another logger with different prefix
# log_error, error_count = make_trade_logger("ERROR")
# log_error("TSLA", "FAILED", 0.0)  # [ERROR] TSLA FAILED @ $0.00
# print(f"Errors: {error_count()}")  # Errors: 1

#Start 10:06
#W4 D3 T1

# numbers = [1, 2, 3, 4]
# result = reduce(lambda acc, x: acc + x, numbers)
# print(result)


# numbers = [1, 2, 3, 4]
# result = reduce(lambda acc, x: acc * x, numbers)
# print(result)

# numbers = [1, 2, 3]
# result = reduce(lambda acc, x: acc + x, numbers, 10)
# print(result)

# words = ["a", "b", "c"]
# result = reduce(lambda acc, x: acc + x, words)
# print(result)

#W4 D3 T2 - reduce practice

# from functools import reduce

# numbers = [2, 3, 4, 5]
# calc = reduce(lambda acc, x: acc * x, numbers)
# print(calc)


# numbers = [3, 7, 2, 9, 4]
# maximum = reduce(lambda acc, x: x if x > acc else acc, numbers)
# print(maximum)


# nested = [[1, 2], [3, 4], [5, 6]]
# flattened = reduce(lambda acc, x: acc + x if type(x) == list else x, nested)
# print(flattened)

#W4 D3 T3 decorator basics

# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @my_decorator
# def say_hi():
#     print("Hi!")

# say_hi()


# def double_result(func):
#     def wrapper(x):
#         return func(x) * 2
#     return wrapper

# @double_result
# def add_ten(n):
#     return n + 10

# print(add_ten(5))


#W4 D3 T4 - Decorator continuation

# def announce(func):
#     '''A decorator that wraps a function which prints 'Executing' before calling the function'''
    
#     def wrapper(*args, **kwargs):
#         print(f'Executing...')
#         func(*args, **kwargs) 
#         return func(*args, **kwargs)
    
#     return wrapper

# @announce
# def greet(name: str):
#     print(f'Hello, {name}')
    
# @announce
# def add(a, b):
#     return a + b

# greet("Alice")
# result = add(3, 5)
# print(result)



#W4 D3 T5 - reduce practice

# trades = [
#     {"ticker": "AAPL", "pnl": 150.0},
#     {"ticker": "GOOGL", "pnl": -50.0},
#     {"ticker": "MSFT", "pnl": 200.0},
#     {"ticker": "TSLA", "pnl": -100.0},
#     {"ticker": "NVDA", "pnl": 300.0},
# ]

# # Part A: Calculate total PnL using reduce
# total_pnl = reduce(lambda acc, value: acc + value['pnl'], trades, 0)
# print(f"Total PnL: ${total_pnl}")  # Total PnL: $500.0
# #Tutaj kluczowe było dodanie 0 jako wartości startowej, bo inaczej nie mogłem tego chwycić i wyskakiwały TypeErrory!


# # Part B: Count winning trades using reduce
# win_count = reduce(lambda acc, trade: acc + 1 if trade['pnl'] > 0 else acc, trades, 0)
# print(f"Winning trades: {win_count}")  # Winning trades: 3

# # Part C: Find the best trade (highest pnl) using reduce
# best_trade = reduce(lambda acc, trade: acc if acc['pnl'] > trade['pnl'] else trade, trades)
# print(f"Best trade: {best_trade['ticker']} with ${best_trade['pnl']}")
# # Best trade: NVDA with $300.0


#W4 D3 T6
# def decorator(func):
#     def wrapper(*args):
#         return func(*args) + 10
#     return wrapper

# @decorator
# def multiply(a, b):
#     return a * b

# print(multiply(3, 4))

#W4 D3 T7 - Building a decorator

# def log_call(func):
#     """
#     Decorator that prints the function name and arguments when called.

#     Example output:
#     Calling calculate_pnl(entry=100, exit=110, qty=10)
#     """
#     def wrapper(*args, **kwargs):
#         print(f'Executing {func.__name__}({*args, *kwargs})')
#         return func(*args, **kwargs)
    
#     return wrapper

# # Test:
# @log_call
# def calculate_pnl(entry: float, exit: float, qty: float) -> float:
#     return (exit - entry) * qty

# @log_call
# def is_winner(pnl: float) -> bool:
#     return pnl > 0


# result = calculate_pnl(100.0, 110.0, 10.0)
# # Expected: Calling calculate_pnl(100.0, 110.0, 10.0)
# print(f"PnL: {result}")  # PnL: 100.0
# win = is_winner(result)
# # Expected: Calling is_winner(100.0)
# print(f"Winner: {win}")  # Winner: True


#W4 D3 T8 - combined lambda, map, filter, reduce

# trades = [
#     {"ticker": "AAPL", "side": "BUY", "entry": 150, "exit": 160, "qty": 10},
#     {"ticker": "GOOGL", "side": "SELL", "entry": 2800, "exit": 2750, "qty": 5},
#     {"ticker": "MSFT", "side": "BUY", "entry": 300, "exit": 290, "qty": 20},
#     {"ticker": "TSLA", "side": "BUY", "entry": 700, "exit": 750, "qty": 8},
#     {"ticker": "NVDA", "side": "SELL", "entry": 500, "exit": 480, "qty": 15},
# ]

# # Step 1: Calculate PnL for each trade using map
# # Step 2: Filter only winning trades using filter
# # Step 3: Calculate total winning PnL using reduce

# trades_with_pnl = list(map(
#     lambda t: {**t, "pnl": (t['exit'] - t['entry']) * t['qty']} if t['side'] == 'BUY' else
#     {**t, "pnl": (t['entry'] - t['exit']) * t['qty']},
#     trades
# ))

# print(trades_with_pnl)


# winning_trades = list(filter(lambda t: t if t['pnl'] > 0 else 0, trades_with_pnl))
# print(winning_trades)

# total_winning_pnl = reduce(lambda acc, t: acc + t['pnl'], winning_trades, 0)


# print(f"Winning trades: {len(winning_trades)}")
# print(f"Total winning PnL: ${total_winning_pnl}")

#Below is a quick recap of string operations, since I'm also following the Edube course from Python Institute (PCAP preparation)
#I'm familiar with these concepts, but a little review didn't harm anyone

# str1 = 'a'
# str2 = 'b'

# print(str1 + str2) #'ab'
# print(str2 + str1) # 'ba
# print(5 * 'a') #aaaaa
# print('b' * 4) #bbbb


# print(ord('a')) #using the ord() we can print the code point of a given symbol (ASCII)

# print(chr(97)) #using the chr() function, we can take a code point and return a character
# print(chr(945))

# print(chr(ord('x')) == 'x') #True


# the_string = 'silly walks'

# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ')
    

# alpha = "abdefg"

# print(alpha[1:3]) #bd
# print(alpha[3:]) #efg
# print(alpha[:3]) #abd
# print(alpha[3:-2]) #e
# print(alpha[-3:4]) #e
# print(alpha[::2]) #adf
# print(alpha[1::2]) #beg

#Remember that PYTHON STRINGS ARE IMMUTABLE

#WE CANNOT USE append, insert etc.
#We can only use del to remove the string as a WHOLE!


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# #del alphabet[0] #ERROR!
# print(alphabet)
# del(alphabet) #WE CAN DELETE THE WHOLE STRING
# print(alphabet) #Now this won't work, as we've deleted the string


# alphabet = "bcdefghijklmnopqrstuvwxy"
# alphabet = "a" + alphabet
# alphabet = alphabet + "z" #works well

# print(alphabet)


#WE CAN ALSO USE index() method to find the index of a specific element specified in index's argument
# alphabet = "bcdefghijklmnopqrstuvwxy"
# print(alphabet.index('p'))
# print(alphabet.index('a')) #Value absent - RETURNS A VALUEERROR!

# print("Alpha".capitalize()) #Alpha
# print('ALPHA'.capitalize()) #Alpha
# print(' Alpha'.capitalize()) #  alpha
# print('123'.capitalize()) #123
# print("αβγδ".capitalize()) #Αβγδ

#W4 D4 T1

# def outer():
#     x = 10
#     def inner():
#         return x
#     return inner

# f = outer()
# print(f())

# from functools import reduce
# print(reduce(lambda a, b: a + b, [1, 2, 3, 4], 10))

# result = (filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# print(result)

# result = map(lambda x: x * 2, [1, 2, 3])
# print(result)


# Broken:
# functions = [lambda: i for i in range(3)]
# print(functions)

# list = []
# functions = [i for i in range(3)]
# print(functions)

#W4 D4 T2
# nums = [1, 2, 3, 4, 5]
# result = map(lambda x: x ** 2, nums)
# print(next(result))
# print(next(result))


# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: i * 2)

# print(funcs[0](), funcs[1](), funcs[2]())


#W4 D4 T3

# def validate_positive(func):
#     """Decorator that ensures the result is positive."""
#     def wrapper(*args):
#         result = func(*args)
#         if result < 0:
#             raise ValueError("Result must be positive")
#         return result
#     return wrapper

# @validate_positive
# def subtract(a, b):
#     return a - b

# # Should work:
# print(subtract(10, 3))  # 7

# # Should raise ValueError:
# print(subtract(3, 10))  # -7 → ValueError

# from collections import defaultdict

#W4 D4 T4
# def make_stats_tracker():
#     """
#     Create a statistics tracker using closures.

#     Returns a function that:
#     - Accepts a number
#     - Tracks count, sum, min, max
#     - Returns a dict with current stats

#     Example:
#         track = make_stats_tracker()
#         print(track(10))  # {'count': 1, 'sum': 10, 'min': 10, 'max': 10, 'avg': 10.0}
#         print(track(20))  # {'count': 2, 'sum': 30, 'min': 10, 'max': 20, 'avg': 15.0}
#         print(track(5))   # {'count': 3, 'sum': 35, 'min': 5, 'max': 20, 'avg': 11.67}
#     """
    
#     tracker = defaultdict(int)
#     tracker['max'] = 0
#     tracker['min'] = 999
    
#     def track(number):
#         tracker['sum'] += number
#         tracker['count'] += 1
#         if number < tracker['min']:
#             tracker['min'] = number
#         elif number > tracker['max']:
#             tracker['max'] = number
#         tracker['avg'] = round(tracker['sum'] / tracker['count'], 2)
#         return tracker
#     return track
        

# # Test:
# track = make_stats_tracker()
# print(track(10))
# print(track(20))
# print(track(5))
# print(track(15))

#W4 D4 T5
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner

# counter = outer()
# print(counter(), counter(), counter())


# def deco(f):
#     def w():
#         return f() + "!"
#     return w

# @deco
# def say():
#     return "Hi"

# print(say())

# x = list(filter(None, [0, 1, "", "a", [], [1]]))
# print(x)

# add = lambda a, b: a + b
# print(add.__name__)


#W4 D4 T6 - creating a complete processing pipeline with functional patterns

# from functools import reduce
# from typing import List, Dict, Callable

# Sample trades
# trades = [
#     {"id": 1, "ticker": "AAPL", "side": "BUY", "entry": 150, "exit": 165, "qty": 10},
#     {"id": 2, "ticker": "GOOGL", "side": "BUY", "entry": 2800, "exit": 2750, "qty": 5},
#     {"id": 3, "ticker": "MSFT", "side": "SELL", "entry": 300, "exit": 280, "qty": 20},
#     {"id": 4, "ticker": "TSLA", "side": "BUY", "entry": 700, "exit": 720, "qty": 8},
#     {"id": 5, "ticker": "NVDA", "side": "SELL", "entry": 500, "exit": 520, "qty": 15},
# ]

# def calculate_pnl(trade: Dict) -> float:
#     """Calculate PnL: BUY = (exit-entry)*qty, SELL = (entry-exit)*qty"""
#     # Your code here (use ternary expression)
#     trade['pnl'] = (trade['exit'] - trade['entry']) * trade['qty'] if trade['side'] == 'BUY' else (trade['entry'] - trade['exit']) * trade['qty']


# for trade in trades:
#     calculate_pnl(trade)

# # unnecessary and weird, as I instantly add pnl with a single line in calculate_pnl, but I wanted to try and practice this
# # trades_with_pnl = map(lambda t: {t** 'pnl': calculate_pnl(t)}, trades)

# is_winner = lambda t: t['pnl'] > 0
# is_loser = lambda t: t['pnl'] < 0
# is_buy = lambda t: t['side'] == 'BUY'

# total_pnl = reduce(lambda acc, t: acc + t['pnl'], trades, 0)
# win_count = reduce(lambda acc, t: acc + 1 if t['pnl'] > 0 else acc, trades, 0)
# loss_count = reduce(lambda acc, t: acc + 1 if t['pnl'] < 0 else acc, trades, 0)
# best = reduce(lambda acc, t: t if t['pnl'] > acc['pnl'] else acc, trades)
# worst = reduce(lambda acc, t: t if t['pnl'] < acc['pnl'] else acc, trades)
# print(best)
# print(worst)


# def get_stats(trades_list: List[Dict]) -> Dict:
#     """
#     Calculate: total_pnl, win_count, loss_count, best_trade, worst_trade
#     """
#     if not trades_list:
#         return {}

#     total_pnl = reduce(lambda acc, t: acc + t['pnl'], trades, 0)
#     win_count = reduce(lambda acc, t: acc + 1 if t['pnl'] > 0 else acc, trades, 0)
#     loss_count = reduce(lambda acc, t: acc + 1 if t['pnl'] < 0 else acc, trades, 0)
#     best = reduce(lambda acc, t: t if t['pnl'] > acc['pnl'] else acc, trades)
#     worst = reduce(lambda acc, t: t if t['pnl'] < acc['pnl'] else acc, trades)

#     return {
#         "total_pnl": total_pnl,
#         "win_count": win_count,
#         "loss_count": loss_count,
#         "best_ticker": best["ticker"],
#         "worst_ticker": worst["ticker"],
#     }
    
    
# print("All trades with PnL:")
# for t in trades:
#     print(f"  {t['ticker']}: ${t['pnl']}")

# print(f"\nWinners: {[t['ticker'] for t in filter(is_winner, trades)]}")
# print(f"Losers: {[t['ticker'] for t in filter(is_loser, trades)]}")
# print(f"BUY trades: {[t['ticker'] for t in filter(is_buy, trades)]}")

# stats = get_stats(trades)
# print(f"\nStats: {stats}")


#W4 D4 T7
from functools import wraps

# Without @wraps - function metadata is lost
# def bad_decorator(func):
#     def wrapper(*args, **kwargs):
#         '''Wrapper test metadata'''
#         return func(*args, **kwargs)
#     return wrapper

# @bad_decorator
# def greet(name):
#     """Greets a person by name."""
#     return f"Hello, {name}!"

# print(greet.__name__)  # What does this print? - wrapper - the wrapper's name as metadata is lost
# print(greet.__doc__)   # What does this print? - None - as wrapper function has no metadata


# def good_decorator(func):
#     @wraps(func)  # Add this line
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper

# @good_decorator
# def greet(name):
#     """Greets a person by name."""
#     return f"Hello, {name}!"

# print(greet.__name__)  # Now what?
# print(greet.__doc__)   # Now what?

#Edube notes/tests
# t = "zeta"
# print(t.endswith("a"))
# print(t.endswith("A"))
# print(t.endswith("et"))
# print(t.endswith("eta"))


# print(",".join(["omicron", "pi", "rho"]))

# print("pythoninstitute.org".lstrip(".org"))

# print("This is it!".replace("is", "are", 1)) 
# print("This is it!".replace("is", "are", 2))


# # Demonstrating the rfind() method:
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau tau".rfind("ta", 3, 9))


# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# print(s2)

#W4 D5 T1
# funcs = [(lambda x: x + i) for i in range(3)]
# print(funcs[0](10), funcs[1](10), funcs[2](10)) #12, 12, 12 - LAMBDA LATE BINDING TRAP

# funcs = [(lambda x, i=i: x + i) for i in range(3)]
# print(funcs[0](10), funcs[1](10), funcs[2](10)) #10, 11, 12 (i = i rozwiązuje problem)

# result = (lambda: (lambda x: x * 2)(5))()
# print(result)

#W4 D5 T2

# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def get():
#         return count
#     return increment, get

# inc, get = counter()
# print(inc(), inc(), get())

# def make_multipliers():
#     return [lambda x, i=i: x * i for i in range(4)]

# mults = make_multipliers()
# print(mults[2](10))


# def factory(start):
#     value = start
#     def add(x):
#         nonlocal value
#         value += x
#         return value
#     return add

# adder1 = factory(10)
# adder2 = factory(100)
# print(adder1(5), adder2(5), adder1(5))


#W4 D5 T3

# from functools import reduce

# transactions = [
#     {"id": 1, "type": "BUY", "amount": 1000, "fee": 10},
#     {"id": 2, "type": "SELL", "amount": 500, "fee": 5},
#     {"id": 3, "type": "BUY", "amount": 2000, "fee": 20},
#     {"id": 4, "type": "SELL", "amount": 800, "fee": 8},
#     {"id": 5, "type": "BUY", "amount": 300, "fee": 3},
# ]

# # Part A: Use map to add net_amount (amount - fee) to each transaction
# # HINT: Create a function that returns a NEW dict with net_amount added
# # Part B: Use filter to get only BUY transactions with net_amount > 500
# # Part C: Use reduce to calculate total net_amount of filtered transactions


# result = list(map(lambda t: {**t, 'net_amount': t['amount'] - t['fee']}, transactions))


# new_trades = [] #Look, adding a new dict would be absolutely retarded, as we'd have to have a key for each trade, which doesn't make sense imo.
# for transaction in result:
#     new_trades.append(transaction)
    
# filtered_buys = [t for t in new_trades if t['type'] == 'BUY' and t['net_amount'] > 500] #started with this, much simpler approach, but then I read your instructions and used filter below
# filtered_buys = list(filter(lambda t: t['type'] == 'BUY' and t['net_amount'] > 500, new_trades))
# print(filtered_buys)

# total_net_amount = reduce(lambda acc, t: acc + t['net_amount'], filtered_buys, 0)
# print(total_net_amount)


# trades_with_pnl = list(map(
#     lambda t: {**t, "pnl": (t['exit'] - t['entry']) * t['qty']} if t['side'] == 'BUY' else
#     {**t, "pnl": (t['entry'] - t['exit']) * t['qty']},
#     trades
# ))


#W4 D5 T4
# from functools import wraps

# def repeat(times):
#     """
#     Decorator that runs a function multiple times.

#     Example:
#         @repeat(3)
#         def say_hello():
#             print("Hello!")

#         say_hello()
#         # Output:
#         # Hello!
#         # Hello!
#         # Hello!
#     """
    
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

        

# @repeat(3)
# def greet(name):
#     print(f"Hi, {name}!")

# greet("Alice")

# @repeat(2)
# def double(x):
#     print(f"Doubling {x}")
#     return x * 2

# result = double(5)
# print(f"Final result: {result}")


#W4 D5 T5
# def deco(f):
#     def wrapper():
#         return f() * 2
#     return wrapper

# @deco
# @deco
# def five():
#     return 5

# print(five())


# x = 10
# def outer():
#     x = 20
#     def inner():
#         global x
#         return x
#     return inner()

# print(outer())

# from functools import reduce
# words = ["a", "b", "c"]
# result = reduce(lambda acc, w: acc + [w.upper()], words, [])
# print(result)


#W4 D5 T6

# from functools import reduce
# from typing import List, Dict, Callable



# # Part A: Create a closure that generates crossover signals
# def make_level_detector(level: float):
#     """
#     Returns a function that detects when price crosses a level.

#     The returned function should:
#     - Accept current_price and previous_price
#     - Return "BUY" if price crosses UP through level
#     - Return "SELL" if price crosses DOWN through level
#     - Return "HOLD" otherwise

#     Example:
#         detect_105 = make_level_detector(105)
#         detect_105(106, 104)  # Returns "BUY" (crossed up through 105)
#         detect_105(104, 106)  # Returns "SELL" (crossed down through 105)
#         detect_105(107, 106)  # Returns "HOLD" (didn't cross 105)
#     """
    
#     def generate_signal(current_price: float, previous_price: float):
#         '''Closure used to generate signals based on previous price, current price and the set price level'''
#         if previous_price <= level and current_price >= level:
#             return 'BUY'
#         elif previous_price >= level and current_price <= level:
#             return 'SELL'
#         elif (previous_price >= level and current_price >= level) or (previous_price <= level and current_price <= level):
#             return 'HOLD'
              
#     return generate_signal



# detect_105 = make_level_detector(105)
# print(detect_105(106, 104))  # Returns "BUY" (crossed up through 105)
# print(detect_105(104, 106))  # Returns "SELL" (crossed down through 105)
# print(detect_105(107, 106))  # Returns "HOLD" (didn't cross 105)


# prices = [100, 102, 105, 103, 108, 106, 110, 112, 109, 115]

# price_pairs = list(map(lambda i: (prices[i-1], prices[i]), range(1, len(prices))))
# print(price_pairs)
# signals = []
# for price_pair in price_pairs:
#     result = detect_105(price_pair[1], price_pair[0]) #current, previous
#     signals.append(result)

# print(signals)

# action_signals = list(filter(lambda signal: signal == 'BUY' or signal == 'SELL', signals))
# print(action_signals)
# buy_signals = reduce(lambda acc, x: acc + 1 if x == 'BUY' else acc, action_signals, 0)
# print(buy_signals)

#W4 D5 T7

# def bold(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#     return wrapper

# def italic(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#     return wrapper

# @bold
# @italic
# def greet(name):
#     return f"Hello, {name}"

# print(greet("World"))


# funcs = [lambda x: x + i for i in range(3)]
# print(funcs[0](10))


# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1

# a = Counter()
# b = Counter()
# c = Counter()
# print(a.count, Counter.count)

# nums = [1, 2, 3, 4, 5]
# result = map(lambda x: x * 2, nums)
# print(next(result), next(result))

# from functools import reduce
# result = reduce(lambda a, b: a + [b*2], [1, 2, 3], [])
# print(result)


#W5 D1 T1
# import datetime

# today = datetime.date.today()
# print(today)
# print(today.weekday())
# print(today.isoweekday())

# tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)
# print(tomorrow.weekday())

# yesterday = today - datetime.timedelta(days=1)
# print(yesterday.weekday())
# print(yesterday.isoweekday())


# dt = datetime.datetime(2026, 2, 14, 10, 30)
# print(dt.strftime("%A, %B %d"))

# from datetime import datetime, timedelta

# now = datetime(2026, 2, 2, 12, 0)
# future = now + timedelta(days=7, hours=12)
# print(future.day, future.hour)

# from datetime import datetime, date

# dt = datetime.strptime("2026-02-14", "%Y-%m-%d")
# print(type(dt).__name__, dt.month)

# d1 = date(2026, 3, 1)
# d2 = date(2026, 2, 1)
# diff = d1 - d2
# print(type(diff).__name__, diff.days)


#W5 D1 T3

# with open('week5_file.md', 'w') as f:
#     f.write('Hello, World!\n')

# with open('week5_file.md', 'a') as a:
#     a.write('New line\n')

# lines = ['one', 'two', 'three']
# with open('week5_file.md', 'a') as append:
#     for word in lines:
#         append.write(f'{word}\n')
        

#W5 D1 T4
# with open('week5_file.md', 'r') as f:
#     x = f.read()
# print(x)


#W5 D1 T5 - Trade logger class

# from datetime import datetime
# from typing import List

# class TradeLogger:
#     """
#     Logs trade information to a file.

#     Requirements:
#     1. __init__(self, filepath: str) - store filepath, create empty file
#     2. log_trade(self, symbol: str, side: str, price: float, quantity: int)
#        - Appends a line to the file in format:
#          "2026-02-02 10:30:45 | BUY AAPL @ 150.50 x 100"
#        - Use datetime.now() for timestamp
#     3. get_trades(self) -> List[str]
#        - Returns all logged trades as a list of strings
#     4. clear_log(self)
#        - Clears the file (hint: open with 'w' and close immediately)

#     Example usage:
#         logger = TradeLogger('trades.log')
#         logger.log_trade('AAPL', 'BUY', 150.50, 100)
#         logger.log_trade('GOOGL', 'SELL', 2800.00, 10)
#         print(logger.get_trades())
#         # ['2026-02-02 10:30:45 | BUY AAPL @ 150.50 x 100',
#         #  '2026-02-02 10:30:46 | SELL GOOGL @ 2800.00 x 10']
#     """
    
#     def __init__(self, filepath: str):
#         self.filepath = filepath
#         with open(self.filepath, 'w') as w:
#             pass

#     def log_trade(self, symbol: str, side: str, price: float, quantity: int):
#         '''Method used to append a new trade to the existing list'''
#         with open(self.filepath, 'a') as a:
#             a.write(f'{datetime.now()} || {side} {symbol} @ {price} x {quantity}\n')
    
#     def get_trades(self) -> List[str]:
#         '''Method used to get all trades currently in our file'''
#         trade_list = []
        
#         with open(self.filepath, 'r') as r:
#             for line in r:
#                 trade_list.append(line)
#         return trade_list
    
#     def clear_log(self):
#         '''Method used to clear the file from all logged trades'''
#         with open(self.filepath, 'w') as w:
#             pass
#         print('Log cleared.')



# logger = TradeLogger('test_trades.log')
# logger.log_trade('AAPL', 'BUY', 150.50, 100)
# logger.log_trade('GOOGL', 'SELL', 2800.00, 10)
# print(logger.get_trades())
# logger.clear_log()
# print(logger.get_trades())  # Should be empty list


# with open('file.txt', 'a') as f:
#     result = f.write('Hello')
# print(result)


# with open('data.txt', 'r') as f:
#     f.read()

# from datetime import date, datetime

# dt1 = datetime(2026, 2, 2, 23, 59)
# dt2 = datetime(2026, 2, 3, 0, 1)
# diff = dt2 - dt1
# print(diff.total_seconds())

# dt = datetime.strptime("14:30", "%H:%M")
# print(dt.year, dt.month, dt.day)


#edube strings #1

# from typing import List

# def mysplit(string : str) -> List[str]:
#     '''A method used to return a list of words from a string, divided by whitespaces'''
    
#     result = []
#     if string == "" or string is None:
#         return result
#     else:
#         cleaned_str = string.strip()
#         return cleaned_str.split(' ')
        
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

#STRING COMPARISONS
# print('alpha' < 'alphabet') #TRUE - #longer string -> GREATER
# print('beta' > 'Beta') #TRUE - #lower-case -> GREATER
# print('alpha' < 'beta') #True - farther letter -> GREATER

# #ALSO STRING NUMERALS ARE COMPARED AS LETTERS, NOT STANDARD NUMERICALSS
# print('10' == '010') #False
# print('10' > '010') #True
# print('10' > '8') #False
# print('20' < '8') #True
# print('20' < '80') #True


#Seven-segment display 

# x = input('Please enter an integer number above 0 (e.g. 123, 5642, 302): ')
# def calculator_display(x = x):

#     digits = {        
#         '1': ['  #', '  #', '  #', '  #', '  #'],
#         '2': ['###', '  #', '###', '#  ', '###'],
#         '3': ['###', '  #', '###', '  #', '###'],
#         '4': ['# #', '# #', '###', '  #', '  #'],
#         '5': ['###', '#  ', '###', '  #', '###'],
#         '6': ['###', '#  ', '###', '# #', '###'],
#         '7': ['###', '  #', '  #', '  #', '  #'],
#         '8': ['###', '# #', '###', '# #', '###'],
#         '9': ['###', '# #', '###', '  #', '###'],
#         '0': ['###', '# #', '# #', '# #', '###']
#     }
    
#     for row in range(5):
#         line = ''
#         for char in x:
#             line += digits[char][row] + '  '
#         print(line)
    
# calculator_display()

#Start 12:05
#W5 D2 T1

# from datetime import date

# def days_until(target_year: int, target_month: int, target_day: int) -> int:
#     '''Return number of days from today until target date, negative if past'''

#     final_date = date(target_year, target_month, target_day)
#     today = date.today()
    
#     days_diff = (final_date - today).days
#     return days_diff
    
# print(days_until(2026, 12, 31))
# print(days_until(2026, 1, 1))


# from datetime import datetime

# def format_trade_timestamp(dt: datetime) -> str:
#     """Return timestamp as 'YYYY-MM-DD HH:MM:SS' string."""
#     return dt.strftime("%Y-%m-%d %H:%M:%S")

# print(format_trade_timestamp(datetime(2026, 2, 14, 10, 30, 45)))


# from datetime import datetime

# def parse_csv_date(date_str: str) -> datetime:
#     """Parse date string in format 'DD/MM/YYYY' to datetime object."""
#     return datetime.strptime(date_str, '%d/%m/%Y')

# dt = parse_csv_date("14/02/2026")
# print(dt.year, dt.month, dt.day)  # 2026 2 14


#W5 D2 T2

# def count_lines(filepath: str) -> int:
#     """Return the number of lines in a file."""
    
#     counter = 0
#     with open(filepath, 'r') as r:
#         for line in r:
#             counter += 1
    
#     return counter


# with open('test_file.txt', 'a') as a:
#     for i in range(100):
#         a.write('XD\n')
        
# x = count_lines('test_file.txt')
# print(x)

# from datetime import datetime

# def log_entry(filepath: str, message: str) -> None:
#     """Append '[YYYY-MM-DD HH:MM:SS] message' to file."""
    
#     with open(filepath, 'a') as a:
#         a.write(f'[{datetime.now()}] {message}\n')

# log_entry("app.log", "Application started")
# log_entry("app.log", "User logged in")
    
# with open('app.log', 'r') as r:
#     counter = 0
#     for line in r:
#         counter += 1
#         print(f'Line {counter}: {line}')
    


#W5 D2 T3

# from datetime import datetime

# def make_date_formatter(format_string: str):
#     """
#     Return a function that formats datetime objects using the given format.

#     Example:
#         us_format = make_date_formatter("%m/%d/%Y")
#         eu_format = make_date_formatter("%d/%m/%Y")

#         dt = datetime(2026, 2, 14)
#         print(us_format(dt))  # "02/14/2026"
#         print(eu_format(dt))  # "14/02/2026"
#     """
    
#     def format_date(date_string):
#         return datetime.strftime(date_string, format_string)
    
#     return format_date



# us_format = make_date_formatter("%m/%d/%Y")
# eu_format = make_date_formatter("%d/%m/%Y")

# dt = datetime(2026, 2, 14)
# print(us_format(dt))  # "02/14/2026"
# print(eu_format(dt))  # "14/02/2026"


# from datetime import datetime
# from time import sleep

# def make_time_tracker():
#     """
#     Return a function that returns seconds elapsed since tracker was created.

#     Example:
#         tracker = make_time_tracker()
#         # ... do some work ...
#         print(tracker())  # e.g., 2.5 (seconds elapsed)
#     """
    
#     saved_time = datetime.now()
    
#     def check_time():
#         return f'{(datetime.now() - saved_time).seconds} seconds has passed since this tracker was created!'
#     return check_time



# x = make_time_tracker()
# sleep(3)
# print(x())
# sleep(4)
# print(x())


#W5 D3 T4


# from datetime import datetime, timedelta
# from typing import List, Optional

# class TradeLogger:
#     """
#     Logs trade information to a file.

#     Requirements:
#     1. __init__(self, filepath: str) - store filepath, create empty file
#     2. log_trade(self, symbol: str, side: str, price: float, quantity: int)
#        - Appends a line to the file in format:
#          "2026-02-02 10:30:45 | BUY AAPL @ 150.50 x 100"
#        - Use datetime.now() for timestamp
#     3. get_trades(self) -> List[str]
#        - Returns all logged trades as a list of strings
#     4. clear_log(self)
#        - Clears the file (hint: open with 'w' and close immediately)

#     Example usage:
#         logger = TradeLogger('trades.log')
#         logger.log_trade('AAPL', 'BUY', 150.50, 100)
#         logger.log_trade('GOOGL', 'SELL', 2800.00, 10)
#         print(logger.get_trades())
#         # ['2026-02-02 10:30:45 | BUY AAPL @ 150.50 x 100',
#         #  '2026-02-02 10:30:46 | SELL GOOGL @ 2800.00 x 10']
#     """
    
#     def __init__(self, filepath: str):
#         self.filepath = filepath
#         with open(self.filepath, 'w') as w:
#             pass

#     def log_trade(self, symbol: str, side: str, price: float, quantity: int):
#         '''Method used to append a new trade to the existing list'''
#         with open(self.filepath, 'a') as a:
#             a.write(f'{datetime.now()} || {side} {symbol} @ {price} x {quantity}\n')
    
#     def get_trades(self) -> List[str]:
#         '''Method used to get all trades currently in our file'''
#         trade_list = []
        
#         with open(self.filepath, 'r') as r:
#             for line in r:
#                 trade_list.append(line)
#         return trade_list
    
#     def clear_log(self):
#         '''Method used to clear the file from all logged trades'''
#         with open(self.filepath, 'w') as w:
#             pass
#         print('Log cleared.')
        
    
#     def get_trades_since(self, dt: datetime) -> List[str]:
#         '''Returns only trades logged after the given datetime'''
        
#         matching_trades = []
#         converted_dt = datetime.strptime(dt, '%Y-%m-%d')
#         with open(self.filepath, 'r') as r:
#             for line in r:
#                 line_date = line.strip().split(' ')[0]
#                 datetime_date = datetime.strptime(line_date, '%Y-%m-%d')
#                 print(datetime_date)
#                 print(type(datetime_date))
#                 if datetime_date > converted_dt:
#                     matching_trades.append(line)
#         return matching_trades
    
    
#     def get_trades_by_symbol(self, symbol: str) -> List[str]:
#         '''Return trades for a specific symbol'''
        
#         filtered_trades = []
#         trades = self.get_trades()
#         for trade in trades:
#             properties = trade.strip().split(' ')
#             trade_symbol = properties[4]
#             if trade_symbol == symbol:
#                 filtered_trades.append(trade)
            
#         return filtered_trades
    
#     def get_trade_count(self) -> int:
#         trades = self.get_trades()
#         return len(trades)
    

# logger = TradeLogger('trades.log')
# logger.log_trade('AAPL', 'BUY', 150.50, 100)
# logger.log_trade('GOOGL', 'SELL', 2800.00, 10)
# #print(logger.get_trades())
# #print(logger.get_trades_since('2026-02-02'))
# # ['2026-02-02 10:30:45 | BUY AAPL @ 150.50 x 100',
# #  '2026-02-02 10:30:46 | SELL GOOGL @ 2800.00 x 10']
# trades_by_symbol = logger.get_trades_by_symbol('AAPL')
# print(trades_by_symbol)
# print(logger.get_trade_count())


#W5 D3 T5

# from datetime import datetime, timedelta, date

# dt = datetime(2026, 2, 28, 23, 30)
# dt2 = dt + timedelta(hours=1)
# print(dt2.day, dt2.month)


# with open('test.txt', 'w') as f:
#     f.write('abc')
#     f.write('def')

# with open('test.txt', 'r') as f:
#     print(f.readline())
    
    
# d = date.today()
# print(type(d.year).__name__)
    
    
# lines = []
# with open('test.txt', 'w') as f:
#     f.writelines(['a\n', 'b\n'])

# with open('test.txt', 'r') as f:
#     for line in f:
#         lines.append(line.strip())
# print(lines)

# from datetime import datetime

# dt1 = datetime(2026, 2, 1, 12, 0)
# dt2 = datetime(2026, 2, 1, 14, 30)
# diff = dt2 - dt1
# print(type(diff).__name__)


#W5 D3 T6

# from datetime import datetime
# from typing import Optional

# class ConfigManager:
#     """
#     A configuration manager that persists settings to a file.

#     Properties:
#     - last_updated (read-only): datetime of last config change
#     - debug_mode: bool, with getter and setter
#     - max_trades: int, with validation (must be > 0)

#     The config file format (config.txt):
#     debug_mode=True
#     max_trades=100
#     last_updated=2026-02-03 10:30:45
#     """

#     def __init__(self, filepath: str):
#         self.filepath = filepath
#         self._debug_mode = False
#         self._max_trades = 10
#         self._last_updated: Optional[datetime] = None
#         self._load_config()

#     def _load_config(self):
#         """Load config from file if exists."""
#         try:
#             with open(self.filepath, 'r') as r:
#                 print(r.read())
#         except FileNotFoundError:
#             print('Cannot load config, as it does not exist - create it first!')

#     def _save_config(self):
#         """Save current config to file."""
#         with open(self.filepath, 'w') as w:
#             w.write(f'debug_mode={self.debug_mode}\nmax_trades={self.max_trades}\nlast_updated={self.last_updated}')

#     @property
#     def last_updated(self) -> Optional[datetime]:
#         """Read-only: when config was last modified."""
#         return self._last_updated

#     @property
#     def debug_mode(self) -> bool:
#         # Your code:
#         return self._debug_mode

#     @debug_mode.setter
#     def debug_mode(self, value: bool):
#         # Your code (update _last_updated, save to file):
#         self._debug_mode = value
#         self._last_updated = datetime.now()
#         with open(self.filepath, 'w') as w:
#             w.write(f'debug_mode={value}\nmax_trades={self.max_trades}\nlast_updated={self.last_updated}')

#     @property
#     def max_trades(self) -> int:
#         return self._max_trades

#     @max_trades.setter
#     def max_trades(self, value: int):
#         if value < 0:
#             print('Cannot update max_trades value with a value below 0!')
#         else:
#             self._max_trades = value

# # Test:
# config = ConfigManager('config.txt')
# config.debug_mode = True
# config.max_trades = 50
# print(f"Debug: {config.debug_mode}, Max: {config.max_trades}")
# print(f"Last updated: {config.last_updated}")


#W5 D3 T7

# from datetime import datetime
# from functools import wraps

# def log_to_file(filepath: str):
#     """
#     Decorator factory that logs function calls to a file.

#     Log format: "YYYY-MM-DD HH:MM:SS | function_name(args) -> result"

#     Example usage:
#         @log_to_file("calls.log")
#         def add(a, b):
#             return a + b

#         add(2, 3)  # Logs: "2026-02-03 10:30:45 | add(2, 3) -> 5"
#     """
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(filepath, 'w') as a:
#                 a.write(f'{datetime.now()} || {func.__name__} called with {func(*args, **kwargs)} and received {result}\n')
#             return result
#         return wrapper
#     return decorator

# # Test:
# @log_to_file("function_calls.log")
# def multiply(a, b):
#     return a * b

# @log_to_file("function_calls.log")
# def greet(name):
#     return f"Hello, {name}!"

# multiply(3, 4)
# multiply(5, 6)
# greet("Alice")

# # Read and print the log file
# with open("function_calls.log", "r") as f:
#     print(f.read())

#W5 D3 T8

# from datetime import date, timedelta

# def mondays_in_month(year: int, month: int) -> list:
#     """Return list of all Monday dates in the given month."""
#     first_day = date(year, month, 1)
#     last_day = date(year, month + 1, 1) - timedelta(1)
    
#     current_date = first_day
#     mondays_list = []
    
#     while current_date <= last_day:
#         if current_date.weekday() == 0:
#             mondays_list.append(current_date)
#         current_date += timedelta(1)
    
#     return mondays_list


# from datetime import date, timedelta

# def trading_days_between(start: date, end: date) -> int:
#     """Return count of weekdays (Mon-Fri) between start and end (exclusive)."""
#     days_list = []
#     current_date = start
#     print(current_date.weekday())
#     while current_date < end:
#         if current_date.weekday() == 5 or current_date.weekday() == 6:
#             current_date += timedelta(1)
#         elif current_date.weekday != 5 and current_date.weekday != 6:
#             days_list.append(current_date)
#             current_date += timedelta(1)
#     return len(days_list)

# # Test:
# print(trading_days_between(date(2026, 2, 2), date(2026, 2, 9)))  # Mon to Mon = 5 trading days


# from datetime import datetime, timedelta

# start = datetime(2026, 1, 1)
# deltas = [timedelta(days=30) for _ in range(3)]
# current = start

# for d in deltas:
#     current += d
#     print(current.strftime("%B"), end=" ")
    
#February

#Finish 14:52

#Edube

# Numbers Processor.

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("The total is:", total)
# except:
#     print(substr, "is not a number.")

#Start 10:25

#W5 D3 T2

# from functools import wraps

# def log_calls(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         with open('calls.log', 'a') as f:  # BUG HERE
#             f.write(f'{func.__name__} called\n')
#         return result
#     return wrapper

# @log_calls
# def greet(name):
#     return f'Hello, {name}'

# greet('Alice')
# greet('Bob')
# greet('Charlie')


# from functools import wraps

# def debug(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Calling {func.__name__} with {args}')
#         result = func(*args, **kwargs)
#         print(f'Result: {result}')
#         return result
#     return wrapper

# @debug
# def expensive_operation(n):
#     print('Doing expensive work...')
#     return n * 2

# expensive_operation(5)


#W5 D3 T3

# from datetime import datetime
# from functools import wraps

# def log_to_file(filepath: str):
#     """
#     Decorator factory that logs function calls to a file.

#     Requirements:
#     1. APPEND to file (don't overwrite)
#     2. Call wrapped function ONCE only
#     3. Format: "TIMESTAMP | func_name(args) -> result"
#     4. Preserve function metadata with @wraps
#     """
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(filepath, 'a') as a:
#                 a.write(f'{datetime.now()} | {func.__name__}{args} -> {result}\n')
#                 return result #This is not mandatory here, as we already save the result in our file, but I implemented it nevertheless, as a standard approach
#         return wrapper
#     return decorator



# # Test:
# @log_to_file('operations.log')
# def add(a, b):
#     return a + b

# @log_to_file('operations.log')
# def multiply(a, b):
#     return a * b

# # Clear log first
# open('operations.log', 'w').close()

# add(2, 3)
# add(10, 20)
# multiply(4, 5)

# # Print the log
# with open('operations.log', 'r') as f:
#     print(f.read())



#W5 D3 T4

# from datetime import datetime

# def format_date(dt: datetime) -> str:
#     """Format datetime as string."""
#     parsed = datetime.strptime(dt, '%Y-%m-%d')  # ???
#     return parsed.strftime('%B %d, %Y')

# x = format_date('2025-2-12')
# print(x)


# def process_count(count: int) -> str:
#     return f'Count is {count}'

# x = process_count(23)
# print(x)


#W5 D3 T5 - BacktestEngine - algo_backtest/engine/backtest_engine.py


# from typing import List
# from datetime import datetime
# from position import Position
# from trade import Trade
# from position_manager import PositionManager


# class BacktestEngine:
#     """
#     Orchestrates backtesting using existing Position and Trade classes.

#     Lifecycle: Position (open) -> Trade (closed)

#     Attributes:
#         position_manager: Manages open positions
#         completed_trades: List of closed Trade objects
#     """
    
#     def __init__(self):
#         self.position_manager = PositionManager()
#         self.completed_trades: List[Trade] = []
#         self._win_rate = 0
#         self._total_pnl = 0
        
#     def open_position(self, ticker, side, entry, quantity, stop_loss, take_profit) -> Position:
#         """
#         Open a new position and add to manager.

#         Returns:
#             The created Position object
#         """
        
#         position = Position(ticker, side, entry, quantity, stop_loss, take_profit)
#         self.position_manager.add_position(position)
        
    
#     def process_price(self, current_price: float) -> List[Trade]:
        
#         """
#         Check all positions against current price.
#         Close any that hit SL/TP and convert to Trade objects.

#         Steps:
#         1. Use position_manager.close_triggered_positions(current_price)
#         2. For each closed position, create a Trade object
#         3. Add Trade to completed_trades
#         4. Return list of newly created trades

#         Returns:
#             List of newly closed trades (empty if none closed)
#         """
#         closed_positions = self.position_manager.close_triggered_positions(current_price)
#         newly_closed_trades = []
#         for position in closed_positions:
#             exit_reason = position.should_close(current_price)[1]
#             trade = Trade(position.ticker, 
#                           position.side, 
#                           position.entry_price, 
#                           current_price, 
#                           position.quantity,
#                           exit_reason = exit_reason)
#             newly_closed_trades.append(trade)
#             self.completed_trades.append(trade)
            
#         return newly_closed_trades
            
 
 
#     @property
#     def total_pnl(self) -> float:
#         """Sum of PnL from all completed trades."""
#         self._total_pnl = sum([trade.pnl for trade in self.completed_trades])
#         return self._total_pnl

#     @property
#     def win_rate(self) -> float:
#         """Win rate using Trade.calculate_win_rate()."""
#         self._win_rate = Trade.calculate_win_rate(self.completed_trades)
#         return self._win_rate


#W5 D3 T6

# with open('xd.log', 'a') as a:
#     a.write('File created.')

# with open('xd.log', 'x') as x:
#     print('Open')


#W5 D3 T7

# from typing import List

# def read_non_empty_lines(filepath: str) -> List[str]:
#     """
#     Read a file and return only non-empty lines.

#     Requirements:
#     1. Strip whitespace from each line
#     2. Skip lines that are empty after stripping
#     3. Return as a list of strings (without newlines)

#     Example:
#         File contents:
#         "hello\n"
#         "\n"
#         "  \n"
#         "world\n"

#         Returns: ['hello', 'world']
#     """
#     table_of_contents = []
    
#     with open(filepath, 'r') as r:
#         for line in r:
#             content = line.strip()
#             print(content)
#             if content is not None and content != '':
#                 table_of_contents.append(content)
#             else:
#                 continue
            
#     return table_of_contents
    

# # Test:
# # Create test file
# with open('test_lines.txt', 'w') as f:
#     f.write('hello\n\n   \nworld\n  python  \n')

# result = read_non_empty_lines('test_lines.txt')
# print(result)  # ['hello', 'world', 'python']


#W5 D3 T8
# from functools import wraps


# def rate_limiter(max_calls: int):
#     """
#     Decorator factory that limits how many times a function can be called.

#     After max_calls, the function returns None without executing.

#     Example:
#         @rate_limiter(3)
#         def greet(name):
#             return f'Hello, {name}'

#         print(greet('A'))  # Hello, A
#         print(greet('B'))  # Hello, B
#         print(greet('C'))  # Hello, C
#         print(greet('D'))  # None (limit reached)

#     Hint: Use a list to track call count (closure trick from Week 4)
#     """
    
#     def decorator(func):
#         call_count = 0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal call_count
#             if call_count >= max_calls:
#                 return None
#             else:
#                 result = func(*args, **kwargs)
#                 call_count += 1
#             return result
#         return wrapper
#     return decorator

# # Test:
# @rate_limiter(3)
# def expensive_api_call(query):
#     return f'Results for: {query}'

# print(expensive_api_call('python'))  # Results for: python
# print(expensive_api_call('java'))    # Results for: java
# print(expensive_api_call('rust'))    # Results for: rust
# print(expensive_api_call('go'))      # None
# print(expensive_api_call('c++'))     # None

#Edube - 1

# def improved_caesar_cipher(str: str, shift_value: int) -> str:
#     chars = []
#     index = -1 #starting position

#     if shift_value > 25 or shift_value < 1:
#         print('Invalid number! We need a number from 1 to 25!')
#         return None
#     else:
#         str.strip()
#         for character in str:
#             index += 1
#             if not character.isalpha():
#                 chars.append(character)
#             else:
#                 original_code = ord(character)
#                 new_code = original_code + shift_value
                
#                 if character.isupper() and new_code > 90:
#                     difference = new_code - 90 #if we go past Z, calculate how far from Z we go
#                     new_code = 64 + difference #And now we go back to A(ord 65) + THE DIFFERENCE
                    
#                 elif character.islower() and new_code > 122: #same logic for lowercase, if we go past z
#                     difference = new_code - 122
#                     new_code = 96 + difference
                    
#                 chars.append(chr(new_code))

#     return ''.join(chars)
            
# original_str = input('Please input a line of text e.g. (John hit a wall): ')
# shift_value = int(input('Please input a number from 1 to 25: '))

# cipher = improved_caesar_cipher(original_str, shift_value)
# print(cipher)


#Edube - 2 - Palindrome checker

# def palindrome_check(string: str) -> str:
#     '''A function used to check whether a given character is a palindrome, or not'''
    
#     list_of_chars = [character.lower() for character in string if character.isalpha()]
#     print(list_of_chars)

#     index = -1
#     reverse_index = 0
    
#     for _ in list_of_chars:
#         index += 1
#         reverse_index -= 1
#         if list_of_chars[index] != list_of_chars[reverse_index]:
#             print(f'The string is not a palindrome, as char {list_of_chars[index]} from index {index} is different from char {list_of_chars[reverse_index]} from index {reverse_index}')
#             return 'It is not a palindrome'
    
#     return 'It is a palindrome'


# string = str(input('Please enter a string: '))
# x = palindrome_check(string)
# print(x)

#Edube - 3 - Anagram checker

# def anagram_checker(word1: str, word2: str) -> bool:
#     '''Func used to check whether two given words are anagrams or not'''
#     chars1 = [character.lower() for character in word1 if character.isalpha()]
#     chars2 = [character.lower() for character in word2 if character.isalpha()]
    
#     word1_chars = sorted(chars1)
#     word2_chars = sorted(chars2)
#     print(word1_chars)
#     print(word2_chars)
#     if word1_chars == word2_chars:
#         return 'Anagrams'
#     else:
#         return 'Not anagrams'

# word1 = str(input('Please enter the first word: '))
# word2 = str(input('Please enter the second word: '))

# x = anagram_checker(word1, word2)
# print(x)

#W5 D4 T1


# def decorator(arg):
#     def inner(func):
#         def wrapper(*args):
#             return func(*args)
#         return wrapper
#     return inner

# @decorator(5)
# def add(a, b):
#     return a + b

# print(add(4, 15))


#W5 D4 T2

# from datetime import datetime
# from functools import wraps

# def timer(func):
#     '''Decorator that prints execution time of a function.
    
    
#        Example output: add took 0.001 seconds
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         end = datetime.now()
#         print(f'{func.__name__} took {end - start}')
#         return result
#     return wrapper

# @timer
# def slow_function():
#     total = 0
#     for i in range(1000000):
#         total += i
#     return total

# result = slow_function()
# print(f'Result: {result}')
# # Expected output:
# # slow_function took X.XXX seconds
# # Result: 499999500000
# print(datetime.now().strftime("%Y"))


#W5 D4 T3

# def f(x=[]):
#     x.append(1)
#     return x

# print(len(f()), len(f()))


#W5 D4 T5

# Write a simple test in `practice.py` that:
# 1. Creates a BacktestEngine
# 2. Opens 2 positions (one BUY, one SELL)
# 3. Processes a price that triggers one of them
# 4. Prints the results

# from algo_backtest.engine.backtest_engine import BacktestEngine
# engine = BacktestEngine()
# print(engine)

# engine.open_position('FDAX', 'BUY', 24410, 7, 24390, 25600)

# engine.process_price(25610)
# engine.open_position('BTCUSD', 'SELL', 70800, 5, 72100, 66400)
# engine.process_price(66300)

# print(engine.total_pnl)
# print(engine.win_rate)


#W5 D4 T6
# def add_item(item, items=None):

#     if items is None:
#         items = []
#     items.append(item)
#     return items

# print(add_item('a'))
# print(add_item('b'))


#Edube Labs - #1 today - Digit of life, instruction below


# '''Some say that the Digit of Life is a digit evaluated using somebody's birthday. 
# It's simple - you just need to sum all the digits of the date. 
# If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. 

# For example:

# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.

# Your task is to write a program which:

# - asks the user her/his birthday 
# (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)

# - outputs the Digit of Life for the date.'''


# def digit_of_life(birth_date: str) -> int:

#     num_list = [int(num) for num in birth_date if num.isnumeric()]
#     sum_nums = reduce(lambda acc, num: acc + num, num_list, 0)

#     iteration_num = 0

#     while sum_nums > 9:
#         iteration_num += 1
#         split_nums =[int(num) for num in str(sum_nums)]
#         print(f'Iteration number {iteration_num}, the current number is {sum_nums}')
#         sum_nums = reduce(lambda acc, num: acc + num, split_nums, 0)
        
#     return sum_nums

# birth_date = input('Please share your birthday date e.g.(1993-12-1, 05022003 etc - the order does not matter): ')
# digit = digit_of_life(birth_date)
# print(digit)

#Edube - 2 - comprising words

'''Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;

if the second string is "vcxzxdcybfdstbywuefsas", 
the answer is no (as there are neither the letters "d", "o", or "g", in this order)'''



# def comprising_words(string1, string2) -> str:
#     '''A function used to check whether the characters comprising the first string hidden in the second string'''
    
#     matching_list = []
#     chars = [char for char in string1]
#     for char in chars:
#         position = string2.find(char)
#         if position == -1:
#             return 'No'
#         else:
#             matching_list.append(char)
    
#     if chars == matching_list:
#         return 'Yes'
            


# string1 = input('Please input the first string: ').lower()
# string2 = input('Please input the second string: ').lower()
# x = comprising_words(string1, string2)
# print(x)

#Start 10:55
#Week5 D5 T1

# data = [1, 2, [3, 4]]
# copy = data[:]
# copy[2].append(5)
# print(data)

#Week5 D5 T2

# from functools import wraps

# def retry(max_attempts: int):
#     """
#     Decorator factory that retries a function if it raises an exception.

#     After max_attempts failures, re-raise the last exception.

#     Example:
#         @retry(3)
#         def flaky_api():
#             # might fail sometimes
#             ...
#     """
    
    
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             last_exception = None
#             for attempt in range(max_attempts):
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except Exception as e:
#                     last_exception = e
#             raise last_exception
#         return wrapper
#     return decorator

# # Test:
# attempt_count = 0

# @retry(3)
# def unstable_function():
#     global attempt_count
#     attempt_count += 1
#     if attempt_count < 3:
#         raise ValueError(f'Attempt {attempt_count} failed')
#     return 'Success!'

# print(unstable_function())


#W5 D5 T3

# from datetime import datetime
# from typing import List

# def filter_log_by_date(filepath: str, start: datetime, end: datetime) -> List[str]:
#     '''Read a log file and return only lines where timestamp falls between stard and end (inclusive
    
#       Log format per line "YYYY-MM-DD HH:MM:SS | message"
#     )'''
#     matching_logs = []
#     with open(filepath, 'r') as r:
#         for line in r:
#             parts = line.split(' ')
#             date = parts[0:2]
#             date = str(' '.join(date))
#             date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            
#             if date > start and date < end:
#                 matching_logs.append(line)
    
#     return matching_logs
            
    
# with open('test_filter.log', 'w') as f:
#     f.write('2026-02-01 10:00:00 | Server started\n')
#     f.write('2026-02-03 14:30:00 | Trade executed\n')
#     f.write('2026-02-05 09:15:00 | Error occurred\n')
#     f.write('2026-02-06 16:00:00 | Shutdown\n')

# start = datetime(2026, 2, 2)
# end = datetime(2026, 2, 5, 23, 59)
# results = filter_log_by_date('test_filter.log', start, end)

# for line in results:
#     print(line)
    
#W5 D5 T4
    
# with open('x.txt', 'w') as f:
#     f.write('abc\n')
#     f.write('def\n')

# with open('x.txt') as f:
#     lines = f.readlines()
# print(len(lines), lines[0].strip())

#W5 D5 T5 - addded __str__ method to BacktestEngine (algo_backtest/engine/backtest_engine.py)
        
# def __str__(self) -> str:
#     """
#     Return a summary like:
#     BacktestEngine: 2 open | 3 closed | PnL: $1500.00
#     """
    
#     return f'BacktestEngine: {(self.position_manager.get_position_count())} open | {len(self.completed_trades)} closed | PnL: ${self.total_pnl}'


# from algo_backtest.engine.backtest_engine import BacktestEngine

# engine = BacktestEngine()

# # Open a BUY position: entry 1.0800, SL 1.0750, TP 1.0850
# pos = engine.open_position('EURUSD', 'BUY', 1.0800, 10000,
#                             stop_loss=1.0750, take_profit=1.0850)

# print(f'Open positions: {engine.position_manager.get_position_count()}')  # 1

# # Price moves to 1.0820 - no trigger
# closed = engine.process_price(1.0820)
# print(f'Trades closed: {len(closed)}')  # 0

# # Price hits TP at 1.0850
# closed = engine.process_price(1.0850)
# print(f'Trades closed: {len(closed)}')  # 1
# print(f'Total PnL: ${engine.total_pnl:.2f}')  # $500.00

# print(engine)


#W5 D5 T7
# def bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper

# def italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper

# @bold
# @italic
# def say_hello():
#     return 'hello'

# print(say_hello())


# @italic
# @bold
# def say_hello():
#     return 'hello'

# print(say_hello())


#W5 D5 T8

# from typing import Dict

# def read_multiple_files(filepaths: list) -> Dict[str, str]:
#     """
#     Attempt to read each file in the list.

#     Returns:
#         Dict mapping filepath -> contents (for successful reads)

#     Files that don't exist or can't be read should be skipped
#     (not crash the program). Print a warning for each skipped file.

#     Example:
#         result = read_multiple_files(['exists.txt', 'missing.txt', 'also_exists.txt'])
#         # Prints: "Warning: could not read missing.txt"
#         # Returns: {'exists.txt': 'contents...', 'also_exists.txt': 'contents...'}
#     """
    
#     contents = {}
#     for filepath in filepaths:
#         try: 
#             with open(filepath, 'r') as r:
#                 text = r.read()
#                 contents[filepath] = {text}
                    
#         except Exception as e:
#             print(f'Warning, an exception {str(e)} occured within filepath {filepath}, continuing.')
#             continue   
    
#     return contents

# # Test:
# # Create some test files
# with open('file_a.txt', 'w') as f:
#     f.write('content A')
# with open('file_c.txt', 'w') as f:
#     f.write('content C')

# result = read_multiple_files(['file_a.txt', 'file_b.txt', 'file_c.txt'])
# print(result)
# Expected:
# Warning: could not read file_b.txt
# {'file_a.txt': 'content A', 'file_c.txt': 'content C'}


#Edube - 1 - Sudoku Reader - DIFFICULT - I needed to use AI to assist me - this is not a pattern I feel confident it, I'd need more practice to solve similar tasks with ease
# from typing import List
# from collections import defaultdict

# def sudoku_checker(sudoku_str: str, pattern: List[str] = None) -> str:
    
#     if pattern is None: #I've added this for practice, assuming that perhaps there's a custom sudoku out there with different set of characters, but it's probably not relevant
#         pattern = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9']
        
#     rows = sudoku_str.split()
#     #basic validation
#     for row in rows:
#         if sorted(row) != pattern:
#             return f'No, row {row} is not equal to the pattern'
#     print('Basic rows are valid, time to check 3x3')
    
#     square_starts = [(0, 0), (0, 3), (0, 6),
#                      (3, 0), (3, 3), (3, 6),
#                      (6, 0), (6, 3), (6, 6)                     
#                      ]
    
#     square_num = defaultdict[list]
#     for square_num, (start_row, start_col) in enumerate(square_starts):
#         square_values = []
#         for r in range(start_row, start_row + 3):
#             for c in range(start_col, start_col + 3):
#                 square_values.append(rows[r][c])
                
#         if sorted(square_values) != pattern:
#             return f'No, square {square_num} is invalid'
                

#     return 'All squares are valid, it is a valid sudoku!'

# stringg = '''195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671'''

# x = sudoku_checker(stringg)
# print(x)


# from datetime import datetime

# dt = datetime(2026, 2, 14, 15, 30)
# print(dt.strftime('%I:%M %p'))


# with open('test.txt', 'w') as f:
#     n = f.write('Python')
# print(n)


# class Animal:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

# class Dog(Animal):
#     def bark(self):
#         return f'{self.__name} barks'

# d = Dog('Rex')
# print(d.get_name())


# from datetime import datetime

# d1 = datetime.strptime('2026-02-14', '%Y-%m-%d')
# d2 = datetime.strptime('14/02/2026', '%d/%m/%Y')
# print(d1 == d2)

# data = {'a': 1, 'b': 2, 'c': 3}
# result = list(map(lambda kv: kv[1] * 2, data.items()))
# print(result)

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

# a = Counter()
# b = Counter()
# c = Counter()
# print(Counter.get_count())

#W6 D1 T1

# numbers = [10, 20, 30]
# it = iter(numbers)
# print(next(it))
# print(next(it))

# it2 = iter(numbers)
# print(next(it2))


# gen = (x * 2 for x in range(4))
# print(next(gen))
# print(next(gen))

# gen2 = iter(gen)
# print(next(gen2))
# print(gen is gen2)

#W6 D1 T3

# class FibonacciIterator:
#     """
#     Iterator that yields Fibonacci numbers up to max_value.

#     Usage:
#         for n in FibonacciIterator(100):
#             print(n)
#         # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#     """

#     def __init__(self, max_value: int):
#         # Your code: store max_value and initialize Fibonacci state
#         self.fibo_nums = iter([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
#         self.current = 0
#         self.max_value = max_value
        

#     def __iter__(self):
#         return self

#     def __next__(self) -> int:
#         if self.current >= self.max_value:
#             raise StopIteration
#         self.current = next(self.fibo_nums)
#         return self.current


# # Test:
# fib = FibonacciIterator(50)
# print(list(fib))
# # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# # Test: Can be used in for loop
# for n in FibonacciIterator(20):
#     print(n, end=' ')
# # Expected: 0 1 1 2 3 5 8 13

#W6 D1 T4

# class Logger:
#     _instance = None

#     def __new__(cls, name):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self, name):
#         self.name = name

# a = Logger("FileLogger")
# b = Logger("DBLogger")
# print(a.name)
# print(a is b)


# class AlwaysPositive(int):
#     def __new__(cls, value):
#         return super().__new__(cls, abs(value))

# x = AlwaysPositive(-42)
# print(x)
# print(type(x))
# print(isinstance(x, int))


#W6 D1 T5

#A 
# ORIGINAL (nested for loops)

#B
# data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# def flatten(*iterables):
#     for iterable in iterables:
#         yield from iterable

# print(flatten(data))


# def price_source(prices: list):
#     """Yield each price from the list."""
#     for price in prices:
#         yield price
        
# # Stage 2: Filter out prices below a threshold
# def filter_above(prices, threshold: float):
#     """Yield only prices above the threshold."""
#     for price in prices:
#         if price > threshold:
#                 yield price

# # Stage 3: Apply a spread (add a fixed amount)
# def apply_spread(prices, spread: float):
#     """Yield each price with spread added."""
#     for price in prices:
#             yield price + spread

# # Test the pipeline:
# raw_prices = [100.5, 98.2, 105.3, 97.1, 110.0, 99.8]
# pipeline = apply_spread(filter_above(price_source(raw_prices), 100.0), 0.5)
# print(list(pipeline))

#W6 D1 T7 - modified backtest_engine to become ticker aware and added unique id to positions in Position + modified str/repr in position to account for that id.
#The id is not yet added to Trade and that will be perhaps the next planned change - we'll  see, but for now everythign works

# from algo_backtest.engine.backtest_engine import BacktestEngine
# engine = BacktestEngine()

# # Open positions on different tickers
# engine.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
# engine.open_position('EURUSD', 'BUY', 1.0800, 10000, stop_loss=1.0750, take_profit=1.0850)

# # FDAX price moves — should only affect FDAX position
# closed = engine.process_price('FDAX', 24600)
# print(f'FDAX trades closed: {len(closed)}')       # 1 (TP hit)
# print(f'Open positions: {engine.position_manager.get_position_count()}')  # 1 (EURUSD still open)

# # EURUSD price moves — should only affect EURUSD position
# closed = engine.process_price('EURUSD', 1.0850)
# print(f'EURUSD trades closed: {len(closed)}')      # 1 (TP hit)
# print(f'Open positions: {engine.position_manager.get_position_count()}')  # 0

# # Verify unique IDs
# engine2 = BacktestEngine()
# p1 = engine2.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
# p2 = engine2.open_position('FDAX', 'SELL', 24500, 1, stop_loss=24550, take_profit=24400)
# print(p1.position_id != p2.position_id)  # True — different IDs


#W6 D2 T1

# class Repeater:
#     def __init__(self, value, times):
#         self.value = value
#         self.times = times
#         self.count = 0

#     def __iter__(self):
#         self.count = 0   # reset on every iter() call
#         return self

#     def __next__(self):
#         if self.count >= self.times:
#             raise StopIteration
#         self.count += 1
#         return self.value

# r = Repeater("hi", 3)
# print(list(r))
# print(list(r))


# data = [10, 20, 30, 40]
# it = iter(data)
# next(it)
# next(it)

# for x in it:
#     print(x, end=' ')

#W6 D2 T2

# from functools import wraps

# def enforce_types(*expected_types):
#     """
#     Decorator that checks if positional arguments match expected types.
#     Usage: @enforce_types(str, float)
#     """
#     def decorator(func):          # What goes here?
#         @wraps(func)              # What goes here?
#         def wrapper(*args, **kwargs):
#             for arg, expected in zip(args, expected_types):
#                 if not isinstance(arg, expected):   # What goes here?
#                     return f"TypeError: expected {expected.__name__}, got {type(arg).__name__}"
#             return func(*args, **kwargs)         # What goes here? (call the original function)
#         return wrapper            # What goes here?
#     return decorator

# # Test:
# @enforce_types(str, float, int)
# def create_order(ticker, price, quantity):
#     return f"Order: {ticker} @ {price} x {quantity}"

# print(create_order("FDAX", 24500.0, 1))
# print(create_order("FDAX", "bad_price", 1))
# print(create_order.__name__)

# #$ python practice.py
# # Order: FDAX @ 24500.0 x 1
# # TypeError: expected float, got str
# # create_order

#W6 D2 T3

# class FibonacciIterator:
#     """Iterator that yields Fibonacci numbers up to max_value."""

#     def __init__(self, max_value: int):
#         self.max_value = max_value
#         self.a = 0
#         self.b = 1

#     def __iter__(self):
#         return self

#     def __next__(self) -> int:
#         if self.a > self.max_value:
#             raise StopIteration
#         result = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return result
      
# # Test:
# print(list(FibonacciIterator(50)))
# # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# print(list(FibonacciIterator(1000)))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]



#W6 D2 T4
# class UpperStr(str):
#     def __new__(cls, value):
#         instance = super().__new__(cls, value.upper())
#         return instance

#     def __init__(self, value):
#         self.original = value

# s = UpperStr("hello")
# print(s)
# print(s.original)
# print(type(s).__name__)

# class ClampedInt(int):
#     """Integer that clamps to range [0, 100]."""
#     def __new__(cls, value):
#         clamped = max(0, min(100, value))
#         return super().__new__(cls, clamped)

#     def __init__(self, value):
#         self.raw_value = value

# x = ClampedInt(250)
# print(x)
# print(x.raw_value)
# print(x + 10)



#W6 D2 T5 - modified the logic of position_manager to check for ticker in checking close positions, but also to retain other positions correctly!

    # def close_triggered_positions(self, ticker: str, current_price: float) -> List[Position]:
    #     """
    #     Check all positions for SL/TP triggers and remove them.

    #     Args:
    #         current_price: Current market price.

    #     Returns:
    #         List of positions that should be closed.
    #     """
    #     closed_positions = [p for p in self.positions if p.ticker == ticker and p.should_close(current_price)]
        
    #     closed_ids = [p.position_id for p in closed_positions]
    #     self.positions = [p for p in self.positions if p.position_id not in closed_ids]
        

    #     return closed_positions
    

# from algo_backtest.engine.backtest_engine import BacktestEngine
# engine = BacktestEngine()
# engine.open_position('FDAX', 'BUY', 24500, 1, 24450, 24600)
# # (self, ticker, side, entry, quantity, stop_loss, take_profit)
# engine.open_position('EURUSD', 'BUY', 1.0800, 100000, 1.0750, 1.0850)

# x = engine.process_price('FDAX', 24600)
# print(x)
# print(engine)

#W6 D2 T6

# from algo_backtest.engine.backtest_engine import BacktestEngine

# engine = BacktestEngine()
# p = engine.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
# print(f"Position ID: {p.position_id}")

# closed = engine.process_price('FDAX', 24600)
# if closed:
#     trade = closed[0]
#     print(f"Trade position_id: {trade.position_id}")
#     print(f"IDs match: {str(p.position_id) == trade.position_id}")


#W6 D2 T7

# class CountdownIterator:
#     """
#     Iterator counting down from start to 1.

#     Usage:
#         for n in CountdownIterator(5):
#             print(n)
#         # Output: 5, 4, 3, 2, 1
#     """

#     def __init__(self, start: int):
#         self.current = start + 1
        
#     def __iter__(self):
#         return self

#     def __next__(self) -> int:
#         if self.current <= 1:
#             raise StopIteration
#         self.current -= 1
#         return self.current
        
        
        
# # Test 1:
# print(list(CountdownIterator(5)))
# # Expected: [5, 4, 3, 2, 1]

# # Test 2:
# print(list(CountdownIterator(1)))
# # Expected: [1]

# # Test 3 — exhaustion:
# c = CountdownIterator(3)
# print(next(c))  # 3
# print(next(c))  # 2
# print(list(c))  # [1] — remaining items
# print(list(c))  # [] — exhausted

#W6 D2 T8

# def gen():
#     yield from range(3)
#     yield from range(3, 6)

# print(list(gen()))


# class OnlyNew:
#     def __new__(cls, val):
#         obj = super().__new__(cls)
#         obj.x = val * 2
#         return obj

# o = OnlyNew(5)
# print(o.x)
# print(hasattr(o, '__dict__'))


#Edube - Exceptions Labs - 1

# def read_int(prompt: str, min: int, max: int) -> int:
#     '''
#     A function that checks whether the input integer value is in the specified range
    
#     '''
#     while True: #We can do it here as we will break out of the loop as soon as we get a correct number
#         try:
#             value = int(input(prompt))
#             if min <= value <= max:
#                 return value
#             else:
#                 print(f'Error: the value is not within permitted range ({min}..{max})')
#         except ValueError:
#             print('Error: wrong input!')



# v = read_int("Enter a number from -10 to 10: ", -10, 10)

# print("The number is:", v)


#Edube - Exceptions Labs - 2


# try:
#     x = 1/0
# except ZeroDivisionError:
#     print('XD')
# except ZeroDivisionError:
#     print('PP')

#W6 D3 T1
# class IteratorStyle:
#     def __init__(self):
#         self.items = [1, 2, 3]
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         val = self.items[self.index]
#         self.index += 1
#         return val

# obj = IteratorStyle()
# print(iter(obj) is obj) #True
# print(list(obj))
# print(list(obj))



# class IterableStyle:
#     def __init__(self):
#         self.items = [1, 2, 3]

#     def __iter__(self):
#         for item in self.items:
#             yield item

# obj = IterableStyle()
# it1 = iter(obj)
# it2 = iter(obj)
# print(it1 is it2) #False, separate entities
# print(list(obj)) #[1, 2, 3]
# print(list(obj)) #[1, 2, 3]


#W6 D3 T2

# from functools import wraps

# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
#         result = func(*args, **kwargs)
#         print(f'Returned: {result}')
#         return result
#     return wrapper


# # Test:
# @log_call
# def add(a, b):
#     return a + b

# @log_call
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# print(add(3, 5))
# print(greet("Alice", greeting="Hi"))
# print(add.__name__)


#W6 D3 T3

# class NumberRange:
#     '''Iterable that yields numbers from stard to end (inclusive).'''
    
#     def __init__(self, start: int, end: int):
#         self.start = start
#         self.end = end
    
#     def __iter__(self):
#         for num in range(self.start, self.end + 1):
#             yield num
            
            
# r = NumberRange(1, 5)
# # print(list(r))   # [1, 2, 3, 4, 5]
# # print(list(r))   # [1, 2, 3, 4, 5] — works again!


# it1 = iter(r)
# it2 = iter(r)
# print(next(it1))  # 1
# print(next(it1))  # 2
# print(next(it2))  # 1 — independent! Not 3!

# print(iter(r) is r)         # False — it's an iterable, not an iterator
# print(iter(r) is iter(r))   # False — each call makes a new generator

#W6 D3 T4

# def gen():
#     yield 1
#     yield 2
#     return "done"

# g = gen()
# print(next(g))
# print(next(g))

# try:
#     next(g)
# except StopIteration as e:
#     print(e.value)
    
    
# # 1 2 done


# def outer():
#     yield from [10, 20]
#     yield from (x * 3 for x in range(3))

# print(list(outer()))

# def count_up(n):
#     for i in range(n):
#         yield i

# gen = count_up(4)
# print(next(gen))
# print(next(gen))

# for x in gen:
#     print(x, end=' ')


#W6 D3 T5 - generator that streams price data from a csv file as named tuples

# from collections import namedtuple
# from algo_backtest.data.data_loader import DataLoader

# PriceTick = namedtuple('PriceTick', ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# def create_price_stream(filepath: str, ticker: str = None):
#     '''A method used to stream price data from a csv file as named tuples'''
    
#     loader = DataLoader(filepath)
#     data = loader.load_data()
    
#     for idx, row in data.iterrows():
#         if ticker is None or row.ticker == ticker:
#             yield PriceTick(row.timestamp, row.ticker, row.open, row.high, row.low, row.close, row.volume)
 
    

# Test with your ohlc_mock_data.csv:
#stream = create_price_stream('ohlc_mock_data.csv')

#Get first 3 ticks:
# for i, tick in enumerate(stream):
#     if i >= 3:
#         break
#     print(f"{tick.timestamp} | {tick.ticker} | Close: {tick.close}")

#W6 D3 T6 - implementing a tick-by-tick test with generator from T5

# stream = create_price_stream('ohlc_mock_data.csv', ticker = 'EURUSD')

# from algo_backtest.engine.backtest_engine import BacktestEngine

# stream = create_price_stream('ohlc_mock_data.csv', ticker = 'EURUSD')

# engine = BacktestEngine()
# engine.open_position('EURUSD', 'BUY', 101.1, 10000, 100.0, 103.0)

# for i, tick in enumerate(stream):
#     closed = engine.process_price(tick.ticker, tick.close)
#     if closed != []:
#         print(f'Closed trade: {closed}')
        
# print(engine)
# print(engine.total_pnl, engine.win_rate)
# print(engine.position_manager.get_position_count())

#W6 D3 T7
# list_comp = [x ** 2 for x in range(5)]
# gen_exp = (x ** 2 for x in range(5))

# print(type(list_comp))
# print(type(gen_exp))
# print(list_comp)
# print(list(gen_exp))
# print(list(gen_exp))


# nums = [1, 2, 3, 4, 5]
# squares = (n ** 2 for n in nums)

# nums.append(6)
# print(list(squares))


#Edube - OOP - Labs1

# class Stack:
#     def __init__(self):
#         self.__stk = []

#     def push(self, val):
#         self.__stk.append(val)

#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val


# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__counter = 0

#     def get_counter(self):
#         return self.__counter

#     def pop(self):
#         val = Stack.pop(self)
#         self.__counter += 1
#         return val
	

# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

#Edube - OOP - Labs2


# class QueueError(IndexError):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
    
#     def __str__(self):
#         return f'{self.message}'


# class Queue:
#     def __init__(self):
#         self.__queue_participants = []

#     def put(self, elem):
#         self.__queue_participants.append(elem)

#     def get(self):
#         if self.__queue_participants:
#             first_elem = self.__queue_participants.pop(-1)
#             return first_elem
#         else:
#             raise QueueError


# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     raise QueueError('Queue Error')


#Edube - OOP - Labs3

# class QueueError(IndexError):
#     def __init__(self, message):
#         super().__init__(self)
#         self.message = message
        
#     def __str__(self):
#         return f'Error: {self.message}'



# class Queue:
#     def __init__(self):
#         self.queue_participants = []

#     def put(self, elem):
#         self.queue_participants.append(elem)

#     def get(self):
#         if self.queue_participants:
#             first_elem = self.queue_participants.pop(-1)
#             return first_elem
#         else:
#             raise QueueError




# class SuperQueue(Queue):
#     def __init__(self):
#         super().__init__()
    
#     def isempty(self):
#         if self.queue_participants:
#             return False
#         else:
#             return True


# que = SuperQueue()
# que.put(1)
# que.put("dog")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Queue empty")

#W6 D4 T1

# class Mystery1:
#     def __init__(self):
#         self.data = [10, 20, 30]
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i >= len(self.data):
#             raise StopIteration
#         val = self.data[self.i]
#         self.i += 1
#         return val

# m = Mystery1()
# print(list(m))  # What?
# print(list(m))  # What?

#StoPiteration#

# class Mystery2:
#     def __init__(self):
#         self.data = [10, 20, 30]

#     def __iter__(self):
#         return iter(self.data)

# m = Mystery2()
# print(list(m))  # What?
# print(list(m))  # What?


# class Mystery3:
#     def __init__(self):
#         self.data = [10, 20, 30]

#     def __iter__(self):
#         for item in self.data:
#             yield item

# m = Mystery3()
# print(list(m))  # What?
# print(list(m))  # What?

#W6 D4 T2

# from functools import wraps

# def repeat(n):
#     """Decorator factory that repeats function execution n times."""
    
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result_list = []
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#                 result_list.append(result)
#             return result_list
#         return wrapper
#     return decorator


# # Test 1 — simple function:
# @repeat(3)
# def roll_dice():
#     import random
#     return random.randint(1, 6)

# print(roll_dice())  # Should return list of 3 random numbers


# # Test 2 — function with arguments:
# @repeat(4)
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']


# # Test 3 — metadata preserved:
# print(greet.__name__)  # greet



#W6 D4 T3


# Scenario A: Multiple passes needed
# def scenario_b_gen():
#     data = (x ** 2 for x in range(10000000))
#     max_val = max(data)
#     sum_val = sum(data)
#     return max_val, sum_val


# max_val, sum_val = scenario_b_gen() #Doesn't work, we'd get 0 as sum_val as the generator is exhausted after the first run.
# print(max_val, sum_val)

# def gen_with_return():
#     yield 1
#     yield 2
#     return "DONE"

# g = gen_with_return()
# print(list(g))


# def counter():
#     total = 0
#     while True:
#         x = yield total
#         if x is not None:
#             total += x

# c = counter()
# next(c)  # Prime the generator
# c.send(5)
# c.send(10)
# print(c.send(3))

#W6 D4 T5


# from collections import namedtuple
# from algo_backtest.data.data_loader import DataLoader

# PriceTick = namedtuple('PriceTick', ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# def create_price_stream(filepath: str, ticker: str = None, filter_func: callable = None):
#     '''A method used to stream price data from a csv file as named tuples'''
    
#     loader = DataLoader(filepath)
#     data = loader.load_data()
    
#     for idx, row in data.iterrows():
#         if ticker is None or row.ticker == ticker:
#             result = PriceTick(row.timestamp, row.ticker, row.open, row.high, row.low, row.close, row.volume)
            
#             if filter_func is None or filter_func(result):
#                 yield result


# # Test 1 — filter by ticker AND high price:
# def high_volatility(tick):
#     return tick.high - tick.low > 2.0

# stream = create_price_stream('ohlc_mock_data.csv', 
#                               ticker='EURUSD', 
#                               filter_func=high_volatility)

# for i, tick in enumerate(stream):
#     if i >= 3:
#         break
#     print(f"{tick.timestamp} | Range: {tick.high - tick.low:.2f}")


# # Test 2 — filter by volume threshold:
# stream2 = create_price_stream('ohlc_mock_data.csv',
#                                filter_func=lambda t: t.volume > 15000)

# print(f"\nHigh volume ticks: {sum(1 for _ in stream2)}")


#W6 D4 T6

# from collections import namedtuple
# from algo_backtest.data.data_loader import DataLoader

# PriceTick = namedtuple('PriceTick', ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# def create_price_stream(filepath: str, ticker: str = None, filter_func: callable = None):
#     '''A method used to stream price data from a csv file as named tuples'''
    
#     loader = DataLoader(filepath)
#     data = loader.load_data()
    
#     for idx, row in data.iterrows():
#         if ticker is None or row.ticker == ticker:
#             result = PriceTick(row.timestamp, row.ticker, row.open, row.high, row.low, row.close, row.volume)
            
#             if filter_func is None or filter_func(result):
#                 yield result



# from collections import deque

# def sma_indicator(price_stream, window=5):
#     """
#     Generator that calculates Simple Moving Average over price stream.

#     Args:
#         price_stream: Generator yielding PriceTick objects.
#         window: Number of periods for SMA calculation.

#     Yields:
#         Tuple of (PriceTick, sma_value) for each tick after window fills.
#     """
    
#     price_list = []
#     sma_value = 0
    
#     for i, tick in enumerate(price_stream):
#         price_list.append(tick.close)
#         if len(price_list) >= window:
#             sma_value = float(sum(price_list) / window)
#             price_list.pop()
#         yield tick, sma_value
            

# # Test:
# stream = create_price_stream('ohlc_mock_data.csv', ticker='EURUSD')
# sma_stream = sma_indicator(stream, window=3)

# for i, (tick, sma) in enumerate(sma_stream):
#     if i >= 5:
#         break
#     print(f"{tick.timestamp} | Close: {tick.close} | SMA(3): {sma:.2f}")

#W6 D4 T8

# gen = (x for x in range(3))
# print(0 in gen) #True
# print(1 in gen) #True

# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# times_three = make_multiplier(3)
# print(times_three(5))
# print(times_three.__name__)

#W6 D5 T1
# gen = (x for x in range(5))
# print(0 in gen)   # Line A
# print(0 in gen)   # Line B
# print(4 in gen)   # Line C


#W6 D5 T2

# class Data:
#     def __init__(self):
#         self.items = [1, 2, 3]
#     def __iter__(self):
#         return iter(self.items)

# d = Data()
# it = iter(d)
# print(it is d)      # Line 1
# print(list(d))      # Line 2
# print(list(it))     # Line 3

#W6 D5 T5

# def count():
#     yield 10
#     yield 20
#     yield 30

# a = count()
# b = count()
# print(next(a))
# print(next(b))
# print(next(a))


# def count():
#     yield 10
#     yield 20
#     yield 30

# g = count()
# x = iter(g)
# y = iter(g)
# print(x is y)     # ?
# print(next(x))    # ?
# print(next(y))    # ?


# nums = [10, 20, 30]
# x = iter(nums)
# y = iter(nums)
# print(x is y)     # ?
# print(next(x))    # ?
# print(next(y))    # ?

#Edube - OOP - Classes

# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1._ExampleClass__counter) #{'_ExampleClass__first': 1} 3
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter) #{'_ExampleClass__first': 2} 3
# print(example_object_3._ExampleClass__counter) #3



# class ExampleClass:
#     varia = 1
#     def __init__(self, val):
#         ExampleClass.varia = val


# print(ExampleClass.__dict__) #varia = 1
# example_object = ExampleClass(2)

# print(ExampleClass.__dict__) #varia's value changed to 2
# print(example_object.__dict__) #Empty



# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2


# example_object = ExampleClass()

# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))


# from collections import namedtuple

# Trade = namedtuple('Trade', 'ticker price quantity')
# t = Trade('AAPL', 150.0, 100)
# print(t[1])
# print(t.ticker)
# print(isinstance(t, tuple))

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

# c = Circle(5)
# print(c.r)
# 


#W7 D1 T4
# import logging
# import sys

# def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
#     '''A funciton that creates a named logger and adds a StreamHandler that writes to stdout'''

#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     format = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')
#     handler = logging.StreamHandler(sys.stdout)
#     handler.setFormatter(format)
#     logger.addHandler(handler)
    
#     return logger


# logging.warning("Deprecated usage detected")
# import warnings
# warnings.warn("Deprecated usage detected", DeprecationWarning)
# print('Test print')


# import logging


# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")

#W7 D2 #T1
# 
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.WARNING)  # second call
# logging.debug("hello")

#W7 D2 #T2
# import logging
# import sys

# logger = logging.getLogger('gate_test')
# logger.setLevel(logging.DEBUG)          # Gate 1: Logger

# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.INFO)       # Gate 2: Handler
# logger.addHandler(handler)

# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")

#W7 D2 #T3

# import logging

# a = logging.getLogger('my_logger')
# b = logging.getLogger('my_logger')
# c = logging.getLogger('other_logger')

# print(a is b) #True
# print(a is c) #False
# print(id(a) == id(b)) #True

#W7 D2 #T4
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.debug("a") 
# logging.info("b")
# logging.warning("c")


# import logging
# import sys

# logger = logging.getLogger('predict')
# logger.setLevel(logging.ERROR)

# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# logger.debug("1")
# logger.info("2")
# logger.warning("3")
# logger.error("4")
# logger.critical("5")

# import logging
# import sys

# logger = logging.getLogger('predict2')
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.ERROR)
# logger.addHandler(handler)

# logger.debug("1")
# logger.warning("3")
# logger.error("4")

# import logging
# import sys

# logger = logging.getLogger('backtest')
# logger.setLevel(logging.DEBUG)

# logger.warning('test')

# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# format = logging.Formatter('[%(levelname)s]: %(message)s')
# handler.setFormatter(format) #lazy formatting with %s - does not actually format a string unless it actually gets printed - superior to f-string in this matter
# logger.addHandler(handler)

# logger.warning('test')

# f_handler = logging.FileHandler('test.log')
# f_handler.setLevel(logging.DEBUG)
# f_handler.setFormatter(format)

# logger.addHandler(f_handler)

# logger.debug('Debug line')
# logger.warning('Warning line')


#W7 D2 #T5

# import logging
# import sys

# import logging
# import sys

# def build_logger(name: str, filepath: str, level: int = logging.INFO) -> logging.Logger:
    
#     if logging.getLogger(name).handlers:
#         return logging.getLogger(name)
    
#     else:
#         root = logging.getLogger(name)
#         root.setLevel(level)
    
#         fmt = logging.Formatter('[%(levelname)s]: %(message)s')
        
#         console = logging.StreamHandler(sys.stdout)
#         console.setFormatter(fmt)
        
#         file_handler = logging.FileHandler(filepath)
#         file_handler.setFormatter(fmt)
        
#         root.addHandler(console)
#         root.addHandler(file_handler)
#         return logging.getLogger(name)



# x = build_logger('test-loggy', 'super_log.log')
# y = build_logger('test-loggy', 'super_log.log')
# print(x)
# print(y)

#Edube - Classes labs - 1

# class Timer:
#         '''A class '''
#         def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
#             self.__hours = hours
#             self.__minutes = minutes
#             self.__seconds = seconds

#         def __str__(self):
#             return f'{self.__hours}:{self.__minutes}:{self.__seconds}'
        
#         def next_second(self):
#             self.__seconds += 1
#             if self.__seconds == 60:
#                 self.__seconds = 0
#                 self.__minutes += 1
#                 if self.__minutes == 60:
#                     self.__minutes = 0
#                     self.__hours += 1
#                     if self.__hours == 24:
#                         self.__hours = 0
            
#         def prev_second(self):
#             self.__seconds -= 1
#             if self.__seconds == -1:
#                 self.__seconds = 59
#                 self.__minutes -= 1
#                 if self.__minutes == -1:
#                     self.__minutes = 59
#                     self.__hours -= 1
#                     if self.__hours == -1:
#                         self.__hours = 23


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)

# time_str = str(timer)
# print(time_str)

# def time_string_format(time_string: str) -> str:
#     '''Formats the time string to a required format'''
#     values = time_string.split(':')
#     final_value_list = []
#     print(values)
#     for value in values:
#         if len(value) == 1:
#             value = f'0{value}'
#             final_value_list.append(value)
#         else:
#             final_value_list.append(value)
    
#     final_output = ':'.join(final_value_list)
#     return final_output
        
# format_str = time_string_format(time_str)
# print(format_str)

#Edube - Classes labs - 2

# class WeekDayError(Exception):
#     pass
	

# class Weeker:
#     '''A class used to manipulate dates of the week
    
#     Accepts the following values:
#     'Mon Tue Wed Thu Fri Sat Sun'
    
#     Allows to add or subtract days with add_days and subtract_days methods and returns the final day of the week as a result.
#     '''

#     def __init__(self, day):
#         self.weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#         if day in self.weekdays:
#             self.current_day = day
#         else:
#             raise WeekDayError
        
#     def __str__(self):
#         return f'{self.current_day}'

#     def add_days(self, n):
#         current_index = self.weekdays.index(self.current_day)
#         shift_number = n % 7
#         final_index = current_index + shift_number
#         self.current_day = self.weekdays[final_index]
#         return self.current_day

#     def subtract_days(self, n):
#         current_index = self.weekdays.index(self.current_day)
#         shift_number = n % 7
#         final_index = current_index - shift_number
#         if final_index < 0:
#             final_index = 7 - (abs(final_index))
#         self.current_day = self.weekdays[final_index]
#         return self.current_day
# try:
#     weekday = Weeker('Mon')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Monday')
# except WeekDayError:
#     print("Sorry, I can't serve your request.")


#Edube - Classes labs - 3


# import math

# ###I obviously had to Google these things as Edube site hinted, but I've managed to do it - pretty satisfying :))

# class Point:
#     '''A class which stores a point with (x, y) coordinates and allows to use the following methods:
    
#     - getx() - returns the value of x coordinate
#     - gety() - returns the value of y coordinate
#     - distance_from_xy - calculates the distance from a given point, given the coordinates
#     - distance from point - calculates the distance from a given point, given the point
     
#     '''
#     def __init__(self, x: float = 0.0, y: float = 0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         '''Returns the value of x coordinate'''
#         return self.__x

#     def gety(self):
#         '''Returns the value of y coordinate'''
#         return self.__y

#     def distance_from_xy(self, x, y) -> float:
#         '''calculates the distance from a given point, given the coordinates
        
#         args:
#         x, y - float values
        
#         returns:
#         float value
#         '''
#         distance = math.hypot(self.__x, self.__y)
#         return distance
        
#     def distance_from_point(self, point) -> float:
#         x = point.getx()
#         y = point.gety()
#         distance = math.hypot(x, y)

#         return distance



# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.point1 = vertice1
#         self.point2 = vertice2
#         self.point3 = vertice3

#     def perimeter(self):
        
#         '''Calculates the perimeter with the use of vertices (x1y1, x2y2, x3y3)'''
        
#         x1 = self.point1.getx()
#         x2 = self.point2.getx()
#         x3 = self.point3.getx()
#         y1 = self.point1.gety()
#         y2 = self.point2.gety()
#         y3 = self.point3.gety()
#         ab = math.sqrt((x1 - x2)**2 + (y1 - y2) ** 2)
#         bc = math.sqrt((x3 - x2)**2 + (y3 - y2) ** 2)
#         ca = math.sqrt((x1 - x3)**2 + (y3 - y1) ** 2)
        
#         perimeter = ab + bc + ca
#         return perimeter


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())


#W7 D3 T1

# import logging
# import sys

# logger = logging.getLogger('exc_test')
# logger.setLevel(logging.DEBUG)
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# try:
#     result = 1 / 0
# except ZeroDivisionError:
#     logger.error("error() call")
#     logger.exception("exception() call")


#W7 D3 T3

# class BankAccount:
#     _interest_rate = 0.05

#     def __init__(self, owner: str, balance: float) -> None:
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount: float) -> None:
#         self.balance += amount

#     def __repr__(self) -> str:
#         return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


# acc = BankAccount("Alice", 1000.0)
# acc.nickname = "main account"   # attribute added from outside the class
# acc._internal_note = "VIP"      # protected attribute added from outside

# print(acc.__dict__)
# print(BankAccount.__dict__)

# print(hasattr(acc, 'nickname'))
# print(getattr(acc, 'credit_limit', 'No credit limit attribute!'))
# print(setattr(acc, 'balance', 1500.0))
# print(getattr(acc, 'balance'))

# print(acc.__dict__)
# attribute_names = [attribute for attribute in acc.__dict__ if attribute.startswith('_')]
# print(attribute_names)

#Crappy Data Python W2 D4
# students = "anna kowalska; piotr nowak; KATARZYNA zielinska; marek WÓJCIK; ola kaczmarek; tomasz lewandowski; JULIA król; pawel adamski; agnieszka dabrowska; michal zielinski; john smith; Piotr Konrad"
# students = students.split(';')
# students = [student.strip().title() for student in students]
# print(students)

#W7 D4 T1

# import logging
# import sys

# logger = logging.getLogger('final_fix')
# logger.setLevel(logging.DEBUG)
# h = logging.StreamHandler(sys.stdout)
# h.setLevel(logging.DEBUG)
# h.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
# logger.addHandler(h)

# print("--- before try ---")
# try:
#     x = int("not_a_number")
# except ValueError:
#     logger.error("error() was called")
#     logger.exception("exception() was called")
# print("--- after try ---")


#W7 D4 T2
# import logging
# import sys

# def build_logger(name: str, filepath: str, level: int = logging.INFO) -> logging.Logger:
    
#     if logging.getLogger(name).handlers:
#         return logging.getLogger(name)
    
#     else:
#         root = logging.getLogger(name)
#         root.setLevel(level)
    
#         fmt = logging.Formatter('[%(levelname)s]: %(message)s')
        
#         console = logging.StreamHandler(sys.stdout)
#         console.setFormatter(fmt)
        
#         file_handler = logging.FileHandler(filepath)
#         file_handler.setFormatter(fmt)
        
#         root.addHandler(console)
#         root.addHandler(file_handler)
#         return logging.getLogger(name)


# logger = build_logger('logger_test', 'test.log')


# def safe_divide(a: float, b: float) -> float:
#     '''Function created to safely divide numbers and handle errors'''
#     try:
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             logger.warning(f'Value error: one of your values is not a number!')
#             raise ValueError('One of your values is not a number')
#         result = a / b

#     except ZeroDivisionError as e:
#         logger.error(f'Zero Division error: {str(e)}')
    
#     else:
#         logger.info('The division was successful')
#         return result
        

# x = safe_divide(5, 0)
# print(x)
# x = safe_divide('X', 5)
# print(x)
# x = safe_divide(10, 2)
# print(x)

#W7 D4 T3
# try:
#     raise ValueError("bad value")
# except Exception as e: #we will see this
#     print("Exception:", e)
# except ValueError as e:
#     print("ValueError:", e)


# try:
#     x = int("abc")
# except (ValueError, TypeError) as e:
#     print(type(e).__name__, "caught")



#W7 D4 T4
# def parse_trade_log(line: str) -> dict:
#     '''Function used to parse a trade log from a raw line format
#         e.g. "2026-02-18,AAPL,BUY,150.25,100"
        
#         to a nice dict as in:
#         {"date": "2026-02-18", "ticker": "AAPL", "side": "BUY", "price": 150.25, "qty": 100}
#     '''
    
#     values = line.split(',')
#     stripped_values = [value.strip() for value in values]
    
#     if not len(stripped_values) == 5:
#         raise ValueError('Line must have exactly 5 fields!')
    
#     final_dict = {
#         'date': stripped_values[0],
#         'ticker': stripped_values[1],
#         'side': stripped_values[2],
#         'price': float(stripped_values[3]),
#         'qty': int(stripped_values[4])
#     }
    
#     return final_dict

# x = parse_trade_log("2026-02-18,AAPL,BUY,150.25,100")
# print(x)

# x = parse_trade_log("2026-02-18,   AAPL  ,XD , 444.44,  100")
# print(x)


#W7 D4 T6

# from functools import wraps
# import logging

# def log_calls(func):
#     '''A decorator that logs every function before and after the call'''
#     @wraps(func)
#     def wrapper(*args):
#         logger = logging.getLogger(__name__)
#         logger.setLevel(logging.DEBUG)
#         logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]: %(message)s')
#         logger.debug(f'Function {func.__name__} called with args {args}')
#         try:
#             if not all(isinstance(arg, int) for arg in args):
#                 raise ValueError
#             result = func(*args)
#             logger.info(f'{func.__name__} returned {result}')
#             return result
#         except ValueError as e:
#             logger.exception(f'ValueError in {func.__name__}: expected numbers and got {args}')
#     return wrapper


# @log_calls
# def func_multiply(a: int, b: int) -> int:
#     result = a * b
#     return result


# x = func_multiply(5, 3)
# y = func_multiply('x', 3)

# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = (msg,)


# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)


# print(True or False)


#W7 D5 T2

# import logging
# import sys

# def build_logger(name: str, filepath: str, level: int = logging.INFO) -> logging.Logger:
    
#     if logging.getLogger(name).handlers:
#         return logging.getLogger(name)
    
#     else:
#         root = logging.getLogger(name)
#         root.setLevel(level)
    
#         fmt = logging.Formatter('[%(levelname)s]: %(message)s')
        
#         console = logging.StreamHandler(sys.stdout)
#         console.setFormatter(fmt)
        
#         file_handler = logging.FileHandler(filepath)
#         file_handler.setFormatter(fmt)
        
#         root.addHandler(console)
#         root.addHandler(file_handler)
#         return logging.getLogger(name)


# logger = build_logger('logger_test', 'test.log')


# def safe_divide(a: float, b: float) -> float:
#     '''Function created to safely divide numbers and handle errors'''
#     try:
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise ValueError
#         result = a / b
        
#     except ValueError as e:
#         logger.warning('Invalid input %s', e)
#     except ZeroDivisionError as e:
#         logger.error('Division by zero: %s / %s', a, b)
    
#     else:
#         logger.info('The division was successful')
#         return result
    
    
# x = safe_divide(5, 0)
# print(x)
# x = safe_divide(5, 'XD')
# print(x)
# x = safe_divide(5, 2)
# print(x)

#W7 D5 T3

# from algo_backtest.engine.position import Position
# position = Position('DAX', 'BUY', 24600, 5)




# def audit_object(obj: object) -> dict:
    
#     object_name = type(obj).__name__
#     instance_attributes = obj.__dict__
#     others = type(obj).__dict__
#     print(f'The class name of the object is {object_name}')
#     print(f'The instance attributes of this class instance are: {instance_attributes}')
#     print(f'The private attributes are: {[attribute for attribute in instance_attributes if str(attribute).startswith('_')]}')
#     has_repr = True if '__repr__' in others else False
#     print(f'The object has a __repr__ method: {has_repr}')


# x = audit_object(position)
    
    
# try:
#     raise ValueError("oops")
# except Exception:
#     print("A")
# except ValueError:
#     print("B")
# finally:
#     print("C")


#W7 D5 T5

# def make_validator(min_val: float, max_val: float):
#     '''A fuctory function that creates validators with min and max value to check any number'''
#     def validate(value: float):
#         result = (value >= min_val) and (value <= max_val)
#         return result
#     return validate


# x = make_validator(10, 20)
# print(x(15))
# print(x(1))
# print(x(555))

# is_valid_price = make_validator(0.01, 10000.0)
# print(is_valid_price(4343434))
# print(is_valid_price(43))
# print(is_valid_price(-1))

# print(isinstance(True, int))\

#W8 D1 T1

# a = (1, [2, 3], 4)
# a[1].append(5)
# print(a)

# print(type(lambda: None).__name__)


#W8 D1 T2

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner

# f = outer()
# print(f())


# def make_accumulator(factor):
#     items = []
#     def add(x):
#         items.append(x * factor)
#         return items
#     return add

# acc = make_accumulator(10)
# acc(1)
# print(acc(2))


# def outer():
#     x = "outer"
#     def middle():
#         x = "middle"
#         def inner():
#             print(x)
#         inner()
#     middle()

# outer()


#W8 D1 T3

# class InvalidPriceError(ValueError):
#     '''A cusom exception based on ValueError that takes price + reason'''
#     def __init__(self, *args, reason: str, price: float):
#         super().__init__(*args)
#         self.price = price
#         self.reason = reason
        
#     def __str__(self):
#         return f'Invalid price 99.0: must be positive: {self.reason}, {self.price}'


# entry_price = -50.0
# quantity = 10
# try:
#     result = entry_price * quantity
#     if entry_price < 0:
#         raise InvalidPriceError(reason = 'XD', price = entry_price)
# except InvalidPriceError:
#     print(f'InvalidPriceError: Invalid price 99.0: must be positive: XD, {entry_price}')


#W8 D1 T4 - updated algo_backtest/engine/backtest_engine.py - added module level docstring


#W8 D1 T6 - broken decorator

# import logging

# def log_call(func):
#     def wrapper(*args):
#         logging.info("Calling %s", func.__name__) #this would return wrapper as the func name, and I reckon it's not what we want
#         result = func(*args) #we're calculating the result, but not returnign any
#         logging.info("Done")
#         return #lack of return
#     return func #wrong return

# #fixed version:


# import logging
# logging.basicConfig(level = logging.INFO)

# def log_call(func):
#     def wrapper(*args):
#         logging.info("Calling %s", func.__name__)
#         result = func(*args)
#         logging.info("Done")
#         return result
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b

# x = add(5, 15)
# print(x)


#W8 D1 T7 - full backtest in main.py
'''I'm not pasting the code, check main.py for reference - the backtest went successfully and I also had a chance
to fix a few imports + references in backtest_engine/position_manager'''



#W8 D2 T1

# class A:
#     def __init__(self):
#         self.x = 1

# class B(A):
#     def __init__(self):
#         self.y = 2

# b = B()
# print(b.x, b.y)

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) * 2
#     return wrapper

# @decorator
# @decorator
# def get_five():
#     return 5

# print(get_five())

# class C:
#     _x = 0

#     @classmethod
#     def increment(cls):
#         cls._x += 1

#     @staticmethod
#     def description():
#         return "I am C"

# C.increment()
# C.increment()
# print(C._x, C.description())

# try:
#     x = int("abc")
# except (ValueError, TypeError) as e:
#     print(type(e).__name__)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# a = Node(1)
# b = Node(2)
# a.next = b
# b.next = a

# print(a.next.next.val)


#W8 D2 T2

# #Erratic class chain - bug identification
# class Animal:
#     def __init__(self, name: str, sound: str):
#         self.name = name
#         self.sound = sound

#     def speak(self) -> str:
#         return f"{self.name} says {self.sound}"
# #everything ok up to this point

# class Dog(Animal):
#     def __init__(self, name: str, breed: str):
#         #ISSUE 1 - WE'RE NOT fetching name, sound from our parent class - this will be an issue in speak
#         self.breed = breed

#     def speak(self) -> str:
#         return super().speak() + f" (breed: {self.breed})"


# class GuideDog(Dog):
#     def __init__(self, name: str, breed: str, owner: str):
#         super().__init__(name, breed)
#         self.owner = owner

#     def speak(self) -> str:
#         return super().speak() + f" [guide dog for {self.owner}]"


# gd = GuideDog("Rex", "Labrador", "Alice")
# print(gd.speak())



#FIX

#Erratic class chain - bug identification
# class Animal:
#     def __init__(self, name: str, sound: str):
#         self.name = name
#         self.sound = sound

#     def speak(self) -> str:
#         return f"{self.name} says {self.sound}"
# #everything ok up to this point

# class Dog(Animal):
#     def __init__(self, name, sound, breed: str):
#         super().__init__(name, sound)
#         self.breed = breed

#     def speak(self) -> str:
#         return super().speak() + f" (breed: {self.breed})"
    
# #fixed this now


# class GuideDog(Dog):
#     def __init__(self, name: str, sound: str, breed: str, owner: str):
#         super().__init__(name, breed, sound)
#         self.owner = owner

#     def speak(self) -> str:
#         return super().speak() + f" [guide dog for {self.owner}]"


# dog = Dog('Johny', 'Woof', 'Labrador')
# print(dog.speak())

# gd = GuideDog("Rex", 'Woof', "Labrador", "Alice")
# print(gd.speak())


# a = [1, 2, 3]
# b = a[:]
# a[0] = 99
# print(b[0])


# class A:
#     def method(self):
#         return "A"

# class B(A):
#     pass

# class C(A):
#     def method(self):
#         return "C"

# class D(B, C):
#     pass

# print(D().method())


# def f(a, b, /, c, d):
#     return a + b + c + d

# print(f(1, 2, c=3, d=4))


# class A:
#     def __init__(self):
#         self.__x = 10

#     def get_x(self):
#         return self.__x

# a = A()
# print(a.get_x(), a._A__x)

#W8 D2 T4

# class Countdown:
#     '''A practice iterator class which takes the following args:
    
#     start: int
    
#     It yields values from start down to 1 inclusive, and then raises StopIteration,
#     but the value can be reset by calling .reset() method.
#     '''
    
#     def __init__(self, start: int):
#         self.start = start
#         self.current = start
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < 1:
#             raise StopIteration
#         else:
#             value = self.current
#             self.current -= 1
#             return value
    
#     def reset(self):
#         self.current = self.start
#         print('Restored the current value to the starting value.')
    
    

# for x in Countdown(5):
#     print(x)

# print(list(Countdown(4)))
# print(list(Countdown(7)))

#W8 D2 T5 - identifying issues & refactoring
# def load_price(filepath):
#     try:
#         f = open(filepath) #lack of opening mode + lack of context manager
#         data = f.read()  #this is just the effect of choosing the above way
#         f.close() #THIS IS NECESSARY HERE, BUT IT'S A FAULTY APPROACH, AN OLD-STYLE WHICH CAUSES US TO USE THIS
#         return float(data.strip()) #this is weird, but maybe we need float, who knows
#     except:
#         return None #LACK OF ERROR HANDLING
    
# #fixed version

# def load_price(filepath):
#     try:
#         with open(filepath, 'r') as r:
#             data = r.read()
#             return float(data.strip())
#     except FileNotFoundError:
#         print('File not found!')
#     except Exception as e:
#         print(f'Unexpected exception: {str(e)}')
    

# class Account:
#     balance = 0

# a1 = Account()
# a2 = Account()
# a1.balance += 100
# print(a1.balance, a2.balance) #100 0


# class Account:
#     balance = 0

# a1 = Account()
# a2 = Account()
# Account.balance += 100
# print(a1.balance, a2.balance) #100 100

#Crappy Data Python
# lista = [5, 2, 6, 4, 2, 9, 6, 3, 8, 1, 7, 2, 6, 10, 4, 2, 11, 6, 13, 2, 14, 6, 15, 2, 16]

# lista.pop(3)
# lista.pop(lista.index(6))
# lista.insert(2, 8)
# print(lista)
# lista.reverse()
# print(lista)
# find_index = lista.index(2)
# print(find_index)
# len_lista = len(lista)

#W8 D3 T1

# def f(a, b=2, *args, c=3):
#     print(a, b, c, args)

# f(1, 4, 5, 6, c=10)


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.__mro__)

# a = {"x": 1}
# b = a.copy()
# b["x"] = 99
# b["y"] = 2
# print(a)

# def gen(n):
#     for i in range(n):
#         yield i * i

# g = gen(5)
# print(next(g), next(g), sum(g))


#W8 D3 T2 - engine/trade.py small tweaks
# - removed print(trades_profits)
# - init exit reason changed to .lower() for consistency with other modules

#W8 D3 T3  - engine/trade.py + backtest_engine.py
# - added R multiple as a property

#W8 D3 T4 - Continuation - added strategy_id + strategy_name
#It required multiple checks and modifications in all of the components (backtest_engine, position, position_manager, trade)
#and I'm unable to list them all here, but generally speaking I've added strategy id/name wherever needed
#and created a test in main.py which ran with success

# zip([1,2,3], [4,5])

#W8 D3 T6
# def f(x):
#     return x * 2

# result = map(f, [1, 2, 3])
# print(result) #map memory object - we'd need to wrap it in a list to see the actual values
# print(list(result)) #[2, 4, 6]
# print(list(result)) #[]


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# d = (*a, *b)
# print(type(c).__name__, type(d).__name__)


#W8 D4 T1

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(list(zip(a, b)))
# print(list(zip(*zip(a, b))))


# class C:
#     def __init__(self, val):
#         self._val = val
#     def __repr__(self):
#         return f'C({self._val!r})'

# items = [C(3), C(1), C(2)]
# items.sort(key=lambda c: c._val)
# print(items)

#W8 D4 T2 - added two new methods in algo_backtest/engine/backtest_engine.py

'''trades_by_strategy filters trades based on their strategy

    strategy_report calls trades_by_strategy and prints out a report with division based on strategies and a total report
    
    Currently the report is rather minimalistic but I will definitely be testing and updating it as soon as we get the project ready and work on real data (soon)
'''

    # def trades_by_strategy(self) -> dict[str, list[Trade]]:
    #     '''Method used to filter trades based on their strategy - it can be called explicitly and/or its return may be eventually added to Class attributes, 
    #     but for now it just returns the dict, and we will use it in strategy_report without adding extra Class attributes
        
    #     Args:
    #     None - we use the self.completed_trades from our Class instance
        
    #     Returns:
    #     A dict where each strategy_id represents a key, and its trades are represented as a list.
        
    #     e.g 
        
    #     {'432': [Trade(position_id='957d8746-f5c1-4c9e-93df-2342e2a316d6', ticker='EURUSD', side='BUY', entry_price=105.6, exit_price=104.2, quantity=10000, pnl=-14000.00, exit_reason='still open', strategy_id='432', strategy_name='Super XD'), 
    #     Trade(position_id='e14c1475-c77b-4683-90cd-fda6946f42dd', ticker='EURUSD', side='SELL', entry_price=105.6, exit_price=104.2, quantity=10000, pnl=14000.00, exit_reason='still open', strategy_id='432', strategy_name='Super XD')]}
    #     '''
        
    #     if not self.completed_trades:
    #         logger.info(f'There are no completed trades in self.completed_trades, and we cannot proceed with filtering them by the strategy.')
    #         return None
    #     else:
    #         strategies_set = set([(trade.strategy_id, trade.strategy_name) for trade in self.completed_trades])
    #         completed_trades_by_strategy = {}
    #         for strategy in strategies_set:
    #             filtered_trades = [trade for trade in self.completed_trades if trade.strategy_id == strategy[0]]
    #             completed_trades_by_strategy[strategy] = filtered_trades
    #         return completed_trades_by_strategy
        
    # def strategy_report(self):
    #     '''Method used to call trades_by_strategy method to get filtered trades and print out a report with stats for every strategy and portfolio total'''
        
    #     trades_filtered_by_strategy = self.trades_by_strategy()
    #     for strategy in trades_filtered_by_strategy:
    #         total_pnl = round(sum([trade.pnl for trade in trades_filtered_by_strategy[strategy]]), 2)
    #         win_rate = Trade.calculate_win_rate(trades_filtered_by_strategy[strategy])
    #         avg_r = sum(trade.r_multiple for trade in trades_filtered_by_strategy[strategy]) / len(trades_filtered_by_strategy[strategy])
    #         print(f'''{3* '-'} {strategy[0]} (ID: {strategy[1]}) {3* '-'}
                  
    #               Trades: {len(trades_filtered_by_strategy[strategy])}
    #               Win Rate: {win_rate}%
    #               Total PnL: ${total_pnl:.2f}
    #               Avg R: {avg_r:.2f}R
                  
    #               ''')
    #     print(f'''{3* '-'} PORTFOLIO TOTAL  {3* '-'}
                  
    #               Trades: {len(self.completed_trades)}
    #               Win Rate: {self.win_rate}%
    #               Total PnL: ${self.total_pnl}
    #               Avg R: {round(sum(trade.r_multiple for trade in self.completed_trades) / len(self.completed_trades), 2)}R
                  
    #               ''')
    


#W8 D4 T3

# class A:
#     def __init__(self):
#         self.__x = 10

# a = A()
# a.__x = 99
# print(a.__x, a._A__x)

# x = {1, 2, 3}
# y = {2, 3, 4}
# print(x & y, x | y, x - y)

# def f(x: int) -> str:
#     return x * 2

# print(f("hello"))

#W8 D4 T5

# x = [1, 2, 3]
# y = x
# x = x + [4]
# print(y)

# def f(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = f(n-1) + f(n-2)
#     return memo[n]

#Edube - Module 4 - exercises

#1
# any_list = [1, 2, 3, 4]
# even_list = list(map(lambda x: x + 1 if x % 2 == 0 else x, any_list))
# print(even_list)
# x = list(map(lambda n: n | 1, any_list)) #This is the solution proposed by Edube - | is an operator I didn't know.
# print(x)

#2
# def replace_spaces(replacement='*'):
#     def new_replacement(text):
#         return text.replace(' ', replacement)
#     return new_replacement


# stars = replace_spaces()
# print(stars("And Now for Something Completely Different"))

#W8 D5 T1

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# class Poodle(Dog):
#     pass

# p = Poodle()
# print(isinstance(p, Animal), isinstance(p, Dog), isinstance(p, Poodle))

# xs = [10, 20, 30, 40, 50]
# result = sorted(xs, key=lambda x: x % 3)
# print(result)

# class A: pass
# class B(A): pass
# class C(B): pass

# obj = C()
# print(issubclass(C, A), issubclass(A, C), isinstance(obj, A))


#W8 D5 T2

# def f(x=[]):
#     x.append(1)
#     return x

# print(f())
# print(f())
# print(f([]))
# print(f())


# x = 5
# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner

# outer()()


# try:
#     raise ValueError("bad")
# except ValueError as e:
#     result = str(e)
# finally:
#     result = "cleaned"

# print(result) #'cleaned'


# class Meta(type):
#     def __new__(mcs, name, bases, namespace):
#         namespace['greeting'] = 'hello'
#         return super().__new__(mcs, name, bases, namespace)

# class Foo(metaclass=Meta):
#     pass

# print(Foo.greeting)


#W8 D5 T3

# gen = (x * 2 for x in range(5))
# print(3 in gen)
# print(list(gen))


# x = [1, 2, 3]
# y = x[:]
# y.append(4)
# print(x, y)

# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))
# g2 = iter(g)
# print(g is g2)

# xs = [1, 2, 3, 4, 5]
# evens = filter(lambda x: x % 2 == 0, xs)
# print(list(evens))
# print(list(evens))


# def f(*args, **kwargs):
#     print(type(args), type(kwargs))

# f(1, 2, a=3)

# class C:
#     def __init__(self, x):
#         self.x = x
#     def __eq__(self, other):
#         return self.x == other.x

# a = C(1)
# b = C(1)
# c = a
# print(a == b, a is b, a is c)

# import sys
# xs = list(range(1000))
# gen = (x for x in range(1000))
# print(sys.getsizeof(xs) > sys.getsizeof(gen))

#W8 D5 T4 - backtest_engine.py
#Added repr and verified it by testing what repr and str print in main.py


#W8 D5 T5
# def deco_a(f):
#     def wrapper():
#         print("A in")
#         f()
#         print("A out")
#     return wrapper

# def deco_b(f):
#     def wrapper():
#         print("B in")
#         f()
#         print("B out")
#     return wrapper

# @deco_a
# @deco_b
# def hello():
#     print("hello")

# hello()


# try:
#     x = int("abc")
# except (ValueError, TypeError) as e:
#     print(type(e).__name__)
# else:
#     print("no error")
# finally:
#     print("done")

# class CustomError(Exception):
#     pass

# try:
#     raise CustomError("oops")
# except Exception as e:
#     print(isinstance(e, CustomError), isinstance(e, Exception)) #True True


# x = [2, 5, 8]
# x.append(6)
# x.insert(0, 7)
# x.sort()
# x[0]

# del x[4]
# print(x)


# x = (2, "text", 3)
# x.index(3)
# x.count(2)
# x.insert(0, 'xd')

# uczniowie = ('aleksander', 'adam', 'seweryn', 'bartosz', 'tomasz')

# uczniowie_tuple = tuple(('aleksander', 'adam', 'seweryn', 'bartosz', 'tomasz'))
# print(uczniowie_tuple)


# class C:
#     @property
#     def x(self):
#         return self.x

# c = C()
# print(c.x)
# 

# a_set = {1, 2, 3}
# a_set.add(56)
# print(a_set) #{1, 2, 3, 56}
# b_set = {4, 5, 6}
# print(a_set.update(b_set))
# print(a_set)

#W9 D1

# def f(*args, **kwargs):
#     print(args, kwargs)

# xs = [10, 20]
# d = {'a': 1, 'b': 2}
# f(*xs, **d)


# f([10, 20], {'a': 1})


# xs = "hello"
# print(xs.find("x"), xs.index("l"))

# s = "  hello  world  "
# print(s.strip().split())

# s = "aabbccdd"
# print(s.replace("b", "X", 1))


# parts = ["a", "b", "c"]
# print("-".join(parts))
# print("".join(reversed(parts)))


# class C:
#     x = 0

#     def increment(self):
#         self.x += 1

# c1 = C()
# c2 = C()
# c1.increment()
# c1.increment()
# print(C.x, c1.x, c2.x)


# students_scores = {"anna kowalska":8.5,"piotr nowak":6.2,"marta wisniewska":9.1,"tomasz kaczmarek":4.7,"karolina mazur":7.8,"jakub zielinski":5.3,"agnieszka lewandowska":9.9,"pawel szymanski":3.4,"katarzyna wojcik":8.0,"marcin kaminska":6.6,"monika dabrowska":7.2,"lukasz piotrkowski":2.9,"aleksandra adamska":9.4,"bartosz grabowski":5.8,"natalia pawlak":8.7,"krzysztof michalski":4.1,"dorota krol":6.9,"sebastian jablonski":7.5,"weronika wrobel":9.0,"mateusz czarnecki":3.8,"joanna stefanska":8.3,"damian kubiak":5.0,"klaudia piotrowska":7.1,"adrian lis":6.4,"patrycja baran":9.6}
# students = [student for student in students_scores.items() if student[1] > 6.0]
# print(students)


#W9 D3 -  T1

# def make_adder(n):
#     def add(x):
#         return x + n
#     n = n * 10
#     return add

# fn = make_adder(3)
# print(fn(1))

#W9 D3 -  T2

# try:
#     raise FileNotFoundError("no file")
# except Exception:
#     print("A") #this will be printed
# except OSError:
#     print("B")
# except FileNotFoundError:
#     print("C")
    
    
# try:
#     open("x.txt")
# except FileNotFoundError:
#     print("file missing")
# except Exception:
#     print("generic")


# try:
#     raise KeyError("k")
# except LookupError:
#     print("LookupError")
# except KeyError:
#     print("KeyError")

#W9 D3 -  T3
# def f():
#     print(val)
#     val = 5

# f() #UNBOUNDLOCALEERROR

# def f():
#     print(val)

# f() #NAMEERROR

'''It seems that UnboundLocalError relates to situations where a given name is occupied/defined, but it's defined later. 
It seems that it still precreates a memory object or something like that, that makes it an UnboundLocalError before a given variable/name is actually defined. 
Anyway, for me this is a sign that the variables/object names are prechecked to check if they exist, before they are checked again to check their values. Interesting.

As for NameError, it simply occurs when a given name is not defined.'''


#W9 D3 -  T4
# class A:
#     data = []

# class B(A):
#     pass

# B.data.append(1)
# A.data.append(2)
# print(A.data, B.data) #[1, 2] [1, 2]

# import logging
# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger("test")
# logger.setLevel(logging.DEBUG)
# logger.debug("debug msg") #printed, this logger is not affected by the basicconfig setting
# logger.warning("warn msg") #printed


# try:
#     raise RuntimeError("r")
# except RuntimeError as e:
#     err = e

# print(err)

# xs = list(range(5))
# it = iter(xs)
# next(it)
# next(it)
# print(list(it)) #[2, 3, 4]


# multipliers = []
# for n in [1, 2, 3]:
#     multipliers.append(lambda x: x * n)

# print([m(10) for m in multipliers])  #[30, 30, 30]


# def make_fns():
#     result = []
#     for i in range(4):
#         def fn(i=i):
#             return i ** 2
#         result.append(fn)
#     return result

# print([f() for f in make_fns()]) #[0, 1, 4, 9]


#Edube - Module 4 - File I/O practice

#readline()
# stream = open('text.txt', 'r')
# x = stream.readline(20)
# y = stream.readline(20)
# z = stream.readline(20)
# a = stream.readline(20)
# b = stream.readline(20)

# '''
# If we use readline and set a limit of bytes and it will not print out a given line's content,
# in the next call of readline() we will continue with the previous line's content, e.g.
# '''

# print(x) #timestamp,ticker,ope
# print(y) #n,high,low,close,vol
# print(z) #ume
# print(a) #2024-01-01 09:00:00,
# print(b) #EURUSD,100.50,101.20
# stream.close()

# '''If we set enough bytes as limit in readlines,
# it will properly print full content of a given line
# And we will not exceed that'''

# #Example below:
# stream = open('text.txt', 'r')
# x = stream.readline(120)
# y = stream.readline(120)
# z = stream.readline(120)
# a = stream.readline(120)
# b = stream.readline(120)

# print(x) #timestamp,ticker,open,high,low,close,volume
# print(y) #2024-01-01 09:00:00,EURUSD,100.50,101.20,100.10,100.80,15000
# print(z) #2024-01-01 09:01:00,EURUSD,100.80,101.50,100.70,101.30,18000
# print(a) #2024-01-01 09:02:00,EURUSD,101.30,101.80,101.00,101.50,22000
# print(b) #2024-01-01 09:03:00,EURUSD,101.50,102.00,101.20,101.90,25000
# stream.close()


# from os import strerror

# try:
# 	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
# 	for i in range(10):
# 		s = f'line #{i + 1}\n'
#   #"line #" + str(i+1) + "\n"
# 		for ch in s:
# 			fo.write(ch)
# 	fo.close()
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))

# import sys
# sys.stderr.write("Error message") #the stderr stream is automatically written, no need to open anything



# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 - i

# for b in data:
#     print(hex(b))


# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.


# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

# # Your code that reads bytes from the stream should go here.


# from os import strerror

# try:
#     bf = open('file.bin', 'rb')
#     data = bytearray(bf.read())
#     bf.close()

#     for b in data:
#         print(hex(b), end=' ')

# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))




#Edube - Module 4 - File IO - Labs #1

'''
Level of difficulty
Medium

Objectives
improving the student's skills in operating with files (reading)
using data collections for counting numerous data.
Scenario
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt

the expected output should look as follows:

a -> 1
b -> 1
c -> 1

'''


# from os import strerror
# from collections import defaultdict

# file_name = input('Please input the file name e.g. (file.txt): ')
# try:
#     with open(file_name, 'w') as w:
#         w.write('aBc')
# except IOError as exc:
#     print(f'IOError occured: {strerror(exc.errno)}')
    
# letters_count = defaultdict(int)
# try:
#     r = open(file_name, 'r')
#     read = r.read()
#     print(read)
#     for char in read:
#         char = char.lower()
#         if char.isalpha():
#             letters_count[char] += 1
#             print(f'{char} -> 1')
#         else:
#             continue
#     r.close()
#     letters_count = sorted(letters_count.keys())
#     print(letters_count)
# except IOError as e: 
#     print(f'IOError: {strerror(e.errno)}')


#Edube - Module 4 - File IO - Labs #2

'''
Level of difficulty
Medium

Prerequisites
4.3.1.15

Objectives
improve the student's skills in operating with files (reading/writing)
using lambdas to change the sort order.
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

'''



# from os import strerror
# from collections import defaultdict

# file_name = input('Please input the file name e.g. (file.txt): ')

# try:
#     with open(file_name, 'w') as w:
#         w.write('cBabAafdsa3092mkvcaddASDK32dt45t4vcxxz')
# except IOError as exc:
#     print(f'IOError occured: {strerror(exc.errno)}')


# letters_count = defaultdict(int)
# try:
#     r = open(file_name, 'r')
#     read = r.read()
#     print(read)
#     for char in read:
#         char = char.lower()
#         if char.isalpha():
#             letters_count[char] += 1
#         else:
#             continue
#     r.close()
#     print(letters_count)
#     letters_count = sorted(letters_count.items(), key = lambda x: x[1], reverse = True)
#     for item, value in letters_count:
#         print(f'{item} -> {value}\n')

#     new_filename_core = file_name.split('.')[0]
#     with open(f'{new_filename_core}.hist', 'w') as w:
#         for item, value in letters_count:
#             w.write(f'{item} -> {value}\n')

# except IOError as e: 
#     print(f'IOError: {strerror(e.errno)}')
    
    
   
#Edube - Module 4 - File IO - Labs #3


# class StudentsDataException(Exception):
#     pass


# class BadLine(StudentsDataException):
#     def __init__(self, line_content):
#         self.line_content = line_content
#         super().__init__(f'Bad line: {line_content.strip()}')

# class FileEmpty(StudentsDataException):
#     def __init__(self, filename):
#         self.filename = filename
#         super().__init__(f'FileEmpty: The file {filename} is empty!')

# grades_dict = {}
# filename = 'jekyll.txt'

# try:
#     with open(filename, 'r') as r:
#         if not r:
#             raise FileEmpty(filename)
#         for line in r:
#             contents = line.split()
#             if len(contents) != 3:
#                 raise BadLine(contents)
#             name = contents[0] + ' ' + contents[1]
#             if not name in grades_dict:
#                 grades_dict.update({name : float(contents[2])})
#             else:
#                 grades_dict[name] += float(contents[2])
                
#         grades_dict = sorted(grades_dict.items(), key = lambda x: x[0])
#         for student, grades_sum in grades_dict:
#             print(f'''{student}: {grades_sum}''')
        
#         print(grades_dict)
# except FileNotFoundError:
#     print(f'Error: The file {filename} does not exist')
# except FileEmpty as e:
#     print(f'Error: {str(e)}')
# except BadLine as e:
#     print(f'Error: {str(e)}')
    
    

#W9 D4 T1

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.warning("warn")
# logging.debug("debug")


# import logging

# parent = logging.getLogger("app")
# child  = logging.getLogger("app.module")

# parent.setLevel(logging.WARNING)
# child.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# parent.addHandler(handler)

# child.info("info from child")
# child.warning("warning from child")


#W9 D4 T2


# total = 0

# def add(n):
#     total += n
#     return total

# add(5) #UnboundLocalError


# items = []

# def append_item(x):
#     items.append(x)

# append_item(1)
# print(items) #[1]



# def outer():
#     x = 0
#     def inner():
#         x += 1
#         return x
#     return inner()

# outer() #UnboundLocalError

#W9 D4 T3


# def make_multiplier(n):
#     n = n * 3
#     def fn(x):
#         return x * n
#     return fn

# f = make_multiplier(4)
# print(f(2)) --> 24

# def outer(a, b):
#     result = a + b
#     result = result * 2
#     def inner():
#         return result
#     return inner

# fn = outer(3, 4)
# print(fn()) 


# def factory(val):
#     val += 10
#     val *= 2
#     def fn():
#         return val
#     return fn

# g = factory(5)
# print(g()) #30


# def build(n):
#     def step1():
#         return n + 1
#     n = n * 10
#     return step1

# h = build(3)
# print(h()) #31


#W9 D4 T4
# try:
#     x = int("abc")
# except (ValueError, TypeError) as e:
#     print(type(e).__name__)


# gen = (x * x for x in range(5))
# print(3 in gen) #False
# print(list(gen)) #[]


# from os import strerror
# import errno

# print(IOError is OSError)
# print(EnvironmentError is OSError)


# try:
#     stream = open("image.png", "rb")
#     image = bytearray(stream.read())
#     stream.close()
# except IOError:
#     print("failed")
# else:
#     print("success")


#Edube - Module 4 - os

# import os

# print(os.listdir())
# os.chdir('algo_backtest')
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())

# os.mkdir('testxd')
# print(os.listdir())
# os.chdir('testxd')
# os.chdir('../')
# os.rmdir('testxd')
# print(os.listdir())

# print(os.getcwd())


# import os
# os.system('pwd') #allows to run shell commands - returns 0 (exit status indicating success on Unix systems)


#Edube - Module 4 - os - Labs - #1

'''
you need to write a program that will search for directories in a given location.

Your program should meet the following requirements:

Write a function or method called find that takes two arguments called path and dir. 
The path argument should accept a relative or absolute path to a directory
where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. 
Your program should display the absolute paths if it finds a directory with the given name.
The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.

Creating the required test directory structure to be able to test everything properly'''

# os.makedirs('tree/c/other_courses/cpp')
# os.chdir('tree')
# os.makedirs('cpp/other_courses/c')
# os.makedirs('python/other_courses/c')
# os.chdir('c/other_courses')
# os.mkdir('python')
# os.chdir('../../')
# os.chdir('cpp/other_courses')
# os.mkdir('python')
# os.chdir('../../')
# os.chdir('python/other_courses')
# os.mkdir('cpp')
# os.chdir('../../')
# print(os.listdir())

# import os

# def find(path: str, dir: str) -> str:
#     '''A function that allows to find and list the absolute paths and finds the directory with a given name
#     It recursively searches all subdirectories in the given path
    
#     Args:
#         path: str = relative/absolute path to a dreictory where the search should start
#         dir: str = name of a directory that we want to find in a given path
#     '''
#     file_location = None
    
#     os.chdir(path)
#     folders = [directory for directory in os.listdir()]
#     print(folders)
#     if dir in folders:
#         print(f'Directory found in {os.getcwd()}')
#         file_location = os.getcwd()
#         return file_location
#     else:
#         for folder in folders:
#             os.chdir(folder)
#             print(f'Current directory: {os.getcwd()}')
#             print(f'{os.listdir()}')
#             current_folders = [directory for directory in os.listdir()]
#             if dir in current_folders:
#                 print(f'Directory found in {os.getcwd()}')
#                 file_location = os.getcwd()
#                 return file_location
#             else:
#                 os.chdir('../')
#         print('Directory not found!')            

# find(path="./tree", dir="xd")


#Edube - datetime review

# from datetime import date
# import time

# today = date.today()

# print("Today:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)

# timestamp = time.time() #in UNIX - the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC)
# print("Timestamp:", timestamp)

# d = date.fromtimestamp(timestamp)
# print("Date:", d)
# d = date.fromisoformat('2019-11-04')
# print(d)
# d = d.replace(year = 1995, month = 12, day = 22)
# print(d)


# d = date(2019, 11, 6)
# print(d.weekday())

# from datetime import time #it works differently than standard python module 'time'

# t = time(14, 53, 20, 1)

# print("Time:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)
# print("Microsecond:", t.microsecond)


# import time

# class Student:
#     def take_nap(self, seconds):
#         print("I'm very tired. I have to take a nap. See you later.")
#         time.sleep(seconds)
#         print("I slept well! I feel great!")

# student = Student()
# student.take_nap(5)


# import time

# timestamp = 1572879180
# x = time.ctime(timestamp) #converts time in secs since Jan 1, 1970 (Unix) to str

# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))


# st = time.gmtime(timestamp)

# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


# from datetime import datetime

# dt = datetime(2019, 11, 4, 14, 53)

# print("Datetime:", dt)
# print("Date:", dt.date())
# print("Time:", dt.time())

# from datetime import datetime

# print("today:", datetime.today())
# print("now:", datetime.now())
# print(f'Timestamp: {dt.timestamp()}')


# dt = datetime(2020, 10, 4, 14, 55)
# print("Timestamp:", dt.timestamp())

# from datetime import date, datetime
# d = datetime(2020, 1, 4, 15, 39, 10)
# print(d.strftime('%Y/%m/%d %H:%M:%S'))


# from datetime import time
# from datetime import datetime

# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))

# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%Y/%m/%d %H:%M:%S"))

# import time

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

# timestamp = 1572879180
# st = time.gmtime(timestamp)

# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
# datetime.strftime
# datetime.strptime


# from datetime import date
# from datetime import datetime

# d1 = date(2020, 11, 4) 
# d2 = date(2019, 11, 4)

# print(d1 - d2) #timedelta object, created automatically

# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)

# print(dt1 - dt2) #timedelta object, created automatically


# from datetime import timedelta

# delta = timedelta(weeks=2, days=2, hours=3)
# print(delta)
# print("Days:", delta.days)
# print("Seconds:", delta.seconds)
# print("Microseconds:", delta.microseconds)


# a = {"anna": 3, "ola": 5, "kinga": 1}
# a["anna"] = 4
# print(a["anna"])


# a = {"a"}
# b = {}
# print(type(a) == type(b))

# x = (1, 2)
# print(x[-1])

# x = {-1 : 'a'}
# print(x[-1])

# x = [8]
# print(x[-1])


# a = {1, 2, 3, 4}
# b = {4, 5, 6, 7}
# c = a.union(b)
# print(len(c))


#W9 D5 T1
# import logging

# logging.basicConfig(level=logging.INFO)   # root handler: INFO+

# logger = logging.getLogger("app")
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# handler.setLevel(logging.ERROR)
# logger.addHandler(handler)

# logger.info("info") #INFO:app:info - root handler prints this, named handler does not
# logger.error("error") #error / ERROR:app:error - printed both by the named handler and the root handler


# import logging

# logging.basicConfig(level=logging.WARNING)  # root handler: WARNING+

# logger = logging.getLogger("app")
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# logger.debug("debug")
# logger.warning("warn")


# import logging

# logging.basicConfig(level=logging.DEBUG)

# logger = logging.getLogger("app")
# logger.setLevel(logging.DEBUG)
# logger.propagate = False             # <-- notice this

# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# logger.info("info")
# logger.error("error")

# import logging

# parent = logging.getLogger("app")
# child  = logging.getLogger("app.module")

# parent.setLevel(logging.DEBUG)
# child.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# parent.addHandler(handler)

# child.warning("warn from child")



# import logging

# logging.basicConfig(level=logging.DEBUG)

# logger = logging.getLogger("app")
# # No setLevel called on logger
# # No handlers added to logger

# logger.debug("debug")
# logger.warning("warn")

# #
# import logging

# logging.basicConfig(level=logging.ERROR)

# logger = logging.getLogger("app")
# logger.setLevel(logging.DEBUG)

# h1 = logging.StreamHandler()
# h1.setLevel(logging.WARNING)
# logger.addHandler(h1)

# logger.warning("warn")
# logger.error("error")
# logger.critical("critical")

#W9 D5 T2

# print(round(0.1 + 0.2, 10) == round(0.3, 10))


# a = 0.1
# b = 0.1
# c = 0.1
# print(a + b + c == 0.3)
# print(a + b + c)
# 


#W9 D5 T3

# a, *b, c = (1, 2, 3, 4, 5)
# print(type(b), b)

# first, *rest = "hello"
# print(type(rest), rest)

# *a, b = [10
#          ]
# print(a, b)

# x, *y, z = range(5)
# print(x, y, z)

#W9 D5 T5

# try:
#     open("nofile.txt")
# except Exception:
#     print("Exception") #exception gets printed, as it's first
# except FileNotFoundError:
#     print("FileNotFoundError")

# try:
#     raise ValueError("v")
# except (TypeError, ValueError):
#     print("caught")
# except Exception:
#     print("exception")

# gen = (i for i in range(10))
# print(next(gen))
# print(next(gen))
# list(gen)
# print(next(gen))


# try:
#     raise ValueError("v")
# except ValueError as e:
#     err = e
# print(err)


# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x += 1
#     inner()
#     inner()
#     return x
# print(outer())

# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1

# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(Counter.count)

# import logging

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger("myapp")
# logger.setLevel(logging.DEBUG)

# h = logging.StreamHandler()
# h.setLevel(logging.WARNING)
# logger.addHandler(h)

# logger.info("info")
# logger.warning("warn")
# logger.error("error")

# 5 lines — `info` from root, `warn` from both, `error` from both

# from datetime import datetime

# today = datetime.today()
# start_date = datetime.strptime('2025-10-20', '%Y-%m-%d')
# print(start_date)
# diff = today - start_date
# print(f'It has been {diff.days} days')


#Crappy Data Python tasks #3

# value = "4"

# def change_type(value=value):
#     result = None
#     conversions_attempted = False
#     try:
#         result = int(value)
#     except TypeError as e:
#         print(f'Cannot convert type {type(value)} to int: {str(e)}')
#     except Exception as e:
#         print(f'Unexpected exception occured: {str(e)}')
#     finally:
#         conversions_attempted = True

#     #### wpisz kod powyżej
#     return result, conversions_attempted


# new_value, conversion = change_type(value=value)
# print(new_value)
# print(f"conversion attempted: {conversion}")

# nums = [0, 1, 2, 3]
# numbers = [16, 9, 0, 3, 58]
# nums = [4, 12, 16, 17, 20, 12]

# def find_median(numbers=numbers):
#     ### wpisz kod poniżej

#         median = None
#         table_length = len(numbers)
#         if table_length % 2 == 0:
#             median = (numbers[table_length // 2] + numbers[table_length // 2 - 1]) / 2
#         else:
#             median = numbers[table_length // 2]

#     #### wpisz kod powyżej
#         return median


# print(find_median(numbers))
# print(find_median(nums))

#Edube - Module 4

# from datetime import timedelta
# from datetime import date
# from datetime import datetime

# delta = timedelta(weeks=2, days=2, hours=2)
# print(delta) #16 days, 2:00:00

# delta2 = delta * 2
# print(delta2)

# d = date(2019, 10, 4) + delta2 
# print(d) #2019-11-05

# dt = datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)  #2019-11-05 18:53:00

#Edube - Module 4 - datetime/time labs - Exercise 1

# from datetime import datetime

# def create_datetime(time_str: str) -> datetime:
#     datetime_object1 = datetime.strftime(time_str, '%Y/%m/%d %H:%M:%S') #2020/11/04 14:53:00
#     datetime_object2 = datetime.strftime(time_str, '%y/%B/%d %H:%M:%S %p') #20/November/04 14:53:00 PM
#     datetime_object3 = datetime.strftime(time_str, '%a, %Y %b %d') #Wed, 2020 Nov 04
#     datetime_object4 = datetime.strftime(time_str, 'Weekday: %u') #Weekday: 3
#     datetime_object5 = datetime.strftime(time_str, 'Day of the year: %j') #Day of the year: 309
#     datetime_object6 = datetime.strftime(time_str, 'Week number of the year: %U')
#     print(datetime_object1)
#     print(datetime_object2)
#     print(datetime_object3)
#     print(datetime_object4)
#     print(datetime_object5)
#     print(datetime_object6)
    
# time_string = datetime(2020, 11, 4, 14, 53, 0)
# create_datetime(time_string)


# from datetime import time

# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))


# from datetime import date
# import time

# timestamp = time.time() #Number of seconds that passed since Jan 1, 1970, 00:00 UTC
# print(timestamp)
# d = date.fromtimestamp(timestamp)

# import calendar

# x = calendar.setfirstweekday(calendar.SUNDAY)
# print(x)
# calendar.prmonth(2020, 12) #we print the whole December 2020 and every week starts from Sunday (as specified above)

# print(calendar.weekday(2020, 12, 24)) #3

# import calendar
# print(calendar.weekheader(3)) #gives us headers/shortened versions of the weekdays
# #based on number of chars specified in the parameter e.g.

# #weekheader(2) Su Mo Tu We Th Fr Sa
# #weekheader(3) Sun Mon Tue Wed Thu Fri Sat

# #setfirstweekday affects this as well, so here's still Sunday as the first day of the week

# '''Checking whether a given year is a leap year'''

# print(calendar.isleap(2020)) #True/False - here True
# print(calendar.leapdays(2010, 2021))  #Returns the number of leap days in the given range of years - here 3


#Python Crappy Data - 12.03

# value = "abc465e"

# def check_value(value=value):
#     ### wpisz kod poniżej

#     tylko_litery = [char.isalpha() for char in value]
#     tylko_cyfry = [char.isnumeric() for char in value]
#     litery_i_cyfry = [char.isalnum() for char in value]


#     if not False in tylko_litery:
#         result = 'tekst zawiera tylko litery'
#     elif not False in tylko_cyfry:
#         result = 'tekst zawiera tylko cyfry'   
#     elif not False in litery_i_cyfry:
#         result = 'tekst zawiera litery i cyfry'
#     else:
#         result = 'tekst zawiera inne znaki'
        
        
#     return result
#     #### wpisz kod powyżej

# print(check_value(value))


# value = 120

# def check_value(value=value):
#     ### wpisz kod poniżej
    
#     if value > 100 or value % 2 == 0:
#         chars = [char for char in str(value)]
#         result = int(chars[0])
#     else:
#         result = None
#     #### wpisz kod powyżej
#     return result


# print(check_value(value))

# value = 120

# def check_value(value=value):
#     ### wpisz kod poniżej

#     conditions = [value > 100, value % 2 == 0]
#     print(conditions)
#     if any(conditions):
#         result = int(str(value)[0])
#     else:
#         result = None

#     #### wpisz kod powyżej
#     return result


# print(check_value(value))


# email = "ola@gmail.com"

# def verify_email(email=email):
#     ### wpisz kod poniżej
#     verified_domains = ["gmail.com", "yahoo.com", "proton.com"]
    
#     if '@' not in email or email.split('@')[1] not in verified_domains:
#         result = 'not verified'
#     else:
#         result = 'verified'

#     #### wpisz kod powyżej
#     return result


# print(verify_email(email))


#Crappy Data Python tasks - 13.03.26
# number = 123

# def reverse_number(number=number):
#     ### wpisz kod poniżej

#     result = [num for num in str(number)]
#     result.reverse()
#     result = int(('').join(result))
#     #### wpisz kod powyżej
#     return result


# print(reverse_number(number=number))

#Crappy Data Python #2

#porównanie alfabetyczne nazwisk, jeśli są takie same to imion

# person_1 = "Anna Kowalska"
# person_2 = "Roman Nowak"

# def find_name(person_1=person_1, person_2=person_2):
#     ### wpisz kod poniżej

#     result = None
#     if person_1.split()[1] == person_2.split()[1]:
#         result = person_1 if person_1 < person_2 else person_2
#     else:
#         result = person_1 if person_1.split()[1] < person_2.split()[1] else person_2

#     #### wpisz kod powyżej
#     return result


# print(find_name(person_1=person_1, person_2=person_2))


#Crappy Data Python #3

# amount = 500
# discounts = {
#     250: 0.1,
#     350: 0.2,
#     500: 0.3
# }

# def calculate_new_amount(amount=amount, discounts=discounts):
#     ### wpisz kod poniżej

#     sorted_discounts = sorted(discounts.keys(), reverse = True)
#     chosen_discount = 0
#     for discount in sorted_discounts:
#         if amount >= discount:
#             chosen_discount = discount
#             break
    
#     final_amount = round(amount - amount * discounts[chosen_discount], 2)
#     #### wpisz kod powyżej
#     return final_amount


# print(calculate_new_amount(amount))

# a = 15

# if None:
#     a = 10

# print(a)

# a = "blabla"

# try:
#     a = int(a)
# except TypeError:
#     pass
    
# print(type(a))


# import calendar  

# c = calendar.Calendar(calendar.SUNDAY)

# for weekday in c.iterweekdays():
#     print(weekday, end=" ")
    
# print(repr(c))
# print(c)

# for date in c.itermonthdates(2025, 5): #there are also days from April to complete the first week - it would be the same if the last day of may ended outside of Sunday, or other day specified in the Calendar object as the start of the week day
#     print(date)
    
# for date in c.itermonthdays(2025, 5):
#     print(date)
    
# for data in c.monthdays2calendar(2020, 12): #returns a tuple with (day of the month, day of week) e.g. (0, 6), (1, 1), (2, 2) etc.
#     print(data)
    

#Edube - Module 4 - Calendar Labs - #1

'''
During this course, we looked at the Calendar class a bit. 
Your task is to extend its functionality with a new method called count_weekday_in_year, 
which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
create the count_weekday_in_year method with the year and weekday parameters. 
The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. 
The method should return the number of days as an integer;
in your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

'''


# from calendar import Calendar


# class MyCalendar(Calendar):
    
#     def count_weekday_in_year(self, year: int, weekday: int):
#         counter = 0
#         for month in range(1, 13):
#             x = Calendar.monthdays2calendar(self, year = year, month = month)
#             day_check = [day[1] for week in x for day in week if day[0] != 0]
#             counter += sum([1 for day in day_check if day == weekday])
#         return counter
            
# x = MyCalendar()
# print(x.count_weekday_in_year(2000, 6))


# import calendar
# x = calendar.weekheader(3)
# print(x)

# print(calendar.calendar(2026))


# x = [1, 5, 6, 54, 43]
# b = list(map(lambda a: a**2, x))
# print(b)

# b = list(filter(lambda a: a > 2, x))
# print(b)


# number = (1, 2, 5, 9, 15)

# def filter_numbers(num):
#     nums = (1, 5, 17)
#     if num in nums:
#         return True
#     else:
#         return False

# filtered_numbers = filter(filter_numbers, number)
# for n in filtered_numbers:
#     print(n)
    
    
# import calendar
# cal = calendar.isleap(2019)
# print(cal)


#W10 D1 T1

# class A:
#     def hello(self):
#         return "A"

# class B(A):
#     def hello(self):
#         return super().hello() + "B"

# class C(A):
#     def hello(self):
#         return super().hello() + "C"

# class D(B, C):
#     pass

# print(D().hello())
# print(D.__mro__)



# import logging

# logging.basicConfig(level=logging.DEBUG)

# logger = logging.getLogger("app")
# logger.debug("debug")
# logger.warning("warn")


#CD Python tasks - 1

# elements = [1, " ", 8.5, "blabla", 5]


# def find_sum(elements=elements):
#     ### wpisz kod poniżej

#     result = sum([el if isinstance(el, (int, float)) and not isinstance(el, bool) else 0 for el in elements])
#     #### wpisz kod powyżej
#     return result


# print(find_sum(elements))



#CD Python tasks - 2

# exam = {
#     "anna kowalska": 18, "piotr nowak": 12, "marta zielinska": 15, "jakub lewandowski": 9,
#     "agnieszka mazur": 17, "pawel kaminski": 14, "karolina dabrowska": 16, "tomasz wojcik": 11,
#     "magdalena krupa": 19, "lukasz piotrowski": 13, "katarzyna kaczmarek": 15, "mateusz grabowski": 8,
#     "monika pawlak": 20, "wojciech michalak": 10, "joanna adamczyk": 16, "dawid dudek": 7,
#     "patrycja walczak": 18, "sebastian stepien": 12, "natalia baran": 17, "marcin lis": 14,
#     "klaudia maj": 15, "rafal szymanski": 9, "dominika ostrowska": 16, "krzysztof gorski": 13
# }

# passed = [name for name, value in exam.items() if value >= 15]

#CD Python tasks - 3

# words = ['ola', 'ma', 'kota']

# def find_longest_word(words=words):
#     ### wpisz kod poniżej
    
#     longest = None
#     length = 0
    
#     for word in words:
#         if len(word) > length:
#             length = len(word)
#             longest = word
        

#     #### wpisz kod powyżej
#     return longest

# print(find_longest_word(words))


#CD Python tasks - 4

# from datetime import datetime, date

# x = date.today()
# start = date(2025, 10, 19)
# print(x - start)

# text = 'ania'
# from collections import defaultdict

# def count_letters(text=text):
#     ### wpisz kod poniżej

#     defdict = defaultdict(int)
#     for i in text:
#         defdict[i] += 1
#     counter = dict(defdict)

#     #### wpisz kod powyżej
#     return counter


# print(count_letters(text))


#W10 D2 T1

# try:
#     raise ValueError("v")
# except Exception as e:
#     print(type(e).__name__)
#     print(isinstance(e, BaseException))
#     print(isinstance(e, Exception))

# try:
#     1 / 0
# except ArithmeticError:
#     print("arithmetic")
# except ZeroDivisionError:
#     print("zero")

# try:
#     raise TypeError("t")
# except (ValueError, TypeError) as e:
#     print("caught:", e)
#     raise

# print("done")
#caught: t
#TypeError: t

# try:
#     try:
#         raise ValueError("inner")
#     except TypeError:
#         print("inner handler")
# except ValueError:
#     print("outer handler")
# finally:
#     print("finally")

#outer handler - finally

#W10 D2 T2
# class A:
#     x = []

# a = A()
# b = A()
# a.x.append(1)
# print(b.x)
# print(A.x)


# class A:
#     def __init__(self):
#         self.__secret = 42

# a = A()
# print(a.__secret) #AttributeError


# class A:
#     def __init__(self):
#         self.__secret = 42

# a = A()
# print(a._A__secret) #42


# class Animal:
#     def speak(self):
#         return "..."

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# class Cat(Animal):
#     def speak(self):
#         return "meow"

# animals = [Dog(), Cat(), Animal()]
# for a in animals:
#     print(a.speak())

#woof, meow, ...


# class Counter:
#     def __init__(self):
#         self._count = 0

#     @property
#     def count(self):
#         return self._count

#     @count.setter
#     def count(self, value):
#         if value < 0:
#             raise ValueError("negative")
#         self._count = value

# c = Counter()
# c.count = 5
# print(c.count)
# c.count = -1



# class A:
#     def __str__(self):
#         return "str_A"
#     def __repr__(self):
#         return "repr_A"

# a = A()
# print(a)
# print(repr(a))
# print([a])
# print(f"{a}")


#W2 D2 T3

# x = "global"

# def outer():
#     x = "outer"
#     def inner():
#         x = "inner"
#         return x
#     return inner()

# print(outer()) #inner - no UnboundLocalError, as we do not modify the outer x
# print(x) #global



# x = 0

# def f():
#     global x
#     x += 10

# f()
# f()
# print(x) #20


# def make_multiplier(n):
#     return lambda x: x * n

# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5)) #10
# print(triple(5)) #15
# print(double(triple(2))) #12


# fns = [lambda x: x + n for n in range(4)]
# print([f(0) for f in fns]) #[3, 3, 3, 3]

# fns = [lambda x, n=n: x + n for n in range(4)]
# print([f(0) for f in fns]) #[0, 1, 2, 3]

#W10 D2 T4

# def gen():
#     for i in range(3):
#         yield i * 2

# g = gen()
# print(next(g)) #0
# print(next(g)) #2
# print(list(g)) #[4, 6]


# def gen():
#     yield 1
#     yield 2

# g = gen()
# print(list(g)) #[1, 2]
# print(list(g)) #[]


# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# print(sum(countdown(5))) #sum([5, 4, 3, 2, 1]) = 15

# def gen():
#     yield from [1, 2, 3]
#     yield from range(3)

# print(list(gen())) #[1, 2, 3, 0, 1, 2]



# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration
#         self.current += 1
#         return self.current

# print(list(Counter(3))) #[1, 2, 3]


#W10 D2 T5
# nums = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)

# #[2, 4, 6]


# nums = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, nums))
# print(result) #[1, 4, 9, 16]



# from functools import reduce

# result = reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 10) #11 -> 13 -> 16 -> 20
# print(result) #20



# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("before")
#         result = func(*args, **kwargs)
#         print("after")
#         return result
#     return wrapper

# @decorator
# def greet(name):
#     print(f"hello {name}")

# greet("Alice")

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("before")
#         result = func(*args, **kwargs)
#         print("after")
#         return result
#     return wrapper

# @decorator
# @decorator
# def greet(name):
#     print(f"hello {name}")

# greet("Bob")

#W10 D2 T6 - SLICING exercises

# s = "Python"
# print(s[1:4]) #yth
# print(s[-3:]) #hon
# print(s[::2]) #Pto
# print(s[::-1]) #nohtyP


# s = "hello world"
# print(s.upper()) #HELLO WORLD
# print(s.capitalize()) #Hello world
# print(s.title()) #Hello World

# s = "  hello  "
# print(len(s)) #9
# print(len(s.strip())) #5



# s = "a,b,,c,d"
# parts = s.split(",") #
# print(len(parts)) #5
# print(parts) #['a', 'b', '', 'c', 'd']



# print("{}{}{}".format(1, 2, 3)) #123
# print("{2}{0}{1}".format("a", "b", "c")) #cab
# print(f"{'hello':>10}") #i don't know

#W10 D2 T7
# class A:
#     pass

# a = A()
# a.x = 10
# print(a.__dict__)


# xs = [1, 2, 3]
# ys = xs[:]
# ys.append(4)
# print(xs) #[1, 2, 3]
# print(ys) #[1, 2, 3, 4] - new object created with [:]

# print(bool(0), bool(""), bool([]), bool(None)) #False False False FAlse
# print(bool(1), bool("0"), bool([0])) #True True True


# d = {"a": 1, "b": 2}
# for k, v in d.items():
#     d[k] = v * 2

# print(d)


# import copy

# original = [[1, 2], [3, 4]]
# shallow = copy.copy(original)
# shallow[0].append(99)

# print(original) [[1, 2, 99], [3,4]]
# print(shallow) [[1, 2, 99], [3,4]]

# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# foo = tuple(filter(lambda x: x>1, my_tuple))
# print(foo)

# foo = list(filter(lambda x: x-0 and x-1, my_tuple)) #[2, 3, 4, 5, 6]
# print(foo)

# foo = list(filter(lambda x: x==0 and x==1, my_tuple)) #[]
# print(foo)

# b = bytearray(3)
# print(b)


# def fun(n):
#     s = '+'
#     for i in range(n):
#         print(f'Before: {s}')
#         s += s
#         print(f'After {s}')
#         yield s
        
        
# for x in fun(2):
#     print(x, end = '')
    
    
#lambda review

#lambda args: expression (unltimited args, single expression)

# f = lambda x: x * 2
# f = lambda x: x * 2; x + 1 #SYNTAX ERROR - multiple expressions

#lambda args
# f0 = lambda x, y: x + y #(2 args, 1 expression - alright)
# f1 = lambda x, y, z, c: sum([x, y, z, c]) #4 args, 1 expression, alright

# print(f1(5, 52, 12, 5.3))

# with open('file.txt', 'a') as w:
#     w.write('xdas32')
    

# for x in open('file.txt', 'rt'):
#     print(x)

# import math
# print(dir(math))

# import random
# a = random.randint(0, 100)
# a = random.randrange(10, 100, 3)
# c = random.choice((0, 100, 3))
# print(c)

#0, 1, 4, 9, 16

# numbers = [i*i for i in range(5)]
# foo = list(filter(lambda x: x % 2, numbers))
# print(foo)

# from datetime import datetime
# dt1 = datetime(2019, 11, 27, 11, 27, 22)
# dt2 = datetime(2019, 11, 27, 0, 0, 0)

# print(dt1 - dt2)

# print(float('1.3'))


# import os
# print(os.uname)


#Test - 70%...


#If there are more than one except branches after the try clause, we can say that:
#one or more except blocks will be executed,
#none of the except blocks will be executed
#not more than one except block will be executed


#the following line of code:
# for line in open('text.txt', 'rt'):
#     pass
# #is invalid because open returns nothing
# #is valid because open retursn an interable object
# #is invalid because open returns a non-tireable object


# #Aassuming invo that the open() invocation was successful, te following snippet:
# for x in open('file', 'rt'):
#     print(x)
    
#will read the file line by line
#cause an exception
#read the whole character by character


#which lines of code would you insert so that it's possible for the program to output the following result:

#6 82 0

#A
#import random
#a = random.randrange(10, 100, 3) #won't work because of that
#b = random.randint(0, 100)
#c = random.choice((0, 100, 3))

#b
#import random
#a = random.randint(0, 100)
#b = random.choice(0, 100, 3) - won't work because of that
#c = random.randrange((10, 100, 3))

#c - seems ok
#import random
#a = random.randint(0, 100)
#b = random.randrange(10, 100, 3)
#c = random.choice((0, 100, 3))

#d - this is the answer I chose, what's wrong here?
#import random
#a = random.choice((0, 100, 3))
#b = random.randrange(10, 100, 3)
#c = random.randint(0, 100)\
    
# x = '\\\'
# print(len(x)) #SyntaxError, unterminated string literal


# print(chr(ord('p') + 2)) #r


#The sys.stderr stream is normally associated weith
#the keyboard
#a null device
#the screen


# try:
#     raise Exception
# except:
#     print('c')
# except BaseException:
#     print('a')
# except Exception:
#     print('b')
#This causes a Syntax error, as the default except must be last. This is weird and unexpected, I don't remember us handling that.


# class A:    
#     A = 1
#     def __init__(self):
#         self.a = 0
        
# print(hasattr(A, 'a')) #False,


# numbers = [0, 2, 7, 9, 10]
# foo = map(lambda num : num ** 2, numbers) #numbers printed out properly with map as we put them in a list
# print(list(foo))

# #what will be the output of the following code, located in the p.py file?
# print(__name__)

#__p.py
#main
#__main__


#CD Python t1

# students = ["Anna Kowalska", "Roman Nowak", "Aleksandra Buch"]

# def create_students_id(students=students):
#     ### wpisz kod poniżej

#     id = 0
#     students_sorted = sorted([f'{student.split()[1]} {student.split()[0]}' for student in students])
#     student_ids = {}
#     for student in students_sorted:
#         id += 1
#         student_ids[id] = student
    

#     #### wpisz kod powyżej
#     return student_ids


# print(create_students_id(students))

#CD Python t2


# words = ["kot", "pies", "rower", "noc", "okno"]

# def create_word_length(words=words):
#     ### wpisz kod poniżej

#     unique_words = set(word for word in words)
#     word_lengths = {word : len(word) for word in unique_words}
#     final_dict = {}

#     for length in word_lengths.values():
#         counter = sum([1 for item in word_lengths.items() if item[1] == length])
#         final_dict[length] = counter

    
#     return final_dict


# print(create_word_length(words))


#CD Python t3 

'''
Zadanie
Istnieją różne algorytmy sortowania, jeden z nich to tzw. sortowanie przez wybieranie (ang. selection sort).

Jego poszczególne kroki to:

Znajdź najmniejszą liczbę w liście.
Dodaj ją do nowej listy.
Usuń ją z oryginalnej listy.
Powtarzaj, aż lista będzie pusta
Spróbuj zaimplementować ten algorytm i posortować listę numbers, zapisując wynik w liście sorted_numbers.
'''

# numbers = [57, 12, 98, 34, 76, 5, 63, 41, 89, 23, 67, 14, 92, 38, 71, 6, 54, 83, 29, 47, 95, 18, 72, 31, 64, 9, 87, 26, 53, 44, 79, 3, 68, 21, 90, 36, 58, 11, 74, 49, 82, 7, 61, 28, 93]

# sorted_numbers = []
# while len(numbers) > 0:
#     lowest_num = min(numbers)
#     sorted_numbers.append(lowest_num)
#     numbers.remove(lowest_num)
    
# print(numbers)
# print(sorted_numbers)

#W10 D3 T1
# try:
#     raise ValueError("v")
# except Exception:
#     print("Exception")
# except ValueError:
#     print("ValueError")


#W10 D3 T2
# with open('test.txt', 'w') as f:
#     f.write('hello\nworld\n')

# with open('test.txt', 'r') as f:
#     lines = f.readlines()

# print(len(lines)) #2
# print(repr(lines[0])) #'hello\n'


# with open('test.txt', 'w') as f:
#     f.writelines(['a', 'b', 'c'])

# with open('test.txt', 'r') as f:
#     print(f.read()) #abc

# with open('test.txt', 'w') as f:
#     f.write('hello world')

# with open('test.txt', 'r') as f:
#     print(f.read())
#     print(f.read())

#W10 D3 T3
# import os
# print(type(os.environ)) #
# print(os.environ.get('NONEXISTENT_KEY_XYZ', 'default')) #default


# import os
# print(os.path.basename('/home/user/project/main.py')) #main.py
# print(os.path.dirname('/home/user/project/main.py')) #/home/user/project/
# print(os.path.splitext('data.csv')) #('data', '.csv')

# import os
# print(os.name) #nt for Windows, posix on linux/mac


# import os
# path = os.path.join('algo_backtest', 'data', 'prices.csv')
# print(path) #algo_backtest/data/prices.csv

# from datetime import datetime
# dt = datetime(2026, 3, 19, 14, 30, 0)
# print(dt.strftime("%A, %d %B %Y")) #Thursday, 19, March, 2026
# print(dt.strftime("%H:%M")) #14:30


#W10 D3 T4
# from datetime import datetime
# s = "19/03/2026 14:30"
# dt = datetime.strptime(s, "%d/%m/%Y %H:%M")
# print(dt.year, dt.month, dt.day) #2026 3 19


# from datetime import timedelta
# delta = timedelta(days=2, hours=3, seconds=30)
# print(delta.days)
# print(delta.seconds)
# print(delta.total_seconds())

# import time
# t = time.localtime()
# print(type(t).__name__)
# print(t.tm_wday)   # assuming today is Wednesday

# import time
# print(type(time.time())) #float


# import calendar
# print(calendar.weekday(2026, 3, 19)) #3
# print(calendar.THURSDAY) #3
# print(calendar.isleap(2026)) #False


# import calendar
# first_day, num_days = calendar.monthrange(2024, 2)
# print(first_day, num_days)
# 

#W10 D3 T5
# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1

# a1 = A()
# a2 = A()
# a3 = A()
# print(A.count)
# print(a1.count)


# print(bool(""))
# print(bool("0"))
# print(bool([]))
# print(bool([0]))


# x = (1, 2, 3)
# y = x
# y += (4,)
# print(x)
# print(y)


# a, *b, c = [1, 2, 3, 4, 5]
# print(type(b)) #list
# print(b) [2, 3, 4]
# print(c) #5

# xs = [1, 2, 3]
# ys = xs[:]
# ys[0] = 99
# print(xs[0])
# print(ys[0])



#CD Python - task 1

'''Na podstawie listy studentów students oraz 3 list z wynikami kartkówek, 
stwórz słownik results, w którym:

kluczem będzie imię i nazwisko studenta
wartością będzie lista wyników z trzech kartkówek'''


# students = ["Anna Kowalska", "Roman Nowak", "Aleksandra Buch", "Marek Zieliński"]

# quiz1 = [8, 5, 9, 6]
# quiz2 = [7, 6, 8, 7]
# quiz3 = [9, 7, 10, 8]

# def organize_exams(students=students, quiz1=quiz1, quiz2=quiz2, quiz3=quiz3):
#     ### wpisz kod poniżej

#         results = {student : [] for student in students}
#         index = 0
#         for result in results:
#             results[result].append(quiz1[index])
#             results[result].append(quiz2[index])
#             results[result].append(quiz3[index])
#             index += 1
#         print(results)

#     #### wpisz kod powyżej
#         return results


# print(organize_exams(students, quiz1, quiz2, quiz3))




#CD Python - task 2
'''
Stwórz listę wszystkich lat przestępnych pomiędzy 2000 a 3000 rokiem (włącznie)
i przypisz ją do zmiennej years.

Rok jest przestępny, jeżeli dzieli się przez 4, 
z wyłączeniem lat podzielnych przez 100, ale nie przez 400 .
'''
#I know the purpose of this excercise is to calculate it manually, but I'd also like to practice calendar for PCAP
# years = []
# import calendar
# for year in range(2000, 3001, 4):
#     if calendar.isleap(year):
#         years.append(year)

# print(years)




#CD Python - task 3


'''
Policz ile razy sekwencja znaków short_string pojawia się w stringu long_string. 
Wynik przypisz do zmiennej result. Jeżeli się nie pojawia, przypisz 0.

Sekwencje mogą się na siebie nakładać.
'''

# short_string = "aa"
# long_string = "aaaa"

# def find_inside(short_string=short_string, long_string=long_string):
        
#         len_short = len(short_string)
#         len_long = len(long_string)
#         result = 0
#         for i in range(0, len_long - len_short + 1):
#             if long_string[i:i+len_short] == short_string:
#                 result += 1

        


#         return result

# print(find_inside(short_string, long_string))

#Really struggled with this task btw, as this was quite unintuitive + needed to handle edge cases


#W10 D4 - PCAP review tasks and gaps focus

# t = (1, 2)
# t += (3,)
# print(id(t) == id((1, 2, 3)))


# def f(t):
#     t += (99,)

# x = (1, 2)
# f(x)
# print(x)


# try:
#     raise TypeError("bad type")
# except TypeError as e:
#     print(e)
    
    
# e = OSError(2, "No such file or directory")
# print(str(e))

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(type(e).__name__)
#     print(str(e))


# import os
# print(os.path.split('/home/user/project/main.py'))

# import os
# print(os.path.exists('/this/path/does/not/exist/xyz123'))

# with open('test.txt', 'w') as f:
#     f.writelines(['line1', 'line2', 'line3']) #IT DOES NOT ADD LINE SEPARATORS BY DEFAULT!

# with open('test.txt', 'r') as f:
#     print(len(f.readlines())) #SO THAT WOULD BE 1!


# import os
# p = os.path.join('data', 'raw', 'prices.csv')
# print(os.path.basename(p))
# print(os.path.dirname(p))

#W4 D4 T5

# a, *b, c = [1]
# print(a, b, c) #ValueError - expected at least 2 values, got 1

# import calendar
# print(calendar.WEDNESDAY) #Monday is 0
# print(calendar.weekday(2026, 1, 1)) #This is Thursday

# 2
# 3


# def f():
#     pass

# print(bool(f())) #False


#CD Python - Task 1
'''
Znajdź w zmiennej text numer PESEL i przypisz go jako string do zmiennej pesel. 
Pesel składa się dokładnie z 11 cyfr, w tekście znajduje się tylko jeden taki numer.
'''

# text = "System raportowy generuje dzienne zestawienia klientów, identyfikatory zamówień takie jak ORD88231, ORD88232, numery telefonów 501223344, 602334455, różne kody referencyjne AX9921, BX7732, CX8811 oraz losowe liczby jak 4412, 998877, 234234, 887766, identyfikatory użytkowników USER44821, USER99812, USER77123, dane archiwalne z systemu billingowego zawierające rekordy operacyjne, dodatkowe liczby jak 77221133, 44556677, 99331122, oraz różne ciągi znaków jak AB1234XY, GH8821JK, TT7732AA, 123TT773264 a także informacje o kliencie Jan Malinowski z Warszawy którego identyfikator w bazie to CL99123 oraz numer PESEL 91052734567 zapisany w systemie centralnym obok innych danych jak numer sprawy SP99211, SP99212, SP99213, identyfikatory sesji SESSION8811, SESSION9912, SESSION1112 oraz różne liczby jak 121212, 343434, 565656, 787878, 909090 i inne dane systemowe używane do raportowania."
# entities = text.split()

# for entity in entities:
#     if len(entity) == 11 and entity.isnumeric():
#         pesel = entity


#CD Python - Task 2

'''
Napisz kod, który porządkuje string dirty_string i zapisuje wynik w zmiennej clean_string.

Etapy przekształcenia:

posortuj litery alfabetycznie
każdą literę zapisz raz, a następnie liczbę razy, ile pojawiła się w stringu.
Przykład
daccdacb → a2b1c3d2


'''

# dirty_string = "daccdacb"

# def clean_dirty_string(dirty_string=dirty_string):
#     ### wpisz kod poniżej

#     letters = sorted([letter for letter in dirty_string])
#     letters_nums = {}
#     for letter in letters:
#         if letter not in letters_nums:
#             letters_nums[letter] = 1
#         else:
#             letters_nums[letter] += 1

#     clean_string = str()
#     for letter, value in letters_nums.items():
#         clean_string += f'{letter}{value}'
#     #### wpisz kod powyżej
#     return clean_string


# print(clean_dirty_string(dirty_string))

#CD Python - Task 3

'''
W liście numbers znajdź największą różnicę między dwoma kolejnymi elementami
i przypisz ją do zmiennej result.
'''

# numbers = [4, 9, 2, 15, 6, 20]

# def max_difference(numbers=numbers):
#     ### wpisz kod poniżej

#     result = 0
#     for i in range(len(numbers) - 1):
#         difference = abs(numbers[i] - numbers[i+1])
#         if difference > result:
#             result = difference
#     #### wpisz kod powyżej
#     return result

# print(max_difference(numbers))


#CD Python - Task 4

'''
Pomijaj sumowanie liczb podzielnych przez podzielnych przez 3.

Przerwij wykonywanie pętli, gdy suma przekroczy wartość 1000.
'''

# suma = 0
# for i in range(1000):
#     if i % 3 == 0:
#         continue
#     elif suma < 1000:
#         suma += i
#     else:
#         break


#CD Python - Task 5

'''
Napisz kod, który odwraca wielkość liter w stringu letters. 
Małe litery zamień na wielkie, a wielkie na małe. 
Znaki, które nie są literami alfabetu, pozostaw bez zmian. 
Wynik zapisz w zmiennej result.
'''

# letters = "aBDc"

# def swap_cases(letters=letters):
#     ### wpisz kod poniżej

#     result = ''
#     for letter in letters:
#         if letter.isalpha():
#             if letter.isupper():
#                 letter = letter.lower()
#             elif letter.islower():
#                 letter = letter.upper()
#         result += letter

#     #### wpisz kod powyżej
#     return result


# print(swap_cases(letters))


#W10 D5 T1
'''
Write a function `flatten(nested: list) -> list` that takes a list which may contain other lists (one level deep only) and returns a flat list of all elements.
'''


# def flatten(nested: list) -> list:
    
#     flattened_list = []
#     for element in nested:
#         if isinstance(element, (int, float)):
#             flattened_list.append(element)
#         else:
#             for el in element:
#                 flattened_list.append(el)
            
#     print(flattened_list)
#     return flattened_list
    

# flatten([1, [2, 3], 4, [5, 6]])  # → [1, 2, 3, 4, 5, 6]
# flatten([1, 2, 3])               # → [1, 2, 3]
# flatten([[1], [2], [3]])  


#W10 D5 T2

'''
Write a class `BoundedList` that behaves like a list but never exceeds a fixed max size. 
When a new item is added and the list is full, the oldest item is removed (FIFO).
'''

# class BoundedList:
    
#     def __init__(self, max_size: int):
#         self.max_size = max_size
#         self._items: list[float] = []
    
#     @property
#     def values(self) -> list:
#         return list(self._items) #returning a copy, so there's no way to mutate the list from the outside
    
#     @property
#     def average(self) -> float:
#         if not self._items:
#             return 0.0
#         return sum(self._items) / len(self._items)
    
#     def __len__(self) -> int:
#         return len(self._items)
    
#     def add(self, item: float) -> None:
#         if self.__len__() == self.max_size:
#             del self._items[0]
#         self._items.append(item)
            

# bl = BoundedList(max_size=3)
# bl.add(1)
# bl.add(2)
# bl.add(3)
# bl.add(4)      # drops 1
# print(bl.values)   # [2, 3, 4]
# print(len(bl))     # 3
# print(bl.average)

#W10 D5 T4
'''
Write the corrected version of each. 
Identify what is wrong first (one sentence), then fix it.
'''


# def running_average(numbers):
#     if not numbers:
#         return 0.0
#     total = sum(numbers)
#     return total / len(numbers)

# print(running_average([5, 3, 2]))



# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

# s1 = Stack()
# s2 = Stack()
# s1.push(1)
# print(s2.items)  # expected: []


# import os

# def find_csvs(folder: str) -> list:
#     try:
#         cvs = [f for f in os.listdir(folder) if f.endswith('.csv')]
#         return cvs
#     except FileNotFoundError as e:
#         print(f'FileNotFoundError: {str(e)}')
#     except Exception as e:
#         print(f'Unhandled exception: {str(e)}')

# files = find_csvs('nonexistent_folder')
# print(files)


#W10 D5 T5
#Imported real OHLCV M1 data for FDAX with bid/ask volumes + vwap into data/ folder (also put it in gitignore, so it won't be visible in the repo)
#Tested loading & verifying data in main - everything went well.

#W10 D5 T6
# I've ran the strategy on 216k rows with real FDAX data, with a very simple open/close conditions.
# Test worked properly, I think.

# The next steps would be:

# 1. to implement more sophisticated strategy conditions, maybe add a datetime as one of the conditions of generating a signal.
# 2. It would also be great to figure out a way to then simulate testing more than one strategy.
# 3. After we're done with running two strategies (a mini stress-test of the real purpose of this and combining the logic of more than one strategy in the code to still look neat), I have an idea of how we can simulate portfolio performance. We could maybe create a new class for that, or maybe not - that depends.

# We could take the datetime and R/profit performance of a given trade, and save it in a df, or wherever.
# Then we would do that for every tested strategy, and after every strategy has been tested, we would then take these performance/profit rows with datetimes and sort them by their datetime. We could then simulate portfolio's performance, extract more things like Sharpe/Profit Factor, maybe run Montecarlo simulations etc.

# And it all would work without async and complex logic - I think it's a good idea.

# import errno
# print(errno.ENOENT)

#W11 D1 T1

# class A:
#     def f(self): return "A"

# class B(A):
#     def f(self): return super().f() + "B"

# class C(A):
#     def f(self): return "C" + super().f()

# class D(B, C):
#     pass

# print(D().f())


# MRO order: D -> B -> C -> A 
# Output: CAB

#W11 D1 T2

# class A:
#     def __init__(self):
#         self.items = []
#         print("A")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")

# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("C")

# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print("D")

# d = D()
# print(len(d.items)) #0

#MRO ORDER: D -> B -> C -> A 
#Output: A -> C -> B - > D
#len 0, no items added


#W11 D1 T3

# class A:
#     def greet(self): return "A"

# class B(A):
#     def greet(self): return "B"   # no super()

# class C(B):
#     def greet(self): return super().greet() + "C"

# print(C().greet())

#'BC' 
#A is not reached, as B doesn't call super().greet() and it overwrites A's greet

#W11 D1 T4

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self): pass

#     @abstractmethod
#     def move(self): pass

# class Dog(Animal):
#     def sound(self): return "woof"

# d = Dog()
# print(d.sound())

#Error - Dog will not work - it would necessarily have to also add the move method as in the abstractmethod!

#W11 D1 T5

# def gen():
#     return
#     yield 1
#     yield 2

# g = gen()
# print(type(g).__name__)
# print(list(g))

#generator
#[1, 2]


#W11 D1 T6
# def parse(value):
#     try:
#         return int(value)
#     except ValueError:
#         print("inner caught")
#         raise

# try:
#     result = parse("abc")
# except ValueError:
#     print("outer caught")


#CD Python - task 77

'''
Stwórz funkcję split_string, która dzieli string po myślnikach - i zwraca listę fragmentów.

liczby zapisz jako int
puste "" fragmenty pomiń
'''


# from typing import List
# text = "-14--abc3-08-"
# def split_string(text_string: str) -> List:
#     parts = text_string.split('-')
#     parts_filtered = [part for part in parts if part.isalnum()]
#     parts = [int(part) if part.isnumeric() else part for part in parts_filtered]
#     return parts

# # napisz kod tutaj
# print(split_string(text))

#CD Python - task 78

'''
Stwórz funkcję print_word_stats, która przyjmuje string text.

Funkcja powinna:

Zamienić tekst na małe litery
Podzielić go na słowa (po spacji)
Usunąć znaki specjalne z początku i końca słów (np. .,!?)
Policz ile razy każde słowo występuje
Wypisać wynik w formacie: słowo: liczba. Każde słowo w nowej linii.

Funkcja nie powinna nic zwracać, tylko wyprintować wyniki.

'''



# text = "Python, python! Data science, python."

# def print_word_stats(text):
#     lcase = text.lower()
#     parts = lcase.split()
    
#     cleaned = []
#     for part in parts:
#         for char in part:
#             if not char.isalnum():
#                 print(f'Not alnum detected: {char}')
#                 part = part.replace(char, '')
#         cleaned.append(part)
#     print(cleaned)
    
#     summary_dict = {}
#     for word in cleaned:
#         if word not in summary_dict:
#             summary_dict[word] = 1
#         else:
#             summary_dict[word] += 1
#     print(summary_dict)
    
#     for item in summary_dict.items():
#         print(f'{item[0]}: {item[1]}') #pozadany w zadaniu format 

# print_word_stats(text)



#CD Python - task 79

'''
Stwórz funkcję random_numbers, która przyjmuje argument n i zwraca listę n losowych liczb całkowitych z zakresu od 0 do 100.
'''

# import random

# def random_numbers(n: int) -> list:
#     return [random.randint(0, 100) for i in range(n)]


#CD Python - task 80
'''
Napisz funkcję longest_prefix, która przyjmuje dwa argumenty a i b, a następnie zwraca najdłuższy wspólny prefiks tych dwóch wartości.
'''

# def longest_prefix(a: str, b: str) -> str:
#     '''
#     Accepts two string args and returns their shared prefix
#     '''
    
#     shared_prefix = None
#     for i in range(len(a)):
#         if not a[0:i+1] == b[0:i+1]:
#             break
#         shared_prefix = a[0:i+1]
    
#     print(shared_prefix)
#     return shared_prefix


#CD Python - task 81
'''
Napisz funkcje common_words, która zwraca listę słów, które występują w obu tekstach. 
Ignoruj wielkość liter (np. A i a traktuj jako tę samą literę).
'''

# from typing import List

# def common_words(text1: str, text2: str) -> List[str]:
#     '''
#     Accepts two strings, finds a list of all words that are found in both of them
#     Args:
#     text1: str
#     text2: str
    
#     Returns:
#     a list of strings
#     '''
    
#     s1 = set(text1.lower().split())
#     s2 = set(text2.lower().split())
    
#     print(s1, s2)
    
#     return list(s1 & s2)
    
# text1 = "python data science machine learning"
# text2 = "data analysis python statistics"

# print(common_words(text1, text2))


#CD Python - task 82

'''
Na podstawie słownika students stwórz słownik students_sorted, 
w którym studenci są posortowani rosnąco (zaczynając od najmniejszej liczby) na podstawie wyników kartkówek.
'''


# students = {
#     "Anna": 7,
#     "Bartek": 5,
#     "Staś": 8,
#     "Michał": 3,
#     "Ola": 6,
#     "Tomek": 2,
#     "Piotr": 4
# }

# students_sorted = sorted(students.items(), key = lambda x: x[1])
# students_sorted = {student: grade for student, grade in students_sorted}
# print(students_sorted)


#W11 D2 #T1

# def gen():
#     return
#     yield 1
#     yield 2

# g = gen()
# print(type(g).__name__) #GENERATOR
# print(list(g)) #[]


# def gen2():
#     yield
#     return
#     yield 1

# print(list(gen2())) #[None]


#W11 D2 #T2
# print(IOError is OSError) #True
# print(issubclass(FileNotFoundError, OSError)) #True
# print(issubclass(FileNotFoundError, IOError)) #True


#W11 D2 #T3
# with open("test.txt", "w") as f:
#     f.write("line1\n")
#     f.write("line2\n")

# with open("test.txt", "r") as f:
#     lines = f.readlines()

# print(len(lines)) #2
# print(repr(lines[0])) #line1\n
# print(repr(lines[-1])) #line2\n


#W11 D2 T4

# with open("test.txt", "w") as f:
#     f.write("hello")

# with open("test.txt", "r") as f:
#     print(repr(f.read(3))) #'hel'
#     print(repr(f.read(3))) #'lo '
#     print(repr(f.read(3))) #'   '


#W11 D2 T5

# with open("test.txt", "w") as f:
#     f.write("alpha\nbeta\ngamma\n")

# with open("test.txt", "r") as f:
#     line = f.readline()
#     print(repr(line)) #'alpha\n'
#     line = f.readline() 
#     print(repr(line)) #'beta\n'
    


#W11 D2 T6

# import os

# path = "/home/user/docs/report.pdf"
# print(os.path.basename(path)) #report.pdf
# print(os.path.dirname(path)) #home/user/docs
# print(os.path.split(path)) # ('home/user/docs', 'report.pdf')
# print(os.path.splitext(path)) #('home/user/docs/report', 'pdf')

#W11 D2 T7
# from datetime import datetime, timedelta

# dt = datetime(2026, 3, 24, 10, 30, 0)
# delta = timedelta(days=3, hours=2)
# result = dt + delta

# print(result.day) #27
# print(result.hour) #12

#W11 D2 T9

# from datetime import timedelta

# td = timedelta(days=1, seconds=3600)
# print(td.days) #1
# print(td.seconds) #3600
# print(td.total_seconds()) #IDK - this is weird and stupid, humans don't remember such things and this will not be checked on PCAP exam


#W11 D2 T11
# def evens(limit):
#     n = 0
#     while n <= limit:
#         yield n
#         n += 2

# gen = evens(6)
# print(next(gen)) #0
# print(next(gen)) #2
# print(list(gen)) #[4, 6]

#W11 D2 T12
# def gen():
#     yield from [1, 2, 3]
#     yield from range(3)

# result = list(gen())
# print(result)  #[1, 2, 3, 0, 1, 2]
# print(len(result)) #6

#W11 D2 T13

# def squares():
#     for i in range(5):
#         yield i ** 2

# g = squares()
# list(g) 
# print(next(g)) #StopIteration is raised

#W11 D2 T14
# import errno

# try:
#     f = open("no_such_file.txt", "r")
# except OSError as e:
#     print(e.errno) #2
#     print(type(e).__name__) #FileNotFoundError


# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner

# f = outer()
# print(f())


#CD Python - task 83

'''
Znajdź sekretną wiadomość ukrytą w pliku w aktualnym folderze roboczym i przypisz ją do zmiennej message_for_you.
'''


# import os
# current_path = os.getcwd()
# all_files = os.listdir(current_path)
# print(all_files) #teraz obczajamy pliki

# #po sprawdzeniu plików znalazłem secret_message.txt
# with open('secret_message.txt', 'r') as r:
#     message_for_you = r.read()

# print(message_for_you)


#CD Python - task 84

'''Napisz funkcję get_random_students, która losuje z listy students n unikalnych osób (bez powtórzeń) 
i zwraca je alfabetycznie w postaci listy. Domyślnie funkcja powinna losować 2 osoby.'''

# from typing import List
# import random

# def get_random_students(students: List[str], n: int = 2) -> List[str]:
    
#     return random.sample(students, n)

# students = ["Ola", "Emil", "Radosław"]

# print(get_random_students(students, n = 1))


#CD Python - task 85

'''
Napisz funkcję longest_word, która przyjmuje string text i zwraca słowo zawierające największą liczbę unikalnych liter.

Ignoruj liczby oraz znaki specjalne (analizuj tylko litery).
Ignoruj wielkość liter (np. A i a traktuj jako tę samą literę).
Jeśli kilka słów ma taką samą maksymalną liczbę unikalnych liter, zwróć je w postaci listy.

Podpowiedź
Aby usunąć znaki specjalne i liczby, możesz użyć funkcji findall() z biblioteki re: re.findall(r"[a-zA-Z]+", text)
'''

# import re


# def longest_word(text: str) -> str:
#     list_of_words = re.findall('[a-zA-Z]+', text.lower())
#     words_dict = {}
#     for word in list_of_words:
#         unique_letters = set([letter for part in word for letter in part])
#         if word not in words_dict:
#             words_dict[word] = len(unique_letters)
    
#     sorted_words = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
#     max_length = max([x[1] for x in sorted_words])
#     longest_word = [word for word, length in sorted_words if length == max_length]
#     if len(longest_word) == 1:
#         longest_word = longest_word[0]
    
#     return longest_word
        
        
# text = "Ania ma kota kota!"
# print(longest_word(text))



#CD Python - task 86

'''
Zadanie
Napisz funkcję stats, która przyjmuje jako argument listę liczb
i zwraca średnią (zaokrągloną do 2 miejsc po przecinku) oraz liczbę elementów z listy.
'''
# from typing import List, Tuple

# def stats(list_of_nums: List) -> Tuple[float, int]:
#     '''
#     Func calculates the average number found in the list.
    
#     Args:
#     - A list (of numbers - ints/floats)
    
#     Returns: 
#     A tuple (x, y)
#     - x - the average rounded to 2 decimals
#     - y - the n of numbers in the list
#     '''
    
    
#     avg = round(sum(list_of_nums) / len(list_of_nums), 2)
#     return avg, len(list_of_nums)

# numbers = [5, 10, 8.5, 14]

# avg, count = stats(numbers)
# print(avg)
# print(count)

#W11 D3 T1 - predict the output

# class Item:
#     def __repr__(self): return "Item(42)"
#     def __str__(self): return "an item"

# x = Item()
# print(x) #an item
# print(repr(x)) #Item(42)
# print([x]) #[Item(42)]
# print(f"{x}") #{an item}

# lines = ["hello\n", "world\n"]
# print(lines[0]) #hello
# print(repr(lines[0]))  #'hello\n'

#W11 D3 T2

# import os

# path = "/home/user/projects/report.pdf"
# print(os.path.basename(path)) #report.pdf
# print(os.path.dirname(path)) #/home/user/projects/
# print(os.path.split(path)) #(/home/user/projects, report.pdf)
# print(os.path.splitext(path)) #('/home/user/projects/report', '.pdf') - this is weird but this is how it works


# '''On Linux, the slashes are turned to the opposite side (\), but the rest is the same.
# That's the reason why we use os path, as it works correctly for both Linux/Windows,
# handling this difference and dealing with different slashes every time.
# This wway we don't have to remember or guess it.'''


#W11 D3 T3

# import errno

# try:
#     open("missing.txt", "r")
# except OSError as e:
#     print(e.errno)
#     print(errno.ENOENT)
#     print(e.errno == errno.ENOENT)
#     print(type(e).__name__)

# print(IOError == OSError) #True
    
#2
#2
#True
#FileNotFoundError

#W11 D3 T4

# import random

# x = random.randint(1, 5) #can include both ends
# y = random.randrange(0, 10, 3) #can include both ends (if the step allows it) - here we'd have 0, 3, 6, 9
# z = random.choice((10, 20, 30)) #WE CAN ONLY RETURN a value from teh sequence - 10, 20 OR 30
# print(x, y)

#W11 D3 T5

# a = '\\'
# b = "\'"
# c = '\\\''
# d = "it\'s"

# print(a, b, c, d)
# print(len(a))
# print(len(b))

#W11 D3 T6 - Fibonacci


# def fibonacci(n: int):
#     '''
#     This generator generates Fibonacci numbers indefinitely
#     '''
#     x = 0
#     y = 1
#     fib_numbers = []
    
#     for i in range(n):
#         fib_numbers.append(x)
#         x, y = y, x + y
    
#     return fib_numbers
        
# x = fibonacci(8)
# print(x)


#W11 D3 T7 - closures

# funcs = []
# for i in range(4):
#     funcs.append(lambda: i)

# print([f() for f in funcs])
    
# #We'd get [3, 3, 3, 3]
# #FIX:

# funcs = []
# for i in range(4):
#     funcs.append(lambda i=i: i)
    
# print([f() for f in funcs])


# def outer():
#     total = 0
#     def add(n):
#         nonlocal total
#         total += n
#         return total
#     return add

# f = outer()
# print(f(5))
# print(f(3))
# print(f(2))


#W11 D2 T8 - added time filtering for sessions
# '''
# This turned out to be quite a complex task, but it still will be extended even more in the future

# To add a time filter I had to make an important architectural decisions first - consulted Claude for that, as I honestly want to use this backtester for my own purposes
# For now I will be using filter in main.py's run_backtest method, which is getting pretty packed, BUT IMO STILL READABLE;

# - I also implemented abstractmethod for each strategy class with start and end time (with None as default)
# - I also had to add force close option (force_close_all method) to backtest_engine (which also required me to add remove_position to position_manager,
# as I didn't expect manual position removal besides standard SL/TP closing)

# Claude suggested ticker-based force close, but I opted for a strategy based close, as it makes A LOT MORE sense
# and I could have different strategies with different start/end times for whatever reason

# There's no point in me pasting all of the code excerpts here, but you can surely loop up my main.py (run_backtest)/position_manager.py/backtest_engine.py
# Also, I am planning more modifications, so that it becomes even more modular and prepared for handling multiple strategies with multiple different time filters in run_backtest all at once
# '''

#CD Python - task 87

'''
Stwórz funkcję top_results, która przyjmuje listę studentów oraz ich wyniki egzaminów.

Funkcja powinna zwrócić słownik, w którym:

kluczami są imiona studentów,
wartości to True lub False określające, czy dany student uzyskał wynik powyżej 90 percentyla.
Percentyl możesz policzyć za pomocą funkcji percentile z biblioteki numpy.
'''

# from typing import List, Dict
# import numpy as np

# def top_results(students_list: List[str], student_exam_grades: List[int]) -> Dict[str, bool]:
#     '''
#     A func, which calculates the 90th percentile and checks whether a given student exceeded it
    
#     Args:
#     Two lists - one with students' names (str), and another with students' exam grades (int).
    
#     Returns:
#     A dict with student names as keys and bool signifying whether a given student exceeded the 90th percentile, or not
#     '''
    
#     perc_90 = np.percentile(student_exam_grades, 90)
#     students_grades = list(zip(students_list, student_exam_grades))
#     final_dict = {student: True if grade > perc_90 else False for student, grade in students_grades}
    
#     return final_dict



# students = [
#     "Ola", "Ela", "Ania", "Bartek", "Tomek",
#     "Kasia", "Marek", "Julia", "Piotr", "Zosia",
#     "Adam", "Natalia", "Krzysztof", "Magda", "Paweł"
# ]

# exams = [
#     55, 60, 58, 72, 65,
#     90, 85, 88, 70, 95,
#     40, 77, 82, 91, 68
# ]


# print(top_results(students, exams))


#CD Python - task 88
'''
Na podstawie zmiennej orders znajdź użytkownika z największym zamówieniem i przypisz tę osobę do zmiennej top_order.

Do rozwiązania zadania spróbuj użyć funkcji max() z funkcją lambda, modyfikując poniższy kod.

max(orders, key = lambda x: x)
'''

# orders = [{"user": "Ola", "amount": 120}, {"user": "Ela", "amount": 80}, {"user": "Ania", "amount": 200}, {"user": "Bartek", "amount": 50}, {"user": "Tomek", "amount": 150}, {"user": "Kasia", "amount": 90}, {"user": "Marek", "amount": 300}, {"user": "Julia", "amount": 220}, {"user": "Piotr", "amount": 75}, {"user": "Zosia", "amount": 180}]

# top_order = max(orders, key = lambda x: x['amount'])['user']
# print(top_order)



#CD Python - task 89

'''
Napisz funkcję change_str, która zwraca string z przesuniętymi n elementami z końca stringu do indeksu i.

Przykłady
initial_string = "abcde"
n = 1
i = 3
1 ostatnia litera e zostaje przesunięta do indeksu 3, funkcja powinna zwrócić abced

'''

# def change_str(initial_string: str, n: int, i: int) -> str:
#     '''
#     A weird function, that causes the n values of the initial string to be moved from the end of the string to index i.
#     Args:
#     initial_string (str) - self-explanatory,
#     n - the number of characters you want to move to the index i
#     i - the index which is the desired place for the 'n' number of elements in the final string
    
#     Returns:
#     modified string
#     '''
    
#     cut_chars = initial_string[-n:]
#     cut_list = initial_string[:-n]
    
#     final_string = cut_list[:i] + cut_chars + cut_list[i:]
#     print(final_string)
#     return final_string


# initial_string = "abcde"
# n = 2
# i = 0

# print(change_str(initial_string, n, i))


#CD Python - task 90

'''
Zadanie
Stwórz funkcję higher_than_avg, która liczy ile kolejnych elementów jest większych niż średnia poprzednich elementów.
Pomiń liczenie dla pierwszego elementu.
'''

# from typing import List

# def higher_than_avg(nums: List) -> int:
#     '''
#     A func that calculates how many elements of a list are higher than the avg of all the previous elements.
#     It omits the first element of the list.
    
#     Args:
#     nums - list of numbers (here ints, but floats are also fine)
    
#     Returns:
#     The number of elements higher than the avg of their previous elements (int)
#     '''
    
#     higher = 0
#     for index, val in enumerate(nums, start = 1):
#         if val > sum(nums[:index]) / len(nums[:index]):
#             higher += 1
#     return higher


# numbers = [200, 500, 300, 800]
# print(higher_than_avg(numbers))


#W11 D4 #T1

# import os

# path = "/var/log/app/error.log"
# print(os.path.basename(path)) #error.log (the file)
# print(os.path.dirname(path)) #/var/log/app (the folder)
# print(os.path.split(path)) #('/var/log/app', 'error.log') - tuple with folder and file split
# print(os.path.splitext(path)) #('/var/log/app/error', '.log') - again tuple with folder and file, but this time the split fragment is the file type
# print(os.path.join("var", "log", "app")) #var\log\app (and this is very important, that this uniquely handles both Linux/Windows paths, dpeending on the used environment)


#W11 D4 T2

# a = '\\'        # ? Valid, len = 1
# b = "it\'s"     # ? Valid, it's, len = 4
# c = '\\\''      # ? Valid, \' , len = 2
# d = '\n\t'      # ? Valid, looks empty. len = 2
# e = "\\"        # ? Valid, \, len = 1

#W11 D4 T3 - InfiniteFibo generator

# def fibonacci():
#     x, y = 0, 1
#     while True:
#         yield x
#         x, y = y, x + y


# gen = fibonacci()
# for i in range(10):
#     print(f'Number: {i+1}, {next(gen)}')


# def squares(n):
#     for i in range(n-1):
#         yield i**2


# x = squares(5)
# print(next(x)) #0
# print(list(x)) #[1, 4, 9]
# print(next(x)) #StopIteration error


#W11 D4 T4 - output prediction

# try:
#     raise ValueError("bad input")
# except Exception:
#     print("Exception branch")
# except ValueError:
#     print("ValueError branch")
    
#Exception branch is printed

# try:
#     pass
# except ValueError:
#     print("caught")
# else:
#     print("else")
# finally:
#     print("finally")
    
#else - finally

#W11 D4 T5 - predict the output 

# x = 1
# def f():
#     x = 2
#     def g():
#         return x
#     x = 3
#     return g()

# print(f())

# #3



# def make_multiplier(n):
#     return lambda x: x * n

# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5), triple(5))

# #10, 15



# fns = [lambda x, n=n: x + n for n in range(4)]
# print(fns[2](10))

#12


#W11 D4 T6 - predint the output

# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))
# print(list(g))
# print(list(g))

# #1
# #2
# #[3]
# #[]



# def gen():
#     return
#     yield

# g = gen()
# print(type(g).__name__)
# print(list(g))

# #generator
# #[None]




# g = (x ** 2 for x in range(5))
# print(next(g))
# print(next(g))
# print(sum(g))

#0
#1
#29


#W11 D4 T7 - MRO 

# class A:
#     def f(self): return "A"

# class B(A):
#     def f(self): return "B" + super().f()

# class C(A):
#     def f(self): return "C" + super().f()

# class D(B, C):
#     pass

# print(D().f())

# #Output: BCA


# def outer():
#     x = []
#     def inner(val):
#         x.append(val)
#         return x
#     return inner

# f = outer()
# f(1) #[1]
# f(2) #[1, 2]
# print(f(3)) #[1, 2, 3]

#W11 D4 T8 - modularized run_backtest() in main.py to accept a list of strategies (each with its own defined start/end time).
#I've also modified base_strategy to create a uuid for every strategy.
#A next step would be to also add start/end time to each strategy instance so that we could run multiple tests of a given strategy with different start/end times
#Anyway, the tests were successful :))

#CD Python - task 91

'''
Napisz funkcję count_similar_words, która przyjmuje słowo word oraz listę słów words_list.

Funkcja powinna zwracać listę słów, które:

zaczynają się na tę samą literę co word
mają tę samą długość co word
Ignoruj wielkość liter (traktuj "Kot" i "kot" tak samo).
'''

# from typing import List


# def count_similar_words(word: str, words_list: List[str]) -> List[str]:
#     starting_letter = word[0]
#     word_length = len(word)
    
#     matching_words = [word for word in words_list if word[0].lower() == starting_letter.lower() and len(word) == word_length]
#     return matching_words

# word = "kot"
# words_list = ["koc", "pies", "kot", "KOT", "kto", "dom", "kog"]

# print(count_similar_words(word, words_list))


#CD Python - task 92
'''
Istnieją funkcje any() oraz all(), które przyjmują jako argument obiekt iterowalny i sprawdzają,
czy przynajmniej jeden (any) lub wszystkie (all) elementy z listy są prawdziwe (True).

Przykłady
any([1>0, 1==0, 1<0]) -> True
any([1<0, 2<1, 3<1]) -> False
all([1>0, 1==0, 1<0]) -> False
all([1>0, 2>1, 3>1]) -> True

Napisz funkcje is_positive, która sprawdza czy wszystkie elementy z listy numbers są większe od 0. Funkcja powinna zwracać wartości True / False.
'''
# from typing import List

# def is_positive(numbers_list: List) -> bool:
    
#     result = all([num > 0 for num in numbers_list])
#     return result

# numbers = [8, -10, 15, -4]
# print(is_positive(numbers))


#CD Python - task 93

'''
Dwa słowniki zawierają wyniki egzaminów kursantów, którzy uczestniczyli w kursie SQL i Python.

Stwórz pod zmienną top_students listę 3 studentów, którzy uczestniczyli w obydwu kursach i osiągnęli najlepsze średnie wyniki z wszystkich egzaminów z obydwu kursów.

'''


# students_sql = {"anna kowalska":[8,9,10,9],"piotr nowak":[6,7,8,7],"monika mazur":[10,9,10,10],"jan zielinski":[4,5,6,5],"pawel krawczyk":[9,8,9,10],"kasia lis":[7,8,7,8],"tomasz wojcik":[5,6,7,6],"agnieszka dabrowska":[9,9,8,9],"michal lewandowski":[6,5,7,6],"karolina krupa":[10,10,9,10],"lukasz wojciechowski":[8,7,8,9],"ola kaminska":[9,8,9,9],"bartosz sikora":[5,6,5,6],"patrycja adamska":[7,8,9,8],"kamil piotrowski":[6,7,6,7]}

# students_python = {"anna kowalska":[9,10,9,10],"piotr nowak":[7,8,7,8],"monika mazur":[10,10,10,9],"pawel krawczyk":[8,9,10,9],"kasia lis":[8,8,9,8],"tomasz wojcik":[6,7,8,7],"agnieszka dabrowska":[9,10,9,9],"michal lewandowski":[7,7,8,7],"karolina krupa":[10,9,10,10],"lukasz wojciechowski":[9,8,9,8],"ola kaminska":[8,9,9,8],"daniel czajka":[5,6,6,5],"natalia wrobel":[9,9,8,9],"katarzyna grabowska":[7,8,7,8],"mateusz kaczmarek":[6,7,6,7]}

# keys_to_remove = []
# for student in students_sql:
#     if student in students_python:
#         students_sql[student] += students_python[student]
#     else:
#         keys_to_remove.append(student)

# for key in keys_to_remove:
#     students_sql.pop(key)


# top_students = sorted(students_sql.items(), key = lambda x: sum(x[1])/len(x[1]), reverse = True)[0:3]
# top_students = [student[0] for student in top_students]



#CD Python - task 94

'''
Dwa słowniki zawierają wyniki egzaminów kursantów, którzy uczestniczyli w kursie SQL i Python.

W którym kursie mediana wszystkich egzaminów studentów była wyższa? Przypisz odpowiedź sql lub python do zmiennej course

Do obliczenia mediany możesz użyć funkcji median z biblioteki Numpy
'''

# import numpy as np


# students_sql = {"anna kowalska":[8,9,10,9],"piotr nowak":[6,7,8,7],"monika mazur":[10,9,10,10],"jan zielinski":[4,5,6,5],"pawel krawczyk":[9,8,9,10],"kasia lis":[7,8,7,8],"tomasz wojcik":[5,6,7,6],"agnieszka dabrowska":[9,9,8,9],"michal lewandowski":[6,5,7,6],"karolina krupa":[10,10,9,10],"lukasz wojciechowski":[8,7,8,9],"ola kaminska":[9,8,9,9],"bartosz sikora":[5,6,5,6],"patrycja adamska":[7,8,9,8],"kamil piotrowski":[6,7,6,7]}

# students_python = {"anna kowalska":[9,10,9,10],"piotr nowak":[7,8,7,8],"monika mazur":[10,10,10,9],"pawel krawczyk":[8,9,10,9],"kasia lis":[8,8,9,8],"tomasz wojcik":[6,7,8,7],"agnieszka dabrowska":[9,10,9,9],"michal lewandowski":[7,7,8,7],"karolina krupa":[10,9,10,10],"lukasz wojciechowski":[9,8,9,8],"ola kaminska":[8,9,9,8],"daniel czajka":[5,6,6,5],"natalia wrobel":[9,9,8,9],"katarzyna grabowska":[7,8,7,8],"mateusz kaczmarek":[6,7,6,7]}

# print(students_sql.values())
# course = 'sql' if np.median([value for value in students_sql.values()]) > np.median([value for value in students_python.values()]) else 'python'
# print(course)


#CD Python - task 95


'''
Napisz funkcje is_anagram, która sprawdza czy 2 słowa przekazane do tej funkcji są anagramami. Funkcja powinna zwracać wartość True lub False.

Anagram to wyraz powstały przez przestawienie liter innego wyrazu, przy wykorzystaniu wszystkich liter materiału wyjściowego dokładnie jeden raz.

Przykłady anagramów:
arbuz -> burza
ekran -> nerka
wektor -> wtorek
'''

# def is_anagram(word1: str, word2: str) -> bool:
#     '''
#     A func that checks if given two words are anagrams
#     Args:
#     word1 & word2 - strings
    
#     Returns:
#     bool
#     '''
#     sorted1 = sorted([char.lower() for char in word1])
#     sorted2 = sorted([char.lower() for char in word2])
    
#     result = sorted1 == sorted2
#     return result
    
# word_1 = "arbuz"
# word_2 = "burza"

# print(is_anagram(word_1, word_2))



#CD Python - task 96

'''
To pytanie jest już dużo trudniejsze, ale jest klasyką programowania, więc warto spróbować przynajmniej zrozumieć ten problem.

Napisz funkcję is_valid_parentheses, która sprawdza, czy nawiasy w podanym stringu są poprawnie zamknięte.

Zasady:

istnieją 3 typy nawiasów: (), [], {}
każdy otwierający nawias ma zamykający
nawiasy są poprawnie zagnieżdżone
Funkcja powinna zwracać True lub False.

Przykłady z poprawnymi nawiasami:
abc
(a + b)
[x * (y + z)]
{a + [b * (c + d)]}
Przykłady z niepoprawnymi nawiasami:
abc)
(
{]
[(])

'''

# def is_valid_parentheses(checked_string: str) -> bool:
#     '''
#     A function used to check whether all parentheses are correctly closed and matched
    
#     It checks three types of parentheses:
#     (), [], {}
    
#     Args:
#     checked_string - any string
    
#     Return:
#     bool
#     '''
    
#     #Valid = (, ) both in the string and ( before )
    
#     valid_parentheses = {')': '(',
#                          ']': '[',
#                          '}': '{'}
    
#     open_parentheses = []
#     is_closed = False
    
#     for i in checked_string:
#         if i in valid_parentheses.values():
#             open_parentheses.append(i)
#         elif i in valid_parentheses.keys():
#             if len(open_parentheses) == 0:
#                 return is_closed
#             elif valid_parentheses[i] == open_parentheses[-1]:
#                 open_parentheses.pop()
#             else:
#                 return is_closed
    
#     if len(open_parentheses) == 0:
#         is_closed == True
    
#     return is_closed

#     #difficult!

    
    
# initial_string = "[x * (y + z)]"

# print(is_valid_parentheses(initial_string))

#W11 D5 T1
# from datetime import datetime, timedelta

# dt = datetime(2026, 3, 27, 14, 45, 30)
# print(dt.year) #2026
# print(dt.hour) #14
# print(dt.minute) #45
# print(dt.date()) #2026-03-27
# print(dt.time()) #14:45:30


# dt = datetime(2026, 3, 27, 9, 0, 0)
# delta = timedelta(days=2, hours=3, minutes=30)
# result = dt + delta #2026-03-29 12:30
# print(result.day) #29
# print(result.hour) #12
# print(result.minute) #30


# td1 = timedelta(hours=2, minutes=30)
# td2 = timedelta(hours=1, minutes=45)
# diff = td1 - td2 #
# print(diff.seconds) #45 mins * 60 - WHAT THE FUCK, WHY WOULD I EVEN REMEMBER THAT?
# print(diff.total_seconds()) #same, stupid, retarded question - humans are not meant to be living calculators


# dt = datetime(2026, 3, 27, 9, 30, 0)
# print(dt.strftime("%Y-%m-%d")) #2026-03-27
# print(dt.strftime("%H:%M:%S")) #09:30:00
# print(dt.strftime("%d/%m/%Y %H:%M")) #27/03/2026 9:30


#W11 D5 T2

# from datetime import datetime, time

# s = "2026-03-27 09:30:00"
# dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
# print(dt.year) #2026
# print(dt.minute) #30
# print(type(dt).__name__) #datetime


# from datetime import time

# t1 = time(9, 0)
# t2 = time(17, 30)
# t3 = time(10, 15)

# print(t1 < t3 < t2) #True
# print(t3 > t2) #False
# print(t1 == time(9, 0, 0)) #True


# from datetime import date, datetime

# d1 = date(2026, 3, 27)
# d2 = date(2026, 3, 1)
# delta = d1 - d2
# print(delta.days) #26
# print(type(delta).__name__) #timedelta


# print(datetime.now())
# print(datetime.today())

#W11 D5 T3

# try:
#     x = int("abc")
# except TypeError:
#     print("TypeError")
# except ValueError:
#     print("ValueError")
# except Exception:
#     print("Exception")

#ValueError

# def f():
#     try:
#         return 1
#     finally:
#         return 2

# print(f()) #2


# x = 0
# try:
#     x = 1
#     raise RuntimeError
#     x = 2
# except RuntimeError:
#     x += 10
# else:
#     x += 100
# finally:
#     x += 1000

# print(x) #1011



# class MyError(Exception):
#     pass

# class SpecificError(MyError):
#     pass

# try:
#     raise SpecificError("oops")
# except MyError as e:
#     print(type(e).__name__)

#SpecificError


#W11 D5 T4
# class A:
#     def __init__(self):
#         self.x = 1

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.x += 10

# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.x += 100

# class D(B, C):
#     pass

# d = D()
# print(d.x) #111



# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1

# a = Counter()
# b = Counter()
# c = Counter()
# print(Counter.count) #3
# print(a.count) #3



# class A:
#     def hello(self):
#         return "A"

# class B(A):
#     pass

# class C(A):
#     def hello(self):
#         return "C"

# class D(B, C):
#     pass

# print(D().hello())

#MRO: D -> B -> C -> A
#Output: C


#W11 D5 T5

# def gen(n):
#     for i in range(n):
#         yield i * 2

# g = gen(4)
# print(next(g)) #0
# print(next(g)) #2
# print(list(g)) #[4, 6]
# print(list(g)) #[]


# def gen():
#     yield 1
#     yield from range(2, 5)
#     yield 5

# print(list(gen())) #[1, 2, 3, 4, 5]


# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration
#         self.current += 1
#         return self.current

# print(list(Counter(4)))   #[1, 2, 3, 4]


# g = (x for x in range(10) if x % 3 == 0)
# print(next(g)) #0
# print(next(g)) #3
# print(list(g)) #[6, 9]


#W11 D5 T6

# fns = []
# for i in range(3):
#     fns.append(lambda: i * 2)

# print([f() for f in fns]) #[4, 4, 4]


# fns = [lambda i=i: i * 2 for i in range(3)]
# print([f() for f in fns]) #[0, 2, 4]

# from functools import reduce

# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda acc, x: acc + x, nums, 10)
# print(result) #25

# data = [3, 1, 4, 1, 5, 9]
# result = sorted(data, key=lambda x: -x)
# print(result[:3]) #[9, 5, 4]


#PCAP Exam final prep
# g = (x ** 2 for x in range(6))
# print(next(g))
# print(next(g))
# print(sum(g))

# def gen():
#     return
#     yield 1
#     yield 2


# def gen():
#     yield
#     return
#     yield 1


# g = gen()
# print(type(g).__name__)
# print(list(g))



# with open("test.txt", "w") as f:
#     f.write("hello")

# with open("test.txt", "r") as f:
#     print(repr(f.read(3))) #hel
#     print(repr(f.read(10)))  #lo


# x = 'global'

# def f():
#     print(x)
#     x = 'local'

# f()


# from datetime import date

# d1 = date(2026, 1, 1)
# d2 = date(2026, 3, 28)
# delta = d2 - d1
# print(delta.days)
# print(type(delta).__name__)

# import platform
# print(platform.platform())
# print(platform.uname())


# import sys
# b1 = type(dir(sys)) is str
# b2 = type(sys.path[-1]) is str
# print(b1 and b2)



# m = 0

# def foo(n):
#     global m
#     assert m != 0
#     try:
#         return 1/n
#     except ArithmeticError:
#         raise ValueError
    
# try:
#     foo(0)
# except ArithmeticError:
#     m += 2
# except:
#     m += 1
# print(m) #1


# d = {'1': '1', '2': '2'}
# try:
#     d['1'] = d['3']
# except BaseException as error:
#     print(type(error))
    
#KeyError


# x = 'python'.find('')
# x = 'python'.rindex('th') #print(x) #2
# #x = sort('python') #WRONG, NOT A STRING METHOD!
# #x ='python'.sorted() - WRONG as well


# the_string = ',,'.join(('alpha', 'omega'))
# the_list = the_string.split(',')
# print(',' in the_list) #False
# print(the_list)




# class A:
#     __VarA = 1

#     def get(self):
#         return self.__VarA

# class B(A):
#     __VarA = 2

#     def get(self):
#         return self.__VarA

# class C(B):
#     __VarA = 3

# obj_a = A()
# obj_b = B()
# obj_c = C()


# print(hasattr(B, 'get')) #True
# print(obj_c.get() == 2) #True
# print(isinstance(obj_b, C)) #False
# print(C._C__VarA == 2) #False

# x = 8 ** (1 / 3)
# y = 2. if x < 2.3 else 3.
# print(y) #2.0


# def foo(x, y, z):
#     return x(y) - x(z)

# print(foo(lambda x: x % 2, 2, 1))


# my_list = [i for i in range(5)]
# m = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]
# print(m)


# import random 

# a = random.random()
# b = random.uniform(0, 10)
# c = random.randint(0, 10)
# d = random.randrange(0, 3)
# e = random.choice(list(range(5)))
# f = random.sample(list(range(5)), k=1)

# print(d, type(f))

#W12 D1 T1

# try:
#     {}['missing']
# except BaseException as e:
#     print(type(e).__name__) #KeyError - despite the handle
#     print(str(e)) #'missing'
    
    
# try:
#     raise FileNotFoundError("gone")
# except OSError as e:
#     print(e) #gone
#     print(type(e).__name__) #FileNotFoundError
#     print(isinstance(e, OSError)) #True
#     print(isinstance(e, FileNotFoundError)) #True
    
    
# try:
#     int("abc")
# except Exception as e:
#     print(e) #invalid literal for int() with base 10: 'abc'
#     print(type(e) is ValueError) #True
#     print(type(e) is Exception) #False


# try:
#     1 / 0
# except ArithmeticError as err:
#     print(type(err) is ArithmeticError) #False
#     print(type(err) is ZeroDivisionError) #True
#     print(type(err).__name__ == 'ArithmeticError') #False
#     print(isinstance(err, ZeroDivisionError)) #True


#W12 D1 T2


# def foo():
#     raiseRuntimeError

# foo()

#NameError, undefined


# try:
#     raise IndexError
# except TypeError:
#     raise ValueError
# except:
#     print("caught") #this is printed


# m = 0

# def foo(n):
#     global m
#     assert m != 0
#     try:
#         return 1/n
#     except ArithmeticError:
#         raise ValueError
    
# try:
#     foo(0)
# except ArithmeticError:
#     m += 2
# except:
#     m += 1
# print(m) #1? Why???

#W12 D1 T3
# - `print(e)` calls `__str__`
# - `str(e)` calls `__str__`
# - `repr(e)` calls `__repr__` (default: `ClassName(args)`)
# - `print(type(e).__name__)` → class name string


# class AppError(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)
#         self.code = 500

#     def __str__(self):
#         return f"AppError[{self.code}]"

# try:
#     raise AppError("server down")
# except AppError as e:
#     print(e) #AppError[500]
#     print(str(e)) #AppError[500]
#     print(e.args[0]) #server down - THIS IS VERY UNINTUITIVE
#     print(type(e).__name__) #AppError
#     print(e.args) #('server down',) 



# class AppError(Exception):
#     def __init__(self, msg):
#         self.code = 500          # no super().__init__()
#     def __str__(self):
#         return f"AppError[{self.code}]"

# try:
#     raise AppError("server down")
# except AppError as e:
#     print(e) #AppError[500]
#     print(e.args) #('server down',)


# class InvalidPriceError(Exception):
#     def __init__(self, price: float, reason: str):
#         self.reason = reason
#         self.price = price
    
#     def __str__(self):
#         return f'Invalid price {self.price}: {self.reason}'
    

# def mock_func(a):
#     if a < 0:
#         raise InvalidPriceError((a), 'Lol')

# mock_func(-1)



#W12 D1 T4


# class A:
#     x = 10
#     def __init__(self):
#         self.y = 20

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# d = D()

# print(D.__bases__) #<class '__main__.B'>, <class '__main__.C'>
# print(d.__class__)
# print(D.__mro__) #(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# print(D.__dict__) #{'__module__': '__main__', '__firstlineno__': 12978, '__static_attributes__': (), '__doc__': None}
# print(A.__dict__) #{'__module__': '__main__', '__firstlineno__': 12967, 'x': 10, '__init__': <function A.__init__ at 0x00000192DF197C40>, '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# print(d.__dict__)

#W12 D1 T5 - Lambdas edge cases

# "Cannot return None"              → FALSE — lambdas CAN return None
# "Cannot be defined without params"→ FALSE — lambda: 42 is valid
# "Must contain return keyword"     → FALSE — return is implicit
# "Are anonymous functions"         → TRUE
# "Can be defined without params"   → TRUE



# def foo(x, y, z):          # x here is the FUNCTION
#     return x(y) - x(z)     # x(y) = call that function with y

# print(foo(lambda x: x % 2, 2, 1))

#return foo(2) - foo(1)
#0 - 1 = -1


# 1. lambda: 42               — valid Python? #Yes
# 2. lambda x: print(x)      — can this return None? #
# 3. f = lambda: None; f()   — what does f() return?
# 4. lambda x, y: x + y      — valid (multi-param)?
# 5. lambda x: return x + 1  — valid Python?
# 6. result = (lambda x: x**2)(5) — what is result?

# lambda: 42
# print(lambda: 42)

# x = None
# f = lambda: None
# print(f()) #Works propelry

# result = (lambda x: x**2)(5) #25
# print(result)

# def apply(fn, a, b):
#     return fn(a) + fn(b)

# print(apply(lambda x: x ** 2, 3, 4)) #fn(3) + fn(4) = 9 + 16 = 25
# print(apply(lambda x: x % 2, 7, 4)) #fn(7) + fn(4) = 1 + 0 = 1

# def foo(x, y, z):
#     return x(y) - x(z)

# print(foo(lambda x: x % 2, 2, 1)) # foo(2) - foo(1) = 0 - 1 = -1
# print(foo(lambda x: x * 3, 5, 2)) # foo(5) - foo(2) = 15 - 6 = 9

#W12 D1 T6
# range(4, 0, -1) → iterates: 4, 3, 2, 1 (DESCENDING)
# # Result preserves ITERATION ORDER, not sorted order
# # If you iterate 4→3→2→1 and pick odds: 3, 1 → output [3, 1] not [1, 3]


# #File I/O
# Default mode    → 'r' (NOT 'w'!)
# 'w' mode        → truncates all previous content
# 'a' mode        → appends (safe for logs)
# 'x' mode        → fails if file already exists
# 'r+' mode       → read+write, file MUST exist

# my_list = [0, 1, 2, 3, 4]
# m = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]
# print(m) #[3, 1]

# evens = [x for x in range(10, 0, -2)]
# print(evens) #[10, 8, 6, 4, 2]

# squares = [x**2 for x in range(5, 0, -1) if x % 2 == 0]
# print(squares) #[16, 4]


#W12 D1 T7

# 2.          # float: 2.0       ← real exam trap
# 1_000_000   # int with underscores
# 0xFF        # hex int: 255
# 0o77        # octal int: 63
# 0b1010      # binary int: 10
# 3+2j        # complex number

#The above cause NO ERRORS whatsoever

# import platform
# print(platform.platform())     # full platform string: 'Windows-10-...'
# print(platform.system())        # just OS name: 'Windows'
# print(platform.uname())         # namedtuple with ALL info — NOT just platform name
# print(platform.python_version())# Python version: '3.11.4'

# print(type(1_000_000))
# print(1_000_000) #prints as normal int, 1000000

# x = 8 ** (1/3) #8 ** (1/3) - pierwiastek szescienny z 8 inaczej
# # print(x) #2.0
# y = 2. if x < 2.3 else 3.
# print(y) #2.0
# print(type(y)) #float


#W12 D1 T8 - Name mangling + inheritance traps

# class A:
#     __x = 1           # stored as _A__x
#     def get(self): return self.__x   # compiled: self._A__x

# class B(A):
#     __x = 2           # stored as _B__x
#     def get(self): return self.__x   # compiled: self._B__x

# class C(B):
#     __x = 3           # stored as _C__x
#     # NO get() method defined here!
    
# #MRO = C -> B -> A -> object
# x = C()
# print(x)
# print(C.__mro__)
# print(x.__dict__)

#There is no get() method in C, so the x.get() method resolves to B.get(). In there, self.__x was compiled as self._B__x = 2
#THIS IS VERY WEIRD AND DIFFICULT, DEFINITELY A SNEAKY TRAP AND WE NEED TO LEARN THIS WELL



# class A:
#     __VarA = 1
#     def get(self): return self.__VarA

# class B(A):
#     __VarA = 2
#     def get(self): return self.__VarA

# class C(B):
#     __VarA = 3

# obj_a = A() #MRO: A
# obj_b = B() #MRO: B -> A -> obj
# obj_c = C() #MRO: C -> B -> A -> obj

# print(obj_a.get()) #1
# print(obj_b.get()) #2
# print(obj_c.get()) #2 AGAIN, AS THERE'S NO get() method here, so the last get is taken from the B object
# print(obj_c._C__VarA) #3
# print(obj_c._B__VarA) #2


#hasattr(B, 'get')                  # True
#obj_c.get() == 2                   # True
#isinstance(obj_b, C)               # False - obj_b is not an instance of C class, but rather of B
#C._C__VarA == 3                    # True
#obj_c._A__VarA == 1                # True

# print(isinstance(obj_b, C)) #False
# print(isinstance(obj_b, A)) #But as it inherits from A, it's an instance of A as well, True


#W12 D2 T1

# x = 0

# def bar(n):
#     assert n > 0, "must be positive"
#     try:
#         return 100 / n
#     except ZeroDivisionError:
#         return -1

# try:
#     result = bar(0)
# except AssertionError:
#     x = 1
# except:
#     x = 2
# print(x) #1


#bar() is called with 0
#assertion fails, but it's not handled in the function, so it's propagated outside to the outer try.
#it's handled there and x is set to 1

# count = 0

# def process(val):
#     assert isinstance(val, int), "not int"
#     try:
#         return val * 2
#     except TypeError:
#         return 0

# try:
#     process("hello")
# except TypeError:
#     count = 10
# except AssertionError:
#     count = 20
# except:
#     count = 30
# print(count) #20

#process is called with 'hello' string as an argument
#the assertion fails, and it's not handled in the process function, so it would normally crash the code, but it's in the outer try block instead
#TypeError is ignored, as it's not the error type raised here
#It's handled by the except with AssertionError, setting the count to 20


# def inner(x):
#     if x < 0:
#         raise ValueError("negative")
#     return x

# def outer(x):
#     try:
#         return inner(x) * 2
#     except TypeError:
#         return -1

# try:
#     outer(-5)
# except ValueError as e:
#     print("caught:", e)
# except:
#     print("bare caught")
    

#outer is called with -5 as an argument
#outer calls inner with -5 as an argument in a try block
#inner does a check and since -5 is lower than 0, it raises ValueError with 'negative'
#since everything is put in a try/except block with ValueError handling, it prints caught: nagative


# m = 0

# def foo(n):
#     global m
#     assert n > 0
#     try:
#         return 10 / n
#     except ArithmeticError:
#         raise RuntimeError("math fail")

# try:
#     foo(-1)
# except RuntimeError:
#     m += 10
# except AssertionError:
#     m += 5
# except:
#     m += 1
# print(m)

#foo is called with -1 as an argument
#foo properly grabs the value of m with global keyword
#foo runs an assertion for the argument, which fails, as -1 is lower than 0 
#It's NOT handled by the foo function , as it's put outside the try/except block there, so it propagates to the outside
#Since the whole foo call is put into a try/except block - there is a chance it will handle that exception
#It's handled by the except AssertionError handle, putting m at 5


#W12 D2 T2

# class Vehicle:
#     wheels = 4
#     engine = "V6"

#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#         self._speed = 0

#     def accelerate(self):
#         self._speed += 10

# v = Vehicle("Toyota", 2020)

# print('wheels' in Vehicle.__dict__)      #True
# print('engine' in Vehicle.__dict__)      #True
# print('accelerate' in Vehicle.__dict__)  #True
# print('brand' in Vehicle.__dict__)       #False
# print('brand' in v.__dict__)             #True
# print('_speed' in v.__dict__)            #True
# print('wheels' in v.__dict__)            #False
# print('__init__' in Vehicle.__dict__)    #True


# v.accelerate()
# v.accelerate()
# print(v.__dict__)    # predict the full output


# {'brand': 'Toyota', 'year': 2020, '_speed': 20}


# class A:
#     x = 1
#     def __init__(self):
#         self.x = 2       # shadows the class attr

# a = A()
# print('x' in A.__dict__)    #True
# print('x' in a.__dict__)    #True
# print(a.x)                  #2
# print(A.x)                  #1


#W12 D2 T3

# type(obj) is SomeClass    → EXACT match only — ignores inheritance
# isinstance(obj, SomeClass) → True if obj is SomeClass OR any subclass

# class Animal: pass
# class Dog(Animal): pass
# class GuideDog(Dog): pass

# g = GuideDog()


# print(type(g) is GuideDog)      # True
# print(type(g) is Dog)           # False
# print(type(g) is Animal)        # False
# print(isinstance(g, GuideDog))  # True
# print(isinstance(g, Dog))       # True
# print(isinstance(g, Animal))    # True
# print(isinstance(g, object))    # True


# class X: pass
# class Y(X): pass
# obj = Y()

# print(type(obj) is X) #False
# print(type(obj) is Y) #True
# print(isinstance(obj, X)) #True
# print(type(obj) == isinstance(obj, Y)) #False


# print(type(42) is int) #True
# print(type(42) is float) #False
# print(isinstance(42, (int, float)))  #True
# print(isinstance(True, int))        #True
# print(type(True) is int)        #False

#W12 D2 T4

# class Base:
#     __secret = "base"
#     def reveal(self):
#         return self.__secret          # compiled: self._Base__secret

# class Middle(Base):
#     __secret = "middle"
#     def reveal(self):
#         return self.__secret          # compiled: self._Middle__secret

# class Top(Middle):
#     __secret = "top"
    
    

# b = Base()
# m = Middle()
# t = Top()

# print(b.reveal())           # 'base'
# print(m.reveal())           # 'middle'
# print(t.reveal())           # 'middle' - there's no reveal in Top, so Middle's reveal() runs
# print(t._Top__secret)       # top
# print(t._Middle__secret)    # middle
# print(t._Base__secret)      # base


# print(hasattr(Top, 'reveal'))         # False
# print(hasattr(Top, '_Top__secret'))   # True
# print(Top.__bases__ == (Middle,))     # True
# print(Middle in Top.__mro__)          # True
# print(Base in Top.__mro__)            # True
# print(len(Top.__mro__))               # 4
# print(Top.__mro__)

#W12 D2 T5

# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(C, D): pass

# print(E.__bases__)          #C, D
# print(E.__mro__)            #E -> C -> D -> B -> A -> object
# print(len(E.__mro__))       # 6
# print(A in E.__bases__)     # False
# print(A in E.__mro__)       # True
# print(B in E.__bases__)     # False


# class X: pass
# class Y(X): pass
# class Z(X, Y): pass    # ← is this valid? - NO!

#TypeError, this is flase


#W12 D2 T6
# import platform
# platform.platform()       # 'Windows-10-10.0.19041-SP0' — full string
# platform.system()         # 'Windows' — just OS name
# platform.node()           # hostname of machine
# platform.python_version() # '3.11.4'
# platform.uname()          # named tuple with ALL: system, node, release, version...

# import os
# path = os.getcwd()               # current working directory string
# os.listdir(path)          # list of filenames in directory
# os.path.exists(path)      # True/False
# os.path.join('xd', 'pd')        # safe path joining (handles slashes)
# print(os.path.basename(path))    # last component: '/foo/bar.txt' → 'bar.txt'
# print(os.path.dirname(path))     # directory part: '/foo/bar.txt' → '/foo'
# os.sep                    # path separator: '\\' on Windows, '/' on Unix
# os.name                   # 'nt' on Windows, 'posix' on Unix/Mac

#Which platform funciton returns these?
# 1. The string `'Windows'` (OS name only, no version)
# 2. A namedtuple with system, node, release, version, machine, processor
# 3. The Python version as a string like `'3.11.4'`
# 4. The full platform description string including version numbers

# 1 - platform.system()
# 2 - platform.uname()
# 3 - platform.python_version()
# 4 - platform.platform()

#True or False about `os`:

# import os
# # assume running on Windows
# print(os.name == 'nt')           # True
# print(os.sep == '\\')            # True
# print(os.sep == '/')             # False - this is on UNIX
# print(type(os.getcwd()) is str)  # True


# import os
# path = '/home/user/projects/algo/data/prices.csv'
# print(os.path.basename(path))   # prices.csv
# print(os.path.dirname(path))    # /home/user/projects/algo/data
# print(os.path.exists(path))     # False



#W12 D2 T7

# # bytes — IMMUTABLE sequence of integers 0-255
# b = b"hello"
# b[0]          # 104 (ASCII code of 'h')
# b[0] = 65     # TypeError! bytes is immutable

# # bytearray — MUTABLE bytes
# ba = bytearray(b"hello")
# ba[0] = 72    # OK → bytearray(b'Hello')
# ba[0]         # 72

# # Creating:
# bytes(5)              # b'\x00\x00\x00\x00\x00' — 5 zero bytes
# bytes([72, 101, 108]) # b'Hel' — from int list
# bytearray(b"abc")     # mutable copy of bytes literal

# # Encoding / decoding:
# "hello".encode('utf-8')        # b'hello'
# b"hello".decode('utf-8')       # 'hello'

# b = b"Python"
# print(b[0])                  # 80 - but I had to check that  - I won't remember it by heart, this shouldn't be the goal of this
# print(type(b[0]))            # int
# print(len(b))                # 6
# b[0] = 80                    # Error!


# ba = bytearray(b"Python")
# ba[0] = 112                  # lowercase 'p' = 112 
# print(ba)                    # #bytearray(b'python')
# print(ba.decode('utf-8'))    # python


# data = bytearray(b"hello")
# data.append(33)         # 33 = '!'
# print(data.decode())    # 'hello!'
# print(list(data))       # 'h', 'e', 'l', 'l', 'o', '!' #in byte codes, which I don't know and DON'T EXPECT ME TO KNOW THEM BY HEART



#W12 D3 T1

# str.find(sub)      → returns index or -1  (no exception)
# str.index(sub)     → returns index or raises ValueError
# str.count(sub)     → non-overlapping occurrences
# str.split(sep)     → default sep=None splits on ANY whitespace, strips leading/trailing
# str.split(' ')     → splits on single space only — '' entries for multiple spaces!
# str.strip()        → removes BOTH ends
# str.lstrip()       → left only
# str.rstrip()       → right only
# str.replace(a, b)  → replaces ALL occurrences by default
# str.replace(a, b, n) → replaces at most n occurrences


# s = "  hello world  "
# print(s.strip()) #"hello world"
# print(s.lstrip()) #"hello world  "
# print(s.rstrip()) #"  hello world"
# print(len(s))  #15
# print(len(s.strip())) #11


# s = "a  b  c"
# print(s.split())    #['a', 'b', 'c']
# print(s.split(' '))   #['a', '', 'b', '', 'c']
# print(s.count('a')) #1
# print(s.find('z')) #-1
# print(s.index('b')) #3


# s = "banana"
# print(s.replace('a', 'o'))  #bonono
# print(s.replace('a', 'o', 2)) #bonona
# print(s.count('a')) #3
# print(s.count('an')) #2


#W12 D3 T2

# \n   → newline
# \t   → tab
# \\   → literal backslash
# \'   → literal single quote (inside single-quoted string)
# \"   → literal double quote
# \r   → carriage return (cursor to start of line, does NOT add newline)

# print("hello\rworld")   # 'world' overwrites 'hello' from position 0
# # Output on most terminals: 'world'
# # But len("hello\rworld") = 11  — \r is ONE character


# print("line1\nline2") #line1(new line)line2
# print("col1\tcol2") #col1   col2
# print("back\\slash") #back\slash
# print(len("a\tb")) #a   b
# print(len("a\\b")) #a\b
# print(len("\n")) # '(new line)'

# s1 = '\'' #"'"", 1
# s2 = "\"" # """, 1
# s3 = '\\\'' # "\'" 2
# s4 = "\\\"" # "\""2

# print(len(s1), s1)
# print(len(s2), s2)
# print(len(s3), s3)
# print(len(s4), s4)


# print("AAAA\rBB") #BBAA - this is a bit weird
# print(len("AAAA\rBB")) #7 -- also werid, we count all characters + /r as 1


#W12 D3 T3
# def make_adder(n):
#     def add(x):
#         return x + n    # n is captured by reference
#     return add

# add5 = make_adder(5)
# print(add5) #funciton memory object
# print(add5(3))    # 8 — n=5 is still alive in the closure

# def outer():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# f = outer()
# print(f) #function memory object
# print(f()) #1
# print(f()) #2
# print(f()) #3


# string = str(1/3)
# dummy = ''
# for character in string:
#     dummy = dummy + character
# print(dummy[-1])  #3
# print(dummy)


# string = 'REPTILE'[:3:] #REPILE #E + LE
# print(string) #REP - this is actually weird - it's a confusing pattern, as the second : is there to just deceive us and confuse - WE NEED TO TAKE THIS INTO ACCOUNT
# string = string[-1] + string[-2::-1]
# print(string)


# def outer():
#     x = 10
#     def inner():
#         x = 20        # creates LOCAL x, does NOT modify outer x
#         return x
#     inner()
#     return x

# print(outer()) #10


# funcs = []
# for i in range(4):
#     funcs.append(lambda: i)

# print(funcs[0]()) #3
# print(funcs[2]()) #3
# print(funcs[3]()) #3


# funcs = []
# for i in range(4):
#     funcs.append(lambda i=i: i)   # i=i captures current value

# print(funcs[0]()) #0
# print(funcs[2]()) #2
# print(funcs[3]()) #3


#W12 D3 T4
# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(g) #gen memory object
# next(g)   # 1
# next(g)   # 2
# next(g)   # 3
# next(g)   # StopIteration raised



# def gen():
#     yield 1
#     return          # legal — causes StopIteration immediately
#     yield 2         # NEVER reached

# print(list(gen()))    # [1]

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# list(countdown(3))   # [3, 2, 1]



# def gen():
#     print("start")
#     yield 1
#     print("middle")
#     yield 2
#     print("end")

# g = gen() #start
# print(next(g)) #1
# print(next(g)) #middle\n2
# print("done") #done

# def gen(flag):
#     yield 1
#     if flag:
#         return
#     yield 2
#     yield 3

# print(list(gen(True))) #[1]
# print(list(gen(False))) #[1, 2, 3]




# def evens_up_to(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1

# result = list(evens_up_to(8)) #[0, 2, 4, 6, 8]
# print(result) #[0, 2, 4, 6, 8]
# print(sum(evens_up_to(6))) #12


#W12 D3 T5
# hasattr(obj, 'name')          # checks the full MRO chain — inherited counts!
# 'name' in SomeClass.__dict__  # checks ONLY this class's own namespace


# class A:
#     def foo(self): pass

# class B(A): pass

# hasattr(B, 'foo')        # True — inherited from A
# 'foo' in B.__dict__      # False — not defined IN B
# 'foo' in A.__dict__      # True — defined IN A


# class Shape:
#     color = 'red'
#     def area(self): return 0

# class Circle(Shape):
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5)

# print(hasattr(c, 'color'))           # True
# print(hasattr(c, 'area'))            # True
# print(hasattr(c, 'radius'))          # True
# print('color' in Circle.__dict__)    # False
# print('area' in Circle.__dict__)     # True
# print('area' in Shape.__dict__)      # True
# print('radius' in Circle.__dict__)   # False - this is very tricky! It's not instantiated so it's not present there
# print('radius' in c.__dict__)        # True


# print('color' in c.__dict__)         # False
# print('color' in Shape.__dict__)     # True
# print(hasattr(Shape, 'area'))        # True
# print(hasattr(Circle, 'color'))      # True


#W12 D3 T6

# def f(x=[]):
#     x.append(1)
#     return x

# print(f()) #[1]
# print(f()) #[1, 1]
# print(f()) #[1, 1, 1]


# def gen():
#     yield 1
#     yield 2
#     yield 3
    
# x = gen()
# print(x())

#W12 D3 T7

# def f():
#     try:
#         return "try"
#     except:
#         return "except"
#     finally:
#         return "finally"

# print(f()) #finally

# def g():
#     try:
#         return 10
#     finally:
#         print("cleanup") #cleanup

# print(g()) #10



# def h():
#     try:
#         raise RuntimeError("boom")
#     except RuntimeError:
#         return "caught"
#     finally:
#         print("always")

# print(h())
#always, caught


#W12 D4 T1
# s = 'REPTILE'
# print(s[:3:]) #REP
# print(s[:3:1])     #REP     
# print(s[::2])          #RPIE
# print(s[::-1])        #ELITPER
# print(s[-1] + s[-2::-1])  #E + LITPER [od drugiej litery, do tyłu]

# s = 'PYTHON'
# print(s[-1] + s[-2::-1])  #N + OHTYP -> NOHTYP
# print(s[2:5]) #THO
# print(s[2:5:])    #THO        
# print(s[1::2])     #YHN   
# print(s[-3:])      #HON 

# s = 'abcdef'
# print(s[-1]) #f
# print(s[-3:-1]) #de
# print(s[-3::1])    #def
# print(s[-1:-4:-1])  #fed


#W12 D4 T2

# s = "banana"
# print(s.find('a'))     # 1
# print(s.rfind('a'))    # 5
# print(s.index('a'))    # 1
# print(s.rindex('a'))   # 5
# print(s.find('z'))     # -1
# print(s.rfind('z'))    # -1

# s = "hello"
# print(s.index('l'))    # 2
# print(s.rindex('l'))   # 3

# try:
#     print(s.index('z'))
# except ValueError as e:
#     print(f"ValueError: {e}") #ValueError: substring not found
# try:
#     print(s.rindex('z'))
# except ValueError as e:
#     print(f"ValueError: {e}") #ValueError: substring not found


#W12 D4 T3


# import sys
# sys.argv          # list of command-line args: argv[0] = script name
# sys.path          # list of directories Python searches for modules
# sys.modules       # dict of all currently imported modules (cached)
# sys.stdin         # standard input stream
# sys.stdout        # standard output stream
# sys.stderr        # standard error stream
# sys.exit(code)    # exit interpreter; code=0 is clean exit
# sys.version       # Python version string: '3.11.4 (main, ...)'
# sys.platform      # 'win32', 'linux', 'darwin'


# import mymodule          # loads, executes, caches in sys.modules
# import mymodule          # does NOT reload — returns cached version
# # State mutations from first import PERSIST on re-import


# 1. sys.argv[0] is the first argument passed to the script (not the script name) #FALSE
# 2. sys.path can be modified at runtime to add new import directories #True
# 3. import X twice always re-executes the module code #False
# 4. sys.exit(0) raises SystemExit #True
# 5. sys.platform returns 'windows' on Windows #False, win32
# 6. sys.modules is a dictionary #True


# import sys
# print(sys.argv) #practice.py
# print(sys.argv[0]) #practice.py
# #print(sys.argv[1]) #IndexError
# print(len(sys.argv)) #1


# import sys

# import os
# import os    # second import
# print(len([k for k in sys.modules if 'os' in k]))   # how many 'os'-related entries? #2
# print('os' in sys.modules) #True
# print(type(sys.modules['os'])) #module

# print(sys.modules)

#W12 D4 T4 - os review

'''import os

os.getcwd()                  # current working directory
os.chdir(path)               # change working directory
os.listdir(path)             # list contents of directory
os.mkdir(path)               # create directory (fails if exists)
os.makedirs(path)            # create dirs recursively
os.remove(path)              # delete a FILE
os.rmdir(path)               # delete an empty DIRECTORY
os.rename(src, dst)          # rename file or directory

os.path.exists(path)         # True/False
os.path.isfile(path)         # True only if it's a file
os.path.isdir(path)          # True only if it's a directory
os.path.join(a, b, c)        # OS-safe path join
os.path.split(path)          # returns (dir, filename) tuple
os.path.splitext(path)       # returns (path_without_ext, ext) tuple
os.path.basename(path)       # filename only
os.path.dirname(path)        # directory only
os.path.abspath(path)        # absolute path

os.sep                       # '\\' Windows, '/' Unix
os.name                      # 'nt' Windows, 'posix' Unix
os.linesep                   # '\r\n' Windows, '\n' Unix'''


#W12 D4 T5

# def f():
#     try:
#         raise ValueError("first") 
#     except ValueError:
#         raise RuntimeError("second") 
#     finally:
#         print("finally")

# try:
#     f()
# except RuntimeError as e:
#     print(f"caught: {e}")
    
    
# 1. inner raise is carried out by the ValueError handler - it raises RuntimeError (which is caught by the outer try/except block)
# 2. At the same time, finally is printed, as it always is.
# 3. The outer except RuntimeError handle catches the Runtime Error and prints caught: second (the msg from the handle + the message from the raise)

#finally
#caught: second

# def g():
#     try:
#         raise KeyError("missing")
#     except ValueError:
#         return "value error caught"
#     finally:
#         print("cleanup")

# try:
#     g()
# except KeyError as e:
#     print(f"key error: {e}")
    
#1 - KeyError is raised but there's no handler for it in the g() function
#2 - it propagates to the outside and is handler by the KeyError handler there printing - key error: missing
#3 cleanup is printed, as the last element of the g() function from the finally block

#I'm wrong with the order - it's actualy cleanup -> key error: 'missing'.
#I don't understand why though - how to determine what is first - the inner finally or the outer message?


# try:
#     try:
#         1 / 0
#     except ZeroDivisionError as e:
#         raise ValueError("bad input") from e
# except ValueError as e:
#     print(type(e).__name__)
#     print(type(e.__cause__).__name__)
    

#The division raises the handler with ZeroDivisionError, but the handler raises ValueError found in the outer try/except block.
#The outer block prints ZeroDivisionError , ZeroDivisionError
#I was FUCKING WRONG AGAIN, BUT WHY!!!
#In the exam trap there was a KeyError handled by the BaseException handler, but it still fucking printed KeyError there....
#Here it's different. It's so FUCKING CONFUSING AND EASY TO GET LOST HERE....


#W12 D4 T6

# import sys

# print(sys.modules) #dict
# print(sys.path) #list
# print(sys.version) #str
# print(sys.platform) #literal string


#W12 D4 T7

# ', '.join(['a', 'b', 'c'])      # 'a, b, c' — separator is the string, not argument
# 'hello'.startswith('he')        # True
# 'hello'.endswith('lo')          # True
# 'hello'.startswith(('he', 'wo'))  # True — accepts tuple of prefixes!


# words = ['Python', 'is', 'great']
# print(' '.join(words)) #Python is great
# print('-'.join(words)) #Python-is-great
# print(''.join(words)) #Pythonisgreat
# print(', '.join(str(i) for i in range(5))) #0, 1, 2, 3, 4

# s = "hello.py"
# print(s.startswith('hello')) #True
# print(s.endswith('.py')) #True
# print(s.endswith(('.py', '.txt', '.csv')))  #True
# print(s.startswith(('foo', 'bar', 'hello'))) #True

# files = ['data.csv', 'model.py', 'notes.txt', 'train.py']
# py_files = [f for f in files if f.endswith('.py')]
# print(py_files) #['model.py', 'train.py']
# print(', '.join(py_files)) #'model.py, train.py'

#W12 D5 T1
'''str comparisons review

Comparison is character by character using Unicode ordinal (ord()) values.
First differing character determines the result.
If one string runs out of characters first → shorter string is "less than".

'A'–'Z' = 65–90     (uppercase)
'a'–'z' = 97–122    (lowercase)
'0'–'9' = 48–57     (digits)

D < U < L

Rules:
  digits < uppercase < lowercase
  'A' < 'B' < ... < 'Z' < ... < 'a' < 'b' < ... < 'z'
  'a' > 'A'   (97 > 65)
  '9' < 'A'   (57 < 65)
  
Examples:

'abc' vs 'abd'
  'a'=='a' → tie, next
  'b'=='b' → tie, next
  'c' < 'd' → 'abc' < 'abd'

'aa' vs 'aaa'
  'a'=='a' → tie, next
  'a'=='a' → tie, next
  left runs out → 'aa' < 'aaa'
'''

# print('abc' < 'abd')        # True
# print('aa' < 'aaa')         #  True
# print('aa' > 'aaa')         # False
# print('abc' == 'abc')       # True
# print('A' < 'a')            # True
# print('Z' < 'a')            # True
# print('9' < 'A')            # True
# print('banana' > 'apple')   # True
# print('Python' > 'python')  # False

# 'z', 'A', '9', 'aa', 'aA', 'AA', 'Aa'

# #from lowest to highest:

# '9', 'A', 'AA', 'Aa', 'aA', 'aa', 'z'
# x = ['z', 'A', '9', 'aa', 'aA', 'AA', 'Aa']
# print(sorted(x))


# words = ['banana', 'Apple', 'cherry', 'apple', 'Banana']
# print(sorted(words))   #'Apple', 'Banana', 'apple', 'banana', 'cherry'


#W12 D5 T2

# def f():
#     try:
#         int("abc")
#     except ValueError as original: #cause
#         raise TypeError("bad type") from original #raised

# try:
#     f()
# except TypeError as e:
#     print(type(e).__name__)            # TypeError
#     print(type(e.__cause__).__name__)  # ValueError
#     print(str(e))                      # bad type
#     print(str(e.__cause__))            # Value Error's message

# try:
#     try:
#         1/0
#     except ZeroDivisionError: #triggered
#         raise RuntimeError("failed")   #causes this
# except RuntimeError as e: #triggered
#     print(type(e).__name__) #RuntimeError
#     print(e.__cause__)       #None
#     print(e.__context__)     #division by zero - this is weird though - i hope there will be no such examples

#W12 D5 T3 - outer except vs finally order trap

# finally belongs to the function it's WRITTEN IN.
# It runs before control leaves that function — whether via return, raise, or fall-through.
# The outer caller only gets control AFTER the inner function is done (including its finally).

# def inner():
#     try:
#         raise IndexError #1. raised
#     except ValueError:
#         print("inner except")
#     finally:
#         print("inner finally") #2. printed, as we're going out of the inner function now, as the inexerror is not handled here

# try:
#     inner() 
# except IndexError: #raised
#     print("outer except") #printed
    
#inner finally
#outer except


# def process():
#     try:
#         return "ok" #1. returned
#     finally:
#         print("process finally") #2. still printed


# result = process() #process finally - it prints first
# print(result) #ok


# def compute():
#     try:
#         return "try result"
#     finally:
#         return "finally result"   

# print(compute()) #finally result


# def a():
#     try:
#         raise RuntimeError #1. raised and propagated outside
#     finally:
#         print("a-finally") #2 printed first, as we're leaving A

# def b():
#     try:
#         a() 
#     except RuntimeError: #3. raised, as we're handling the RuntimeError from a() which propagates to the outside
#         print("b-except") #4. printed
#     finally:
#         print("b-finally") #5. printed

# b()


#W12 D5 T4 - ABCD


'''
**Q1.** `type(e)` when catching `FileNotFoundError` with `except OSError` returns:
- A: `OSError`
- B: `FileNotFoundError`
- C: `Exception`
- D: Depends on how it was raised

B


**Q2.** `'hello'[1:4:2]` evaluates to:
- A: `'ell'`
- B: `'el'`
- C: `'eo'`  ← careful
- D: `'hlo'`

B

**Q3.** Which is True about `__bases__`?
- A: Contains the full MRO chain
- B: Contains only direct parent classes
- C: Is a list, not a tuple
- D: Always contains `object` as the first element

B

**Q4.** `'banana'.rindex('a')` returns:
- A: `1`
- B: `3`
- C: `5`
- D: `-1`

C


**Q5.** What does `sys.exit(1)` raise?
- A: `RuntimeError`
- B: `SystemExit`
- C: `ExitError`
- D: Nothing — it silently exits

B


**Q6.** `isinstance(True, int)` is:
- A: `False` — bool is not int
- B: `True` — bool is a subclass of int
- C: `TypeError`
- D: Depends on Python version

B

**Q7.** `os.path.split('/foo/bar.txt')` returns:
- A: `['/foo', 'bar.txt']`
- B: `('/foo', 'bar.txt')`
- C: `('/foo/bar', '.txt')`
- D: `('/foo/bar.txt', '')`

B

**Q8.** `lambda: 42` is:
- A: SyntaxError — lambda needs parameters
- B: Valid — returns 42 when called
- C: Valid — but always returns None
- D: Valid — but cannot be assigned to a variable

B

**Q9.** After `raise ValueError("x") from KeyError("y")`, caught as `e`:
- `type(e).__name__` is `'ValueError'` — True or False?
- `e.__cause__` is `None` — True or False?
- `type(e.__cause__).__name__` is `'KeyError'` — True or False?

True, False, True

**Q10.** `'aa' > 'aaa'` is:
- A: `True`
- B: `False`
- C: `TypeError`
- D: Depends on locale

B

**Q11.** `[x for x in range(5, 0, -1) if x % 2 == 0]` gives:
- A: `[2, 4]`
- B: `[4, 2]`
- C: `[2, 4, 0]`
- D: `[]`

B

**Q12.** `hasattr(Child, 'method')` where `method` is only defined in `Parent(Child inherits from)`:
- A: `False` — not defined in Child
- B: `True` — inherited
- C: `AttributeError`
- D: Depends on the method type

A


**Q13.** `b"hello"[0]` returns:
- A: `'h'`
- B: `104` (int)
- C: `b'h'`
- D: `TypeError`

B

**Q14.** Default mode of `open('file.txt')`:
- A: `'w'`
- B: `'a'`
- C: `'r'`
- D: `'x'`

C


**Q15.** Which correctly imports platform and gets the OS name string only (e.g., `'Windows'`):
- A: `platform.platform()`
- B: `platform.uname()`
- C: `platform.system()`
- D: `platform.os()`

C


**Q16.** Name mangling: `class Foo` with `__x = 1` — the attribute is stored as:
- A: `__x`
- B: `_x`
- C: `_Foo__x`
- D: `Foo__x`

C

**Q17.** `nonlocal x` inside a nested function:
- A: Makes `x` global
- B: Allows writing to the enclosing (non-global) scope's `x`
- C: Creates a new local `x`
- D: Is only valid if `x` is a list or dict

B

**Q18.** A generator function with `yield` — when is its body first executed?
- A: When the function is defined
- B: When the function is called (returns generator object)
- C: When `next()` is first called on the returned generator
- D: When the generator is assigned to a variable

C

**Q19.** `os.name` on Windows returns:
- A: `'windows'`
- B: `'win32'`
- C: `'nt'`
- D: `'Windows'`

C

**Q20.** `'Python'[0] > 'python'[0]` is:
- A: `True`
- B: `False`  ← 'P'=80, 'p'=112
- C: `TypeError`
- D: Depends on encoding

B

'''
#W12 D5 T5 - string comparisons

# print('abc' < 'b')         # True
# print('ABC' < 'abc')       # True
# print('abc' < 'abcd')      # True
# print('abcd' < 'abce')     # True
# print('1python' < 'Python') # True
# print('' < 'a')            # True


# items = ['cherry', 'Apple', 'banana', 'CHERRY', '1apple']
# print(sorted(items)) # ['1apple', 'Apple', 'CHERRY', 'banana', 'cherry']

# print(min('a', 'A', '1', 'z')) #1
# print(max('a', 'A', '1', 'z')) #z


#W12 D5 T7 

# class MyError(Exception):
#     def __init__(self, msg):
#         self.msg = msg          # no super().__init__()
#     def __str__(self):
#         return f"MyError: {self.msg}"

# try:
#     raise MyError("oops")
# except MyError as e:
#     print(e) #MyError: oops
#     print(e.args) #('oops',)
    


# class A:
#     __v = 10
#     def get(self): return self.__v

# class B(A):
#     __v = 20
#     def get(self): return self.__v

# class C(B):
#     __v = 30

# obj_c = C()
# print(obj_c.get()) #20


# def gen():
#     yield 1
#     yield 2
#     return
#     yield 3

# print(list(gen())) #[1, 2]

# m = 0
# def foo(n):
#     global m
#     assert n > 0 #1. AssertionError, unhandled in foo, propagates to the outside
#     try:
#         return 10 / n
#     except ArithmeticError:
#         raise RuntimeError

# try:
#     foo(0) 
# except RuntimeError:
#     m = 10
# except AssertionError: #2. Handled here
#     m = 5 #sets the value to 5
# except:
#     m = 1
    
    
# print(m) #5


# class Parent:
#     def __init__(self):
#         self.__x = 10

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__x = 99

#     def show(self):
#         print(self._Parent__x)
#         print(self._Child__x)

# Child().show() #10, 99

# import sys
# print(sys.modules)


# def risky():
#     raise ValueError("inner")

# try:
#     risky()
# except ValueError as e:
#     raise RuntimeError("outer") from e
#

#W13 D1 T1 - custom __str__ on exceptions, predicting outputs

'''
print(e)  →  calls e.__str__()
str(e)    →  calls e.__str__()
repr(e)   →  calls e.__repr__() — default is ClassName(args)
e.args    →  tuple from super().__init__() — unaffected by __str__
'''


# class AppError(Exception):
#     def __init__(self, code, msg):
#         super().__init__(msg)
#         self.code = code

#     def __str__(self):
#         return f"[{self.code}] error occurred"

# try:
#     raise AppError(404, "not found")
# except AppError as e:
#     print(e)              #[404] error occurred
#     print(str(e))         #[404] error occurred
#     print(repr(e))        #code: 404
#     print(e.args)         #code: 404
#     print(e.code)         # 404
    
    

# class AppError(Exception):
#     def __init__(self, code, msg):
#         super().__init__(msg)
#         self.code = code

# try:
#     raise AppError(404, "not found")
# except AppError as e:
#     print(e)              #'not found'
#     print(e.args)         #('not found', ) #THIS FEELS STILL SUPER FUCKING DIFFICULT...


#W13 D1 T2
'''
Mode   | Creates? | Truncates? | Pointer start | Read? | Write?
'r'    | No (fail)| No         | Beginning     | Yes   | No
'w'    | Yes      | Yes        | Beginning     | No    | Yes
'a'    | Yes      | No         | END           | No    | Yes
'x'    | No(fail) | No         | Beginning     | No    | Yes  ← exclusive create
'r+'   | No (fail)| No         | Beginning     | Yes   | Yes  ← read+write, no truncate
'w+'   | Yes      | Yes        | Beginning     | Yes   | Yes  ← truncates!
'a+'   | Yes      | No         | END (writes)  | Yes   | Yes  ← writes always at end
'''

# 1. open('f', 'r+') truncates the file - NO
# 2. open('f', 'w+') truncates the file - Yes
# 3. open('f', 'a+') allows reading # Yes
# 4. open('f', 'a') allows reading #No
# 5. open('f', 'r+') raises an error if the file doesn't exist #Yes
# 6. open('f', 'x') raises FileExistsError if file already exists #Yes
# 7. open('f', 'a') always writes at the end, regardless of seek() #Yes
# 8. open('f') is the same as open('f', 'r') #Yes


# 1. Read + write, no truncate, pointer at start, file must exist  → r+
# 2. Write only, always appends, creates if missing                → a
# 3. Read + write, truncates first, creates if missing             → w+
# 4. Exclusive create, fails if exists                             → x
# 5. Read + write + append, writes always go to end               → a+



#W13 D1 T3 - random module

'''import random
random.seed(n)          # set seed → reproducible sequence
random.random()         # float in [0.0, 1.0)  — NEVER >= 1
random.randint(a, b)    # int in [a, b] inclusive — CAN return b
random.choice(seq)      # random element from non-empty sequence
random.sample(seq, k)   # k unique elements from seq, returns list
random.shuffle(lst)     # shuffles list IN PLACE, returns None

random.seed(1); v1 = random.random()
random.seed(1); v2 = random.random()
v1 == v2   # True — same seed → same sequence

random.random() >= 1   # ALWAYS False — range is [0.0, 1.0)
random.choice([1,2,3]) >= 1  # ALWAYS True — min value is 1
len(random.sample([1,2,3], 2)) > 2  # ALWAYS False — len==2
'''

# import random
# random.seed(99)
# a = random.random()
# random.seed(99)
# b = random.random()

# print(a == b)                           #True
# print(a < 1)                            #False
# print(a >= 0)                           #True
# print(random.choice([5, 10, 15]) >= 5) #True
# print(len(random.sample([1,2,3], 2)) == 3)  #False


#W13 D1 T4 - PCAP simulation - in tasks.md

# y = lambda x: None
# print(y(1))

#W13 D1 T5

# class Engine:
#     horsepower = 200
#     def start(self): pass

# class Car(Engine):
#     def __init__(self, brand):
#         self.brand = brand
#     def drive(self): pass

# c = Car('Toyota')


# print(hasattr(c, 'horsepower'))          #True
# print(hasattr(c, 'start'))               #True
# print(hasattr(Car, 'start'))            #True
# print('start' in Car.__dict__)           #False
# print('start' in Engine.__dict__)        #True
# print('horsepower' in Car.__dict__)      #False
# print('brand' in Car.__dict__)          #False
# print('brand' in c.__dict__)           #True
# print('drive' in Car.__dict__)          #True

# > `hasattr(X, 'name')` returns True if `'name'` exists anywhere in the mro
# > `'name' in X.__dict__` returns True only if `'name'` is defined in a given Class instance

#CD Python tasks - Pandas basics - I didn't paste all of the tasks here, as they're rather similar, but I've pasted some of them to show examples
#I'll most likely return to pasting all of the tasks here once we start doing more complex Pandas tasks

# import pandas as pd
# from collections import Counter

# url = "https://drive.google.com/uc?id=1zHvNI4WpLlRm-rvBZxKKUlYls_UuGHFv"
# df = pd.read_csv(url)

# pd.set_option('display.max_rows', 20)
# pd.set_option('display.max_columns', None)
# print(df.describe())
# s = df['price']
# print(type(s))
# mini_df=df[['price', 'area', 'rooms_no']]
# print(mini_df)

# offer_build_type = df['build_type'].iloc[-7]
# print(offer_build_type)


# c = Counter(df['market_type'])
# print(c)
# top_market_type = 'secondary'

# import pandas as pd
# url = "https://drive.google.com/uc?id=10YhzOgkUaOvhAXZIEzRdakgU6uSfKbhR"
# df = pd.read_excel(url, sheet_name='2021') #tu bardzo ważne to sheet_name!!
# print(df.head)

# rows = df.shape[0]
# print(rows)

#W13 D2 T1

'''
e.args     → a TUPLE. Set by Exception.__init__() via super().__init__(*stuff).
             Whatever you pass to super().__init__() becomes e.args.
             If you don't call super().__init__(), e.args = ().

str(e)     → calls __str__. If you defined __str__, that runs.
print(e)   → same as str(e).
             If NO __str__ defined, Python falls back to str(e.args[0]) if len==1,
             or str(e.args) if multiple.

repr(e)    → calls __repr__. Default is: ClassName(arg1, arg2, ...)
             where the args come from e.args — NOT from __str__.
             __str__ has ZERO effect on repr().
'''

# e.args = ('not found',)
# repr(e) → "AppError('not found')"
#            ^^^^^^^^  ^^^^^^^^^^^
#            class     e.args unpacked

# e.args = ('not found', 404)
# repr(e) → "AppError('not found', 404)"

# e.args = ()   (no super().__init__() called)
# repr(e) → "AppError()"


# class E1(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)   # msg goes into e.args

# e = E1("something broke")
# print(str(e))     # 'something broke'   ← e.args[0] since len==1
# print(repr(e))    # "E1('something broke')"
# print(e.args)     # ('something broke',)


# class E2(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)
#     def __str__(self):
#         return "CUSTOM MESSAGE"

# e = E2("something broke")
# print(str(e))     # 'CUSTOM MESSAGE'        ← __str__ wins
# print(repr(e))    # "E2('something broke')" ← __str__ has NO effect on repr
# print(e.args)     # ('something broke',)    ← unaffected by __str__


# class E3(Exception):
#     def __init__(self, code, msg):
#         super().__init__(code, msg)   # BOTH go into e.args

# e = E3(404, "not found")
# print(str(e))     # '(404, \'not found\')'  ← multiple args: str(e.args)
# print(repr(e))    # "E3(404, 'not found')"  ← both args in repr
# print(e.args)     # (404, 'not found')


# class E4(Exception):
#     def __init__(self, code, msg):
#         super().__init__(msg)   # only msg goes to super → e.args = (msg,)
#         self.code = code        # code is just an instance attr, NOT in e.args

# e = E4(404, "not found")
# print(str(e))     # 'not found'           ← e.args[0]
# print(repr(e))    # "E4('not found')"     ← only msg in args
# print(e.args)     # ('not found',)        ← code NOT here
# print(e.code)     # 404                   ← separate instance attr


# class E5(Exception):
#     def __init__(self, msg):
#         self.msg = msg          # super() NOT called → e.args = ()

# e = E5("something broke")
# print(str(e))     # ''                    ← empty args → empty str
# print(repr(e))    # "E5()"               ← empty args
# print(e.args)     # ()
# print(e.msg)      # 'something broke'    ← only reachable as e.msg



# class PriceError(Exception):
#     def __init__(self, price, reason):
#         super().__init__(reason)    # only reason goes to super
#         self.price = price
#     def __str__(self):
#         return f"Bad price {self.price}: {self.args[0]}"

# e = PriceError(-5, "negative")
# print(str(e)) #Bad price -5: negative
# print(repr(e)) #PriceError('negative')
# print(e.args) #('negative',)
# print(e.price) #-5


# class ConnError(Exception):
#     def __init__(self, host, port, msg):
#         super().__init__(host, port, msg)   # all three to super

# e = ConnError("localhost", 5432, "timeout")
# print(str(e)) #('localhost', 5432, 'timeout)
# print(repr(e)) #ConnError('localhost', 5432, 'timeout)
# print(e.args) #('localhost', 5432, 'timeout)
# print(len(e.args)) #3

# class SimpleError(Exception): #this example is very unintuitive still
#     pass   # no __init__, no __str__

# e = SimpleError("oops")
# print(str(e)) #oops
# print(repr(e)) #SimpleError('oops')
# print(e.args) #('oops',)

# class E(Exception):
#     def __str__(self):
#         return 'hi'

# e = E('ignored')

# print(repr(e))
# print(e.args)
# print(str(e))


#W13 D2 T2

# s = "abracadabra"
# print(s.find('a'))      #0
# print(s.rfind('a'))     #10
# print(s.index('a'))     #0
# print(s.rindex('a'))    #10
# print(s.find('z'))      #-1
# print(s.rfind('z'))     #-1
# print(s.index('z'))     #valueError
# print(s.rindex('z'))    #valueError



#W13 D2 T3

# class X:
#     __val = 'x'
#     def show(self): return self.__val

# class Y(X):
#     __val = 'y'
#     def show(self): return self.__val

# class Z(Y):
#     __val = 'z'

# obj = Z()
# print(obj.show())   #y
# print(obj._Z__val) #'z'
# print(obj._Y__val) #'y'
# print(obj._X__val) #'x'


# print(hasattr(Z, 'show'))       #True
# print('show' in Z.__dict__)     #False
# print('show' in Y.__dict__)     #True
# print(Z.__bases__ == (Y,))      #True
# print(Y in Z.__mro__)           #True

#W13 D2 T4

# result = 0
# def compute(n):
#     assert n > 0 #1.This assertion fails inside -> raises AssertionError
#     try:
#         return 100 / n
#     except ZeroDivisionError:
#         raise RuntimeError("div fail")

# try:
#     compute(0) # 2. The error is unhandled inside the compute function, so it propagates to the outside
# except RuntimeError:
#     result = 1
# except AssertionError: # 3. This handle handles the AssertionError
#     result = 2
# except:
#     result = 3
# print(result) #2


# result = 0
# def compute(n):
#     assert n > 0
#     try:
#         return 100 / n
#     except ZeroDivisionError:
#         raise RuntimeError("div fail")

# try:
#     compute(-1) #basically the same as above
# except RuntimeError:
#     result = 1
# except AssertionError:
#     result = 2
# except:
#     result = 3
# print(result) #2



# result = 0
# def compute(n):
#     assert n > 0 #1. this time the assertion is correct
#     try:
#         return 100 / n #This works properly, returning the result (20)
#     except ZeroDivisionError:
#         raise RuntimeError("div fail")

# try:
#     compute(5) 
# except RuntimeError:
#     result = 1
# except AssertionError:
#     result = 2
# except:
#     result = 3
# print(result) #0, the result is not updated with the result of compute() function


#W13 D2 T5

# print('abc' > 'ABC')          # True
# print('abc' == 'ABC'.lower()) # True
# print('Z' > 'a')              # False
# print('' < 'a')               # True
# print('aa' == 'aa ')          # False
# print('1abc' < 'abc')         # True


# lst = [i for i in range(6)]
# result = [lst[i] for i in range(5, -1, -1) if lst[i] % 2 == 0]
# print(result) #[4, 2, 0]

#[lst[5] if lst[5] % 2 == 0] -> X (5 not divided by 2 without extra 1)
#[lst[4] if lst[4] % 2 == 0] -> 4 
#-> etc... 2, 0

# result = [x ** 2 for x in range(4, 0, -1) if x % 2 != 0]
# print(result) #[9, 1]

#W13 D2 T6 - PCAP select two simulation

'''**Q1.** Which expressions always evaluate to True? (Select two)
```python
import random
random.seed(5)
v = random.random()
```
- A: `v >= 1`
- B: `v < 1`
- C: `v >= 0`
- D: `v == 1`

B, C

**Q2.** Which of the following are true about exception classes? (Select two)
```python
class AppError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    def __str__(self):
        return "app error"

e = AppError("details")
```
- A: `str(e) == "app error"`
- B: `e.args == ()`
- C: `repr(e) == "app error"`
- D: `e.args == ("details",)`

A, D

**Q3.** Which expressions evaluate to True? (Select two)
```python
class A: pass
class B(A): pass
class C(B): pass
```
- A: `B in C.__bases__`
- B: `A in C.__bases__`
- C: `A in C.__mro__`
- D: `object in C.__bases__`

A, C

**Q4.** Which are valid Python? (Select two)
- A: `lambda: 42`
- B: `lambda x: return x`
- C: `lambda x, y=0: x + y`
- D: `lambda x: x if x > 0 else -x`

A, D

**Q5.** What is true about the following code? (Select two)
```python
class P:
    __x = 1
    def get(self): return self.__x

class Q(P):
    __x = 2

obj = Q()
```
- A: `obj.get() == 1`
- B: `obj.get() == 2`
- C: `obj._P__x == 1`
- D: `obj._Q__x == 1`

A, C
'''


#W13 D2 T7

# try:
#     {}['missing']
# except Exception as e:
#     print(type(e).__name__)           # KeyError
#     print(isinstance(e, KeyError))    # True
#     print(isinstance(e, Exception))   # True
#     print(type(e) is Exception)       # False
#     print(type(e) is KeyError)        # True


#Crappy Data Python tasks

'''
Jaki jest 99-ty percentyl wartości w kolumnie score?

Użyj notebooka, żeby znaleźć odpowiedź na powyższe pytanie
i przypisz ręcznie wartość z dokładnością 2 cyfry po przecinku do zmiennej score_99.
'''

# import pandas as pd
# import random

# random.seed(42)
# names = ["Anna", "Piotr", "Kasia", "Tomasz", "Marta", "Jan", "Ola", "Michał"]
# countries = ["PL", "UK", "US", "DE"]
# data = []
# for i in range(20):
#     row = {
#         "user_id": i + 1,
#         "name": random.choice(names),
#         "age": random.randint(18, 60),
#         "country": random.choice(countries),
#         "score": round(random.uniform(0, 100), 2)
#     }
#     data.append(row)
# df = pd.DataFrame(data)
# x = df.describe(percentiles = [0.99])
# print(x)
# score_99 = 84.41



#Crappy Data Python tasks 
'''
Która z kolumn dataframe df zdaje się mieć podejrzane dane?

Użyj notebooka, żeby znaleźć odpowiedź na powyższe pytanie
i przypisz ręcznie nazwę kolumny do zmiennej suspicious_column.
'''

# import pandas as pd
# url = "https://drive.google.com/uc?id=11mTxuLJGLDAbqS71P90hwAgWgZuqozWY"
# df = pd.read_csv(url)
# pd.set_option('display.max_columns', None)
# print(df.shape)
# print(df.dtypes) 
# print(df.head(5))
# print(df.tail(5))
# print(df.describe(percentiles = [0.05, 0.1, 0.25, 0.50, 0.75, 0.9, 0.95, 0.99]))
# print(df.describe(include = 'all'))

# suspicious_column = "heating"



'''
Uporządkuj nazwy kolumn w dataframe df:

zamień wszystkie litery na małe
zamień spacje na _
usuń znaki specjalne (znaki interpunkcyjne, nawiasy itd.)
Na końcu przypisz zmienione nazwy z powrotem do dataframe df, możesz skorzystać z poniższego schematu:

df.columns = ["col1", "col2", "col3"]
'''

# import pandas as pd
# import random

# random.seed(42)
# data = {
#     "User ID": [i for i in range(1, 11)],
#     "First Name": [random.choice(["Anna", "Piotr", "Kasia", "Jan"]) for _ in range(10)],
#     "Last Name!": [random.choice(["Nowak", "Kowalski", "Wiśniewski"]) for _ in range(10)],
#     "Age (Years)": [random.randint(18, 60) for _ in range(10)],
#     "Country-Code": [random.choice(["PL", "UK", "US"]) for _ in range(10)],
#     "Score 2023": [round(random.uniform(0, 100), 2) for _ in range(10)],
#     "Score 2024!": [round(random.uniform(0, 100), 2) for _ in range(10)],
#     "E-mail Address": [f"user{i}@mail.com" for i in range(10)]
# }
# df = pd.DataFrame(data)

# new_names = []
# to_delete = ["-", "!", "(", ")"]
# for col in df.columns:
#     col = [char for char in col if char not in to_delete]
#     col = ''.join(col)
#     new_col = col.lower()
#     new_col = new_col.replace(' ', '_')
#     new_names.append(new_col)
# df.columns = new_names
# print(df.columns)



# string = 'PYTHON'[:3:]
# string = string[-1] + string[-2::-1] #T + YP
# print(string) #TYP

# print(len(""""""))
# print('1' + '2')

# print('a' * 3 > 'a' * 2)
# print('ABC'.lower() > 'ABC')


# the_string = ',,'.join(('left', 'right')) #left,,right
# the_list = the_string.split(',') #left, ' ', right
# print(len(the_list)) #3

#W13 D3 T2

# import sys
# print(sys.path) #LIST
# print(sys.modules) #DICT
# print(sys.argv)

# print(type(sys.path) is list) #True
# print(type(sys.modules) is dict) #True
# print(isinstance(sys.path, list)) #True
# print(type(sys.argv) is list) #True
# print(type(sys.argv[0]) is str) #True

# #Given: script run as `python myscript.py alpha 42`

# import sys
# print(sys.argv[0])         #myscript.py -> here it's practice.py as I run it in here
# print(sys.argv[1])         #alpha # here it would be IndexError, same below
# print(sys.argv[2])         #42
# print(type(sys.argv[2]))   #str
# print(len(sys.argv))       #3

# import sys
# # 'sys' is already imported
# print('sys' in sys.modules)          #True
# print('os' in sys.modules)           #False
# import os
# print('os' in sys.modules)           #True


#W13 D3 T3

'''
Default __str__(obj)   → '<ClassName object at 0x7f...>'  (NOT the var name, NOT class name alone)
Default __repr__(obj)  → same as __str__ if __repr__ not defined
str(obj) == 'obj'      → ALWAYS False (default repr is memory address, not variable name)

When __str__ IS defined: str(obj) calls it, repr(obj) does NOT use it (uses __repr__).
'''

# class Box:
#     pass

# b = Box()
# print(str(b) == 'b')                  #False
# print(str(b) == 'Box')                #False
# print('Box' in str(b))                #True <Box object at ....>
# print('object' in str(b))             #True
# print(str(b) == repr(b))              #True


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"Animal({self.name})"

# a = Animal("cat")
# print(str(a))          #Animal(cat)
# print(repr(a))         #<main.Animal object at ...>
# print(str(a) == repr(a))  #False


#W13 D3 T4

'''
lambda           → valid, zero params: lambda: 42
lambda x:        → must have body: lambda x: x
lambda x, y=0:   → default args valid: lambda x, y=0: x + y
lambda *args:    → *args valid: lambda *args: sum(args)
return keyword   → FORBIDDEN inside lambda body (SyntaxError)
lambda CAN return None → lambda: None is perfectly valid
'''

# f1 = lambda: 42 #Valid
# f2 = lambda x: return x #Invalid
# f3 = lambda x, y=0: x + y #Valid
# f4 = lambda x: x if x > 0 else -x #Valid
# f5 = lambda x, y: x * y #Valid
# f6 = lambda: None #Valid
# f7 = lambda x: print(x) #valid


# f = lambda: None
# print(f() is None)    #True
# print(f() == None)    #True
# print(bool(f()))      #False


#W13 D3 T5 - I/O modes

# 1. Read-only, file must exist, pointer at start:              r
# 2. Read+write, no truncate, file must exist, pointer at start:  r+
# 3. Creates/truncates, write-only:                              w
# 4. Creates/truncates, read+write:                              w+
# 5. Appends only, creates if missing:                          a
# 6. Read+write appends, creates if missing:                    a+
# 7. Exclusive create, fails if file exists:                    x


# Assume 'data.txt' already exists with content "hello"
# f = open('data.txt', 'r+')
# # Which statements are True?
# ```
# - A: `f.read()` works → True
# - B: `f.write('x')` works → True
# - C: `f.write('x')` truncates the file first → False
# - D: The pointer starts at the beginning → True
# - E: If file doesn't exist, `FileNotFoundError` is raised → True


#W13 D3 T6 

# class P:
#     speed = 100
#     def move(self): pass

# class Q(P):
#     def stop(self): pass

# class R(Q):
#     pass

# r = R()

# print(hasattr(r, 'speed')) #True, full MRO check
# print(hasattr(r, 'move'))#True, full MRO check - methods also pertrain to this

# s = '--'.join(('a', 'b', 'c'))
# parts = s.split('-')
# print(parts)
# print(len(parts))


#W13 D4 T1

# f1 = lambda x: x * 2 #valid
#f2 = lambda x: if x > 0: x else -x #SyntaxError
# f3 = lambda x: x if x > 0 else -x #VALID
#f4 = lambda x: [i for i in range(x)] #valid
# f5 = lambda x: for i in range(x): print(i) #syntaxerr
# f6 = lambda x: (x, x * 2) #VALID
# f7 = lambda x: return x + 1 #SyntaxErorr
# f8 = lambda x: assert x > 0 #SyntaxErorr
# f9 = lambda x: print(x) or x #Valid
# f10 = lambda x, y=[], z=0: x + z #Valid


# ops = {
#     'add': lambda x, y: x + y,
#     'sub': lambda x, y: x - y,
#     'mul': lambda x, y: x * y,
# }
# print(ops['add'](3, 4)) #7
# print(ops['mul'](ops['sub'](10, 4), 2)) #12



#W13 D4 T2

# def outer():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#     increment()
#     increment()
#     increment()
#     return count

# print(outer()) #3


# def make_counter():
#     n = 0
#     def up():   nonlocal n; n += 1
#     def down(): nonlocal n; n -= 1
#     def get():  return n
#     return up, down, get 

# up, down, get = make_counter()
# up(); up(); up() #1, 2, 3
# down() #2
# print(get()) #2


# x = 10
# def outer():
#     x = 20
#     def inner():
#         x = 30
#         print(x) 
#     inner() #30
#     print(x) #20
# outer() #30, 20
# print(x) #10

#W13 D4 T3 - inner/outer exception chains output tracing

# try:
#     try:
#         x = 1 / 0 #1. zDiv Error
#     except ZeroDivisionError: #2. Handled here 
#         print('inner caught') #2. Prints
#         raise ValueError('from inner') #3. This is raised
#     print('after inner try') #4. This is printed, as we propagate to the outside try/except block
# except ValueError:
#     print('outer caught ValueError') #5. this handle causes the ValueError raised in the inner block - outer caught ValueError prints
# except ZeroDivisionError:
#     print('outer caught ZeroDivision')
# print('end') #6. This prints

#print wise:
#1. inner caught
#2. after inner try
#3. outer caught ValueError
#4. end



# def f():
#     try:
#         return 'try' 
#     finally:
#         return 'finally'

# def g():
#     try:
#         raise RuntimeError('boom') #2. this is called and propagated to the outside
#     finally:
#         print('finally runs') #3. this is printed BEFORE we handle the Runtime error outside

# print(f()) #1. finally prints
# try:
#     g()
# except RuntimeError:
#     print('caught runtime') #4. this is printed.
    
#1. finally
#2. finally runs
#3. caught runtime


# try:
#     try:
#         raise TypeError('t') #1. This is raised, no handle so it's propagated to the outside
#     except ValueError:
#         print('inner ValueError')
#     else:
#         print('inner else')
#     finally:
#         print('inner finally') #2. This prints, as w're leaving the inner block
# except TypeError: #3. This block handles the TypeError from the inner try/except
#     print('outer TypeError') #3. This prints
# finally:
#     print('outer finally') #4. This prints
    
#1. inner finally
#2. outer TypeError
#3. outer finally


# def risky(n):
#     try:
#         result = 10 / n
#     except ZeroDivisionError:
#         print('zero!')
#         result = 0
#     except (TypeError, ValueError) as e:
#         print(f'bad input: {type(e).__name__}')
#         result = -1
#     else:
#         print(f'ok: {result}') 
#     finally:
#         print('done')
#     return result

# print(risky(2)) #ok: 5.0 -> done -> 5.0
# print(risky(0)) #zero! -> done -> 0
# print(risky('x')) #bad input: TypeError -> done -> -1


#W13 D4 T4 - str vs repr traps

'''
str(obj)   → __str__ if defined, else falls back to __repr__
repr(obj)  → __repr__ if defined, else '<ClassName object at 0x...>'
print(obj) → calls str(obj)

If ONLY __repr__ defined:
  str(obj)  → uses __repr__  ← TRAP
  repr(obj) → uses __repr__

If ONLY __str__ defined:
  str(obj)  → uses __str__
  repr(obj) → default '<ClassName object at 0x...>'

Exception repr(e) → always "ClassName(arg1, arg2)" — uses e.args, ignores __str__
'''


# class Token:
#     def __init__(self, val):
#         self.val = val
#     def __repr__(self):
#         return f"Token({self.val!r})"

# t = Token("hello")
# print(str(t)) #Token(hello)
# print(repr(t)) #Token(hello)
# print(str(t) == repr(t)) #True


# class Tag:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"<{self.name}>"

# g = Tag("div") 
# print(str(g)) #<div>
# print(repr(g)) #<__main__.Tag object at XXXX...>
# print(str(g) == repr(g)) #False

#Czyli jak mamy str zdefiniowane, to repr go nie używa
#W odwrotną stronę, jak mamy repr zdefiniowane a nie mamy repr, to str printuje repr



# class A:
#     def __init__(self):
#         self.x = 1

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.x = 2

# class C(B):
#     pass

# obj = C()
# print(obj.x) #2

# try:
#     try:
#         raise ValueError('bad')
#     except ValueError as e:
#         raise TypeError('worse')
#     except TypeError:
#         print('caught type error') #THIS ERROR REMAINS UNHANDLED HERE - EACH LEVEL CAN HANDLE 1 ERROR ONLY!
# except TypeError:
#     print('caught the type error in the outer block') #It only gets handled here


# class Counter:
#     _count = 0
#     def __init__(self):
#         Counter._count += 1
#     @classmethod
#     def get_count(cls):
#         return cls._count

# a = Counter()
# b = Counter()
# c = Counter()
# print(Counter.get_count())

# x = [1, 2, 3]
# y = x
# y += [4]
# print(x) #[1, 2, 3, 4]
# print(y is x) #True

# class Base:
#     __secret = 42
#     def reveal(self):
#         return self.__secret

# class Child(Base):
#     __secret = 99

# obj = Child()
# print(obj.reveal()) #42


# class Animal:
#     sound = 'generic'
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f'{self.name} says {self.sound}'

# class Dog(Animal):
#     sound = 'woof'

# class Cat(Animal):
#     def speak(self):
#         return f'{self.name} meows'

# animals = [Dog('Rex'), Cat('Mimi'), Animal('Thing')]
# for a in animals:
#     print(a.speak()) #Rex says woof, 'Mimi meows, 'Thing says generic


# def process(items, fn=lambda x: x):
#     return [fn(item) for item in items]

# nums = [3, -1, 4, -1, 5]
# print(process(nums)) #[3, -1, 4, -1, 5]
# print(process(nums, abs)) #[3, 1, 4, 1, 5]
# print(process(nums, lambda x: x * 2 if x > 0 else 0)) #[6, 0, 8, 0, 10]


# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# g = countdown(5) 
# print(next(g)) #5
# print(next(g)) #4
# for x in g: 
#     print(x) #3, 2, 1
# print('done') #done

# print('python'.rfind('o'))


#CD Python

'''
Przypisz do zmiennej common_cols nazwy kolumn (w postaci listy lub zbioru), 
które występują zarówno w df1 jak i df2.
'''

# import pandas as pd

# df1 = pd.read_csv("df1.csv")
# df2 = pd.read_csv("df2.csv")
# common_cols = set(df1.columns).intersection(set(df2.columns))

# import pandas as pd

# x = pd.DataFrame()
# x = pd.read_csv()


# import pandas as pd
# from collections import Counter

# url = "https://drive.google.com/uc?id=1zHvNI4WpLlRm-rvBZxKKUlYls_UuGHFv"
# df = pd.read_csv(url)

# pd.set_option('display.max_rows', 20)
# pd.set_option('display.max_columns', None)
# print(df.head(5))

# are_equal_rows = df.shape[0] == len(df)
# print(are_equal_rows)


# s = df[df.columns[0]]
# are_equal_rows = len(df) == len(s)
# print(are_equal_rows)


#CD Python - task 120 


'''
Zadanie
Zmień index dataframe df na wartości kolumny url. 
Nie zachowuj kolumny z pierwotnym indeksem.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")

# df.set_index('url', drop = True, inplace=True)
# print(df)

#CD Python - task 121

'''Stwórz nowe zmienne o typie DataFrame na podstawie df:

df2 - zawiera pierwsze 50 wierszy oraz wszystkie kolumny
df3 - zawiera wszystkie wiersze oraz kolumny: price_per_m, rooms_no
df4 - zawiera wiersze od 4 do 10 oraz kolumny od 6 do 10 (według kolejności występowania)'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df2 = df.iloc[:50]
# df3 = df.loc[:, ['price_per_m', 'rooms_no']]
# df4 = df.iloc[3:10, 5:10]

#CD Python - task 122

'''
Ile ofert ma przynajmniej 3 pokoje (rooms_no)?
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# big_flats = len(df[df['rooms_no'] >= 3])


#CD Python - task 123

'''
Ile procent mieszkań wśród mieszkań z przynajmniej 3 pokojami (rooms_no) ma centralne (urban) ogrzewanie?

Przypisz procent zaokrąglony do 2 miejsc po przecinku do zmiennej urban_perc
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# pd.set_option('display.max_columns', None)
# df.info

# filtered_df = df[df['rooms_no'] >= 3]
# urban_perc = round(len(filtered_df[df['heating'] == 'urban'])/(len(filtered_df)) * 100, 2)
# print(urban_perc)


# x = 'adi'
# x[0] = 'ba'
# print(x)

# import os
# path = 'reports/2024/summary.csv'
# head, tail = os.path.split(path)
# root, ext = os.path.splitext(tail)
# print(root)
# print(ext)

# class Foo:
#     def __init__(self, x):
#         self.x = x

#     def __eq__(self, other):
#         return self.x == other.x

#     def __str__(self):
#         return f'Foo({self.x})'

# a = Foo(3)
# b = Foo(3)
# print(a == b) #True
# print(str(a)) #Foo(3)
# print(a is b) #False

# data = [0, '', None, 1, 'a', [], [0]]
# result = list(filter(bool, data))
# print(len(result)) #3

# class Formatter:
#     def format(self, val):
#         return str(val)

#     def render(self):
#         return f'[{self.format(42)}]'

# class HexFormatter(Formatter):
#     def format(self, val):
#         return hex(val)

# f = HexFormatter()
# print(f.render())

#CD Python - task 124 


'''
Możemy odwoływać się do kolumn w DataFrame nie tylko poprzez df["column_name"] , lecz również używając składni: df.column_name.

Zapis df.column_name jest jednak trochę podchwytliwy, ponieważ może prowadzić do błędów, jeśli:

nazwa kolumny pokrywa się z istniejącą metodą (np. count, mean)
nazwa kolumny zawiera spacje lub znaki specjalne
nazwa kolumny pokrywa się z inną zmienną w kodzie
Przypisz do zmiennej dates daty zamówienia z df w postaci pd.Series.
'''


# import pandas as pd

# data = {
#     "id": [1, 2, 3, 4, 5],
#     "order date": ["2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07", "2024-01-10"],
#     "value": [100, 150, 120, 180, 130]
# }
# df = pd.DataFrame(data)

# values = df.value
# print(values)

# dates = None
# df['order_date'] = df['order date'] #tu w razie co możnaby jeszcze użyć pd.to_datetime
# dates = df.order_date
# print(dates)


#CD Python - task 125

'''
Ile mieszkań w danych df ma taras lub ogród?

Przypisz liczbę mieszkań do zmiennej cosy_flats
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")

# df.describe()
# cosy_flats = len(df[(df['garden'] == True) | (df['terrace'] == True)])
# print(cosy_flats)


#CD Python - task 126

'''
Skonwertuj kolumny w DataFrame df na odpowiednie typy numeryczne i daty. Niepoprawne dane tekstowe zamień na NaN.
'''

# import pandas as pd

# data = {
#     "delivery_date": ["2024-01-10", "2024-02-15", "2024-03-20"],
#     "price": ["100.5", "200", "408"],
#     "discount": ["0.1", "0.25", None],
#     "rating": ["4.5", "3", "not available"]
# }

# df = pd.DataFrame(data)
# print(df.dtypes)
# df['delivery_date'] = pd.to_datetime(df["delivery_date"], errors = 'coerce', format = '%Y-%m-%d')
# df['price'] = pd.to_numeric(df['price'], errors = 'coerce')
# df['discount'] = pd.to_numeric(df['discount'], errors = 'coerce')
# df['rating'] = pd.to_numeric(df['rating'], errors = 'coerce')
# print(df.dtypes)



#CD Python - task 127

'''
Posortuj oferty mieszkań w df na podstawie lokalizacji geograficznej: od zachodu do wschodu i od północy do południa.
'''


#W14 D2 - Mock PCAP exams 

# import pandas as pd
# df = pd.read_csv("mini-df.csv")

# pd.set_option('display.max_columns', None)
# print(df.head())
# df = df.sort_values(['longitude', 'latitude'], ascending = [True, False])

# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))
# g2 = gen()
# print(next(g2))

# data = [None, 0, '', 'hello', [], {1: 2}, False]
# result = list(filter(None, data))
# print(result) #['hello', {1: 2}]

# names = ['Charlie', 'Alice', 'Bob']
# result = sorted(names, key=lambda s: s[-1])
# print(result[0])
# print(result[-1])
# print(result)

# import os
# p = '/var/log/app/errors.log'
# print(os.path.basename(p))
# print(os.path.dirname(p).split('/')) #['', 'var', 'log', 'app]

# class Tracker:
#     __slots__ = ['value']

#     def __init__(self, v):
#         self.value = v

# t = Tracker(10)
# print(t.value)
# print(hasattr(t, '__dict__')) #False


# with open('test.txt', 'r+') as f:
#     f.seek(0, 2)
#     f.write('!')
# f2 = open('test.txt', 'r')
# print(f2.read())
# f2.close()

# ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
# result = ops[0](ops[1](ops[2](2)))
# print(result) #9

#CD Python - task 128

'''
Zadanie
Ile jest mieszkań, które zostały wybudowane między 2000 a 2012 rokiem (włącznie)
i nie mają podanego właściciela budynku (build_owner)?

Odpowiedź przypisz do zmiennej count_flats.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# pd.set_option('display.max_columns', None)
# df.head(5)
# df = df[((df['build_year'] >= 2000) & (df['build_year'] <= 2012)) & df['build_owner'].isna()]
# count_flats = len(df)


#CD Python - task 129

'''
Zadanie
Jaka jest średnia cena za metr 10 mieszkań, które mają najmniejszą powierzchnię?

Przypisz średnią zaokrągloną do 2 miejsc po przecinku do zmiennej avg_price.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# pd.set_option('display.max_columns', None)
# df.head(5)
# df = df.sort_values('area')
# first_ten = df[:10]
# avg_price = first_ten.describe()
# avg_price = 13012.50


#CD Python - task 130

'''
Więcej ogłoszeń o pracę zawiera w kolumnie z technologiami słowo SQL czy Python?
Zachowaj wielkość liter.

Jeżeli jest to SQL, przypisz wartość True do zmiennej sql_more_often, w innym przypadku przypisz wartość False.
'''

# import pandas as pd
# df = pd.read_csv("offers.csv")
# pd.set_option('display.max_columns', None)
# print(df.head(5))

# print(df.columns)
# counters = {'Python': 0, 'SQL': 0}
# sql_more_often = None
# for index, row in df.iterrows():
#     # techs = str(row['TECHNOLOGIE']).split()
#     # print(techs)
#     if 'Python' in str(row['TECHNOLOGIE']).split():
#         counters['Python'] += 1
#     elif 'SQL' in str(row['TECHNOLOGIE']).split():
#         counters['SQL'] += 1

# if counters['Python'] > counters['SQL']:
#     sql_more_often = False
# else:
#     sql_more_often = True

# print(counters)
# print(sql_more_often)

#CD Python - task 131

'''
Ile ofert pracy zawiera w technologiach słowo Python i ma zdalny tryb pracy?

Przypisz ilość ofert do zmiennej cnt_offers.
'''

# import pandas as pd
# df = pd.read_csv("offers.csv")
# pd.set_option('display.max_columns', None)
# print(df.columns)

# df = df[df['TYP PRACY'] == 'Remote']
# print(df.head(5))

# df = df[df['TECHNOLOGIE'].str.contains('Python')]
# print(df.head(5))
# cnt_offers = len(df)




#W14 D3 - PCAP Mock exams exercises

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f'{self.name} speaks'

# class Dog(Animal):
#     def speak(self):
#         return f'{self.name} barks'

#     def describe(self):
#         return self.speak()

# d = Dog('Rex')
# print(d.describe())



# class Printer:
#     def output(self, text):
#         return text

#     def print_all(self, items):
#         return [self.output(i) for i in items]

# class UpperPrinter(Printer):
#     def output(self, text):
#         return text.upper()

# up = UpperPrinter()

# print(up.print_all(['hello', 'world']))

# class Shape:
#     def area(self):
#         return 0

#     def summary(self):
#         return f'Area: {self.area()}'

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# s = Square(4)
# print(s.summary())

# with open('log.txt', 'w') as f:
#     f.write('ERROR: timeout')

# with open('log.txt', 'r') as f:
#     line = f.readline()
#     rest = f.read()

# print(repr(line))
# print(repr(rest))


# data = ['apple', 'banana', 'cherry', 'date']
# result = sorted(data, key=lambda s: (len(s), s))
# print(result[0])
# print(result[-1])


# import sys

# print(type(sys.modules) is dict)
# print(type(sys.argv) is list)

# try:
#     x = None + 1
# except TypeError as e:
#     print(type(e).__name__) #TypeError
#     print('caught') #caught

# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Money(self.amount + other.amount)

#     def __str__(self):
#         return f'${self.amount}'

# a = Money(10)
# b = Money(5)
# print(a + b) #$15
# print(str(a)) #$10


# class Base:
#     def greet(self):
#         return 'base'

#     def run(self):
#         return self.greet()

# class Sub(Base):
#     def greet(self):
#         return 'sub'

# s = Sub()
# print(s.greet())



# class A:
#     pass

# class B(A):
#     pass

# print(B.__bases__) #(<class '__main__.A'>,)
# print(A.__bases__) #(<class 'object'>,)


#CD Python - task 132

'''Zimportuj dane z pliku clients.csv.

Ogranicz dane tylko do kobiet, posortuj według alfabetycznie według nazwiska oraz zapisz kolumnę z nr pesel jako indeks.'''

# import pandas as pd

# df = pd.read_csv('clients.csv')
# df = df[df['plec'] == 'K']
# df.set_index('pesel', inplace = True)
# df.sort_values('nazwisko', inplace = True)
# print(df.head)


#CD Python - task 133

'''Zadanie
Ile kosztuje najmniejsze mieszkanie, które zawiera piwnicę lub garaż? Przypisz cenę do zmiennej price.'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# conditions =  (df['garage'] == 1) | (df['basement'] == 1)
# df = df[conditions]
# pd.set_option('display.max_columns', None)
# df = df.sort_values('area')
# price = df.iloc[0]['price']
# print(price)

#CD Python - task 134

'''Zadanie
Jaki odsetek ofert pracy zawiera w wymaganych technologiach AI lub ML?

Wynik zaokrąglony do 2 miejsc po przecinku zapisz w zmiennej ai_share.
'''

# import pandas as pd
# df = pd.read_csv("offers.csv")

# pd.set_option('display.max_columns', None)
# ai_offers = df[(df['TECHNOLOGIE'].str.contains('AI')) | (df['TECHNOLOGIE'].str.contains('ML'))]
# ai_share = round(len(ai_offers) / len(df) * 100, 2)
# print(ai_share)

# print(len(""""""))
# print(len('\''))
# print(chr(ord('A') + 1) == 'B')


# class Renderer:
#     def render(self, text):
#         return text

#     def output(self):
#         return self.render('data')

# class HtmlRenderer(Renderer):
#     def render(self, text):
#         return f'<p>{text}</p>'

# hr = HtmlRenderer()
# print(hr.output())


# def logger(prefix):
#     messages = []
#     def log(msg):
#         messages.append(f'{prefix}: {msg}')
#         return messages[:]
#     return log

# info = logger('INFO')
# warn = logger('WARN')
# print(info('start'))
# print(warn('alert'))
# print(info('end'))



# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# g = countdown(3)
# vals = list(g)
# print(vals)
# print(next(g, 'done'))

# fns = [lambda x, k=k: x * k for k in [2, 3, 5]]
# results = [f(4) for f in fns]
# print(results)

#CD Python - task 135

'''
Przefiltruj df, wybierając oferty mieszkań, których wartość w kolumnie date
należy do: '2020-12-16', '2020-09-07', '2020-12-21', '2020-10-06', '2020-10-18'.

Wynik przypisz do zmiennej df_limited.
'''


# import pandas as pd 
# df = pd.read_csv("mini-df.csv")
# df.head()

# pd.set_option('display.max_columns', None)
# df_limited = df[df['date'].str.contains('2020-12-16|2020-09-07|2020-12-21|2020-10-06|2020-10-18')]
# print(df_limited)


#CD Python - task 136

'''Zamień typy danych we wszystkich kolumnach df na dane numeryczne.'''

# import pandas as pd

# df = pd.DataFrame({
#     "price": ["450000", "520000", "610000", None, "480000"],
#     "area": ["45.5", "60.0", "72.3", "50.0", None],
#     "rooms": ["2", "3", "3", "2", "4"],
#     "floor": ["1", "2", "parter", "4", "3"],
#     "year_built": ["2005", "2010", "brak", "1998", "2001"],
# })

# columns_to_convert = ['price', 'area', 'rooms', 'floor', 'year_built']

# for column in columns_to_convert:
#     df[column] = pd.to_numeric(df[column], errors = 'coerce')
# print(df.head)
# print(df.dtypes)


#CD Python - task 137

'''
Jaką powierzchnię ma mieszkanie z rynku pierwotnego o najwyższej cenie za metr kwadratowy?

Przypisz powierzchnię do zmiennej area.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# df.sort_values('price_per_m', ascending = False, inplace = True)
# area = df.iloc[0]['area']
# print(area)



#CD Python - task 138

'''
Policz liczbę wierszy, dla których build_owner
nie jest pusty oraz co najmniej jedna z kolumn build_type lub build_status nie jest pusta.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()
# condition = df['build_owner'].notna() & (df['build_type'].notna() | df['build_status'].notna())
# df = df[df['build_owner'].notna() & (df['build_type'].notna() | df['build_status'].notna())]
# number = len(df)
# print(number)




#PCAP MOCK EXAMS - some qs to confirm AFTER answering

# a = [1, 2, 3]
# b = ['x', 'y']
# result = list(zip(a, b))
# print(result) #[(1, 'x'), (2, 'y')] - SO ONLY THE ELEMENTS THAT CAN BE ZIPPED AND HAVE A PAIR
# print(len(result)) #2


# values = [0, '', None, 1, 'hello', [], False, 42]
# result = list(filter(None, values))
# print(result) #[1, 'hello', 42]
# print(len(result)) #3


# class Strict:
#     pass

# try:
#     raise Strict()
# except TypeError:
#     print('type error')
# except Exception:
#     print('exception')


# items = [1, 'two', 3.0, None]
# print(f'{items!r}') #[1, 'two', 3.0, None]
# print(f'{len(items)!s}') #4


# class Team:
#     members = []

# t1 = Team()
# t2 = Team()
# t1.members.append('Alice')

# print(t1.__dict__) #{}
# print(t2.__dict__) #{}
# print(t1.members)#['Alice]
# print(t2.members) #['Alice]
# print(t1.members is t2.members) #True


# data = [3, 1, 4, 1, 5, 9, 2, 6]
# unique_sorted = sorted(set(data))
# print(unique_sorted)
# print(unique_sorted[-1])


#CD Python - 20.04.2026

# import pandas as pd
# df = pd.read_csv('ohlc_mock_data.csv', index_col ='timestamp')
# print(df.head)
# print(df.shape)
# print(len(df.iloc[0:5, :]))

# import pandas as pd 
# data = {
#     "id": [1, 2, 3, 4, 5],
#     "full_name": [
#         "Anna Kowalska",
#         "Jan Nowak",
#         "Kasia Zielińska",
#         "Piotr Wiśniewski",
#         "Ola Mazur"
#     ]
# }

# df = pd.DataFrame(data)
# df.head()

# df['first_name'] = df['full_name'].apply(lambda x: x.split()[0])
# df['last_name'] = df['full_name'].apply(lambda x: x.split()[1])
# print(df)

# def get_gender(full_name):
#     first_name = full_name.split()[0]
#     if first_name.endswith('a'):
#         gender = 'female'
#     else:
#         gender = 'male'
#     return gender

# df['gender'] = df['full_name'].apply(get_gender)
# print(df)


#CD Python - 21.04 - task 

'''
Dodaj kolumnę build_age, która liczy wiek budynku w latach. Usuń kolumnę build_year.
'''


# import pandas as pd

# df = pd.read_csv("mini-df.csv")
# df.head()

# from datetime import datetime
# today = datetime.today() #można by było tak, ale w zasadzie po co


# pd.set_option('display.max_columns', None)
# df['build_age'] = 2026 - df['build_year']
# df.drop(columns = ['build_year'], inplace = True)


#CD Python - 21.04 - task2

'''
Stwórz kolumnę requires_python, w której są wartości True/False. 
Ustaw wartość True dla wierszy zawierających słowo Python w kolumnie TECHNOLOGIE lub OPIS. 
Pomiń wielkość liter (uwzględniaj zarówno Python jak i python).

Następnie przypisz do zmiennej python_share proporcję ile ofert z wszystkich wymaga Pythona. 
Zaokrąglij do 2 cyfr po przecinku.
'''


# import pandas as pd
# df = pd.read_csv("offers.csv")
# df.head()

# condition1 = df['OPIS'].str.lower().str.contains('python')
# condition2 = df['TECHNOLOGIE'].str.lower().str.contains('python')

# python_offers = df[condition1 | condition2]
# pd.set_option('display.max_columns', None)
# print(python_offers.head())
# python_share = round(len(python_offers) / len(df), 2)
# print(python_share)


#CD Python - 21.04 - task3

'''
Zmień precyzję w kolumnie price_per_m, aby wartości miały 4 cyfry po przecinku.

Oblicz je na podstawie kolumn area i price.
'''
# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()
# df['price_per_m'] = round(df['price'] / df['area'], 4)
# pd.set_option('display.max_columns', None)
# print(df.head())

#CD Python - 21.04 - task4

'''
Uzupełnij brakujące wartości w kolumnie build_year medianą z tej kolumny.

Oblicz średnią wartość w tej kolumnie i przypisz ją do zmiennej mean_build_year.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# print(df['build_year'].isna().sum())
# df['build_year'] = df['build_year'].fillna(df['build_year'].median())
# mean_build_year = df['build_year'].mean()
# print(mean_build_year)


#CD Python - 21.04 - task5
'''
Jeżeli mieszkanie zawiera jedno z poniższych typów ogrzewania: 
"electrical", "boiler_room", "gas", zwiększ jego cenę (kolumnę price) o 500.

'''
# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()
# pd.set_option('display.max_columns', None)

# heating_to_change = ["electrical", "boiler_room", "gas"]
# df.loc[df["heating"].isin(heating_to_change), "price"] += 500



#CD Python - 21.04 - task6
'''
Jaki jest najbardziej popularna wartość w kolumnie build_type?

Przypisz odpowiedź do zmiennej top_build_type.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# top_build_type = df['build_type'].value_counts().head(1).index
# print(top_build_type)


#CD Python - 21.04 - task7

'''
Stwórz kolumnę cnt_benefits, która sumuje ile benefitów ma każde mieszkanie.

Benefity znajdują się w kolumnach z wartościami 0/1 pojawiających się w df po kolumnie date

Przypisz wartość indexu mieszkania z największą ilością benefitów do zmiennej best_flat_id.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# pd.set_option('display.max_columns', None)

# benefit_columns = 'air_conditioning	balcony	basement	garage	garden	lift	nan	separate_kitchen	terrace	two_storey	usable_room	alarm	anti_burglary_door	closed_area	entryphone	monitoring	roller_shutters'.split()

# df['cnt_benefits'] = df[benefit_columns].sum(axis = 1)
# best_flat_id = df[df['cnt_benefits'] == df['cnt_benefits'].max()].index
# print(best_flat_id)



#CD Python - 22.04 - task 1

'''
Zastąp wartości boiler_room w kolumnie heating wartościami gas.

Jaką proporcję wszystkich niebrakujących wierszy stanowią wiersze z wartością gas?
Zaokrąglij do 2 cyfr po przecinku i przypisz do zmiennej gas_share.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# df['heating'] = df['heating'].replace('boiler_room', 'gas')
# length_without_nans = df['heating'].isna().sum()
# gas_share = round(df['heating'].value_counts()['gas'] / (len(df) - length_without_nans), 2)
# print(gas_share)


#CD Python - 22.04 - task 2

'''Stwórz w DataFrame df kolumnę build_category w której wierszami z wartościami block, apartment, 
tenement w kolumnie build_type przypiszesz wartość shared, a dla wierszy z wartością house -> standalone.'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# mask_plan = {
#     'block': 'shared',
#     'apartment': 'shared',
#     'tenement': 'shared',
#     'house': 'standalone'
#     }
# df['build_category'] = df['build_type'].map(mask_plan)
# print(df['build_category'])


#CD Python - 22.04 - task 3

'''
Stwórz w DataFrame df kolumnę price_category.

Kolumna powinna przyjmować następujące kategorie na podstawie wartości kolumny price_per_m:

poniżej 8000 -> cheap
8000-9999 -> moderate
10000 - 12999 -> expensive
powyżej 13000 -> very expensive
Ile mieszkań przyjmuje najczęściej spotykaną kategorię? Przypisz odpowiedź do zmiennej cnt_top
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# def check_category(price):
#     if price < 8000:
#         return 'cheap'
#     elif 8000 <= price <= 9999:
#         return 'moderate'
#     elif 10000 <= price <= 12999:
#         return 'expensive'
#     else:
#         return 'very expensive'

# df['price_category'] = df['price_per_m'].apply(check_category)
# print(df['price_category'])

# cnt_top = df['price_category'].value_counts().head(1).item()
# print(cnt_top)


#CD Python - 22.04 - task 4

'''
Która z kolumn, poza kolumną url zawiera największą liczbę unikalnych wartości?

Przypisz nazwę kolumny do zmiennej most_unique_col
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# pd.set_option('display.max_columns', None)
# most_unique_col = df.nunique()[1:].head(1).index.item() # TU ŹLE - tu ogólnie wydziubałem to, ALE WCALE ONE NIE SĄ POSORTOWANE, WIĘC WYNIK BYŁ ZŁY - to była po prostu druga kolumna - akurat tam ułożyły się posortowane i tak sięwydawało xd


# pd.set_option('display.max_columns', None)
# unique_col_numbers = list(df.nunique()[1:].items()) #lista oprócz urla, akurat był w pozycji 0
# most_unique_col = sorted(unique_col_numbers, key = lambda x: x[1], reverse = True)[0][0]
# print(most_unique_col)

#CD Python - 24.04 - task 1

'''
Wyciągnij miasto i wiek użytkowników z kolumny info i przypisz je do nowych kolumn city oraz age.

Usuń kolumnę info
'''


# import pandas as pd

# data = {
#     "id": [1, 2, 3],
#     "info": [
#         {"city": "Warszawa", "age": 25},
#         {"city": "Kraków", "age": 30},
#         {"city": "Gdańsk", "age": 28}
#     ]
# }
# df = pd.DataFrame(data)
# df.head()
# df['age'] = df['info'].apply(lambda x: x['age'])
# df['city'] = df['info'].apply(lambda x: x['city'])
# df.drop(columns =['info'], inplace = True)
# df.head()


#CD Python - 24.04 - task 2

'''
Zmień wartości w kolumnie city:

jeżeli miasto wchodzi w skład miast z listy wojewodzkie, zostaw wartość miasta
jeżeli nie wchodzi, zamień wartość na None
'''

# import pandas as pd
# import random 
# random.seed(42)

# wojewodzkie = [
#     "Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań",
#     "Gdańsk", "Szczecin", "Bydgoszcz", "Toruń", "Lublin",
#     "Białystok", "Katowice", "Kielce", "Olsztyn",
#     "Gorzów Wielkopolski", "Zielona Góra", "Opole", "Rzeszów"
# ]
# cities = [
#     "Warszawa","Kraków","Łódź","Wrocław","Poznań","Gdańsk","Szczecin","Bydgoszcz",
#     "Lublin","Białystok","Katowice","Gorzów Wielkopolski","Zielona Góra","Opole",
#     "Rzeszów","Kielce","Olsztyn","Toruń",
#     "Radom","Płock","Siedlce","Nowy Sącz","Tarnów","Koszalin","Legnica","Elbląg",
#     "Piotrków Trybunalski","Kalisz","Konin","Chełm","Zamość","Suwałki","Ełk",
#     "Ostrołęka","Przemyśl","Stalowa Wola","Mielec","Puławy","Świdnica","Gniezno",
#     "Leszno","Inowrocław","Świnoujście","Kołobrzeg","Sopot","Zakopane","Sieradz",
#     "Kutno","Otwock","Mińsk Mazowiecki"
# ]

# data = {
#     "id": range(1, 101),
#     "city": [random.choice(cities) for _ in range(100)],
# }

# df = pd.DataFrame(data)
# df.head()

# df['city'] = df['city'].apply(lambda x: x if x in wojewodzkie else None) #Opcja 1
# print(df.head())

# from typing import List

# def check_city(city: str, wojewodzkie: List[str] = wojewodzkie) -> str: #Opcja2
#     if city in wojewodzkie:
#         return city
#     else:
#         return None
    
# df['city'] = df['city'].apply(check_city)
# df.head()
# print(df.head())


#CD Python - 24.04 - task 3

'''
Zadanie
Stwórz listę pod zmienną numerical_cols, która zawiera nazwy kolumn DataFrame df z danymi numerycznymi.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# numerical_cols = [col for col in df.columns if df[col].dtype != object]
# print(numerical_cols)


#CD Python - 24.04 - task 4

'''
Stwórz kolumnę desired_flat, która zawiera wartość True dla mieszkań,
które są tańsze niż 10 000 za metr, mają balkon i są z rynku wtórnego.

Przypisz do zmiennej median_area jaka jest mediana powierzchni takich mieszkań.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()
# pd.set_option('display.max_columns', None)

# conditions = (df['price_per_m'] <= 10000) & (df['balcony'] == 1) & (df['market_type'] == 'secondary')
# df['desired_flat'] = False
# df['desired_flat'] = df['desired_flat'].mask(conditions, True)
# print(df.head())

# desired_flats = df[conditions]
# print(desired_flats.describe())
# median_area = desired_flats['area'].quantile(0.5)
# print(median_area)


#CD Python - 24.04 - task 5

'''
Ile mieszkań ma zarówno balkon, garaż, jak i windę?

Przypisz ilość mieszkań do zmiennej decent_flats
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# pd.set_option('display.max_columns', None)
# print(df.head())

# conditions = (df['balcony'] == 1) & (df['garage'] == 1) & (df['lift'] == 1)
# decent_flats = len(df[conditions])
# print(decent_flats)



#CD Python - 24.04 - task 6

'''
Zadanie
Która z wymienionych niżej kolumn z listy cols zawiera najwięcej duplikatów?

cols = ["area", "price", "build_year",  "build_floor_num", "date"]
Przypisz odpowiedź do zmiennej most_duplicated_col.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# cols = ["area", "price", "build_year",  "build_floor_num", "date"]
# cols_dups = [(column, df[column].duplicated().sum()) for column in cols]
# print(cols_dups)
# sorted_cols = sorted(cols_dups, key = lambda x: x[1], reverse = True)
# most_duplicated_col = sorted_cols[0][0]


#CD Python - 24.04 - task 7

'''

Zamień wartości w kolumnie MIASTO na Other dla miast, z których każde stanowi mniej niż 1% wszystkich ofert pracy.
'''


# import pandas as pd
# df = pd.read_csv("offers.csv")
# df.head()
# minimum_threshold = len(df) / 100

# low_number_cities = []
# miasta = df['MIASTO'].value_counts().to_frame().reset_index()
# for index, row in miasta.iterrows():
#     count = row.iloc[1]
#     if count < minimum_threshold:
#         low_number_cities.append(row.iloc[0])

# print(low_number_cities)
# df['MIASTO'] = df['MIASTO'].mask(df['MIASTO'].isin(low_number_cities), 'Other')
# pd.set_option('display.max_columns', None)
# print(df.head())

#Ja to ogarnąłem tak, ale Kasia w sumie miałą lepsze rozwiązanie

# miasto_df = df["MIASTO"].value_counts(normalize=True).reset_index() #tu od razu wbijamy na wartości procentowe, któe mnie interesują, nie ma po co liczyć
#cities_to_remove = miasto_df["MIASTO"][miasto_df["proportion"] < 0.01].values.tolist() - zręczne wyfiltrowanie

# df["MIASTO"] = df["MIASTO"].mask(df["MIASTO"].isin(cities_to_remove), "Other") #i na koniec w zasadzie to samo


#CD Python - 24.04 - task 8

'''
Dla każdej wartości z poniższej listy skills utwórz nową kolumnę w DataFrame df
o nazwie kolumny jak wartość z listy.

skills = ['Excel', 'Power BI', 'SQL', 'Python', 'Tableau']
W każdej z tych kolumn wpisz:

True jeśli dana wartość występuje w liście w kolumnie skills w tym wierszu
False w przeciwnym przypadku

'''

# import pandas as pd

# data = {
#     "id": [1, 2, 3, 4, 5, 6, 7, 8],
#     "skills": [
#         ["SQL", "Python", "Excel"],
#         ["Python", "Tableau"],
#         ["Excel", "Power BI", "SQL", "Python"],
#         ["Python"],
#         ["SQL", "Tableau", "Power BI"],
#         ["Python", "SQL"],
#         ["Excel", "SQL", "Tableau"],
#         ["Python", "Excel"]
#     ]
# }
# df = pd.DataFrame(data)
# skills = ['Excel', 'Power BI', 'SQL', 'Python', 'Tableau']
# for skill in skills:
#     df[skill] = df['skills'].apply(lambda x: skill in x)
# df.head()


#CD Python - 27.04 - task 1

'''
Zadanie
Jaki typ budynku (build_type) ma najtańszą średnią cenę za metr? Nazwę typu budynku przypisz do zmiennej cheapest_type.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# df_agg = df.groupby('build_type')['price_per_m'].mean().reset_index()
# print(df_agg)
# cheapest_type = df_agg.sort_values('price_per_m').head(1)['build_type'].item()
# print(cheapest_type)


#CD Python - 27.04 - task 2

'''
Zadanie
Stwórz dataframe o nazwie df, który zawiera dane z wszystkich wierszy z df1 i df2, ale tylko ze wspólnych kolumn.
'''

# import pandas as pd

# df1 = pd.DataFrame({
#     "id": [1, 2, 3],
#     "name": ["Anna", "Jan", "Ola"],
#     "city": ["Warszawa", "Kraków", "Gdańsk"],
#     "salary": [5000, 6000, 5500]
# })

# df2 = pd.DataFrame({
#     "id": [4, 5],
#     "name": ["Piotr", "Kasia"],
#     "age": [28, 34],
#     "country": ["Polska", "Polska"]
# })

# common_cols = list(set(df1.columns).intersection(df2.columns))
# print(common_cols)

# df = pd.concat([df1[common_cols], df2[common_cols]], ignore_index = True)
# print(df)


#CD Python - 27.04 - task 3

'''
Dołącz do df_users dodatkowe kolumny z df_cities na podstawie łączenia wspólnej kolumny.
'''

# import pandas as pd

# df_users = pd.DataFrame({
#     "user_id": [1, 2, 3, 4],
#     "name": ["Anna", "Jan", "Ola", "Piotr"],
#     "city_id": [10, 20, 10, 30]
# })

# df_cities = pd.DataFrame({
#     "city_id": [10, 20, 30, 40],
#     "city_name": ["Warszawa", "Kraków", "Gdańsk", "Wrocław"],
#     "region": ["Mazowieckie", "Małopolskie", "Pomorskie", "Dolnośląskie"]
# })


# df_users = df_users.merge(df_cities, on = 'city_id')
# print(df_users)


#CD Python - 28.04 - task 1

'''
Na podstawie DataFrame users oraz orders stwórz listę użytkowników,
którzy nigdy niczego nie zamówili i przypisz ją do zmiennej users_list.
'''

# import pandas as pd
# import numpy as np

# np.random.seed(42)

# n_users = 50
# users = pd.DataFrame({
#     "user_id": range(1, n_users + 1),
#     "city": np.random.choice(
#         ["Warszawa", "Kraków", "Gdańsk", "Wrocław", "Poznań", "Łódź"],
#         size=n_users
#     )
# })

# n_orders = 80
# orders = pd.DataFrame({
#     "order_id": range(1001, 1001 + n_orders),
#     "user_id": np.random.choice(users["user_id"], size=n_orders, replace=True),
#     "amount": np.random.randint(50, 500, size=n_orders),
#     "order_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(
#         np.random.randint(0, 180, size=n_orders), unit="D"
#     )
# })

# users_no_orders = users.merge(orders, how = 'left')


# def check_none(row):
#     if row.isna():
#         return 'no_order'

# users_no_orders['order_id'] = users_no_orders['order_id'].mask(users_no_orders['order_id'].isna(), 'no_orders')
# users_list = users_no_orders[users_no_orders['order_id'] == 'no_orders'].reset_index()
# users_list = users_list['user_id'].values.tolist()
# print(users_list)


#CD Python - 28.04 - task 2
'''
Na podstawie DataFrame users oraz orders stwórz DataFrame df, który zawiera 3 kolumny:

user_id
city
avg_amount: średnia kwota zamówienia użytkownika. 
Jeżeli użytkownik nie miał żadnych zamówień, przypisz 0 do tej kolumny.
'''

# import pandas as pd
# import numpy as np

# np.random.seed(42)

# n_users = 50
# users = pd.DataFrame({
#     "user_id": range(1, n_users + 1),
#     "city": np.random.choice(
#         ["Warszawa", "Kraków", "Gdańsk", "Wrocław", "Poznań", "Łódź"],
#         size=n_users
#     )
# })

# n_orders = 80
# orders = pd.DataFrame({
#     "order_id": range(1001, 1001 + n_orders),
#     "user_id": np.random.choice(users["user_id"], size=n_orders, replace=True),
#     "amount": np.random.randint(50, 500, size=n_orders),
#     "order_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(
#         np.random.randint(0, 180, size=n_orders), unit="D"
#     )
# })


# orders_agg = orders.groupby("user_id")["amount"].mean().reset_index()
# df = users.merge(orders_agg, on = 'user_id', how = 'left')
# df["amount"] = df["amount"].fillna(0)
# df.rename(columns={"amount": "avg_amount"}, inplace=True)
# print(df)


#CD Python - 28.04 - task 3
'''
Przypisz do zmiennej leader ID leadera, który ma pod sobą najwięcej pracowników.
'''

# import pandas as pd
# employees = pd.DataFrame({"employee_id":list(range(1,59)),"employee_name":["Anna","Jan","Kasia","Piotr","Ola","Marek","Ewa","Tomek","Magda","Paweł","Natalia","Kasia","Ola","Ewa","Bartek","Zosia","Adam","Karolina","Michał","Monika","Filip","Alicja","Kamil","Joanna","Rafał","Piotr","Marek","Tomek","Paweł","Bartek","Julia","Mateusz","Weronika","Łukasz","Dominika","Szymon","Iwona","Robert","Jan","Magda","Natalia","Zosia","Karolina","Monika","Alicja","Joanna","Julia","Weronika","Dominika","Iwona","Helena","Artur","Beata","Dawid","Nina","Wiktor","Laura","Krystian"],"department":["Sales","Sales","Sales","Sales","Sales","Sales","Marketing","Marketing","Marketing","Marketing","Marketing","Marketing","Marketing","Marketing","Finance","Finance","Finance","Finance","Finance","Finance","Finance","Analytics","Analytics","Analytics","Analytics","Analytics","Analytics","Analytics","Analytics","Analytics","Customer Success","Customer Success","Customer Success","Customer Success","Customer Success","Customer Success","Customer Success","Customer Success","Sales","Sales","Sales","Sales","Sales","Sales","Marketing","Marketing","Marketing","Marketing","Marketing","Marketing","Finance","Finance","Finance","Finance","Finance","Finance","Finance","Finance"],"assigned_at":pd.to_datetime(["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05","2024-01-06","2024-01-07","2024-01-08","2024-01-09","2024-01-10","2024-01-11","2024-01-12","2024-01-13","2024-01-14","2024-01-15","2024-01-16","2024-01-17","2024-01-18","2024-01-19","2024-01-20","2024-01-21","2024-01-22","2024-01-23","2024-01-24","2024-01-25","2024-01-26","2024-01-27","2024-01-28","2024-01-29","2024-01-30","2024-02-01","2024-02-02","2024-02-03","2024-02-04","2024-02-05","2024-02-06","2024-02-07","2024-02-08","2024-02-09","2024-02-10","2024-02-11","2024-02-12","2024-02-13","2024-02-14","2024-02-15","2024-02-16","2024-02-17","2024-02-18","2024-02-19","2024-02-20","2024-02-21","2024-02-22","2024-02-23","2024-02-24","2024-02-25","2024-02-26","2024-02-27","2024-02-28"]),"lead_id":[1001,1001,1001,1001,1001,1001,1002,1002,1002,1002,1002,1002,1002,1002,1003,1003,1003,1003,1003,1003,1003,1004,1004,1004,1004,1004,1004,1004,1004,1004,1005,1005,1005,1005,1005,1005,1005,1005,1006,1006,1006,1006,1006,1006,1007,1007,1007,1007,1007,1007,1008,1008,1008,1008,1008,1008,1008,1008]})
# employees.head()

# leader = employees['lead_id'].value_counts().reset_index().head(1).values.tolist()[0][0]
# print(leader)


#CD Python - 29.04 - task 1


'''
Dla każdej kombinacji miasta i produktu oblicz łączną wartość przychodu.

Najwyższy przychód dla kombinacji miasto/produkt przypisz do zmiennej top_product_city_amount.
'''


# import pandas as pd

# df = pd.DataFrame({
#     "order_id": [1,2,3,4,5,6,7,8],
#     "city": ["Kraków","Kraków","Warszawa","Warszawa","Warszawa","Gdańsk","Gdańsk","Kraków"],
#     "product": ["Laptop","Telefon","Laptop","Tablet","Laptop","Telefon","Laptop","Tablet"],
#     "price": [4000,2000,4200,1500,4100,2100,3900,1600]
# })

# print(df.head())
# city_product_revenue = df.groupby(['city', 'product']).agg('sum')
# print(city_product_revenue)

# top_product_city_amount = max(city_product_revenue['price'])
# print(top_product_city_amount)


#CD Python - 29.04 - task 2

'''
Dla jakiego rynku, pierwotnego czy wtórnego, bardziej zmieniła się średnia cena za metr kwadratowy mieszkania
porównując pierwszy i ostatni dzień dostępny w danych?

Przypisz nazwę primary lub secondary do zmiennej changed_more.

'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# #czyli avg price_per_m dla primary i secondary marketów z pierwszego i ostatniego dnia

# average_prices = df.groupby(['market_type', 'date']).agg({'price_per_m': 'mean'})

# diff = average_prices.groupby(level='market_type').last() - average_prices.groupby(level='market_type').first()
# print(diff)
# changed_more = 'secondary'


#CD Python - 29.04 - task 3

'''
Zadanie
W jakim miesiącu była największa zmiana (na plus lub minus) w średniej cenie za metr mieszkania?

Przypisz miesiąc w postaci YYYY-MM, np. 2021-01 do zmiennej greatest_change.

Przydadzą Ci się metody:

dt.to_period("M") - które wyciąga rok-miesiąc z kolumny o typie danych datetime
shift(1) - które wyciąga wartość z poprzedniego wiersza

'''

# import pandas as pd
# from datetime import date, datetime
# df = pd.read_csv("mini-df.csv")
# df.head()

# df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")
# df_price = df["price_per_m"].groupby(df["month"]).mean().reset_index().sort_values(by="month")
# df_price["next_price_per_m"] =  df_price["price_per_m"].shift(1)
# df_price["difference"] = abs(df_price["price_per_m"] - df_price["next_price_per_m"])
# greatest_change = df_price.sort_values(by="difference", ascending=False)
# print(greatest_change)


#CD Python - 29.04 - task 4


'''
Zadanie
Jakie produkty kupił Piotr, których nie kupił Jan?

Nazwy produktów przypisz do zmiennej piotr_products w formie listy.

Odpowiedź na podstawie dataframes users, orders i products.

'''

# import pandas as pd


# users = pd.DataFrame({"user_id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],"name":["Anna","Jan","Kasia","Piotr","Ola","Marek","Ewa","Tomek","Magda","Paweł","Natalia","Bartek","Zosia","Adam","Karolina"]})
# orders = pd.DataFrame({"order_id":[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],"user_id":[1,2,2,3,4,4,4,6,7,7,8,9,10,10,11,12,13,13,14,20],"product_id":[10,11,12,10,11,13,10,12,10,14,11,12,10,15,11,12,10,13,14,10]})
# products = pd.DataFrame({"product_id":[10,11,12,13,14],"product_name":["Laptop","Telefon","Tablet","Monitor","Klawiatura"]})


# users_orders = users.merge(orders, on = 'user_id')
# users_orders_products = users_orders.merge(products, on = 'product_id')
# print(users_orders_products)

# jan_products = set()
# piotr_products = set()
# for index, order in users_orders_products.iterrows():
#     if order['name'] == 'Jan':
#         jan_products.add(order['product_name'])
#     elif order['name'] == 'Piotr':
#         piotr_products.add(order['product_name'])
        
# print(jan_products)
# print(piotr_products)

# piotr_products = list(piotr_products - jan_products)
# print(piotr_products)



#CD Python - 30.04 - task 1

'''
Na podstawie dataframes orders i transactions dodaj do dataframe users kolumny:

count_transactions - liczba transakcji użytkownika
count_orders - liczba zamówień użytkownika
mean_transactions - średnia kwota transakcji
mean_orders - średnia kwota zamówień użytkownika
sum_total - suma kwot wydanych przez użytkownika na transakcje i zamówienia
Brakujące wartości w kolumnach count oraz sum uzupełnij wartością 0.

'''


# import pandas as pd

# users = pd.DataFrame({"user_id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],"name":["Anna","Jan","Kasia","Piotr","Ola","Marek","Ewa","Tomek","Magda","Paweł","Natalia","Bartek","Zosia","Adam","Karolina"],"city":["Warszawa","Kraków","Gdańsk","Wrocław","Poznań","Łódź","Katowice","Lublin","Szczecin","Bydgoszcz","Rzeszów","Białystok","Gdynia","Opole","Toruń"]})

# orders = pd.DataFrame({"order_id":[101,102,103,104,105,106,107,108,109,110,111,112],"user_id":[1,2,1,3,4,5,2,6,7,8,9,10],"order_date":["2024-01-05","2024-01-07","2024-01-10","2024-01-12","2024-01-15","2024-01-18","2024-01-20","2024-01-22","2024-01-25","2024-01-27","2024-02-01","2024-02-03"],"amount":[120,200,150,80,300,220,50,400,90,180,250,130]})

# transactions = pd.DataFrame({"transaction_id":[1001,1002,1003,1004,1005,1006,1007,1008],"order_id":[101,102,103,104,105,106,107,110],"payment_method":["card","blik","card","paypal","card","blik","card","card"],"transaction_date":["2024-01-05","2024-01-07","2024-01-10","2024-01-12","2024-01-15","2024-01-18","2024-01-20","2024-01-27"],"amount":[120,200,150,80,300,220,50,180]})


# users_orders = users.merge(orders, on = 'user_id', how = 'left')
# users = users_orders.merge(transactions, on = 'order_id', how = 'left')

# agg_function = ['mean', 'count', 'sum']
# col_names = {agg: agg +'_orders' for agg in agg_function}
# orders_agg = orders['amount'].groupby(orders['user_id']).agg(agg_function).reset_index().rename(columns = col_names)

# agg_function = ['mean', 'count', 'sum']
# col_names = {agg: agg +'_transactions' for agg in agg_function}
# transactions_agg = transactions['amount'].groupby(orders['user_id']).agg(agg_function).reset_index().rename(columns = col_names)
# print(transactions_agg)

# users = users.merge(orders_agg, on = 'user_id')
# users = users.merge(transactions_agg, on = 'user_id')

# cols_to_fill = [col for col in users.columns if 'count' in col or 'sum' in col]
# users[cols_to_fill] = users[cols_to_fill].fillna(0)
# print(users)

# users['total_sum'] = users['sum_orders'] + users['sum_transactions']
# users.drop(columns = ['sum_orders', 'sum_transactions'], inplace = True)
# print(users)


#CD Python - 30.04 - task 2

'''
Ilu użytkowników wydało więcej (kolumna amount) niż 200 na transakcje lub zamówienia (lub to i to)?
'''


# import pandas as pd

# orders = pd.DataFrame({"order_id":[301,302,303,304,305,306,307,308,309,310,311,312],"user_id":[1,2,1,3,4,5,6,2,7,8,9,10],"order_date":["2024-03-01","2024-03-02","2024-03-03","2024-03-05","2024-03-06","2024-03-07","2024-03-08","2024-03-10","2024-03-11","2024-03-12","2024-03-13","2024-03-15"],"amount":[250,180,90,300,120,400,75,60,500,130,210,95]})

# transactions = pd.DataFrame({"transaction_id":[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010],"user_id":[1,2,3,4,5,11,12,1,7,13],"transaction_date":["2024-03-01","2024-03-02","2024-03-05","2024-03-06","2024-03-07","2024-03-08","2024-03-09","2024-03-10","2024-03-11","2024-03-12"],"payment_method":["card","blik","paypal","card","blik","card","paypal","card","card","blik"],"amount":[250,180,300,120,400,220,150,60,500,75]})


# orders_agg = orders[["user_id", "amount"]].groupby("user_id").sum().reset_index().rename(columns={"amount":"orders_amount"})
# transactions_agg = transactions[["user_id", "amount"]].groupby("user_id").sum().reset_index().rename(columns={"amount":"transactions_amount"})

# orders_transactions = orders_agg.merge(transactions_agg, on = 'user_id', how = 'outer')
# orders_transactions = orders_transactions.fillna(0)
# print(orders_transactions)

# orders_transactions['total'] = orders_transactions['orders_amount'] + orders_transactions['transactions_amount']
# print(orders_transactions)
# count_users = len(orders_transactions[orders_transactions['total'] >200])
# print(count_users)



#CD Python - 30.04 - task 3


'''
Zadanie
Do dataframe orders dodaj kolumnę higher_than_avg, która przyjmuje wartość True, 
jeżeli kwota zamówienia przewyższa średnią kwotę zamówień z danego tygodnia. Dla reszty zamówień przypisz wartość False.

Wskazówka
Aby wyciągnąć tydzień, możesz użyć metody .dt.strftime('%U') na kolumnie z typem danych datetime.
'''


# import pandas as pd

# orders = pd.DataFrame({
#     "order_id":[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530],
#     "user_id":[1,2,3,4,5,1,2,6,7,8,3,4,5,6,7,1,2,3,8,9,10,1,2,3,4,5,6,7,8,9],
#     "order_date":[
#         "2024-01-02","2024-01-02","2024-01-03","2024-01-04","2024-01-05","2024-01-06",
#         "2024-01-09","2024-01-09","2024-01-10","2024-01-11","2024-01-12","2024-01-13",
#         "2024-01-16","2024-01-17","2024-01-18","2024-01-19","2024-01-20","2024-01-21",
#         "2024-01-23","2024-01-24","2024-01-25","2024-01-26","2024-01-27","2024-01-28",
#         "2024-02-01","2024-02-01","2024-02-02","2024-02-03","2024-02-03","2024-02-04" 
#     ],
#     "amount":[120,80,200,150,300,90,50,400,220,180,75,60,500,130,210,95,140,160,300,120,250,180,90,70,220,310,60,80,200,150]
# })

# print(orders.head())
# print(orders.dtypes)
# orders['week'] = pd.to_datetime(orders['order_date']).dt.strftime('%U')
# print(orders)


# orders_agg = orders['amount'].groupby(orders['week']).mean().reset_index().rename(columns={"amount":"avg_amount"})
# print(orders_agg)

# orders = orders.merge(orders_agg, on = 'week')
# orders['higher_than_avg'] = orders['amount'] > orders['avg_amount']
# print(orders)


#CD Python - 1.05 - task 1

'''
Zadanie
Jaka jest średnia kwota zamówienia dla top 10% najdroższych zamówień?

Przypisz ją z dokładnością 2 cyfry po przecinku do zmiennej top_avg_amount.
'''


# import pandas as pd

# orders = pd.DataFrame({"order_id":list(range(1001,1151)),"user_id":[3,1,7,2,5,9,4,6,8,2,1,3,10,7,5,6,9,8,4,2,6,3,1,8,7,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,6,1,7,8,5,10,9,4,2,3,1,6,7,5,10,8,9,4,2],"order_date":pd.date_range("2024-01-02", periods=150, freq="2D"),"amount":[135,220,180,75,310,260,90,410,120,200,150,170,330,190,210,95,280,240,130,160,140,300,110,205,270,320,180,150,100,260,170,220,195,280,140,310,260,180,150,200,175,220,140,260,300,180,210,170,190,230,260,140,210,180,320,260,140,200,170,150,180,240,260,220,300,180,150,210,170,200,260,140,210,180,320,260,140,200,170,150,180,240,260,220,300,180,150,210,170,200,260,140,210,180,320,260,140,200,170,150,180,240,260,220,300,180,150,210,170,200,260,140,210,180,320,260,140,200,170,150,180,240,260,220,300,180,150,210,170,200,260,140,210,180,320,260,140,200,170,150,180,240,260,220,300,180,150,210,170,200]})
# orders.head()
# orders_top_10 = orders['amount'].quantile(0.9)
# top_avg_amount = round(orders[orders['amount'] >= orders_top_10]['amount'].mean(), 2)
# print(top_avg_amount)



#CD Python - 1.05 - task 2
'''
Zadanie
Znajdź kolumnę, która ma największą rozpiętość wartości (różnicę między wartością maksymalną a minimalną).

Przypisz nazwę kolumny do zmiennej max_span_column.
'''

# max_span_column = None
# max_span_value = 0
# for column in df.columns:
#     diff = abs(df[column].max() - df[column].min())
#     if diff > max_span_value:
#         max_span_column = column
#         max_span_value = diff
        
# print(max_span_column, max_span_value)


#CD Python - 1.05 - task 3

'''
Zadanie
Jaka grupa wiekowa średnio wydaje najwięcej pieniędzy w zamówieniu?

Stwórz grupy wiekowe:

young <= 25 lat
middle_young 26 - 35 lat
middle_old 36 - 50 lat
old >= 51 lat
(Przepraszam jeżeli kogokolwiek uraziłam nazwą grupy.)

'''

# import pandas as pd

# users = pd.DataFrame({
#     "user_id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
#     "name":["Anna","Jan","Kasia","Piotr","Ola","Marek","Ewa","Tomek","Magda","Paweł","Natalia","Bartek","Zosia","Adam","Karolina","Michał","Alicja","Filip","Monika","Kamil","Julia","Mateusz","Weronika","Łukasz","Dominika"],
#     "age":[19,22,25,28,31,None,37,40,43,46,39,52,55,58,49,41,21,27,33,22,45,51,57,63,38],
#     "city":["Warszawa","Kraków","Gdańsk","Wrocław","Poznań","Łódź","Katowice","Lublin","Szczecin","Bydgoszcz","Rzeszów","Białystok","Gdynia","Opole","Toruń","Kielce","Olsztyn","Radom","Zielona Góra","Koszalin","Płock","Elbląg","Legnica","Słupsk","Tarnów"]
# })

# orders = pd.DataFrame({
#     "order_id":[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240],
#     "user_id":[1,2,3,1,4,5,2,6,7,8,9,10,11,12,13,14,15,3,5,7,2,1,16,17,18,19,20,21,22,23,24,25,16,18,20,22,24,17,19,21],
#     "order_date":[
#         "2024-01-05","2024-01-07","2024-01-10","2024-01-12","2024-01-15","2024-01-18","2024-01-20","2024-01-22","2024-01-25","2024-01-27",
#         "2024-02-01","2024-02-03","2024-02-05","2024-02-07","2024-02-10","2024-02-12","2024-02-15","2024-02-18","2024-02-20","2024-02-22",
#         "2024-02-25","2024-02-28","2024-03-02","2024-03-04","2024-03-06","2024-03-08","2024-03-10","2024-03-12","2024-03-14","2024-03-16",
#         "2024-03-18","2024-03-20","2024-03-22","2024-03-24","2024-03-26","2024-03-28","2024-03-30","2024-04-01","2024-04-03","2024-04-05"
#     ],
#     "amount":[120,200,150,80,300,220,50,400,90,180,250,130,75,310,160,300,95,140,275,60,210,330,180,95,260,310,120,150,40,220,130,170,280,200,90,350,410,160,240,30]
# })

# def define_age_group(age):
    # if age <= 25:
    #     return 'young'
    # elif age >= 26 and age <= 35:
    #     return 'middle_young'
    # elif age >= 36 and age <= 50:
    #     return 'middle_old'
    # elif age >= 51:
    #     return 'old'

# users['age_group'] = users['age'].apply(define_age_group)
# users = users.merge(orders, on = 'user_id')

# averages = users['amount'].groupby(users['age_group']).mean().reset_index()
# top_age_group = averages.sort_values(by='amount', ascending = False).head(1)['age_group'].item()

# print(top_age_group)


#CD Python - 1.05 - task 4

'''
Zadanie
W którym miesiącu 2024 łączny przychód w tym roku przekroczył 30 000?

Nazwę miesiąca w formie YYYY-MM (np. 2024-01) przypisz do zmiennej searched_month.

*Rozwiązanie wymaga małego researchu i samodzielnego znalezienia funkcji, których nie przerabialiśmy na nagraniach.
'''


import pandas as pd
df = pd.read_csv("orders.csv")
df.head()

df['month'] = pd.to_datetime(df['order_date']).dt.to_period('M')
df = df.sort_values('order_date')
df['cum_sum'] = df['amount'].cumsum()

searched_month = None
for index, row in df.iterrows():
    if row['cum_sum'] >= 30000:
        searched_month = str(row['month'])
        break

print(searched_month)