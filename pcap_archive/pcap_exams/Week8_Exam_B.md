# Week 8 — Mock Exam B
## PCAP-31-03 Full Simulation | 30 Questions | 40 Minutes

**Instructions:** No running code. Choose the single best answer. Time yourself.

---

#Start 21:24

### Q1
What is the output?
```python
d = {'a': 1, 'b': 2, 'c': 3}
print(list(d.items())[:2])
```
- A) `[('a', 1), ('b', 2)]`
- B) `['a', 'b']`
- C) `[1, 2]`
- D) `TypeError`

A

---

### Q2
What is the output?
```python
def f(x, /, y):
    return x + y

print(f(1, 2))
print(f(1, y=2))
```
- A) `3`, `3`
- B) `3`, `TypeError`
- C) `TypeError`, `3`
- D) `TypeError`, `TypeError`

A

---

### Q3
What is the output?
```python
class A:
    def __init__(self):
        self.x = 1
        self.__y = 2

a = A()
print(hasattr(a, '_A__y'), hasattr(a, '__y'))
```
- A) `True True`
- B) `True False`
- C) `False True`
- D) `False False`

B

---

### Q4
What is the output?
```python
xs = [1, 2, 3]
xs += [4]
ys = xs
xs = xs + [5]
print(xs, ys)
```
- A) `[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]`
- B) `[1, 2, 3, 4, 5] [1, 2, 3, 4]`
- C) `[1, 2, 3, 4, 5] [1, 2, 3]`
- D) `TypeError`

B

---

### Q5
What is the output?
```python
class MyIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val = self.i
        self.i += 1
        return val

obj = MyIter(3)
print(list(obj))
print(list(obj))
```
- A) `[0, 1, 2]`, `[]`
- B) `[0, 1, 2]`, `[0, 1, 2]`
- C) `[0, 1, 2]`, `StopIteration`
- D) `TypeError`

B

---

### Q6
What is the output?
```python
from functools import wraps

def deco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@deco
def hello():
    """says hello"""
    pass

print(hello.__name__, hello.__doc__)
```
- A) `wrapper None`
- B) `hello says hello`
- C) `wrapper says hello`
- D) `hello None`

B

---

### Q7
What is the output?
```python
xs = [5, 3, 8, 1, 9, 2]
print(sorted(xs, key=lambda x: x % 4))
```
- A) `[8, 1, 9, 5, 2, 3]`
- B) `[1, 2, 3, 5, 8, 9]`
- C) `[8, 5, 9, 1, 2, 3]`
- D) The order is stable but there are multiple valid answers depending on sort stability

B

---

### Q8
What is the output?
```python
def gen():
    yield from range(3)
    yield from range(3)

print(list(gen()))
```
- A) `[0, 1, 2]`
- B) `[0, 1, 2, 0, 1, 2]`
- C) `[0, 0, 1, 1, 2, 2]`
- D) `TypeError`

B

---

### Q9
What is the output?
```python
import logging
logger = logging.getLogger("myapp")
logger2 = logging.getLogger("myapp")
print(logger is logger2)
```
- A) `False`
- B) `True`
- C) `AttributeError`
- D) Depends on Python version

B

---

### Q10
What is the output?
```python
class C:
    def __repr__(self):
        return "C-repr"

    def __str__(self):
        return "C-str"

c = C()
print(str(c))
print(repr(c))
print(f"{c}")
print(f"{c!r}")
```
- A) `C-str`, `C-repr`, `C-str`, `C-repr`
- B) `C-repr`, `C-repr`, `C-str`, `C-repr`
- C) `C-str`, `C-repr`, `C-repr`, `C-str`
- D) `C-str`, `C-str`, `C-str`, `C-str`

A

---

### Q11
What is the output?
```python
def outer():
    results = []
    for i in range(3):
        results.append(lambda: i)
    return results

fns = outer()
print([f() for f in fns])
```
- A) `[0, 1, 2]`
- B) `[2, 2, 2]`
- C) `[0, 0, 0]`
- D) `NameError`

B

---

### Q12
What is the output?
```python
try:
    int("x")
except ValueError:
    print("ValueError")
except Exception:
    print("Exception")
else:
    print("else")
finally:
    print("finally")
```
- A) `ValueError`, `finally`
- B) `ValueError`, `else`, `finally`
- C) `Exception`, `finally`
- D) `ValueError`

A

---

### Q13
What is the output?
```python
class A:
    def __init__(self):
        self.val = 10

    def __add__(self, other):
        return A()

a = A()
b = A()
c = a + b
print(type(c).__name__, c.val)
```
- A) `A 10`
- B) `A 20`
- C) `int 10`
- D) `TypeError`

B

---

### Q14
What is the output?
```python
xs = (x * x for x in range(10))
total = sum(xs)
print(total, sum(xs))
```
- A) `285 285`
- B) `285 0`
- C) `0 285`
- D) `TypeError`

B

---

### Q15
What is the output?
```python
class Base:
    class_var = []

class Child(Base):
    pass

Base.class_var.append(1)
Child.class_var.append(2)
print(Base.class_var)
```
- A) `[1]`
- B) `[1, 2]`
- C) `[2]`
- D) `AttributeError`

