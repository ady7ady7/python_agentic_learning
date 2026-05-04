# MRO & `super()` — How the Chain Actually Works

---

## The key insight you're missing

`super()` does NOT mean "call my parent class."
`super()` means **"call the next class in the MRO of the actual object being used."**

The MRO is computed once for the actual object (`D`). Every `super()` call in the entire chain uses **that same MRO list**.

---

## Trace it step by step

```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return super().method() + "B"

class C(A):
    def method(self): return super().method() + "C"

class D(B, C):
    pass
```

MRO of D: `[D, B, C, A]`

---

**Step 1:** `D().method()` — D has no `method`, next in MRO is **B**.

**Step 2:** `B.method()` runs. It calls `super().method()`.
- We're inside B, so `super()` = next after B in D's MRO = **C**
- B cannot return yet — it's waiting for `super().method()` to come back.

**Step 3:** `C.method()` runs. It calls `super().method()`.
- We're inside C, so `super()` = next after C in D's MRO = **A**
- C cannot return yet — it's waiting.

**Step 4:** `A.method()` runs. Returns `"A"`. No super call.

**Step 5:** Stack unwinds back to C: `"A" + "C"` = `"AC"`. C returns.

**Step 6:** Stack unwinds back to B: `"AC" + "B"` = `"ACB"`. B returns.

---

## Why the intuitive model is wrong

You might expect B to complete fully before C runs:
```
B → "A" + "B" = "AB"    ← WRONG — B pauses, doesn't complete yet
C → "A" + "C" = "AC"    ← WRONG — these don't run independently
```

The reality: B **pauses in the middle**, hands off to C, C **pauses**, hands off to A. Then the whole stack unwinds in reverse:

```
A returns "A"
C resumes:  "A" + "C" = "AC"
B resumes:  "AC" + "B" = "ACB"
```

Think of it like nested function calls:
```python
# What's actually happening:
B_result = C_result + "B"        # B is waiting
C_result = A_result + "C"        # C is waiting
A_result = "A"                   # A returns first

# Unwind:
C_result = "A" + "C" = "AC"
B_result = "AC" + "B" = "ACB"
```

---

## The mental model that works

**Don't think of MRO as execution order. Think of it as a queue.**

Every `super()` call pops the next item off the queue. The returns happen in **reverse** — last called, first to return.

```
Call order:   D → B → C → A
Return order: A → C → B → D

String builds from the inside out:
A returns "A"
C wraps it: "A" + "C"
B wraps it: "AC" + "B"
Result: "ACB"
```

---

## Quick rule for exam questions

When you see `super().method() + "X"` — the `"X"` is appended **on the way back up**.
So the string reads in **reverse MRO order** (excluding D): A first, then C, then B = `"ACB"`.

If it were `"X" + super().method()` instead, B prepends before handing off:
```
B runs first:  "B" + (waiting...)
C runs next:   "C" + (waiting...)
A returns:     "A"
C finishes:    "C" + "A" = "CA"
B finishes:    "B" + "CA" = "BCA"
Result: "BCA"
```

---

## Additional Examples

---

### Example 1 — Three-level linear chain

```python
class A:
    def greet(self): return "Hello"

class B(A):
    def greet(self): return super().greet() + " World"

class C(B):
    def greet(self): return super().greet() + "!"

print(C().greet())
```

MRO of C: `[C, B, A]`

```
Call order:   C → B → A
A returns:    "Hello"
B resumes:    "Hello" + " World" = "Hello World"
C resumes:    "Hello World" + "!" = "Hello World!"

Output: Hello World!
```

---

### Example 2 — `__init__` chain (most common real use)

```python
class A:
    def __init__(self):
        print("A init")
        self.a = 1

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
        self.b = 2

class C(A):
    def __init__(self):
        super().__init__()
        print("C init")
        self.c = 3

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")

D()

```

MRO of D: `[D, B, C, A]`

```
D.__init__ calls super() → B
B.__init__ calls super() → C      (NOT A — that's the whole point)
C.__init__ calls super() → A
A.__init__ runs, prints "A init"
C resumes, prints "C init"
B resumes, prints "B init"
D resumes, prints "D init"

Output:
A init
C init
B init
D init

#A init, a = 1, C init, c = 3, B init, b = 2, D init
```

A runs once. Without cooperative MRO, A would run twice (once via B, once via C). `super()` prevents the diamond duplication.

---

### Example 3 — prepend vs append changes the output

```python
class A:
    def tag(self): return "A"

class B(A):
    def tag(self): return "B-" + super().tag()   # prepend

class C(A):
    def tag(self): return "C-" + super().tag()   # prepend

class D(B, C):
    pass

print(D().tag())
```

MRO: `[D, B, C, A]`

```
B runs:   "B-" + (waiting...)
C runs:   "C-" + (waiting...)
A runs:   "A"
C returns: "C-" + "A"  = "C-A"
B returns: "B-" + "C-A" = "B-C-A"

Output: B-C-A
```

Compare with `super().method() + "X"` (append):
- append → `"ACB"` (reverse MRO)
- prepend → `"B-C-A"` (forward MRO)

---

### Example 4 — what if one class doesn't call `super()`?

```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"      # no super() call — chain STOPS here

class C(A):
    def method(self): return super().method() + "C"

class D(B, C):
    pass

print(D().method())
```

MRO: `[D, B, C, A]`

```
D → B.method() runs
B returns "B" immediately — no super() call
C and A are never reached

Output: B
```

**Exam trap:** If any class in the chain omits `super()`, everything below it in the MRO is silently skipped. No error.

---

### Example 5 — PCAP-style multiple choice

```python
class A:
    def f(self): return "A"

class B(A):
    def f(self): return super().f() + "B"

class C(B):
    def f(self): return super().f() + "C"

class D(C):
    def f(self): return super().f() + "D"

print(D().f())
```

MRO: `[D, C, B, A]`

```
D calls super() → C
C calls super() → B
B calls super() → A
A returns "A"
B returns "A" + "B" = "AB"
C returns "AB" + "C" = "ABC"
D returns "ABC" + "D" = "ABCD"

Output: ABCD
```

Linear chain (no diamond) → result reads in MRO order, because each class appends after getting the result from everything below it.

---

## Summary Table

| Pattern | Call order | Return order | Result shape |
|---|---|---|---|
| `super().f() + "X"` (append) | MRO top→bottom | bottom→top | reversed MRO |
| `"X" + super().f()` (prepend) | MRO top→bottom | bottom→top | forward MRO |
| No `super()` in middle class | stops at that class | — | chain cut |
| Linear chain (no diamond) + append | MRO order | reverse | reads in MRO order |

---

## PCAP Trap Summary

1. `super()` follows the MRO of the **actual instantiated object**, not the class where `super()` is written.
2. In `D(B, C)`, `super()` inside B skips to C — not to A, even though `class B(A)` declares A as parent.
3. A class that doesn't call `super()` silently breaks the chain — no error raised.
4. String builds from the **innermost return outward** — A finishes first, then wraps up through the chain.
