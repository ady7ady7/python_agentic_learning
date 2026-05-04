# Week 5 - PCAP Mock Exam B

**Time Limit:** 65 minutes (PCAP standard)
**Passing Score:** 70% (21/30)
**Topics:** Weeks 1-5 (Modules, Strings, OOP, Functional Programming, datetime, File I/O, Decorators)

**Instructions:**
- Choose ONE answer per question (unless stated otherwise)
- Write your answer letter next to each question
- No running code — predict outputs mentally


#Start 9:49
---

**Q1.** What is the output?
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args):
            result = ''
            for _ in range(n):
                result += func(*args)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(word):
    return word

print(say('ha'))
```
- A) ha
- B) hahaha
- C) hahahahahahaha
- D) Error

**Your answer:**
B



---

**Q2.** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('abc')

with open('test.txt', 'r') as f:
    f.readline()
    print(f.read())
```
- A) abc
- B) (empty string)
- C) Error
- D) None

**Your answer:**
A

---

**Q3.** What is the output?
```python
from datetime import datetime

dt = datetime(2026, 12, 25, 8, 0)
print(dt.strftime('%A'))
```
- A) Friday
- B) Thursday
- C) 25
- D) December

**Your answer:**
A

---

**Q4.** What is the output?
```python
class Vehicle:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError('Speed cannot be negative')
        self._speed = value

v = Vehicle(60)
v.speed = 80
print(v.speed)
```
- A) 60
- B) 80
- C) Error
- D) None

**Your answer:**
B

---

**Q5.** What is the output?
```python
words = ['hello', 'world', 'python']
result = list(map(lambda w: w[0].upper() + w[1:], words))
print(result)
```
- A) ['HELLO', 'WORLD', 'PYTHON']
- B) ['Hello', 'World', 'Python']
- C) ['hELLO', 'wORLD', 'pYTHON']
- D) Error

**Your answer:**
B

---

**Q6.** What is the output?
```python
try:
    result = 10 / 0
except ArithmeticError:
    print('A', end=' ')
except ZeroDivisionError:
    print('B', end=' ')
finally:
    print('C')
```
- A) A C
- B) B C
- C) A B C
- D) Error

**Your answer:**
A

---

**Q7.** What is the output?
```python
from datetime import date

d1 = date(2026, 6, 15)
d2 = date(2026, 3, 15)
diff = d1 - d2
print(diff.days)
```
- A) 3
- B) 90
- C) 92
- D) Error

**Your answer:**
C // Note: stupid question, humans do not naturally possess an ability to count such things in memory, and this doesn't refer to Python knowledge at all

---

**Q8.** What is the output?
```python
class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return 'B' + super().method()

class C(A):
    def method(self):
        return 'C' + super().method()

class D(B, C):
    def method(self):
        return 'D' + super().method()

print(D().method())
```
- A) DBA
- B) DBCA
- C) DCA
- D) Error

**Your answer:**
A

---

**Q9.** What is the output?
```python
with open('log.txt', 'w') as f:
    for i in range(3):
        f.write(f'line{i}\n')

with open('log.txt', 'r') as f:
    first = f.readline().strip()
    rest = f.read().strip()
print(first)
print(rest)
```
- A) line0 / line1\nline2
- B) line0 / line1 line2
- C) line0\n / line1\nline2\n
- D) line0line1line2

Note: `/` represents the separation between the two print outputs.

**Your answer:**
B

---

**Q10.** What is the output?
```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    """Return sum of a and b."""
    return a + b

print(add.__name__)
print(add.__doc__)
```
- A) add / Return sum of a and b.
- B) wrapper / None
- C) add / None
- D) wrapper / Return sum of a and b.

**Your answer:**
B

---

**Q11.** What is the output?
```python
s = 'Python Programming'
print(s.split()[1][:4])
```
- A) Prog
- B) Pyth
- C) gram
- D) Progr

**Your answer:**
A

---

**Q12.** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 1, 1, 0, 0)
dt2 = dt + timedelta(hours=25)
print(dt2.day, dt2.hour)
```
- A) 1 25
- B) 2 1
- C) 2 0
- D) Error

**Your answer:**
B

---

**Q13.** What is the output?
```python
class MyClass:
    __secret = 42

    @classmethod
    def reveal(cls):
        return cls.__secret

print(MyClass.reveal())
```
- A) 42
- B) Error (AttributeError)
- C) None
- D) __secret

**Your answer:**
A

---

**Q14.** What is the output?
```python
from functools import reduce

words = ['Hello', ' ', 'World', '!']
result = reduce(lambda a, b: a + b, words)
print(result)
```
- A) ['Hello', ' ', 'World', '!']
- B) Hello World!
- C) HelloWorld!
- D) Error

**Your answer:**
B

---

**Q15.** What is the output?
```python
with open('data.txt', 'w') as f:
    f.writelines(['a', 'b', 'c'])

with open('data.txt', 'r') as f:
    print(f.readlines())
