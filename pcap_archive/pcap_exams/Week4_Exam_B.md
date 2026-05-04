# PCAP Mock Exam B - Week 4
## 30 Questions | 45 Minutes | Passing Score: 70% (21/30)

**Date:** 2026-01-30 (Weekend)

**Topics Covered:** Weeks 1-4 (Modules, OOP, Properties, Functional Programming)

**Instructions:**
- Choose the BEST answer for each question
- No code execution allowed during the exam
- Write your answers at the bottom



#Start 9:57

---

### Question 1
What is the output?
```python
f = lambda x, y=2, z=3: x * y + z
print(f(2))
```
- A) 7
- B) 8
- C) 10
- D) Error

A

---

### Question 2
What is the output?
```python
class Parent:
    def __init__(self):
        self.value = "parent"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "child"

c = Child()
print(c.value)
```
- A) parent
- B) child
- C) Error
- D) None

B

---

### Question 3
What is the output?
```python
from functools import reduce
result = reduce(lambda acc, x: acc if acc > x else x, [3, 1, 4, 1, 5, 9, 2, 6])
print(result)
```
- A) 3
- B) 6
- C) 9
- D) Error

C

---

### Question 4
What is the output?
```python
def gen_nums():
    for i in range(3):
        yield i * 2

g = gen_nums()
print(list(g))
print(list(g))
```
- A) [0, 2, 4] [0, 2, 4]
- B) [0, 2, 4] []
- C) [] []
- D) Error

B

---

### Question 5
What is the output?
```python
result = list(filter(None, [0, 1, "", "a", [], [1], False, True]))
print(result)
```
- A) [None]
- B) [1, "a", [1], True]
- C) [0, 1, "", "a", [], [1], False, True]
- D) Error

B

---

### Question 6
What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    pass

class D(B, C):
    pass

print(D().method())
```
- A) A
- B) B
- C) Error
- D) None

B


---

### Question 7
What is the output?
```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```
- A) Hello
- B) Before Hello After
- C) Before After Hello
- D) Error

B

---

### Question 8
What is the output?
```python
nums = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, nums)
print(next(result), next(result))
```
- A) 2 4
- B) 1 2
- C) [2, 4, 6, 8, 10]
- D) Error

A

---

### Question 9
Which is TRUE about abstract base classes (ABC)?
- A) You can instantiate an abstract class directly
- B) Abstract methods must be implemented by subclasses
- C) `@abstractmethod` decorator makes a method optional
- D) ABCs don't support inheritance

B

---

### Question 10
What is the output?
```python
def make_adders():
    adders = []
    for i in range(3):
        adders.append(lambda x, i=i: x + i)
    return adders

a = make_adders()
print(a[0](10), a[1](10), a[2](10))
```
- A) 12 12 12
- B) 10 11 12
- C) 10 10 10
- D) Error

B

---

### Question 11
What is the output?
```python
class Price:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._amount = value

p = Price(100)
p.amount = 50
print(p.amount)
```
- A) 100
- B) 50
- C) Error
- D) None

B

---

### Question 12
What is the output?
```python
def outer():
    count = [0]
    def inner():
        count[0] += 1
        return count[0]
    return inner

f = outer()
print(f(), f(), f())
```
- A) 1 1 1
- B) 1 2 3
- C) 0 1 2
- D) Error

D

---

### Question 13
What does this import do: `from package import *`?
- A) Imports all modules from the package
- B) Imports names listed in `__all__` if defined, otherwise all public names
- C) Always imports everything including private names
- D) Raises an error

B

---

### Question 14
What is the output?
```python
try:
    raise ValueError("test")
except Exception as e:
    print(type(e).__name__, end=" ")
finally:
    print("done")
```
- A) ValueError done
- B) Exception done
- C) test done
- D) Error

A

---

### Question 15
What is the output?
```python
def deco1(f):
    def wrapper():
        return f() + "1"
    return wrapper

def deco2(f):
    def wrapper():
        return f() + "2"
    return wrapper

@deco1
@deco2
def get():
    return "X"

print(get())
```
- A) X12
- B) X21
- C) 12X
- D) 21X

D

---

### Question 16
What is the output?
```python
class Counter:
    instances = 0

    def __init__(self):
        Counter.instances += 1
        self.id = Counter.instances

