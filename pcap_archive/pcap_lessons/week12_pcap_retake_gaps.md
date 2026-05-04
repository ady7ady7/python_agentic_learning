# Week 12 — PCAP Retake: Targeted Gap Closure

These are the exact traps that cost points on the real exam. Every section has the rule, the trap, and a drill.

---

## 1. `type(e)` vs the handler class — Q11

**The trap:** You caught the exception as `BaseException`, so you assumed `type(e)` would return `BaseException`. Wrong.

**The rule:** `type(e)` returns the **actual class of the object** — what it was when it was raised. The handler label never changes the object's identity.

```python
d = {'a': 1}
try:
    d['z']
except BaseException as error:
    print(type(error))        # <class 'KeyError'>  ← actual class
    print(type(error).__name__)  # KeyError
    print(isinstance(error, BaseException))  # True — it IS a BaseException
    print(isinstance(error, KeyError))       # True — it's also a KeyError
```

**Mental model:** Catching with `BaseException` is like putting any animal in a cage labelled "Animal". The animal is still a dog, not an "Animal". `type()` tells you what's in the cage, not what the cage is labelled.

**PCAP drill — what does this print?**
```python
try:
    raise FileNotFoundError("gone")
except OSError as e:
    print(type(e).__name__)
```
Answer: `FileNotFoundError` — not `OSError`, even though it was caught as one.

---

## 2. Name mangling + inheritance — Q24

**The trap:** `C` sets `__VarA = 3`, so `obj_c.get()` should return 3. Wrong.

**The rule:** Name mangling is resolved **at the class where the method is written**, not where the instance was created.

```python
class A:
    __x = 1          # stored as _A__x
    def get(self): return self.__x   # compiled as: return self._A__x

class B(A):
    __x = 2          # stored as _B__x
    def get(self): return self.__x   # compiled as: return self._B__x

class C(B):
    __x = 3          # stored as _C__x
    # NO get() defined here
```

`C` has no `get()`, so `obj_c.get()` resolves to `B.get()`. Inside `B.get()`, `self.__x` was compiled as `self._B__x` = **2**. Python doesn't re-mangle at runtime based on the instance's class.

```python
obj_c = C()
print(obj_c.get())       # 2 — B.get() runs, reads _B__x
print(obj_c._C__x)       # 3 — C's own mangled var, only accessible this way
print(obj_c._B__x)       # 2
print(obj_c._A__x)       # 1
```

**Rule to remember:** Private name mangling is a **compile-time** operation. The class that *defines* the method determines the mangling prefix — forever.

---

## 3. `__bases__`, `__dict__`, `__mro__` — Q29

These are guaranteed PCAP topics. Memorise all of them.

```python
class A:
    x = 10
    def __init__(self):
        self.y = 20

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

| Attribute | What it is | Example |
|---|---|---|
| `__bases__` | Tuple of **direct** parent classes | `D.__bases__` → `(B, C)` |
| `__mro__` | Tuple of full resolution order | `D.__mro__` → `(D, B, C, A, object)` |
| `__dict__` | Namespace dict of class or instance | `A.__dict__` has `'x'` but NOT `'y'` |
| `__name__` | String name of the class | `D.__name__` → `'D'` |
| `__module__` | Module where the class was defined | `D.__module__` → `'__main__'` |
| `__class__` | The class an instance belongs to | `d = D(); d.__class__` → `D` |

**Key traps:**
```python
print(D.__bases__)          # (B, C) — only direct parents, NOT A
print(len(D.__bases__))     # 2
print(A in D.__bases__)     # False — A is grandparent, not direct
print(A in D.__mro__)       # True — __mro__ includes full chain

a = A()
print('x' in A.__dict__)    # True  — class attribute
print('y' in A.__dict__)    # False — instance attribute, not on class
print('y' in a.__dict__)    # True  — instance attribute on the object
```

**PCAP question pattern:** "which expression evaluates to True?" — always check `__bases__` vs `__mro__` carefully. Direct vs full chain.

---

## 4. `open()` modes and defaults — Q35

**Default mode is `'r'`** — not `'w'`, not `'rb'`. Always read, always text.

| Mode | Meaning | File must exist? | Creates file? | Truncates? |
|---|---|---|---|---|
| `'r'` | read text (default) | YES — fails if missing | no | no |
| `'w'` | write text | no | YES | YES — wipes contents |
| `'a'` | append text | no | YES | no — adds to end |
| `'x'` | exclusive create | no | YES | fails if exists |
| `'r+'` | read + write | YES | no | no |
| `'rb'`, `'wb'` | binary modes | same rules | same | same |

**The Q35 trap:**
- A said default is `'w'` → **False**, default is `'r'`
- D said opening with `'w'` loses previous contents → **True**

```python
open('file.txt')          # same as open('file.txt', 'r')
open('file.txt', 'w')     # creates or TRUNCATES — all previous content gone
open('file.txt', 'a')     # creates or appends — safe for logging
```

---

## 5. Lambda — parameters and return value — Q34

**Two things PCAP tests that most people get wrong:**

**A) Lambdas CAN have zero parameters:**
```python
f = lambda: 42        # valid — no parameters
f()                   # 42

g = lambda: None      # valid — returns None explicitly
h = lambda: print("hi")  # valid — print() returns None, so h() returns None
```

**B) Lambdas CAN return None:**
```python
f = lambda x: print(x)   # print returns None → f(5) returns None
result = f(5)             # prints 5, result = None
print(result)             # None
```

**What lambdas CANNOT do:**
- Multiple statements
- `return` keyword
- `yield`
- Assignments (`x = 1`)
- `if/else` as statements (but ternary `x if cond else y` is fine)

**PCAP trap options — mark True or False:**
- "Cannot return None" → **False**
- "Cannot be defined without parameters" → **False**
- "Are called anonymous functions" → **True**
- "Can be defined without parameters" → **True**
- "Must contain the return keyword" → **False** — `return` is implicit

---

## 6. Lambda as function argument — reading Q36-style questions

**The pattern:**
```python
def foo(x, y, z):
    return x(y) - x(z)

