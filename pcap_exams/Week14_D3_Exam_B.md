# Week 14 — PCAP Mock Exam B (Day 3)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#Start 11:47
---

**1.** What is the expected output of the following code?

```python
import math
print(math.ceil(-2.1))
print(math.floor(-2.1))
print(math.trunc(-2.9))
```

A. `-2` / `-3` / `-2`
B. `-3` / `-3` / `-2`
C. `-2` / `-2` / `-2`
D. An exception is raised.

A

---

**2.** What is the expected output of the following code?

```python
import os
p = '/data/project/src/main.py'
print(os.path.dirname(p))
print(os.path.splitext(os.path.basename(p))[0])
```

A. `/data/project/src` / `main`
B. `/data/project` / `main.py`
C. `/data/project/src` / `main.py`
D. An exception is raised.

A

---

**3.** What is true about Python modules and packages? (Select two answers)

A. A module is a single `.py` file.
B. Importing a module executes its top-level code every time it is imported.
C. `__name__` equals `'__main__'` only when a module is run directly, not when imported.
D. `from module import name` removes the module object from the namespace.


C, D

---

**4.** What is the expected output of the following code?

```python
import sys

print(type(sys.modules) is dict)
print(type(sys.argv) is list)
```

A. `True` / `True`
B. `False` / `True`
C. `True` / `False`
D. `False` / `False`

A

---

**5.** Which of the following are true about the `os.path` module? (Select two answers)

A. `os.path.exists(path)` returns `False` if the path does not exist (no exception raised).
B. `os.path.join('a', 'b', 'c')` returns `'a/b/c'` on Unix.
C. `os.path.split('/a/b/c')` returns `('/a/b', '/c')`.
D. `os.path.isfile(path)` raises `FileNotFoundError` if the file does not exist.

A, B

---

**6.** What is the expected output of the following code?

```python
import random
random.seed(1)
vals = [random.randint(1, 10) for _ in range(3)]
random.seed(1)
vals2 = [random.randint(1, 10) for _ in range(3)]
print(vals == vals2)
print(all(1 <= v <= 10 for v in vals))
```

A. `True` / `True`
B. `False` / `True`
C. `True` / `False`
D. `False` / `False`

A

---

**7.** What is the expected output of the following code?

```python
class NetworkError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

    def __str__(self):
        return f'[{self.code}] {self.args[0]}'

err = NetworkError('timeout', 408)
print(str(err))
print(err.args)
```

A. `[408] timeout` / `('timeout',)`
B. `[408] timeout` / `('timeout', 408)`
C. `timeout` / `('timeout',)`
D. An exception is raised.

A

---

**8.** What is the expected output of the following code?

```python
def outer():
    try:
        return 'try'
    except:
        return 'except'
    finally:
        return 'finally'

print(outer())
```

A. `try`
B. `except`
C. `finally`
D. An exception is raised.

C

---

**9.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    raise ValueError
except ValueError:
    pass
else:
    print('ok')
```

B.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    raise ValueError('wrap')
except ValueError:
    pass
```

C.
```python
try:
    x = int('abc')
except ValueError:
    x = 0
finally:
    x += 1
```

D.
```python
try:
    raise RuntimeError
except TypeError:
    pass
```

A, C

---

**10.** What is the expected output of the following code?

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('zero not allowed')
    finally:
        print('cleanup')

try:
    print(divide(10, 0))
except ValueError as e:
    print(str(e))
```

A. `cleanup` / `zero not allowed`
B. `zero not allowed` / `cleanup`
C. `cleanup` / `0`
D. An exception is raised without being caught.

A

---

**11.** What is the expected output of the following code?

```python
try:
    x = None + 1
except TypeError as e:
    print(type(e).__name__)
    print('caught')
```

A. `TypeError` / `caught`
B. `ValueError` / `caught`
C. `AttributeError` / `caught`
D. The code is erroneous and will not execute.

A

---

**12.** What is the expected output of the following code?

```python
s = 'Python is great'
print(s[7:9])
print(s[-5:])
```

A. `is` / `great`
B. `is` / `reat`
C. `i ` / `great`
D. An exception is raised.

A

---

**13.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'PCAP'
t = s[::-1] + s[0]
```

A. `len(t) == 5`
B. `t[0] == 'P'`
C. `t[-1] == 'P'`
D. `t == 'PCAPP'`

