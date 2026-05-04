# Week 12 — PCAP Practice Exam 2
**Format mirrors real PCAP-31-03 exam**
40 Questions | Passing Score: 70% (28/40) | Time: 65 min


#Start 14:00
---

**1.** Which of the following `platform` module functions returns a namedtuple with full system information (system, node, release, version, machine, processor)?

A. `platform.platform()`
B. `platform.system()`
C. `platform.uname()`
D. `platform.node()`

C

---

**2.** Which of the following are valid ways to use a function from a module? (Select two answers)

A. `from math import sqrt` / `sqrt(4)`
B. `import sqrt from math` / `sqrt(4)`
C. `import math` / `math.sqrt(4)`
D. `from math import *` / `math.sqrt(4)`

A, C

---

**3.** What is true about Python modules? (Select two answers)

A. A module is a single file containing Python definitions and statements.
B. The `__name__` variable equals `'__main__'` only when the module is run directly.
C. Importing a module twice always re-executes it.
D. A module file must always define at least one function.

A, B

---

**4.** Which of the following correctly describe `sys.path`? (Select two answers)

A. It is a list of strings representing directories Python searches for modules.
B. It can be modified at runtime to add new search paths.
C. It is a dictionary mapping module names to file paths.
D. It always contains only the standard library directory.

A, B

---

**5.** What is the expected output of the following code?

```python
import sys
print(type(sys.argv) is list)
print(type(sys.modules) is dict)
```

A. `True` / `False`
B. `False` / `True`
C. `True` / `True`
D. `False` / `False`

C

---

**6.** What is the expected output of the following code?

```python
import random
random.seed(0)
a = random.randint(1, 10)
random.seed(0)
b = random.randint(1, 10)
print(a == b)
print(a >= 1)
```

A. `False` / `True`
B. `True` / `False`
C. `True` / `True`
D. `False` / `False`

C

---

**7.** What is true about the following snippet? (Select two answers)

```python
class MyEx(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "something went wrong"

try:
    print('before')
    raise MyEx('details')
except MyEx as e:
    print(e)
else:
    print('no exception')
```

A. The output includes `before`
B. The output includes `something went wrong`
C. The output includes `details`
D. The `else` block executes

A, B

---

**8.** What is the expected behavior of the following code?

```python
try:
    x = 1 / 0
except:
    print('a')
except ZeroDivisionError:
    print('b')
```

A. It outputs `a`.
B. It outputs `b`.
C. It outputs `a` then `b`.
D. The code is erroneous and will not execute.

D

---

**9.** Which of the following snippets execute without raising any unhandled exceptions? (Select two answers)

A.
```python
try:
    x = int('42')
except ValueError:
    x = 0
else:
    x = x + 1
```

B.
```python
try:
    x = 1 / 0
except TypeError:
    x = -1
else:
    x = x + 1
```

C.
```python
try:
    x = 2
except:
    x = 0
else:
    x = x * 2
```

D.
```python
try:
    raise NameError
except ValueError:
    pass
```

A, C

---

**10.** What is the expected output of the following code?

```python
n = 0

def bar(x):
    global n
    assert x >= 0
    try:
        return 10 / x
    except ZeroDivisionError:
        raise RuntimeError

try:
    bar(-1)
except RuntimeError:
    n = 10
except AssertionError:
    n = 5
except:
    n = 1
print(n)
```

A. `10`
B. `1`
C. `5`
D. `0`

C

---

**11.** What is the expected output of the following code?

```python
lst = [1, 2, 3]
try:
    lst[0] = lst[5]
except BaseException as e:
    print(type(e).__name__)
```

A. `BaseException`
B. `Exception`
C. `IndexError`
D. The code is erroneous and will not execute.

C

---

**12.** What is the expected output of the following code?

```python
string = str(2 / 4)
result = ''
for ch in string:
    result += ch
print(result[0])
```

A. `0`
B. `2`
C. `5`
D. An exception is raised.

A

---

