# Week 14 — PCAP Mock Exam A
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#Start - 12:53

---

**1.** Which of the following statements about the `math` module are true? (Select two answers)

A. `math.floor()` always returns an integer.
B. `math.ceil(-2.1)` returns `-3`.
C. `math.sqrt(4)` returns the integer `2`.
D. `math.trunc(-3.9)` returns `-3`.

C, D

---

**2.** A Python script is run with the command: `python script.py alpha 42`. Which of the following are true? (Select two answers)

A. `sys.argv[0]` equals `'script.py'`
B. `sys.argv[2]` equals the integer `42`
C. `len(sys.argv)` equals `3`
D. `sys.argv[1]` equals `'alpha'`

A, D 

This question puzzles me though

---

**3.** What is true about Python modules? (Select two answers)

A. A module is re-executed every time it is imported.
B. `__name__` equals `'__main__'` only when the module is run directly.
C. The `dir()` function called on a module returns a list of its attribute names.
D. Importing a module with `from module import *` always imports everything.

B, C

---

**4.** What is the expected output of the following code?

```python
import os
path = '/home/user/docs/report.pdf'
print(os.path.basename(path))
print(os.path.dirname(path))
```

A. `report.pdf` / `/home/user/docs`
B. `docs` / `/home/user`
C. `report.pdf` / `/home/user/docs/`
D. An exception is raised.

A

---

**5.** What is the expected output of the following code?

```python
import sys
print(type(sys.argv) is list)
print(type(sys.argv[0]) is str)
```

A. `True` / `False`
B. `False` / `True`
C. `True` / `True`
D. `False` / `False`

C

---

**6.** Assuming the code below executes successfully, which expressions always evaluate to `True`? (Select two answers)

```python
import random
random.seed(7)
x = random.randint(1, 10)
random.seed(7)
y = random.randint(1, 10)
```

A. `x != y`
B. `x == y`
C. `x >= 1 and x <= 10`
D. `random.random() >= 1`

B, C

---

**7.** What is the expected output of the following code?

```python
class AppError(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code

    def __str__(self):
        return f'error-{self.code}'

try:
    raise AppError(404)
except AppError as e:
    print(str(e))
    print(repr(e))
    print(e.args)
```

A. `error-404` / `AppError(404)` / `(404,)`
B. `error-404` / `error-404` / `(404,)`
C. `AppError(404)` / `AppError(404)` / `()`
D. `error-404` / `AppError(404)` / `()`

A

---

**8.** What is the expected behavior of the following code?

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print('zero')
    raise ValueError('new error')
except ValueError:
    print('value')
print('done')
```

A. Outputs `zero` then `value` then `done`.
B. Outputs `zero` then raises unhandled `ValueError`.
C. Outputs `zero` then `done`.
D. The code is erroneous and will not execute.

B

---

**9.** Which of the following snippets will execute without raising any unhandled exceptions? (Select two answers)

A.
```python
try:
    x = int('3')
except ValueError:
    x = 0
else:
    x += 1
finally:
    x *= 2
```

B.
```python
try:
    x = [][0]
except IndexError:
    raise NameError
except NameError:
    x = 0
```

C.
```python
try:
    x = 1 / 0
except TypeError:
    x = 0
```

D.
```python
try:
    x = 5
except:
    x = 0
else:
    x += 1
finally:
    print(x)
```

A, D

---

**10.** What is the expected output of the following code?

```python
def process(val):
    try:
        assert val > 0
        return 10 / val
    except ZeroDivisionError:
        return -1
    except AssertionError:
        return -2
    finally:
        print('cleanup')

print(process(0))
print(process(-1))
```

A. `cleanup` / `-1` / `cleanup` / `-2`
B. `cleanup` / `-2` / `cleanup` / `-2`
C. `-1` / `cleanup` / `-2` / `cleanup`
D. `cleanup` / `cleanup`

C

---

**11.** What is the expected output of the following code?

```python
try:
    x = {}
    x['key']
except (KeyError, IndexError) as e:
    print(type(e).__name__)
```

A. `Exception`
B. `KeyError`
C. `IndexError`
D. The code is erroneous and will not execute.

B


---

**12.** What is the expected output of the following code?

```python
s = 'hello world'
result = s.split()
print(len(result))
print(result[-1])
```

A. `2` / `world`
B. `11` / `d`
C. `2` / `hello`
D. An exception is raised.

A

---

**13.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'PYTHON'[::2] #PTO
s = s[::-1] #OTP
```

