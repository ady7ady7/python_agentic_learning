# PCAP Mock Exam - Week 3, Exam B

**Time Limit:** 65 minutes (suggested)
**Passing Score:** 70% (21/30)
**Topics:** Modules, Strings, Exceptions, OOP, Properties, Dunder Methods, Generators

---

## Instructions

- Select the ONE best answer for each question
- Write your answers in the Answer Sheet at the bottom
- No IDE/interpreter - this simulates exam conditions
- After completing, check answers in `exam_feedback.md`

---


#Początek 10:03

## Questions

### Q1
What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x = self.x + 1

b = B()
print(b.x)
```
- A) `1`
- B) `2`
- C) `AttributeError`
- D) `None`

B

---

### Q2
What is the output?
```python
text = "PYTHON"
print(text[::2] + text[1::2])
```
- A) `PYTHONYTO`
- B) `PTOYHN`
- C) `PYTONHTN`
- D) `PTOYHNYTO`


B

---

### Q3
What is the output?
```python
def count():
    n = 0
    while True:
        yield n
        n += 1

c = count()
print(next(c), next(c), next(c))
```
- A) `0 0 0`
- B) `0 1 2`
- C) `1 2 3`
- D) `StopIteration`

B

---

### Q4
Which is TRUE about abstract methods?
- A) They must have an implementation in the abstract class
- B) They must be overridden in concrete subclasses
- C) They are automatically inherited without overriding
- D) They can only exist in regular classes

B


---

### Q5
What is the output?
```python
class A:
    def __init__(self):
        self.__x = 10

a = A()
print(a._A__x)
```
- A) `10`
- B) `AttributeError`
- C) `None`
- D) `NameError`

A

---

### Q6
What is the output?
```python
try:
    x = int("abc")
except ValueError:
    print("V", end=" ")
except TypeError:
    print("T", end=" ")
else:
    print("E", end=" ")
finally:
    print("F")
```
- A) `V F`
- B) `T F`
- C) `V E F`
- D) `E F`

A

---

### Q7
What is the output?
```python
s = "hello world"
print(s.split()[1].upper())
```
- A) `HELLO`
- B) `WORLD`
- C) `['hello', 'world']`
- D) `hello world`

B

---

### Q8
What is the output?
```python
class MyList:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, index):
        return self.data[index]

m = MyList()
print(m[1])
```
- A) `[1, 2, 3]`
- B) `1`
- C) `2`
- D) `TypeError`

C

---

### Q9
What does `from package import *` import?
- A) All modules in the package
- B) Only names listed in `__all__` (if defined)
- C) Nothing
- D) Only the `__init__.py` file


B

---

### Q10
What is the output?
```python
gen = (x**2 for x in range(4))
print(sum(gen))
```
- A) `6`
- B) `9`
- C) `14`
- D) `TypeError`

C


---

### Q11
What is the output?
```python
class A:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val * 2

a = A()
a.value = 5
print(a.value)
```
- A) `5`
- B) `10`
- C) `25`
- D) `AttributeError`

B

---

### Q12
What is the output?
```python
class Parent:
    class_attr = "parent"

class Child(Parent):
    pass

Child.class_attr = "child"
print(Parent.class_attr)
```
- A) `parent`
- B) `child`
- C) `None`
- D) `AttributeError`

A

---

### Q13
What is the output?
```python
def gen():
    yield 1
    yield 2
    return "done"

g = gen()
print(list(g))
```
- A) `[1, 2, 'done']`
- B) `[1, 2]`
- C) `[1, 2, None]`
- D) `StopIteration`

B


---

### Q14
What is the output?
```python
class A:
    def __contains__(self, item):
        return item > 0

a = A()
print(5 in a, -3 in a)
```
- A) `True True`
- B) `True False`
- C) `False True`
- D) `TypeError`

B

---

### Q15
What is the output?
```python
text = "a,b,,c"
print(len(text.split(",")))
```
- A) `3`
- B) `4`
- C) `2`
- D) `5`

B

---

### Q16
What is the output?
```python
class A:
    def __init__(self):
        self.value = 1

