# PCAP-31-03 Mock Exam — Week 9, Exam A
**Date:** 2026-03-07/08 | **Time limit:** 65 minutes | **Questions:** 30

Write your answers (letter only) in the Answers section at the bottom.

---

## Section 1: Modules & Packages (Q1–Q4)

#sTART 18:41

**Q1:** What is the output?
```python
# mymod.py
x = 10

# main.py
import mymod
mymod.x = 99
import mymod
print(mymod.x)
```
- A) `10`
- B) `99`
- C) `AttributeError`
- D) `ImportError`

B

**Q2:** What happens?
```python
from os.path import join, exists
join = "overwritten"
print(exists("/"))
```
- A) `True`
- B) `False`
- C) `NameError`
- D) `TypeError`

B

**Q3:** Which statement about `__init__.py` is TRUE?
- A) It is required in Python 3 to make a directory a package
- B) It is optional in Python 3 but its presence controls what `from package import *` exports
- C) It runs only when `from package import *` is called, not on regular import
- D) It can only contain `__all__` assignments

A

**Q4:** What is the output?
```python
import sys
print(type(sys.path))
```
- A) `<class 'tuple'>`
- B) `<class 'list'>`
- C) `<class 'set'>`
- D) `<class 'dict'>`

B

---

## Section 2: Strings (Q5–Q7)

**Q5:** What is the output?
```python
s = "hello world"
print(s.find("xyz"))
print(s.index("xyz"))
```
- A) `-1`, then `ValueError`
- B) `-1`, `-1`
- C) `ValueError`, `ValueError`
- D) `None`, `ValueError`

A


**Q6:** What is the output?
```python
s = "  hello  "
print(repr(s.strip()))
print(repr(s.lstrip()))
```
- A) `'hello'`, `'hello  '`
- B) `'hello'`, `'  hello'`
- C) `'hello  '`, `'hello'`
- D) `'hello'`, `'hello'`

A


**Q7:** What is the output?
```python
s = "abcabc"
print(s.replace("a", "X", 1))
```
- A) `XbcXbc`
- B) `Xbcabc`
- C) `abcXbc`
- D) `XbcXbc` — replaces all occurrences

B

---

## Section 3: Exception Handling (Q8–Q11)

**Q8:** What is the output?
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("zero")
else:
    print("else")
finally:
    print("finally")
```
- A) `zero`, `finally`
- B) `else`, `finally`
- C) `zero`, `else`, `finally`
- D) `finally`

A

**Q9:** What is the output?
```python
try:
    raise ValueError("v")
except ValueError as e:
    pass

print(e)
```
- A) `v`
- B) `ValueError: v`
- C) `NameError: name 'e' is not defined`
- D) `None`

A

**Q10:** Which is the correct hierarchy?
- A) `Exception` → `BaseException` → `ArithmeticError` → `ZeroDivisionError`
- B) `BaseException` → `Exception` → `ArithmeticError` → `ZeroDivisionError`
- C) `BaseException` → `Exception` → `ZeroDivisionError` → `ArithmeticError`
- D) `Exception` → `ArithmeticError` → `BaseException` → `ZeroDivisionError`

B

**Q11:** What is the output?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```
- A) `1`
- B) `2`
- C) `RuntimeError`
- D) `1` then `2`

B

---

## Section 4: OOP (Q12–Q16)

**Q12:** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

b = B()
print(b.x, b.y)
```
- A) `AttributeError`
- B) `1 2`
- C) `None 2`
- D) `1 None`

B

**Q13:** What is the output?
```python
class A:
    def greet(self):
        return "A"

class B(A):
    pass

class C(B):
    def greet(self):
        return super().greet() + "C"

print(C().greet())
```
- A) `AC`
- B) `BC`
- C) `ABC`
- D) `AttributeError`

A

**Q14:** What is the output?
```python
class Foo:
    __x = 10

f = Foo()
print(f.__x)
```
- A) `10`
- B) `None`
- C) `AttributeError`
- D) `NameError`

C

**Q15:** What does `__slots__` do?
- A) Makes all attributes read-only
- B) Restricts instances to only the declared attributes, saving memory
- C) Hides attributes from `dir()`
- D) Prevents inheritance

we didn't have that, i discard that question. And it's not PCAP relevant.

**Q16:** What is the output?
```python
class A:
    def __init__(self):
        self._x = 1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val * 2

