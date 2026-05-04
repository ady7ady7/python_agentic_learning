# PCAP Mock 1 — Gap Closure Reference

Gaps identified from first full Edube mock test. Each section has the rule, the trap, and a concrete example.

---

## 1. Multiple `except` branches — at most ONE executes

**Rule:** Python tries each `except` clause top to bottom. The first one that matches runs. All remaining `except` clauses are skipped entirely — even if they would also match.

```python
try:
    raise ValueError("v")
except ValueError:
    print("first")     # ← this matches first
except Exception:
    print("second")    # ← never reached

# Output: first
```

```python
try:
    raise ValueError("v")
except Exception:
    print("Exception")     # ← Exception is parent of ValueError → matches first
except ValueError:
    print("ValueError")    # ← never reached (unreachable code)

# Output: Exception
```

**Answer to the PCAP question:** "not more than one except block will be executed" — exactly one or zero, never more.

**PCAP trap:** Putting a parent class before a child class makes the child unreachable. Python does NOT raise a `SyntaxError` for this (unlike bare `except` — see section 8). The code runs silently with the wrong handler.

---

## 2. Bare `except` must be last — SyntaxError otherwise

**Rule:** A bare `except:` (no exception type) is a catch-all. Python requires it to be the **last** except clause. Putting it before any typed clause is a `SyntaxError`.

```python
# SyntaxError — bare except before typed clauses
try:
    raise ValueError
except:           # ← SyntaxError here
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
```

```python
# Valid — bare except last
try:
    raise ValueError
except ValueError:
    print("value")
except TypeError:
    print("type")
except:
    print("anything else")   # ← fine, it's last
```

**Why:** A bare `except` matches everything, so any typed clause after it would be unreachable. Python enforces this at parse time as a `SyntaxError` — it doesn't even try to run the code.

**Contrast with section 1:** Putting `Exception` before `ValueError` is legal syntax (just unreachable). Putting bare `except:` before any typed clause is a `SyntaxError`. The difference: bare vs typed.

---

## 3. File objects are iterable — `for line in open(...)`

**Rule:** `open()` returns a file object. File objects implement `__iter__` and `__next__`, making them directly iterable. Each iteration yields one line including the trailing `\n`.

```python
# Valid — file object is iterable
for line in open('file.txt', 'rt'):
    print(line)         # each line includes \n

# Equivalent — explicit readline loop
f = open('file.txt', 'rt')
for line in f:
    print(line.strip()) # strip() removes the \n
f.close()
```

**What each iteration yields:**
```
File contents:       What you get per iteration:
"hello\nworld\n"  → "hello\n", "world\n"
```

**PCAP options decoded:**
- "invalid because open returns nothing" — Wrong. `open()` returns a file object.
- "valid because open returns an iterable object" — **Correct.**
- "reads character by character" — Wrong. Iteration yields full lines.
- "reads the whole file at once" — Wrong. That's what `f.read()` does.

**Memory note:** Iterating a file object reads one line at a time — memory efficient for large files. `readlines()` loads everything into a list first.

---

## 4. `random` module — `randint` vs `randrange` vs `choice`

Three functions, three distinct behaviours. The PCAP tests whether you know what each *can and cannot* produce.

### `random.randint(a, b)` — integer, both ends **inclusive**
```python
import random
random.randint(0, 100)   # can return 0, 1, 2, ... 99, 100
random.randint(1, 6)     # simulates a die: 1 through 6 inclusive
```

### `random.randrange(start, stop, step)` — like `range()`, stop **excluded**
```python
random.randrange(10, 100, 3)
# Produces values: 10, 13, 16, 19, ... 97  (never 100)
# 82 is valid: 10 + 24*3 = 82 ✓
```

### `random.choice(sequence)` — picks ONE element from the sequence
```python
random.choice((0, 100, 3))
# Can ONLY return: 0, 100, or 3
# Cannot return 6, 7, 82, or any other value
```

**The mock question — target output: `6 82 0`**

| Variable | Target value | Which function |
|---|---|---|
| `a` | `6` | `randint(0, 100)` — 6 is in [0, 100] ✓ |
| `b` | `82` | `randrange(10, 100, 3)` — 82 = 10+24×3 ✓ |
| `c` | `0` | `choice((0, 100, 3))` — 0 is in the tuple ✓ |

**Why option D was wrong:**
```python
# D had:
a = random.choice((0, 100, 3))   # can only return 0, 100, or 3 — NEVER 6
```
`a=6` is impossible with `choice((0, 100, 3))`. The tuple has only three possible outputs.

**Why option C is correct:**
```python
import random
a = random.randint(0, 100)          # 6 is possible ✓
b = random.randrange(10, 100, 3)    # 82 is possible ✓
c = random.choice((0, 100, 3))      # 0 is possible ✓
```

---

## 5. String escape sequences and `SyntaxError`

**Rule:** In a string, `\\` is one backslash. `\'` is a literal quote. But the parser reads left to right — if `\'` appears in a single-quoted string, Python interprets it as an escaped quote (closing the string early or extending it), not as the end of the string.

```python
x = '\\' + "'"     # two separate strings — valid, x = "\'"
x = '\\'            # one backslash, string closed by final ' — valid
x = '\\\''          # SyntaxError — explained below
```

