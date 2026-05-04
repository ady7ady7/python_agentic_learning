# Week 14 — PCAP Mock Exam A (Day 5)
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#11:56
---

**1.** What is the expected output of the following code?

```python
import math
print(math.ceil(-2.1))
print(math.floor(2.9))
print(math.trunc(-2.9))
```

A. `-2` / `2` / `-2`
B. `-3` / `3` / `-3`
C. `-2` / `2` / `-3`
D. An exception is raised.

A

---

**2.** What is the expected output of the following code?

```python
import os
print(os.path.join('/home', 'user', 'file.txt'))
print(os.path.join('/a', '/b', 'c'))
```

A. `/home/user/file.txt` / `/b/c`
B. `/home/user/file.txt` / `/a/b/c`
C. `/home/user/file.txt` / `/a/b`
D. An exception is raised.

B
---

**3.** Which of the following are true about `sys.path`? (Select two answers)

A. `sys.path[0]` is the directory of the script being run.
B. `sys.path` is a tuple and cannot be modified at runtime.
C. `sys.path` can be modified with `.insert()` or `.append()`.
D. `sys.path` contains only directories from the Python installation.

A, C

---

**4.** What is the expected output of the following code?

```python
import sys

# Assume script is run as: python run.py --verbose 42
# sys.argv = ['run.py', '--verbose', '42']
print(sys.argv[1])
print(len(sys.argv))
print(type(sys.argv[2]))
```

A. `--verbose` / `3` / `<class 'str'>`
B. `run.py` / `3` / `<class 'str'>`
C. `--verbose` / `2` / `<class 'int'>`
D. An exception is raised.

A

---

**5.** Which of the following are true about the `random` module? (Select two answers)

A. `random.randint(1, 5)` can return `5`.
B. `random.randrange(1, 5)` can return `5`.
C. `random.choice([])` returns `None`.
D. `random.random()` returns a float in `[0.0, 1.0)`.

C, D

---

**6.** What is the expected output of the following code?

```python
class NetworkError(Exception):
    pass

class TimeoutError(NetworkError):
    pass

try:
    raise TimeoutError('connection timed out')
except NetworkError as e:
    print(type(e).__name__)
    print(str(e))
except TimeoutError:
    print('timeout branch')
```

A. `TimeoutError` / `connection timed out`
B. `NetworkError` / `connection timed out`
C. `timeout branch`
D. An exception is raised.

A

---

**7.** What is the expected output of the following code?

```python
def fetch(x):
    try:
        if x < 0:
            raise ValueError('negative')
        return x * 2
    except ValueError:
        return -1
    finally:
        print('cleanup')

print(fetch(-3))
print(fetch(5))
```

A. `cleanup` / `-1` / `cleanup` / `10`
B. `-1` / `cleanup` / `10` / `cleanup`
C. `cleanup` / `cleanup` / `-1` / `10`
D. An exception is raised.


A

---

**8.** Which of the following snippets executes without raising any unhandled exception? (Select two answers)

A.
```python
try:
    pass
except Exception:
    pass
else:
    x = 1
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
    x = 1 / 0
except ZeroDivisionError:
    pass
finally:
    print('ok')
```

D.
```python
try:
    raise KeyError
except Exception:
    raise
```

A, C

---

**9.** What is the expected output of the following code?

```python
try:
    try:
        x = int('bad')
    except ValueError:
        print('inner caught')
        raise RuntimeError('wrapped')
except RuntimeError as e:
    print(str(e))
print('done')
```

A. `inner caught` / `wrapped` / `done`
B. `inner caught` / `done`
C. `wrapped` / `done`
D. An exception is raised.

A

---

**10.** What is the expected output of the following code?

```python
def convert(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

print(convert('42'))
print(convert('abc'))
print(convert(None))
```

A. `42` / `None` / `None`
B. `42` / `None` / `0`
C. `'42'` / `None` / `None`
D. An exception is raised.

a

---

**11.** What is the expected output of the following code?

```python
s = 'abcdefgh'
print(s[6:1:-2])
```

A. `gec`
B. `ceg`
C. `hfd`
D. An exception is raised.


A

---

**12.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'abcdefgh'
```

A. `s[1:5] == 'bcde'`
B. `s[-3:] == 'fgh'`
C. `s[2:2] == ' '`
D. `s[::-1][0] == 'a'`

A, B

---

**13.** What is the expected output of the following code?

```python
s = 'hello world'
print(s.find('xyz'))
print(s.index('world'))
```

A. `-1` / `6`
B. `0` / `6`
C. `-1` / `-1`
D. An exception is raised.

A

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'hello'.startswith('he')`
B. `'  x  '.strip() == 'x'`
C. `'abc'.center(5, '*') == '**abc'`
D. `'hello'.find('z') == 0`

