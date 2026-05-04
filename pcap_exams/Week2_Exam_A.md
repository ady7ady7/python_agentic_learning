# PCAP Mock Exam - Week 2, Exam A

**Time Limit:** 65 minutes (simulates real exam pace)
**Questions:** 30
**Passing Score:** 70% (21/30)

**Instructions:**
- No external resources (notes, internet, IDE)
- Write your answer letter next to each question
- For code output questions, write the exact output

---

#START 18:48


## Section 1: Inheritance & OOP (Questions 1-10)

**Question 1:** What is the output of this code?

```python
class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "woof"

d = Dog()
print(d.speak())
```

A) sound
B) woof
C) soundwoof
D) Error

**Your answer:**
B

---

**Question 2:** What does `super()` do in Python?

A) Creates a new superclass
B) Returns a proxy object to access parent class methods
C) Makes the current class a superclass
D) Deletes the parent class

**Your answer:**
b


---

**Question 3:** What is the output?

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

A) 10
B) 20
C) 30
D) Error: value not defined

**Your answer:**
B

---

**Question 4:** Which statement about abstract classes is TRUE?

A) Abstract classes can be instantiated directly
B) Abstract methods must be implemented by child classes
C) Python doesn't support abstract classes
D) Abstract classes cannot have regular methods

**Your answer:**
B

---

**Question 5:** What is the output?

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

A) 1
B) 2
C) Error
D) None

**Your answer:**
B

---

**Question 6:** What is the MRO of class D in the previous question?

A) D → B → C → A → object
B) D → C → B → A → object
C) D → A → B → C → object
D) D → B → A → C → object

**Your answer:**
A

---

**Question 7:** What happens if you don't call `super().__init__()` in a child class?

A) Python raises an error
B) Parent's `__init__` is called automatically
C) Parent's instance attributes are not initialized
D) The child class cannot be created

**Your answer:**

B
---

**Question 8:** What is the output?

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count

c1 = Counter()
c2 = Counter()
print(c1.count, c2.count, Counter.count)
```

A) 1 2 2
B) 2 2 2
C) 1 1 2
D) 0 0 2

**Your answer:**
B

---

**Question 9:** Which is TRUE about `isinstance()` and `issubclass()`?

A) `isinstance()` checks class hierarchy, `issubclass()` checks object type
B) `isinstance()` checks object type, `issubclass()` checks class hierarchy
C) Both check the same thing
D) Neither works with inheritance

**Your answer:**
B

---

**Question 10:** What is the output?

```python
class Base:
    def method(self):
        return "Base"

class Child(Base):
    def method(self):
        return super().method() + " Child"

c = Child()
print(c.method())
```

A) Base
B) Child
C) Base Child
D) Child Base

**Your answer:**
C

---

## Section 2: Class & Static Methods (Questions 11-15)

**Question 11:** What is the first parameter of a `@classmethod`?

A) self (the instance)
B) cls (the class)
C) None (no automatic parameter)
D) super (the parent)

**Your answer:**
B

---

**Question 12:** What is the first parameter of a `@staticmethod`?

A) self (the instance)
B) cls (the class)
C) None (no automatic parameter)
D) super (the parent)

**Your answer:**
C

---

**Question 13:** What is the output?

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(Math.add(2, 3))
print(Math().multiply(2, 3))
```

A) 5, 6
B) Error, 6
C) 5, Error
D) Error, Error

**Your answer:**
a

---

**Question 14:** Can a `@staticmethod` access class attributes?

A) Yes, via `cls`
B) Yes, via `self`
C) No, unless you hardcode the class name
D) No, never

**Your answer:**
d

---

**Question 15:** When should you use `@classmethod`?

A) When you don't need any class or instance data
B) When you need to create alternative constructors
C) When the method is completely independent
D) When you need to modify instance attributes

**Your answer:**
C

---

## Section 3: Exception Handling (Questions 16-20)

**Question 16:** What is the output?

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("A")
except Exception:
    print("B")
finally:
    print("C")
```

A) A
B) A C
C) B C
D) A B C

**Your answer:**

b

---

**Question 17:** When does the `else` block in try/except execute?

A) Always
B) When an exception occurs
C) When no exception occurs
D) Only with finally

**Your answer:**
c

---

**Question 18:** What is the output?

```python
def func():
    try:
        return 1
    finally:
        return 2

