# Week 14 — PCAP Mock Exam B (Day 5)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**

#Start 12:16

---

**1.** What is the expected output of the following code?

```python
import math
print(math.sqrt(144))
print(math.pow(2, 10))
print(type(math.pow(2, 10)))
```

A. `12.0` / `1024.0` / `<class 'float'>`
B. `12` / `1024` / `<class 'int'>`
C. `12.0` / `1024.0` / `<class 'int'>`
D. An exception is raised.


B

---

**2.** What is the expected output of the following code?

```python
import os
p = 'reports/2024/q1/summary.csv'
print(os.path.splitext(p)[0])
print(os.path.dirname(os.path.dirname(p)))
```

A. `reports/2024/q1/summary` / `reports/2024`
B. `reports/2024/q1/summary` / `reports`
C. `summary` / `reports/2024`
D. An exception is raised.

B


---

**3.** Which of the following are true about `sys.modules`? (Select two answers)

A. `sys.modules` is a plain `dict` mapping module names to module objects.
B. Deleting a module from `sys.modules` causes it to be re-executed on next import.
C. `sys.modules` only contains modules from the standard library.
D. `sys.modules` is read-only and cannot be modified at runtime.

A, B

---

**4.** What is the expected output of the following code?

```python
import sys

# Assume: python script.py alpha beta gamma
# sys.argv = ['script.py', 'alpha', 'beta', 'gamma']
print(sys.argv[-1])
print(len(sys.argv) - 1)
print(sys.argv[0])
```

A. `gamma` / `3` / `script.py`
B. `alpha` / `3` / `script.py`
C. `gamma` / `4` / `script.py`
D. An exception is raised.

A

---

**5.** Which of the following are true about the `random` module? (Select two answers)

A. `random.uniform(1, 5)` can return exactly `1.0`.
B. `random.randrange(0, 10, 3)` can return `8`.
C. `random.sample([1, 2, 3], 5)` raises `ValueError`.
D. `random.seed()` with no arguments produces reproducible results across runs.

B, C

---

**6.** What is the expected output of the following code?

```python
class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

class QueryError(DatabaseError):
    pass

try:
    raise QueryError('bad SQL')
except ConnectionError:
    print('connection')
except DatabaseError as e:
    print(f'db: {e}')
except Exception:
    print('generic')
```

A. `db: bad SQL`
B. `connection`
C. `generic`
D. An exception is raised.

A

---

**7.** What is the expected output of the following code?

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('zero')
        return 0
    else:
        print('ok')
        return result
    finally:
        print('done')

print(divide(10, 2))
```

A. `ok` / `done` / `5.0`
B. `ok` / `5.0` / `done`
C. `done` / `ok` / `5.0`
D. An exception is raised.

A

---

**8.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    x = 1
except ValueError:
    pass
else:
    print(x)
```

B.
```python
try:
    raise TypeError
except ValueError:
    pass
```

C.
```python
try:
    pass
finally:
    raise RuntimeError
```

D.
```python
try:
    x = int('5')
except (ValueError, TypeError):
    x = 0
finally:
    print(x)
```

A, D

---

**9.** What is the expected output of the following code?

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('cannot divide by zero') from e

try:
    safe_div(1, 0)
except ValueError as e:
    print(str(e))
    print(type(e.__cause__).__name__)
```

A. `cannot divide by zero` / `ZeroDivisionError`
B. `cannot divide by zero` / `ValueError`
C. `ZeroDivisionError` / `ValueError`
D. An exception is raised.

A

---

**10.** What is the expected output of the following code?

```python
class Strict:
    pass

try:
    raise Strict()
except TypeError:
    print('type error')
except Exception:
    print('exception')
```

A. `exception`
B. `type error`
C. Nothing is printed.
D. An exception is raised without being caught.

B - why though?

---

**11.** What is the expected output of the following code?

```python
s = 'abcdefgh'
print(s[7:0:-3])
```

A. `heb`
B. `beh`
C. `hfc`
D. An exception is raised.

A

---

**12.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'PYTHON'
```

A. `s[0:4:2] == 'PT'`
B. `s[1::2] == 'YHN'`
C. `s[-1::-1] == 'PYTHON'`
D. `len(s[2:5]) == 4`

A, B


---

**13.** What is the expected output of the following code?

```python
s = 'abracadabra'
print(s.count('abr'))
print(s.rfind('a'))
```

A. `2` / `10`
B. `2` / `7`
C. `3` / `10`
D. An exception is raised.

A

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello world'.count('l') == 3`
B. `'abc'.ljust(5, '-') == 'abc--'`
C. `'  hello  '.strip() == '  hello'`
D. `'python'.upper()[:3] == 'Pyt'`

A, B

---

**15.** What is the expected output of the following code?

