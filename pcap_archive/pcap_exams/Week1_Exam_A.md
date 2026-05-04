# Week 1 Mock PCAP Exam A

**Time Limit:** 65 minutes (simulates actual PCAP exam conditions)
**Total Questions:** 30
**Passing Score:** 70% (21/30 correct)

---

## Instructions

- Answer all 30 questions
- Each question has exactly ONE correct answer
- No partial credit
- Mark your answers clearly (A/B/C/D)
- Review your answers before checking the answer key at the end

#Start 9:10
---

## Section 1: Modules & Packages (Questions 1-6)

### Question 1
What is the output of the following code?

```python
import math
print(type(math))
```

A) `<class 'module'>`
B) `<class 'package'>`
C) `<class 'library'>`
D) `<class 'object'>`

**Your answer:** A

---

### Question 2
Which import statement will cause a `SyntaxError`?

A) `from math import *`
B) `import math as m`
C) `from math import sqrt, pow`
D) `import math.sqrt`

**Your answer:** D

---

### Question 3
What is the output?

```python
import sys
print(len(sys.path) > 0)
```

A) `True`
B) `False`
C) `1`
D) `TypeError`

**Your answer:** A

---

### Question 4
Which statement about `__init__.py` is TRUE?

A) It must contain code to run when the package is imported
B) It marks a directory as a Python package
C) It is required in Python 3.3+ for all packages
D) It automatically imports all modules in the package

**Your answer:** Honestly, I don't know.

---

### Question 5
What happens when you import a module for the second time in the same program?

A) Python re-executes all code in the module
B) Python raises an `ImportError`
C) Python uses the cached version from `sys.modules`
D) Python creates a new copy of the module

**Your answer:** D

---

### Question 6
What is the output?

```python
from math import pi as p
from math import pi
print(pi == p)
```

A) `True`
B) `False`
C) `NameError`
D) `ImportError`

**Your answer:**  A

---

## Section 2: Strings (Questions 7-12)

### Question 7
What is the output?

```python
s = "Python"
print(s[10:20])
```

A) `""`
B) `"Python"`
C) `IndexError`
D) `None`

**Your answer:** A

---

### Question 8
What is the output?

```python
s = "  PCAP  "
print(s.strip().lower())
```

A) `"  pcap  "`
B) `"pcap"`
C) `"  PCAP  "`
D) `"PCAP"`

**Your answer:** B

---

### Question 9
What is the result of `"hello".find("x")`?

A) `-1`
B) `0`
C) `ValueError`
D) `None`

**Your answer:** A

---

### Question 10
What is the output?

```python
s = "abc"
s[0] = "z"
print(s)
```

A) `"zbc"`
B) `"abc"`
C) `TypeError`
D) `IndexError`

**Your answer:** A

---

### Question 11
What is the output?

```python
print("PCAP".replace("P", "X", 1))
```

A) `"XCAP"`
B) `"XCAX"`
C) `"PCAP"`
D) `"XXAP"`

**Your answer:** A

---

### Question 12
What does `"test".index("x")` return?

A) `-1`
B) `None`
C) `ValueError`
D) `0`

**Your answer:** C

---

## Section 3: Exceptions (Questions 13-18)

### Question 13
What is the output?

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("A")
except Exception:
    print("B")
finally:
    print("C")
```

A) `A C`
B) `B C`
C) `C`
D) `A B C`

**Your answer:** A

---

### Question 14
Which exception order is CORRECT?

A)
```python
try:
    pass
except Exception:
    pass
except ValueError:
    pass
```

B)
```python
try:
    pass
except ValueError:
    pass
except Exception:
    pass
```

C)
```python
try:
    pass
except:
    pass
except Exception:
    pass
```

D) Both A and B are correct

**Your answer:** B

---

### Question 15
What is the output?

```python
try:
    print("A")
    raise ValueError()
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D")
```

A) `A B C D`
B) `A B D`
C) `A C D`
D) `A D`

**Your answer:** B (manually raising ValueError will result in printing B and prevent C from showing up)

---

### Question 16
What happens if no exception occurs in a `try` block that has an `else` clause?

A) The `else` block executes
B) The `else` block is skipped
C) A `SyntaxError` occurs
D) The `finally` block runs instead

**Your answer:** A

---

### Question 17
What is the output?

```python
try:
    x = int("abc")
except:
    print("Error")
print("Done")
```

A) `Error Done`
B) `Error`
C) `Done`
D) `ValueError`

**Your answer:**  A

---

### Question 18
Which exception is raised when you try to access a dictionary key that doesn't exist?

A) `ValueError`
B) `KeyError`
C) `IndexError`
D) `AttributeError`

**Your answer:** B

---

## Section 4: OOP Fundamentals (Questions 19-24)

### Question 19
What is the output?

```python
class Dog:
    species = "Canis"

