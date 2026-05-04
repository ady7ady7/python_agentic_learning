# Week 12 — Mock Exam A
**PCAP-31-03 Certification Preparation**
Date: 2026-04-03 | Time Limit: 65 minutes | 30 Questions | Passing Score: 70% (21/30)


#Start 12:20
---

## Question 1

What is the output of the following code?

```python
try:
    raise ValueError("bad value")
except Exception as e:
    print(type(e))
```

A) `<class 'Exception'>`
B) `ValueError`
C) `<class 'ValueError'>`
D) `<type 'ValueError'>`

C


---

## Question 2

What does `type(e)` return when `e` is caught by `except TypeError as e:`?

A) The string `"TypeError"`
B) The class object `TypeError`
C) The instance `e` itself
D) `<class 'Exception'>`

B

---

## Question 3

What is the output of the following code?

```python
try:
    raise ValueError("oops")
except Exception as e:
    print(type(e) == ValueError)
    print(type(e) is ValueError)
```

A) `False` then `False`
B) `True` then `False`
C) `True` then `True`
D) `False` then `True`

C

---

## Question 4

What is the output of the following code?

```python
class MyError(Exception):
    def __str__(self):
        return "custom message" #the __str__ alwasys wins over the constructor agument!

try:
    raise MyError("ignored arg")
except MyError as e:
    print(e) #__str__ here
    #if we had e.message, then we'd have ignored arg here.
```

A) `ignored arg`
B) `MyError: ignored arg`
C) `custom message`
D) `MyError: custom message`

A - this is still confusing

---

## Question 5

What is the output of the following code?

```python
class A(Exception):
    def __str__(self):
        return f"A:{self.args[0]}"

try:
    raise A("hello")
except Exception as e:
    print(str(e))
    print(repr(e))
```

A) `A:hello` then `A('hello')`
B) `hello` then `A('hello')`
C) `A:hello` then `Exception('hello')`
D) `A:hello` then `A:hello`

A - this is confusing

---

## Question 6

What is the output of the following code?

```python
class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

try:
    raise ConnectionError("lost")
except DatabaseError as e:
    print(type(e).__name__)
except ConnectionError:
    print("connection")
```

A) `DatabaseError`
B) `ConnectionError`
C) `connection`
D) `DatabaseError` then `ConnectionError`

B

---

## Question 7

What is true about the following code?

```python
def risky():
    raise ValueError("inner")

try:
    risky()
except ValueError as e:
    raise RuntimeError("outer") from e
```

A) Only `RuntimeError` is shown; `ValueError` is suppressed
B) Only `ValueError` is shown; `RuntimeError` replaces it silently
C) Both exceptions are shown; the traceback says "The above exception was the direct cause"
D) A `SyntaxError` is raised because you cannot use `from e` with a variable

A

---

## Question 8

What is the result of the following code?

```python
try:
    raise TypeError("t")
except TypeError as e:
    raise ValueError("v") from None
```

A) `TypeError: t` is shown, `ValueError` is suppressed
B) `ValueError: v` is shown; the `TypeError` context is suppressed
C) Both exceptions are shown with chaining
D) `RuntimeError` is raised automatically

B

---

## Question 9

What does the following expression evaluate to?

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.__bases__)
```

A) `(<class 'A'>, <class 'B'>)`
B) `(<class 'B'>,)`
C) `(<class 'A'>,)`
D) `(<class 'object'>, <class 'A'>, <class 'B'>, <class 'C'>)`

B

---

## Question 10

What does the following print?

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.__mro__)
```

A) `(<class 'C'>, <class 'B'>, <class 'A'>)`
B) `(<class 'C'>, <class 'B'>, <class 'A'>, <class 'object'>)`
C) `(<class 'A'>, <class 'B'>, <class 'C'>, <class 'object'>)`
D) `(<class 'C'>, <class 'object'>)`

B

---

## Question 11

What is the output of the following code?

```python
class Animal:
    def __init__(self):
        self.__secret = "dna"

class Dog(Animal):
    def reveal(self):
        return self.__secret

d = Dog()
print(d.reveal())
```

A) `dna`
B) `AttributeError: 'Dog' object has no attribute '_Dog__secret'`
C) `AttributeError: 'Dog' object has no attribute '__secret'`
D) `AttributeError: 'Animal' object has no attribute '_Animal__secret'`

B

---

## Question 12

Which attribute name is created for `self.__value` defined inside class `Outer`?

A) `__value`
B) `_value`
C) `_Outer__value`
D) `Outer__value`

C


---

## Question 13

What is the output of the following code?

```python
class Parent:
    def __init__(self):
        self.__x = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__x = 99

    def show(self):
        print(self._Parent__x)
        print(self._Child__x)

Child().show()
```

A) `99` then `99`
B) `10` then `10`
C) `10` then `99`
D) `AttributeError`

C

---

## Question 14

What is the output of the following code?

```python
f = lambda x, y=2: x ** y
print(f(3))
print(f(3, 3))
```

A) `9` then `27`
B) `6` then `9`
C) `9` then `9`
D) `TypeError`

A

---

## Question 15

