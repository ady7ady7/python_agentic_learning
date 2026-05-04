# Week 1, Day 3: OOP Fundamentals - Classes, Objects & Methods

**Learning Objectives:**
- Understand what classes are and why we use them
- Master `__init__` and the `self` parameter
- Distinguish between instance attributes and class attributes
- Understand methods vs functions
- Create professional, well-structured classes

---

## Procedural vs Object-Oriented Approach (PCAP Theory)

### The Procedural World

In procedural programming, there are **two separate worlds**:

| World | Contains | Example |
|-------|----------|---------|
| **Data** | Variables of different kinds | `balance = 1000`, `owner = "Alice"` |
| **Code** | Functions grouped into modules | `def deposit(account_id, amount)` |

**Key limitation:** Functions can use (and abuse) data, but data cannot use functions. There's nothing stopping `math.sin(bank_balance)` — the function has no idea what the data represents.

```python
# Procedural: data and code live separately
balance = 1000
owner = "Alice"

def deposit(amount):
    global balance
    balance += amount     # function manipulates disconnected data

deposit(500)              # works, but who does this belong to?
```

### The Object-Oriented World

OOP **merges data and code** into a single unit: the **class**.

```python
# OOP: data and code live together inside the object
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # data
        self.balance = balance    # data

    def deposit(self, amount):    # code that BELONGS to the data
        self.balance += amount

account = BankAccount("Alice", 1000)
account.deposit(500)              # the object controls its own data
```

### Core OOP Vocabulary

| Term | Meaning | Example |
|------|---------|---------|
| **Class** | A recipe/blueprint for creating objects | `class BankAccount:` |
| **Object** | An incarnation of a class (like a cheesecake from a recipe) | `account = BankAccount(...)` |
| **Attribute/Property** | A trait the object has (data) | `self.balance`, `self.owner` |
| **Method** | An activity the object can perform (code) | `def deposit(self, amount)` |
| **Inheritance** | New classes built from existing ones, inheriting + extending | `class SavingsAccount(BankAccount)` |
| **Encapsulation** | Object protects its data from unauthorized modification | `self.__balance` (private) |

### Naming Conventions & Quick Distinctions

**What's what:**
- **Attribute** = data stored on an object (`self.balance = 1000`) — accessed without `()`
- **Parameter** = variable in a function/method definition (`def deposit(self, amount)`) — `amount` is the parameter
- **Method** = function that belongs to a class (`def deposit(self, amount)`) — called with `()`, has `self`

**Naming rules:**
- **Classes:** `PascalCase` — `BankAccount`, `PositionManager`
- **Objects, attributes, methods:** `snake_case` — `my_account`, `self.entry_price`, `def calculate_pnl()`
- **Constants:** `UPPER_CASE` — `MAX_POSITIONS = 10`
- **Private:** `_protected`, `__private` — `self._ticker`, `self.__pnl`

### Why This Matters

1. **Data protection:** Objects control access to their own data — no random function can corrupt it
2. **No border between data and code:** They live as one inside objects
3. **Inheritance:** Recipes (classes) can be modified to create more specific versions without rewriting everything
4. **Real-world modeling:** OOP reflects real relationships — a `Position` HAS a `ticker`, CAN `calculate_pnl()`

> **PCAP Exam Note:** The exam tests understanding of WHY OOP exists, not just syntax. Know the difference: procedural = data and code are separate; OOP = data and code are enclosed together in classes.

---

## Why Object-Oriented Programming?

**The Problem with Functions Alone:**

```python
"""Example: Managing bank accounts with just functions (messy!)."""

# Account data stored separately - easy to lose sync
account_balances = {}
account_owners = {}
account_types = {}


def create_account(account_id: str, owner: str, initial_balance: float) -> None:
    """Create a new account - data scattered across dictionaries."""
    account_balances[account_id] = initial_balance
    account_owners[account_id] = owner
    account_types[account_id] = "checking"


def deposit(account_id: str, amount: float) -> None:
    """Deposit money - have to manually validate account exists."""
    if account_id in account_balances:
        account_balances[account_id] += amount
    else:
        print("Account not found")


def get_balance(account_id: str) -> float:
    """Get balance - error-prone lookups."""
    return account_balances.get(account_id, 0.0)


# Problems:
# 1. Data is scattered (balances, owners, types in separate dicts)
# 2. No validation (can set negative balance)
# 3. Hard to maintain (add new field = update 5+ functions)
# 4. No encapsulation (anyone can modify account_balances directly)
```

**The OOP Solution: Bundle Data + Behavior Together**