```python
values = [10, 20, 30]
print(f'total={sum(values):05d}')
print(f'first={values[0]:#010x}')
```

A. `total=00060` / `first=0x0000000a`
B. `total=60` / `first=0xa`
C. `total=00060` / `first=000000000a`
D. An exception is raised.

Dude, cut it out. What the fuck is this? I'm not a computer, but a human being.

---

**16.** Which of the following are true about string encoding? (Select two answers)

A. `len('café'.encode('utf-8')) == 5`
B. `'hello'.encode('utf-8') == b'hello'`
C. `b'abc'.decode('utf-8') == b'abc'`
D. `'naïve'.encode('ascii')` completes without error.

Same with above, cut it out. I told you recently to avoid such questions - I'm not a robot. This is irrelevant to real PCAP exam questions.

---

**17.** What is the expected output of the following code?

```python
s = 'hello world'
words = s.split()
result = '-'.join(w.capitalize() for w in words)
print(result)
print(len(words))
```

A. `Hello-World` / `2`
B. `hello-world` / `2`
C. `Hello-World` / `11`
D. An exception is raised.

A

---

**18.** What is the expected output of the following code?

```python
s = 'aabbccdd'
print(s.replace('bb', 'B', 1))
print(s.replace('cc', ''))
```

A. `aaBccdd` / `aabbdd`
B. `aaBBccdd` / `aabbdd`
C. `aaBccdd` / `aabb dd`
D. An exception is raised.

C

---

**19.** What is the expected output of the following code?

```python
items = [1, 'two', 3.0, None]
print(f'{items!r}')
print(f'{len(items)!s}')
```

A. `[1, 'two', 3.0, None]` / `4`
B. `[1, two, 3.0, None]` / `4`
C. `(1, 'two', 3.0, None)` / `4`
D. An exception is raised.

A, BUT AGAIN - WHAT THE FUCK IS THIS AND WHAT'S THE POINT OF THAT?

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

c = Car('BMW')
c.wheels = 3
```

A. `c.wheels == 3`
B. `Car.wheels == 3`
C. `Car.wheels == 4`
D. `'wheels' not in c.__dict__`

A, C

---

**21.** What is the expected output of the following code?

```python
class Converter:
    def convert(self, val):
        return val

    def convert_all(self, items):
        return [self.convert(x) for x in items]

class DoubleConverter(Converter):
    def convert(self, val):
        return val * 2

dc = DoubleConverter()
print(dc.convert_all([1, 2, 3]))
```

A. `[1, 2, 3]`
B. `[2, 4, 6]`
C. `[1, 4, 9]`
D. An exception is raised.

B

---

**22.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Team:
    members = []

t1 = Team()
t2 = Team()
t1.members.append('Alice')
```

A. `t2.members == ['Alice']`
B. `t1.members is t2.members`
C. `'members' in t1.__dict__`
D. `Team.members == []`

A, B

---

**23.** What is the expected output of the following code?

```python
class Bag:
    def __init__(self, items):
        self._items = list(items)

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

b = Bag([10, 20, 30])
print(20 in b)
print(99 not in b)
print(len(b))
```

A. `True` / `True` / `3`
B. `True` / `False` / `3`
C. `False` / `True` / `3`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Printer:
    def format(self, val):
        return str(val)

    def print_all(self, items):
        return [self.format(x) for x in items]

class UpperPrinter(Printer):
    def format(self, val):
        return str(val).upper()

up = UpperPrinter()
```

A. `up.print_all(['a', 'b']) == ['A', 'B']`
B. `up.print_all(['a', 'b']) == ['a', 'b']`
C. `issubclass(UpperPrinter, Printer)`
D. `'print_all' in UpperPrinter.__dict__`

A, C

---

**25.** What is the expected output of the following code?

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'Node({self.val})'

n1 = Node(1)
n2 = Node(2)
n1.next = n2
print(repr(n1))
print(n1.next.val)
```

A. `Node(1)` / `2`
B. `Node(1)` / `Node(2)`
C. `1` / `2`
D. An exception is raised.

A

---

**26.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `issubclass(bool, object)`
B. `isinstance(False, int)`
C. `type(False) is int`
D. `issubclass(str, bytes)`

A, B

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class A: pass
class B(A): pass
class C(B): pass
class D(A): pass
```

A. `class E(C, D): pass`
B. `class E(D, C): pass`
C. `class E(A, C): pass`
D. `class E(C, A, D): pass`

A, B

---

**28.** What is the expected output of the following code?

```python
class Renderer:
    def tag(self, text):
        return text

    def render_list(self, items):
        return [self.tag(x) for x in items]

class BoldRenderer(Renderer):
    def tag(self, text):
        return f'<b>{text}</b>'

