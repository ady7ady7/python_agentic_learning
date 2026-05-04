# Week 6 - PCAP Mock Exam A

**Time Limit:** 65 minutes (PCAP standard)
**Passing Score:** 70% (21/30)
**Topics:** Weeks 1-6 (Modules, Strings, OOP, Functional Programming, datetime, File I/O, Decorators, Iterators, Generators, Named Tuples, `__new__`)

**Instructions:**
- Choose ONE answer per question (unless stated otherwise)
- Write your answer letter next to each question
- No running code — predict outputs mentally


#Start 9:16

---

**Q1.** What is the output?
```python
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

c = Countdown(3)
print(list(c))
```
- A) `[3, 2, 1]`
- B) `[2, 1, 0]`
- C) `[3, 2, 1, 0]`
- D) `[2, 1]`

**Your answer:**
B

---

**Q2.** What is the output?
```python
gen = (x ** 2 for x in range(5))
print(9 in gen)
print(16 in gen)
```
- A) `True` `True`
- B) `True` `False`
- C) `False` `True`
- D) `False` `False`

**Your answer:**
A

---

**Q3.** What is the output?
```python
class Repeat:
    def __init__(self, val, n):
        self.val = val
        self.n = n
    def __iter__(self):
        for _ in range(self.n):
            yield self.val

r = Repeat('hi', 3)
print(list(r))
print(list(r))
```
- A) `['hi', 'hi', 'hi']` then `[]`
- B) `['hi', 'hi', 'hi']` then `['hi', 'hi', 'hi']`
- C) `['hi', 'hi', 'hi']` then Error
- D) Error

**Your answer:**
B

---

**Q4.** What is the output?
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x = 10
print(p)
```
- A) `Point(x=10, y=4)`
- B) `Point(x=3, y=4)`
- C) Error
- D) `(10, 4)`

**Your answer:**
C

---

**Q5.** What is the output?
```python
def make_formatter(prefix):
    def formatter(text):
        return f"{prefix}: {text}"
    return formatter

log = make_formatter("LOG")
print(log("started"))
print(log.__name__)
```
- A) `LOG: started` `log`
- B) `LOG: started` `formatter`
- C) `LOG: started` `make_formatter`
- D) Error

**Your answer:**
B

---

**Q6.** What is the output?
```python
nums = [1, 2, 3]
it = iter(nums)
print(iter(it) is it)
```
- A) `True`
- B) `False`
- C) Error
- D) `None`

**Your answer:**
A

---

**Q7.** What is the output?
```python
class Weird:
    def __new__(cls):
        return 42

    def __init__(self):
        self.value = 100

obj = Weird()
print(obj)
print(type(obj))
```
- A) `42` `<class 'Weird'>`
- B) `100` `<class 'Weird'>`
- C) `42` `<class 'int'>`
- D) Error

**Your answer:**
A

---

**Q8.** What is the output?
```python
def gen():
    yield 1
    yield 2
    return "done"

g = gen()
print(list(g))
```
- A) `[1, 2, "done"]`
- B) `[1, 2]`
- C) `[1, 2, None]`
- D) Error

**Your answer:**
B

---

**Q9.** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

class C(B):
    pass

c = C()
print(c.x, c.y)
```
- A) `1 2`
- B) Error — C has no `__init__`
- C) `None None`
- D) Error — `super()` doesn't chain

**Your answer:**
A

---

**Q10.** What is the output?
```python
def chain():
    yield from range(3)
    yield from [10, 20]

result = list(chain())
print(result)
print(len(result))
```
- A) `[0, 1, 2, 10, 20]` `5`
- B) `[[0, 1, 2], [10, 20]]` `2`
- C) `[range(0, 3), [10, 20]]` `2`
- D) Error

**Your answer:**
A

---

**Q11.** What is the output?
```python
gen = (x for x in range(4))
print(0 in gen)
print(0 in gen)
print(3 in gen)
```
- A) `True` `True` `True`
- B) `True` `False` `True`
- C) `True` `True` `False`
- D) `True` `False` `False`

**Your answer:**
D

---

**Q12.** What is the output?
```python
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args) + 1
    return wrapper

@deco
@deco
def value():
    return 5

print(value())
print(value.__name__)
```
- A) `7` `value`
- B) `6` `value`
- C) `7` `wrapper`
- D) `6` `wrapper`

**Your answer:**
A

---

**Q13.** What is the output?
```python
try:
    x = int("abc")
except ValueError as e:
    print("caught")
except Exception:
    print("general")
finally:
    print("done")
```
- A) `caught` `done`
- B) `general` `done`
- C) `caught`
- D) `caught` `general` `done`

**Your answer:**
A

---