```python
"""Example: Bank account using a class (clean!)."""


class BankAccount:
    """
    Represents a bank account with balance and operations.

    Attributes:
        owner: Account holder's name.
        balance: Current account balance.
        account_type: Type of account (checking, savings).
    """

    def __init__(self, owner: str, initial_balance: float) -> None:
        """Initialize a new bank account."""
        self.owner = owner
        self.balance = initial_balance
        self.account_type = "checking"

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive")

    def get_balance(self) -> float:
        """Return current balance."""
        return self.balance


# Usage - much cleaner!
account = BankAccount("Alice", 1000.0)
account.deposit(500.0)  # Deposited $500.00. New balance: $1500.00
print(account.get_balance())  # 1500.0
```

**Why Classes Win:**
1. **Encapsulation:** Data (balance, owner) and behavior (deposit, withdraw) are bundled together
2. **Validation:** The class controls how data is modified
3. **Reusability:** Create multiple accounts easily: `account1 = BankAccount(...)`, `account2 = BankAccount(...)`
4. **Maintainability:** Add a new feature (e.g., interest rate) in ONE place

---

## 1. Classes vs Objects: The Blueprint Analogy

**Class:** A blueprint/template for creating objects
**Object (Instance):** An actual entity created from the class

```python
"""Understanding classes vs objects."""


class Car:
    """Blueprint for creating car objects."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize a new car."""
        self.make = make
        self.model = model
        self.year = year

    def describe(self) -> str:
        """Return a description of the car."""
        return f"{self.year} {self.make} {self.model}"


# Car is the CLASS (blueprint)
# car1, car2 are OBJECTS (instances)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(car1.describe())  # "2020 Toyota Camry"
print(car2.describe())  # "2021 Honda Civic"

# Each object has its own data
print(car1.make)  # "Toyota"
print(car2.make)  # "Honda"
```

**Key Insight:** You can create MANY objects from ONE class, each with different data.

---

## 2. The `__init__` Method (Constructor)

**Purpose:** Initialize new objects with starting values

```python
"""Understanding __init__ - the constructor."""


class Player:
    """Represents a game player."""

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Initialize a new player.

        Args:
            name: Player's name.
            health: Starting health (default 100).
        """
        self.name = name
        self.health = health
        self.score = 0  # Always starts at 0
        print(f"Player {name} created with {health} health")


# __init__ is called automatically when you create an object
player1 = Player("Alice")  # Player Alice created with 100 health
player2 = Player("Bob", 150)  # Player Bob created with 150 health

print(player1.name)    # "Alice"
print(player1.health)  # 100
print(player2.health)  # 150
```

