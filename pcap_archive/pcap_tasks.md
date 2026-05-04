# Week 13 Day 4 — Final Heavy Review: All Active Gaps
**Date:** 2026-04-10 | **Focus:** lambda expressions, sys.modules, nonlocal, nested exceptions, __str__/__repr__ trap, type(e), single-answer discipline, project verify

---

## Task 1 — Lambda body: expression only [D3 T6 Q3 slip]

**THE RULE:**
```
Lambda body = ONE expression. Expressions produce values.
Statements (if, for, while, return, del, assert) → FORBIDDEN → SyntaxError
Ternary IS an expression:     x if cond else y  ✅
List comprehension:           [x for x in ...]  ✅
Function call:                print(x)          ✅
```

**A)** Valid (V) or SyntaxError (S):
```python
f1 = lambda x: x * 2
f2 = lambda x: if x > 0: x else -x
f3 = lambda x: x if x > 0 else -x
f4 = lambda x: [i for i in range(x)]
f5 = lambda x: for i in range(x): print(i)
f6 = lambda x: (x, x * 2)
f7 = lambda x: return x + 1
f8 = lambda x: assert x > 0
f9 = lambda x: print(x) or x
f10 = lambda x, y=[], z=0: x + z
```

**B)** Predict the output:
```python
ops = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
}
print(ops['add'](3, 4))
print(ops['mul'](ops['sub'](10, 4), 2))
```

**C)** SINGLE answer — which statement about lambda is true?
- A: A lambda body can contain multiple statements separated by semicolons
- B: A lambda can use a ternary expression as its body
- C: A lambda must always accept at least one argument
- D: A lambda cannot be assigned to a variable

Write answers here:
```
A) f1-f10:
# f1 = lambda x: x * 2 #valid
#f2 = lambda x: if x > 0: x else -x #SyntaxError
# f3 = lambda x: x if x > 0 else -x #VALID
#f4 = lambda x: [i for i in range(x)] #valid
# f5 = lambda x: for i in range(x): print(i) #syntaxerr
# f6 = lambda x: (x, x * 2) #VALID
# f7 = lambda x: return x + 1 #SyntaxErorr
# f8 = lambda x: assert x > 0 #SyntaxErorr
# f9 = lambda x: print(x) or x #Valid
# f10 = lambda x, y=[], z=0: x + z #Valid


B) 2 outputs:
7, 12

C) Single answer:
C
```

---

## Task 2 — `nonlocal` mechanics [W12 Exam A Q27 gap]

**THE RULE:**
```
nonlocal x  → binds x to nearest enclosing (non-global) scope
global x    → binds x to module level
No keyword  → reading outer x works; assigning creates a NEW local x (shadowing)
```

**A)** Predict the output:
```python
def outer():
    count = 0
    def increment():
        nonlocal count
        count += 1
    increment()
    increment()
    increment()
    return count

print(outer())
```

```python
def make_counter():
    n = 0
    def up():   nonlocal n; n += 1
    def down(): nonlocal n; n -= 1
    def get():  return n
    return up, down, get

up, down, get = make_counter()
up(); up(); up()
down()
print(get())
```

```python
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
    inner()
    print(x)
outer()
print(x)
```

**B)** Predict the output — late binding trap:
```python
def factory():
    results = []
    for i in range(3):
        def f():
            return i
        results.append(f)
    return results

fns = factory()
print(fns[0]())
print(fns[1]())
print(fns[2]())
```

```python
def factory():
    results = []
    for i in range(3):
        def f(n=i):
            return n
        results.append(f)
    return results

fns = factory()
print(fns[0]())
print(fns[1]())
print(fns[2]())
```

**C)** SINGLE answer — what does `nonlocal` do?
- A: Makes a variable visible in all scopes
- B: Binds a variable to the nearest enclosing non-global scope
- C: Binds a variable to the module-level scope
- D: Creates a new variable in the local scope

Write answers here:
```
A) 3 snippets:
3;
2;
30, 20, 10;



B) 2 snippets:
12, 12, 12
10, 11, 12


C) Single answer:
B
```

---

