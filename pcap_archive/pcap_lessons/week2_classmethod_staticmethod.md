# Week 2: @classmethod and @staticmethod

This lesson covers the two special method decorators in Python: `@classmethod` and `@staticmethod`.

---

## Regular Methods (Review)

Regular methods receive `self` (the instance) as the first parameter:

```python
class Trade:
    def __init__(self, ticker: str, price: float):
        self.ticker = ticker
        self.price = price

    def get_info(self):  # Regular method - receives self
        return f"{self.ticker} @ {self.price}"

# Usage
trade = Trade("AAPL", 150.0)
print(trade.get_info())  # "AAPL @ 150.0"
```

**Key point:** Regular methods need an instance to be called.

---

## @classmethod

A class method receives the **class** (not an instance) as the first parameter, conventionally named `cls`.

```python
class Position:
    default_risk_percent = 1.0  # Class attribute

    def __init__(self, ticker: str, quantity: float):
        self.ticker = ticker
        self.quantity = quantity

    @classmethod
    def calculate_position_size(cls, account_balance: float,
                                 entry_price: float,
                                 stop_loss: float) -> float:
        """Calculate position size based on default risk."""
        risk_dollars = account_balance * (cls.default_risk_percent / 100)
        distance = abs(entry_price - stop_loss)
        if distance == 0:
            return 0
        return risk_dollars / distance

# Usage - called on the CLASS, not an instance
size = Position.calculate_position_size(10000, 50.0, 48.0)
print(size)  # 50.0
```

### What @classmethod receives:

| Parameter | What it is | Can access |
|-----------|------------|------------|
| `cls` | The class itself (e.g., `Position`) | Class attributes, other class methods |

### What @classmethod CANNOT access:

- `self` - there's no instance!
- Instance attributes (like `self.ticker`)

```python
@classmethod
def broken_method(cls):
    return cls.ticker  # ERROR! 'ticker' is instance attribute, not class attribute
```

### Common use cases for @classmethod:

**1. Alternative constructors (factory methods):**

```python
class Trade:
    def __init__(self, ticker: str, side: str, price: float):
        self.ticker = ticker
        self.side = side
        self.price = price

    @classmethod
    def from_string(cls, trade_string: str):
        """Create Trade from string like 'AAPL,BUY,150.0'"""
        parts = trade_string.split(",")
        return cls(parts[0], parts[1], float(parts[2]))

    @classmethod
    def buy(cls, ticker: str, price: float):
        """Shortcut for creating BUY trades."""
        return cls(ticker, "BUY", price)

# Usage
trade1 = Trade("AAPL", "BUY", 150.0)           # Regular constructor
trade2 = Trade.from_string("GOOGL,SELL,2800")  # Alternative constructor
trade3 = Trade.buy("MSFT", 300.0)              # Another alternative
```

**2. Accessing/modifying class attributes:**

```python
class Strategy:
    active_strategies = 0  # Class attribute - shared by all instances

    def __init__(self, name: str):
        self.name = name
        Strategy.active_strategies += 1

    @classmethod
    def get_active_count(cls) -> int:
        """Return number of active strategies."""
        return cls.active_strategies

    @classmethod
    def reset_count(cls):
        """Reset the counter."""
        cls.active_strategies = 0

# Usage
s1 = Strategy("MA")
s2 = Strategy("Level Cross")
print(Strategy.get_active_count())  # 2
Strategy.reset_count()
print(Strategy.get_active_count())  # 0
```

---

## @staticmethod

A static method receives **nothing automatically** - no `self`, no `cls`. It's just a regular function that lives inside a class for organizational purposes.

```python
class RiskCalculator:

    @staticmethod
    def validate_price(price: float) -> bool:
        """Check if price is valid (positive number)."""
        return price > 0

    @staticmethod
    def calculate_distance(entry: float, stop_loss: float) -> float:
        """Calculate distance between entry and stop loss."""
        return abs(entry - stop_loss)

# Usage - can be called on class OR instance
print(RiskCalculator.validate_price(50.0))  # True
print(RiskCalculator.validate_price(-10))   # False

calc = RiskCalculator()
print(calc.validate_price(100.0))  # Also works on instance
```

### What @staticmethod receives:

| Parameter | What it is |
|-----------|------------|
| Nothing automatically | Only explicit parameters you define |

### What @staticmethod CANNOT access:

- `self` - no instance
- `cls` - no class reference
- Instance attributes
- Class attributes (unless you hardcode the class name)

```python
@staticmethod
def broken_method():
    return cls.default_risk  # ERROR! 'cls' is not defined
    return self.ticker       # ERROR! 'self' is not defined
```

### Common use cases for @staticmethod:

**1. Utility functions that don't need class/instance data:**

