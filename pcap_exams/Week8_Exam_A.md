# Week 8 — Mock Exam A
## PCAP-31-03 Full Simulation | 30 Questions | 40 Minutes

**Instructions:** No running code. Choose the single best answer. Time yourself.

---
#Start 21:11

### Q1
What is the output?
```python
xs = [1, 2, 3, 4, 5]
print(xs[1:4:2])
```
- A) `[2, 4]`
- B) `[2, 3, 4]`
- C) `[1, 3, 5]`
- D) `[2, 3]`

A

---

### Q2
What is the output?
```python
def f(a, b=2, *args):
    print(a, b, args)

f(1, 3, 4, 5)
```
- A) `1 2 (3, 4, 5)`
- B) `1 3 (4, 5)`
- C) `1 3 [4, 5]`
- D) `TypeError`

B
---

### Q3
What is the output?
```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B" + super().greet()

class C(A):
    def greet(self):
        return "C" + super().greet()

class D(B, C):
    pass

print(D().greet())
```
- A) `BA`
- B) `BCA`
- C) `BC`
- D) `BA` then `CA`

B

---

### Q4
What is the output?
```python
gen = (x ** 2 for x in range(5))
print(next(gen))
print(next(gen))
print(list(gen))
```
- A) `0`, `1`, `[4, 9, 16]`
- B) `0`, `1`, `[0, 1, 4, 9, 16]`
- C) `0`, `1`, `[2, 3, 4]`
- D) `0`, `0`, `[0, 1, 4, 9, 16]`

A

---

### Q5
What is the output?
```python
try:
    raise TypeError("t")
except (ValueError, TypeError) as e:
    print("caught", type(e).__name__)
except Exception:
    print("fallback")
finally:
    print("final")
```
- A) `caught TypeError`, `final`
- B) `fallback`, `final`
- C) `caught TypeError`
- D) `final`

A

---

### Q6
What is the output?
```python
def make_adder(n):
    return lambda x: x + n

add10 = make_adder(10)
add10.__name__ = "custom"
print(add10.__name__, add10(5))
```
- A) `custom 15`
- B) `<lambda> 15`
- C) `make_adder 15`
- D) `AttributeError`

A

---

### Q7
What is the output?
```python
import logging
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)

logger.debug("d")
logger.warning("w")
```
- A) `d` and `w` both printed
- B) Only `w` printed
- C) Only `d` printed
- D) Nothing printed

B

---

### Q8
What is the output?
```python
x = [1, 2, 3]
y = x
x = x + [4, 5]
print(x, y)
```
- A) `[1, 2, 3, 4, 5] [1, 2, 3]`
- B) `[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]`
- C) `[1, 2, 3] [1, 2, 3]`
- D) `TypeError`

A

---

### Q9
What is the output?
```python
class C:
    _count = 0

    def __init__(self):
        C._count += 1

    @classmethod
    def get_count(cls):
        return cls._count

a = C()
b = C()
print(C.get_count())
```
- A) `0`
- B) `1`
- C) `2`
- D) `AttributeError`

C

---

### Q10
What is the output?
```python
def deco(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) * 2
    return wrapper

@deco
@deco
def val():
    return 3

print(val())
```
- A) `6`
- B) `9`
- C) `12`
- D) `3`

C
---

### Q11
What is the output?
```python
xs = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(xs, key=lambda x: -x)[:3])
```
- A) `[-9, -6, -5]`
- B) `[9, 6, 5]`
- C) `[1, 1, 2]`
- D) `[-3, -1, -4]`

B

---

### Q12
What is the output?
```python
def f():
    try:
        return "try"
    finally:
        return "finally"

print(f())
```
- A) `try`
- B) `finally`
- C) `try` then `finally`
- D) `RuntimeError`

B

---

### Q13
Which statement about `iter(obj)` is correct?
- A) `iter(generator)` returns a new generator object
- B) `iter(generator) is generator` evaluates to `True`
- C) `iter()` can only be called on lists and tuples
- D) `iter(obj)` always raises `TypeError` if `obj` has no `__iter__`

B

---

### Q14
What is the output?
```python
class A:
    x = 1

class B(A):
    pass

b = B()
b.x = 99
print(A.x, B.x, b.x)
```
- A) `1 1 99`
- B) `99 99 99`
- C) `1 99 99`
- D) `AttributeError`

A

---

### Q15
What is the output?
```python
from functools import reduce
print(reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9, 4]))
```
- A) `3`
- B) `7`
- C) `9`
- D) `25`

C

---

### Q16
What is the output?
```python
def outer(x):
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer(10)
print(f(), f(), f())
```
- A) `11 12 13`
- B) `10 11 12`
- C) `11 11 11`
- D) `UnboundLocalError`

A

---

### Q17
What is the output?
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

