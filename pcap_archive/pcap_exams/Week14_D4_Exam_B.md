# Week 14 — PCAP Mock Exam B (Day 4)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#16:50

---

**1.** What is the expected output of the following code?

```python
import math
print(math.isfinite(float('inf')))
print(math.isnan(float('nan')))
print(math.fabs(-7.5))
```

A. `False` / `True` / `7.5`
B. `True` / `True` / `7.5`
C. `False` / `False` / `-7.5`
D. An exception is raised.

Cut it out, what the fuck is that shit? We didn't have it in PCAP material.

---

**2.** What is the expected output of the following code?

```python
import os
path = 'project/src/utils/helpers.py'
print(os.path.splitext(path)[1])
print(os.path.basename(os.path.dirname(path)))
```

A. `.py` / `utils`
B. `.py` / `src`
C. `helpers.py` / `utils`
D. An exception is raised.

B

---

**3.** What is true about Python's import system? (Select two answers)

A. `import pkg.mod` makes `pkg.mod` accessible but does NOT add `mod` to the current namespace.
B. `from pkg import mod` makes `mod` accessible and also adds `pkg` to the namespace.
C. Re-importing an already-imported module returns the cached object from `sys.modules`.
D. A package's `__init__.py` is executed every time any submodule of the package is imported.

A, C

---

**4.** What is the expected output of the following code?

```python
import sys

print('os' in sys.modules)
import os
print('os' in sys.modules)
```

A. `False` / `True`
B. `True` / `True`
C. `False` / `False`
D. `True` / `False`

A

---

**5.** Which of the following are true about `os.path`? (Select two answers)

A. `os.path.abspath('.')` returns the absolute path of the current directory.
B. `os.path.join('/a', '/b')` returns `'/a/b'` on Unix.
C. `os.path.exists` returns `True` for files, but `False` for directories.
D. `os.path.splitext('file')` returns `('file', '')`.

A, B

---

**6.** What is the expected output of the following code?

```python
import random
items = list(range(1, 6))
random.seed(5)
random.shuffle(items)
print(items == sorted(items))
print(len(items))
```

A. `False` / `5`
B. `True` / `5`
C. `False` / `4`
D. An exception is raised.

A

---

**7.** What is the expected output of the following code?

```python
class ParseError(Exception):
    def __init__(self, line, msg):
        self.line = line
        super().__init__(f'line {line}: {msg}')

try:
    raise ParseError(10, 'unexpected token')
except ParseError as e:
    print(e.line)
    print(str(e))
    print(len(e.args))
```

A. `10` / `line 10: unexpected token` / `1`
B. `10` / `line 10: unexpected token` / `2`
C. `10` / `unexpected token` / `1`
D. An exception is raised.

A

---

**8.** What is the expected output of the following code?

```python
def process():
    try:
        raise ValueError
    except ValueError:
        print('caught')
    finally:
        print('finally')
    print('after')

process()
```

A. `caught` / `finally` / `after`
B. `caught` / `after` / `finally`
C. `finally` / `caught` / `after`
D. An exception is raised.

A

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    x = {}['key']
except KeyError:
    x = 'default'
else:
    x = x.upper()
```

B.
```python
try:
    raise ValueError
except TypeError:
    pass
finally:
    raise RuntimeError
```

C.
```python
try:
    x = int('5') * 2
except (ValueError, TypeError):
    x = 0
finally:
    print(x)
```

D.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    raise
```

A, C

---

**10.** What is the expected output of the following code?

```python
def attempt(val):
    try:
        if not isinstance(val, int):
            raise TypeError('need int')
        return val * 10
    except TypeError as e:
        return str(e)
    finally:
        print('checked')

print(attempt(5))
print(attempt('x'))
```

A. `checked` / `50` / `checked` / `need int`
B. `50` / `checked` / `need int` / `checked`
C. `checked` / `checked` / `50` / `need int`
D. An exception is raised.

A

---

**11.** What is the expected output of the following code?

```python
try:
    result = 2 ** 1000
    raise OverflowError
except OverflowError:
    print('overflow')
except Exception:
    print('exception')
```

A. `overflow`
B. `exception`
C. Nothing is printed.
D. An exception is raised without being caught.

A

---

**12.** What is the expected output of the following code?

```python
s = 'Hello, World!'
print(s[7:12])
print(s[-6:-1])
```