## Task 3 — Nested exception handling: inner/outer flows [replaces raise X from Y]

**THE RULES:**
```
except catches → only from its paired try block
An exception raised inside except → escapes current try, propagates to outer try
bare except: → catches EVERYTHING including SystemExit, KeyboardInterrupt
else:        → runs only if NO exception in try (skipped if exception caught or uncaught)
finally:     → ALWAYS runs (even if return, even if exception escapes)
finally with return → overrides try's return AND suppresses propagating exceptions
```

**A)** Predict the output — trace carefully:
```python
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print('inner caught')
        raise ValueError('from inner')
    print('after inner try')
except ValueError:
    print('outer caught ValueError')
except ZeroDivisionError:
    print('outer caught ZeroDivision')
print('end')
```

**B)** Predict the output:
```python
def f():
    try:
        return 'try'
    finally:
        return 'finally'

def g():
    try:
        raise RuntimeError('boom')
    finally:
        print('finally runs')

print(f())
try:
    g()
except RuntimeError:
    print('caught runtime')
```

**C)** Predict the output:
```python
try:
    try:
        raise TypeError('t')
    except ValueError:
        print('inner ValueError')
    else:
        print('inner else')
    finally:
        print('inner finally')
except TypeError:
    print('outer TypeError')
finally:
    print('outer finally')
```

**D)** Predict the output:
```python
def risky(n):
    try:
        result = 10 / n
    except ZeroDivisionError:
        print('zero!')
        result = 0
    except (TypeError, ValueError) as e:
        print(f'bad input: {type(e).__name__}')
        result = -1
    else:
        print(f'ok: {result}')
    finally:
        print('done')
    return result

print(risky(2))
print(risky(0))
print(risky('x'))
```

Write answers here:
```
A) outputs:
#print wise:
#1. inner caught
#2. after inner try
#3. outer caught ValueError
#4. end


B) outputs:
#1. finally
#2. finally runs
#3. caught runtime


C) outputs:
#1. inner finally
#2. outer TypeError
#3. outer finally


D) outputs (all lines from all 3 calls):
print(risky(2)) #ok: 5.0 -> done -> 5.0
print(risky(0)) #zero! -> done -> 0
print(risky('x')) #bad input: TypeError -> done -> -1

```

---

## Task 4 — `__str__` / `__repr__` trap: full drill [recurring]

**THE RULES:**
```
str(obj)   → __str__ if defined, else falls back to __repr__
repr(obj)  → __repr__ if defined, else '<ClassName object at 0x...>'
print(obj) → calls str(obj)

If ONLY __repr__ defined:
  str(obj)  → uses __repr__  ← TRAP
  repr(obj) → uses __repr__

If ONLY __str__ defined:
  str(obj)  → uses __str__
  repr(obj) → default '<ClassName object at 0x...>'

Exception repr(e) → always "ClassName(arg1, arg2)" — uses e.args, ignores __str__
```

**A)** Predict the output:
```python
class Token:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return f"Token({self.val!r})"

t = Token("hello")
print(str(t))
print(repr(t))
print(str(t) == repr(t))
```

```python
class Tag:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"<{self.name}>"

g = Tag("div")
print(str(g))
print(repr(g))
print(str(g) == repr(g))
```

**B)** SINGLE answer:
```python
class Node:
    def __repr__(self):
        return "Node()"
```
- A: `str(Node())` raises `AttributeError`
- B: `str(Node())` returns `"Node()"`
- C: `str(Node())` returns `"<Node object at 0x...>"`
- D: `repr(Node())` returns `"<Node object at 0x...>"`

**C)** SINGLE answer:
```python
class E(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    def __str__(self):
        return "custom"

try:
    raise E("original")
except E as e:
    pass
```
- A: `repr(e)` returns `"custom"`
- B: `repr(e)` returns `"E('original')"`
- C: `str(e)` returns `"E('original')"`
- D: `e.args` is empty

