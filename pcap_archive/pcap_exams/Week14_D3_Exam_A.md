# Week 14 — PCAP Mock Exam A (Day 3)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**

10:55 Start
---

**1.** What is the expected output of the following code?

```python
import math
print(type(math.floor(3.9)))
print(type(math.pow(2, 4)))
print(type(2 ** 4))
```

A. `<class 'int'>` / `<class 'float'>` / `<class 'int'>`
B. `<class 'float'>` / `<class 'float'>` / `<class 'int'>`
C. `<class 'int'>` / `<class 'int'>` / `<class 'int'>`
D. An exception is raised.

A

---

**2.** What is the expected output of the following code?

```python
import os
p = 'C:/Users/admin/docs/report.final.pdf'
name = os.path.basename(p)
root, ext = os.path.splitext(name)
print(root)
print(ext)
```

A. `report` / `.final.pdf`
B. `report.final` / `.pdf`
C. `docs` / ``
D. An exception is raised.

A

---

**3.** What is true about `sys.argv` and `sys.path`? (Select two answers)

A. Both `sys.argv` and `sys.path` are lists.
B. `sys.path[0]` is always the path to the Python interpreter.
C. `sys.argv[0]` is the name of the script being run.
D. `sys.path` can be modified at runtime to add new import locations.

C, D

---

**4.** What is the expected output of the following code?

```python
import sys

def check():
    return 'math' in sys.modules

import math
print(check())
```

A. `False`
B. `True`
C. An exception is raised.
D. `None`

B

---

**5.** Which of the following are true about Python's `random` module? (Select two answers)

A. `random.randint(1, 5)` can return `5`.
B. `random.random()` returns a float in the range `[0.0, 1.0)`.
C. `random.choice([])` returns `None` when the list is empty.
D. `random.seed()` with no arguments always produces the same sequence.

A, B

---

**6.** What is the expected output of the following code?

```python
try:
    raise ValueError('bad input')
except ValueError as e:
    print(str(e))
    print(repr(e))
    print(type(e).__name__)
```

A. `bad input` / `ValueError('bad input')` / `ValueError`
B. `ValueError('bad input')` / `ValueError('bad input')` / `ValueError`
C. `bad input` / `bad input` / `ValueError`
D. An exception is raised.

A

---

**7.** What is the expected output of the following code?

```python
def risky(x):
    try:
        return 10 // x
    except ZeroDivisionError:
        return 0
    finally:
        print('fin')

a = risky(2)
b = risky(0)
print(a + b)
```

A. `fin` / `fin` / `5`
B. `5` / `fin` / `0` / `fin`
C. `fin` / `5` / `fin` / `0`
D. `fin` / `fin` / `0`

B

---

**8.** What is the expected output of the following code?

```python
def f():
    try:
        raise RuntimeError
    except RuntimeError:
        print('caught')
        return 'from except'
    finally:
        print('finally')
        return 'from finally'

print(f())
```

A. `caught` / `finally` / `from except`
B. `caught` / `finally` / `from finally`
C. `caught` / `from except` / `finally`
D. An exception is raised.

B

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    raise TypeError('bad')
except (TypeError, ValueError):
    pass
finally:
    x = 1
```

B.
```python
try:
    x = int('5')
except ValueError:
    pass
else:
    y = x * 2
raise RuntimeError
```

C.
```python
try:
    x = []
    y = x[0]
except IndexError as e:
    z = str(e)
```

D.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    raise TypeError
except TypeError:
    pass
```

A, C

---

**10.** What is the expected output of the following code?

```python
class MyError(Exception):
    def __init__(self, val):
        self.val = val
        super().__init__(f'error: {val}')

try:
    raise MyError(42)
except MyError as e:
    print(e.val)
    print(e.args[0])
```

A. `42` / `error: 42`
B. `42` / `42`
C. `error: 42` / `error: 42`
D. An exception is raised.

B

---

**11.** What is the expected output of the following code?

```python
s = 'programming'
print(s[3:9:2])
print(s[-3:])
```

A. `grmi` / `ing`
B. `rmn` / `ing`
C. `gam` / `ing`
D. An exception is raised.


C



---

**12.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello'.replace('l', 'r', 1) == 'herlo'`
B. `'abcabc'.count('bc') == 3`
C. `'  python  '.strip() == 'python'`
D. `'python'.find('xyz') == -1`

A, C, D - THREE ANSWERS ARE TRUE.

---

**13.** What is the expected output of the following code?

```python
s = 'Hello World'
parts = s.split()
print(len(parts))
print('_'.join(parts).lower())
```