**Critical PCAP Concepts:**
- `__init__` runs **automatically** when you create an object: `obj = ClassName()`
- First parameter is **always** `self` (represents the object being created)
- You can have default parameters: `health: int = 100`
- `__init__` typically has `-> None` return type (doesn't return anything)

---

## 3. Understanding `self`: The Object Reference

**What is `self`?**
- `self` refers to the **current object** (the instance)
- It's how methods access the object's own data
- Always the **first parameter** in instance methods
- Python passes it **automatically** (you don't provide it when calling)

```python
"""Understanding self - the object reference."""


class Counter:
    """A simple counter."""

    def __init__(self, start: int = 0) -> None:
        """Initialize counter with starting value."""
        self.value = start  # self.value belongs to THIS object

    def increment(self) -> None:
        """Increase counter by 1."""
        self.value += 1  # Access THIS object's value

    def get_value(self) -> int:
        """Return current value."""
        return self.value  # Return THIS object's value


# Create two separate counters
counter1 = Counter(0)
counter2 = Counter(10)

counter1.increment()  # Python automatically passes counter1 as self
counter1.increment()

counter2.increment()

print(counter1.get_value())  # 2 (counter1's value)
print(counter2.get_value())  # 11 (counter2's value)
```

**Visualization of what happens:**
```python
counter1.increment()
# Python internally does: Counter.increment(counter1)
# Inside increment(), self = counter1
# self.value += 1  becomes  counter1.value += 1
```

**PCAP Trap:** Forgetting `self` in method definitions

```python
class Broken:
    def __init__(self, value):
        self.value = value

    # WRONG - forgot self!
    def get_value() -> int:  # Missing self parameter
        return self.value  # NameError: self is not defined


# Correct:
class Fixed:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:  # ✅ self is first parameter
        return self.value
```

---

## 4. Instance Attributes vs Class Attributes

**Instance Attributes:** Belong to a **specific object** (each object has its own copy)
**Class Attributes:** Shared by **all objects** of the class

```python
"""Instance attributes vs class attributes."""


class Dog:
    """Represents a dog."""

    # CLASS ATTRIBUTE - shared by all dogs
    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        """Initialize a dog."""
        # INSTANCE ATTRIBUTES - unique to each dog
        self.name = name
        self.age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Instance attributes - different for each dog
print(dog1.name)  # "Buddy"
print(dog2.name)  # "Max"

# Class attribute - same for all dogs
print(dog1.species)  # "Canis familiaris"
print(dog2.species)  # "Canis familiaris"

# Modifying class attribute affects ALL instances
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # "Canis lupus familiaris"
print(dog2.species)  # "Canis lupus familiaris"
```

**When to Use Which:**
- **Instance attributes** (with `self.`): Data that varies per object (name, balance, position)
- **Class attributes** (without `self.`): Constants or defaults shared by all objects (species, max_speed, default_color)

**PCAP Example:**

```python
"""Tracking total number of objects created."""


class Employee:
    """Employee with automatic ID assignment."""

    # Class attribute - shared counter
    total_employees = 0

    def __init__(self, name: str) -> None:
        """Initialize employee and assign ID."""
        self.name = name  # Instance attribute
        Employee.total_employees += 1  # Increment class attribute
        self.employee_id = Employee.total_employees  # Unique ID


emp1 = Employee("Alice")
emp2 = Employee("Bob")
emp3 = Employee("Charlie")

print(emp1.employee_id)  # 1
print(emp2.employee_id)  # 2
print(emp3.employee_id)  # 3
print(Employee.total_employees)  # 3
```

---

## 5. Methods vs Functions

**Function:** Standalone, called directly: `result = my_function(arg)`
**Method:** Belongs to a class, called on an object: `result = obj.my_method(arg)`

```python
"""Methods vs functions."""


# FUNCTION - standalone
def calculate_area(width: float, height: float) -> float:
    """Calculate rectangle area (function)."""
    return width * height


# CLASS WITH METHODS
class Rectangle:
    """Rectangle with dimensions."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle."""
        self.width = width
        self.height = height

    # METHOD - belongs to the class, has access to self
    def calculate_area(self) -> float:
        """Calculate area using object's dimensions."""
        return self.width * self.height

    def is_square(self) -> bool:
        """Check if rectangle is a square."""
        return self.width == self.height


# Function usage
area1 = calculate_area(5, 10)  # 50

# Method usage
rect = Rectangle(5, 10)
area2 = rect.calculate_area()  # 50 - method has access to self.width, self.height
print(rect.is_square())  # False
```

**Key Differences:**
- Methods have `self` as first parameter (access to object's data)
- Methods are called on objects: `obj.method()`
- Functions are called standalone: `function()`

---

## 6. Practical Example: OHLC Candle Class

```python
"""Professional class for representing OHLC candles."""

from typing import Optional


class OHLCCandle:
    """
    Represents a single OHLC (Open, High, Low, Close) price candle.

    Attributes:
        timestamp: Time of the candle.
        ticker: Trading symbol (e.g., "EURUSD").
        open: Opening price.
        high: Highest price during period.
        low: Lowest price during period.
        close: Closing price.
        volume: Trading volume.
    """

    def __init__(
        self,
        timestamp: str,
        ticker: str,
        open_price: float,
        high: float,
        low: float,
        close: float,
        volume: int
    ) -> None:
        """Initialize OHLC candle with validation."""
        self.timestamp = timestamp
        self.ticker = ticker
        self.open = open_price
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def is_valid(self) -> bool:
        """
        Validate OHLC integrity.

        Returns:
            True if high >= low and all prices are positive.
        """
        if self.high < self.low:
            return False
        if any(price < 0 for price in [self.open, self.high, self.low, self.close]):
            return False
        return True

    def is_bullish(self) -> bool:
        """Check if candle closed higher than it opened."""
        return self.close > self.open

    def get_body_size(self) -> float:
        """Calculate candle body size (absolute difference open-close)."""
        return abs(self.close - self.open)

    def get_range(self) -> float:
        """Calculate candle range (high - low)."""
        return self.high - self.low

    def __str__(self) -> str:
        """Return string representation for printing."""
        return f"{self.ticker} [{self.timestamp}]: O={self.open:.2f} H={self.high:.2f} L={self.low:.2f} C={self.close:.2f}"


# Usage
candle = OHLCCandle(
    timestamp="2024-01-01 09:00:00",
    ticker="EURUSD",
    open_price=100.50,
    high=101.20,
    low=100.10,
    close=100.80,
    volume=15000
)

print(candle)  # EURUSD [2024-01-01 09:00:00]: O=100.50 H=101.20 L=100.10 C=100.80
print(f"Valid: {candle.is_valid()}")  # True
print(f"Bullish: {candle.is_bullish()}")  # True
print(f"Body size: {candle.get_body_size():.2f}")  # 0.30
print(f"Range: {candle.get_range():.2f}")  # 1.10
```

---

## PCAP TRAPS & GOTCHAS

**Trap 1: Modifying Mutable Class Attributes**

```python
"""DANGEROUS: Mutable class attributes are shared!"""


class ShoppingCart:
    """Shopping cart - BROKEN IMPLEMENTATION."""

    items = []  # CLASS ATTRIBUTE - shared by ALL carts!

    def __init__(self, customer: str) -> None:
        """Initialize cart."""
        self.customer = customer

    def add_item(self, item: str) -> None:
        """Add item to cart."""
        self.items.append(item)


cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

cart1.add_item("Laptop")
cart2.add_item("Phone")

print(cart1.items)  # ['Laptop', 'Phone'] - SURPRISE! Alice sees Bob's items
print(cart2.items)  # ['Laptop', 'Phone'] - Both share the same list!
```

**FIX: Use instance attributes for mutable data**

```python
"""CORRECT: Each cart has its own items list."""


class ShoppingCart:
    """Shopping cart - CORRECT IMPLEMENTATION."""

    def __init__(self, customer: str) -> None:
        """Initialize cart with empty items list."""
        self.customer = customer
        self.items = []  # Instance attribute - unique to each cart

    def add_item(self, item: str) -> None:
        """Add item to cart."""
        self.items.append(item)


cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

cart1.add_item("Laptop")
cart2.add_item("Phone")

print(cart1.items)  # ['Laptop'] - Correct!
print(cart2.items)  # ['Phone'] - Correct!
```

---

**Trap 2: Forgetting `self` When Accessing Attributes**

```python
"""Common mistake: Forgetting self prefix."""


class Temperature:
    """Temperature converter - common mistakes."""

    def __init__(self, celsius: float) -> None:
        """Initialize with Celsius temperature."""
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """Convert to Fahrenheit - WRONG."""
        return celsius * 9/5 + 32  # NameError: celsius not defined
        # Should be: self.celsius


# CORRECT VERSION:
class Temperature:
    """Temperature converter - correct."""

    def __init__(self, celsius: float) -> None:
        """Initialize with Celsius temperature."""
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """Convert to Fahrenheit."""
        return self.celsius * 9/5 + 32  # ✅ Use self.celsius
```

---

**Trap 3: `__init__` Return Value**

```python
"""PCAP Trap: __init__ must not return a value."""


class Person:
    def __init__(self, name: str) -> None:  # ✅ Return type is None
        self.name = name
        # return self  # WRONG! TypeError: __init__() should return None


# __init__ implicitly returns the new object
# You never explicitly return from __init__
```

---

**Trap 4: Class Attributes as Default Arguments**

```python
"""Subtle bug: Using class attribute in method signature."""


class Logger:
    """Logger with timestamp - TRICKY BEHAVIOR."""

    log_count = 0  # Class attribute

    def __init__(self) -> None:
        """Initialize logger."""
        pass

    def log(self, message: str, count: int = log_count) -> None:
        """
        Log message with count.

        TRAP: Default argument is evaluated at function DEFINITION time,
        not call time! count will always be 0.
        """
        print(f"[{count}] {message}")


logger = Logger()
Logger.log_count = 5
logger.log("Test")  # [0] Test - SURPRISE! Uses 0, not 5


# CORRECT: Access class attribute inside method
class Logger:
    """Logger - correct implementation."""

    log_count = 0

    def log(self, message: str) -> None:
        """Log message with current count."""
        print(f"[{Logger.log_count}] {message}")
        Logger.log_count += 1
```

---

## Exam Tips

**Critical Concepts for PCAP:**

1. **`self` is mandatory** as the first parameter of instance methods
2. **`__init__` is called automatically** when creating an object
3. **Instance attributes** (`self.x`) vs **class attributes** (defined outside methods)
4. **Mutable class attributes** are shared by all instances (common trap!)
5. **Methods** vs **functions**: Methods have `self`, functions don't

**Common PCAP Questions:**
- "What is the output?" - testing shared class attributes
- "What happens when...?" - testing `self` understanding
- Predict behavior when modifying class vs instance attributes
- Identify bugs in `__init__` methods (missing `self`, wrong return type)

**PCAP Multiple Choice Pattern:**
```python
class Test:
    value = 10  # Class attribute

    def __init__(self):
        self.value = 20  # Instance attribute (shadows class attribute)

obj = Test()
print(obj.value)  # What prints? Answer: 20 (instance attribute shadows class)
print(Test.value)  # What prints? Answer: 10 (class attribute unchanged)
```

---

**Next Steps:**
Now that you understand OOP fundamentals, you're ready to:
1. Build the `DataLoader` class properly (you already started!)
2. Create `Position` and `Trade` classes for the AlgoBacktest project
3. Learn inheritance and polymorphism (Week 2)

---