**13.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
s = 'LAMBDA'[:4:]
s = s[-1] + s[-2::-1]
```

A. `s[0] == 'B'`
B. `len(s) == 4`
C. `s[-1] == 'L'`
D. `s is None`

'LAMB' -> B + MAL = 'BMAL' 

A, B, C - all three are true

---

**14.** Which of the following expressions evaluate to True? (Select two answers)

A. `len('') == 0`
B. `len("\\") == 1`
C. `ord('a') - ord('A') == 32`
D. `chr(65) == 'a'`

A, B

---

**15.** Which of the following are true about character encoding? (Select two answers)

A. Unicode can represent characters from all writing systems.
B. ASCII uses 16 bits per character.
C. The `ord()` function returns the Unicode code point of a character.
D. `chr(65)` returns `'a'`.

A, C

As for D, this is a retarded fucking question, how would I remember that. Honestly dude, don't expect me to remember such things by heart...

---

**16.** Which of the following expressions evaluate to True? (Select two answers)

A. `'abc' < 'abcd'`
B. `'A' > 'a'`
C. `'z' > 'Z'`
D. `'2' + '3' == 5`

A, C

---

**17.** Which of the following expressions evaluate to True? (Select two answers)

A. `'py' in 'python'`
B. `str(1 - 1) in '01234'`
C. `'xyz' not in 'xyzabc'`
D. `'abc' not in 'cba'[::-1]`

A, B

---

**18.** Which of the following invocations are valid? (Select two answers)

A. `'hello'.rfind('l')`
B. `'hello'.rindex('z')`
C. `'hello'.sorted()`
D. `sorted('hello')`

A, B

---

**19.** What is the expected output of the following code?

```python
s = '--'.join(('a', 'b', 'c'))
parts = s.split('-')
print(len(parts))
```

A. `3`
B. `4`
C. `5`
D. An exception is raised.
a--b--c
['a', '', 'b', '', 'c']

C

---

**20.** Assuming the code below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class Alpha:
    value = 10

    def __init__(self, x):
        self.x = x

class Beta(Alpha):
    pass

obj = Beta(3)
```

A. `len(Beta.__bases__) == 1`
B. `obj.value == 10`
C. `'x' in Beta.__dict__`
D. `str(obj) == 'obj'`

A, B

---

**21.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class Sample:
    p = q = 0

    def __init__(self, val):
        self.r = val

s = Sample(7)
```

A. `'p' in Sample.__dict__`
B. `'r' in Sample.__dict__`
C. `'q' in Sample.__dict__`
D. `'r' in s.__dict__`

A, C

---

**22.** What is the expected behavior of the following code?

```python
class Vault:
    total = 0

    def __lock(self):
        Vault.total += 1
        return Vault.total

v = Vault()
v.__Vault_lock()
print(v.__Vault_lock())
```

A. It outputs `2`.
B. It outputs `1`.
C. It raises an `AttributeError`.
D. It outputs `3`.

C
Wrong spelling, it should be _Vault__lock if we were to call it properly.

---

**23.** What is the expected output of the following code?

```python
class Item:
    stock = 0

    def __init__(self, qty):
        self.qty = qty
        Item.stock += 1

x = Item(5)
y = Item(10)
print(Item.stock + x.qty + y.qty)
```

A. `17`
B. `15`
C. `2`
D. An exception is raised.

A

---

**24.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class P:
    __val = 10
    def get(self): return self.__val

class Q(P):
    __val = 20
    def get(self): return self.__val

class R(Q):
    __val = 30

obj_p = P()
obj_q = Q()
obj_r = R()
```

A. `obj_r.get() == 20`
B. `obj_r.get() == 30`
C. `isinstance(obj_q, P)`
D. `type(obj_r) is Q`

A, C

---

**25.** What is the expected output of the following code?

```python
class Animal:
    def __init__(self):
        self.name = 'animal'

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'dog'

obj = Dog()
print(isinstance(obj, Animal), end=' ')
print(obj.name)
```

A. `True animal`
B. `False dog`
C. `True dog`
D. `False animal`

C

---

**26.** What is true about Object-Oriented Programming in Python? (Select two answers)

A. A class variable is shared across all instances.
B. `__init__` is called automatically when an object is created.
C. Subclasses cannot override methods from their parent class.
D. Python does not support multiple inheritance.

A, B

---

**27.** Given the following classes, which class definitions are declared properly? (Select two answers)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(C): pass
```

A. `class X(B, C): pass`
B. `class X(D, C): pass`
C. `class X(C, D): pass`
D. `class X(A, B): pass`

A, B

---

**28.** What is the expected output of the following code?

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"area={self.area()}"

class Square(Shape):
    def area(self):
        return 4

class Triangle(Shape):
    def area(self):
        return 3

s = Square()
t = Triangle()
print(s.describe(), t.describe())
```

A. `area=0 area=0`
B. `area=4 area=3`
C. `area=4 area=0`
D. An exception is raised.

A

---

