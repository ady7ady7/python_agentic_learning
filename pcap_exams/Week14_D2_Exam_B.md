# Week 14 — PCAP Mock Exam B (Day 2)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#Start 11:32

---

**1.** Which of the following are true about the `math` module? (Select two answers)

A. `math.pi` is a constant available without calling a function.
B. `math.pow(2, 3)` returns the integer `8`.
C. `math.log(1)` returns `0.0`.
D. `math.sqrt` can be called without importing the module first.

B, C

---

**2.** What is the expected output of the following code?

```python
import os
p = '/var/log/app/errors.log'
print(os.path.basename(p))
print(len(os.path.dirname(p).split('/')))
```

A. `errors.log` / `3`
B. `errors.log` / `4`
C. `app` / `3`
D. An exception is raised.

B 

---

**3.** What is true about Python's `import` system? (Select two answers)

A. `from package import module` makes `module` available in the current namespace.
B. `import x; import x` executes the module body twice.
C. `__init__.py` can be an empty file and the directory is still a valid package.
D. `import math as math` is a syntax error.

A, C

---

**4.** What is the expected output of the following code?

```python
import sys
sys.path.append('/extra')
print(sys.path[-1])
print(isinstance(sys.path, list))
```

A. `/extra` / `True`
B. `/extra` / `False`
C. `` / `True`
D. An exception is raised.

A

---

**5.** A script runs as `python app.py 10 20 30`. Which of the following are true? (Select two answers)

A. `sys.argv[3]` equals `'30'`
B. `int(sys.argv[1]) + int(sys.argv[2])` equals `30`
C. `sys.argv[0]` equals `'10'`
D. `len(sys.argv)` equals `3`

A, B

---

**6.** Assuming the code executes successfully, which expressions always evaluate to `True`? (Select two answers)

```python
import random
random.seed(0)
v = random.choice(['x', 'y', 'z'])
```

A. `v in ['x', 'y', 'z']`
B. `len(v) == 1`
C. `type(v) is int`
D. `v == 'x'`

B - ONLY this one is true, despite you claiming there are two True expressions.

---

**7.** What is the expected output of the following code?

```python
class ConfigError(Exception):
    pass

try:
    raise ConfigError('bad value')
except ConfigError as e:
    print(type(e).__name__)
    print(e.args[0])
    print(isinstance(e, Exception))
```

A. `ConfigError` / `bad value` / `True`
B. `Exception` / `bad value` / `True`
C. `ConfigError` / `bad value` / `False`
D. An exception is raised.

A

---

**8.** What is the expected output of the following code?

```python
def calc():
    try:
        x = 10 / 2
        return x
    except ZeroDivisionError:
        return -1
    finally:
        print('end')

result = calc()
print(result)
```

A. `end` / `5.0`
B. `5.0` / `end`
C. `end` / `-1`
D. `-1` / `end`

A

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    x = [][0]
except IndexError:
    x = 99
finally:
    x += 1
```

B.
```python
try:
    raise ValueError
except TypeError:
    pass
```

C.
```python
try:
    x = 1
except Exception:
    pass
else:
    x += 1
```

D.
```python
try:
    x = int('bad')
except ValueError:
    raise
```

A, C

---

**10.** What is the expected output of the following code?

```python
def safe_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('called')
    return result

print(safe_div(10, 2))
print(safe_div(5, 0))
```

A. `called` / `5.0` / `called` / `None`
B. `5.0` / `called` / `None` / `called`
C. `called` / `called` / `5.0` / `None`
D. An exception is raised.

A

---

**11.** What is the expected output of the following code?

```python
try:
    x = int('3.14')
except ValueError as e:
    print(type(e).__name__)
except TypeError:
    print('type error')
```

A. `TypeError`
B. `type error`
C. `ValueError`
D. The code is erroneous and will not execute.

C

---

**12.** What is the expected output of the following code?

```python
s = 'abcde'
print(s[1:-1])
print(s[::2])
```

A. `bcd` / `ace`
B. `bcde` / `ace`
C. `bcd` / `bd`
D. An exception is raised.

A

---

**13.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'OpenAI'
t = s[::-1]
```

A. `t[0] == 'I'`
B. `t == 'IAnepO'`
C. `len(t) == len(s)`
D. `t[-1] == 'I'`

A, B, C (Three True answers)

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello world'.title() == 'Hello World'`
B. `'abc'.zfill(5) == '00abc'`
C. `'123'.isdigit() == False`
D. `'  hello'.lstrip() == 'hello  '`