A. `s[0] == 'N'`
B. `len(s) == 3`
C. `s[-1] == 'P'`
D. `s == 'NHP'`

B, C


---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'Hello'.lower() == 'hello'`
B. `'abc'.upper() > 'abc'`
C. `'  hello  '.strip() == 'hello'`
D. `'python'.replace('py', 'PY') == 'PYthon'`


A, C, D - also True

---

**15.** Which of the following statements about strings in Python are true? (Select two answers)

A. Strings in Python are immutable.
B. `str.split()` with no arguments splits on any whitespace and removes empty strings.
C. `'a' * 0` raises a `ValueError`.
D. The `in` operator checks for substring presence.

A, B, D - again THREE values seem to be True...


---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'cat' < 'cats'`
B. `'B' > 'a'`
C. `'abc' == 'ABC'.lower()`
D. `'' < 'a'`

A, C, D - dude - again three fucking values are 100% true - what the fuck XD


---

**17.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'th' in 'python'`
B. `str(0) in '1234'`
C. `'xyz' not in 'abcxyz'`
D. `'ab' not in 'ba'`

A, D

---

**18.** What is the expected output of the following code?

```python
s = 'abcabc'
print(s.find('c'))
print(s.rfind('c'))
print(s.count('c'))
```

A. `2` / `5` / `2`
B. `2` / `2` / `1`
C. `5` / `2` / `2`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
parts = ['one', 'two', 'three']
s = '-'.join(parts)
print(s.startswith('one'))
print(s.endswith('ee'))
```

A. `True` / `True`
B. `True` / `False`
C. `False` / `True`
D. `False` / `False`

A

---

**20.** Assuming the code below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Animal:
    kingdom = 'Animalia'

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        return 'woof'

d = Dog('Rex')
```

A. `'kingdom' in Dog.__dict__`
B. `hasattr(d, 'kingdom')`
C. `'bark' in Dog.__dict__`
D. `'name' in Dog.__dict__`

B, C

---

**21.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Point:
    dimensions = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
```

A. `'x' in Point.__dict__`
B. `'x' in p.__dict__`
C. `'dimensions' in p.__dict__`
D. `'dimensions' in Point.__dict__`

B, D

---

**22.** What is the expected output of the following code?

```python
class Counter:
    __count = 0

    def increment(self):
        Counter.__count += 1

    def get(self):
        return Counter.__count

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
print(c2.get())
```

A. `1`
B. `2`
C. `3`
D. An exception is raised.

C

---

**23.** What is the expected output of the following code?

```python
class Node:
    instances = 0

    def __init__(self, val):
        self.val = val
        Node.instances += 1

    def __del__(self):
        Node.instances -= 1

a = Node(1)
b = Node(2)
del a
print(Node.instances)
```

A. `0`
B. `1`
C. `2`
D. An exception is raised.

B - although we didn't have that as far as I can remember, but it seems logical

---

**24.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Base:
    def method(self):
        return 'base'

class Mid(Base):
    def method(self):
        return 'mid'

class Leaf(Mid):
    pass

obj = Leaf()
```

A. `obj.method() == 'base'`
B. `obj.method() == 'mid'`
C. `isinstance(obj, Base)`
D. `type(obj) is Mid`

B, C

---

**25.** What is the expected output of the following code?

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

c = Circle('red', 5)
print(c.color, c.radius)
```

A. An exception is raised.
B. `red 5`
C. `None 5`
D. `red None`

B

---

**26.** What is true about OOP in Python? (Select two answers)

A. `type(obj)` always returns the exact class the object was instantiated from.
B. A child class always inherits all methods from its parent.
C. Overriding a method in a subclass hides the parent's version permanently for all objects.
D. `issubclass(B, A)` returns `True` if `B` is `A` itself.

A, D

---

**27.** Given the inheritance below, which class definitions are valid? (Select two answers)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(C): pass
```

A. `class X(B, D): pass`
B. `class X(D, B): pass`
C. `class X(A, D): pass`
D. `class X(B, C): pass`

B, D

---

**28.** What is the expected output of the following code?

```python
class Formatter:
    def format(self, val):
        return str(val)

    def render(self):
        return f'[{self.format(42)}]'