animals = [Dog(), Cat(), Animal()]
print([a.speak() for a in animals])
```
- A) `['woof', 'meow', '...']`
- B) `['...', '...', '...']`
- C) `TypeError`
- D) `['woof', 'meow']`

A

---

### Q18
What is the output?
```python
g = (x for x in [1, 2, 3, 4, 5])
print(2 in g)
print(list(g))
```
- A) `True`, `[3, 4, 5]`
- B) `True`, `[1, 2, 3, 4, 5]`
- C) `True`, `[]`
- D) `False`, `[1, 2, 3, 4, 5]`

A

---

### Q19
What is the output?
```python
class C:
    def __init__(self, v):
        self.__v = v

    def get(self):
        return self.__v

c = C(42)
c.__v = 99
print(c.get(), c.__v)
```
- A) `42 99`
- B) `99 99`
- C) `42 42`
- D) `AttributeError`

D

---

### Q20
What is the output?
```python
import logging
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
logging.debug("hello")
```
- A) `hello`
- B) Nothing printed
- C) `DEBUG:root:hello`
- D) `WARNING:root:hello`

B

---

### Q21
What is the output?
```python
xs = [1, 2, 3]
ys = xs * 2
ys[0] = 99
print(xs, ys)
```
- A) `[99, 2, 3] [99, 2, 3, 1, 2, 3]`
- B) `[1, 2, 3] [99, 2, 3, 1, 2, 3]`
- C) `[1, 2, 3] [1, 2, 3, 1, 2, 3]`
- D) `TypeError`

B

---

### Q22
What is the output?
```python
def f(x: int) -> str:
    return str(x)

result = f(3.7)
print(type(result).__name__)
```
- A) `int`
- B) `float`
- C) `str`
- D) `TypeError`

C

---

### Q23
What is the output?
```python
class Counter:
    def __init__(self):
        self._n = 0

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        if value < 0:
            raise ValueError("negative")
        self._n = value

c = Counter()
c.n = 5
c.n = -1
print(c.n)
```
- A) `-1`
- B) `5`
- C) `ValueError` is raised
- D) `AttributeError`

C

---

### Q24
What is the output?
```python
a = (1, 2, 3)
b = list(a)
b[0] = 99
print(a, b)
```
- A) `(99, 2, 3) [99, 2, 3]`
- B) `(1, 2, 3) [99, 2, 3]`
- C) `(1, 2, 3) [1, 2, 3]`
- D) `TypeError`

B

---

### Q25
What is the output?
```python
from datetime import datetime
dt = datetime(2026, 2, 27)
print(dt.strftime("%y-%m-%d"))
```
- A) `2026-02-27`
- B) `26-02-27`
- C) `2026-2-27`
- D) `TypeError`

B

---

### Q26
What is the output?
```python
def gen():
    for i in range(3):
        yield i

g1 = gen()
g2 = gen()
print(next(g1), next(g2), next(g1))
```
- A) `0 0 1`
- B) `0 0 0`
- C) `0 1 2`
- D) `StopIteration`

A

---

### Q27
What is the output?
```python
class Base:
    def __init__(self, x):
        self.x = x

class Child(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

c = Child(1, 2)
print(c.x, c.y)
```
- A) `AttributeError`
- B) `1 2`
- C) `None 2`
- D) `1 None`

B

---

### Q28
What is the output?
```python
xs = [1, 2, 3, 4, 5, 6]
result = list(filter(None, map(lambda x: x if x % 2 == 0 else None, xs)))
print(result)
```
- A) `[1, 3, 5]`
- B) `[2, 4, 6]`
- C) `[None, 2, None, 4, None, 6]`
- D) `[]`

B

---

### Q29
What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D().method())
```
- A) `A`
- B) `C`
- C) `TypeError`
- D) `AttributeError`

A

---

### Q30
What is the output?
```python
import sys

def f():
    pass

print(type(f), callable(f), f.__name__)
```
- A) `<class 'function'> True f`
- B) `<class 'method'> True f`
- C) `<class 'function'> False f`
- D) `TypeError`

A

#Koniec 21:23

---

## Answer Key (fill in after completing)

Q1: ___ | Q2: ___ | Q3: ___ | Q4: ___ | Q5: ___
Q6: ___ | Q7: ___ | Q8: ___ | Q9: ___ | Q10: ___
Q11: ___ | Q12: ___ | Q13: ___ | Q14: ___ | Q15: ___
Q16: ___ | Q17: ___ | Q18: ___ | Q19: ___ | Q20: ___
Q21: ___ | Q22: ___ | Q23: ___ | Q24: ___ | Q25: ___
Q26: ___ | Q27: ___ | Q28: ___ | Q29: ___ | Q30: ___

**Score: ___ / 30**
