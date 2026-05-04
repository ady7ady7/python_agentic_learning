# PCAP-31-03 Mock Exam — Week 11, Exam B
**Date:** 2026-03-28 | **Time limit:** 65 minutes | **Questions:** 30

Write your answers (letter only) in the Answers section at the bottom.

#Start 12:31

---

## Section 1: Modules & Packages (Q1–Q5)

**Q1:** What is the output?
```python
import os

path = "/var/log/system/error.log"
print(os.path.split(path))
print(os.path.splitext(path))
```
- A) `('/var/log/system', 'error.log')` then `('/var/log/system/error', '.log')`
- B) `('/var/log/system/', 'error.log')` then `('/var/log/system/error', '.log')`
- C) `('/var/log/system', 'error.log')` then `('/var/log/system/error.log', '')`
- D) `('/var/log/system', 'error')` then `('.log')`

A

---

**Q2:** What is the output?
```python
import sys
print(type(sys.path))
print(sys.path[0])
```
- A) `list` then the current script's directory
- B) `tuple` then the current script's directory
- C) `dict` then `''`
- D) `list` then `None`

A

---

**Q3:** Which is the correct way to handle a missing optional import?
```python
try:
    import ujson as json
except ___:
    import json
```
- A) `ModuleNotFoundError`
- B) `ImportError`
- C) `AttributeError`
- D) Both A and B are correct — `ModuleNotFoundError` is a subclass of `ImportError`


D

---

**Q4:** What does `if __name__ == '__main__':` guard against?
- A) Syntax errors when the module is imported
- B) Code running when the module is imported rather than run directly
- C) Circular imports
- D) The module being imported more than once

B

---

**Q5:** A directory structure is:
```
mypackage/
    __init__.py
    tools.py
    utils/
        __init__.py
        helpers.py
```
Which import is valid from outside `mypackage`?
- A) `import mypackage.utils.helpers`
- B) `import helpers from mypackage.utils`
- C) `from mypackage import helpers`
- D) `import mypackage/utils/helpers`


A

---

## Section 2: Exceptions & File I/O (Q6–Q10)

**Q6:** What is the output?
```python
try:
    int("abc")
except (TypeError, ValueError) as e:
    print(type(e).__name__)
```
- A) `TypeError`
- B) `ValueError`
- C) `Exception`
- D) Both printed

B

---

**Q7:** What is the output?
```python
try:
    pass
except ValueError:
    print("except")
else:
    print("else")
finally:
    print("finally")
```
- A) `finally`
- B) `else` then `finally`
- C) `except` then `finally`
- D) nothing


B


---

**Q8:** What is the output?
```python
class MyError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

try:
    raise MyError("oops", 404)
except MyError as e:
    print(str(e))
    print(e.code)
```
- A) `oops` then `404`
- B) `MyError: oops` then `404`
- C) `oops` then `None`
- D) `TypeError`

B

---

**Q9:** What is the output?
```python
with open("test.txt", "w") as f:
    f.write("alpha\nbeta\ngamma\n")

with open("test.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(repr(lines[0]))
```
- A) `3` then `'alpha'`
- B) `3` then `'alpha\n'`
- C) `4` then `'alpha\n'`
- D) `3` then `alpha`

B

---

**Q10:** What is the output?
```python
try:
    raise ValueError("first")
except ValueError:
    raise RuntimeError("second")
except RuntimeError:
    print("caught runtime")
```
- A) `caught runtime`
- B) `RuntimeError: second` propagates uncaught
- C) Both exceptions printed
- D) `ValueError: first` propagates uncaught

D - this is a weird example though

---

## Section 3: OOP (Q11–Q16)

**Q11:** What is the output?
```python
class A:
    def f(self): return "A"

class B(A):
    def f(self): return "B" + super().f()

class C(A):
    def f(self): return "C" + super().f()

class D(B, C):
    pass

print(D().f())
```
- A) `BA`
- B) `BCA`
- C) `BC`
- D) `BAC`

B

---

**Q12:** What is the output?
```python
class A:
    x = []
    def add(self, val):
        self.x.append(val)

a = A()
b = A()
a.add(1)
b.add(2)
print(a.x)
print(b.x)
```
- A) `[1]` then `[2]`
- B) `[1, 2]` then `[1, 2]`
- C) `[1]` then `[1, 2]`
- D) `[]` then `[1, 2]`

B

---

**Q13:** What is the output?
```python
class Foo:
    def __init__(self):
        self.__secret = 42

f = Foo()
print(f._Foo__secret)
```
- A) `AttributeError`
- B) `42`
- C) `None`
- D) `NameError`

B

---

**Q14:** Which is TRUE about `@staticmethod` vs `@classmethod`?
- A) Both receive the instance as first argument
- B) `@staticmethod` receives the class, `@classmethod` receives neither
- C) `@classmethod` receives the class as first argument, `@staticmethod` receives neither
- D) They are identical in behaviour

C

---

**Q15:** What is the output?
```python
class Base:
    def __init__(self):
        self.value = 10

    def show(self):
        print(self.value)

class Child(Base):
    def __init__(self):
        super().__init__()
        self.value = 20

c = Child()
c.show()
```
- A) `10`
- B) `20`
- C) `None`
- D) `AttributeError`

B

---

**Q16:** What is the output?
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self) -> str: ...

class Car(Vehicle):
    def fuel_type(self): return "petrol"

class Boat(Vehicle):
    pass