```python
class DataValidator:

    @staticmethod
    def is_valid_ticker(ticker: str) -> bool:
        """Check if ticker format is valid."""
        return len(ticker) <= 5 and ticker.isalpha() and ticker.isupper()

    @staticmethod
    def format_price(price: float, decimals: int = 2) -> str:
        """Format price with specified decimal places."""
        return f"{price:.{decimals}f}"

# Usage
print(DataValidator.is_valid_ticker("AAPL"))   # True
print(DataValidator.is_valid_ticker("apple"))  # False
print(DataValidator.format_price(123.456, 2))  # "123.46"
```

**2. Grouping related functions:**

```python
class MathUtils:
    """Collection of math utilities for trading calculations."""

    @staticmethod
    def percent_change(old_value: float, new_value: float) -> float:
        """Calculate percentage change."""
        if old_value == 0:
            return 0
        return ((new_value - old_value) / old_value) * 100

    @staticmethod
    def round_to_tick(price: float, tick_size: float = 0.01) -> float:
        """Round price to nearest tick size."""
        return round(price / tick_size) * tick_size
```

---

## Comparison Table

| Feature | Regular Method | @classmethod | @staticmethod |
|---------|---------------|--------------|---------------|
| First parameter | `self` (instance) | `cls` (class) | Nothing |
| Can access instance attributes | ✅ Yes | ❌ No | ❌ No |
| Can access class attributes | ✅ Yes (via `self.__class__` or class name) | ✅ Yes (via `cls`) | ❌ No (unless hardcoded) |
| Needs instance to call | ✅ Yes | ❌ No | ❌ No |
| Can create new instances | ✅ Yes | ✅ Yes (via `cls()`) | ⚠️ Yes (but must hardcode class name) |

---

## When to Use Which?

### Use regular method when:
- You need to access or modify instance attributes (`self.something`)
- The method operates on a specific instance

```python
def close_position(self, exit_price: float):
    self.exit_price = exit_price  # Modifies instance
    self.is_open = False
```

### Use @classmethod when:
- You need to access class attributes
- You're creating alternative constructors
- You need to create instances but want to use `cls()` (works with inheritance)

```python
@classmethod
def from_dict(cls, data: dict):
    return cls(data['ticker'], data['price'])  # Works with subclasses too!
```

### Use @staticmethod when:
- The method doesn't need `self` or `cls`
- It's a utility function that logically belongs with the class
- You could write it as a standalone function, but it makes sense to group it

```python
@staticmethod
def validate_ticker(ticker: str) -> bool:
    return len(ticker) <= 5 and ticker.isupper()
```

---

## PCAP Exam Traps

### Trap 1: Confusing cls and self

```python
class Example:
    value = 10

    @classmethod
    def class_method(cls):
        return cls.value  # ✅ Correct - uses cls

    @classmethod
    def wrong_method(cls):
        return self.value  # ❌ NameError: 'self' is not defined
```

### Trap 2: @staticmethod trying to use cls

```python
class Example:
    count = 0

    @staticmethod
    def static_method():
        return cls.count  # ❌ NameError: 'cls' is not defined
        return Example.count  # ✅ This would work (but defeats the purpose)
```

### Trap 3: Calling classmethod on instance

```python
class Counter:
    total = 0

    @classmethod
    def get_total(cls):
        return cls.total

# Both of these work!
print(Counter.get_total())  # 0 - Called on class
c = Counter()
print(c.get_total())        # 0 - Called on instance (also works!)
```

### Trap 4: @classmethod first parameter must be cls

```python
class Example:
    @classmethod
    def method(self):  # ❌ Will "work" but 'self' is actually the class!
        print(type(self))  # <class 'type'> - It's the class, not instance!
```

**Best practice:** Always name it `cls` by convention.

---

## Practice Exercise

Predict the output:

```python
class BankAccount:
    interest_rate = 0.05  # 5%

    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def add_interest(self):
        self.balance *= (1 + self.__class__.interest_rate)

# What happens?
acc = BankAccount(1000)
BankAccount.set_interest_rate(0.10)
print(BankAccount.interest_rate)  # ?
print(acc.balance)                # ?
acc.add_interest()
print(acc.balance)                # ?
print(BankAccount.validate_amount(-50))  # ?
```

<details>
<summary>Click for answer</summary>

```
0.10          # Class attribute changed by classmethod
1000          # Balance unchanged yet
1100.0        # Balance after 10% interest
False         # -50 is not > 0
```

</details>

---

## Summary

| Decorator | First Param | Use When |
|-----------|-------------|----------|
| (none) | `self` | Need instance data |
| `@classmethod` | `cls` | Need class data or alternative constructor |
| `@staticmethod` | (none) | Utility function, no class/instance needed |

**Memory trick:**
- Regular method → works on **self** (the object)
- Class method → works on **cls** (the blueprint)
- Static method → works on **nothing** (just a function in a class)
