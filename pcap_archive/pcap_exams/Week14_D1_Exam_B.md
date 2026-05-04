# Week 14 — PCAP Mock Exam B
**40 Questions | Passing Score: 70% (28/40) | Time: 65 min**


#Start 13:17

---

**1.** Which of the following are true about the `os` module? (Select two answers)

A. `os.getcwd()` returns the current working directory as a string.
B. `os.path.split('/home/user/file.txt')` returns `('/home/user', 'file.txt')`.
C. `os.listdir()` returns a sorted list of files in the current directory.
D. `os.path.exists()` raises an exception if the path does not exist.

A, B

---

**2.** What is true about the `import` statement? (Select two answers)

A. `import math as m` allows using `m.sqrt()` instead of `math.sqrt()`.
B. `from os import path, getcwd` imports two names into the current namespace.
C. `import math.sqrt` is a valid way to import the `sqrt` function directly.
D. `from module import *` always imports all names including those starting with `_`.

A, B

---

**3.** What is true about Python packages? (Select two answers)

A. A package is a directory that organises related modules.
B. Sub-packages are imported automatically when a parent package is imported.
C. `__init__.py` is executed when the package is first imported.
D. `.pyc` files are source files that have not yet been compiled.

A, B

---

**4.** What is the expected output of the following code?

```python
import os
path = 'reports/2024/summary.csv'
head, tail = os.path.split(path)
root, ext = os.path.splitext(tail)
print(root)
print(ext)
```

A. `summary` / `.csv`
B. `reports/2024` / `summary.csv`
C. `summary.csv` / ``
D. An exception is raised.

A

---

**5.** What is the expected output of the following code?

```python
import sys
sys.path.insert(0, '/custom')
print(sys.path[0])
print(type(sys.path) is list)
```

A. `/custom` / `True`
B. `/custom` / `False`
C. An exception is raised.
D. `` / `True`

A

---

**6.** Assuming the code below executes successfully, which expressions always evaluate to `True`? (Select two answers)

```python
import random
items = ['a', 'b', 'c', 'd']
choice = random.choice(items)
```

A. `choice == 'a'`
B. `choice in items`
C. `type(choice) is str`
D. `len(choice) > 1`

B, C

---

**7.** What is the expected output of the following code?

```python
class Oops(Exception):
    pass

try:
    raise Oops
except Oops as e:
    print(type(e).__name__)
    print(isinstance(e, Exception))
```

A. `Oops` / `True`
B. `Exception` / `True`
C. `Oops` / `False`
D. An exception is raised.

A

---

**8.** What is the expected behavior of the following code?

```python
def risky():
    try:
        return 1 / 0
    except ZeroDivisionError:
        raise RuntimeError('fail')
    finally:
        print('finally')

try:
    risky()
except RuntimeError as e:
    print(str(e))
```

A. `finally` / `fail`
B. `fail` / `finally`
C. `finally` only
D. Raises unhandled `ZeroDivisionError`

A



---

**9.** Which of the following snippets will execute without raising any unhandled exceptions? (Select two answers)

A.
```python
try:
    raise TypeError
except (TypeError, ValueError):
    pass
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
except ValueError:
    x = -1
finally:
    x += 1
```

D.
```python
try:
    x = [][1]
except IndexError:
    raise ValueError
except ValueError:
    pass
```

A, C

---

**10.** What is the expected output of the following code?

```python
def f(n):
    try:
        if n == 0:
            raise ValueError
        return n * 2
    except ValueError:
        return -1
    finally:
        return 99

print(f(5))
print(f(0))
```

A. `10` / `-1`
B. `99` / `99`
C. `10` / `99`
D. `-1` / `99`

B

---

**11.** What is the expected output of the following code?

```python
try:
    x = int(None)
except TypeError as e:
    print(type(e).__name__)
except ValueError:
    print('value')
```

A. `ValueError`
B. `TypeError`
C. `value`
D. The code is erroneous and will not execute.

B
This is confusing for me, e.g. when it is TypErro and when ValueError in similar cases.


---

**12.** What is the expected output of the following code?

```python
s = 'Hello, World!'
print(s.count('l'))
print(s.index('W'))
```

A. `3` / `7`
B. `2` / `6`
C. `3` / `6`
D. An exception is raised.

A

---

**13.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
s = 'abcdef'
t = s[1:5:2] #bd
```

A. `t == 'bd'`
B. `len(t) == 3`
C. `t[0] == 'b'`
D. `t[-1] == 'e'`

A, C

---

**14.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'python'.find('xy') == -1`
B. `'python'.index('py') == 0`
C. `'python'.rindex('on') == 4`
D. `'python'.rfind('z') == 0`