a = Counter()
b = Counter()
Counter.instances = 100
c = Counter()
print(a.id, b.id, c.id)
```
- A) 1 2 3
- B) 1 2 101
- C) 100 100 101
- D) 1 2 100

B

---

### Question 17
What is the output?
```python
result = [x for x in range(10) if x % 2 == 0]
print(result)
```
- A) [0, 2, 4, 6, 8]
- B) [1, 3, 5, 7, 9]
- C) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- D) Error

A

---

### Question 18
What is the output?
```python
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

print(f(6))
```
- A) 6
- B) 8
- C) 13
- D) 21

#f(6) = f(5) + f(4) = f(4) + F(3) + f(3) + f(2) = f(3) + f(2) + (f2) + 1 + 1 = f(2) + 1 + 1 + 1 + 1 + 1 = 1 + 1 + 1 + 1 + 1 + 1
That's my interpretation, BUT IT could bew rong - if that's the case, plaese spend some time to explain me how these functions work, as there was a simi9lar one on PCEP and perhaps there will also be on PCAP and I need to be prepared for these regressive pseudo-infinite functions

A

---

### Question 19
What is the output?
```python
s = "hello"
print(s[1:4], s[::2], s[::-1])
```
- A) ell hlo olleh
- B) ell hlo olleh
- C) hel hlo olleh
- D) ello hlo olleh

A & B are exactly the same... - both correct - this is an error on your side!

---

### Question 20
What is the output?
```python
from functools import reduce
result = reduce(lambda a, b: a + [b*2], [1, 2, 3], [])
print(result)
```
- A) [1, 2, 3]
- B) [2, 4, 6]
- C) 12
- D) Error

B

---

### Question 21
What is the output?
```python
class A:
    x = 10

class B(A):
    pass

B.x = 20
print(A.x, B.x)
```
- A) 10 20
- B) 20 20
- C) 10 10
- D) Error

A

---

### Question 22
What is the output?
```python
def wrapper(func):
    def inner(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return inner

@wrapper
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```
- A) Hello, Alice
- B) Calling greet\nHello, Alice
- C) Calling inner\nHello, Alice
- D) Error

C

---

### Question 23
What is the output?
```python
nums = [1, 2, 3]
result = list(map(lambda x: x ** 2, filter(lambda x: x > 1, nums)))
print(result)
```
- A) [1, 4, 9]
- B) [4, 9]
- C) [2, 3]
- D) Error

B

---

### Question 24
What is the output?
```python
class MyClass:
    def __len__(self):
        return 42

obj = MyClass()
print(len(obj))
```
- A) 0
- B) 42
- C) Error
- D) None

B

---

### Question 25
What is the output?
```python
x = 10
def outer():
    global x
    x = 20
    def inner():
        global x
        x = 30
    inner()
    return x

print(outer(), x)
```
- A) 20 10
- B) 30 30
- C) 20 30
- D) 30 20

B

---

### Question 26
What is the output?
```python
def gen():
    yield 1
    return 2
    yield 3

g = gen()
print(list(g))
```
- A) [1]
- B) [1, 2]
- C) [1, 2, 3]
- D) Error

A

---

### Question 27
What is the output?
```python
items = [(1, 'b'), (2, 'a'), (3, 'c')]
result = sorted(items, key=lambda x: x[1])
print(result)
```
- A) [(1, 'b'), (2, 'a'), (3, 'c')]
- B) [(2, 'a'), (1, 'b'), (3, 'c')]
- C) [(3, 'c'), (1, 'b'), (2, 'a')]
- D) Error

B

---

### Question 28
What is the output?
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        self.age = age

c = Child("Alice", 10)
print(hasattr(c, 'name'))
```
- A) True
- B) False
- C) Error
- D) None

B

---

### Question 29
What is the output?
```python
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter(10)
print(c1(), c2(), c1())
```
- A) 1 11 2
- B) 1 10 2
- C) 0 10 1
- D) Error

A

---

### Question 30
What is the output?
```python
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(5)
print(s.area())
```
- A) 25
- B) Error (NotImplementedError)
- C) Error (TypeError)
- D) None

A


#Koniec 10:17

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