A, B, C - three True answers

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello'.center(9) == ' hello '`
B. `'abc'.ljust(5) == 'abc  '`
C. `'abc'.rjust(2) == 'abc'`
D. `'xyz'.center(3, '-') == '-xyz-'`

We didn't have this and I don't think it's relevant, but I'll try.

B, D

---

**15.** What is the expected output of the following code?

```python
s = 'aabbccdd'
print(s[::2])
print(s[1::2])
```

A. `abcd` / `abcd`
B. `aabb` / `ccdd`
C. `acac` / `bdbd`
D. An exception is raised.

A

---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'abc' * 0 == ''`
B. `len('') == 0`
C. `bool('False') == False`
D. `'0' == 0`

A, B,


---

**17.** What is the expected output of the following code?

```python
s = 'the quick brown fox'
words = s.split()
print(words[1])
print(len(words))
```

A. `quick` / `4`
B. `the` / `4`
C. `quick` / `3`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
s = 'abcabc'
print(s.replace('a', 'X', 1))
print(s.replace('a', 'X'))
```

A. `Xbcabc` / `XbcXbc`
B. `XbcXbc` / `Xbcabc`
C. `Xbcabc` / `Xbcabc`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
items = ['a', 'bb', 'ccc', 'dddd']
result = ', '.join(i.upper() for i in items if len(i) > 1)
print(result)
```

A. `BB, CCC, DDDD`
B. `A, BB, CCC, DDDD`
C. `bb, ccc, dddd`
D. An exception is raised.

A

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Node:
    count = 0

    def __init__(self, val):
        self.val = val
        Node.count += 1

n1 = Node(1)
n2 = Node(2)
```

A. `'val' in Node.__dict__`
B. `Node.count == 2`
C. `n2.count == 2`
D. `n1.count == 0`

B, C

---

**21.** What is the expected output of the following code?

```python
class Writer:
    def format(self, text):
        return text

    def write(self):
        return self.format('hello')

class LoudWriter(Writer):
    def format(self, text):
        return text.upper()

w = LoudWriter()
print(w.write())
```

A. `hello`
B. `HELLO`
C. `Hello`
D. An exception is raised.

B

---

**22.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Foo:
    x = 10
    y = 20

    def __init__(self):
        self.z = 30

f = Foo()
```

A. `'x' in f.__dict__`
B. `'z' in f.__dict__`
C. `'y' in Foo.__dict__`
D. `'z' in Foo.__dict__`

B, C

---

**23.** What is the expected output of the following code?

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f'${self.amount}'

a = Money(10)
b = Money(5)
print(a + b)
print(str(a))
```

A. `$15` / `$10`
B. `Money(15)` / `$10`
C. `$15` / `Money(10)`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Base:
    def greet(self):
        return 'base'

    def run(self):
        return self.greet()

class Sub(Base):
    def greet(self):
        return 'sub'

s = Sub()
```

A. `s.run() == 'base'`
B. `s.run() == 'sub'`
C. `isinstance(s, Base)`
D. `type(s) is Base`

B, C

---

**25.** What is the expected output of the following code?

```python
class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return super().method() + 'B'

class C(A):
    def method(self):
        return super().method() + 'C'

class D(B, C):
    pass

d = D()
print(d.method())
```

A. `AB`
B. `ACB`
C. `ABC`
D. An exception is raised.

B

---

**26.** What is true about Python's `isinstance` and `issubclass`? (Select two answers)

A. `isinstance(True, int)` returns `True`.
B. `issubclass(bool, str)` returns `True`.
C. `isinstance([], object)` returns `True`.
D. `issubclass(int, float)` returns `True`.

A, C

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class P: pass
class Q(P): pass
class R(P): pass
```

A. `class S(Q, R): pass`
B. `class S(P, Q): pass`
C. `class S(R, Q): pass`
D. `class S(P, R, Q): pass`

A, C

---

**28.** What is the expected output of the following code?

```python
class Converter:
    def convert(self, val):
        return val

    def pipeline(self, values):
        return [self.convert(v) for v in values]

class DoubleConverter(Converter):
    def convert(self, val):
        return val * 2

dc = DoubleConverter()
print(dc.pipeline([1, 2, 3]))
```

A. `[1, 2, 3]`
B. `[2, 4, 6]`
C. `[1, 4, 9]`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class A:
    pass

