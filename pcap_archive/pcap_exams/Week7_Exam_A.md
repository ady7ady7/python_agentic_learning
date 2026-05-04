# Week 7 — Mock Exam A
## PCAP-31-03 Full Simulation | 30 Questions | 40 Minutes

**Instructions:** No running code. Choose the single best answer. Time yourself.


#Start 13:48
---

### Q1
What is the output?
```python
x = 5
def f():
    print(x)
f()
```
- A) `NameError`
- B) `UnboundLocalError`
- C) `5`
- D) `None`

C

---

### Q2
What is the output?
```python
x = 5
def f():
    x = x + 1
    print(x)
f()

A
```
- A) `6`
- B) `NameError`
- C) `UnboundLocalError`
- D) `5`

---

### Q3
`iter(obj)` is called on a generator object. What does it return?
- A) A new independent copy of the generator
- B) A list of remaining values
- C) The same generator object
- D) `TypeError`

C

---

### Q4
What is `__name__` equal to inside `algo_backtest/engine/trade.py` when it is **imported** by another module?
- A) `"trade"`
- B) `"engine.trade"`
- C) `"algo_backtest.engine.trade"`
- D) `"__main__"`

C

---

### Q5
What is the output?
```python
raise "something went wrong"
```
- A) `SyntaxError` at parse time
- B) `TypeError` at runtime
- C) `ValueError` at runtime
- D) Raises the string as an exception message

D

---

### Q6
What is the output?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```
- A) `1`
- B) `2`
- C) `1` then `2`
- D) `None`

B

---

### Q7
Which of the following correctly describes `logging.exception("msg")`?
- A) Logs at CRITICAL and re-raises the current exception
- B) Logs at ERROR and appends the traceback; does not raise
- C) Only valid outside `except` blocks
- D) Identical to `logging.error("msg")`

B

---

### Q8
What is the output?
```python
class A:
    x = 10

class B(A):
    pass

B.x = 20
print(A.x, B.x)
```
- A) `10 10`
- B) `20 20`
- C) `10 20`
- D) `20 10`

C

---

### Q9
What is the output?
```python
def outer():
    results = []
    for i in range(3):
        results.append(lambda: i)
    return results

fns = outer()
print(fns[0](), fns[1](), fns[2]())
```
- A) `0 1 2`
- B) `2 2 2`
- C) `0 0 0`
- D) `TypeError`

B

---

### Q10
`isinstance(True, int)` returns:
- A) `False` — `bool` and `int` are separate types
- B) `True` — `bool` is a subclass of `int`
- C) `TypeError`
- D) Depends on Python version

B

---

### Q11
What is the output?
```python
try:
    raise ValueError("oops")
except Exception:
    print("A")
except ValueError:
    print("B")
finally:
    print("C")
```
- A) `A C`
- B) `B C`
- C) `A B C`
- D) `SyntaxError`

A

---

### Q12
A generator function has been exhausted. What happens when you call `next()` on it again?
- A) Returns `None`
- B) Restarts from the beginning
- C) Raises `StopIteration`
- D) Raises `GeneratorExit`

C

---

### Q13
What does `%y` produce in `strftime`?
- A) Full 4-digit year (e.g. `2026`)
- B) 2-digit year (e.g. `26`)
- C) ISO year number
- D) Timezone-aware year

B

---

### Q14
What is the output?
```python
x = [1, 2, 3]
y = x[:]
y.append(4)
print(x)
```
- A) `[1, 2, 3, 4]`
- B) `[1, 2, 3]`
- C) `[4]`
- D) `TypeError`

B

---

### Q15
Which statement about `basicConfig()` is true?
- A) Can be called multiple times to reconfigure logging
- B) Has no effect if any handler has already been added to the root logger
- C) Only affects named loggers, not the root logger
- D) Automatically adds a `FileHandler`

B

---

### Q16
What is the output?
```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add5.n = 99
print(add5(10))
```
- A) `109`
- B) `15`
- C) `99`
- D) `AttributeError`

B

---

### Q17
What is the default logging level for a newly created logger?
- A) `DEBUG`
- B) `INFO`
- C) `WARNING`
- D) `NOTSET`

C

---

### Q18
What is the output?
```python
class C:
    @property
    def val(self):
        return self.val
