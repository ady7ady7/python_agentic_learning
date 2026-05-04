# Week 14 — PCAP Mock Exam A (Day 4)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**

#Start 16:12

---

**1.** What is the expected output of the following code?

```python
import math
print(math.log(math.e))
print(math.log10(1000))
print(type(math.log(1)))
```

A. `1.0` / `3.0` / `<class 'float'>`
B. `1` / `3` / `<class 'int'>`
C. `1.0` / `3.0` / `<class 'int'>`
D. An exception is raised.

B

---

**2.** What is the expected output of the following code?

```python
import os
p = '/home/user/docs/notes.txt'
parts = os.path.split(p)
print(parts[0])
print(parts[1])
```

A. `/home/user/docs` / `notes.txt`
B. `/home/user` / `docs/notes.txt`
C. `/home/user/docs/` / `notes.txt`
D. An exception is raised.

A

---

**3.** Which of the following are true about Python's module system? (Select two answers)

A. `import os` makes `os.path` accessible without a separate import.
B. `from os import path` makes `os` accessible in the current namespace.
C. A name starting with `_` in a module is excluded from `import *` by default.
D. `__all__` in a module has no effect on `from module import *`.

A, C

---

**4.** What is the expected output of the following code?

```python
import sys

sys.path.insert(0, '/first')
sys.path.insert(0, '/second')
print(sys.path[0])
print(sys.path[1])
```

A. `/first` / `/second`
B. `/second` / `/first`
C. `/second` / `/second`
D. An exception is raised.

B

---

**5.** A script is run as `python calc.py add 3 4`. Which of the following are true? (Select two answers)

A. `sys.argv[2]` equals `'3'`
B. `sys.argv[1]` equals `'add'`
C. `len(sys.argv)` equals `3`
D. `sys.argv[0]` equals `'add'`


A, B

---

**6.** What is the expected output of the following code?

```python
import random
random.seed(99)
a = random.randrange(0, 10)
random.seed(99)
b = random.randrange(0, 10)
print(a == b)
print(0 <= a < 10)
```

A. `True` / `True`
B. `False` / `True`
C. `True` / `False`
D. `False` / `False`

A

---

**7.** What is the expected output of the following code?

```python
class AppError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return f'AppError: {self.args[0]}'

try:
    raise AppError('crash')
except AppError as e:
    print(str(e))
    print(repr(e))
```

A. `AppError: crash` / `AppError('crash')`
B. `crash` / `AppError('crash')`
C. `AppError: crash` / `AppError: crash`
D. An exception is raised.

A

---

**8.** What is the expected output of the following code?

```python
def calc(x):
    try:
        result = 100 / x
        return result
    except ZeroDivisionError:
        return -1
    finally:
        print('done')

print(calc(5))
print(calc(0))
```

A. `done` / `20.0` / `done` / `-1`
B. `20.0` / `done` / `-1` / `done`
C. `done` / `done` / `20.0` / `-1`
D. An exception is raised.

A

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    raise ValueError('x')
except ValueError:
    pass
finally:
    x = 10
```

B.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    raise RuntimeError
except RuntimeError:
    pass
```

C.
```python
try:
    x = int('7')
except ValueError:
    x = 0
else:
    x **= 2
```

D.
```python
try:
    raise KeyError
except TypeError:
    pass
```

A, C

---

**10.** What is the expected output of the following code?

```python
def safe(fn, *args):
    try:
        return fn(*args)
    except Exception as e:
        return type(e).__name__

print(safe(int, 'hello'))
print(safe(int, '42'))
```

A. `ValueError` / `42`
B. `ValueError` / `'42'`
C. `Exception` / `42`
D. An exception is raised.

A

---

**11.** What is the expected output of the following code?

```python
try:
    raise Exception('outer')
except Exception:
    try:
        raise ValueError('inner')
    except ValueError as e:
        print(str(e))
    print('after inner')
print('after outer')
```

A. `inner` / `after inner` / `after outer`
B. `inner` / `after outer`
C. `outer` / `after inner` / `after outer`
D. An exception is raised.

A

---

**12.** What is the expected output of the following code?

```python
s = 'abcdefgh'
print(s[2:6])
print(s[::3])
```

A. `cdef` / `adg`
B. `cdef` / `adf`
C. `bcde` / `adg`
D. An exception is raised.

A

---

**13.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'hello'
t = s.upper()
u = t[::-1]
```

A. `u == 'OLLEH'`
B. `u[0] == 'H'`
C. `len(u) == len(s)`
D. `u[-1] == 'O'`

A, C

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'café'.encode('utf-8') == b'cafe'`
B. `'hello'.encode('ascii') == b'hello'`
C. `'python'.upper().lower() == 'python'`
D. `b'hello' == 'hello'`