A, B

---

**15.** What is the expected output of the following code?

```python
val = 3.14159
name = 'Alice'
print(f'{val:.3f}')
print(f'{name:>10}')
```

A. `3.142` / `     Alice`
B. `3.141` / `Alice     `
C. `3.14159` / `     Alice`
D. An exception is raised.

A

---

**16.** Which of the following are true about string encoding? (Select two answers)

A. `b'hello'.decode('ascii') == 'hello'`
B. `'café'.encode('ascii')` raises `UnicodeEncodeError`.
C. `'hello'.encode('utf-8') == 'hello'`
D. `b'\x41'.decode('ascii') == 'B'`


What the fuck is this shit dude. I didn't have it, fuck off - cut it out.

---

**17.** What is the expected output of the following code?

```python
s = 'one:two:three'
print(s.partition(':'))
print(s.rpartition(':'))
```

A. `('one', ':', 'two:three')` / `('one:two', ':', 'three')`
B. `('one', ':', 'two:three')` / `('one', ':', 'two:three')`
C. `['one', 'two', 'three']` / `['one', 'two', 'three']`
D. An exception is raised.

Same, this is some bullshit, cut it out.

---

**18.** What is the expected output of the following code?

```python
s = 'Python'
print(''.join(reversed(s)))
print(s[::-1] == ''.join(reversed(s)))
```

A. `nohtyP` / `True`
B. `nohtyP` / `False`
C. `Python` / `True`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
s = 'caf\u00e9'
print(f'{s!r}')
print(f'{s!a}')
```

A. `'café'` / `'caf\\u00e9'`
B. `café` / `caf\u00e9`
C. `'café'` / `'café'`
D. An exception is raised.

What the fuck is this bullshit, cut it out!

---

**20.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Point:
    origin = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
```

A. `'x' in p.__dict__`
B. `'origin' in p.__dict__`
C. `'origin' in Point.__dict__`
D. `'__init__' in p.__dict__`

A, C

---

**21.** What is the expected output of the following code?

```python
class Logger:
    def format(self, msg):
        return msg

    def log(self, msg):
        print(self.format(msg))

class PrefixLogger(Logger):
    def format(self, msg):
        return f'[INFO] {msg}'

pl = PrefixLogger()
pl.log('started')
```

A. `started`
B. `[INFO] started`
C. `[INFO] [INFO] started`
D. An exception is raised.

B

---

**22.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Counter:
    total = 0

c1 = Counter()
c2 = Counter()
c1.total = 10
Counter.total = 5
```

A. `c1.total == 10`
B. `c2.total == 5`
C. `Counter.total == 10`
D. `c2.total == 0`

A, B

---

**23.** What is the expected output of the following code?

```python
class Menu:
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

m = Menu(['a', 'b', 'c'])
print(len(m))
print(m[1])
print(m[-1])
```

A. `3` / `b` / `c`
B. `3` / `a` / `c`
C. `2` / `b` / `c`
D. An exception is raised.

A

---

**24.** Assuming the snippet executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f'area={self.area()}'

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

sq = Square(4)
```

A. `sq.describe() == 'area=16'`
B. `sq.describe() == 'area=0'`
C. `isinstance(sq, Shape)`
D. `'describe' in Square.__dict__`

A, C

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

class D(C):
    def greet(self):
        return super().greet() + 'D'

print(D().greet())
```

A. `ABCD`
B. `DCBA`
C. `AD`
D. An exception is raised.

A

---

**26.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `isinstance(True, int)`
B. `isinstance([], tuple)`
C. `issubclass(float, int)`
D. `type(1) is int`

A, D

---

**27.** Given the inheritance below, which class definitions produce a valid MRO? (Select two answers)

```python
class P: pass
class Q(P): pass
class R(P): pass
class S(Q, R): pass
```

A. `class T(S, R): pass`
B. `class T(P, S): pass`
C. `class T(S, Q): pass`
D. `class T(R, Q, S): pass`

A, C

---

**28.** What is the expected output of the following code?

```python
class Serializer:
    def serialize(self, val):
        return str(val)

    def dump(self, items):
        return ', '.join(self.serialize(x) for x in items)

class JsonSerializer(Serializer):
    def serialize(self, val):
        return f'"{val}"'

js = JsonSerializer()
print(js.dump([1, 2, 3]))
```

A. `1, 2, 3`
B. `"1", "2", "3"`
C. `'1', '2', '3'`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class Dog:
    def __repr__(self):
        return 'Dog(repr)'

d = Dog()
print(d)
print(repr(d))
print(str(d))
```

A. `Dog(repr)` / `Dog(repr)` / `Dog(repr)`
B. `Dog(repr)` / `Dog(repr)` / `Dog`
C. `Dog` / `Dog(repr)` / `Dog(repr)`
D. An exception is raised.

