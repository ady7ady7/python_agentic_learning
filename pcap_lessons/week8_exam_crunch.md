# Week 8: Exam Crunch & Documentation

**Goal:** Consolidate every PCAP-31-03 topic. Lock in the remaining gaps. Finish the project with proper docstrings.

---

## PART 1 — The PCAP-31-03 Exam Map

The official exam covers **five sections**. Know which section each topic lives in so you can budget time and priority.

| Section | Weight | Key Topics |
|---------|--------|-----------|
| 1 — Modules & Packages | ~12% | import, sys.path, __init__.py, __name__, pip |
| 2 — Exceptions | ~14% | hierarchy, try/except/else/finally, raise, custom exceptions |
| 3 — Strings | ~18% | slicing, methods, formatting (%, .format, f-strings) |
| 4 — OOP | ~34% | classes, inheritance, MRO, encapsulation, ABC, dunder methods |
| 5 — Miscellaneous | ~22% | generators, iterators, closures, lambda, decorators, stdlib |

**OOP is almost a third of the exam.** If your OOP is shaky, that's where you lose the most points.

---

## PART 2 — The Master Trap List

These are the patterns that appear repeatedly in PCAP questions and have tripped you up this programme. Read each one. Say the answer out loud.

### 2.1 — Scope & Closures

**Reading outer var — no nonlocal needed:**
```python
x = 10
def f():
    print(x)   # works — LEGB finds x in enclosing/global scope
f()            # 10
```

**Writing outer var — nonlocal required:**
```python
def outer():
    x = 10
    def inner():
        x += 1   # assignment → x marked local → UnboundLocalError
    inner()
```
Fix: add `nonlocal x` inside `inner`.

**Late binding in closures (lambda trap):**
```python
fns = [lambda: i for i in range(3)]
print(fns[0](), fns[1](), fns[2]())  # 2 2 2 — all see final i
```
Fix: `lambda i=i: i` (capture at definition time).

---

### 2.2 — raise

```python
raise "something"          # TypeError at RUNTIME (strings are not exceptions)
raise ValueError           # valid — raises ValueError() with no message
raise ValueError("oops")   # valid — raises with message
raise                      # valid inside except — re-raises current exception
```

**Never confuse these three:**
- `raise "string"` → `TypeError` at RUNTIME (not SyntaxError — parser allows it)
- `raise ExceptionClass` → valid (Python instantiates it)
- `raise ExceptionClass()` → valid (explicit instance)

---

### 2.3 — Exception Handling Order

```python
try:
    raise ValueError()
except Exception:    # catches first — ValueError IS-A Exception
    print("A")
except ValueError:   # never reached
    print("B")
```
**Rule:** Python checks `except` clauses top-to-bottom, first match wins. Put specific exceptions BEFORE general ones.

**finally always runs:**
```python
def f():
    try:
        return 1
    finally:
        return 2   # overrides the try return
f()  # 2
```

---

### 2.4 — Generators & Iterators

**iter(generator) returns the generator itself:**
```python
gen = (x for x in range(3))
assert iter(gen) is gen   # True — generators implement both __iter__ and __next__
```

**Exhausted generator returns empty:**
```python
gen = (x for x in range(3))
list(gen)   # [0, 1, 2]
list(gen)   # [] — exhausted
```

**next() after exhaustion:**
```python
next(gen)   # StopIteration
next(gen, "done")   # "done" — default prevents StopIteration
```

**__getitem__ enables iteration without __iter__:**
```python
class S:
    def __getitem__(self, i):
        if i >= 3: raise IndexError
        return i * 10
for x in S():
    print(x)   # 0, 10, 20 — legacy sequence protocol
```

---

### 2.5 — __name__

```python
# In file algo_backtest/engine/trade.py:
print(__name__)
# When IMPORTED: "algo_backtest.engine.trade"
# When RUN DIRECTLY (python trade.py): "__main__"
```

The standard guard:
```python
if __name__ == "__main__":
    main()
```

---

### 2.6 — OOP Traps

**Mutable class attribute shared by all instances:**
```python
class A:
    data = []          # ONE list, shared by all instances

a1, a2 = A(), A()
a1.data.append(1)
print(a2.data)         # [1] — same object
```

**Instance attribute shadows class attribute:**
```python
class Dog:
    sound = "woof"

d = Dog()
d.sound = "bark"       # creates INSTANCE attribute, shadows class attr
del d.sound            # deletes INSTANCE attribute
print(d.sound)         # "woof" — class attribute visible again
```

**Name mangling:**
```python
class A:
    def __init__(self):
        self.__x = 1   # stored as _A__x in __dict__

a = A()
print(a.__dict__)      # {'_A__x': 1}
print(a._A__x)         # 1  — accessible, just renamed
```

**@property calling itself → RecursionError:**
```python
class C:
    @property
    def val(self):
        return self.val    # infinite recursion!
```
Fix: use `self._val` (store in backing attribute).

**MRO and super():**
```python
class A:
    def method(self): return "A"
class B(A):
    def method(self): return super().method() + "B"
class C(B):
    def method(self): return super().method() + "C"

C().method()   # "ABC" — MRO: C → B → A
```

---

### 2.7 — Context Managers (light PCAP topic)

The `with` statement requires `__enter__` and `__exit__` to be defined on the class.