A, C

---

**15.** What is the expected output of the following code?

```python
s = 'one two three'
print(s.split(' ', 1))
print(len(s.split()))
```

A. `['one', 'two three']` / `3`
B. `['one', 'two', 'three']` / `3`
C. `['one', 'two three']` / `2`
D. An exception is raised.


B



---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello' == 'HELLO'.lower()`
B. `ord('A') == 65`
C. `chr(ord('a') + 1) == 'c'`
D. `'abc'.upper() == 'Abc'`

A, B

---

**17.** What is the expected output of the following code?

```python
s = '  hello world  '
print(s.strip().replace(' ', '_'))
print(s.lstrip().rstrip())
```

A. `hello_world` / `hello world`
B. `_hello_world_` / `hello world`
C. `hello world` / `hello_world`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
data = 'a:b:c:d'
parts = data.split(':')
print(':'.join(reversed(parts)))
```

A. `d:c:b:a`
B. `a:b:c:d`
C. `['d', 'c', 'b', 'a']`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
s = 'Python'
print(f'{s!r}')
print(f'{s!s}')
```

A. `'Python'` / `Python`
B. `Python` / `Python`
C. `"Python"` / `'Python'`
D. An exception is raised.

What the fuck IS THIS QUESTION?
CUT IT OUT

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def __del__(self):
        Robot.population -= 1

r1 = Robot('R1')
r2 = Robot('R2')
del r1
```

A. `Robot.population == 2`
B. `Robot.population == 1`
C. `r2.population == 1`
D. `r2.name == 'R1'`


B, C

---

**21.** What is the expected output of the following code?

```python
class Transformer:
    def transform(self, val):
        return val

    def apply(self, items):
        return [self.transform(x) for x in items]

class Squarer(Transformer):
    def transform(self, val):
        return val ** 2

sq = Squarer()
print(sq.apply([1, 2, 3, 4]))
```

A. `[1, 2, 3, 4]`
B. `[1, 4, 9, 16]`
C. `[2, 4, 6, 8]`
D. An exception is raised.

B

---

**22.** What is the expected output of the following code?

```python
class Vehicle:
    count = 0

    def __init__(self, brand):
        self.brand = brand
        Vehicle.count += 1

v1 = Vehicle('Toyota')
v2 = Vehicle('BMW')
v2.count = 99
print(Vehicle.count)
print(v1.count)
print(v2.count)
```

A. `2` / `2` / `99`
B. `99` / `99` / `99`
C. `2` / `2` / `2`
D. An exception is raised.

A

---

**23.** What is the expected output of the following code?

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return len(self._data) > 0

s = Stack()
print(bool(s))
s.push(1)
print(bool(s))
print(len(s))
```

A. `False` / `True` / `1`
B. `True` / `True` / `1`
C. `False` / `False` / `0`
D. An exception is raised.

A



---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Renderer:
    def render(self, text):
        return text

    def output(self):
        return self.render('data')

class HtmlRenderer(Renderer):
    def render(self, text):
        return f'<p>{text}</p>'

hr = HtmlRenderer()
```

A. `hr.output() == 'data'`
B. `hr.output() == '<p>data</p>'`
C. `isinstance(hr, Renderer)`
D. `type(hr) is Renderer`

B, C

---

**25.** What is the expected output of the following code?

```python
class A:
    def greet(self):
        return 'A'

class B(A):
    def greet(self):
        return super().greet() + 'B'

class C(B):
    def greet(self):
        return super().greet() + 'C'

print(C().greet())
```

A. `ABC`
B. `CBA`
C. `AC`
D. An exception is raised.

A

---

**26.** What is true about Python's class system? (Select two answers)

A. `__dict__` on a class returns a `mappingproxy` object, not a plain `dict`.
B. Instance attributes always shadow class attributes with the same name.
C. Deleting a class attribute also removes all instance attributes with the same name.
D. `vars(obj)` raises an exception if the object has no `__dict__`.

B, C

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class X: pass
class Y(X): pass
class Z(X): pass
class W(Y): pass
```

A. `class V(W, Z): pass`
B. `class V(Z, W): pass`
C. `class V(X, W): pass`
D. `class V(Y, W): pass`

A, and it seems to be the only correct one - this is also weird as B and D follow basically the same logic. I don't see any major idfference.

---

**28.** What is the expected output of the following code?

```python
class Encoder:
    def encode(self, val):
        return str(val)

    def process(self, items):
        return '-'.join(self.encode(x) for x in items)

class HexEncoder(Encoder):
    def encode(self, val):
        return hex(val)

he = HexEncoder()
print(he.process([10, 255]))
```

