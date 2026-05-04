# PCAP Mock Exam - Week 3, Exam A

**Time Limit:** 65 minutes (suggested)
**Passing Score:** 70% (21/30)
**Topics:** Modules, Strings, Exceptions, OOP, Properties, Dunder Methods, Generators

---

## Instructions

- Select the ONE best answer for each question
- Write your answers in the Answer Sheet at the bottom
- No IDE/interpreter - this simulates exam conditions
- After completing, check answers in `exam_feedback.md`

#Start 9:51
---

## Questions

### Q1
What is the output?
```python
class A:
    x = 1

class B(A):
    pass

B.x = 2
print(A.x, B.x)
```
- A) `1 1`
- B) `2 2`
- C) `1 2`
- D) `2 1`

A
---

### Q2
What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g) + next(g))
```
- A) `1`
- B) `3`
- C) `6`
- D) `StopIteration`

B

---

### Q3
Which statement about `__init__` is TRUE?
- A) It must always return `self`
- B) It is automatically called when creating an object
- C) It can only have `self` as a parameter
- D) It is inherited and cannot be overridden


B

---

### Q4
What is the output?
```python
text = "Python"
print(text[1:4:2])
```
- A) `yh`
- B) `yth`
- C) `yt`
- D) `IndexError`

A

---

### Q5
What happens when you call `next()` on an exhausted generator?
- A) Returns `None`
- B) Returns an empty list
- C) Raises `StopIteration`
- D) Raises `GeneratorExit`

C

---

### Q6
What is the output?
```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(a.count, Counter.count)
```
- A) `1 3`
- B) `3 3`
- C) `1 1`
- D) `3 1`

B

---

### Q7
Which creates a generator expression?
- A) `[x**2 for x in range(5)]`
- B) `(x**2 for x in range(5))`
- C) `{x**2 for x in range(5)}`
- D) `list(x**2 for x in range(5))`


B

---

### Q8
What is the output?
```python
class Parent:
    def __init__(self):
        self.value = 10

class Child(Parent):
    def __init__(self):
        self.value = 20

c = Child()
print(c.value)
```
- A) `10`
- B) `20`
- C) `30`
- D) `AttributeError`

B

---

### Q9
What does `sys.path` contain?
- A) The current working directory only
- B) A list of directories Python searches for modules
- C) The path to the Python executable
- D) Environment variables

B

---

### Q10
What is the output?
```python
try:
    x = 1 / 0
except ArithmeticError:
    print("A", end=" ")
except ZeroDivisionError:
    print("Z", end=" ")
finally:
    print("F")
```
- A) `A F`
- B) `Z F`
- C) `A Z F`
- D) `F`

B

---

### Q11
What is the output?
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value * 2

obj = MyClass(5)
print(obj.value)
```
- A) `5`
- B) `10`
- C) `25`
- D) `AttributeError`

B

---

### Q12
What is the correct way to import only the `sqrt` function from the `math` module?
- A) `import sqrt from math`
- B) `from math import sqrt`
- C) `import math.sqrt`
- D) `from math import * sqrt`


B

---

### Q13
What is the output?
```python
def gen():
    for i in range(3):
        yield i

g = gen()
list(g)
print(list(g))
```
- A) `[0, 1, 2]`
- B) `[]`
- C) `[0, 1, 2, 0, 1, 2]`
- D) `StopIteration`


B

---

### Q14
What is the output?
```python
class A:
    def __str__(self):
        return "A"

    def __repr__(self):
        return "repr_A"

a = A()
print(a)
```
- A) `A`
- B) `repr_A`
- C) `<__main__.A object>`
- D) `A repr_A`

A

---

### Q15
What does name mangling do to `self.__value`?
- A) Makes it truly private and inaccessible
- B) Encrypts the value
- C) Renames it to `_ClassName__value`
- D) Raises an error


C

---

### Q16
What is the output?
```python
s = "hello"
print(s.find("z"), s.index("l"))
```
- A) `-1 2`
- B) `None 2`
- C) `-1 3`
- D) `ValueError`


A

---

### Q17
What is the output?
```python
class A:
    def __len__(self):
        return 5

a = A()
print(len(a))
```
- A) `0`
- B) `5`
- C) `TypeError`
- D) `None`

B

---

### Q18
Which exception is the parent of `ValueError` and `TypeError`?
- A) `BaseException`
- B) `Exception`
- C) `StandardError`
- D) `RuntimeError`

B (but Base Exceptioni s the father of all Exceptions here, so that could be a bit ambigous)

---

### Q19
What is the output?
```python
gen = (x for x in [1, 2, 3])
print(type(gen).__name__)
```
- A) `list`
- B) `tuple`
- C) `generator`
- D) `genexpr`

C

---

### Q20
What is the output?
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

c = Car("Toyota", 4)
print(c.brand)
```
- A) `Toyota`
- B) `None`
- C) `AttributeError`
- D) `TypeError`

A

---

### Q21
What does `__all__` do in a module?
- A) Lists all functions in the module
- B) Controls what is exported with `from module import *`
- C) Makes all names public
- D) Prevents any imports

B

---

### Q22
What is the output?
```python
text = "  hello  "
print(len(text.strip()))
```
- A) `5`
- B) `7`
- C) `9`
- D) `8`

A


---

### Q23
What is the output?
```python
class A:
    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

a = A()
a.items = [1, 2, 3]
print(list(a))
```
- A) `[]`
- B) `[1, 2, 3]`
- C) `TypeError`
- D) `<__main__.A object>`

B

---

### Q24
What is the output?
```python
def func():
    yield 1
    return
    yield 2

print(list(func()))
```
- A) `[1, 2]`
- B) `[1]`
- C) `[1, None]`
- D) `StopIteration`

B

---

### Q25
Which is TRUE about `@property`?
- A) It can only create read-only attributes
- B) It replaces the need for getter methods
- C) It must be followed by `@setter`
- D) It makes attributes truly private


B

---

### Q26
What is the output?
```python
class A:
    pass

class B(A):
    pass

print(issubclass(B, A), isinstance(B(), A))
```
- A) `True True`
- B) `True False`
- C) `False True`
- D) `False False`

B

---

### Q27
What is the output?
```python
s = "python"
print(s[-2::-2])
```
- A) `otp`
- B) `nhy`
- C) `ohn`
- D) `ot`

A

---

### Q28
What happens when a class defines `__eq__` but not `__hash__`?
- A) Objects can be used in sets
- B) Objects become unhashable
- C) Python auto-generates `__hash__`
- D) A `SyntaxError` is raised


B

---

### Q29
What is the output?
```python
try:
    raise ValueError("error")
except Exception as e:
    print(type(e).__name__)
```
- A) `Exception`
- B) `ValueError`
- C) `error`
- D) `BaseException`

C


---

### Q30
What is the output?
```python
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return A(self.x + other.x)

a = A(5)
b = A(3)
c = a + b
print(c.x)
```
- A) `5`
- B) `3`
- C) `8`
- D) `TypeError`

C


#Koniec 10:03
---

## Answer Sheet

Write your answers below:

```
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
```

---

**When complete:** Submit your answers and I will provide detailed feedback with explanations.
