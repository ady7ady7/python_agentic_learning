# Week 4: Lambda Functions, Closures & Functional Programming

**PCAP Relevance:** HIGH - Lambda and closures are common exam topics

---

## Table of Contents

| Topic | Description | Line |
|-------|-------------|------|
| [Lambda Functions](#lambda-functions) | Anonymous one-line functions | ~25 |
| [Lambda Syntax](#lambda-syntax) | How to write lambdas | ~50 |
| [Lambda Use Cases](#lambda-use-cases) | When to use them | ~100 |
| [map() Function](#map-function) | Apply function to all items | ~150 |
| [filter() Function](#filter-function) | Select items by condition | ~220 |
| [Closures](#closures) | Functions that remember their environment | ~290 |
| [Closure Use Cases](#closure-use-cases) | Practical applications | ~380 |
| [PCAP Traps](#pcap-traps) | Common exam pitfalls | ~430 |
| [reduce() Function](#reduce-function-from-functools) | Cumulative reduction | ~545 |
| [Decorators](#decorators-closures-in-action) | Function wrappers using closures | ~610 |
| [functools.wraps](#functoolswraps---preserving-function-metadata) | Preserving decorated function metadata | ~755 |

---

## Lambda Functions

A **lambda** is a small, anonymous function defined in a single line.

### Why "Anonymous"?

Regular functions have names:
```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8
```

Lambda functions don't need names:
```python
add = lambda a, b: a + b

result = add(3, 5)  # 8
```

Both do the same thing, but lambda is more compact.

---

## Lambda Syntax

```python
lambda parameters: expression
```

**Key rules:**
1. Starts with keyword `lambda`
2. Parameters separated by commas (no parentheses needed)
3. Single colon `:` separates parameters from expression
4. **Only ONE expression** (no statements, no `return` keyword)
5. The expression's result is automatically returned

### Examples

```python
# No parameters
greet = lambda: "Hello!"
print(greet())  # "Hello!"

# One parameter
double = lambda x: x * 2
print(double(5))  # 10

# Two parameters
add = lambda a, b: a + b
print(add(3, 4))  # 7

# With default parameter
greet = lambda name="World": f"Hello, {name}!"
print(greet())        # "Hello, World!"
print(greet("Alice")) # "Hello, Alice!"

# Conditional expression (ternary)
absolute = lambda x: x if x >= 0 else -x
print(absolute(-5))  # 5
print(absolute(3))   # 3
```

### What You CANNOT Do in Lambda

```python
# NO multiple statements
lambda x: print(x); return x  # SyntaxError!

# NO assignments
lambda x: y = x * 2  # SyntaxError!

# NO loops
lambda x: for i in x: print(i)  # SyntaxError!

# NO if statements (only ternary expressions)
lambda x: if x > 0: return x  # SyntaxError!
```

**Rule:** Lambda body must be a single expression that evaluates to a value.

---

## Lambda Use Cases

### Use Case 1: Quick Throwaway Functions

When you need a function for one-time use:

```python
# Without lambda - clutters namespace
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))

# With lambda - cleaner
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### Use Case 2: Sorting with Custom Key

```python
# Sort strings by length
words = ["apple", "pie", "banana", "kiwi"]
words.sort(key=lambda x: len(x))
print(words)  # ['pie', 'kiwi', 'apple', 'banana']

# Sort tuples by second element
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# Sort dictionaries by value
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
data.sort(key=lambda x: x['age'])
print(data)  # [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```

### Use Case 3: As Argument to Higher-Order Functions

```python
# With filter()
numbers = [1, -2, 3, -4, 5]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [1, 3, 5]

# With map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

---

## map() Function

`map(function, iterable)` applies a function to every item in an iterable.

### Basic Syntax

```python
map(function, iterable)
# Returns a map object (iterator)
```

### Examples

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# Convert to uppercase
words = ["hello", "world"]
upper = map(str.upper, words)
print(list(upper))  # ['HELLO', 'WORLD']

# Using a regular function
def add_ten(x):
    return x + 10

numbers = [1, 2, 3]
result = map(add_ten, numbers)
print(list(result))  # [11, 12, 13]
```

### map() with Multiple Iterables

```python
# Add corresponding elements
a = [1, 2, 3]
b = [10, 20, 30]
sums = map(lambda x, y: x + y, a, b)
print(list(sums))  # [11, 22, 33]

# Stops at shortest iterable
a = [1, 2, 3, 4, 5]
b = [10, 20]
sums = map(lambda x, y: x + y, a, b)
print(list(sums))  # [11, 22] - only 2 elements!
```

### map() vs List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

# Using map()
squared = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (usually preferred in Python)
squared = [x ** 2 for x in numbers]

# Both produce: [1, 4, 9, 16, 25]
```

**When to use which:**
- List comprehension: More Pythonic, easier to read
- map(): When you already have a function to apply

---

## filter() Function

`filter(function, iterable)` selects items where function returns True.

### Basic Syntax

```python
filter(function, iterable)
# Returns a filter object (iterator)
```

### Examples

```python
# Keep only positive numbers
numbers = [1, -2, 3, -4, 5, -6]
positive = filter(lambda x: x > 0, numbers)
print(list(positive))  # [1, 3, 5]

# Keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8]

# Keep non-empty strings
strings = ["hello", "", "world", "", "python"]
non_empty = filter(lambda x: x, strings)  # Empty string is falsy
print(list(non_empty))  # ['hello', 'world', 'python']

# Keep strings longer than 3 characters
words = ["hi", "hello", "bye", "goodbye"]
long_words = filter(lambda x: len(x) > 3, words)
print(list(long_words))  # ['hello', 'goodbye']
```

### filter() with None

When function is `None`, filter removes falsy values:

```python
items = [0, 1, False, 2, '', 3, None, 4]
truthy = filter(None, items)
print(list(truthy))  # [1, 2, 3, 4]
```

### filter() vs List Comprehension

```python
numbers = [1, -2, 3, -4, 5]

# Using filter()
positive = list(filter(lambda x: x > 0, numbers))

# Using list comprehension (usually preferred)
positive = [x for x in numbers if x > 0]

# Both produce: [1, 3, 5]
```

---

## Closures

A **closure** is a function that "remembers" variables from its enclosing scope, even after that scope has finished executing.

### The Problem Closures Solve

```python
# We want to create multiple multiplier functions
def double(x):
    return x * 2

def triple(x):
    return x * 3

def quadruple(x):
    return x * 4

# This is repetitive! Can we generalize?
```

### Creating a Closure

```python
def make_multiplier(n):
    """Factory function that creates multiplier functions."""
    def multiplier(x):
        return x * n  # 'n' is from the enclosing scope
    return multiplier

# Create specific multipliers
double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

# Use them
print(double(5))     # 10
print(triple(5))     # 15
print(quadruple(5))  # 20
```

### How It Works

```python
def make_multiplier(n):  # n = 2 when we call make_multiplier(2)
    def multiplier(x):
        return x * n     # This 'n' refers to the outer 'n'
    return multiplier    # Return the inner function

double = make_multiplier(2)
# Now 'double' is the 'multiplier' function with n=2 "remembered"

print(double(5))  # 5 * 2 = 10
```

**Key insight:** The inner function `multiplier` "closes over" the variable `n` from the outer function. Even after `make_multiplier` finishes, `n` is preserved.

### Checking Closure Variables

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)

# See what the closure remembers
print(double.__closure__)  # (<cell at 0x...: int object at 0x...>,)
print(double.__closure__[0].cell_contents)  # 2
```

### Another Example: Counter

```python
def make_counter(start=0):
    """Create a counter that remembers its count."""
    count = start

    def counter():
        nonlocal count  # Needed to modify the outer variable
        count += 1
        return count

    return counter

# Create counters
counter_a = make_counter(0)
counter_b = make_counter(100)

print(counter_a())  # 1
print(counter_a())  # 2
print(counter_a())  # 3

print(counter_b())  # 101
print(counter_b())  # 102
```

**Note:** We need `nonlocal` to MODIFY the outer variable. Without it, `count += 1` would create a new local variable.

---

## Closure Use Cases

### Use Case 1: Configuration/Factory Functions

```python
def make_logger(prefix):
    """Create a logger with a specific prefix."""
    def log(message):
        print(f"[{prefix}] {message}")
    return log

info = make_logger("INFO")
error = make_logger("ERROR")

info("Application started")   # [INFO] Application started
error("File not found")       # [ERROR] File not found
```

### Use Case 2: Data Hiding (Encapsulation without Classes)

```python
def make_account(initial_balance):
    """Create a bank account with private balance."""
    balance = initial_balance  # This is "private"

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        raise ValueError("Insufficient funds")

    def get_balance():
        return balance

    # Return functions that can access balance
    return deposit, withdraw, get_balance

# Usage
deposit, withdraw, get_balance = make_account(100)

print(get_balance())  # 100
deposit(50)
print(get_balance())  # 150
withdraw(30)
print(get_balance())  # 120
```

### Use Case 3: Callback Functions with Context

```python
def make_price_checker(threshold):
    """Create a function that checks if price exceeds threshold."""
    def check(price):
        if price > threshold:
            return f"ALERT: Price {price} exceeds {threshold}!"
        return f"Price {price} is OK"
    return check

check_100 = make_price_checker(100)
check_500 = make_price_checker(500)

print(check_100(95))   # Price 95 is OK
print(check_100(150))  # ALERT: Price 150 exceeds 100!
print(check_500(150))  # Price 150 is OK
```

---

## PCAP Traps

### Trap 1: Lambda Can Only Have One Expression

```python
# WRONG - multiple statements
f = lambda x: x += 1; return x  # SyntaxError

# CORRECT - single expression
f = lambda x: x + 1
```

### Trap 2: Lambda Returns the Expression Value

```python
# No 'return' keyword needed
f = lambda x: x * 2
print(f(5))  # 10, not None

# Using 'return' is a SyntaxError
f = lambda x: return x * 2  # SyntaxError!
```

### Trap 3: map() and filter() Return Iterators, Not Lists

```python
numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)
print(result)        # <map object at 0x...>
print(list(result))  # [2, 4, 6]
print(list(result))  # [] - exhausted!
```

### Trap 4: Closure Variable Capture (Late Binding)

```python
# TRAP: All functions capture the SAME variable
functions = []
for i in range(3):
    functions.append(lambda: i)

# All return 2 (the final value of i)!
print(functions[0]())  # 2
print(functions[1]())  # 2
print(functions[2]())  # 2

# FIX: Capture the value at definition time
functions = []
for i in range(3):lsy
    functions.append(lambda i=i: i)  # Default argument captures current value

print(functions[0]())  # 0
print(functions[1]())  # 1
print(functions[2]())  # 2
```

### Trap 5: nonlocal vs global

```python
x = 10  # Global

def outer():
    x = 20  # Enclosing (outer)

    def inner():
        nonlocal x  # Refers to outer's x (20), not global x (10)
        x = 30

    inner()
    print(x)  # 30 (modified by inner)

outer()
print(x)  # 10 (global unchanged)
```

---

## reduce() Function (from functools)

`reduce()` applies a function cumulatively to items, reducing a sequence to a single value.

### Import Required

```python
from functools import reduce
```

### How reduce() Works

```python
from functools import reduce

# reduce(function, iterable, [initializer])
# function takes TWO arguments: accumulator and current item

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Step by step:
# Step 1: acc=1, x=2 → 1+2=3
# Step 2: acc=3, x=3 → 3+3=6
# Step 3: acc=6, x=4 → 6+4=10
# Step 4: acc=10, x=5 → 10+5=15
```

### Common reduce() Patterns

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum (same as sum())
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Product (multiply all)
product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120

# Maximum (same as max())
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(maximum)  # 5

# With initializer (starting value)
total = reduce(lambda acc, x: acc + x, numbers, 100)
print(total)  # 115 (100 + 1 + 2 + 3 + 4 + 5)

#Flattening a list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda acc, x: acc + x if type(x) == list else x, nested)
print(flattened) #[1, 2, 3, 4, 5, 6]

```

### reduce() with Strings

```python
from functools import reduce

words = ["Hello", " ", "World", "!"]

# Concatenate
sentence = reduce(lambda acc, x: acc + x, words)
print(sentence)  # "Hello World!"

# Or use str.join (more Pythonic)
sentence = "".join(words)
```

### When to Use reduce()

- **Use reduce:** When you need to combine all elements into one result
- **Don't use:** When built-in functions exist (sum, max, min, any, all)
- **Pythonic preference:** List comprehensions and built-ins are usually clearer

```python
# Prefer this:
total = sum(numbers)

# Over this:
total = reduce(lambda acc, x: acc + x, numbers)
```

---

## Decorators (Closures in Action)

A **decorator** is a function that wraps another function to modify its behavior. Decorators use closures!

### Basic Decorator Pattern

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### How It Works

The `@decorator` syntax is just shorthand:

```python
@my_decorator
def say_hello():
    print("Hello!")

# Is equivalent to:
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)
```

### Decorator with Arguments (Using *args, **kwargs)

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 5)
# Output:
# Calling add
# Finished add
print(result)  # 8
```

### Practical Decorator: Timing

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()  # slow_function took 1.0012 seconds
```

### Decorator Factory (Decorator with Parameters)

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Why Decorators Use Closures

```python
def my_decorator(func):    # Outer function receives the function to wrap
    def wrapper(*args, **kwargs):  # Inner function (closure)
        # Can access 'func' from enclosing scope
        return func(*args, **kwargs)
    return wrapper  # Returns the closure
```

The `wrapper` function is a closure that "remembers" the `func` variable from `my_decorator`'s scope.

---

## functools.wraps - Preserving Function Metadata

When you decorate a function, the wrapper replaces it. This loses the original function's metadata (`__name__`, `__doc__`, etc.).

### The Problem

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print(greet.__name__)  # 'wrapper' - NOT 'greet'!
print(greet.__doc__)   # None - docstring lost!
```

### The Solution: @wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves func's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print(greet.__name__)  # 'greet' - preserved!
print(greet.__doc__)   # 'Greets a person by name.' - preserved!
```

### Why It Matters

1. **Debugging:** Stack traces show correct function names
2. **Documentation:** `help(greet)` shows the right docstring
3. **Introspection:** Tools that inspect functions work correctly
4. **Professional code:** Always use `@wraps` in production decorators

### Complete Decorator Template

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper
```

This is the standard pattern for production-quality decorators.

---

## Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| Lambda (no params) | `lambda: expr` | `lambda: 42` |
| Lambda (one param) | `lambda x: expr` | `lambda x: x * 2` |
| Lambda (multiple) | `lambda a, b: expr` | `lambda a, b: a + b` |
| map() | `map(func, iter)` | `map(lambda x: x*2, [1,2,3])` |
| filter() | `filter(func, iter)` | `filter(lambda x: x>0, nums)` |
| Closure | nested function | See examples above |
| nonlocal | `nonlocal var` | Modify enclosing scope var |

---

## Practice Problems

**Problem 1:** What's the output?
```python
f = lambda x, y=10: x + y
print(f(5))
print(f(5, 20))
```
<details>
<summary>Answer</summary>
15, 25
</details>

**Problem 2:** What's the output?
```python
nums = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2, nums)
print(list(result))
```
<details>
<summary>Answer</summary>
[1, 3, 5] - odd numbers (x % 2 is truthy for odd numbers)
</details>

**Problem 3:** What's the output?
```python
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3), add10(3))
```
<details>
<summary>Answer</summary>
8, 13
</details>

---

**Next:** Apply these concepts to sorting and filtering trade data in your backtesting project!