What is the output of the following code?

```python
fns = [lambda x, i=i: x + i for i in range(3)]
print(fns[0](10))
print(fns[2](10))
```

A) `12` then `12`
B) `10` then `12`
C) `10` then `10`
D) `TypeError`

B

---

## Question 16

What is the output of the following code?

```python
fns = [lambda x: x + i for i in range(3)]
print(fns[0](10))
print(fns[2](10))
```

A) `10` then `12`
B) `12` then `12`
C) `13` then `13`
D) `11` then `13`

B

---

## Question 17

What is the output of the following code?

```python
result = [x * 2 for x in range(5, 0, -1)]
print(result)
```

A) `[2, 4, 6, 8, 10]`
B) `[10, 8, 6, 4, 2]`
C) `[1, 2, 3, 4, 5]`
D) `[10, 8, 6, 4, 2, 0]`

B

---

## Question 18

What is the output of the following code?

```python
result = [x for x in range(10, 0, -3)]
print(result)
```

A) `[10, 7, 4, 1]`
B) `[10, 7, 4]`
C) `[9, 6, 3]`
D) `[10, 7, 4, 1, -2]`

A

---

## Question 19

Which `open()` mode opens a file for both reading and writing without truncating, with the pointer at the beginning?

A) `"w+"`
B) `"a+"`
C) `"r+"`
D) `"x+"`

B

---

## Question 20

What happens when you open a file with mode `"x"` and the file already exists?

A) The file is truncated and overwritten
B) The file is opened for appending
C) A `FileExistsError` is raised
D) A `PermissionError` is raised

C

---

## Question 21

What is the output of the following code?

```python
print(2.)
print(type(2.))
```

A) `2` then `<class 'int'>`
B) `2.0` then `<class 'float'>`
C) `2.` then `<class 'float'>`
D) `SyntaxError`

B

---

## Question 22

Given `sys.argv = ["prog.py", "alpha", "beta"]`, what is the output?

```python
print(len(sys.argv))
print(sys.argv[0])
```

A) `2` then `alpha`
B) `3` then `prog.py`
C) `2` then `prog.py`
D) `3` then `alpha`

B

---

## Question 23

Which statement about `sys.modules` is correct?

A) It is a list of all installed packages
B) It is a dictionary mapping module names to module objects for already-imported modules
C) It is a set of module names available to import
D) It contains only standard library modules

B

---

## Question 24

What is the output of the following code?

```python
import os.path
print(os.path.basename("/home/user/data/prices.csv"))
print(os.path.dirname("/home/user/data/prices.csv"))
```

A) `prices.csv` then `/home/user/data`
B) `data/prices.csv` then `/home/user`
C) `prices` then `/home/user/data`
D) `prices.csv` then `/home/user/data/`

A

---

## Question 25

Which set of results is correct?

```python
print("aa" > "aaa")
print("aa" < "aaa")
print("B" > "a")
```

A) `True`, `False`, `True`
B) `False`, `True`, `False`
C) `False`, `True`, `True`
D) `True`, `False`, `False`

B

---

## Question 26

What is the output of the following code?

```python
def process():
    try:
        return "try"
    finally:
        return "finally"

print(process())
```

A) `try`
B) `finally`
C) `try` then `finally`
D) `RuntimeError: conflicting return`

B

---

## Question 27

What is the output of the following code?

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    inner()
    inner()
    return inner()

print(outer())
```

A) `1`
B) `2`
C) `3`
D) `0`

B

---

## Question 28

What is the output of the following code?

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
print(next(g))
```

A) `1`, `2`, `1`, `3`
B) `1`, `2`, `1`, `1`
C) `1`, `1`, `1`, `1`
D) `1`, `2`, `3`, `1`

A

---

## Question 29

What is the output of the following code?

```python
b = bytearray(b"hello")
b[0] = 72
print(b)
print(type(b))
```

A) `bytearray(b'Hello')` then `<class 'bytearray'>`
B) `b'Hello'` then `<class 'bytes'>`
C) `bytearray(b'hello')` then `<class 'bytearray'>`
D) `TypeError: 'bytes' object does not support item assignment`


A

---

## Question 30

What is the output of the following code?

```python
s = "python is great"
print(s.find("is"))
print(s.find("xx"))
print(s.index("xx"))
```

A) `7` then `-1` then `-1`
B) `7` then `-1` then `ValueError`
C) `7` then `0` then `ValueError`
D) `-1` then `-1` then `ValueError`

B

---

## Answer Key

1. C
2. B
3. C
4. C
5. A
6. B
7. C
8. B
9. B
10. B
11. B
12. C
13. C
14. A
15. B
16. B
17. B
18. A
19. C
20. C
21. B
22. B
23. B
24. A
25. B
26. B
27. C
28. A
29. A
30. B

## Scoring Guide

| Score | Result |
|-------|--------|
| 27–30 (90–100%) | Excellent — exam ready |
| 24–26 (80–89%) | Strong — review weak areas |
| 21–23 (70–79%) | Pass threshold — targeted revision needed |
| Below 21 (< 70%) | Fail — significant revision required |