A. `World` / `World`
B. `World` / `orld!`
C. `orld!` / `World`
D. An exception is raised.

A

---

**13.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'abcdef'
t = s[1::2]
```

A. `t == 'bdf'`
B. `t[0] == 'a'`
C. `len(t) == 3`
D. `t[-1] == 'e'`

A, C

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello world'.title() == 'Hello World'`
B. `'abc'.zfill(5) == 'abc00'`
C. `'hello'.capitalize() == 'HELLO'`
D. `'  '.isspace()`

A, D

---

**15.** What is the expected output of the following code?

```python
s = 'mississippi'
print(s.count('ss'))
print(s.index('p'))
```

A. `2` / `8`
B. `1` / `8`
C. `2` / `9`
D. An exception is raised.

A

---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'10' < '9'`
B. `'abc' < 'abd'`
C. `'' > 'a'`
D. `'Z' > 'a'`

A, B

---

**17.** What is the expected output of the following code?

```python
s = 'a,b,,c,d'
parts = s.split(',')
non_empty = [p for p in parts if p]
print(len(parts))
print(len(non_empty))
```

A. `5` / `4`
B. `4` / `3`
C. `5` / `3`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
template = 'x={x:.2f}, y={y:.2f}'
print(template.format(x=3.14159, y=2.71828))
```

A. `x=3.14, y=2.72`
B. `x=3.14159, y=2.71828`
C. `x=3, y=2`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
words = ['apple', 'banana', 'cherry']
result = [w for w in words if 'a' in w]
print(', '.join(result))
```

A. `apple, banana`
B. `apple, banana, cherry`
C. `banana`
D. An exception is raised.

A

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Config:
    DEBUG = False
    VERSION = '1.0'

    def __init__(self, env):
        self.env = env

c = Config('prod')
```

A. `'env' in Config.__dict__`
B. `'env' in c.__dict__`
C. `'DEBUG' in c.__dict__`
D. `hasattr(c, 'VERSION')`

B, D

---

**21.** What is the expected output of the following code?

```python
class Validator:
    def validate(self, value):
        return value > 0

    def check(self, value):
        if self.validate(value):
            return 'ok'
        return 'fail'

class StrictValidator(Validator):
    def validate(self, value):
        return value > 100

sv = StrictValidator()
print(sv.check(50))
print(sv.check(200))
```

A. `ok` / `ok`
B. `fail` / `ok`
C. `ok` / `fail`
D. An exception is raised.

B

---

**22.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name

class Bird(Animal):
    legs = 2

b = Bird('Eagle')
```

A. `b.legs == 4`
B. `b.legs == 2`
C. `Animal.legs == 4`
D. `'legs' in b.__dict__`

B, C

---

**23.** What is the expected output of the following code?

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(repr(v1))
```

A. `Vector(4, 6)` / `Vector(1, 2)`
B. `(4, 6)` / `Vector(1, 2)`
C. `Vector(4, 6)` / `(1, 2)`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Base:
    def compute(self, x):
        return x

    def run(self, values):
        return sum(self.compute(v) for v in values)

class Doubler(Base):
    def compute(self, x):
        return x * 2

d = Doubler()
```

A. `d.run([1, 2, 3]) == 6`
B. `d.run([1, 2, 3]) == 12`
C. `isinstance(d, Base)`
D. `'run' in Doubler.__dict__`


B, C

---

**25.** What is the expected output of the following code?

```python
class X:
    def method(self):
        return 'X'

class Y(X):
    def method(self):
        return super().method() + 'Y'

class Z(X):
    def method(self):
        return super().method() + 'Z'

class W(Y, Z):
    pass

print(W().method())
```

A. `XY`
B. `XZY`
C. `XYZ`
D. An exception is raised.

B

---

**26.** What is true about Python inheritance? (Select two answers)

A. `issubclass(bool, int)` returns `True`.
B. `type(True) is int` returns `True`.
C. `isinstance(1, bool)` returns `True`.
D. `issubclass(int, object)` returns `True`.

A, C

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
```

A. `class E(D, C): pass`
B. `class E(C, D): pass`
C. `class E(A, D): pass`
D. `class E(A, C): pass`

A, B

---

**28.** What is the expected output of the following code?

