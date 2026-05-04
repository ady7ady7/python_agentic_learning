# Week 12 — Mock Exam B
**PCAP-31-03 Certification Preparation**
Date: 2026-04-03 | Time Limit: 65 minutes | 30 Questions | Passing Score: 70% (21/30)

---

## Question 1

What is the output?

```python
import sys
sys.path.insert(0, '/fake/path')
print(sys.path[0])
```

A) The default first entry of `sys.path`
B) `/fake/path`
C) `None`
D) A `TypeError` is raised

---

## Question 2

Which statement about `__all__` in a module is correct?

A) It restricts which names can be defined inside the module
B) It is mandatory for a module to be importable
C) It controls which names are exported when `from module import *` is used
D) It causes an `ImportError` if a listed name does not exist in the module

---

## Question 3

Given the following package structure:
```
shapes/
    __init__.py
    circle.py
    square.py
```
And `shapes/__init__.py` contains:
```python
from .circle import Circle
```
What does `import shapes` make directly available?

A) `shapes.circle`, `shapes.square`, and `shapes.Circle`
B) Only `shapes.Circle`
C) `shapes.circle` and `shapes.square` only
D) Nothing — you must use `from shapes import *`

---

## Question 4

What is the output?

```python
import os.path as p
print(type(p))
```

A) `<class 'str'>`
B) `<class 'module'>`
C) `<class 'type'>`
D) `<class 'function'>`

---

## Question 5

What does `sys.exit(1)` raise?

A) `RuntimeError`
B) `SystemExit`
C) `ExitError`
D) Nothing — it silently terminates the process

---

## Question 6

What is the output?

```python
s = "PCAP"
print(s.center(8, '-'))
```

A) `--PCAP--`
B) `PCAP----`
C) `----PCAP`
D) `PCAP`

---

## Question 7

What is the output?

```python
text = "one,two,,three"
parts = text.split(',')
print(len(parts))
```

A) `3`
B) `4`
C) `5`
D) A `ValueError` is raised

---

## Question 8

What does `str.rindex(sub)` do when `sub` is not found?

A) Returns `-1`
B) Returns `None`
C) Raises `ValueError`
D) Raises `IndexError`

---

## Question 9

What is the output?

```python
s = "abcdef"
print(s[1:-1:2])
```

A) `'bdf'`
B) `'bd'`
C) `'ace'`
D) `'bce'`

---

## Question 10

Which comparison is True?

A) `'aa' > 'aaa'`
B) `'Z' > 'a'`
C) `'abc' < 'abd'`
D) `'Python' > 'python'`

---

## Question 11

What is the output?

```python
try:
    raise ValueError("bad")
except (TypeError, ValueError) as e:
    print(type(e).__name__)
finally:
    print("done")
```

A) `ValueError` then `done`
B) `done` only
C) `bad` then `done`
D) A `RuntimeError` is raised

---

## Question 12

What is the output?

```python
def risky():
    try:
        return 1
    finally:
        return 2

print(risky())
```

A) `1`
B) `2`
C) `None`
D) A `SyntaxError` is raised

---

## Question 13

What does the `__cause__` attribute of an exception store?

A) The traceback object
B) The exception explicitly chained via `raise X from Y`
C) The message string of the exception
D) The class of the original exception

---

## Question 14

What is the output?

```python
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("wrapped") from e
except ValueError as e:
    print(type(e).__name__)
    print(type(e.__cause__).__name__)
```

A) `ZeroDivisionError` then `ZeroDivisionError`
B) `ValueError` then `ValueError`
C) `ValueError` then `ZeroDivisionError`
D) `ZeroDivisionError` then `ValueError`

---

## Question 15

What is the output?

```python
m = 0

def foo(n):
    global m
    assert n > 0
    try:
        return 10 / n
    except ArithmeticError:
        raise RuntimeError

try:
    foo(0)
except RuntimeError:
    m = 10
except AssertionError:
    m = 5
except:
    m = 1
print(m)
```

A) `0`
B) `10`
C) `5`
D) `1`

---

## Question 16

What is the output?

