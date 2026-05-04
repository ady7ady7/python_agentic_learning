# Week 12 — PCAP Practice Exam 1
**Format mirrors real PCAP-31-03 exam**
40 Questions | Passing Score: 70% (28/40) | Time: 65 min

---

#Start 9:50

**1.** Which of the platform module functions should be used to determine the underlying platform name?

A. `platform.uname()`
B. `platform.platform()`
C. `platform.processor()`
D. `platform.python_version()`

B

---

**2.** A Python module named `mymod.py` contains a function named `myfun()`. Which of the following snippets will let you invoke this function? (Select two answers)

A. `import myfun from mymod` / `myfun()`
B. `from mymod import myfun` / `myfun()`
C. `import mymod` / `mymod.myfun()`
D. `from mymod import *` / `mymod.myfun()`

B, C

---

**3.** What is true about Python packages? (Select two answers)

A. A package must always contain a file named `__init__.py` in Python 3.
B. A package is a directory containing related modules.
C. The `.pyc` extension marks a compiled Python file.
D. The `__name__` variable always equals the package name.

B, C

---

**4.** Given the following structure, which imports of `module_a` are valid? (Select two answers)

```
mypack/
    __init__.py
    module_a.py
```

A. `import mypack.module_a`
B. `from mypack import module_a`
C. `import module_a`
D. `import module_a from mypack`

A, B

---

**5.** What is the expected output of the following code?

```python
import sys
b1 = type(sys.path) is list
b2 = type(sys.modules) is dict
print(b1 and b2)
```

A. `False`
B. `None`
C. `True`
D. `0`

A

---

**6.** Assuming the code below executes successfully, which expressions always evaluate to True? (Select two answers)

```python
import random
random.seed(42)
v1 = random.random()
random.seed(42)
v2 = random.random()
```

A. `v1 != v2`
B. `v1 == v2`
C. `v1 >= 1`
D. `random.choice([1, 2, 3]) >= 1`

B, D

---

**7.** What is true about the following snippet? (Select two answers)

```python
class E(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "it's nice to see you"

try:
    print('I feel fine')
    raise E('what a pity')
except E as e:
    print(e)
else:
    print('the show must go on')
```

A. The code outputs: `it's nice to see you`
B. The code outputs: `what a pity`
C. The code outputs: `I feel fine`
D. The `else` block executes

C, A

---

**8.** What is the expected behavior of the following code?

```python
s = '3B'
try:
    n = int(s)
except:
    n = 3
except ValueError:
    n = 2
except ArithmeticError:
    n = 1
print(n)
```

A. It outputs `1`.
B. It outputs `2`.
C. It outputs `3`.
D. The code is erroneous and will not execute.

D - bare except as the first except handle

---

**9.** Which of the following snippets will execute without raising any unhandled exceptions? (Select two answers)

A.
```python
try:
    print(-1, 1)
except:
    print(0/1)
else:
    print(1/1)
```

B.
```python
try:
    x = 1
except:
    x = x + 1
else:
    x = x + 2
```

C.
```python
try:
    x = 1/0
except NameError:
    x = 1/1
else:
    x = x + 1
```

D.
```python
try:
    x = y + 1
except (NameError, SystemError):
    x = y + 1
else:
    y = x
```

A, B

---

**10.** What is the expected behavior of the following code?

```python
m = 0

def foo(n):
    global m
    assert m != 0
    try:
        return 1 / n
    except ArithmeticError:
        raise ValueError

try:
    foo(0)
except ArithmeticError:
    m += 2
except:
    m += 1
print(m)
```

A. It outputs `2`.
B. It outputs `1`.
C. It outputs `3`.
D. The code is erroneous and will not execute.

B

---

**11.** What is the expected behavior of the following code?

```python
d = {'a': 1, 'b': 2}
try:
    d['a'] = d['c']
except BaseException as error:
    print(type(error))
```

A. It outputs `<class 'KeyError'>`.
B. It outputs `<class 'Exception'>`.
C. It outputs `<class 'BaseException'>`.
D. The code is erroneous and will not execute.

A

---

**12.** What is the expected output of the following code?

```python
string = str(1 / 4)
dummy = ''
for ch in string:
    dummy = dummy + ch
print(dummy[-1])
```

A. It raises an exception.
B. `5`
C. `4`
D. `0`

B

---