```
- A) ['a', 'b', 'c']
- B) ['abc']
- C) ['a\n', 'b\n', 'c\n']
- D) abc

**Your answer:**
B

---

**Q16.** What is the output?
```python
def timer(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@timer
def compute(x):
    return x ** 2

value = compute(5)
print(value)
```
- A) start / end / 25
- B) 25 / start / end
- C) start / 25 / end
- D) Error

**Your answer:**

A

---

**Q17.** What is the output?
```python
from datetime import datetime

dt = datetime.strptime('15:45', '%H:%M')
print(dt.year, dt.hour)
```
- A) 2026 15
- B) 1900 15
- C) Error
- D) None 15

**Your answer:**
B

---

**Q18.** What is the output?
```python
class Parent:
    def __init__(self):
        self.x = 1

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.y = 2

c = Child()
print(c.x, c.y)
```
- A) Error
- B) 1 2
- C) None 2
- D) 1 None

**Your answer:**
B

---

**Q19.** What is the output?
```python
data = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, data))
doubled = list(map(lambda x: x * 2, evens))
print(doubled)
```
- A) [2, 4, 6, 8, 10, 12]
- B) [4, 8, 12]
- C) [2, 4, 6]
- D) [1, 4, 9, 16, 25, 36]

**Your answer:**

B

---

**Q20.** What is the output?
```python
with open('test.txt', 'x') as f:
    f.write('new file')

with open('test.txt', 'x') as f:
    f.write('again')
```
- A) Creates file with 'new fileagain'
- B) Creates file with 'again'
- C) FileExistsError on second open
- D) FileNotFoundError

**Your answer:**
C

---

**Q21.** What is the output?
```python
def outer():
    x = 'hello'
    def inner():
        return x.upper()
    return inner

f = outer()
print(f())
```
- A) hello
- B) HELLO
- C) Error
- D) None

**Your answer:**
B

---

**Q22.** What is the output?
```python
from datetime import date

d = date(2024, 2, 29)
print(d.year, d.month, d.day)
```
- A) 2024 2 29
- B) Error (invalid date)
- C) 2024 3 1
- D) 2024 2 28

**Your answer:**
A, again - stupid question - I obviously won't calculate it in my memory and have to Google it.

---

**Q23.** What is the output?
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
```
- A) True
- B) False
- C) Error
- D) None

**Your answer:**

I don't know honestly, first time we're seeing such a thing and it doesn't look like a real life scenario, it's just weird, as it kind of simualtes a classmethod, but it's not a classmethod (not defined as such) - weird question.

---

**Q24.** What is the output?
```python
import sys
print('math' in sys.modules)
import math
print('math' in sys.modules)
```
- A) True True
- B) False True
- C) True False
- D) False False

**Your answer:**
B

---

**Q25.** What is the output?
```python
def validate(min_val, max_val):
    def decorator(func):
        def wrapper(x):
            if min_val <= x <= max_val:
                return func(x)
            return f'{x} out of range'
        return wrapper
    return decorator

@validate(0, 100)
def process(score):
    return f'Score: {score}'

print(process(85))
print(process(150))
```
- A) Score: 85 / 150 out of range
- B) Score: 85 / Score: 150
- C) Error
- D) 85 / 150 out of range

**Your answer:**
A

---

**Q26.** What is the output?
```python
text = 'hello'
print(text.center(11, '-'))
```
- A) ---hello---
- B) --hello---
- C) hello------
- D) ------hello

**Your answer:**
A


---

**Q27.** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('first\nsecond\nthird')

with open('test.txt', 'r') as f:
    f.readline()
    line = f.readline()
print(line.strip())
```
- A) first
- B) second
- C) third
- D) first\nsecond

**Your answer:**
B

---

**Q28.** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 2, 14)
delta = timedelta(weeks=2)
result = dt + delta
print(result.strftime('%B %d'))
```
- A) February 28
- B) March 01
- C) February 14
- D) February 21

**Your answer:**
A

---

**Q29.** Which of the following is TRUE about `__init__.py`?
- A) It is required for all directories in Python 3.3+
- B) It marks a directory as a Python package
- C) It must contain at least one function definition
- D) It is automatically generated by Python

**Your answer:**
B

---

**Q30.** What is the output?
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called')
        return func(*args, **kwargs)
    return wrapper

@log
@log
def greet():
    return 'hi'

greet()
```
- A) greet called
- B) wrapper called / greet called
- C) greet called / greet called
- D) wrapper called

**Your answer:**

D


#End 10:06
---

## Answer Sheet

```
Q1:    Q11:    Q21:
Q2:    Q12:    Q22:
Q3:    Q13:    Q23:
Q4:    Q14:    Q24:
Q5:    Q15:    Q25:
Q6:    Q16:    Q26:
Q7:    Q17:    Q27:
Q8:    Q18:    Q28:
Q9:    Q19:    Q29:
Q10:   Q20:    Q30:
```

**Time taken:** ___ minutes

---

**When complete:** Submit for grading.
