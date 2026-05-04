# Week 14 — PCAP Mock Exam A (Day 2)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#Start 11:10

---

**1.** Which of the following are valid ways to import and use `sqrt` from the `math` module? (Select two answers)

A. `import math.sqrt` then `math.sqrt(9)`
B. `from math import sqrt` then `sqrt(9)`
C. `import math` then `math.sqrt(9)`
D. `from math import sqrt as s` then `math.s(9)`

B, C

---

**2.** What is the expected output of the following code?

```python
import math
print(math.ceil(3.1))
print(math.floor(-3.1))
print(math.trunc(-3.9))
```

A. `4` / `-4` / `-3`
B. `4` / `-3` / `-3`
C. `3` / `-4` / `-3`
D. `4` / `-4` / `-4`

A

---

**3.** What is true about `sys.modules`? (Select two answers)

A. `sys.modules` is a dictionary mapping module names to module objects.
B. `sys.modules` contains only modules from the standard library.
C. If a module is already in `sys.modules`, Python does not re-execute it on re-import.
D. `sys.modules` is a list of strings.

A, C

---

**4.** What is the expected output of the following code?

```python
import os
result = os.path.splitext('archive.tar.gz')
print(result[0])
print(result[1])
```

A. `archive.tar` / `.gz`
B. `archive` / `.tar.gz`
C. `archive.tar.gz` / ``
D. An exception is raised.

B

---

**5.** A script is invoked as `python run.py --verbose output.txt`. Which of the following are true? (Select two answers)

A. `sys.argv[1]` equals `'--verbose'`
B. `sys.argv[0]` equals `'python'`
C. `len(sys.argv)` equals `3`
D. `sys.argv[-1]` equals `'output.txt'`

C, D

---

**6.** Assuming the code executes successfully, which expressions always evaluate to `True`? (Select two answers)

```python
import random
random.seed(42)
a = random.randint(1, 100)
random.seed(42)
b = random.randint(1, 100)
```

A. `a == b`
B. `a != b`
C. `a >= 1 and a <= 100`
D. `type(a) is float`

A, C

---

**7.** What is the expected output of the following code?

```python
class DatabaseError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

    def __str__(self):
        return f'DB-{self.code}: {self.args[0]}'

try:
    raise DatabaseError('connection failed', 503)
except DatabaseError as e:
    print(str(e))
    print(e.args)
    print(e.code)
```

A. `DB-503: connection failed` / `('connection failed',)` / `503`
B. `DB-503: connection failed` / `('connection failed', 503)` / `503`
C. `connection failed` / `('connection failed',)` / `503`
D. An exception is raised.

A

---

**8.** What is the expected output of the following code?

```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```

A. `1`
B. `2`
C. `None`
D. An exception is raised.

B

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    x = int('5')
except ValueError:
    x = 0
else:
    x *= 10
```

B.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    raise
```

C.
```python
try:
    x = int('abc')
except (ValueError, TypeError):
    x = -1
finally:
    x += 10
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
def run(val):
    try:
        if val < 0:
            raise ValueError('negative')
        return val * 2
    except ValueError:
        return -1
    finally:
        print('done')

print(run(3))
print(run(-1))
```

A. `done` / `6` / `done` / `-1`
B. `6` / `done` / `-1` / `done`
C. `done` / `done` / `6` / `-1`
D. `done` / `6` / `-1`

B

---

**11.** What is the expected output of the following code?

```python
try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print(repr(e))
```

A. `KeyError('b')`
B. `'b'`
C. `KeyError`
D. An exception is raised.

A


---

**12.** What is the expected output of the following code?

```python
s = 'racecar'
print(s[::-1] == s)
print(s[1:4])
```

A. `True` / `ace`
B. `False` / `ace`
C. `True` / `rac`
D. `False` / `rac`


A


---

**13.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'Hello, World!'
t = s[7:12]
```

A. `t == 'World'`
B. `len(t) == 6`
C. `t[0] == 'W'`
D. `t[-1] == '!'`

A, C

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'Hello'.lower() == 'hello'`
B. `'PYTHON'.swapcase() == 'Python'`
C. `'abc'.capitalize() == 'Abc'`
D. `'  '.strip() == ' '`

A, C

---

**15.** Which of the following statements about string methods are true? (Select two answers)

