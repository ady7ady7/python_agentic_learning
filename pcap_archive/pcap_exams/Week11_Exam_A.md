# PCAP-31-03 Mock Exam — Week 11, Exam A
**Date:** 2026-03-28 | **Time limit:** 65 minutes | **Questions:** 30

Write your answers (letter only) in the Answers section at the bottom.

#12:06

---

## Section 1: Modules & Packages (Q1–Q5)

**Q1:** What is the output?
```python
# mymod.py
x = 10

# main.py
import mymod
mymod.x = 99
import mymod
print(mymod.x)
```
- A) `10`
- B) `99`
- C) `AttributeError`
- D) `ImportError`

A

---

**Q2:** A package's `__init__.py` contains:
```python
__all__ = ['alpha', 'beta']
```
Which statement is TRUE?
- A) Only `alpha` and `beta` can ever be imported from the package
- B) `from package import *` will import only `alpha` and `beta`
- C) `__all__` must contain module objects, not strings
- D) `import package.gamma` will raise `ImportError`


B

---

**Q3:** What is the output?
```python
import math as m
print(m.floor(3.9))
print(m.ceil(3.1))
```
- A) `3` then `3`
- B) `3` then `4`
- C) `4` then `4`
- D) `3.0` then `4.0`

A

---

**Q4:** What happens?
```python
from os import path as p
print(p.basename('/home/user/file.txt'))
print(p.dirname('/home/user/file.txt'))
```
- A) `file.txt` then `/home/user`
- B) `file.txt` then `/home/user/`
- C) `/home/user` then `file.txt`
- D) `NameError`

A

---

**Q5:** Which of these creates a valid package?
- A) A directory with any `.py` file inside
- B) A directory containing `__init__.py`
- C) A `.zip` file containing Python modules
- D) Both B and C are valid

B

---

## Section 2: Exceptions & File I/O (Q6–Q10)

**Q6:** What is the output?
```python
try:
    raise ValueError("bad")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError")
```
- A) `ValueError`
- B) `Exception`
- C) Both printed
- D) `SyntaxError` at runtime

B

---

**Q7:** What is the output?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```
- A) `1`
- B) `2`
- C) `None`
- D) `RuntimeError`

B

---

**Q8:** What is the output?
```python
x = 0
try:
    x = 1
    raise RuntimeError
except RuntimeError:
    x += 10
else:
    x += 100
finally:
    x += 1000

print(x)
```
- A) `1100`
- B) `1101`
- C) `1011`
- D) `1001`

C

---

**Q9:** Which statement about `IOError` in Python 3 is TRUE?
- A) `IOError` was removed in Python 3
- B) `IOError is OSError` evaluates to `True`
- C) `IOError` is a subclass of `OSError`
- D) `FileNotFoundError` is not related to `IOError`

B

---

**Q10:** What is the output?
```python
with open("test.txt", "w") as f:
    f.write("hello")

with open("test.txt", "r") as f:
    print(repr(f.read(3)))
    print(repr(f.read(10)))
```
- A) `'hel'` then `'lo'`
- B) `'hel'` then `'lo   '` (padded)
- C) `'hel'` then `''`
- D) `ValueError`

B

---

## Section 3: Strings & OOP (Q11–Q16)

**Q11:** What is the output?
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
print([a.speak() for a in animals])
```
- A) `['Woof', 'Meow', '...']`
- B) `['Woof', 'Meow', None]`
- C) `['...', '...', '...']`
- D) `TypeError`

A

---

**Q12:** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x += 10

class C(A):
    def __init__(self):
        super().__init__()
        self.x += 100

class D(B, C):
    pass

print(D().x)
```
- A) `11`
- B) `101`
- C) `111`
- D) `1`

C

---

**Q13:** What is the MRO of class `D`?
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```
- A) `D → A → B → C`
- B) `D → B → C → A`
- C) `D → B → A → C`
- D) `D → C → B → A`

B

---

**Q14:** What is the output?
```python
class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1
        self.total = Counter.total * 10

a = Counter()
b = Counter()
print(Counter.total)
print(b.total)
```
- A) `2` then `20`
- B) `2` then `2`
- C) `20` then `20`
- D) `1` then `20`

A

---

**Q15:** What is the output?
```python
class Foo:
    def __repr__(self): return "Foo(repr)"
    def __str__(self): return "Foo(str)"

f = Foo()
print(f)
print(repr(f))
print([f])
```
- A) `Foo(str)` / `Foo(repr)` / `[Foo(str)]`
- B) `Foo(str)` / `Foo(repr)` / `[Foo(repr)]`
- C) `Foo(repr)` / `Foo(repr)` / `[Foo(repr)]`
- D) `Foo(str)` / `Foo(str)` / `[Foo(str)]`