br = BoldRenderer()
print(br.render_list(['yes', 'no']))
```

A. `['yes', 'no']`
B. `['<b>yes</b>', '<b>no</b>']`
C. `['<b>yes', '<b>no']`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class Box:
    def __str__(self):
        return 'Box(str)'

b = Box()
print(b)
print(str(b))
print(repr(b))
```

A. `Box(str)` / `Box(str)` / `<__main__.Box object at 0x...>`
B. `Box(str)` / `Box(str)` / `Box(str)`
C. `Box(repr)` / `Box(str)` / `Box(repr)`
D. An exception is raised.

A

---

**30.** Which of the following are true about Python's special methods? (Select two answers)

A. `__add__` is called by the `+` operator.
B. `__str__` is called by `print()`.
C. `__del__` is called when an object is created.
D. `__init__` returns the newly created instance.

A, B

---

**31.** What is the expected output of the following code?

```python
def make_multipliers(factors):
    return [lambda x, f=f: x * f for f in factors]

fns = make_multipliers([2, 3, 5])
print(fns[0](10))
print(fns[2](10))
```

A. `20` / `50`
B. `50` / `50`
C. `10` / `10`
D. An exception is raised.

A

---

**32.** What is the expected output of the following code?

```python
def evens(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

g = evens(8)
print(next(g))
print(next(g))
print(list(g))
```

A. `0` / `2` / `[4, 6, 8]`
B. `0` / `2` / `[0, 2, 4, 6, 8]`
C. `0` / `2` / `[2, 4, 6, 8]`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `config.txt` exists with content `host=localhost\nport=8080`?

```python
with open('config.txt', 'r') as f:
    first = f.readline()
    rest = f.read()

print(first.strip())
print(rest.strip())
```

A. `host=localhost` / `port=8080`
B. `host=localhost` / `host=localhost\nport=8080`
C. `host=localhost\nport=8080` / ``
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]
unique_sorted = sorted(set(data))
print(unique_sorted)
print(unique_sorted[-1])
```

A. `[1, 2, 3, 4, 5, 6, 9]` / `9`
B. `[3, 1, 4, 5, 9, 2, 6]` / `6`
C. `[1, 2, 3, 4, 5, 6, 9]` / `6`
D. An exception is raised.

A

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. Opening a file with `'r+'` requires the file to already exist.
B. `'a+'` opens for both appending and reading; the read position starts at the beginning.
C. `'w'` opens for writing; existing content is preserved and new data is appended.
D. `'x'` opens for reading and creation.

A, D

---

**36.** What is the expected output of the following code?

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
result = dict(zip(keys, values))
print(result)
print(len(result))
```

A. `{'a': 1, 'b': 2, 'c': 3}` / `3`
B. `{'a': 1, 'b': 2, 'c': 3, None: 4}` / `4`
C. `{'a': 1, 'b': 2}` / `2`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
words = ['hello', 'world', 'python']
result = list(map(lambda w: w[0].upper() + w[1:], words))
print(result)
```

A. `['Hello', 'World', 'Python']`
B. `['HELLO', 'WORLD', 'PYTHON']`
C. `['hello', 'world', 'python']`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
nums = range(1, 11)
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
print(sum(evens))
```

A. `[2, 4, 6, 8, 10]` / `30`
B. `[1, 3, 5, 7, 9]` / `25`
C. `[2, 4, 6, 8, 10]` / `40`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
students = [('Zara', 95), ('Alice', 95), ('Bob', 80)]
result = sorted(students, key=lambda s: (-s[1], s[0]))
for name, score in result:
    print(f'{name}: {score}')
```

A. `Alice: 95` / `Zara: 95` / `Bob: 80`
B. `Zara: 95` / `Alice: 95` / `Bob: 80`
C. `Bob: 80` / `Alice: 95` / `Zara: 95`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code?

```python
import os

path = 'archive/data.tar.gz'
name, ext = os.path.splitext(path)
print(name)
print(ext)
```

A. `archive/data.tar` / `.gz`
B. `archive/data` / `.tar.gz`
C. `archive/data.tar.gz` / ``
D. An exception is raised.

A


#End 12:37

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | A | 22 | A, B |
| 3 | A, B | 23 | A |
| 4 | A | 24 | A, C |
| 5 | A, C | 25 | A |
| 6 | A | 26 | A, B |
| 7 | A | 27 | A, B |
| 8 | A, D | 28 | B |
| 9 | A | 29 | A |
| 10 | A | 30 | A, B |
| 11 | A | 31 | A |
| 12 | A, B | 32 | A |
| 13 | A | 33 | A |
| 14 | A, B | 34 | A |
| 15 | A | 35 | A, B |
| 16 | A, B | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | A, C | 40 | A |
