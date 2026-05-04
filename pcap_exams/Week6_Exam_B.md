# Week 6 - PCAP Mock Exam B

**Time Limit:** 65 minutes (PCAP standard)
**Passing Score:** 70% (21/30)
**Topics:** Weeks 1-6 (Modules, Strings, OOP, Functional Programming, datetime, File I/O, Decorators, Iterators, Generators, Named Tuples, `__new__`)

**Instructions:**
- Choose ONE answer per question (unless stated otherwise)
- Write your answer letter next to each question
- No running code — predict outputs mentally


#Start 11:03

---

**Q1.** What is the output?
```python
class Range3:
    def __init__(self):
        self.data = [10, 20, 30]
    def __iter__(self):
        return iter(self.data)

r = Range3()
it = iter(r)
print(it is r)
print(next(it))
```
- A) `True` `10`
- B) `False` `10`
- C) `True` Error
- D) `False` Error

**Your answer:**
B

---

**Q2.** What is the output?
```python
def pipeline():
    yield from 'abc'
    yield from (1, 2)
    yield from {10, 20}

print(list(pipeline())[:5])
```
- A) `['a', 'b', 'c', 1, 2]`
- B) `['abc', (1, 2), {10, 20}]`
- C) Error — can't yield from string
- D) `['a', 'b', 'c', 1, 2]` (set order may vary, but first 5 are deterministic)

**Your answer:** 
C

---

**Q3.** What is the output?
```python
nums = [10, 20, 30]
print(next(nums))
```
- A) `10`
- B) `[10, 20, 30]`
- C) Error — list is not an iterator
- D) `None`

**Your answer:**
C

---

**Q4.** What is the output?
```python
from functools import wraps

def add_prefix(func):
    @wraps(func)
    def wrapper(*args):
        return ">> " + func(*args)
    return wrapper

@add_prefix
@add_prefix
def greet(name):
    return f"Hello, {name}"

print(greet("Bob"))
print(greet.__name__)
```
- A) `>> >> Hello, Bob` `greet`
- B) `>> Hello, Bob` `greet`
- C) `>> >> Hello, Bob` `wrapper`
- D) `>> Hello, Bob` `wrapper`

**Your answer:**
A

---

**Q5.** What is the output?
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
print(type(a))
```
- A) `True` `<class 'Singleton'>`
- B) `False` `<class 'Singleton'>`
- C) `True` `<class 'NoneType'>`
- D) Error

**Your answer:**
D

---

**Q6.** What is the output?
```python
gen = (x for x in range(5))
print(3 in gen)
print(2 in gen)
print(4 in gen)
```
- A) `True` `True` `True`
- B) `True` `False` `True`
- C) `True` `True` `False`
- D) `True` `False` `False`

**Your answer:**
B

---

**Q7.** What is the output?
```python
from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'year'])
c = Car('Toyota', 'Camry', 2024)
c2 = c._replace(year=2025)
print(c.year)
print(c2.year)
print(c is c2)
```
- A) `2025` `2025` `True`
- B) `2024` `2025` `False`
- C) `2024` `2025` `True`
- D) Error — namedtuples are immutable

**Your answer:**
D

---

**Q8.** What is the output?
```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print(funcs[0]())
print(funcs[1]())
print(funcs[2]())
```
- A) `0` `1` `2`
- B) `2` `2` `2`
- C) `0` `0` `0`
- D) Error

**Your answer:**
B

---

**Q9.** What is the output?
```python
class Counter:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i
        self.i += 1
        return result

c = Counter(3)
for x in c:
    if x == 1:
        break
for x in c:
    print(x, end=' ')
```
- A) `2`
- B) `0 1 2`
- C) `1 2`
- D) Nothing (empty)

**Your answer:**
D

---

**Q10.** What is the output?
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
result = list(map(lambda a: a.speak(), animals))
print(result)
```
- A) `['Woof', 'Meow', '...']`
- B) `['...', '...', '...']`
- C) Error — can't map lambda on objects
- D) `['Woof', 'Meow', None]`

**Your answer:**
A

---

**Q11.** What is the output?
```python
it = iter(range(5))
print(next(it, 'default'))
print(next(it, 'default'))
next(it)
next(it)
next(it)
print(next(it, 'default'))
```
- A) `0` `1` `default`
- B) `0` `1` Error
- C) `default` `default` `default`
- D) `0` `1` `5`

**Your answer:**
A

---

**Q12.** What is the output?
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

c = C()
print(isinstance(c, A))
print(issubclass(B, C))
```
- A) `True` `True`
- B) `True` `False`
- C) `False` `True`
- D) `False` `False`

**Your answer:**
B

---

**Q13.** What is the output?
```python
def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 10
    yield 20

a = gen_a()
b = gen_b()
print(next(a))
print(next(b))
print(next(a))
print(next(b))
```
- A) `1` `10` `2` `20`
- B) `1` `2` `10` `20`
- C) `1` `10` `10` `20`
- D) Error

**Your answer:**
A

---

**Q14.** What is the output?
```python
s = "Python"
print(s[::-1])
print(s[1:4])
```
- A) `nohtyP` `yth`
- B) `nohtyP` `Pyt`
- C) `nohtyP` `ytho`
- D) `Python` `yth`

**Your answer:**
A

---

**Q15.** What is the output?
```python
from collections import namedtuple

Point = namedtuple('Point', 'x y z')
p = Point(1, 2, 3)
print(p._fields)
print(dict(p._asdict()))
```
- A) `('x', 'y', 'z')` `{'x': 1, 'y': 2, 'z': 3}`
- B) `['x', 'y', 'z']` `{'x': 1, 'y': 2, 'z': 3}`
- C) `('x', 'y', 'z')` `(1, 2, 3)`
- D) Error — `_fields` is private

**Your answer:**
A

---

**Q16.** What is the output?
```python
class Doubler:
    def __new__(cls, value):
        instance = super().__new__(cls)
        instance.doubled = value * 2
        return instance

    def __init__(self, value):
        self.original = value