A

---

### Q16
What is the output?
```python
def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(5))
```
- A) `10`
- B) `15`
- C) `5`
- D) `RecursionError`

B

---

### Q17
What is the output?
```python
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info("hello")
```
- A) `INFO:root:hello`
- B) `INFO:hello`
- C) `hello`
- D) Nothing printed

A

---

### Q18
What is the output?
```python
a = [1, 2, 3]
b = a
a = [4, 5, 6]
b.append(99)
print(a, b)
```
- A) `[4, 5, 6] [1, 2, 3, 99]`
- B) `[4, 5, 6, 99] [4, 5, 6, 99]`
- C) `[1, 2, 3, 99] [1, 2, 3, 99]`
- D) `[4, 5, 6] [1, 2, 3]`

A

---

### Q19
What is the output?
```python
class C:
    @property
    def x(self):
        return self.x

c = C()
print(c.x)
```
- A) `None`
- B) `AttributeError`
- C) `RecursionError`
- D) `0`

B
---

### Q20
What is the output?
```python
xs = [1, 2, 3]
ys = [4, 5, 6]
zs = [7, 8]
print(list(zip(xs, ys, zs)))
```
- A) `[(1, 4, 7), (2, 5, 8), (3, 6)]`
- B) `[(1, 4, 7), (2, 5, 8)]`
- C) `[(1, 4, 7), (2, 5, 8), (3, 6, None)]`
- D) `TypeError`

C


---

### Q21
What is the output?
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5), double(triple(2)))
```
- A) `10 15 12`
- B) `10 15 6`
- C) `10 15 30`
- D) `TypeError`

A

---

### Q22
What is the output?
```python
class A:
    pass

class B(A):
    pass

print(issubclass(B, A), issubclass(A, B), issubclass(A, object))
```
- A) `True False True`
- B) `True True True`
- C) `True False False`
- D) `False True True`

A

---

### Q23
What is the output?
```python
from datetime import datetime, timedelta
d = datetime(2026, 2, 28)
d2 = d + timedelta(days=1)
print(d2.strftime("%Y-%m-%d"))
```
- A) `2026-02-29`
- B) `2026-03-01`
- C) `2026-02-28`
- D) `ValueError`

B

---

### Q24
What is the output?
```python
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
x = next(g)
print(x)
```
- A) `start`, `1`
- B) `1`
- C) `start`, `middle`, `1`
- D) `start`

A

---

### Q25
What is the output?
```python
xs = {1, 2, 3, 4}
ys = {3, 4, 5, 6}
print(xs ^ ys)
```
- A) `{3, 4}`
- B) `{1, 2, 5, 6}`
- C) `{1, 2, 3, 4, 5, 6}`
- D) `TypeError`

B

---

### Q26
What is the output?
```python
class C:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

items = [C(3), C(1), C(2)]
items.sort()
print([i.x for i in items])
```
- A) `[3, 1, 2]`
- B) `[1, 2, 3]`
- C) `[3, 2, 1]`
- D) `TypeError`

B

---

### Q27
What is the output?
```python
def f(*args):
    return args

a = [1, 2]
b = [3, 4]
print(f(*a, *b))
```
- A) `([1, 2], [3, 4])`
- B) `(1, 2, 3, 4)`
- C) `[1, 2, 3, 4]`
- D) `TypeError`

C

---

### Q28
What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(C, B):
    pass

print(D().method())
```
- A) `A`
- B) `B`
- C) `C`
- D) `TypeError`

C

---

### Q29
What is the output?
```python
xs = range(10)
evens = filter(lambda x: x % 2 == 0, xs)
doubled = map(lambda x: x * 2, evens)
print(list(doubled)[:4])
```
- A) `[0, 2, 4, 6]`
- B) `[0, 4, 8, 12]`
- C) `[2, 4, 6, 8]`
- D) `[0, 2, 4, 6, 8]`


B

---

### Q30
What is the output?
```python
class C:
    def __init__(self, x):
        self.__x = x

    def __repr__(self):
        return f"C({self.__x!r})"

    def __eq__(self, other):
        return self.__x == other._C__x

a = C(1)
b = C(1)
c = C(2)
print(a == b, a == c, repr(a))
```
- A) `True False C(1)`
- B) `False False C(1)`
- C) `True True C(1)`
- D) `AttributeError`

A

#Finish 21:35

---

## Answer Key (fill in after completing)

Q1: ___ | Q2: ___ | Q3: ___ | Q4: ___ | Q5: ___
Q6: ___ | Q7: ___ | Q8: ___ | Q9: ___ | Q10: ___
Q11: ___ | Q12: ___ | Q13: ___ | Q14: ___ | Q15: ___
Q16: ___ | Q17: ___ | Q18: ___ | Q19: ___ | Q20: ___
Q21: ___ | Q22: ___ | Q23: ___ | Q24: ___ | Q25: ___
Q26: ___ | Q27: ___ | Q28: ___ | Q29: ___ | Q30: ___

**Score: ___ / 30**
