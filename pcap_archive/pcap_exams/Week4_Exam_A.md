# PCAP Mock Exam A - Week 4
## 30 Questions | 45 Minutes | Passing Score: 70% (21/30)

**Date:** 2026-01-30 (Weekend)

**Topics Covered:** Weeks 1-4 (Modules, OOP, Properties, Functional Programming)

**Instructions:**
- Choose the BEST answer for each question
- No code execution allowed during the exam
- Write your answers at the bottom

#9:42

---

### Question 1
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
- A) 10 10
- B) 15 15
- C) 15 20
- D) Error

C

---

### Question 2
What is the output?
```python
from functools import reduce
result = reduce(lambda a, b: a * b, [1, 2, 3, 4], 2)
print(result)
```
- A) 24
- B) 48
- C) 10
- D) Error

B

---

### Question 3
Which statement about `__init__` is TRUE?
- A) It must always return `self`
- B) It is automatically inherited and called by child classes
- C) It must return `None` (implicitly or explicitly)
- D) It is a class method

C

---

### Question 4
What is the output?
```python
class A:
    x = 1

class B(A):
    pass

class C(A):
    x = 2

class D(B, C):
    pass

print(D.x)
```
- A) 1
- B) 2
- C) Error
- D) None

B

---

### Question 5
What is the output?
```python
funcs = [lambda x: x + i for i in range(3)]
print(funcs[0](10))
```
- A) 10
- B) 11
- C) 12
- D) Error

C

---

### Question 6
What is the output?
```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
```
- A) [1, 3, 5]
- B) [2, 4]
- C) [True, False, True, False, True]
- D) Error

B


---

### Question 7
What does `@property` decorator do?
- A) Makes a method static
- B) Allows a method to be called without parentheses
- C) Makes an attribute read-only
- D) Both B and C are correct

D

---

### Question 8
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
- A) 1 3
- B) 3 3
- C) 1 1
- D) Error

B

---

### Question 9
What is the output?
```python
def deco(f):
    def wrapper(*args):
        return f(*args) + 1
    return wrapper

@deco
def add(a, b):
    return a + b

print(add(2, 3))
```
- A) 5
- B) 6
- C) Error
- D) None

B

---

### Question 10
What is the output?
```python
x = [1, 2, 3]
y = map(lambda n: n * 2, x)
print(type(y).__name__)
```
- A) list
- B) map
- C) generator
- D) iterator

B

---

### Question 11
Which import statement is INVALID?
- A) `from math import sqrt`
- B) `import math as m`
- C) `from math import *`
- D) `import sqrt from math`

D

---

### Question 12
What is the output?
```python
class A:
    def show(self):
        print("A", end=" ")

class B(A):
    def show(self):
        super().show()
        print("B", end=" ")

class C(A):
    def show(self):
        super().show()
        print("C", end=" ")

class D(B, C):
    def show(self):
        super().show()
        print("D", end=" ")

D().show()
```
- A) A B C D
- B) A C B D
- C) A B D
- D) Error

C

---

### Question 13
What is the output?
```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5) + triple(5))
```
- A) 10
- B) 15
- C) 25
- D) Error


C

---

### Question 14
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
- A) Z F
- B) A F
- C) A Z F
- D) F

A

---

### Question 15
What is the output?
```python
class Price:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

p = Price(100)
p.value = 200
print(p.value)
```
- A) 100
- B) 200
- C) Error (AttributeError)
- D) None


C

---

### Question 16
What is the output?
```python
from functools import reduce
words = ["Hello", "World"]
result = reduce(lambda a, b: a + " " + b, words)
print(result)
```
- A) HelloWorld
- B) Hello World
- C) ["Hello", "World"]
- D) Error


B

---

### Question 17
What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g) + next(g))
```
- A) 1
- B) 2
- C) 3
- D) Error

C

---

### Question 18
What is the name mangled version of `__secret` in class `MyClass`?
- A) `__secret`
- B) `_MyClass__secret`
- C) `__MyClass_secret`
- D) `_secret`

B

---

### Question 19
What is the output?
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
add_10 = outer(10)
print(add_5(3), add_10(3))
```
- A) 8 13
- B) 5 10
- C) 3 3
- D) Error

A

---

### Question 20
What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        self.y = 2

b = B()
print(hasattr(b, 'x'), hasattr(b, 'y'))
```
- A) True True
- B) False True
- C) True False
- D) Error

B

---

### Question 21
What is the output?
```python
result = list(map(str.upper, ["a", "b", "c"]))
print(result)
```
- A) ["a", "b", "c"]
- B) ["A", "B", "C"]
- C) "ABC"
- D) Error

B

---

### Question 22
What is the output?
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                result = func(*args)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg, end=" ")
    return msg

say("Hi")
```
- A) Hi
- B) Hi Hi Hi
- C) Hi Hi Hi (returns "Hi")
- D) Error

B

---

### Question 23
What is the output?
```python
nums = [1, 2, 3, 4, 5]
squared = (x**2 for x in nums)
print(sum(squared), sum(squared))
```
- A) 55 55
- B) 55 0
- C) 0 0
- D) Error

B

---

### Question 24
Which is TRUE about `isinstance()` and `issubclass()`?
- A) `isinstance()` checks if an object is an instance of a class
- B) `issubclass()` checks if a class is a subclass of another
- C) Both A and B are correct
- D) Neither A nor B is correct

C

---

### Question 25
What is the output?
```python
def f(a, b=[], c=None):
    if c is None:
        c = []
    b.append(a)
    c.append(a)
    return b, c

print(f(1))
print(f(2))
```
- A) ([1], [1]) ([2], [2])
- B) ([1], [1]) ([1, 2], [2])
- C) ([1], [1]) ([1, 2], [1, 2])
- D) Error


B

---

### Question 26
What is the output?
```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Animal), issubclass(Dog, Animal))
```
- A) True True
- B) True False
- C) False True
- D) False False

A
---


### Question 27
What is the output?
```python
add = lambda a, b: a + b
print(add.__name__)
```
- A) add
- B) lambda
- C) <lambda>
- D) Error


C

---

### Question 28
What is the output?
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
```
- A) Vector(1, 2)
- B) Vector(3, 4)
- C) Vector(4, 6)
- D) Error

C

---

### Question 29
What is the output?
```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c1 = counter()
c2 = counter()
print(c1(), c1(), c2())
```
- A) 1 2 1
- B) 1 2 3
- C) 1 1 1
- D) Error

A

---

### Question 30
What is the output?
```python
import sys
print("math" in sys.modules)
import math
print("math" in sys.modules)
```
- A) True True
- B) False True
- C) True False
- D) False False

B


#Koniec 9:57
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

**When complete:** Submit to mentor for grading. Target: 21/30 (70%)