A. `2` / `hello_world`
B. `11` / `hello world`
C. `2` / `Hello_World`
D. An exception is raised.

A

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'abc123'.isalnum()`
B. `'123'.isdecimal()`
C. `'ABC'.islower()`
D. `' '.isalpha()`

A, B

---

**15.** What is the expected output of the following code?

```python
s = 'abcdef'
print(s[1:5])
print(s[::-2])
```

A. `bcde` / `fdb`
B. `bcde` / `eca`
C. `abcd` / `fdb`
D. An exception is raised.

A

---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'Abc' > 'abc'`
B. `'xyz' > 'xy'`
C. `'a' * 0 == ''`
D. `'Z' < 'a'`

B, D

---

**17.** What is the expected output of the following code?

```python
s = 'one,two,,three'
parts = s.split(',')
print(len(parts))
print(parts[2])
```

A. `3` / `three`
B. `4` / ``
C. `3` / ``
D. An exception is raised.

B

---

**18.** What is the expected output of the following code?

```python
template = '{name} scored {score}%'
result = template.format(name='Alice', score=95)
print(result)
print(result.startswith('Alice'))
```

A. `Alice scored 95%` / `True`
B. `Alice scored 95%` / `False`
C. `{name} scored {score}%` / `False`
D. An exception is raised.


A

---

**19.** What is the expected output of the following code?

```python
s = 'aAbBcC'
print(s.swapcase())
print(s.upper() == s.lower())
```

A. `AaBbCc` / `False`
B. `AaBbCc` / `True`
C. `aAbBcC` / `False`
D. An exception is raised.

A

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1
        self.id = Counter.total

c1 = Counter()
c2 = Counter()
c3 = Counter()
```

A. `c1.id == c2.id`
B. `c3.id == 3`
C. `Counter.total == 3`
D. `c1.total == 1`

B, C

---

**21.** What is the expected output of the following code?

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} speaks'

class Dog(Animal):
    def speak(self):
        return f'{self.name} barks'

    def describe(self):
        return self.speak()

d = Dog('Rex')
print(d.describe())
```

A. `Rex speaks`
B. `Rex barks`
C. An exception is raised.
D. `None`

B

---

**22.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Base:
    class_var = 100

    def __init__(self):
        self.inst_var = 200

class Child(Base):
    pass

obj = Child()
```

A. `'class_var' in obj.__dict__`
B. `'inst_var' in obj.__dict__`
C. `hasattr(obj, 'class_var')`
D. `'class_var' in Child.__dict__`

B, C

---

**23.** What is the expected output of the following code?

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)
print(p1 is p2)
print(repr(p3))
```

A. `True` / `False` / `Point(3, 4)`
B. `True` / `True` / `Point(3, 4)`
C. `False` / `False` / `Point(3, 4)`
D. An exception is raised.

A

---

**24.** What is the expected output of the following code?

```python
class Printer:
    def output(self, text):
        return text

    def print_all(self, items):
        return [self.output(i) for i in items]

class UpperPrinter(Printer):
    def output(self, text):
        return text.upper()

up = UpperPrinter()
print(up.print_all(['hello', 'world']))
```

A. `['hello', 'world']`
B. `['HELLO', 'WORLD']`
C. `['Hello', 'World']`
D. An exception is raised.

B

---

**25.** What is the expected output of the following code?

```python
class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return 'B+' + super().method()

class C(B):
    pass

obj = C()
print(obj.method())
print(isinstance(obj, A))
```

A. `B+A` / `True`
B. `A` / `True`
C. `B+A` / `False`
D. An exception is raised.


A

---

**26.** What is true about Python's OOP? (Select two answers)

A. `__init__` is called automatically when a new instance is created.
B. Calling `super().__init__()` in a child class is mandatory; omitting it always raises an exception.
C. `type(obj) is ChildClass` returns `True` even if `obj` was instantiated from a parent class.
D. `object` is the base class of all Python classes.

A, D

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class A: pass
class B(A): pass
class C(B): pass
```

A. `class X(C, A): pass`
B. `class X(A, C): pass`
C. `class X(C, B): pass`
D. `class X(B, C): pass`

A, C

---

**28.** What is the expected output of the following code?

```python
class Shape:
    def area(self):
        return 0

    def summary(self):
        return f'Area: {self.area()}'

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(4)
print(s.summary())
```

A. `Area: 0`
B. `Area: 16`
C. `Area: 4`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass

class SportsCar(Car):
    pass

sc = SportsCar()
print(issubclass(SportsCar, Vehicle))
print(isinstance(sc, Car))
print(len(SportsCar.__mro__))
```