print(func())
```

A) 1
B) 2
C) 1 2
D) Error

**Your answer:**
B

---

**Question 19:** Which exception order is correct?

A) Exception → ValueError → ZeroDivisionError
B) ZeroDivisionError → ValueError → Exception
C) ValueError → Exception → ZeroDivisionError
D) Any order works

**Your answer:**
This is an ambiguous question.
For factual state of things - D.
For optimal flow we should with specific -> generic order (B). Don't you dare to take away points from me for that!

---

**Question 20:** What is the output?

```python
try:
    raise ValueError("test")
except ValueError as e:
    print(type(e).__name__)
```

A) ValueError
B) test
C) Exception
D) Error

**Your answer:**
A

---

## Section 4: List Comprehensions & Iterables (Questions 21-25)

**Question 21:** What is the output?

```python
result = [x * 2 for x in range(5) if x % 2 == 0]
print(result)
```

A) [0, 2, 4, 6, 8]
B) [0, 4, 8]
C) [2, 4, 6, 8, 10]
D) [0, 2, 4]

**Your answer:**
B

---

**Question 22:** What is the output?

```python
result = [x if x > 3 else 0 for x in [1, 2, 3, 4, 5]]
print(result)
```

A) [4, 5]
B) [0, 0, 0, 4, 5]
C) [1, 2, 3, 4, 5]
D) [0, 0, 3, 4, 5]

**Your answer:**
B

---

**Question 23:** What's wrong with this code?

```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst
```

A) Nothing, it works correctly
B) Mutable default argument bug
C) Syntax error
D) lst should be a tuple

**Your answer:**
B

---

**Question 24:** What is the output?

```python
data = [1, 2, 3]
result = [x for x in data if x > 1 if x < 3]
print(result)
```

A) [1, 2, 3]
B) [2]
C) [2, 3]
D) Error - can't have two ifs

**Your answer:**
B

---

**Question 25:** What is the output?

```python
nums = [1, 2, 3]
result = [[x, x**2] for x in nums]
print(result)
```

A) [1, 1, 2, 4, 3, 9]
B) [[1, 1], [2, 4], [3, 9]]
C) [(1, 1), (2, 4), (3, 9)]
D) Error

**Your answer:**
B

---

## Section 5: Mixed Topics (Questions 26-30)

**Question 26:** What is the output?

```python
class A:
    def __init__(self):
        print("A", end=" ")

class B(A):
    def __init__(self):
        print("B", end=" ")
        super().__init__()

class C(A):
    def __init__(self):
        print("C", end=" ")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D", end=" ")
        super().__init__()

d = D()
```

A) D B A
B) D B C A
C) D B A C A
D) D A B A C A

**Your answer:**
C

---

**Question 27:** What does `__all__` in `__init__.py` control?

A) All classes that can be inherited
B) All methods that are public
C) What is exported with `from package import *`
D) All files in the package

**Your answer:**
C

---

**Question 28:** What is the output?

```python
class Test:
    def __init__(self):
        self._value = 10

    @property
    def value(self):
        return self._value * 2

t = Test()
print(t.value)
```

A) 10
B) 20
C) Error - can't access _value
D) Error - value is not callable

**Your answer:**
WE DIDN'T HAVE SUCH THING AS @property FOR A SINGLE TIME - THIS IS YOUR FAULT, and if thsi is expected, I need to know exactly what it does :)).

B

---

**Question 29:** Which statement about composition is TRUE?

A) Composition means one class inherits from another
B) Composition means one class contains an instance of another
C) Composition requires the `super()` function
D) Composition is the same as multiple inheritance

**Your answer:**

A

---

**Question 30:** What is the output?

```python
class Parent:
    value = "parent"

class Child(Parent):
    pass

c = Child()
c.value = "child"
print(Child.value, c.value)
```

A) parent child
B) child child
C) parent parent
D) child parent

**Your answer:**
B


#18:58 Finish
---

## Answer Key (Check after completing!)

Write your answers in order:

```
1:    2:    3:    4:    5:
6:    7:    8:    9:    10:
11:   12:   13:   14:   15:
16:   17:   18:   19:   20:
21:   22:   23:   24:   25:
26:   27:   28:   29:   30:
```

**Total Score:** ___/30

---

*Complete this exam without any resources, then check your answers with the mentor.*