class B(A):
    pass

print(B.__bases__)
print(A.__bases__)
```

A. `(<class 'A'>,)` / `(<class 'object'>,)`
B. `(<class 'A'>,)` / `()`
C. `(A, object)` / `(<class 'object'>,)`
D. An exception is raised.

A

---

**30.** What is true about Python's `__repr__` and `__str__`? (Select two answers)

A. `str(obj)` calls `__str__` if defined; otherwise falls back to `__repr__`.
B. `repr(obj)` calls `__str__` if `__repr__` is not defined.
C. The default `__repr__` (from `object`) returns something like `<ClassName object at 0x...>`.
D. `print(repr(obj))` and `repr(obj)` always produce identical output.

A, C


---

**31.** What is the expected output of the following code?

```python
def make_power(exp):
    return lambda x: x ** exp

square = make_power(2)
cube = make_power(3)
print(square(4))
print(cube(2))
```

A. `16` / `8`
B. `8` / `16`
C. `16` / `16`
D. An exception is raised.

A

---

**32.** What is the expected output of the following code?

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fibonacci()
result = [next(g) for _ in range(6)]
print(result)
```

A. `[0, 1, 1, 2, 3, 5]`
B. `[1, 1, 2, 3, 5, 8]`
C. `[0, 1, 2, 3, 5, 8]`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `nums.txt` exists with two lines: `10` and `20`?

```python
with open('nums.txt', 'r') as f:
    lines = f.readlines()

print(len(lines))
print(int(lines[0].strip()) + int(lines[1].strip()))
```

A. `2` / `30`
B. `1` / `30`
C. `2` / `1020`
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
data = [('b', 2), ('a', 3), ('c', 1)]
result = sorted(data, key=lambda t: t[1])
print(result[0])
print(result[-1])
```

A. `('c', 1)` / `('b', 2)`
B. `('c', 1)` / `('a', 3)`
C. `('a', 3)` / `('c', 1)`
D. An exception is raised.

B

---

**35.** Which of the following statements about file I/O are true? (Select two answers)

A. `open('f.txt', 'w')` creates the file if it does not exist.
B. `open('f.txt', 'r')` creates the file if it does not exist.
C. After `f.close()`, calling `f.read()` raises a `ValueError`.
D. `with open(...) as f:` only closes the file if no exception was raised.

A, C

---

**36.** What is the expected output of the following code?

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print(result)
```

A. `[4, 16, 36, 64]`
B. `[1, 4, 9, 16, 25, 36, 49, 64]`
C. `[2, 4, 6, 8]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
adders = [lambda x, n=n: x + n for n in range(5)]
print(adders[1](10))
print(adders[4](10))
```

A. `11` / `14`
B. `14` / `14`
C. `10` / `10`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
items = [3, 1, 4, 1, 5, 9, 2, 6]
top3 = sorted(items, reverse=True)[:3]
print(top3)
print(min(top3))
```

A. `[9, 6, 5]` / `5`
B. `[1, 1, 2]` / `1`
C. `[9, 6, 5]` / `6`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
evens = list(filter(lambda x: x % 2 == 0, flat))
print(evens)
print(sum(evens))
```

A. `[2, 4, 6]` / `12`
B. `[1, 3, 5]` / `9`
C. `[2, 4, 6]` / `8`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `config.txt` already exists?

```python
try:
    f = open('config.txt', 'x')
    print('created')
except FileExistsError:
    print('already exists')
except IOError:
    print('io error')
else:
    f.close()
    print('closed')
finally:
    print('done')
```

A. `created` / `closed` / `done`
B. `already exists` / `done`
C. `io error` / `done`
D. `already exists`

B

#END 12:07

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | A | 22 | B, C |
| 3 | A, C | 23 | A |
| 4 | A | 24 | B, C |
| 5 | A, B | 25 | C |
| 6 | A | 26 | A, C |
| 7 | A | 27 | A, C |
| 8 | C | 28 | B |
| 9 | A, C | 29 | A |
| 10 | A | 30 | A, C |
| 11 | A | 31 | A |
| 12 | A | 32 | A |
| 13 | A, C | 33 | A |
| 14 | B, C | 34 | B |
| 15 | A | 35 | A, C |
| 16 | A, B | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | B, C | 40 | B |