c = C()
print(c.val)
```
- A) `None`
- B) `AttributeError`
- C) `RecursionError`
- D) `TypeError`

A

---

### Q19
`getattr(obj, "name", "default")` — what does the third argument do?
- A) Sets the attribute if missing
- B) Returns that value instead of raising `AttributeError` if the attribute doesn't exist
- C) Raises `ValueError` if the attribute doesn't exist
- D) Acts as a type hint for the attribute

B

---

### Q20
What is the output?
```python
d = {}
d['a'] = 1
d['b'] = 2
for k in d:
    d['c'] = 3
```
- A) Runs fine, adds `'c'` to dict
- B) `KeyError`
- C) `RuntimeError: dictionary changed size during iteration`
- D) `StopIteration`

C

---

### Q21
Which is true about `__dict__` on an instance vs. on a class?
- A) Both store the same attributes
- B) Instance `__dict__` holds instance attributes; class `__dict__` holds class-level attributes and methods
- C) Instance `__dict__` includes inherited attributes
- D) Class `__dict__` is always empty

B

---

### Q22
What is the output?
```python
def f(a, b=[]):
    b.append(a)
    return b

print(f(1))
print(f(2))
```
- A) `[1]` then `[2]`
- B) `[1]` then `[1, 2]`
- C) `[1, 2]` then `[1, 2]`
- D) `TypeError`

B

---

### Q23
A logger named `"app.engine"` has no handlers. Its parent `"app"` has a `StreamHandler`. What happens when `"app.engine"` logs a message?
- A) The message is lost — no handler attached
- B) The message propagates to `"app"` and its `StreamHandler` handles it
- C) `AttributeError` — logger must have its own handlers
- D) The message goes to the root logger only

B

---

### Q24
What is the output?
```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace['greet'] = lambda self: f"Hello from {name}"
        return super().__new__(mcs, name, bases, namespace)

class Dog(metaclass=Meta):
    pass

print(Dog().greet())
```
- A) `Hello from Dog`
- B) `Hello from Meta`
- C) `AttributeError`
- D) `TypeError`

A

---

### Q25
Which raises `AttributeError`?
- A) `getattr(obj, "missing", None)`
- B) `obj.missing` where `missing` doesn't exist
- C) `hasattr(obj, "missing")`
- D) `dir(obj)` when `missing` is not present


B

---

### Q26
What is the output?
```python
gen = (x * 2 for x in range(3))
print(list(gen))
print(list(gen))
```
- A) `[0, 2, 4]` then `[0, 2, 4]`
- B) `[0, 2, 4]` then `[]`
- C) `[]` then `[0, 2, 4]`
- D) `StopIteration`

B

---

### Q27
`logging.warning()` vs `warnings.warn()` — which is true?
- A) They are aliases for the same function
- B) `logging.warning()` writes to the logging system; `warnings.warn()` triggers Python's built-in warning mechanism
- C) `warnings.warn()` is only for deprecated code
- D) `logging.warning()` raises an exception; `warnings.warn()` does not


B

---

### Q28
What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return super().method() + "B"

class C(B):
    def method(self):
        return super().method() + "C"

print(C().method())
```
- A) `"C"`
- B) `"BC"`
- C) `"ABC"`
- D) `"ACB"`

C

---

### Q29
What is the output?
```python
import logging
logger = logging.getLogger("myapp")
logger.warning("first")
logging.basicConfig(level=logging.DEBUG)
logger.debug("second")
```
- A) Prints `first` only (WARNING threshold)
- B) Prints `first` and `second`
- C) Prints nothing — no handler attached
- D) `first` only — basicConfig has no effect because root already has a handler from `logger.warning`

B

---

### Q30
Which correctly implements `__iter__` and `__next__` on a class to make it a proper iterator?
```python
# Option A
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Option B
class Counter:
    def __init__(self, stop):
        self.stop = stop
    def __next__(self):
        return range(self.stop)

# Option C
class Counter:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return range(self.stop)
```
- A) Option A only
- B) Option B only
- C) Option C only
- D) All three

A

#End 14:02

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

Q1: C | Q2: C | Q3: C | Q4: C | Q5: B | Q6: B | Q7: B | Q8: C | Q9: B | Q10: B | Q11: A | Q12: C | Q13: B | Q14: B | Q15: B | Q16: B | Q17: D | Q18: C | Q19: B | Q20: C | Q21: B | Q22: B | Q23: B | Q24: A | Q25: B | Q26: B | Q27: B | Q28: C | Q29: D | Q30: A