Write answers here:
```
A) snippet 1 (3 outputs):
print(str(t)) #Token(hello)
print(repr(t)) #Token(hello)
print(str(t) == repr(t)) #True

   snippet 2 (3 outputs):
print(str(g)) #<div>
print(repr(g)) #<__main__.Tag object at XXXX...>
print(str(g) == repr(g)) #False

B) Single answer:
B


C) Single answer:
B

```

---

## Task 5 — Full PCAP gauntlet: 10 questions

**Q1.** What is the output?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```
- A: `1`
- B: `2`
- C: `None`
- D: Raises an exception


B


**Q2.** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x = 2

class C(B):
    pass

obj = C()
print(obj.x)
```
- A: `1`
- B: `2`
- C: Raises `AttributeError`
- D: `None`

B

**Q3.** Which TWO are True?
```python
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    return x

result = outer()
```
- A: `result == 5`
- B: `result == 10`
- C: The code raises `NameError`
- D: `inner()` modifies `x` in `outer`'s scope

B, D

**Q4.** What is the output?
```python
try:
    raise ValueError('bad')
except ValueError as e:
    raise TypeError('worse')
except TypeError:
    print('caught type error')
```
- A: `caught type error`
- B: Raises unhandled `TypeError`
- C: Raises unhandled `ValueError`
- D: No output, no exception

B

**Q5.** What is the output?
```python
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, data)))
print(result)
```
- A: `[1, 4, 9, 16, 25]`
- B: `[1, 9, 25]`
- C: `[2, 4]`
- D: `[4, 16]`

B

**Q6.** What is the output?
```python
class Counter:
    _count = 0
    def __init__(self):
        Counter._count += 1
    @classmethod
    def get_count(cls):
        return cls._count

a = Counter()
b = Counter()
c = Counter()
print(Counter.get_count())
```
- A: `0`
- B: `1`
- C: `2`
- D: `3`

D

**Q7.** What is the output?
```python
x = [1, 2, 3]
y = x
y += [4]
print(x)
print(y is x)
```
- A: `[1, 2, 3]` / `True`
- B: `[1, 2, 3, 4]` / `True`
- C: `[1, 2, 3]` / `False`
- D: `[1, 2, 3, 4]` / `False`

B


**Q8.** What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(sum(g))
```
- A: `1` / `5`
- B: `1` / `6`
- C: `1` / `2`
- D: Raises `StopIteration`

A


**Q9.** Which TWO are True?
```python
import sys
```
- A: `sys.path` is a `list`
- B: `sys.modules` is a `list`
- C: All items in `sys.argv` are strings
- D: `sys.argv[0]` is always the script name

A, D

**Q10.** What is the output?
```python
class Base:
    __secret = 42
    def reveal(self):
        return self.__secret

class Child(Base):
    __secret = 99

obj = Child()
print(obj.reveal())
```
- A: `99`
- B: `42`
- C: Raises `AttributeError`
- D: `None`

B


Write answers here:
```
Q1: B
Q2: B
Q3: B,D
Q4: B
Q5: B
Q6: D
Q7: B
Q8: A
Q9: A, D
Q10: B
```

---

## Task 6 — Output prediction chains

**A)** Predict every line printed:
```python
class Animal:
    sound = 'generic'
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says {self.sound}'

class Dog(Animal):
    sound = 'woof'

class Cat(Animal):
    def speak(self):
        return f'{self.name} meows'

animals = [Dog('Rex'), Cat('Mimi'), Animal('Thing')]
for a in animals:
    print(a.speak())
```

**B)** Predict every line printed:
```python
def process(items, fn=lambda x: x):
    return [fn(item) for item in items]

nums = [3, -1, 4, -1, 5]
print(process(nums))
print(process(nums, abs))
print(process(nums, lambda x: x * 2 if x > 0 else 0))
```

**C)** Predict the output — generator + next:
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

g = countdown(5)
print(next(g))
print(next(g))
for x in g:
    print(x)
print('done')
```

Write answers here:
```
A) outputs:
#Rex says woof, Mimi meows, 'Thing says generic

B) 3 outputs:
print(process(nums)) #[3, -1, 4, -1, 5]
print(process(nums, abs)) #[3, 1, 4, 1, 5]
print(process(nums, lambda x: x * 2 if x > 0 else 0)) #[6, 0, 8, 0, 10]

C) outputs:
5, 4, 3, 2, 1, done (all in separate lines)

```

