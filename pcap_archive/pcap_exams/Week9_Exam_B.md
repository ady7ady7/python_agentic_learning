# PCAP-31-03 Mock Exam — Week 9, Exam B
**Date:** 2026-03-07/08 | **Time limit:** 65 minutes | **Questions:** 30

Write your answers (letter only) in the Answers section at the bottom.


#Star 19:15
---

## Section 1: Modules & Packages (Q1–Q4)

**Q1:** What is the output?
```python
import os
import os
import os
print(os.sep == os.sep)
```
- A) `False` — each import creates a new object
- B) `True` — modules are cached after the first import
- C) `ImportError`
- D) `AttributeError`

B

**Q2:** What happens when you execute:
```python
from math import sqrt as s, pi as p
print(s(p))
```
- A) `1.7724538509055159`
- B) `3.141592653589793`
- C) `TypeError`
- D) `1.0`

A

**Q3:** Which of these correctly defines `__all__` to export only `foo` and `bar`?
- A) `__all__ = ("foo", "bar")`
- B) `__all__ = {foo, bar}`
- C) `__all__ = [foo, bar]`
- D) `export = ["foo", "bar"]`

C

**Q4:** What is the output?
```python
import sys
sys.path.insert(0, "/tmp/mylibs")
print(sys.path[0])
```
- A) The original first entry in sys.path
- B) `/tmp/mylibs`
- C) `None`
- D) `AttributeError`

B

---

## Section 2: Strings (Q5–Q7)

**Q5:** What is the output?
```python
s = "Hello, World!"
print(s[7:12])
print(s[-6:-1])
```
- A) `World`, `World`
- B) `World`, `orld!`
- C) `orld!`, `World`
- D) `World`, `Worl`

A


**Q6:** What is the output?
```python
s = "one,two,,three"
parts = s.split(",")
print(len(parts))
print(parts[2])
```
- A) `3`, `three`
- B) `4`, `''`
- C) `4`, `three`
- D) `3`, `''`

B

**Q7:** What is the output?
```python
names = ["Alice", "Bob", "Charlie"]
print(", ".join(names))
```
- A) `Alice Bob Charlie`
- B) `Alice, Bob, Charlie`
- C) `['Alice', 'Bob', 'Charlie']`
- D) `TypeError`

B

---

## Section 3: Exception Handling (Q8–Q11)

**Q8:** What is the output?
```python
def f():
    try:
        raise ValueError("v")
    except ValueError:
        print("caught")
        raise

try:
    f()
except ValueError:
    print("outer")
```
- A) `caught`
- B) `outer`
- C) `caught`, `outer`
- D) `ValueError: v`

D

**Q9:** What is the output?
```python
try:
    raise ValueError("v")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError")
```
- A) `ValueError`
- B) `Exception`
- C) Both `Exception` and `ValueError`
- D) `SyntaxError`

B


**Q10:** Which exception type is NOT a subclass of `Exception`?
- A) `ValueError`
- B) `SystemExit`
- C) `RuntimeError`
- D) `OSError`

B

**Q11:** What is the output?
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(type(e).__name__, "—", e)
```
- A) `ValueError — invalid literal for int() with base 10: 'abc'`
- B) `TypeError — invalid literal for int() with base 10: 'abc'`
- C) `Exception — invalid literal for int() with base 10: 'abc'`
- D) `ValueError — abc`

B

---

## Section 4: OOP (Q12–Q16)

**Q12:** What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return super().method() + "B"

class C(A):
    def method(self):
        return super().method() + "C"

class D(B, C):
    pass

print(D().method())
```
- A) `AB`
- B) `ACB`
- C) `ABC`
- D) `AB` — C is never called

C

**Q13:** What is the output?
```python
import random
a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c = random.choice((0, 100, 3))
```
Which of the following values is **impossible** for `c`?
- A) `0`
- B) `3`
- C) `6`
- D) `100`

C

**Q14:** What is the output?
```python
class A:
    x = 1
    def __init__(self):
        self.y = 2

print(hasattr(A, 'x'))
print(hasattr(A, 'y'))
```
- A) `True`, `True`
- B) `True`, `False`
- C) `False`, `True`
- D) `False`, `False`

B


**Q15:** What is the output?
```python
class Foo:
    def __repr__(self):
        return "Foo()"

    def __str__(self):
        return "a Foo"

f = Foo()
print(f)
print(repr(f))
print([f])
```
- A) `a Foo`, `Foo()`, `[a Foo]`
- B) `a Foo`, `Foo()`, `[Foo()]`
- C) `Foo()`, `Foo()`, `[Foo()]`
- D) `a Foo`, `a Foo`, `[a Foo]`