print(foo(lambda x: x % 2, 2, 1))
```

**How to read it — 3 steps:**

Step 1: Name the function argument. Here `x` = `lambda x: x % 2`. Rename it mentally to avoid confusion with parameter `x` of the lambda:
```python
# x is a function: fn(n) = n % 2
# y = 2, z = 1
```

Step 2: Substitute:
```python
return fn(2) - fn(1)
return (2 % 2) - (1 % 2)
return 0 - 1
return -1
```

Step 3: Answer is **-1**.

**The trap:** The parameter name `x` is reused for both the function argument and the lambda parameter. They are completely separate scopes. Don't let reused names confuse you — rename one mentally.

**Practice drill:**
```python
def apply(fn, a, b):
    return fn(a) + fn(b)

print(apply(lambda x: x ** 2, 3, 4))  # what is this?
# fn(3) = 9, fn(4) = 16, result = 25
```

---

## 7. List comprehension order preservation — Q39

**The trap:** `range(4, 0, -1)` = 4, 3, 2, 1. The comprehension iterates in **that order**. Results appear in iteration order, not sorted order.

```python
my_list = [0, 1, 2, 3, 4]   # [i for i in range(5)]

m = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]
#    i=4: my_list[4]=4, 4%2==0 → skip
#    i=3: my_list[3]=3, 3%2!=0 → include 3
#    i=2: my_list[2]=2, 2%2==0 → skip
#    i=1: my_list[1]=1, 1%2!=0 → include 1
# Result: [3, 1]  ← in iteration order (descending), NOT sorted ascending
```

**The instinct that kills you:** You see `[1, 3]` and think "those are the odd values" — correct. But the question asks for the output, and the output is in the order they were appended — descending iteration = `[3, 1]`.

**Rule:** List comprehensions preserve iteration order. If you iterate backwards, the result is backwards. Always trace the loop order explicitly.

```python
# Ascending: range(0, 5) → [1, 3]
# Descending: range(4, 0, -1) → [3, 1]
```

---

## 8. `2.` float syntax and ternary — Q32

**Float literals can end with a dot:**
```python
x = 2.     # same as 2.0
y = 3.     # same as 3.0
z = 2. + 3.  # 5.0
```

This is valid Python. The PCAP uses it specifically to make you think there's a syntax error.

**Ternary operator:**
```python
result = value_if_true if condition else value_if_false
```

```python
x = 8 ** (1/3)    # 2.0
y = 2. if x < 2.3 else 3.   # 2.0 < 2.3 → True → y = 2.0
print(y)          # 2.0
```

**PCAP trap checklist when you see unusual syntax:**
- `2.` → valid float ✅
- `1_000_000` → valid int (underscores) ✅
- `0xFF` → valid hex int ✅
- `0o77` → valid octal ✅
- `0b1010` → valid binary ✅
- `j` suffix → complex number (`3+2j`) ✅

---

## 9. `platform` module — Q1

The `platform` module is lightly tested on PCAP. Know these four:

| Function | Returns |
|---|---|
| `platform.platform()` | Full platform string e.g. `'Windows-10-...'` |
| `platform.system()` | OS name: `'Windows'`, `'Linux'`, `'Darwin'` |
| `platform.processor()` | CPU identifier string |
| `platform.python_version()` | Python version string e.g. `'3.11.4'` |
| `platform.uname()` | Named tuple with system, node, release, version, machine, processor |

**Q1 answer:** "underlying platform name" → `platform.platform()`. `uname()` gives a full system info tuple, not just the platform name.

---

## 10. `raiseX` vs `raise X` — Q10

**Without a space, it's a name lookup, not a statement:**
```python
raise ValueError    # raises ValueError — statement
raiseValueError     # looks up variable named raiseValueError — NameError if undefined
```

This is not a SyntaxError — it looks syntactically valid as an expression statement. Python only discovers the problem at runtime when it tries to find `raiseValueError` in scope.

**In Q10:**
```python
assert m != 0          # m=0, AssertionError raised
try:
    return 1/n         # never reached
except ArithmeticError:
    raiseValueError    # NameError — variable doesn't exist
```

`AssertionError` is NOT an `ArithmeticError`, so the inner `except` doesn't catch it. It propagates to the outer `try`, caught by bare `except` → `m += 1` = 1.

---

## Quick-Reference: All New Gaps

| Topic | Rule | Trap |
|---|---|---|
| `type(e)` | Returns actual class, not handler class | Caught as `BaseException` ≠ type is `BaseException` |
| Name mangling + inheritance | Mangling resolved at method's defining class | `C` overrides `__x` but inherits `B.get()` which reads `_B__x` |
| `__bases__` | Direct parents only, as a tuple | Not the same as `__mro__` which is the full chain |
| `open()` default | Default mode is `'r'` | `'w'` truncates, `'a'` appends |
| Lambda params | Zero params is valid | "cannot be defined without parameters" is False |
| Lambda returns None | Lambdas can return None | "cannot return None" is False |
| Lambda as argument | Rename param mentally, substitute step by step | Reused parameter name `x` causes confusion |
| List comp order | Preserves iteration order | `range(4,0,-1)` → result is descending |
| `2.` float syntax | Valid Python, same as `2.0` | Looks like SyntaxError, isn't |
| `platform.platform()` | Returns platform name string | `uname()` returns tuple |
| `raiseX` no space | NameError at runtime | Looks like SyntaxError, but isn't |