B

---

**Q16:** Which is TRUE about abstract base classes?
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    pass
```
- A) `Circle()` can be instantiated since it inherits from `Shape`
- B) `Circle()` raises `TypeError` because `area` is not implemented
- C) `Shape()` can be instantiated directly
- D) `@abstractmethod` has no effect without `ABC`

B

---

## Section 4: Generators & Iterators (Q17–Q21)

**Q17:** What is the output?
```python
def gen():
    return
    yield 1
    yield 2

g = gen()
print(type(g).__name__)
print(list(g))
```
- A) `function` then `[]`
- B) `generator` then `[1, 2]`
- C) `generator` then `[]`
- D) `TypeError`

B

---

**Q18:** What is the output?
```python
def gen():
    yield 1
    yield from range(2, 5)
    yield 5

g = gen()
list(g)
print(next(g))
```
- A) `1`
- B) `5`
- C) `StopIteration` is raised
- D) `None`

C


---

**Q19:** What is the output?
```python
g = (x ** 2 for x in range(6))
print(next(g))
print(next(g))
print(sum(g))
```
- A) `0` / `1` / `50`
- B) `0` / `1` / `25`
- C) `0` / `1` / `54`
- D) `0` / `1` / `14`

A

---

**Q20:** What is the output?
```python
class CountUp:
    def __init__(self, limit):
        self.n = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        self.n += 1
        return self.n

print(list(CountUp(3)))
```
- A) `[0, 1, 2]`
- B) `[1, 2, 3]`
- C) `[0, 1, 2, 3]`
- D) `StopIteration`

B

---

**Q21:** What is the output?
```python
def gen():
    yield
    return
    yield 1

print(list(gen()))
```
- A) `[]`
- B) `[None]`
- C) `[None, 1]`
- D) `[1]`

D

---

## Section 5: Closures, Lambdas & Scope (Q22–Q26)

**Q22:** What is the output?
```python
fns = []
for i in range(4):
    fns.append(lambda: i)

print([f() for f in fns])
```
- A) `[0, 1, 2, 3]`
- B) `[3, 3, 3, 3]`
- C) `[0, 0, 0, 0]`
- D) `TypeError`

B

---

**Q23:** What is the output?
```python
fns = [lambda i=i: i * 2 for i in range(4)]
print(fns[3]())
```
- A) `0`
- B) `4`
- C) `6`
- D) `8`

C

---

**Q24:** What is the output?
```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

f = outer()
print(f())
print(f())
print(f())
```
- A) `5` / `5` / `5`
- B) `5` / `10` / `15`
- C) `0` / `5` / `10`
- D) `UnboundLocalError`

B

---

**Q25:** What is the output?
```python
from functools import reduce

result = reduce(lambda a, b: a * b, [1, 2, 3, 4], 2)
print(result)
```
- A) `24`
- B) `48`
- C) `10`
- D) `2`

B

---

**Q26:** What is the output?
```python
x = 10
def f():
    x = 20
    def g():
        return x
    x = 30
    return g()

print(f())
```
- A) `10`
- B) `20`
- C) `30`
- D) `UnboundLocalError`

C

---

## Section 6: datetime & Miscellaneous (Q27–Q30)

**Q27:** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 3, 28, 23, 0, 0)
result = dt + timedelta(hours=2)
print(result.day)
print(result.hour)
```
- A) `28` then `25`
- B) `29` then `1`
- C) `29` then `2`
- D) `28` then `1`

B

---

**Q28:** What is the output?
```python
from datetime import datetime

s = "28/03/2026 14:30"
dt = datetime.strptime(s, "%d/%m/%Y %H:%M")
print(dt.year)
print(dt.hour)
```
- A) `2026` then `14`
- B) `26` then `14`
- C) `2026` then `30`
- D) `ValueError`

A

---

**Q29:** What is the output?
```python
from datetime import timedelta

td = timedelta(days=1, hours=2)
print(td.days)
print(td.seconds)
```
- A) `1` then `7200`
- B) `1` then `2`
- C) `26` then `0`
- D) `1` then `120`

A

---

**Q30:** What is the output?
```python
data = [5, 3, 8, 1, 9, 2]
top3 = sorted(data, key=lambda x: -x)[:3]
evens = list(filter(lambda x: x % 2 == 0, data))
print(top3)
print(evens)
```
- A) `[9, 8, 5]` then `[8, 2]`
- B) `[9, 8, 5]` then `[2, 8]`
- C) `[1, 2, 3]` then `[8, 2]`
- D) `[9, 8, 5]` then `[5, 3, 8]`

A

#Finished 12:15

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