d1 = Dog()
d2 = Dog()
d1.species = "Lupus"
print(d2.species)
```

A) `"Canis"`
B) `"Lupus"`
C) `AttributeError`
D) `NameError`

**Your answer:** B

---

### Question 20
What does `self` represent in a class method?

A) The class itself
B) The instance of the class
C) A keyword like `this` in Java
D) A global variable

**Your answer:** B

---

### Question 21
What is the output?

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print(c.count)
```

A) `0`
B) `1`
C) `2`
D) `AttributeError`

**Your answer:** C

---

### Question 22
What can `__init__` return?

A) `None` (implicitly)
B) `self`
C) Any value
D) An integer

**Your answer:** A

---

### Question 23
What is the output?

```python
class Test:
    items = []

t1 = Test()
t2 = Test()
t1.items.append(1)
print(len(t2.items))
```

A) `0`
B) `1`
C) `2`
D) `AttributeError`

**Your answer:** B

---

### Question 24
What is the difference between a method and a function?

A) Methods are defined inside classes, functions are not
B) Methods don't take parameters
C) Functions can't return values
D) There is no difference

**Your answer:** A

---

## Section 5: Magic Methods & Pandas (Questions 25-30)

### Question 25
What is the output?

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return None

b = Book("PCAP")
print(b)
```

A) `None`
B) `Book("PCAP")`
C) `TypeError`
D) `<__main__.Book object at 0x...>`

**Your answer:** A

---

### Question 26
When is `__repr__` called?

A) When you print an object and `__str__` is not defined
B) Only when you explicitly call `repr()`
C) Never, it's deprecated
D) When you create an instance

**Your answer:** A

---

### Question 27
What is the output?

```python
import pandas as pd
s = pd.Series([True, False, True])
print(s.sum())
```

A) `3`
B) `2`
C) `True`
D) `TypeError`

**Your answer:** B

---

### Question 28
What is the correct way to filter a DataFrame for rows where `price > 100`?

A) `df[df['price'] > 100]`
B) `df.filter(price > 100)`
C) `df.where(df['price'] > 100)`
D) `df['price' > 100]`

**Your answer:** A

---

### Question 29
What is the output?

```python
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3]})
print(df.isna().sum())
```

A) `0`
B) `3`
C) `a    0\ndtype: int64`
D) `False`

**Your answer:** C

---

### Question 30
What operator do you use for multiple conditions in Pandas filtering?

```python
df[(df['price'] > 100) ??? (df['volume'] > 1000)]
```

A) `and`
B) `&&`
C) `&`
D) `|`

**Your answer:** C


#FINISH 9:22

---

## Answer Key

**STOP! Don't look at the answers until you've completed all questions.**

<details>
<summary>Click to reveal answers</summary>

### Section 1: Modules & Packages
1. A - `<class 'module'>`
2. D - `import math.sqrt` (can't import attributes directly)
3. A - `True` (sys.path is never empty)
4. B - It marks a directory as a Python package
5. C - Python uses the cached version from sys.modules
6. A - `True` (both reference the same value)

### Section 2: Strings
7. A - `""` (slicing never raises IndexError)
8. B - `"pcap"` (strip removes whitespace, lower converts to lowercase)
9. A - `-1` (find returns -1 when substring not found)
10. C - `TypeError` (strings are immutable)
11. A - `"XCAP"` (replaces first occurrence only)
12. C - `ValueError` (index raises exception when not found)

### Section 3: Exceptions
13. A - `A C` (ZeroDivisionError caught, finally always runs)
14. B - Specific exceptions must come before general ones
15. B - `A B D` (else doesn't run when exception occurs)
16. A - The else block executes (runs when no exception)
17. A - `Error Done` (exception caught, execution continues)
18. B - `KeyError`

### Section 4: OOP Fundamentals
19. A - `"Canis"` (d1.species creates instance attribute, d2 still uses class attribute)
20. B - The instance of the class
21. C - `2` (count incremented twice)
22. A - `None` (implicitly, or TypeError if you try to return something else)
23. B - `1` (mutable class attribute shared between instances)
24. A - Methods are defined inside classes

### Section 5: Magic Methods & Pandas
25. C - `TypeError` (__str__ must return string)
26. A - When you print and __str__ is not defined (also when repr() called explicitly)
27. B - `2` (True counts as 1, False as 0)
28. A - `df[df['price'] > 100]`
29. C - `a    0\ndtype: int64` (returns Series with column names)
30. C - `&` (use & for AND, | for OR in Pandas)

### Scoring Guide
- **27-30 correct (90-100%):** Excellent! Ready for Week 2
- **21-26 correct (70-86%):** Good! Review weak areas
- **15-20 correct (50-66%):** Review Week 1 lessons
- **Below 15 (< 50%):** Revisit Week 1 material thoroughly

</details>

---

## Performance Tracking

**Your Score:** ___/30 (___%)

**Topics to Review:**
- [ ] Modules & Packages
- [ ] Strings
- [ ] Exceptions
- [ ] OOP Fundamentals
- [ ] Magic Methods & Pandas

**Notes:**