A, B, C (it seems to me like both B, C are true, they're very similar here)

---

**15.** Which of the following statements about string methods are true? (Select two answers)

A. `'abc'.upper()` returns `'ABC'`.
B. `'  x  '.strip()` returns `'x'`.
C. `'hello'.replace('l', 'r', 1)` returns `'herlo'`.
D. `'abc'.split('')` returns `['a', 'b', 'c']`.


A, B, C - all three are True
---

**16.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'aa' < 'aaa'`
B. `'z' < 'A'`
C. `'1' < '2' < '9'`
D. `'abc' > 'ABC'`

A, C, D - all three are True nigga.

---

**17.** Which of the following expressions evaluate to `True`? (Select two answers)

A. `'cat' in 'concatenate'`
B. `str(True) in 'TrueOrFalse'`
C. `'xyz' not in 'abcxyz'`
D. `'bc' not in 'abcd'`

A, B 

---

**18.** What is the expected output of the following code?

```python
s = 'mississippi'
print(s.count('ss'))
print(s.find('ss'))
print(s.rfind('ss'))
```

A. `2` / `2` / `5`
B. `1` / `2` / `5`
C. `2` / `2` / `2`
D. An exception is raised.

A

---

**19.** What is the expected output of the following code?

```python
words = ['one', 'two', 'three']
s = ', '.join(words)
print(s)
print(len(s.split(', ')))
```

A. `one, two, three` / `3`
B. `one two three` / `3`
C. `one, two, three` / `2`
D. An exception is raised.

A


---

**20.** Assuming the code below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

c = Car(120, 'BMW')
```

A. `hasattr(c, 'speed')`
B. `'speed' in Car.__dict__`
C. `len(Car.__bases__) == 1`
D. `type(c) is Vehicle`

A, C

---

**21.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class MyClass:
    x = y = 0

    def __init__(self):
        self.z = 1

obj = MyClass()
```

A. `'x' in obj.__dict__`
B. `'z' in obj.__dict__`
C. `'x' in MyClass.__dict__`
D. `'z' in MyClass.__dict__`

B, C

---

**22.** What is the expected output of the following code?

```python
class Wallet:
    balance = 1000

    def deposit(self, amount):
        Wallet.balance += amount

w1 = Wallet()
w2 = Wallet()
w1.deposit(500)
print(w2.balance)
```

A. `1000`
B. `500`
C. `1500`
D. An exception is raised.

C

---

**23.** What is the expected output of the following code?

```python
class Foo:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __str__(self):
        return f'Foo({self.x})'

a = Foo(3)
b = Foo(3)
print(a == b)
print(str(a))
print(a is b)
```

A. `True` / `Foo(3)` / `True`
B. `True` / `Foo(3)` / `False`
C. `False` / `Foo(3)` / `False`
D. An exception is raised.

B

---

**24.** Assuming the snippet below executes successfully, which expressions evaluate to `True`? (Select two answers)

```python
class P:
    def speak(self):
        return 'P'

class Q(P):
    def speak(self):
        return 'Q'

class R(Q):
    pass

r = R()
```

A. `r.speak() == 'P'`
B. `r.speak() == 'Q'`
C. `'speak' in R.__dict__`
D. `issubclass(R, P)`

B, D

---

**25.** What is the expected output of the following code?

```python
class A:
    def __init__(self):
        self.val = 1

class B(A):
    pass

class C(B):
    def __init__(self):
        super().__init__()
        self.val = 3

obj = C()
print(obj.val)
print(isinstance(obj, A))
```

A. `1` / `True`
B. `3` / `True`
C. `3` / `False`
D. An exception is raised.

B

---

**26.** What is true about Python OOP? (Select two answers)

A. `__bases__` contains only the direct parent classes.
B. `__mro__` always ends with `object`.
C. `super()` always calls the method from the direct parent class.
D. Multiple inheritance is not supported in Python.

A, B

---

**27.** Given the inheritance below, which class definitions are valid? (Select two answers)

```python
class A: pass
class B(A): pass
class C(B): pass
```

A. `class X(C, B): pass`
B. `class X(B, C): pass`
C. `class X(A, C): pass`
D. `class X(C, A): pass`

A, D

---

**28.** What is the expected output of the following code?

```python
class Processor:
    def process(self, val):
        return val

    def run(self):
        data = [1, 2, 3]
        return [self.process(x) for x in data]

class Doubler(Processor):
    def process(self, val):
        return val * 2

d = Doubler()
print(d.run())
```

A. `[1, 2, 3]`
B. `[2, 4, 6]`
C. `[1, 4, 9]`
D. An exception is raised.

B

---

**29.** What is the expected output of the following code?

```python
class A: pass
class B(A): pass

print(issubclass(B, A))
print(issubclass(A, B))
print(issubclass(A, A))
```

A. `True` / `False` / `True`
B. `True` / `True` / `True`
C. `True` / `False` / `False`
D. An exception is raised.

A

---

**30.** What is true about Python's `__repr__` and `__str__`? (Select two answers)

A. If only `__repr__` is defined, `str(obj)` uses it as a fallback.
B. If only `__str__` is defined, `repr(obj)` uses it as a fallback.
C. `repr(e)` for an exception always ignores `__str__` and uses `e.args`.
D. `print(obj)` calls `repr(obj)` directly.

A, C

---

**31.** What is the expected output of the following code?

```python
fs = [lambda x: x + i for i in range(4)]
print(fs[0](0))
print(fs[0](0) == fs[3](0))
```

A. `0` / `True`
B. `3` / `True`
C. `0` / `False`
D. `3` / `False`

B


---

**32.** What is the expected output of the following code?

```python
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1

g = counter(5)
print(next(g))
print(next(g))
print(next(g))
```

A. `5` / `6` / `7`
B. `0` / `1` / `2`
C. `5` / `5` / `5`
D. Raises `StopIteration`

A

---

**33.** What is the expected output of the following code, assuming `data.txt` exists with content `abcde`?

```python
with open('data.txt', 'r') as f:
    chunk = f.read(2)
    rest = f.read()
print(chunk)
print(rest)
```

A. `ab` / `cde`
B. `abcde` / ``
C. `ab` / `abcde`
D. An exception is raised.

A

---

**34.** What is the expected output of the following code?

```python
def apply_all(fns, val):
    return [f(val) for f in fns]

ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
print(apply_all(ops, 3))
```

A. `[4, 6, 9]`
B. `[4, 8, 16]`
C. `[3, 6, 9]`
D. An exception is raised.

A

---

**35.** Which of the following statements about file modes are true? (Select two answers)

A. `'w'` truncates the file if it exists.
B. `'a'` raises `FileNotFoundError` if the file does not exist.
C. `'x'` fails if the file already exists.
D. `'r'` creates the file if it does not exist.

A, C

---

**36.** What is the expected output of the following code?

```python
nums = range(1, 6)
squared = map(lambda x: x ** 2, nums)
evens = filter(lambda x: x % 2 == 0, squared)
print(list(evens))
```

A. `[4, 16]`
B. `[1, 4, 9, 16, 25]`
C. `[2, 4]`
D. An exception is raised.

A

---

**37.** What is the expected output of the following code?

```python
def make_greeting(prefix):
    def greet(name):
        return f'{prefix}, {name}!'
    return greet

hello = make_greeting('Hello')
hi = make_greeting('Hi')
print(hello('Alice'))
print(hi('Bob'))
print(hello is hi)
```

A. `Hello, Alice!` / `Hi, Bob!` / `True`
B. `Hello, Alice!` / `Hi, Bob!` / `False`
C. `Hi, Alice!` / `Hi, Bob!` / `False`
D. An exception is raised.

B

---

**38.** What is the expected output of the following code?

```python
data = [0, '', None, 1, 'a', [], [0]]
result = list(filter(bool, data))
print(len(result))
```

A. `7`
B. `3`
C. `4`
D. An exception is raised.

B

---

**39.** What is the expected output of the following code?

```python
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
print(sorted_pairs[0])
print(sorted_pairs[-1])
```

A. `(3, 'a')` / `(1, 'b')`
B. `(1, 'b')` / `(3, 'a')`
C. `(3, 'a')` / `(2, 'c')`
D. An exception is raised.


A

---

**40.** What is the expected output of the following code, assuming `config.txt` already exists?

```python
try:
    f = open('config.txt', 'x')
    print(1)
except FileExistsError:
    print(2)
except IOError:
    print(3)
else:
    f.close()
    print(4)
```

A. `1` then `4`
B. `2`
C. `3`
D. `1`

B

#End - 13:40

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | A, B | 21 | B, C |
| 2 | A, B | 22 | C |
| 3 | A, C | 23 | B |
| 4 | A | 24 | B, D |
| 5 | A | 25 | B |
| 6 | B, C | 26 | A, B |
| 7 | A | 27 | A, D |
| 8 | A | 28 | B |
| 9 | A, C | 29 | A |
| 10 | B | 30 | A, C |
| 11 | B | 31 | B |
| 12 | A | 32 | A |
| 13 | A, C | 33 | A |
| 14 | A, B, C | 34 | A |
| 15 | A, B, C | 35 | A, C |
| 16 | A, C, D | 36 | A |
| 17 | A, B | 37 | B |
| 18 | A | 38 | B |
| 19 | A | 39 | A |
| 20 | A, C | 40 | B |