A

---

**30.** Which of the following are true about Python's special methods? (Select two answers)

A. `__eq__` is called by the `==` operator.
B. `__contains__` is called by both `in` and `not in` operators.
C. `__len__` must return a string representing the length.
D. `__repr__` is only called in interactive Python sessions.

A, B

---

**31.** What is the expected output of the following code?

```python
def make_counter(start=0):
    count = [start]
    def increment():
        count[0] += 1
        return count[0]
    return increment

c = make_counter(10)
print(c())
print(c())
print(make_counter()())
```

A. `11` / `12` / `1`
B. `11` / `11` / `1`
C. `10` / `11` / `0`
D. An exception is raised.

A

---

**32.** What is the expected output of the following code?

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

result = list(flatten([1, [2, [3, 4]], 5]))
print(result)
print(len(result))
```

A. `[1, 2, 3, 4, 5]` / `5`
B. `[1, [2, [3, 4]], 5]` / `3`
C. `[1, 2, [3, 4], 5]` / `4`
D. An exception is raised.

A

---

**33.** What is the expected output of the following code, assuming `data.txt` exists with content `alpha\nbeta\ngamma\n`?

```python
with open('data.txt', 'r') as f:
    lines = f.readlines()

print(len(lines))
print(lines[0].strip())
print(lines[-1].strip())
```

A. `3` / `alpha` / `gamma`
B. `3` / `alpha` / ``
C. `4` / `alpha` / `gamma`
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
records = [('bob', 30), ('alice', 25), ('carol', 30), ('dave', 25)]
result = sorted(records, key=lambda r: (r[1], r[0]))
print(result[0])
print(result[-1])
```

A. `('alice', 25)` / `('carol', 30)`
B. `('dave', 25)` / `('bob', 30)`
C. `('alice', 25)` / `('bob', 30)`
D. An exception is raised.

A

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. `'w+'` opens for reading and writing, and truncates the existing file.
B. `'r'` opens for reading and writing.
C. `'a'` opens for appending; all writes go to the end of the file.
D. `'w'` raises `FileNotFoundError` if the file does not exist.

A, C

---

**36.** What is the expected output of the following code?

```python
a = [1, 2, 3]
b = ['x', 'y']
result = list(zip(a, b))
print(result)
print(len(result))
```

A. `[(1, 'x'), (2, 'y')]` / `2`
B. `[(1, 'x'), (2, 'y'), (3, None)]` / `3`
C. `[(1, 'x'), (2, 'y'), (3,)]` / `3`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, nums))
print(result)
print(sum(result))
```

A. `[1, 4, 9, 16, 25]` / `55`
B. `[2, 4, 6, 8, 10]` / `30`
C. `[1, 4, 9, 16, 25]` / `25`
D. An exception is raised.

A

---

**38.** What is the expected output of the following code?

```python
values = [0, '', None, 1, 'hello', [], False, 42]
result = list(filter(None, values))
print(result)
print(len(result))
```

A. `[1, 'hello', 42]` / `3`
B. `[0, '', None, 1, 'hello', [], False, 42]` / `8`
C. `[None, False]` / `2`
D. An exception is raised.

A

---

**39.** What is the expected output of the following code?

```python
items = ['banana', 'apple', 'cherry', 'apricot']
result = sorted(items, key=lambda s: (s[0], len(s)))
print(result[0])
print(result[1])
```

A. `apple` / `apricot`
B. `apricot` / `apple`
C. `apple` / `banana`
D. An exception is raised.

A

---

**40.** What is the expected output of the following code, assuming `log.txt` already exists?

```python
try:
    with open('log.txt', 'x') as f:
        f.write('new entry')
    print('created')
except FileExistsError:
    print('already exists')
finally:
    print('finished')
```

A. `already exists` / `finished`
B. `created` / `finished`
C. `already exists`
D. `finished`

A

#End 12:16

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A | 21 | B |
| 2 | A | 22 | A, B |
| 3 | A, C | 23 | A |
| 4 | A | 24 | A, C |
| 5 | A, D | 25 | A |
| 6 | A | 26 | A, D |
| 7 | A | 27 | A, C |
| 8 | A, C | 28 | B |
| 9 | A | 29 | A |
| 10 | A | 30 | A, B |
| 11 | A | 31 | A |
| 12 | A, B | 32 | A |
| 13 | A | 33 | A |
| 14 | A, B | 34 | A |
| 15 | A | 35 | A, C |
| 16 | A, B | 36 | A |
| 17 | A | 37 | A |
| 18 | A | 38 | A |
| 19 | A | 39 | A |
| 20 | A, C | 40 | A |