---

## Task 7 — Single-answer discipline: 7 questions, one letter each

**Q1.** What does `type(sys.modules)` return?
- A: `<class 'list'>`
- B: `<class 'dict'>`
- C: `<class 'set'>`
- D: `<class 'tuple'>`

B

**Q2.** Which mode opens for reading AND writing, no truncate, raises `FileNotFoundError` if missing?
- A: `'w+'`
- B: `'a+'`
- C: `'r+'`
- D: `'x'`

C


**Q3.** What does `'python'.rfind('o')` return?
- A: `-1`
- B: `4`
- C: `1`
- D: Raises `ValueError`

B


**Q4.** Which expression is a SyntaxError?
- A: `lambda x: x if x > 0 else -x`
- B: `lambda: None`
- C: `lambda x: return x`
- D: `lambda x, y=0: x + y`

C


**Q5.** `hasattr(Child, 'method')` where `method` defined only in `Parent`, `class Child(Parent)`:
- A: `False` — only `Child.__dict__` is checked
- B: `True` — MRO chain is searched
- C: Raises `AttributeError`
- D: Depends on whether `Child` overrides `__init__`

B

**Q6.** Given `f = lambda: None`, what is `bool(f())`?
- A: `True`
- B: `None`
- C: `False`
- D: Raises `TypeError`

A

**Q7.** What is the output?
```python
m = 0
def foo():
    global m
    try:
        m = 1 / 0
    except ZeroDivisionError:
        m = 99
    finally:
        m += 1
foo()
print(m)
```
- A: `0`
- B: `1`
- C: `99`
- D: `100`

D

Write answers here:
```
Q1: B
Q2: C
Q3: B
Q4: C
Q5: B
Q6: A
Q7: D
```

---

## Task 8 — Project: Verify R multiple and Avg R are correct

The exit_reason bug is fixed. Now verify the **R multiple calculation** is producing sensible numbers.

**The formula in `trade.py`:**
```python
r_multiple = pnl / (abs(entry_price - stop_loss) * quantity)
```
This means: how many times your risk did you make/lose.
- A 1R trade = you made exactly what you risked
- A -1R trade = you lost your full risk amount
- Win at TP should be positive R, loss at SL should be exactly -1R

**Your task:**
1. Run `main.py`
2. From the printed trade list, pick **3 trades** — one SL hit, one TP hit, one forced close
3. For each, manually verify the R multiple makes sense:
   - SL trade: `pnl / (abs(entry - sl) * qty)` should be close to `-1.0`
   - TP trade: should be positive (e.g. `+1.5R`, `+2R` etc.)
   - Forced close: R could be anything
4. Check the `Avg R` in the strategy report — does it match the ballpark of the individual trades?
5. Note: if `strategy_report()` crashes with a `TypeError`, that means a trade has `r_multiple = None`. Report if this happens.