a = A()
a.x = 5
print(a.x)
```
- A) `5`
- B) `10`
- C) `AttributeError`
- D) `1`

B
---

## Section 5: Generators & Iterators (Q17–Q19)

**Q17:** What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
g.close()
print(next(g))
```
- A) `1`, `2`, `3`
- B) `1`, `2`, raises `StopIteration`
- C) `1`, `2`, raises `GeneratorExit`
- D) `1`, `2`, `None`

we didn't have close, not PCAP relevant.... I discard the question

**Q18:** What is the output?
```python
xs = [1, 2, 3]
it = iter(xs)
print(next(it))
xs.append(4)
print(list(it))
```
- A) `1`, `[2, 3]`
- B) `1`, `[2, 3, 4]`
- C) `1`, `[1, 2, 3, 4]`
- D) `StopIteration`

B

**Q19:** What is the output?
```python
def counter(start):
    while True:
        yield start
        start += 1

c = counter(5)
print([next(c) for _ in range(3)])
```
- A) `[5, 6, 7]`
- B) `[5, 5, 5]`
- C) `[0, 1, 2]`
- D) `RuntimeError`

A

---

## Section 6: Functional Programming (Q20–Q22)

**Q20:** What is the output?
```python
fns = [lambda x, n=n: x + n for n in range(3)]
print([f(10) for f in fns])
```
- A) `[10, 10, 10]`
- B) `[10, 11, 12]`
- C) `[12, 12, 12]`
- D) `TypeError`

B

**Q21:** What is the output?
```python
from functools import reduce
result = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])
print(result)
```
- A) `10`
- B) `24`
- C) `[1, 2, 6, 24]`
- D) `TypeError`

B

**Q22:** What is the output?
```python
xs = [1, -2, 3, -4, 5]
pos = list(filter(lambda x: x > 0, xs))
doubled = list(map(lambda x: x * 2, pos))
print(doubled)
```
- A) `[2, 6, 10]`
- B) `[2, -4, 6, -8, 10]`
- C) `[1, 3, 5]`
- D) `[-4, -8]`

A

---

## Section 7: Logging (Q23–Q25)

**Q23:** What is the numeric value of `logging.WARNING`?
- A) `10`
- B) `20`
- C) `30`
- D) `40`

C

**Q24:** What is the output? (Count lines printed to stderr/stdout)
```python
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
logger.setLevel(logging.WARNING)

logger.debug("debug")
logger.warning("warn")
```
- A) 0 lines
- B) 1 line — `warn`
- C) 2 lines — `debug`, `warn`
- D) 1 line — `debug`

B
Do not focus on it if it's wrong - it's not even PCAP relevant and PCAP is priority now

**Q25:** What is the output?
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

logging.debug("debug")
logging.error("error")
```
- A) Both `debug` and `error`
- B) Only `error`
- C) Only `debug`
- D) Nothing — no handlers configured

A
Do not focus on it if it's wrong - it's not even PCAP relevant and PCAP is priority now

---

## Section 8: File I/O & errno (Q26–Q28)

**Q26:** Which statement is TRUE about `IOError` in Python 3?
- A) `IOError` is a subclass of `OSError`
- B) `IOError is OSError` evaluates to `True`
- C) `IOError` only applies to file operations, not network
- D) `IOError` does not exist in Python 3

A

**Q27:** What does `readinto(buf)` return?
- A) A new `bytes` object with the file contents
- B) A new `bytearray` with the file contents
- C) The number of bytes read (fills `buf` in-place)
- D) `None` — the result is accessible only via `buf`

C

**Q28:** What is the output?
```python
data = bytearray(3)
print(list(data))
data[0] = 255
print(data[0])
```
- A) `[0, 0, 0]`, `255`
- B) `[None, None, None]`, `255`
- C) `[b'\\x00', b'\\x00', b'\\x00']`, `b'\\xff'`
- D) `TypeError`

C

---

## Section 9: Scope & Closures (Q29–Q30)

**Q29:** What is the output?
```python
x = "global"

def outer():
    x = "outer"
    def inner():
        return x
    x = "mutated"
    return inner()

print(outer())
```
- A) `global`
- B) `outer`
- C) `mutated`
- D) `UnboundLocalError`

C

**Q30:** What is the output?
```python
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3), add10(3))
```
- A) `8 13`
- B) `8 8`
- C) `13 13`
- D) `TypeError`

A

#18:50 - end
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