class HexFormatter(Formatter):
    def format(self, val):
        return hex(val)

f = HexFormatter()
print(f.render())
```

A. `[42]`
B. `[0x2a]`
C. `[hex(42)]`
D. An exception is raised.

A


---

**29.** What is the expected output of the following code?

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(len(C.__mro__))
```

A. `2`
B. `3`
C. `4`
D. An exception is raised.

C

---

**30.** What is true about Python special methods? (Select two answers)

A. `__str__` is called by `print()` and `str()`.
B. `__repr__` is used as a fallback when `__str__` is not defined.
C. Defining `__repr__` makes `str()` always use it instead of `__str__`.
D. `__len__` must return a float.

B, D

---

**31.** What is the expected output of the following code?

```python
def make_multiplier(factor):
    return lambda x: x * factor

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(triple(2)))
```

A. `10`
B. `12`
C. `6`
D. An exception is raised.

B

---

**32.** What is the expected output of the following code?

```python
def gen(n):
    for i in range(n):
        yield i * 2

g = gen(4)
print(next(g))
print(next(g))
print(sum(g))
```

A. `0` / `2` / `10`
B. `0` / `2` / `4`
C. `0` / `2` / `6`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `notes.txt` exists and contains the text `Hello`?

```python
try:
    f = open('notes.txt', 'r+')
    f.write('X')
    f.seek(0)
    print(f.read())
    f.close()
except IOError:
    print(-1)
```

A. `Hello`
B. `Xello`
C. `X`
D. `-1`

C

---

**34.** What is the expected output of the following code?

```python
actions = [lambda x, n=n: x + n for n in range(4)]
print(actions[0](10))
print(actions[3](10))
```

A. `13` / `13`
B. `10` / `13`
C. `13` / `10`
D. `10` / `10`

B

---

**35.** Which of the following statements about `open()` are true? (Select two answers)

A. `'r+'` opens for reading and writing without truncating; file must exist.
B. `'a+'` opens for reading and writing; all writes go to the end.
C. `'w+'` opens for reading only.
D. `'x'` opens an existing file for exclusive writing.

A, B

---

**36.** What is the expected output of the following code?

```python
data = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, data)))
print(result)
```

A. `[9, 36]`
B. `[1, 4, 9, 16, 25, 36]`
C. `[3, 6]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
g = outer(10)
print(f(5))
print(f is g)
```

A. `15` / `True`
B. `15` / `False`
C. `10` / `True`
D. An exception is raised.

B

---

**38.** What is the expected output of the following code?

```python
vals = [-3, -1, 0, 2, 4]
result = list(filter(lambda x: bool(x) and x > 0, vals))
print(result)
```

A. `[2, 4]`
B. `[-3, -1, 2, 4]`
C. `[0, 2, 4]`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row if x % 2 == 0]
print(flat)
```

A. `[2, 4, 6, 8]`
B. `[1, 3, 5, 7, 9]`
C. `[[2], [4, 6], [8]]`
D. An exception is raised.


A


#End - 13:17

---

**40.** What is the expected output of the following code, assuming `log.txt` does not exist?

```python
try:
    f = open('log.txt', 'r')
    data = f.read()
    print(len(data))
except FileNotFoundError:
    print('missing')
except IOError:
    print('io error')
else:
    f.close()
    print('ok')
```

A. `missing`
B. `io error`
C. `0`
D. `ok`

A

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A, D | 21 | B, D |
| 2 | A, C, D | 22 | B |
| 3 | B, D | 23 | A |
| 4 | A | 24 | A, C, D |
| 5 | C | 25 | B |
| 6 | B, C | 26 | A, B, D |
| 7 | A | 27 | A, B, C |
| 8 | B | 28 | C |
| 9 | A, B, D | 29 | C |
| 10 | A | 30 | A, B |
| 11 | B | 31 | A, C |
| 12 | A | 32 | A |
| 13 | A, B, C | 33 | B |
| 14 | A, C, D | 34 | B |
| 15 | A, B, D | 35 | A, B |
| 16 | A, C, D | 36 | B |
| 17 | A, D | 37 | A, C, D |
| 18 | A, C, D | 38 | B |
| 19 | C | 39 | C |
| 20 | B, C | 40 | A |