```python
class Formatter:
    def fmt(self, val):
        return str(val)

    def display_all(self, items):
        return [self.fmt(x) for x in items]

class PaddedFormatter(Formatter):
    def fmt(self, val):
        return str(val).zfill(4)

pf = PaddedFormatter()
print(pf.display_all([1, 42, 100]))
```

A. `['1', '42', '100']`
B. `['0001', '0042', '0100']`
C. `['1   ', '42  ', '100 ']`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
print(isinstance(obj, A))
print(type(obj).__name__)
print(len(C.__mro__))
```

A. `True` / `C` / `4`
B. `True` / `A` / `4`
C. `False` / `C` / `3`
D. An exception is raised.

A

---

**30.** What is true about Python's `__repr__` and `__str__`? (Select two answers)

A. `repr(obj)` is meant to produce an unambiguous, developer-facing string.
B. In an interactive Python session, typing an expression calls `__repr__` to display the result.
C. `str(obj)` always calls `__repr__` first, then `__str__`.
D. `print(obj)` calls `repr(obj)` when no `__str__` is defined.

A, D

---

**31.** What is the expected output of the following code?

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))
print(add10(add5(2)))
```

A. `8` / `17`
B. `8` / `15`
C. `3` / `10`
D. An exception is raised.

A

---

**32.** What is the expected output of the following code?

```python
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

g = countdown(3)
vals = list(g)
print(vals)
print(next(g, 'done'))
```

A. `[3, 2, 1, 0]` / `'done'`
B. `[3, 2, 1, 0]` / `3`
C. `[3, 2, 1]` / `'done'`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `notes.txt` exists with content `line1\nline2\nline3`?

```python
with open('notes.txt', 'r') as f:
    content = f.read()

lines = content.split('\n')
print(len(lines))
print(lines[-1])
```

A. `3` / `line3`
B. `4` / ``
C. `2` / `line3`
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
data = [('b', 3), ('a', 1), ('c', 2)]
result = sorted(data, key=lambda t: t[0])
print(result[0])
print(result[-1])
```

A. `('a', 1)` / `('c', 2)`
B. `('a', 1)` / `('b', 3)`
C. `('b', 3)` / `('a', 1)`
D. An exception is raised.

A

---

**35.** Which of the following statements about file I/O are true? (Select two answers)

A. `f.tell()` returns the current file position as an integer.
B. `f.seek(0)` moves the file pointer to the end of the file.
C. `f.read(n)` reads exactly `n` bytes/characters even if fewer are available.
D. `f.write(s)` returns the number of characters written.

A, C

---

**36.** What is the expected output of the following code?

```python
numbers = range(1, 11)
result = list(filter(lambda x: x % 3 == 0, map(lambda x: x * 2, numbers)))
print(result)
```

A. `[6, 12, 18]`
B. `[3, 6, 9]`
C. `[6, 12, 18, 24]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
fns = [lambda x, k=k: x * k for k in [2, 3, 5]]
results = [f(4) for f in fns]
print(results)
```

A. `[8, 12, 20]`
B. `[20, 20, 20]`
C. `[4, 4, 4]`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
scores = [72, 88, 45, 95, 60, 91]
passing = list(filter(lambda x: x >= 70, scores))
print(len(passing))
print(max(passing))
```

A. `4` / `95`
B. `3` / `95`
C. `4` / `91`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
entries = [('carol', 2), ('alice', 1), ('bob', 3)]
result = sorted(entries, key=lambda e: e[1])
print(result[0][0])
print(result[-1][0])
```

A. `alice` / `bob`
B. `bob` / `alice`
C. `carol` / `alice`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `data.txt` does not exist?

```python
try:
    with open('data.txt', 'x') as f:
        f.write('test')
    print('written')
except FileExistsError:
    print('exists')
finally:
    print('end')
```

A. `written` / `end`
B. `exists` / `end`
C. `written`
D. `end`

A


#End 17:10

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | A | 22 | B, C |
| 3 | A, C | 23 | A |
| 4 | A | 24 | B, C |
| 5 | A, D | 25 | B |
| 6 | A | 26 | A, D |
| 7 | A | 27 | A, B |
| 8 | A | 28 | B |
| 9 | A, C | 29 | A |
| 10 | A | 30 | A, B |
| 11 | A | 31 | A |
| 12 | A | 32 | A |
| 13 | A, C | 33 | A |
| 14 | A, D | 34 | A |
| 15 | A | 35 | A, D |
| 16 | A, B | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | B, D | 40 | A |