A. `'a,b,c'.split(',', 1)` returns `['a', 'b,c']`.
B. `'hello'.find('z')` raises a `ValueError`.
C. `'ab' * 3` returns `'ababab'`.
D. `'abc'.replace('a', 'x', 0)` returns `'xbc'`.

B, C

---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'abc' < 'abd'`
B. `'Z' > 'a'`
C. `'' == False`
D. `'cat' > 'ca'`

A, D

---

**17.** What is the expected output of the following code?

```python
s = 'banana'
print(s.count('a'))
print(s.index('n'))
print(s.rindex('n'))
```

A. `3` / `2` / `4`
B. `3` / `1` / `4`
C. `2` / `2` / `4`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
words = ['alpha', 'beta', 'gamma']
result = ' | '.join(w.upper() for w in words)
print(result)
print(result.count('|'))
```

A. `ALPHA | BETA | GAMMA` / `2`
B. `ALPHA | BETA | GAMMA` / `3`
C. `alpha | beta | gamma` / `2`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
s = 'Python3'
print(s.isalpha())
print(s[:-1].isalpha())
```

A. `True` / `True`
B. `False` / `True`
C. `True` / `False`
D. `False` / `False`

B

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Engine:
    horsepower = 200

    def __init__(self, fuel):
        self.fuel = fuel

e = Engine('diesel')
```

A. `'fuel' in Engine.__dict__`
B. `'horsepower' in Engine.__dict__`
C. `'fuel' in e.__dict__`
D. `'horsepower' in e.__dict__`

B, C

---

**21.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class A:
    x = 10

class B(A):
    pass

b = B()
```

A. `'x' in B.__dict__`
B. `hasattr(b, 'x')`
C. `b.x == 10`
D. `'x' in b.__dict__`

B, C

---

**22.** What is the expected output of the following code?

```python
class Registry:
    _count = 0

    def __init__(self):
        Registry._count += 1

    @classmethod
    def total(cls):
        return cls._count

r1 = Registry()
r2 = Registry()
r3 = Registry()
print(Registry.total())
```

A. `1`
B. `2`
C. `3`
D. An exception is raised.

C

---

**23.** What is the expected output of the following code?

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Item({self.name!r}, {self.price})'

i = Item('book', 29)
print(repr(i))
print(str(i))
```

A. `Item('book', 29)` / `Item('book', 29)`
B. `Item('book', 29)` / `<Item object at 0x...>`
C. `<Item object at 0x...>` / `Item('book', 29)`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Animal:
    def speak(self):
        return 'generic'

class Cat(Animal):
    def speak(self):
        return 'meow'

class Kitten(Cat):
    pass

k = Kitten()
```

A. `k.speak() == 'generic'`
B. `k.speak() == 'meow'`
C. `isinstance(k, Animal)`
D. `type(k) is Cat`

B, C

---

**25.** What is the expected output of the following code?

```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def describe(self):
        return f'speed={self.speed}'

class Truck(Vehicle):
    def __init__(self, speed, payload):
        super().__init__(speed)
        self.payload = payload

t = Truck(90, 5000)
print(t.describe())
print(t.payload)
```

A. An exception is raised.
B. `speed=90` / `5000`
C. `speed=None` / `5000`
D. `speed=90` / `None`

B

---

**26.** What is true about Python's MRO and `isinstance`? (Select two answers)

A. `isinstance(obj, tuple_of_types)` returns `True` if obj matches any type in the tuple.
B. `issubclass(A, A)` always returns `False`.
C. `__mro__` is a tuple, not a list.
D. `isinstance(True, int)` returns `False`.

A, C

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class A: pass
class B(A): pass
class C(A): pass
```

A. `class X(B, C): pass`
B. `class X(A, B): pass`
C. `class X(C, B): pass`
D. `class X(B, A, C): pass`

A, C

---

**28.** What is the expected output of the following code?

```python
class Logger:
    def log(self, msg):
        return f'LOG: {msg}'

    def run(self):
        return self.log('started')

class TimedLogger(Logger):
    def log(self, msg):
        return f'TIMED: {msg}'

tl = TimedLogger()
print(tl.run())
```

A. `LOG: started`
B. `TIMED: started`
C. `LOG: TIMED: started`
D. An exception is raised.

A

---

**29.** What is the expected output of the following code?