```python
class ManagedFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        return self.file        # this becomes the `as` target

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False            # False = don't suppress exceptions

with ManagedFile("data.txt") as f:
    print(f.read())
```

**PCAP trap:** The correct dunder pair is `__enter__` / `__exit__` — not `__open__`/`__close__` or `__start__`/`__stop__`.

---

### 2.8 — Logging

| Concept | Correct answer |
|---------|----------------|
| Root logger default level | `WARNING` (30) |
| Named logger default level | `NOTSET` (0) — defers to parent |
| `basicConfig()` one-shot | No effect if root already has handler |
| `logging.exception()` | Logs at ERROR + traceback; does NOT raise |
| Two-gate filtering | Message must pass BOTH logger level AND handler level |
| Logger singleton | `getLogger("same")` always returns same object |
| Last-resort handler | Fires to stderr when no handler configured; silently adds handler to root |

---

### 2.8 — Floating Point

```python
0.1 + 0.2 == 0.3    # False — IEEE 754 imprecision
0.1 + 0.2           # 0.30000000000000004
```
Use `math.isclose()` or `round()` for float comparison.

---

### 2.9 — Mutability & References

**Rebinding vs mutation:**
```python
a = [1, 2, 3]
b = a
a = [4, 5, 6]   # REBINDING — b still points to [1, 2, 3]
print(b)         # [1, 2, 3]

# vs:
a = [1, 2, 3]
b = a
a += [4]         # MUTATION via __iadd__ — modifies the same list
print(b)         # [1, 2, 3, 4]
```

**Shallow copy:**
```python
x = [1, 2, 3]
y = x[:]         # new list object, same element values
y.append(4)
print(x)         # [1, 2, 3] — x unchanged
```

---

### 2.10 — String Slicing

```python
s = "hello"
s[1:4]    # "ell"   — index 1 inclusive, 4 exclusive
s[:3]     # "hel"
s[::2]    # "hlo"
s[::-1]   # "olleh"
```
Slice never raises IndexError — out-of-range indices are silently clamped.

---

### 2.11 — Dunder Methods & Protocol

| Magic method | Triggered by |
|-------------|-------------|
| `__str__` | `str(obj)`, `print(obj)` |
| `__repr__` | `repr(obj)`, interactive shell |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]`, also enables `for` loop (legacy) |
| `__iter__` | `iter(obj)`, `for` loop |
| `__next__` | `next(obj)` |
| `__contains__` | `x in obj` |
| `__eq__` | `obj == other` |
| `__hash__` | `hash(obj)` — lost when `__eq__` defined without it |
| `__call__` | `obj()` |
| `__enter__`/`__exit__` | `with obj:` |

---

### 2.12 — isinstance vs type

```python
isinstance(True, int)    # True — bool IS-A int (subclass)
type(True) == int        # False — exact type check, bool != int
type(True) is bool       # True
isinstance(True, (int, str))  # True — accepts tuple of types
```

---

## PART 3 — Docstring Reference (Project Use)

Week 8 project work: add Google-style docstrings to all public classes and methods.

**Module docstring:**
```python
"""
Module description — one line summary.

Longer explanation if needed.
"""
```

**Function/method docstring:**
```python
def open_position(self, price: float, direction: str) -> Position:
    """Open a new position at the given price.

    Args:
        price: Entry price for the position.
        direction: "LONG" or "SHORT".

    Returns:
        The newly created Position object.

    Raises:
        ValueError: If direction is not "LONG" or "SHORT".
    """
```

**Class docstring:**
```python
class BacktestEngine:
    """Orchestrates the full backtest simulation lifecycle.

    Manages open positions, processes price ticks, and records
    closed trades for performance analysis.

    Attributes:
        strategy: The trading strategy used to generate signals.
        _trades: List of closed Trade objects.
    """
```

---

## PART 4 — PCAP Exam Technique

1. **Read every option before choosing.** The correct answer is often the one you didn't read first.
2. **Eliminate obviously wrong options first.** Get to 2 candidates, then reason.
3. **Trace code mentally line by line.** Don't guess output — run it in your head with dummy values.
4. **Watch for "which of the following is TRUE/FALSE".** The polarity flips the answer.
5. **For exception questions:** check the order of `except` clauses before anything else.
6. **For scope questions:** ask "does this function ASSIGN to the variable?" — if yes, it's local unless declared global/nonlocal.
7. **Budget time:** 40 questions, 65 minutes. ~90 seconds per question. Skip and return.

---

## PCAP Trap Quick-Reference Card

```
raise "string"           → TypeError at RUNTIME
raise ExcClass           → valid (no parens)
iter(generator)          → same object
list(exhausted_gen)      → []
NOTSET named logger      → defers to parent
WARNING root logger      → default
basicConfig() 2nd call   → ignored (one-shot)
logging.exception()      → ERROR + traceback, does NOT raise
0.1 + 0.2 == 0.3         → False
del instance attr        → reveals class attr (no error)
a = new_list             → rebinding (b unchanged)
a += [item]              → mutation (b sees it)
mutable default arg      → shared across all calls
finally return           → overrides try/except return
except order             → first match wins, specific before general
__name__ when imported   → full dotted path
__name__ when run direct → "__main__"
isinstance(True, int)    → True (bool subclass of int)
type(True) == int        → False (exact type)
__getitem__ defined      → for loop works (no __iter__ needed)
```
