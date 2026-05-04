# Week 3: Generators & Iterators

**PCAP Relevance:** HIGH - Generators appear frequently on the exam

---

## Table of Contents

| Topic | Description | Line |
|-------|-------------|------|
| [What is a Generator?](#what-is-a-generator) | Core concept explanation | ~20 |
| [yield vs return](#yield-vs-return) | Key difference | ~60 |
| [Creating Generators](#creating-generators) | Step-by-step examples | ~100 |
| [Generator Expressions](#generator-expressions) | Compact syntax | ~180 |
| [Memory Efficiency](#memory-efficiency) | Why generators matter | ~220 |
| [Common Patterns](#common-patterns) | Practical use cases | ~280 |
| [PCAP Traps](#pcap-traps) | Exam pitfalls | ~350 |

---

## What is a Generator?

A **generator** is a special type of function that produces a sequence of values **one at a time**, instead of creating them all at once.

### The Problem Generators Solve

Imagine you need to process 1 million numbers:

```python
# WITHOUT generators - creates ALL numbers in memory at once
numbers = [x for x in range(1_000_000)]  # 1 million items in RAM!
for n in numbers:
    process(n)

# WITH generators - creates ONE number at a time
numbers = (x for x in range(1_000_000))  # Almost no memory used!
for n in numbers:
    process(n)
```

**Key insight:** A generator doesn't store all values - it **calculates each value when you ask for it**.

---

## yield vs return

The `yield` keyword is what makes a function a generator.

### `return` - Ends the Function

```python
def give_numbers():
    return 1
    return 2  # Never runs - function already ended
    return 3

result = give_numbers()
print(result)  # 1
print(type(result))  # <class 'int'>
```

### `yield` - Pauses the Function

```python
def give_numbers():
    yield 1  # Pause here, give 1
    yield 2  # When asked again, give 2
    yield 3  # When asked again, give 3

result = give_numbers()
print(result)  # <generator object give_numbers at 0x...>
print(type(result))  # <class 'generator'>
```

**Critical difference:**
- `return` → Function **ends**, returns ONE value
- `yield` → Function **pauses**, can produce MANY values

---

## Creating Generators

### Step 1: Basic Generator Function

```python
def count_to_three():
    yield 1
    yield 2
    yield 3

# Create the generator object
gen = count_to_three()
print(type(gen))  # <class 'generator'>
```

### Step 2: Getting Values with `next()`

```python
gen = count_to_three()

print(next(gen))  # 1 (function runs until first yield)
print(next(gen))  # 2 (function resumes, runs until second yield)
print(next(gen))  # 3 (function resumes, runs until third yield)
print(next(gen))  # StopIteration exception! (no more yields)
```

**What happens internally:**

```
next(gen) called → function runs → hits "yield 1" → PAUSES → returns 1
next(gen) called → function RESUMES after yield 1 → hits "yield 2" → PAUSES → returns 2
next(gen) called → function RESUMES after yield 2 → hits "yield 3" → PAUSES → returns 3
next(gen) called → function RESUMES after yield 3 → function ENDS → StopIteration
```

### Step 3: Using in a For Loop (Recommended)

```python
def count_to_three():
    yield 1
    yield 2
    yield 3

# For loop automatically handles StopIteration
for number in count_to_three():
    print(number)

# Output:
# 1
# 2
# 3
```

The `for` loop calls `next()` internally and stops when `StopIteration` is raised.

### Step 4: Generator with a Loop Inside

```python
def count_up_to(n):
    """Generate numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage
for num in count_up_to(5):
    print(num)

# Output: 1, 2, 3, 4, 5
```

### Step 5: Converting Generator to List

```python
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

# Generator object
gen = count_up_to(5)

# Convert to list (consumes the generator)
numbers = list(gen)
print(numbers)  # [1, 2, 3, 4, 5]

# Generator is now EXHAUSTED
print(list(gen))  # [] - empty! Already consumed.
```

**Warning:** Converting to list defeats the memory benefit - all values are created at once.

---

## Generator Expressions

A compact way to create generators (similar to list comprehensions).

### List Comprehension vs Generator Expression

```python
# List comprehension - uses [ ]
squares_list = [x**2 for x in range(5)]
print(type(squares_list))  # <class 'list'>
print(squares_list)        # [0, 1, 4, 9, 16]

# Generator expression - uses ( )
squares_gen = (x**2 for x in range(5))
print(type(squares_gen))   # <class 'generator'>
print(squares_gen)         # <generator object <genexpr> at 0x...>
```

### Converting Between Them

```python
# Generator expression
gen = (x**2 for x in range(5))

# Convert to list
print(list(gen))  # [0, 1, 4, 9, 16]
```

### Syntax Comparison

| List Comprehension | Generator Expression |
|--------------------|---------------------|
| `[x for x in range(10)]` | `(x for x in range(10))` |
| `[x**2 for x in items]` | `(x**2 for x in items)` |
| `[x for x in items if x > 0]` | `(x for x in items if x > 0)` |

**The ONLY difference is `[ ]` vs `( )`**

---

## Memory Efficiency

### Why This Matters

```python
# BAD for large files - loads EVERYTHING into memory
def read_all_lines(filename):
    with open(filename) as f:
        return f.readlines()  # List of ALL lines

lines = read_all_lines("huge_file.txt")  # 10GB file = 10GB RAM!
for line in lines:
    process(line)


# GOOD - processes one line at a time
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line

for line in read_lines("huge_file.txt"):  # ~0 extra RAM
    process(line)
```

### Memory Comparison

```python
import sys

# List - stores all values
numbers_list = [x for x in range(1_000_000)]
print(sys.getsizeof(numbers_list))  # ~8,000,000 bytes (8 MB)

# Generator - stores almost nothing
numbers_gen = (x for x in range(1_000_000))
print(sys.getsizeof(numbers_gen))   # ~112 bytes (tiny!)
```

**Rule of thumb:**
- Small data → List is fine
- Large/infinite data → Use generator

---

## Common Patterns

### Pattern 1: Infinite Generator

```python
def infinite_counter(start=0):
    """Counts forever - use with care!"""
    n = start
    while True:
        yield n
        n += 1

# Usage (must break or you'll loop forever)
for i in infinite_counter():
    print(i)
    if i >= 5:
        break

# Output: 0, 1, 2, 3, 4, 5
```

### Pattern 2: Filtering Generator

```python
def only_positive(numbers):
    """Yield only positive numbers."""
    for n in numbers:
        if n > 0:
            yield n

data = [-2, 5, -1, 8, 0, 3]
for num in only_positive(data):
    print(num)

# Output: 5, 8, 3
```

### Pattern 3: Transforming Generator

```python
def double_all(numbers):
    """Yield each number doubled."""
    for n in numbers:
        yield n * 2

data = [1, 2, 3, 4, 5]
print(list(double_all(data)))  # [2, 4, 6, 8, 10]
```

### Pattern 4: Generator for Trading Data

```python
def price_ticks(start_price, num_ticks, volatility=0.01):
    """
    Generate simulated price movements.

    Args:
        start_price: Starting price
        num_ticks: Number of prices to generate
        volatility: Max percentage change per tick

    Yields:
        float: Each new price
    """
    import random

    price = start_price
    for _ in range(num_ticks):
        change = random.uniform(-volatility, volatility)
        price = price * (1 + change)
        price = max(price, 0.01)  # Never go below 0.01
        yield price

# Usage
for tick in price_ticks(100.0, 5, 0.02):
    print(f"${tick:.2f}")
```

---

## PCAP Traps

### Trap 1: Generator is Exhausted After One Use

```python
gen = (x for x in range(3))

print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] - EMPTY! Already consumed!
```

**Fix:** Create a new generator if you need to iterate again.

### Trap 2: StopIteration on Exhausted Generator

```python
def simple():
    yield 1
    yield 2

gen = simple()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # StopIteration exception!
```

**PCAP Question:** "What exception is raised when calling `next()` on an exhausted generator?"
**Answer:** `StopIteration`

### Trap 3: Generator Function vs Generator Object

```python
def my_gen():
    yield 1

# This is the FUNCTION
print(type(my_gen))      # <class 'function'>

# This is the GENERATOR OBJECT (created by calling the function)
print(type(my_gen()))    # <class 'generator'>
```

### Trap 4: yield Creates a Generator, Not a List

```python
def gen():
    yield 1
    yield 2
    yield 3

result = gen()
print(result)  # <generator object gen at 0x...>  (NOT [1, 2, 3])

# To get a list:
result = list(gen())
print(result)  # [1, 2, 3]
```

### Trap 5: Generator Expression Needs Parentheses

```python
# In a function call, parentheses can be omitted
sum(x**2 for x in range(5))  # OK - no extra ()

# But for assignment, you need them
squares = (x**2 for x in range(5))  # OK
squares = x**2 for x in range(5)    # SyntaxError!
```

---

## Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| Generator function | `def func(): yield x` | `def gen(): yield 1` |
| Generator expression | `(expr for x in iterable)` | `(x**2 for x in range(5))` |
| Get next value | `next(gen)` | `next(my_gen)` → 1 |
| Convert to list | `list(gen)` | `list(gen)` → [1, 2, 3] |
| Exhausted exception | `StopIteration` | Raised when no more values |
| Check type | `type(gen)` | `<class 'generator'>` |

---

## Practice Problems

**Problem 1:** What's the output?
```python
def nums():
    yield 1
    yield 2

g = nums()
print(next(g) + next(g))
```
<details>
<summary>Answer</summary>
3 (1 + 2)
</details>

**Problem 2:** What's the output?
```python
gen = (x for x in [1, 2, 3])
print(type(gen))
```
<details>
<summary>Answer</summary>
<class 'generator'>
</details>

**Problem 3:** What happens?
```python
def gen():
    yield 1

g = gen()
list(g)
list(g)  # What's returned here?
```
<details>
<summary>Answer</summary>
[] (empty list - generator was exhausted)
</details>

---

**Next:** Now that you understand generators, you can implement memory-efficient iterators for your TradeManager class!