**13.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
string = 'PYTHON'[:3:]
string = string[-1] + string[-2::-1]
```

A. `len(string) == 3`
B. `string[0] == 'N'`
C. `string[-1] == 'Y'`
D. `string is None`

'T' + 'YP'
'TYP'

A, and this is the only answer that's correct here.
You've got something wrong definitely and I'm 100% sure of that.

---

**14.** Which of the following expressions evaluate to True? (Select two answers)

A. `len("""""") == 0`
B. `len('\'') == 1`
C. `ord('Z') - ord('A') == 25`
D. `chr(ord('a') + 1) == 'B'`

A, B

---

**15.** Which of the following statements are true? (Select two answers)

A. ASCII uses 8 bits to represent each character.
B. A code point is a number assigned to a given character.
C. `\e` is a valid Python escape sequence.
D. UTF-8 is backward-compatible with ASCII for the first 128 characters.


B, D

---

**16.** Which of the following expressions evaluate to True? (Select two answers)

A. `'a' * 3 > 'a' * 2`
B. `'ABC'.lower() > 'ABC'`
C. `'1' + '2' == '12'`
D. `'z' < 'Z'`

A, B, C - again you've fucked something up - three expressions ARE true.

---

**17.** Which of the following expressions evaluate to True? (Select two answers)

A. `'yt' in 'python'`
B. `str(0) in '0123456789'`
C. `'True' not in 'False'`
D. `'abc' not in 'abcde'[::-1]`

A, C

---

**18.** Which of the following invocations are valid? (Select two answers)

A. `'python'.find('')`
B. `'python'.rindex('on')`
C. `sort('python')`
D. `'python'.sorted()`

A, B

---

**19.** What is the expected output of the following code?

```python
the_string = ',,'.join(('left', 'right')) #left, ,right
the_list = the_string.split(',')
print(len(the_list))
```

A. `2`
B. `3`
C. `4`
D. An exception is raised.

B

---

**20.** Assuming the code below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class ClassA:
    var = 1
    def __init__(self, prop):
        self.prop = prop

class ClassB(ClassA):
    def __init__(self, prop):
        super().__init__(prop)

obj = ClassB(5)
```

A. `len(ClassB.__bases__) == 1`
B. `ClassA.__module__ == 'ClassA'`
C. `obj.var == 1`
D. `str(obj) == 'obj'`

A, D

---

**21.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class Foo:
    x = y = 0

    def __init__(self, val):
        self.z = val

obj = Foo(3)
```

A. `'x' in Foo.__dict__`
B. `'z' in Foo.__dict__`
C. `'y' in Foo.__dict__`
D. `len(Foo.__dict__) == 1`

A, C

---

**22.** What is the expected behavior of the following code?

```python
class Box:
    count = 0

    def __lock(self):
        Box.count += 1
        return Box.count

b = Box()
b.__Box_lock()
print(b.__Box_lock())
```

A. It outputs `1`.
B. It outputs `2`.
C. It raises an `AttributeError`.
D. It outputs `3`.

C (it should be _Box__lock)

---

**23.** What is the expected output of the following code?

```python
class Counter:
    total = 0

    def __init__(self, val):
        self.val = val
        Counter.total += 1

a = Counter(10)
b = Counter(20)
print(Counter.total + a.val + b.val)
```

A. `30`
B. `32`
C. `2`
D. An exception is raised.


B



#pauza - 10:11
#powrót - 10:31

---

**24.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
class A:
    __v = 1
    def get(self): return self.__v

class B(A):
    __v = 2
    def get(self): return self.__v

class C(B):
    __v = 3

obj_a = A()
obj_b = B()
obj_c = C()
```

A. `obj_c.get() == 2`
B. `obj_c.get() == 3`
C. `hasattr(C, 'get')`
D. `isinstance(obj_b, C)`

A, C

---

**25.** What is the expected output of the following code?

```python
class Vehicle:
    def __init__(self):
        self.kind = 'vehicle'

class Car(Vehicle):
    def __init__(self):
        super().__init__()

obj = Car()
print(isinstance(obj, Car), end=' ')
print(obj.kind)
```

A. `False vehicle`
B. `True car`
C. `True vehicle`
D. `False car`

C

---

**26.** What is true about Object-Oriented Programming in Python? (Select two answers)

A. A class is a template for creating objects.
B. Encapsulation means hiding a class inside a module.
C. Each object of the same class shares the same instance attributes.
D. Inheritance allows a child class to reuse code from a parent class.

A, D


---

**27.** Given the following classes, which class definitions are valid? (Select two answers)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
```

A. `class X(D, A): pass`
B. `class X(B, D): pass`
C. `class X(C, D): pass`
D. `class X(A, C): pass`

A, C 

---

**28.** What is the expected output of the following code?

```python
class Base:
    def value(self):
        return 0

    def doubled(self):
        return self.value() * 2

class Child_A(Base):
    def value(self):
        return 3