A, B

---

**15.** Which of the following statements about string methods are true? (Select two answers)

A. `'abc'.find('d')` returns `-1`.
B. `'abc'.index('d')` returns `-1`.
C. `'hello'.replace('l', 'r')` returns `'herro'`.
D. `'  x  '.rstrip()` returns `'  x'`.

A, D

---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'10' > '9'`
B. `'abc' == 'ABC'.lower()`
C. `'a' < 'b' < 'c'`
D. `'' > 'a'`


B, C
---

**17.** What is the expected output of the following code?

```python
s = 'abracadabra'
print(s.count('abra'))
print(s.find('cad'))
```

A. `2` / `4`
B. `1` / `4`
C. `2` / `3`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
tokens = ['2026', '04', '14']
date_str = '-'.join(tokens)
print(date_str)
print(date_str.split('-')[1])
```

A. `2026-04-14` / `04`
B. `2026 04 14` / `04`
C. `2026-04-14` / `2026`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
s = 'Hello World'
print(s.lower().startswith('hello'))
print(s.upper().endswith('WORLD'))
```

A. `False` / `True`
B. `True` / `True`
C. `True` / `False`
D. `False` / `False`

B

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Config:
    debug = False

    def __init__(self, name):
        self.name = name

cfg = Config('prod')
```

A. `'debug' in cfg.__dict__`
B. `'name' in cfg.__dict__`
C. `hasattr(cfg, 'debug')`
D. `'name' in Config.__dict__`

B, C

---

**21.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Parent:
    tag = 'p'

class Child(Parent):
    pass

c = Child()
```

A. `c.tag == 'p'`
B. `'tag' in Child.__dict__`
C. `'tag' in Parent.__dict__`
D. `type(c) is Parent`

A, C

---

**22.** What is the expected output of the following code?

```python
class Tracker:
    __slots__ = ['value']

    def __init__(self, v):
        self.value = v

t = Tracker(10)
print(t.value)
print(hasattr(t, '__dict__'))
```

A. `10` / `True`
B. `10` / `False`
C. `None` / `False`
D. An exception is raised.

B

---

**23.** What is the expected output of the following code?

```python
class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self.items) > 0

b1 = Box([])
b2 = Box([1, 2])
print(bool(b1))
print(bool(b2))
print(len(b1))
```

A. `False` / `True` / `0`
B. `True` / `True` / `0`
C. `False` / `True` / `2`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Mover:
    def move(self):
        return 'move'

    def act(self):
        return self.move()

class FastMover(Mover):
    def move(self):
        return 'fast move'

fm = FastMover()
```

A. `fm.act() == 'move'`
B. `fm.act() == 'fast move'`
C. `isinstance(fm, Mover)`
D. `'act' in FastMover.__dict__`

A, C

---

**25.** What is the expected output of the following code?

```python
class A:
    def greet(self):
        return 'A'

class B(A):
    def greet(self):
        return 'B: ' + super().greet()

class C(B):
    def greet(self):
        return 'C: ' + super().greet()

obj = C()
print(obj.greet())
```

A. `C: B: A`
B. `C: A`
C. `B: A`
D. An exception is raised.

A

---

**26.** What is true about Python inheritance? (Select two answers)

A. A class with no explicit parent implicitly inherits from `object`.
B. `type(obj).__name__` returns the class name as a string.
C. Python does not support more than one level of inheritance.
D. `super()` can only be used in `__init__`.

A, B

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class W: pass
class X(W): pass
class Y(W): pass
class Z(X): pass
```

A. `class M(Z, Y): pass`
B. `class M(W, Z): pass`
C. `class M(Y, Z): pass`
D. `class M(Z, X): pass`

A, C

---

**28.** What is the expected output of the following code?

```python
class Renderer:
    def render(self, val):
        return str(val)

    def display(self):
        return f'<{self.render(99)}>'

class BinaryRenderer(Renderer):
    def render(self, val):
        return bin(val)

br = BinaryRenderer()
print(br.display())
```

A. `<99>`
B. `<0b1100011>`
C. `<bin(99)>`
D. An exception is raised.

B

Another fucking stupid questions - I WILL NOT REMEMBER BINARY VALUES BY HEART, YOU IDIOT. It's not what humans do.
I can only guess it's B by eliminating other answers.

---

**29.** What is the expected output of the following code?

```python
class A: pass
class B(A): pass
class C(B): pass