**Trace of `'\\\''`:**
```
'           ← open string
\\          ← escape sequence: one literal backslash \
\'          ← escape sequence: one literal quote '
'           ← closes the string
Result: '   (one char: a single quote)   len = 1
```

`'\\\''` is **valid**. The final `'` closes the string after the `\'` escape pair.

**Contrast with `"\\'"` (double-quoted):**
```python
x = "\\'"   # \\ = backslash, ' = plain quote (no escaping needed in double-quoted string)
print(x)    # \'
print(len(x))  # 2
```

---

## 6. `chr()` and `ord()` — character ↔ integer

**`ord(char)`** → integer Unicode code point of the character.
**`chr(n)`** → character whose Unicode code point is `n`.

```python
print(ord('a'))    # 97
print(ord('p'))    # 112
print(ord('A'))    # 65
print(ord('0'))    # 48  ← digit zero, not integer zero

print(chr(97))     # 'a'
print(chr(112))    # 'p'
print(chr(114))    # 'r'   (112 + 2 = 114)
print(chr(65))     # 'A'
```

**The mock question:** `chr(ord('p') + 2)`
```
ord('p') = 112
112 + 2  = 114
chr(114) = 'r'
```

**Useful pattern — iterate over alphabet:**
```python
for i in range(26):
    print(chr(ord('a') + i), end=' ')
# a b c d e f g h i j k l m n o p q r s t u v w x y z
```

---

## 7. `sys.stderr` — where it goes by default

**Three standard streams:**

| Stream | Default destination | Used by |
|---|---|---|
| `sys.stdin` | keyboard | `input()` |
| `sys.stdout` | screen (terminal) | `print()` |
| `sys.stderr` | screen (terminal) | error messages, tracebacks |

**The PCAP trap:** stderr goes to the screen, NOT to a null device or a file. It's a separate stream from stdout, but both appear on the terminal by default.

```python
import sys

print("normal output")           # → stdout → screen
sys.stdout.write("also stdout\n")  # → screen
sys.stderr.write("error msg\n")    # → screen (separate stream, same destination by default)
```

**Why two separate streams going to the same place?** So you can redirect them independently:
```bash
python script.py > output.txt        # stdout to file, stderr still on screen
python script.py 2> errors.txt       # stderr to file, stdout still on screen
python script.py > out.txt 2>&1      # both to file
```

---

## 8. `hasattr()` — class attributes vs instance attributes

**Rule:** Instance attributes set in `__init__` do NOT exist on the class itself. They only exist on instances created from that class. `hasattr(ClassName, 'attr')` checks the class, not any instance.

```python
class A:
    A = 1           # class attribute — exists on A itself
    def __init__(self):
        self.a = 0  # instance attribute — only exists on instances of A

print(hasattr(A, 'A'))    # True  — A.A = 1 exists on the class
print(hasattr(A, 'a'))    # False — self.a only exists after __init__ runs on an instance

instance = A()
print(hasattr(instance, 'a'))   # True  — now self.a exists on this instance
print(hasattr(instance, 'A'))   # True  — instance also inherits class attributes
```

**The PCAP trap:** The question passes the *class* `A` to `hasattr`, not an instance. `self.a` is never set on the class — only on objects created by calling `A()`.

---

## 9. `__name__` — entry point vs imported module

**Rule:** Every Python file has a `__name__` variable. Its value depends on how the file is run.

| How the file is used | `__name__` value |
|---|---|
| Run directly: `python p.py` | `'__main__'` |
| Imported: `import p` | `'p'` (the module name) |
| Imported as alias: `import p as x` | still `'p'` |

```python
# p.py
print(__name__)

# Run directly:   python p.py   →  __main__
# Imported:       import p      →  p
```

**The standard guard:**
```python
if __name__ == '__main__':
    main()
```
This code runs only when the file is the entry point, not when imported as a library.

**PCAP options for `print(__name__)` in `p.py` run directly:**
- `__p.py__` — doesn't exist as a format
- `main` — wrong (no underscores)
- `__main__` — **correct**

---

## Quick-Reference Summary

| Topic | The rule | The trap |
|---|---|---|
| Multiple `except` | At most one runs — first match wins | Parent before child = child unreachable (no SyntaxError) |
| Bare `except` | Must be last | Bare `except` before typed clause = SyntaxError |
| `for line in open(...)` | File objects are iterable, yields lines with `\n` | Not character-by-character |
| `randint(a, b)` | Both ends inclusive | `randint(1,6)` can return 6 |
| `randrange(a, b, s)` | Stop excluded, follows `range()` | `randrange(1,7)` = 1–6 |
| `choice(seq)` | Picks one element from the sequence | Can only return what's in the sequence |
| `'\\\''` | Valid — prints `'`, len=1 | `\\`=backslash, `\'`=quote, final `'` closes the string |
| `chr(ord('p') + 2)` | `ord('p')` = 112, +2 = 114, `chr(114)` = `'r'` | Know ord values: `'a'`=97, `'A'`=65, `'0'`=48 |
| `sys.stderr` | Goes to screen by default | Not null device, not keyboard |
| `hasattr(Class, 'attr')` | Checks the class object, not instances | Instance attrs from `__init__` don't exist on the class |
| `__name__` | `'__main__'` when run directly, module name when imported | Options with wrong format are distractors |