A. `10-255`
B. `0xa-0xff`
C. `hex(10)-hex(255)`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class A: pass
class B(A): pass
class C(B): pass

print(issubclass(C, A))
print(issubclass(B, C))
print(C.__mro__[-1].__name__)
```

A. `True` / `False` / `object`
B. `True` / `True` / `object`
C. `False` / `False` / `A`
D. An exception is raised.

A

---

**30.** What is true about Python's special methods? (Select two answers)

A. `__contains__` is called by the `in` operator.
B. `__call__` makes an instance callable like a function.
C. `__iter__` must return `self`.
D. `__getitem__` is only used by lists and tuples.

A, C

---

**31.** What is the expected output of the following code?

```python
def logger(prefix):
    messages = []
    def log(msg):
        messages.append(f'{prefix}: {msg}')
        return messages[:]
    return log

info = logger('INFO')
warn = logger('WARN')
print(info('start'))
print(warn('alert'))
print(info('end'))
```

A. `['INFO: start']` / `['WARN: alert']` / `['INFO: start', 'INFO: end']`
B. `['INFO: start']` / `['WARN: alert']` / `['INFO: end']`
C. `['INFO: start', 'WARN: alert']` / `['WARN: alert']` / `['INFO: start', 'WARN: alert', 'INFO: end']`
D. An exception is raised.

A

---

**32.** What is the expected output of the following code?

```python
def take(gen, n):
    return [next(gen) for _ in range(n)]

def naturals():
    n = 1
    while True:
        yield n
        n += 1

g = naturals()
print(take(g, 3))
print(take(g, 2))
```

A. `[1, 2, 3]` / `[4, 5]`
B. `[1, 2, 3]` / `[1, 2]`
C. `[1, 2, 3]` / `[3, 4]`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `items.txt` exists with content `apple\nbanana\ncherry`?

```python
with open('items.txt', 'r') as f:
    lines = [line.strip() for line in f]

print(lines[1])
print(len(lines))
```

A. `banana` / `3`
B. `apple` / `3`
C. `banana` / `2`
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
words = ['cherry', 'apple', 'fig', 'mango']
result = sorted(words, key=lambda w: w[-1])
print(result[0])
print(result[-1])
```

A. `apple` / `cherry`
B. `fig` / `mango`
C. `cherry` / `apple`
D. An exception is raised.

A

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. `'r+'` opens for reading and writing; the file must already exist.
B. `'w'` opens for writing and reading; file pointer starts at the beginning.
C. `'a+'` opens for reading and appending; reads from the beginning.
D. `'x'` creates a new file; succeeds even if the file already exists.

A, C

---

**36.** What is the expected output of the following code?

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
keys, vals = zip(*pairs)
print(list(keys))
print(list(vals))
```

A. `[1, 2, 3]` / `['a', 'b', 'c']`
B. `[(1, 'a'), (2, 'b'), (3, 'c')]` / `[]`
C. `[1, 'a']` / `[2, 'b']`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
ops = [lambda x, n=n: x ** n for n in range(1, 4)]
print(ops[0](2))
print(ops[2](2))
```

A. `2` / `8`
B. `8` / `8`
C. `2` / `4`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
data = [5, 3, 8, 1, 9, 2, 7]
result = sorted(filter(lambda x: x > 4, data))
print(result)
print(result[0])
```

A. `[5, 7, 8, 9]` / `5`
B. `[9, 8, 7, 5]` / `9`
C. `[5, 8, 9, 7]` / `5`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
students = [('Alice', 85), ('Bob', 92), ('Carol', 85), ('Dave', 78)]
result = sorted(students, key=lambda s: (-s[1], s[0]))
print(result[0][0])
print(result[-1][0])
```

A. `Bob` / `Dave`
B. `Alice` / `Dave`
C. `Bob` / `Alice`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `out.txt` does not exist?

```python
try:
    with open('out.txt', 'w') as f:
        f.write('hello\n')
        f.write('world\n')
    print('done')
except IOError as e:
    print('error')
```

A. `done`
B. `error`
C. `hello` / `world` / `done`
D. An exception is raised.

A

#End 16:45
---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | A | 22 | A |
| 3 | A, C | 23 | A |
| 4 | B | 24 | B, C |
| 5 | A, B | 25 | A |
| 6 | A | 26 | A, B |
| 7 | A | 27 | A, B |
| 8 | A | 28 | B |
| 9 | A, C | 29 | A |
| 10 | A | 30 | A, B |
| 11 | A | 31 | A |
| 12 | A | 32 | A |
| 13 | A, C | 33 | A |
| 14 | B, C | 34 | A |
| 15 | A | 35 | A, C |
| 16 | A, B | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | B, C | 40 | A |