B

**Q16:** What is the output?
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

c = Circle(5)
print(c.r)
```
- A) `5`
- B) `TypeError: Can't instantiate abstract class`
- C) `AttributeError`
- D) `NotImplementedError`

A

---

## Section 5: Generators & Iterators (Q17–Q19)

**Q17:** What is the output?
```python
def f():
    return
    yield

g = f()
print(type(g).__name__)
print(list(g))
```
- A) `generator`, `[]`
- B) `NoneType`, `TypeError`
- C) `function`, `[]`
- D) `generator`, `[None]`

C

**Q18:** What is the output?
```python
def gen():
    yield from range(3)
    yield from range(3)

print(list(gen()))
```
- A) `[0, 1, 2]`
- B) `[0, 1, 2, 0, 1, 2]`
- C) `[0, 1, 2, 3, 4, 5]`
- D) `TypeError`


B

**Q19:** What is the output?
```python
it = iter([10, 20, 30])
print(next(it, "done"))
print(next(it, "done"))
print(next(it, "done"))
print(next(it, "done"))
```
- A) `10`, `20`, `30`, `StopIteration`
- B) `10`, `20`, `30`, `done`
- C) `10`, `20`, `30`, `None`
- D) `10`, `20`, `done`, `done`

B

---

## Section 6: Functional Programming (Q20–Q22)

**Q20:** What is the output?
```python
fns = []
for n in range(3):
    fns.append(lambda x: x + n)

print([f(0) for f in fns])
```
- A) `[0, 1, 2]`
- B) `[2, 2, 2]`
- C) `[0, 0, 0]`
- D) `TypeError`

B


**Q21:** What is the output?
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
print(c(), c(), c())
```
- A) `0 1 2`
- B) `1 2 3`
- C) `1 1 1`
- D) `UnboundLocalError`

B


**Q22:** What is the output?
```python
result = list(map(str, filter(lambda x: x % 2 == 0, range(6))))
print(result)
```
- A) `['0', '2', '4']`
- B) `['1', '3', '5']`
- C) `[0, 2, 4]`
- D) `['0', '1', '2', '3', '4', '5']`

A

---

## Section 7: Standard Streams & chr/ord (Q23–Q25)

**Q23:** What does `sys.stderr` output to by default?
- A) A log file
- B) `/dev/null`
- C) The screen (terminal), same as stdout
- D) The keyboard input buffer

C


**Q24:** What is the output?
```python
print(chr(ord('a') + 3))
```
- A) `'a'`
- B) `'c'`
- C) `'d'`
- D) `100`

C

**Q25:** What is the output?
```python
# module: utils.py
print(__name__)
```
When run as `python utils.py`:
- A) `utils`
- B) `utils.py`
- C) `__main__`
- D) `__utils__`

C

---

## Section 8: File I/O & errno (Q26–Q28)

**Q26:** What is the output?
```python
import errno
print(errno.ENOENT)
```
- A) `1`
- B) `2`
- C) `13`
- D) `9`

B


**Q27:** Which mode string opens a file for exclusive creation (fails if file exists)?
- A) `'w'`
- B) `'a'`
- C) `'x'`
- D) `'r+'`

C


**Q28:** What is the output?
```python
ba = bytearray(b"hello")
ba[0] = 72  # ord('H') == 72
print(ba.decode())
```
- A) `hello`
- B) `Hello`
- C) `TypeError`
- D) `ValueError`

B

---

## Section 9: Scope & Closures (Q29–Q30)

**Q29:** What is the output?
```python
def outer():
    results = []
    for i in range(3):
        results.append(lambda: i)
    return results

fns = outer()
print([f() for f in fns])
```
- A) `[0, 1, 2]`
- B) `[2, 2, 2]`
- C) `[0, 0, 0]`
- D) `[None, None, None]`

B


**Q30:** What is the output?
```python
def f():
    x = 5
    def g():
        print(x)
    x = 10
    g()
    x = 20
    g()

f()
```
- A) `5`, `5`
- B) `10`, `20`
- C) `5`, `10`
- D) `10`, `10`

B

#19:26 - finsihed

---

## Answers

Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
Q9:
Q10:
Q11:
Q12:
Q13:
Q14:
Q15:
Q16:
Q17:
Q18:
Q19:
Q20:
Q21:
Q22:
Q23:
Q24:
Q25:
Q26:
Q27:
Q28:
Q29:
Q30:
