# Week 5 - PCAP Mock Exam A

**Time Limit:** 65 minutes (PCAP standard)
**Passing Score:** 70% (21/30)
**Topics:** Weeks 1-5 (Modules, Strings, OOP, Functional Programming, datetime, File I/O, Decorators)

**Instructions:**
- Choose ONE answer per question (unless stated otherwise)
- Write your answer letter next to each question
- No running code — predict outputs mentally


#Start 9:30

---

**Q1.** What is the output?
```python
def greet():
    return 'hello'

def shout(func):
    def wrapper():
        return func().upper()
    return wrapper

result = shout(greet)
print(result())
```
- A) hello
- B) HELLO
- C) Error
- D) None

**Your answer:**
B

---

**Q2.** What is the output?
```python
with open('data.txt', 'w') as f:
    f.write('line1\n')
    f.write('line2\n')

with open('data.txt', 'r') as f:
    content = f.read()
print(repr(content))
```
- A) 'line1\nline2\n'
- B) 'line1 line2'
- C) ['line1\n', 'line2\n']
- D) 'line1\nline2'



**Your answer:**
A
---

**Q3.** What is the output?
```python
from datetime import date, timedelta

d = date(2026, 3, 1)
d2 = d - timedelta(days=1)
print(d2)
```
- A) 2026-02-28
- B) 2026-02-29
- C) 2026-03-00
- D) Error

**Your answer:**
A

---

**Q4.** What is the output?
```python
class A:
    def greet(self):
        return 'A'

class B(A):
    def greet(self):
        return 'B'

class C(A):
    pass

class D(B, C):
    pass

print(D().greet())
```
- A) A
- B) B
- C) Error
- D) None

**Your answer:**
B

---

**Q5.** What is the output?
```python
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args):
            return prefix + func(*args)
        return wrapper
    return decorator

@add_prefix('Mr. ')
def name(n):
    return n

print(name('Smith'))
```
- A) Smith
- B) Mr. Smith
- C) Error
- D) Mr.

**Your answer:**
B

---

**Q6.** Which file mode will raise `FileExistsError`?
- A) `open('existing.txt', 'w')`
- B) `open('existing.txt', 'a')`
- C) `open('existing.txt', 'x')`
- D) `open('existing.txt', 'r')`

**Your answer:**
C

---

**Q7.** What is the output?
```python
from datetime import datetime

dt = datetime(2026, 2, 14, 15, 30)
print(dt.strftime('%I:%M %p'))
```
- A) 15:30 PM
- B) 03:30 PM
- C) 3:30 PM
- D) 15:30

**Your answer:**
B

---

**Q8.** What is the output?
```python
try:
    x = int('abc')
except ValueError:
    print('A', end=' ')
except Exception:
    print('B', end=' ')
finally:
    print('C')
```
- A) A C
- B) B C
- C) A B C
- D) C

**Your answer:**
A

---

**Q9.** What is the output?
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5) + triple(5))
```
- A) 25
- B) 30
- C) 15
- D) 10

**Your answer:**
A

---

**Q10.** What is the output?
```python
text = 'Hello, World!'
print(text[7:12])
```
- A) World
- B) World!
- C) orld!
- D) Worl

**Your answer:**
A

---

**Q11.** What is the output?
```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

@log
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__, add.__doc__)
```
- A) wrapper None
- B) add Add two numbers.
- C) add None
- D) wrapper Add two numbers.

**Your answer:**

B

---

**Q12.** What is the output?
```python
with open('test.txt', 'w') as f:
    n = f.write('Python')
print(n)
```
- A) None
- B) 'Python'
- C) 6
- D) True

**Your answer:**
C

---

**Q13.** What is the output?
```python
class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Dog(Animal):
    def bark(self):
        return f'{self.__name} barks'

d = Dog('Rex')
print(d.get_name())
```
- A) Rex
- B) Error in `bark()`
- C) Error in `get_name()`
- D) None

**Your answer:**
A


---

**Q14.** What is the output?
```python
from datetime import datetime

d1 = datetime.strptime('2026-02-14', '%Y-%m-%d')
d2 = datetime.strptime('14/02/2026', '%d/%m/%Y')
print(d1 == d2)
```
- A) True
- B) False
- C) Error
- D) None

**Your answer:**
A


---

**Q15.** What is the output?
```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
```
- A) [1, 3, 5]
- B) [2, 4]
- C) [False, True, False, True, False]
- D) Error

**Your answer:**
B

---

**Q16.** What is the output?
```python
def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

@italic
@bold
def greet():
    return 'hello'

print(greet())
```
- A) `<b><i>hello</i></b>`
- B) `<i><b>hello</b></i>`
- C) `<b>hello</b>`
- D) `<i>hello</i>`

**Your answer:**
B

---

**Q17.** What is the output?
```python
data = {'a': 1, 'b': 2, 'c': 3}
result = list(map(lambda kv: kv[1] * 2, data.items()))
print(result)
```
- A) [2, 4, 6]
- B) {'a': 2, 'b': 4, 'c': 6}
- C) Error
- D) [('a', 2), ('b', 4), ('c', 6)]

**Your answer:**
A

---

**Q18.** What is the output?
```python
with open('file.txt', 'w') as f:
    f.write('hello')

with open('file.txt', 'a') as f:
    f.write(' world')

with open('file.txt', 'r') as f:
    print(f.read())
```
- A) hello
- B) world
- C) hello world
- D) hello\n world

**Your answer:**
C


---

**Q19.** What is the output?
```python
class Base:
    x = 10

class Child(Base):
    pass

class GrandChild(Child):
    pass

GrandChild.x = 30
print(Base.x, Child.x, GrandChild.x)
```
- A) 30 30 30
- B) 10 10 30
- C) 10 30 30
- D) Error

**Your answer:**
B

---

**Q20.** What is the output?
```python
from datetime import date

d = date(2026, 2, 6)
print(d.isoweekday(), d.weekday())
```
- A) 5 4
- B) 6 5
- C) 5 5
- D) 4 5

**Your answer:**
A

---

**Q21.** What is the output?
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def say(msg):
    return msg

print(say.__name__)
```
- A) say
- B) wrapper
- C) decorator
- D) Error

**Your answer:**

B

---

**Q22.** What is the output?
```python
try:
    f = open('missing.txt', 'r')
except FileNotFoundError:
    print('A', end=' ')
except OSError:
    print('B', end=' ')
print('C')
```
- A) A C
- B) B C
- C) A B C
- D) Error

**Your answer:**
A

---

**Q23.** What is the output?
```python
s = 'abcdef'
print(s[1:5:2])
```
- A) bd
- B) bcd
- C) bce
- D) ace

**Your answer:**
A

---

**Q24.** What is the output?
```python
from functools import reduce

result = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(result)
```
- A) 10
- B) 24
- C) [1, 2, 6, 24]
- D) 4

**Your answer:**
B

---

**Q25.** What is the output?
```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

a = Counter()
b = Counter()
c = Counter()
print(Counter.get_count())
```
- A) 1
- B) 3
- C) 0
- D) Error

**Your answer:**
B

---

**Q26.** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 2, 28, 22, 0)
dt2 = dt + timedelta(hours=3)
print(dt2.strftime('%d %B'))
```
- A) 28 February
- B) 01 March
- C) 29 February
- D) Error

**Your answer:**
B

---

**Q27.** What is the output?
```python
with open('nums.txt', 'w') as f:
    f.writelines(['1\n', '2\n', '3\n'])

with open('nums.txt', 'r') as f:
    total = sum(int(line.strip()) for line in f)
print(total)
```
- A) '123'
- B) 6
- C) ['1', '2', '3']
- D) Error

**Your answer:**
B

---

**Q28.** What is the output?
```python
def outer():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)
    return funcs

result = outer()
print(result[0](), result[1](), result[2]())
```
- A) 2 2 2
- B) 0 1 2
- C) 0 0 0
- D) Error

**Your answer:**

B

---

**Q29.** What exception does `open('nonexistent.txt', 'r')` raise?
- A) IOError
- B) FileNotFoundError
- C) OSError
- D) All of the above are correct names for this exception

**Your answer:**
B

---

**Q30.** What is the output?
```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print(f'{c.area():.1f}')
```
- A) 78.5
- B) 78.50
- C) Error (NotImplementedError)
- D) 31.4

**Your answer:**
B


End 9:45
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