print(Car().fuel_type())
print(Boat())
```
- A) `petrol` then `TypeError`
- B) `petrol` then `<Boat object>`
- C) `TypeError` on `Car()`
- D) `petrol` then `None`

A

---

## Section 4: Generators & Iterators (Q17–Q21)

**Q17:** What is the output?
```python
def squares(n):
    for i in range(n):
        yield i ** 2

g = squares(5)
print(next(g))
print(next(g))
remaining = list(g)
print(remaining)
print(list(g))
```
- A) `0` / `1` / `[4, 9, 16]` / `[]`
- B) `0` / `1` / `[4, 9, 16]` / `[4, 9, 16]`
- C) `0` / `1` / `[2, 3, 4]` / `[]`
- D) `0` / `1` / `[4, 16]` / `[]`

A

---

**Q18:** What is the output?
```python
gen = (x * 2 for x in [1, 2, 3, 4, 5])
print(next(gen))
print(next(gen))
print(sum(gen))
```
- A) `2` / `4` / `24`
- B) `2` / `4` / `18`
- C) `2` / `4` / `14`
- D) `2` / `4` / `30`

A

---

**Q19:** What is the output?
```python
def gen():
    yield from range(3)
    yield from range(3)

print(list(gen()))
```
- A) `[0, 1, 2]`
- B) `[0, 1, 2, 0, 1, 2]`
- C) `[0, 0, 1, 1, 2, 2]`
- D) `[0, 1, 2, 3, 4, 5]`

B

---

**Q20:** What is the output?
```python
def gen():
    yield 1
    yield 2

g = gen()
for val in g:
    print(val)

print(list(g))
```
- A) `1` / `2` / `[1, 2]`
- B) `1` / `2` / `[]`
- C) `1` / `2` / `[2]`
- D) Nothing — `TypeError`

B

---

**Q21:** What is the output?
```python
class Evens:
    def __init__(self, limit):
        self.n = 0
        self.limit = limit

    def __iter__(self): return self

    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        val = self.n * 2
        self.n += 1
        return val

print(list(Evens(4)))
```
- A) `[0, 2, 4, 6]`
- B) `[2, 4, 6, 8]`
- C) `[0, 2, 4, 6, 8]`
- D) `[1, 2, 3, 4]`

val: 0 n: 1
2 2
4 3
6 4 - STOP

A = [0, 2, 4, 6]
---

## Section 5: Closures, Lambdas & Scope (Q22–Q26)

**Q22:** What is the output?
```python
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))
print(add10(3))
```
- A) `8` then `13`
- B) `8` then `8`
- C) `15` then `15`
- D) `5` then `10`

A

---

**Q23:** What is the output?
```python
def outer():
    results = []
    for i in range(3):
        results.append(lambda i=i: i ** 2)
    return results

fns = outer()
print([f() for f in fns])
```
- A) `[4, 4, 4]`
- B) `[0, 1, 4]`
- C) `[0, 2, 4]`
- D) `[1, 4, 9]`

B

---

**Q24:** What is the output?
```python
x = 'global'

def f():
    print(x)
    x = 'local'

f()
```
- A) `global`
- B) `local`
- C) `UnboundLocalError`
- D) `NameError`

C

---

**Q25:** What is the output?
```python
from functools import reduce

words = ['py', 'thon', ' ', 'is', ' ', 'fun']
result = reduce(lambda a, b: a + b, words)
print(result)
```
- A) `['py', 'thon', ' ', 'is', ' ', 'fun']`
- B) `python is fun`
- C) `pythonn isfun`
- D) `TypeError`


B

---

**Q26:** What is the output?
```python
def f(x, fn=lambda x: x * 2):
    return fn(x)

print(f(5))
print(f(5, lambda x: x + 10))
```
- A) `10` then `15`
- B) `10` then `25`
- C) `25` then `15`
- D) `10` then `10`

A

---

## Section 6: datetime & Miscellaneous (Q27–Q30)

**Q27:** What is the output?
```python
from datetime import date

d1 = date(2026, 1, 1)
d2 = date(2026, 3, 28)
delta = d2 - d1
print(delta.days)
print(type(delta).__name__)
```
- A) `87` then `timedelta`
- B) `86` then `timedelta`
- C) `87` then `int`
- D) `2` then `timedelta`

B, stupid question - I'd have to check the calendar to calculate that properly

---

**Q28:** What is the output?
```python
from datetime import datetime

dt = datetime(2026, 3, 28, 9, 5, 3)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%d/%m/%Y"))
```
- A) `2026-03-28 09:05:03` then `28/03/2026`
- B) `2026-28-03 09:05:03` then `28/03/2026`
- C) `2026-03-28 9:5:3` then `28/3/2026`
- D) `ValueError`


A
---

**Q29:** What is the output?
```python
from datetime import time

t = time(9, 0)
print(t >= time(9, 0))
print(t > time(8, 59))
print(t < time(9, 0, 1))
```
- A) `True` / `True` / `True`
- B) `True` / `False` / `True`
- C) `False` / `True` / `True`
- D) `True` / `True` / `False`

A

---

**Q30:** What is the output?
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, numbers))
mapped = list(map(lambda x: x ** 2, result))
print(mapped)
```
- A) `[4, 16, 36, 64]`
- B) `[1, 4, 9, 16, 25, 36, 49, 64]`
- C) `[2, 4, 6, 8]`
- D) `[4, 16, 36]`

A

#Koniec 12:45

---

## Answers

| Q | Answer |
|---|--------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
| 14 | |
| 15 | |
| 16 | |
| 17 | |
| 18 | |
| 19 | |
| 20 | |
| 21 | |
| 22 | |
| 23 | |
| 24 | |
| 25 | |
| 26 | |
| 27 | |
| 28 | |
| 29 | |
| 30 | |
