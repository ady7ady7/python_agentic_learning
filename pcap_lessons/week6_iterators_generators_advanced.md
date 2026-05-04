# Week 6: The Iterator Protocol, Advanced Generators & `__new__`

**PCAP Relevance:** HIGH - Iterator protocol and generator mechanics are exam favorites

**Prerequisites:** Week 3 generator basics (yield, next(), generator expressions, exhaustion)

---

## Table of Contents

| Topic | Description |
|-------|-------------|
| [The Iterator Protocol](#the-iterator-protocol) | `__iter__` and `__next__` — how for loops actually work |
| [Building Custom Iterators](#building-custom-iterators) | Making your own iterable classes |
| [iter() and next() Built-ins](#iter-and-next-built-ins) | How Python converts objects for iteration |
| [The `__new__` Method](#the-__new__-method) | Object creation vs initialization |
| [Advanced Generator Patterns](#advanced-generator-patterns) | `yield from`, chaining, pipelines |
| [Named Tuples](#named-tuples) | Lightweight data containers |
| [Generator vs Iterator vs Iterable](#generator-vs-iterator-vs-iterable) | Critical distinctions for PCAP |
| [PCAP Traps](#pcap-traps) | Exam pitfalls |

---

## The Iterator Protocol

Every time you write `for x in something`, Python uses the **iterator protocol** behind the scenes. Understanding this protocol is key to both the PCAP exam and writing professional Python.

### What Happens in a For Loop?

```python
numbers = [1, 2, 3]
for n in numbers:
    print(n)
```

Python translates this into:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)    # Step 1: Get an iterator from the object
while True:
    try:
        n = next(iterator)  # Step 2: Get next value
        print(n)
    except StopIteration:   # Step 3: Stop when exhausted
        break
```

### The Two Methods

The iterator protocol requires TWO methods:

| Method | Purpose | Who Implements It |
|--------|---------|-------------------|
| `__iter__()` | Returns the iterator object | The **iterable** (e.g., list, dict, str) |
| `__next__()` | Returns the next value, raises `StopIteration` when done | The **iterator** itself |

### Key Distinction

```python
numbers = [1, 2, 3]

# The LIST is an ITERABLE (has __iter__, but NOT __next__)
print(hasattr(numbers, '__iter__'))    # True
print(hasattr(numbers, '__next__'))    # False

# Calling iter() on it creates an ITERATOR (has BOTH)
it = iter(numbers)
print(hasattr(it, '__iter__'))         # True
print(hasattr(it, '__next__'))         # True

print(type(it))  # <class 'list_iterator'>
```

**Rule:**
- An **iterable** has `__iter__()` — you can loop over it
- An **iterator** has both `__iter__()` AND `__next__()` — it produces values one at a time

---

## Building Custom Iterators

### Example 1: Countdown Iterator

```python
class Countdown:
    """Iterator that counts down from n to 1."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self  # The iterator IS the iterable

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage:
for n in Countdown(5):
    print(n)
# Output: 5, 4, 3, 2, 1
```

**Key pattern:** When a class IS the iterator (has `__next__`), its `__iter__` returns `self`.

### Example 2: Separate Iterable and Iterator

Sometimes you want the iterable and iterator to be **separate objects**. This lets you iterate multiple times:

```python
class NumberRange:
    """Iterable that can be iterated multiple times."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        # Return a NEW iterator each time
        return NumberRangeIterator(self.start, self.end)


class NumberRangeIterator:
    """Iterator for NumberRange."""

    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Now you CAN iterate multiple times:
nums = NumberRange(1, 4)

for n in nums:
    print(n)  # 1, 2, 3

for n in nums:
    print(n)  # 1, 2, 3 again! (new iterator created)
```

### Why Two Classes?

| Pattern | Re-iterable? | Example |
|---------|-------------|---------|
| Single class (returns `self`) | NO - exhausted after one pass | Generator objects |
| Separate iterable + iterator | YES - fresh iterator each time | Lists, dicts, strings |

This is exactly why generators can only be iterated once!

```python
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] - exhausted!

# But a list:
lst = [0, 1, 2]
print(list(lst))  # [0, 1, 2]
print(list(lst))  # [0, 1, 2] - works again!
```

---

## iter() and next() Built-ins

### iter() with Two Arguments

`iter()` has a lesser-known two-argument form:

```python
# iter(callable, sentinel) — calls callable repeatedly until sentinel is returned
import random

# Roll a die until you get a 6
rolls = iter(lambda: random.randint(1, 6), 6)
for roll in rolls:
    print(roll)  # Prints random numbers 1-5, stops when 6 is rolled
```

**How it works:** `iter(func, sentinel)` calls `func()` repeatedly. When the result equals `sentinel`, it raises `StopIteration`.

### next() with Default

```python
gen = (x for x in [1, 2])

print(next(gen))          # 1
print(next(gen))          # 2
print(next(gen, 'DONE'))  # 'DONE' (instead of StopIteration!)
print(next(gen, 'DONE'))  # 'DONE'
```

**Useful pattern:** `next(iterator, default)` avoids `StopIteration` exceptions.

---

## The `__new__` Method

### What Is `__new__`?

In Python, object creation is a **two-step process**:

```
Step 1: __new__()  → Creates the object (allocates memory)
Step 2: __init__() → Initializes the object (sets attributes)
```

Most of the time you only override `__init__`. But `__new__` is there behind the scenes:

```python
class MyClass:
    def __new__(cls):
        print(f"Creating instance of {cls.__name__}")
        instance = super().__new__(cls)  # Actually creates the object
        return instance

    def __init__(self):
        print("Initializing instance")
        self.value = 42

obj = MyClass()
# Output:
# Creating instance of MyClass
# Initializing instance
```

### `__new__` vs `__init__`

| Feature | `__new__` | `__init__` |
|---------|-----------|------------|
| Purpose | Create the object | Initialize the object |
| First parameter | `cls` (the class) | `self` (the instance) |
| Must return | The new instance | `None` (implicit) |
| Called | BEFORE `__init__` | AFTER `__new__` |
| Typical use | Rare (singletons, immutables) | Common (setting attributes) |

### Why `__new__` Exists

`__new__` is a **class method** (receives `cls`). It's needed for:

1. **Controlling object creation** (e.g., Singleton pattern)
2. **Subclassing immutable types** (str, int, tuple)

### The Singleton Pattern

A singleton ensures only ONE instance of a class ever exists:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True — same object!
print(id(a) == id(b))  # True
```

**How it works:**
1. First call: `_instance` is None, so `super().__new__(cls)` creates a new object and stores it
2. Second call: `_instance` already exists, so it returns the SAME object
3. Result: `a` and `b` point to the exact same object in memory

### Subclassing Immutable Types

You can't modify immutables in `__init__` because the object already exists. Use `__new__`:

```python
class UpperStr(str):
    """A string that's always uppercase."""

    def __new__(cls, value):
        # Must set the value in __new__ because str is immutable
        instance = super().__new__(cls, value.upper())
        return instance

s = UpperStr("hello")
print(s)        # HELLO
print(type(s))  # <class '__main__.UpperStr'>
```

### PCAP Key Points for `__new__`

1. `__new__` is called BEFORE `__init__`
2. `__new__` receives `cls` (class), `__init__` receives `self` (instance)
3. `__new__` MUST return an instance (or `__init__` won't run)
4. If `__new__` returns an instance of a DIFFERENT class, `__init__` is NOT called

---

## Advanced Generator Patterns

### yield from — Delegating to Sub-generators

`yield from` delegates iteration to another iterable:

```python
# WITHOUT yield from
def chain_manual(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# WITH yield from (cleaner!)
def chain(*iterables):
    for iterable in iterables:
        yield from iterable

# Usage:
result = list(chain([1, 2], [3, 4], [5]))
print(result)  # [1, 2, 3, 4, 5]
```

### yield from with Generators

```python
def numbers():
    yield from range(3)     # 0, 1, 2
    yield from range(10, 13)  # 10, 11, 12

print(list(numbers()))  # [0, 1, 2, 10, 11, 12]
```

### Generator Pipelines

Chain generators together like Unix pipes:

```python
def read_prices(data):
    """Stage 1: Yield each price."""
    for price in data:
        yield price

def filter_positive(prices):
    """Stage 2: Keep only positive changes."""
    for price in prices:
        if price > 0:
            yield price

def format_output(prices):
    """Stage 3: Format for display."""
    for price in prices:
        yield f"${price:.2f}"

# Pipeline: data → filter → format
raw_data = [10.5, -2.3, 8.1, -0.5, 15.2]
pipeline = format_output(filter_positive(read_prices(raw_data)))

for item in pipeline:
    print(item)
# $10.50
# $8.10
# $15.20
```

**Why pipelines matter:** Each stage processes ONE item at a time. Even with millions of data points, memory usage stays constant.

---

## Named Tuples

### What Are Named Tuples?

Named tuples are immutable containers where fields have **names** instead of just indices:

```python
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p = Point(3, 4)
print(p.x)      # 3 (access by name)
print(p[0])     # 3 (access by index — still a tuple!)
print(p)        # Point(x=3, y=4)
```

### Named Tuple for Trading Data

```python
from collections import namedtuple

# Define an OHLC candle
Candle = namedtuple('Candle', ['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Create a candle
c = Candle('2026-02-09', 24500, 24600, 24450, 24580, 1200)
print(c.close)       # 24580
print(c.timestamp)   # 2026-02-09
```

### Named Tuples Are Immutable

```python
p = Point(3, 4)
p.x = 10  # AttributeError: can't set attribute
```

### Named Tuple + Generator = Event-Driven Simulation

This is the pattern you'll use in the project:

```python
from collections import namedtuple
import pandas as pd

PriceTick = namedtuple('PriceTick', ['timestamp', 'price'])

def price_stream(df: pd.DataFrame):
    """Convert DataFrame rows to a generator of PriceTick named tuples."""
    for _, row in df.iterrows():
        yield PriceTick(timestamp=row['timestamp'], price=row['close'])

# Usage with BacktestEngine:
# for tick in price_stream(dataframe):
#     engine.process_price(tick.price)
```

### When to Use Named Tuples vs Classes

| Use Case | Named Tuple | Class |
|----------|-------------|-------|
| Simple data container | Yes | Overkill |
| Need methods | No | Yes |
| Immutability required | Yes (built-in) | Must enforce manually |
| PCAP exam | Common question | Common question |
| Performance | Faster | Slower |

---

## Generator vs Iterator vs Iterable

This is one of the most confusing topics on PCAP. Here's the clear distinction:

### Definitions

| Term | Has `__iter__`? | Has `__next__`? | Example |
|------|----------------|----------------|---------|
| **Iterable** | Yes | No | list, dict, str, tuple, set |
| **Iterator** | Yes | Yes | list_iterator, dict_keyiterator |
| **Generator** | Yes | Yes | Generator objects (special iterators) |

### The Hierarchy

```
Iterable (has __iter__)
  └── Iterator (has __iter__ + __next__)
        └── Generator (special iterator created by yield)
```

**Every generator is an iterator. Every iterator is an iterable. But NOT every iterable is an iterator.**

### Proof in Code

```python
# List is ITERABLE but NOT an iterator
numbers = [1, 2, 3]
print(hasattr(numbers, '__iter__'))    # True  — iterable
print(hasattr(numbers, '__next__'))    # False — NOT an iterator

# iter() creates an ITERATOR from an iterable
it = iter(numbers)
print(hasattr(it, '__iter__'))         # True
print(hasattr(it, '__next__'))         # True  — IS an iterator

# Generator is also an iterator
gen = (x for x in [1, 2, 3])
print(hasattr(gen, '__iter__'))        # True
print(hasattr(gen, '__next__'))        # True  — IS an iterator
```

### PCAP Favorite: What Can You Pass to next()?

```python
# next() requires an ITERATOR (must have __next__)
next([1, 2, 3])       # TypeError! List is iterable, NOT iterator
next(iter([1, 2, 3]))  # 1 — iter() creates iterator first

# Generators work directly with next()
gen = (x for x in [1, 2, 3])
next(gen)  # 1 — generators ARE iterators
```

---

## PCAP Traps

### Trap 1: Calling next() on an Iterable (Not Iterator)

```python
numbers = [1, 2, 3]
print(next(numbers))  # TypeError: 'list' object is not an iterator

# Fix:
print(next(iter(numbers)))  # 1
```

### Trap 2: Iterator's `__iter__` Returns Self

```python
it = iter([1, 2, 3])
print(iter(it) is it)  # True — calling iter() on an iterator returns itself
```

This means you can pass an iterator to a for loop (it calls `__iter__` which returns the same iterator).

### Trap 3: Multiple iter() Calls Create Independent Iterators

```python
numbers = [1, 2, 3]
it1 = iter(numbers)
it2 = iter(numbers)

print(next(it1))  # 1
print(next(it2))  # 1 — independent!
print(next(it1))  # 2
```

But on a generator:
```python
gen = (x for x in [1, 2, 3])
it1 = iter(gen)
it2 = iter(gen)

print(it1 is it2)  # True — same object!
print(next(it1))   # 1
print(next(it2))   # 2 — NOT independent!
```

### Trap 4: `__new__` Returns Wrong Type

```python
class Weird:
    def __new__(cls):
        return 42  # Returns an int, not a Weird instance!

    def __init__(self):
        print("This never runs!")

obj = Weird()
print(obj)        # 42
print(type(obj))  # <class 'int'>
```

If `__new__` returns an instance of a **different** class, `__init__` is NOT called.

### Trap 5: Generator with return Value

```python
def gen():
    yield 1
    yield 2
    return "done"  # This becomes the StopIteration value

g = gen()
print(next(g))  # 1
print(next(g))  # 2

try:
    next(g)
except StopIteration as e:
    print(e.value)  # "done"
```

The `return` value in a generator is stored in the `StopIteration` exception's `.value` attribute. You can NOT access it via a regular for loop.

### Trap 6: yield from Passes Through StopIteration

```python
def inner():
    yield 1
    yield 2
    return "finished"

def outer():
    result = yield from inner()  # result = "finished"
    print(f"Inner returned: {result}")
    yield 3

print(list(outer()))
# Inner returned: finished
# [1, 2, 3]
```

`yield from` captures the sub-generator's return value.

---

## Quick Reference

| Concept | Syntax | Key Point |
|---------|--------|-----------|
| Make class iterable | `__iter__()` + `__next__()` | `StopIteration` to end |
| Delegate iteration | `yield from iterable` | Cleaner than nested for |
| Named tuple | `namedtuple('Name', ['field1', 'field2'])` | Immutable, access by name |
| `__new__` | `def __new__(cls): ...` | Called BEFORE `__init__` |
| Singleton | `if cls._instance is None` | One instance ever |
| next() with default | `next(iterator, default)` | Avoids StopIteration |
| iter() two-arg | `iter(callable, sentinel)` | Calls until sentinel |

---

## Practice Checklist

After reading this lesson, you should be able to:

- [ ] Explain the difference between iterable, iterator, and generator
- [ ] Implement a class with `__iter__` and `__next__`
- [ ] Use `yield from` to delegate to sub-generators
- [ ] Explain when `__new__` is called vs `__init__`
- [ ] Implement the Singleton pattern
- [ ] Create and use named tuples
- [ ] Chain generators into a pipeline
- [ ] Predict what `next()` returns on different types

---

**Next:** Apply these concepts to create an event-driven price stream for the BacktestEngine!