class Child_B(Base):
    def value(self):
        return 5

a = Child_A()
b = Child_B()
print(a.doubled() + b.doubled())
```

A. `0`
B. `16`
C. `6`
D. `10`

B

---

**29.** What is the name of the attribute that stores a class's direct superclasses?

A. `__super__`
B. `__ancestors__`
C. `__bases__`
D. `__parents__`

C

---

**30.** What is true about Python class constructors? (Select two answers)

A. The constructor is a method named `__init__`.
B. The constructor must return a non-None value.
C. The constructor must have at least one parameter (`self`).
D. A class can define more than one `__init__` method.

A, C

---

**31.** Which of the following lines of code, placed inside `inc()`, make the snippet output `3`? (Select two answers)

```python
class MyClass:
    Var = 0

    def __init__(self):
        MyClass.Var += 1
        self.prop = MyClass.Var

    def get(self):
        return self.prop

    def put(self, val):
        self.prop = val

    def inc(self, val):
        pass  # replace this line

obj = MyClass()
obj.inc(2)
print(obj.get())
```

A. `self.put(self.prop + val)`
B. `self.put(get() + val)`
C. `self.put(self.get() + val)`
D. `put(self.prop + val)`

A, C

---

**32.** What is the expected output of the following code?

```python
x = 27 ** (1 / 3)
y = 3. if x < 3.1 else 4.
print(y)
```

A. The code is erroneous and will not execute.
B. `3.0`
C. `4.0`
D. `3`

B

---

**33.** What is the expected output of the following code, assuming `data.txt` is a non-empty file in the working directory?

```python
try:
    f = open('data.txt', 'rt')
    chunk = f.read(1)
    print(len(chunk))
    f.close()
except IOError:
    print(-1)
```

A. `-1`
B. `0`
C. `1`
D. An `errno` value

C

---

**34.** What is true about lambda functions? (Select two answers)

A. They are anonymous functions.
B. They can be defined without parameters.
C. They cannot return `None`.
D. They must contain the `return` keyword.

A, C

---

**35.** Which of the following statements are true? (Select two answers)

A. The default mode of `open()` is `'r'`.
B. Opening a file with `'w'` destroys the previous contents if the file exists.
C. `closefile()` is used to close an open file.
D. Opening a file with `'a'` raises an error if the file does not exist.

A, B

---

**36.** What is the expected output of the following code?

```python
def apply(fn, a, b):
    return fn(a) + fn(b)

print(apply(lambda x: x % 2, 3, 4))
```

A. `0`
B. `1`
C. `7`
D. An exception is raised.

B

---

**37.** Assuming the snippet below executes successfully, which expressions evaluate to True? (Select two answers)

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
```

A. `double(3) == triple(2)`
B. `double is triple`
C. `double(5) == 10`
D. `triple(0) == 0`

A, C

---

**38.** What is the expected output of the following code?

```python
nums = range(-3, 3)
result = list(filter(lambda x: abs(x) < 2, nums))
print(len(result))
```

A. `6`
B. `3`
C. `2`
D. An exception is raised.

B

---

**39.** What is the expected output of the following code?

```python
my_list = [i for i in range(6)]
m = [my_list[i] for i in range(5, 0, -1) if my_list[i] % 2 == 0]
print(m)
```

A. `[0, 2, 4]`
B. `[4, 2, 0]`
C. `[4, 2]`
D. `[2, 4]`

C

---

**40.** What is the expected output of the following code, assuming `report.txt` exists in the working directory?

```python
try:
    f = open('report.txt', 'w')
    print(1, end=' ')
except IOError as e:
    print(e.errno, end=' ')
    print(2, end=' ')
else:
    f.close()
    print(3, end=' ')
```

A. `1 2 3`
B. `1 3`
C. `2 3`
D. `1 2`

B

#Koniec - 10:43

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | B | 21 | A, C |
| 2 | B, C | 22 | C |
| 3 | B, C | 23 | B |
| 4 | A, B | 24 | A, C |
| 5 | C | 25 | C |
| 6 | B, D | 26 | A, D |
| 7 | A, C | 27 | A, C |
| 8 | D | 28 | B |
| 9 | A, B | 29 | C |
| 10 | B | 30 | A, C |
| 11 | A | 31 | A, C |
| 12 | B | 32 | B |
| 13 | A, C | 33 | C |
| 14 | B, C | 34 | A, B |
| 15 | B, D | 35 | A, B |
| 16 | A, B | 36 | B |
| 17 | A, B | 37 | A, C |  
| 18 | A, B | 38 | B |
| 19 | C | 39 | C |
| 20 | A, C | 40 | B |