d = Doubler(5)
print(d.doubled)
print(d.original)
```
- A) `10` `5`
- B) `5` `5`
- C) `10` Error
- D) Error

**Your answer:**
A

---

**Q17.** What is the output?
```python
def decorator(func):
    def wrapper():
        return func()
    return wrapper

@decorator
def hello():
    return "hi"

print(hello.__name__)
```
- A) `hello`
- B) `wrapper`
- C) `decorator`
- D) Error

**Your answer:**
B

---

**Q18.** What is the output?
```python
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x > 2, numbers)))
print(result)
```
- A) `[9, 16, 25]`
- B) `[1, 4, 9, 16, 25]`
- C) `[3, 4, 5]`
- D) `[True, True, True]`

**Your answer:**
A

---

**Q19.** What is the output?
```python
class Items:
    def __init__(self):
        self.data = ['a', 'b', 'c']
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        val = self.data[self.i]
        self.i += 1
        return val

obj = Items()
print(list(obj))
print(list(obj))
```
- A) `['a', 'b', 'c']` then `['a', 'b', 'c']`
- B) `['a', 'b', 'c']` then `[]`
- C) `[]` then `[]`
- D) Error

**Your answer:**
B

---

**Q20.** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('abc')

with open('test.txt', 'a') as f:
    f.write('def')

with open('test.txt', 'r') as f:
    print(f.read())
```
- A) `def`
- B) `abc`
- C) `abcdef`
- D) Error

**Your answer:**
C

---

**Q21.** What is the output?
```python
def accumulate():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add

counter = accumulate()
print(counter(5))
print(counter(3))
print(counter(2))
```
- A) `5` `3` `2`
- B) `5` `8` `10`
- C) `5` `5` `5`
- D) Error — can't modify enclosing variable

**Your answer:**
B

---

**Q22.** What is the output?
```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

ml = MyList([10, 20, 30])
print(len(ml))
print(ml[1])
print(20 in ml)
```
- A) `3` `20` `True`
- B) `3` `20` Error
- C) Error — custom class can't use `in`
- D) `3` `20` `False`

**Your answer:**
A


---

**Q23.** What is the output?
```python
gen1 = (x for x in [1, 2, 3])
gen2 = (x for x in [1, 2, 3])
print(gen1 is gen2)

gen3 = (x for x in [1, 2, 3])
it = iter(gen3)
print(gen3 is it)
```
- A) `False` `True`
- B) `True` `True`
- C) `False` `False`
- D) `True` `False`

**Your answer:**
B

---

**Q24.** What is the output?
```python
from datetime import datetime, timedelta

dt1 = datetime(2026, 2, 28, 23, 0)
dt2 = dt1 + timedelta(hours=2)
print(dt2.strftime('%Y-%m-%d %H:%M'))
```
- A) `2026-02-28 25:00`
- B) `2026-03-01 01:00`
- C) `2026-02-29 01:00`
- D) Error

**Your answer:**
B

---

**Q25.** What is the output?
```python
class Parent:
    def __str__(self):
        return "Parent"
    def __repr__(self):
        return "Parent()"

class Child(Parent):
    def __str__(self):
        return "Child"

c = Child()
print(c)
print(repr(c))
```
- A) `Child` `Child()`
- B) `Child` `Parent()`
- C) `Parent` `Parent()`
- D) `Child` Error

**Your answer:**
B

---

**Q26.** What is the output?
```python
def gen():
    yield 'x'
    yield 'y'

g = gen()
print(next(g))
print(next(g))
print(next(g, 'z'))
```
- A) `x` `y` Error
- B) `x` `y` `z`
- C) `x` `y` `None`
- D) Error — generators don't support default

**Your answer:**
B

---

**Q27.** What is the output?
```python
reduce_fn = lambda a, b: a + b

from functools import reduce
result = reduce(reduce_fn, [1, 2, 3, 4], 10)
print(result)
```
- A) `10`
- B) `20`
- C) `24`
- D) Error — lambda defined before import

**Your answer:**
B

---

**Q28.** Which statement about `__new__` is FALSE?
- A) `__new__` is called before `__init__`
- B) `__new__` receives `cls` as its first parameter
- C) If `__new__` returns an instance of a different class, `__init__` still runs
- D) `__new__` is responsible for creating the instance

**Your answer:**
C

---

**Q29.** What is the output?
```python
class Sensor:
    def __init__(self, values):
        self.values = values
    def __iter__(self):
        for v in self.values:
            yield v * 10

s = Sensor([1, 2, 3])
it1 = iter(s)
it2 = iter(s)
print(next(it1))
print(next(it2))
print(next(it1))
```
- A) `10` `10` `20`
- B) `10` `20` `30`
- C) `10` `10` `10`
- D) `1` `1` `2`

**Your answer:**
A

---

**Q30.** What is the output?
```python
names = ['alice', 'bob', 'charlie']
upper_names = map(str.upper, names)
print(type(upper_names).__name__)
first = next(upper_names)
print(first)
remaining = list(upper_names)
print(remaining)
```
- A) `map` `ALICE` `['BOB', 'CHARLIE']`
- B) `list` `ALICE` `['BOB', 'CHARLIE']`
- C) `map` `ALICE` `['ALICE', 'BOB', 'CHARLIE']`
- D) Error — can't call `next()` on map

**Your answer:**
D

---

**End of Exam B — Good luck!**