A. `True` / `True` / `3`
B. `True` / `True` / `4`
C. `False` / `True` / `4`
D. An exception is raised.

B

---

**30.** What is true about Python's dunder methods? (Select two answers)

A. `__str__` is called by `str()` and `print()`; `__repr__` is its fallback.
B. `__len__` must return a non-negative integer.
C. `__repr__` is called by `print()` when `__str__` is also defined.
D. Defining `__add__` automatically defines `__radd__`.

A, B

---

**31.** What is the expected output of the following code?

```python
def make_counter(start):
    val = [start]
    def increment(by=1):
        val[0] += by
        return val[0]
    return increment

c = make_counter(10) #[10]
print(c()) #[11]
print(c(5)) #[16]
print(c()) #[17]
```

A. `11` / `16` / `17`
B. `10` / `15` / `16`
C. `11` / `11` / `11`
D. An exception is raised.

A



---

**32.** What is the expected output of the following code?

```python
def evens(limit):
    n = 0
    while n <= limit:
        if n % 2 == 0:
            yield n
        n += 1

g = evens(8)
print(next(g))
print(next(g))
print(list(g))
```

A. `0` / `2` / `[4, 6, 8]`
B. `0` / `2` / `[2, 4, 6, 8]`
C. `0` / `2` / `[0, 2, 4, 6, 8]`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `log.txt` exists with content `ERROR: timeout`?

```python
with open('log.txt', 'r') as f:
    line = f.readline()
    rest = f.read()

print(repr(line))
print(repr(rest))
```

A. `'ERROR: timeout'` / `''`
B. `'ERROR: timeout\n'` / `''`
C. `'ERROR'` / `': timeout'`
D. An exception is raised.

B

---

**34.** What is the expected output of the following code?

```python
data = ['apple', 'banana', 'cherry', 'date']
result = sorted(data, key=lambda s: (len(s), s))
print(result[0])
print(result[-1])
```

A. `date` / `banana`
B. `apple` / `cherry`
C. `date` / `cherry`
D. An exception is raised.

C

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. `'w+'` opens for both reading and writing and truncates the file.
B. `'a'` mode allows reading from the beginning of the file.
C. `'rb'` opens a file in binary read mode.
D. `'r'` creates the file if it does not exist.

A, C

---

**36.** What is the expected output of the following code?

```python
words = ['hi', 'hello', 'hey', 'howdy']
result = list(filter(lambda w: len(w) > 2, words))
print(result)
print(len(result))
```

A. `['hello', 'hey', 'howdy']` / `3`
B. `['hello', 'howdy']` / `2`
C. `['hey', 'howdy']` / `2`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
fns = []
for val in [10, 20, 30]:
    fns.append(lambda x, v=val: x + v)

print(fns[0](1))
print(fns[2](1))
```

A. `31` / `31`
B. `11` / `31`
C. `11` / `11`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
nums = [4, 7, 2, 9, 1, 5]
top2 = sorted(nums, reverse=True)[:2]
print(top2)
print(sum(top2))
```

A. `[9, 7]` / `16`
B. `[1, 2]` / `3`
C. `[9, 7]` / `18`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
pairs = [(2, 'b'), (1, 'c'), (1, 'a'), (3, 'a')]
result = sorted(pairs)
print(result[0])
print(result[1])
```

A. `(1, 'a')` / `(1, 'c')`
B. `(1, 'c')` / `(1, 'a')`
C. `(1, 'a')` / `(2, 'b')`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `data.txt` does not exist?

```python
try:
    f = open('data.txt', 'r')
except FileNotFoundError:
    print('not found')
except OSError:
    print('os error')
else:
    data = f.read()
    f.close()
    print('read ok')
finally:
    print('done')
```

A. `not found` / `done`
B. `os error` / `done`
C. `not found`
D. `done`

A

End: 11:21

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | B | 22 | B, C |
| 3 | A, C | 23 | A |
| 4 | B | 24 | B |
| 5 | A, B | 25 | A |
| 6 | A | 26 | A, D |
| 7 | A | 27 | A, C |
| 8 | B | 28 | B |
| 9 | A, C | 29 | B |
| 10 | A | 30 | A, B |
| 11 | C | 31 | A |
| 12 | A, C | 32 | A |
| 13 | A | 33 | A |
| 14 | A, B | 34 | C |
| 15 | A | 35 | A, C |
| 16 | B, D | 36 | A |
| 17 | B | 37 | B |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | B, C | 40 | A |