```python
class A:
    __x = 1
    def get(self): return self.__x

class B(A):
    __x = 2
    def get(self): return self.__x

class C(B):
    __x = 3

obj_c = C()
print(obj_c.get())
```

A) `1`
B) `2`
C) `3`
D) `AttributeError`

---

## Question 17

What is `D.__bases__` given:

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

A) `(A,)`
B) `(B, C, A, object)`
C) `(B, C)`
D) `(D, B, C, A, object)`

---

## Question 18

Which expression is True?

```python
class Shape: pass
class Circle(Shape): pass
c = Circle()
```

A) `type(c) is Shape`
B) `type(c) is Circle`
C) `isinstance(c, type)`
D) `type(c) == Shape`

---

## Question 19

What is the MRO for class `D`?

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

A) `D → A → B → C → object`
B) `D → B → C → A → object`
C) `D → C → B → A → object`
D) `D → B → A → C → object`

---

## Question 20

What is `'area' in Circle.__dict__` given:

```python
class Shape:
    def area(self): return 0

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
```

A) `True` — Circle inherits `area`
B) `False` — `area` is not defined in `Circle`'s own namespace
C) `AttributeError`
D) `True` — instance methods are always in the class `__dict__`

---

## Question 21

What is the output?

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

f = outer()
print(f(), f())
```

A) `15 15`
B) `15 20`
C) `10 15`
D) `UnboundLocalError`

---

## Question 22

What is the output?

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
next(g)
print(list(g))
```

A) `[1, 2, 3]`
B) `[2, 3]`
C) `[1, 2]`
D) `[]`

---

## Question 23

What is the output?

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```

A) `[0, 1, 2]`
B) `[2, 2, 2]`
C) `[0, 0, 0]`
D) `NameError`

---

## Question 24

Which is True about `lambda: 42`?

A) `SyntaxError` — lambda requires at least one parameter
B) Valid — returns `42` when called
C) Valid — but always returns `None`
D) Valid — but cannot be assigned to a variable

---

## Question 25

What is the output?

```python
result = [x for x in range(6, 0, -1) if x % 2 != 0]
print(result)
```

A) `[1, 3, 5]`
B) `[5, 3, 1]`
C) `[6, 4, 2]`
D) `[2, 4, 6]`

---

## Question 26

What is the output?

```python
import os
result = os.path.splitext('report.final.csv')
print(result)
```

A) `('report', '.final.csv')`
B) `('report.final', '.csv')`
C) `('report.final.csv', '')`
D) `['report', 'final', 'csv']`

---

## Question 27

What does `sys.argv[0]` always contain?

A) The first argument passed by the user
B) The name/path of the script being executed
C) The Python interpreter version
D) The current working directory

---

## Question 28

What is the output?

```python
ba = bytearray(b"hello")
ba[0] = 72      # 'H'
print(ba.decode('utf-8'))
```

A) `'hello'`
B) `TypeError` — bytearray is immutable
C) `'Hello'`
D) `'Hllo'` — only the first byte changes the rest disappear

---

## Question 29

Which `open()` mode raises `FileExistsError` if the file already exists?

A) `'w'`
B) `'a'`
C) `'x'`
D) `'r+'`

---

## Question 30

Which `platform` function returns ONLY the OS name as a short string (e.g. `'Windows'`)?

A) `platform.platform()`
B) `platform.uname()`
C) `platform.system()`
D) `platform.node()`

---

## Answer Key

1. B
2. C
3. B
4. B
5. B
6. A
7. B
8. C
9. B
10. C
11. A
12. B
13. B
14. C
15. C
16. B
17. C
18. B
19. B
20. B
21. B
22. B
23. B
24. B
25. B
26. B
27. B
28. C
29. C
30. C

## Scoring Guide

| Score | Result |
|-------|--------|
| 27–30 (90–100%) | Excellent — exam ready |
| 24–26 (80–89%) | Strong — review weak areas |
| 21–23 (70–79%) | Pass threshold — targeted revision needed |
| Below 21 (< 70%) | Fail — significant revision required |