**Q14.** What is the output?
```python
class Container:
    def __init__(self, items):
        self.items = items
    def __iter__(self):
        return iter(self.items)

c = Container([10, 20, 30])
it = iter(c)
print(it is c)
next(it)
print(list(c))
print(list(it))
```
- A) `False` `[10, 20, 30]` `[20, 30]`
- B) `False` `[10, 20, 30]` `[10, 20, 30]`
- C) `True` `[10, 20, 30]` `[20, 30]`
- D) `True` `[20, 30]` `[20, 30]`

**Your answer:**
A

---

**Q15.** What is the output?
```python
text = "Hello, World!"
print(text[7:12])
print(text[-6:-1])
```
- A) `World` `World`
- B) `World` `orld!`
- C) `World` `World`
- D) `World!` `World`

**Your answer:**
C


---

**Q16.** What is the output?
```python
def gen():
    yield 'a'
    yield 'b'
    yield 'c'

g1 = gen()
g2 = gen()
next(g1)
next(g1)
print(next(g2))
```
- A) `c`
- B) `b`
- C) `a`
- D) Error

**Your answer:**
C

---

**Q17.** What is the output?
```python
from collections import namedtuple

Trade = namedtuple('Trade', 'ticker price quantity')
t = Trade('AAPL', 150.0, 100)
print(t[1])
print(t.ticker)
print(isinstance(t, tuple))
```
- A) `150.0` `AAPL` `True`
- B) `150.0` `AAPL` `False`
- C) `AAPL` `AAPL` `True`
- D) Error

**Your answer:**
A

---

**Q18.** What is the output?
```python
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
```
- A) `[1, 3, 5]`
- B) `[2, 4]`
- C) `[False, True, False, True, False]`
- D) `[1, 2, 3, 4, 5]`

**Your answer:**
B

---

**Q19.** What is the output?
```python
class Stepper:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += self.step
        return val

s = Stepper(0, 10, 3)
print(list(s))
print(list(s))
```
- A) `[0, 3, 6, 9]` then `[0, 3, 6, 9]`
- B) `[0, 3, 6, 9]` then `[]`
- C) `[3, 6, 9]` then `[3, 6, 9]`
- D) `[0, 3, 6, 9]` then Error

**Your answer:**
A

---

**Q20.** What is the output?
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

c = Circle(5)
print(c.r)
```
- A) `5`
- B) Error — can't instantiate Circle
- C) Error — Shape can't be defined
- D) `None`

**Your answer:**
B

---

**Q21.** What is the output?
```python
nums = [1, 2, 3]
it = iter(nums)
nums.append(4)
print(list(it))
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) Error

**Your answer:**
B

---

**Q22.** What is the output?
```python
class A:
    count = 0
    def __init__(self):
        A.count += 1

a1 = A()
a2 = A()
a3 = A()
print(a1.count, A.count)
```
- A) `1 3`
- B) `3 3`
- C) `1 1`
- D) `0 3`

**Your answer:**
B

---

**Q23.** What is the output?
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

f = outer()
print(f())
print(f())
```
- A) `15` `15`
- B) `15` `20`
- C) `10` `15`
- D) Error

**Your answer:**
B

---

**Q24.** Which statement about iterators and iterables is TRUE?
- A) Every iterable is an iterator
- B) Every iterator is an iterable
- C) Lists are iterators
- D) Generators are iterables but not iterators

**Your answer:**
A

---

**Q25.** What is the output?
```python
from datetime import datetime

dt = datetime(2026, 1, 15, 14, 30)
print(dt.strftime('%y-%m-%d'))
```
- A) `2026-01-15`
- B) `26-01-15`
- C) `26-1-15`
- D) Error

**Your answer:**
A

---

**Q26.** What is the output?
```python
class MyClass:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

obj = MyClass(42)
print(obj.value)
obj.value = 100
```
- A) `42` then `100` is set
- B) `42` then Error
- C) Error on first print
- D) `42` then `None`

**Your answer:**
B

---

**Q27.** What is the output?
```python
gen = (x for x in range(3))
it1 = iter(gen)
it2 = iter(gen)
print(it1 is it2)
print(next(it1))
print(next(it2))
```
- A) `True` `0` `1`
- B) `False` `0` `0`
- C) `True` `0` `0`
- D) `False` `0` `1`

**Your answer:**
B

---

**Q28.** What is the output?
```python
import sys

def check():
    return 'math' in sys.modules

import math
print(check())
del math
print(check())
```
- A) `True` `False`
- B) `True` `True`
- C) `False` `True`
- D) `False` `False`

**Your answer:**
A

---

**Q29.** What is the output?
```python
def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration:
    print("stopped")
```
- A) `1` `2` Error
- B) `1` `2` `stopped`
- C) `1` `2` `None`
- D) `1` `2` `3`

**Your answer:**
B

---

**Q30.** Which statement about generators is FALSE?
- A) A generator function contains at least one `yield` statement
- B) Calling a generator function returns a generator object, not the result
- C) `list()` on a generator consumes it — a second `list()` returns `[]`
- D) Generator expressions must use square brackets `[]`

**Your answer:**
D

#End 9;34

---

**End of Exam A — Good luck!**
