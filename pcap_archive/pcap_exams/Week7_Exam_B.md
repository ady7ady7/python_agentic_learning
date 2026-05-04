# Week 7 — Mock Exam B
## PCAP-31-03 Full Simulation | 30 Questions | 40 Minutes

**Instructions:** No running code. Choose the single best answer. Time yourself.


#Start 14:40

---

### Q1
What is the output?
```python
def outer():
    count = 0
    def inner():
        count += 1
        return count
    return inner

f = outer()
print(f())
```
- A) `1`
- B) `0`
- C) `UnboundLocalError`
- D) `NameError`

C

---

### Q2
What is the output?
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

f = outer()
print(f())
print(f())
```
- A) `1` then `1`
- B) `1` then `2`
- C) `0` then `1`
- D) `UnboundLocalError`

B

---

### Q3
What does `iter(gen)` return when `gen` is a generator?
- A) A fresh copy of the generator
- B) A list of the generator's values
- C) `gen` itself — the same object
- D) `TypeError`

C

---

### Q4
`__name__` inside `algo_backtest/strategies/base.py` when **run directly** (`python base.py`):
- A) `"algo_backtest.strategies.base"`
- B) `"base"`
- C) `"__main__"`
- D) `"strategies.base"`

C

---

### Q5
What is the output?
```python
class A:
    data = []

a1 = A()
a2 = A()
a1.data.append(1)
print(a2.data)
```
- A) `[]`
- B) `[1]`
- C) `AttributeError`
- D) `TypeError`


B

---

### Q6
What is `raise TypeError` without parentheses?
- A) `SyntaxError` — must use parentheses
- B) Valid — raises a `TypeError` instance with no message
- C) Raises the `TypeError` class itself, not an instance
- D) `AttributeError`

B

---

### Q7
What is the output?
```python
x = "hello"
print(x[1:4])
```
- A) `"hel"`
- B) `"ell"`
- C) `"ello"`
- D) `"hell"`

B

---

### Q8
Which format code gives the **full 4-digit year** in `strftime`?
- A) `%y`
- B) `%Y`
- C) `%d`
- D) `%j`

B

---

### Q9
`logging.exception("msg")` — which is true?
- A) Logs at CRITICAL and re-raises
- B) Logs at ERROR, appends traceback, does not raise or stop execution
- C) Only valid inside `except` blocks; raises outside them
- D) Identical to `logging.error("msg")`

B

---

### Q10
What is the output?
```python
d = {'a': 1, 'b': 2}
print(d.get('c', 0))
```
- A) `None`
- B) `KeyError`
- C) `0`
- D) `AttributeError`

C

---

### Q11
What is the output?
```python
gen = (i for i in range(5))
next(gen)
next(gen)
print(list(gen))
```
- A) `[0, 1, 2, 3, 4]`
- B) `[2, 3, 4]`
- C) `[0, 1]`
- D) `StopIteration`

B

---

### Q12
Which is a valid read-only property in Python?
```python
# A
class C:
    @property
    def val(self): return self._val

# B
class C:
    @property
    def val(self): return self.val  # no underscore

# C
class C:
    def val(self): return self._val
```
- A) A only
- B) B only
- C) C only
- D) All three

A

---

### Q13
What is the output?
```python
class A:
    def __init__(self):
        self.x = 1
        self.__y = 2

a = A()
print(a.__dict__)
```
- A) `{'x': 1, '__y': 2}`
- B) `{'x': 1, '_A__y': 2}`
- C) `{'x': 1}`
- D) `AttributeError`

B

---

### Q14
The root logger's default level is:
- A) `DEBUG`
- B) `INFO`
- C) `WARNING`
- D) `NOTSET`

C

---

### Q15
What is the output?
```python
def f():
    try:
        1 / 0
    except ZeroDivisionError:
        return "caught"
    finally:
        return "finally"

print(f())
```
- A) `"caught"`
- B) `"finally"`
- C) `"caught"` then `"finally"`
- D) `ZeroDivisionError`

B

---

### Q16
`isinstance(obj, (int, str))` — what does it check?
- A) Whether `obj` is exactly `int` or exactly `str` (no subclasses)
- B) Whether `obj` is an instance of `int` or `str` (including subclasses)
- C) `TypeError` — tuple argument not allowed
- D) Returns the type name

B


---

### Q17
What is the output?
```python
class Dog:
    sound = "woof"