```
Trade 1 (SL hit):
  entry:         sl:        pnl:       qty:
  Expected R:   Reported R:    Match? Y/N

Trade 2 (TP hit):
  entry:        tp:        pnl:       qty:
  Expected R:   Reported R:    Match? Y/N

Trade 3 (forced close):
  entry:        exit:      pnl:       qty:
  Reported R:

Strategy report Avg R (both strategies):

Any TypeError / None crash? Y/N: No

Instead I will paste you some trades, as I've added R, TP/SL + R:R ratio to each trade object, and everything here seems to be fine for now.
As I averaged the trades they also seem to work well.

[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 3632095d-08fc-43d2-83be-bc8547329d58: [WIN] BUY 1 FDAX: 24550.0 -> 24588.0 (buy tp hit) | P&L: $38.00, SL: 24535.166666666668, TP: 24584.0, R: 2.56, R:R Ratio: 2.2921348314608614
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade a93ef0bb-0fa8-4b30-acdf-54583542ab99: [WIN] BUY 1 FDAX: 24564.0 -> 24588.0 (buy tp hit) | P&L: $24.00, SL: 24526.0, TP: 24584.0, R: 0.63, R:R Ratio: 0.5263157894736842
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 491772ed-cb5f-46b9-bf8f-df24cd36ed41: [LOSS] BUY 1 FDAX: 25068.0 -> 25037.0 (buy sl hit) | P&L: $-31.00, SL: 25042.666666666668, TP: 25120.0, R: -1.22, R:R Ratio: 2.0526315789474667
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade 03c217dc-a7bb-456d-84cb-f2e04677afa4: [LOSS] BUY 1 FDAX: 25091.0 -> 25028.0 (buy sl hit) | P&L: $-63.00, SL: 25033.0, TP: 25120.0, R: -1.09, R:R Ratio: 0.5
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade c0fdf279-ce92-4188-aafc-76e9bee74690: [WIN] BUY 1 FDAX: 25182.0 -> 25221.0 (buy tp hit) | P&L: $39.00, SL: 25162.416666666668, TP: 25213.5, R: 1.99, R:R Ratio: 1.608510638297972
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade f39afdb9-909c-40fb-8b7a-fbb6554b1df8: [WIN] BUY 1 FDAX: 25198.0 -> 25221.0 (buy tp hit) | P&L: $23.00, SL: 25156.5, TP: 25213.5, R: 0.55, R:R Ratio: 0.37349397590361444
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 6d0e4d45-a476-4d6d-95cc-d00bcca2d1ba: [WIN] BUY 1 FDAX: 25298.0 -> 25331.0 (buy tp hit) | P&L: $33.00, SL: 25283.5, TP: 25326.0, R: 2.28, R:R Ratio: 1.9310344827586208
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade 536e289e-f921-4678-94ee-2af3f4bbaee7: [WIN] BUY 1 FDAX: 25308.0 -> 25331.0 (buy tp hit) | P&L: $23.00, SL: 25277.0, TP: 25326.0, R: 0.74, R:R Ratio: 0.5806451612903226
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 89021ed7-7901-4976-be11-f45e9e0e00ae: [WIN] BUY 1 FDAX: 25437.0 -> 25481.0 (buy tp hit) | P&L: $44.00, SL: 25417.333333333332, TP: 25480.0, R: 2.24, R:R Ratio: 2.186440677965967
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade 3216ba39-18b5-4ba2-b570-2f75714b6fdc: [WIN] BUY 1 FDAX: 25451.0 -> 25481.0 (buy tp hit) | P&L: $30.00, SL: 25406.0, TP: 25480.0, R: 0.67, R:R Ratio: 0.6444444444444445
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade f6f0fd23-9b09-4ea5-993b-f0cc5fd9654a: [WIN] BUY 1 FDAX: 25605.0 -> 25615.0 (buy tp hit) | P&L: $10.00, SL: 25555.0, TP: 25615.0, R: 0.2, R:R Ratio: 0.2
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 59473185-a240-477e-8ce8-0cb078aed57c: [WIN] BUY 1 FDAX: 25605.0 -> 25615.0 (buy tp hit) | P&L: $10.00, SL: 25560.833333333332, TP: 25615.0, R: 0.23, R:R Ratio: 0.22641509433961643
[@LPP Strategy | 1435c00d-d8df-40cc-93ba-cf48e4295385] Trade 944b1799-3317-4fef-afd8-c651511cbb0e: [LOSS] BUY 1 FDAX: 25459.0 -> 25431.0 (buy sl hit) | P&L: $-28.00, SL: 25431.166666666668, TP: 25508.0, R: -1.01, R:R Ratio: 1.7604790419162444
[@LPP Strategy | 552524db-4acd-40cd-bb62-ef23115dda35] Trade ea0beb09-8705-41f9-b7d2-6a2c1fb4aad4: [WIN] BUY 1 FDAX: 25480.0 -> 25494.0 (forced close) | P&L: $14.00, SL: 25421.0, TP: 25508.0, R: 0.24, R:R Ratio: 0.4745762711864407

```

---

**When done:** notify me for assessment.