**29.** Which attribute stores the full Method Resolution Order chain including `object`?

A. `__bases__`
B. `__mro__`
C. `__parents__`
D. `__chain__`

B

---

**30.** What is true about Python class constructors? (Select two answers)

A. `__init__` is the constructor method.
B. `__init__` can return any value.
C. `self` is the conventional name for the first parameter of instance methods.
D. Calling `super().__init__()` is always mandatory.

A, C

---

**31.** Which lines, placed inside `double_it()`, make the output equal to `6`? (Select two answers)

```python
class Tool:
    def __init__(self):
        self.val = 3

    def get(self):
        return self.val

    def set(self, v):
        self.val = v

    def double_it(self):
        pass  # replace this line

t = Tool()
t.double_it()
print(t.get())
```

A. `self.set(self.val * 2)`
B. `self.set(val * 2)`
C. `self.set(self.get() * 2)`
D. `set(self.val * 2)`

A, C

---

**32.** What is the expected output of the following code?

```python
x = 64 ** 0.5
y = 8. if x == 8.0 else 0.
print(y)
print(type(y))
```

A. The code is erroneous and will not execute.
B. `0.0` / `<class 'float'>`
C. `8.0` / `<class 'float'>`
D. `8` / `<class 'int'>`

C

---

**33.** What is the expected output of the following code, assuming `log.txt` exists and is non-empty?

```python
try:
    f = open('log.txt', 'r')
    data = f.read(3)
    print(len(data))
    f.close()
except IOError:
    print(-1)
```

A. `-1`
B. `0`
C. `3`
D. An `errno` value

C

---

**34.** What is true about lambda functions? (Select two answers)

A. A lambda can accept zero parameters.
B. A lambda body can contain multiple statements separated by semicolons.
C. A lambda always returns a value (or `None` implicitly).
D. A lambda must be assigned to a variable to be used.

A, C

---

**35.** Which of the following statements are true about `open()`? (Select two answers)

A. `open('f.txt', 'x')` fails if the file already exists.
B. `open('f.txt', 'a')` creates the file if it does not exist.
C. `open('f.txt')` opens the file for writing by default.
D. `open('f.txt', 'r+')` truncates the file content.

A, B

---

**36.** What is the expected output of the following code?

```python
def transform(fn, x, y):
    return fn(x) - fn(y)

print(transform(lambda x: x ** 2, 3, 2))
```

A. `1`
B. `5`
C. `25`
D. An exception is raised.

B

---

**37.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
def outer(n):
    def inner(x):
        return x + n
    return inner

add10 = outer(10)
add20 = outer(20)
```

A. `add10(5) == add20(5)`
B. `add10(10) == add20(0)`
C. `add10(0) == 10`
D. `add20 is add10`

B, C

---

**38.** What is the expected output of the following code?

```python
data = range(-4, 4)
result = list(filter(lambda x: x > 0, data))
print(len(result))
```

A. `8`
B. `4`
C. `3`
D. An exception is raised.

C

---

**39.** What is the expected output of the following code?

```python
my_list = [i * 2 for i in range(5)]
m = [my_list[i] for i in range(4, -1, -1) if my_list[i] % 3 == 0]
print(m)
```

A. `[0, 6]`
B. `[6, 0]`
C. `[0]`
D. `[6]`


B


---

**40.** What is the expected output of the following code, assuming `notes.txt` does NOT exist in the working directory?

```python
try:
    f = open('notes.txt', 'r')
    print(1, end=' ')
except IOError as e:
    print(2, end=' ')
else:
    f.close()
    print(3, end=' ')
```

A. `1 3`
B. `1 2`
C. `2`
D. `2 3`

C

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | C | 21 | A, C, D |
| 2 | A, C | 22 | C |
| 3 | A, B | 23 | A |
| 4 | A, B | 24 | A, C |
| 5 | C | 25 | C |
| 6 | C | 26 | A, B |
| 7 | A, B | 27 | A, C |
| 8 | D | 28 | B |
| 9 | A, C | 29 | B |
| 10 | C | 30 | A, C |
| 11 | C | 31 | A, C |
| 12 | A | 32 | C |
| 13 | A, C | 33 | C |
| 14 | A, B | 34 | A, C |
| 15 | A, C | 35 | A, B |
| 16 | A, C | 36 | B |
| 17 | A, B | 37 | B, C |
| 18 | A, D | 38 | B |
| 19 | C | 39 | B |
| 20 | A, B | 40 | C |