d = Dog()
d.sound = "bark"
del d.sound
print(d.sound)
```
- A) `AttributeError`
- B) `"bark"`
- C) `"woof"`
- D) `None`

A

---

### Q18
Which statement about a `FileHandler` and `StreamHandler` sharing a `Formatter` is true?
- A) Each handler must have its own `Formatter` object — they cannot be shared
- B) A single `Formatter` instance can be passed to multiple handlers with `setFormatter()`
- C) `Formatter` is attached to the logger, not to handlers
- D) `StreamHandler` does not accept a `Formatter`

B


---

### Q19
What is the output?
```python
print(0.1 + 0.2 == 0.3)
```
- A) `True`
- B) `False`
- C) `TypeError`
- D) Depends on platform

A

---

### Q20
Which is the correct way to call `super().__init__()` in `class B(A)`?
- A) `A.__init__(self)`  ← only valid way
- B) `super(B, self).__init__()`  ← only valid way
- C) `super().__init__()`  ← the modern preferred way (Python 3)
- D) Both B and C are valid


C (A would also work)

---

### Q21
What is the output?
```python
a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(b)
```
- A) `[4, 5, 6]`
- B) `[1, 2, 3]`
- C) `[1, 2, 3, 4, 5, 6]`
- D) `None`

A


---

### Q22
`hasattr(obj, "name")` internally does what?
- A) Calls `getattr` and returns `False` if `AttributeError` is raised
- B) Checks `obj.__dict__` only
- C) Raises `AttributeError` if the attribute is missing
- D) Returns the attribute value, not a boolean

A

---

### Q23
What is the output?
```python
def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@dec
def greet(name):
    """Say hello."""
    return f"Hello {name}"

print(greet.__name__)
```
- A) `"greet"`
- B) `"wrapper"`
- C) `"dec"`
- D) `AttributeError`

B

---

### Q24
`logging.getLogger("app")` called three times — how many logger objects are created?
- A) 3 — one per call
- B) 1 — loggers are singletons keyed by name
- C) 2 — first call creates, subsequent calls copy
- D) Depends on whether handlers are attached

B

---

### Q25
What is the output?
```python
class A:
    pass

class B(A):
    pass

print(issubclass(B, A), issubclass(A, B))
```
- A) `True True`
- B) `True False`
- C) `False True`
- D) `False False`

B


---

### Q26
Which `open()` mode creates a new file, and **raises an error** if the file already exists?
- A) `'w'`
- B) `'a'`
- C) `'x'`
- D) `'r+'`


C

---

### Q27
What is the output?
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
logging.debug("test")
```
- A) Prints nothing — ERROR level suppresses DEBUG
- B) Prints the debug message — first `basicConfig` wins
- C) Prints the debug message twice
- D) `AttributeError`

B

---

### Q28
What is the output?
```python
class MyList:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return self.data[idx]

ml = MyList([10, 20, 30])
for item in ml:
    print(item, end=" ")
```
- A) `AttributeError` — no `__iter__` defined
- B) `10 20 30`
- C) `[10, 20, 30]`
- D) `TypeError`

A

---

### Q29
What is the output?
```python
x = [1, 2, 3]
y = x
y += [4]
print(x)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) `TypeError`

B

---

### Q30
Which is true about abstract base classes (`ABC`) and `@abstractmethod`?
- A) A class with `@abstractmethod` can be instantiated if it inherits from `ABC`
- B) A subclass that does not implement all `@abstractmethod` methods raises `TypeError` on instantiation
- C) `@abstractmethod` methods must have no body (pass only)
- D) `ABC` is in the `typing` module


B

#End 14:49


---

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

**Answer Key** *(fold or scroll down only after completing)*

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Q1: C | Q2: B | Q3: C | Q4: C | Q5: B | Q6: B | Q7: B | Q8: B | Q9: B | Q10: C | Q11: B | Q12: A | Q13: B | Q14: C | Q15: B | Q16: B | Q17: C | Q18: B | Q19: B | Q20: D | Q21: B | Q22: A | Q23: B | Q24: B | Q25: B | Q26: C | Q27: B | Q28: B | Q29: B | Q30: B