print(issubclass(C, A))
print(issubclass(A, C))
print(C.__mro__[1] is B)
```

A. `True` / `False` / `True`
B. `True` / `True` / `True`
C. `False` / `False` / `True`
D. An exception is raised.

A

---

**30.** What is true about `__repr__` and `__str__`? (Select two answers)

A. `repr(obj)` calls `__repr__`; it is meant for developers.
B. If `__str__` is not defined, `str(obj)` falls back to `__repr__`.
C. Defining `__str__` makes `repr(obj)` use it as a fallback.
D. `print(obj)` always calls `__repr__`.


A, B
---

**31.** What is the expected output of the following code?

```python
def multiplier(factor):
    def apply(values):
        return [v * factor for v in values]
    return apply

double = multiplier(2)
triple = multiplier(3)
print(double([1, 2, 3]))
print(triple([1, 2]))
```

A. `[2, 4, 6]` / `[3, 6]`
B. `[2, 4, 6]` / `[2, 4]`
C. `[1, 2, 3]` / `[1, 2]`
D. An exception is raised.


A

---

**32.** What is the expected output of the following code?

```python
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

g = squares(5)
print(next(g))
print(next(g))
total = sum(g)
print(total)
```

A. `1` / `4` / `50`
B. `1` / `4` / `25`
C. `1` / `4` / `54`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `test.txt` exists with content `Hello`?

```python
with open('test.txt', 'r+') as f:
    f.seek(0, 2)
    f.write('!')
f2 = open('test.txt', 'r')
print(f2.read())
f2.close()
```

A. `Hello`
B. `Hello!`
C. `!`
D. An exception is raised.

B

---

**34.** What is the expected output of the following code?

```python
ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
result = ops[0](ops[1](ops[2](2)))
print(result)
```

A. `9`
B. `10`
C. `25`
D. An exception is raised.


A

---

**35.** Which of the following statements about file I/O are true? (Select two answers)

A. `f.readline()` reads one line including the newline character if present.
B. `f.readlines()` returns a generator of lines.
C. `f.read()` after reaching EOF returns an empty string `''`.
D. `f.write()` automatically adds a newline at the end.

A, C


---

**36.** What is the expected output of the following code?

```python
data = range(1, 8)
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x + 1, data)))
print(result)
```

A. `[2, 4, 6, 8]`
B. `[2, 4, 6]`
C. `[3, 5, 7]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
counters = []
for i in range(3):
    counters.append(lambda x=i: x * 2)
print(counters[0]())
print(counters[2]())
```

A. `4` / `4`
B. `0` / `4`
C. `0` / `0`
D. An exception is raised.


B


---

**38.** What is the expected output of the following code?

```python
values = [0, 1, 2, '', 'a', None, False, True]
positives = list(filter(bool, values))
print(len(positives))
```

A. `3`
B. `4`
C. `8`
D. An exception is raised.

B

---

**39.** What is the expected output of the following code?

```python
records = [('Eve', 30), ('Adam', 25), ('Zoe', 25)]
result = sorted(records, key=lambda r: (r[1], r[0]))
print(result[0])
print(result[-1])
```

A. `('Adam', 25)` / `('Eve', 30)`
B. `('Zoe', 25)` / `('Eve', 30)`
C. `('Eve', 30)` / `('Adam', 25)`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `notes.txt` does not exist?

```python
try:
    f = open('notes.txt', 'x')
    f.write('hello')
    f.close()
    print('created')
except FileExistsError:
    print('exists')
except IOError:
    print('io')
else:
    print('done')
```

A. `created` / `done`
B. `created`
C. `exists`
D. `io`

A


#End 12:00

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A, C | 21 | A, C |
| 2 | B | 22 | B |
| 3 | A, C | 23 | A |
| 4 | A | 24 | B, C |
| 5 | A, B | 25 | A |
| 6 | A, B | 26 | A, B |
| 7 | A | 27 | A, C |
| 8 | A | 28 | B |
| 9 | A, C | 29 | A |
| 10 | A | 30 | A, B |
| 11 | C | 31 | A |
| 12 | A | 32 | A |
| 13 | A, C | 33 | B |
| 14 | A, B | 34 | A |
| 15 | A, C | 35 | A, C |
| 16 | B, C | 36 | A |
| 17 | A | 37 | B |
| 18 | A | 38 | B |
| 19 | B | 39 | A |
| 20 | B, C | 40 | A |