class B(A):
    pass

class C(A):
    def __init__(self):
        self.value = 3

b = B()
c = C()
print(b.value, c.value)
```
- A) `1 1`
- B) `1 3`
- C) `AttributeError`
- D) `None 3`

B

---

### Q17
What does `sys.argv[0]` contain?
- A) The first command-line argument
- B) The script name
- C) The Python version
- D) The current directory

B

---

### Q18
What is the output?
```python
class A:
    def __repr__(self):
        return "A()"

    def __str__(self):
        return "Instance of A"

a = A()
print(repr(a))
```
- A) `Instance of A`
- B) `A()`
- C) `<__main__.A object>`
- D) `A() Instance of A`

B

---

### Q19
What is the output?
```python
class A:
    def __eq__(self, other):
        return True

a = A()
b = A()
print(a == b, a is b)
```
- A) `True True`
- B) `True False`
- C) `False False`
- D) `False True`


B

---

### Q20
What is the output?
```python
try:
    raise Exception("outer")
except:
    try:
        raise Exception("inner")
    except:
        print("caught inner")
    print("after inner")
```
- A) `caught inner`
- B) `caught inner after inner`
- C) `after inner`
- D) Raises `Exception`

B


---

### Q21
What is the output?
```python
s = "abcdef"
print(s[10:])
```
- A) `IndexError`
- B) `""`
- C) `None`
- D) `"f"`

B

---

### Q22
What is the output?
```python
class A:
    def method(self):
        return "instance"

    @classmethod
    def method(cls):
        return "class"

a = A()
print(a.method())
```
- A) `instance`
- B) `class`
- C) `TypeError`
- D) `instance class`

A

---

### Q23
What is the output?
```python
gen = (i for i in range(3))
for _ in range(2):
    print(next(gen), end=" ")
for x in gen:
    print(x, end=" ")
```
- A) `0 1 2`
- B) `0 1 0 1 2`
- C) `0 1 2 0 1 2`
- D) `0 1`

B

---

### Q24
What is the purpose of `__init__.py` in a package?
- A) It must contain the main() function
- B) It marks a directory as a Python package
- C) It is required only for Python 2
- D) It stores package documentation


B

---

### Q25
What is the output?
```python
class A:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

items = [A(3), A(1), A(2)]
items.sort()
print([x.val for x in items])
```
- A) `[3, 1, 2]`
- B) `[1, 2, 3]`
- C) `TypeError`
- D) `[2, 1, 3]`

B

---

### Q26
What is the output?
```python
def outer():
    x = 1
    def inner():
        yield x
        yield x + 1
    return inner()

gen = outer()
print(next(gen), next(gen))
```
- A) `1 2`
- B) `1 1`
- C) `NameError`
- D) `StopIteration`

A


---

### Q27
What is the output?
```python
class A:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

a = A()
a.x = 10
print(a.x)
```
- A) `0`
- B) `10`
- C) `AttributeError`
- D) `None`

C

---

### Q28
What is the output?
```python
s = "Python"
print(s.replace("o", "0").replace("n", "N"))
```
- A) `Pyth0n`
- B) `Pyth0N`
- C) `PythoN`
- D) `Python`


B

---

### Q29
What is the output?
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C, A))
```
- A) `True`
- B) `False`
- C) `TypeError`
- D) `None`

A

---

### Q30
What is the output?
```python
def gen():
    nums = [1, 2, 3]
    for n in nums:
        yield n * 2

result = gen()
nums = list(result)
nums.extend(list(result))
print(nums)
```
- A) `[2, 4, 6]`
- B) `[2, 4, 6, 2, 4, 6]`
- C) `[]`
- D) `[2, 4, 6, None]`

A


#Koniec 10:23
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