```python
class X: pass
class Y(X): pass
class Z(Y): pass

obj = Z()
print(isinstance(obj, X))
print(type(obj) is X)
```

A. `True` / `True`
B. `True` / `False`
C. `False` / `True`
D. `False` / `False`

B

---

**30.** What is true about Python special methods? (Select two answers)

A. `__eq__` defaults to identity comparison if not defined.
B. Defining `__lt__` automatically provides `__gt__`.
C. `__bool__` is called by `if obj:`.
D. `__len__` returning `0` makes the object truthy.

A, C (We didn't discuss B though)

---

**31.** What is the expected output of the following code?

```python
def outer(n):
    count = 0
    def inner():
        nonlocal count
        count += n
        return count
    return inner

f = outer(3)
print(f())
print(f())
print(f())
```

A. `3` / `3` / `3`
B. `3` / `6` / `9`
C. `0` / `3` / `6`
D. An exception is raised.

B

---

**32.** What is the expected output of the following code?

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
g2 = gen()
print(next(g2))
```

A. `1` / `2` / `1`
B. `1` / `2` / `3`
C. `1` / `1` / `1`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `data.txt` exists with content `12345`?

```python
with open('data.txt', 'r') as f:
    f.seek(2)
    print(f.read(2))
    print(f.read())
```

A. `12` / `345`
B. `34` / `5`
C. `12` / `3`
D. An exception is raised.

B

---

**34.** What is the expected output of the following code?

```python
fns = [lambda x, i=i: x * i for i in range(1, 4)]
print(fns[0](5))
print(fns[2](5))
```

A. `5` / `15`
B. `15` / `15`
C. `5` / `5`
D. An exception is raised.

A

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. Opening a file with `'w'` creates it if it does not exist.
B. `'r+'` truncates the file to zero length before writing.
C. `'a'` always writes at the end of the file, even after `seek(0)`.
D. `'rb'` opens a file for reading in text mode.

A, C

---

**36.** What is the expected output of the following code?

```python
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x - 1, filter(lambda x: x % 2 != 0, nums)))
print(result)
```

A. `[0, 2, 4]`
B. `[1, 2, 3, 4, 5]`
C. `[0, 2, 4, 6, 8]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
def make_adder(n):
    return lambda x: x + n

adders = [make_adder(i) for i in range(3)]
print(adders[0](10))
print(adders[2](10))
```

A. `10` / `12`
B. `12` / `12`
C. `10` / `10`
D. An exception is raised.

B

---

**38.** What is the expected output of the following code?

```python
data = [None, 0, '', 'hello', [], {1: 2}, False]
result = list(filter(None, data))
print(result)
```

A. `['hello', {1: 2}]`
B. `[None, 0, '', [], False]`
C. `['hello', {1: 2}, False]`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
names = ['Charlie', 'Alice', 'Bob']
result = sorted(names, key=lambda s: s[-1])
print(result[0])
print(result[-1])
```

A. `Alice` / `Charlie`
B. `Bob` / `Alice`
C. `Charlie` / `Bob`
D. An exception is raised.

B

Can you explain to me though? I'd expect we sort them based on the last letter, and since 'e' in Alice and Charlie are the same, we go another letter back to 'c' vs 'i' and 'c' wins so it should be Bob, Alice, Charlie, but it's not.

---

**40.** What is the expected output of the following code, assuming `out.txt` does not exist?

```python
try:
    with open('out.txt', 'w') as f:
        f.write('ok')
    print('written')
except IOError:
    print('error')
```

A. `error`
B. `written`
C. `ok`
D. An exception is raised.

B

End: 11:32
---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | B, C | 21 | B, C |
| 2 | B | 22 | C |
| 3 | A, C | 23 | A |
| 4 | A | 24 | B, C |
| 5 | A, D | 25 | B |
| 6 | A, C | 26 | A, C |
| 7 | A | 27 | A, C |
| 8 | B | 28 | B |
| 9 | A, C | 29 | B |
| 10 | A | 30 | A, C |
| 11 | A | 31 | B |
| 12 | A | 32 | A |
| 13 | A, C | 33 | B |
| 14 | A, C | 34 | A |
| 15 | A, C | 35 | A, C |
| 16 | A, D | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | B | 39 | B |
| 20 | B, C | 40 | B |
