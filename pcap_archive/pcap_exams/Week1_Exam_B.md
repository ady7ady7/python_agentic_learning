# Week 1 Mock PCAP Exam B

**Time Limit:** 65 minutes (simulates actual PCAP exam conditions)
**Total Questions:** 30
**Passing Score:** 70% (21/30 correct)

---

## Instructions

- Answer all 30 questions
- Each question has exactly ONE correct answer
- No partial credit
- Mark your answers clearly (A/B/C/D)
- This exam covers the same Week 1 topics as Exam A but with different questions

---
#Start 12:52

## Section 1: Modules & Packages (Questions 1-6)

### Question 1
What is the output?

```python
import math as m
print(m.pi == math.pi)
```

A) `True`
B) `False`
C) `NameError`
D) `ImportError`

**Your answer:** B

---

### Question 2
Which statement is TRUE about the `import` statement?

A) It always executes all code in the imported module
B) It can only be used at the beginning of a file
C) It can be used inside functions
D) It requires the module to be in the current directory

**Your answer:** C

---

### Question 3
What is the output?

```python
from math import sqrt
print(sqrt(16))
```

A) `4`
B) `4.0`
C) `16`
D) `NameError`

**Your answer:** B

---

### Question 4
Which of the following imports ALL functions from the math module?

A) `from math import all`
B) `import math.*`
C) `from math import *`
D) `import * from math`

**Your answer:** c

---

### Question 5
What is stored in `sys.modules`?

A) A list of all available Python modules
B) A dictionary of already imported modules
C) The current working directory
D) Module source code

**Your answer:** A

---

### Question 6
What happens if you try to import a module that doesn't exist?

A) `ImportError` or `ModuleNotFoundError`
B) `SyntaxError`
C) Python creates an empty module
D) `ValueError`

**Your answer:** A

---

## Section 2: Strings (Questions 7-12)

### Question 7
What is the output?

```python
s = "hello"
print(s[-1])
```

A) `"o"`
B) `"h"`
C) `IndexError`
D) `""`

**Your answer:** A

---

### Question 8
What is the output?

```python
s = "a,b,c"
print(s.split(","))
```

A) `"a" "b" "c"`
B) `['a', 'b', 'c']`
C) `('a', 'b', 'c')`
D) `"abc"`

**Your answer:** D

---

### Question 9
What is the output?

```python
print("Python"[2:4])
```

A) `"th"`
B) `"tho"`
C) `"yt"`
D) `"yth"`

**Your answer:** A

---

### Question 10
Which method returns a NEW string?

A) All string methods return new strings
B) Only `.upper()` and `.lower()`
C) Only `.replace()`
D) None, strings are mutable

**Your answer:**  C

---

### Question 11
What is the output?

```python
s = "  test  "
print(len(s.strip()))
```

A) `4`
B) `8`
C) `6`
D) `10`

**Your answer:** A

---

### Question 12
What does `"PCAP".count("P")` return?

A) `1`
B) `2`
C) `0`
D) `True`

**Your answer:** B

---

## Section 3: Exceptions (Questions 13-18)

### Question 13
What is the output?

```python
try:
    print("A")
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D")
```

A) `A C D`
B) `A B D`
C) `A D`
D) `A B C D`

**Your answer:** A

---

### Question 14
What is the output?

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

A) `Error`
B) `Success`
C) `Error Success`
D) No output

**Your answer:** B

---

### Question 15
Which block ALWAYS executes, whether an exception occurs or not?

A) `try`
B) `except`
C) `else`
D) `finally`

**Your answer:** D

---

### Question 16
What is the output?

```python
try:
    x = [1, 2, 3]
    print(x[5])
except IndexError:
    print("Out of range")
except Exception:
    print("General error")
```

A) `Out of range`
B) `General error`
C) `Out of range General error`
D) `IndexError`

**Your answer:** A

---

### Question 17
Can you have a `try` block without an `except` block?

A) Yes, if you have `finally`
B) Yes, if you have `else`
C) No, `except` is required
D) Yes, always

**Your answer:** A

---

### Question 18
What exception is raised when you convert an invalid string to int?

```python
int("hello")
```

A) `TypeError`
B) `ValueError`
C) `ConversionError`
D) `SyntaxError`

**Your answer:** B

---

## Section 4: OOP Fundamentals (Questions 19-24)

### Question 19
What is the output?

```python
class Car:
    wheels = 4

c = Car()
print(c.wheels)
```

A) `4`
B) `0`
C) `AttributeError`
D) `None`

**Your answer:** A

---

### Question 20
What is the output?

```python
class Test:
    def __init__(self):
        return 5

t = Test()
```

A) `5`
B) `None`
C) `TypeError`
D) `Test object`

**Your answer:** C, init should return None

---

### Question 21
What is the output?

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x + p.y)
```

A) `7`
B) `34`
C) `(3, 4)`
D) `TypeError`

**Your answer:** A

---

### Question 22
What is TRUE about class attributes?

A) They are shared among all instances
B) Each instance has its own copy
C) They must be defined in `__init__`
D) They can't be modified

**Your answer:** A

---

### Question 23
What is the output?

```python
class Box:
    items = []

b1 = Box()
b2 = Box()
b1.items.append("A")
b2.items.append("B")
print(len(b1.items))
```

A) `0`
B) `1`
C) `2`
D) `AttributeError`

**Your answer:** C

---

### Question 24
Which parameter is REQUIRED in every instance method?

A) `self`
B) `this`
C) `cls`
D) No parameter is required

**Your answer:** A

---

## Section 5: Magic Methods & Pandas (Questions 25-30)

### Question 25
What is the output?

```python
class Number:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Number({self.val})"

n = Number(5)
print(n)
```

A) `Number(5)`
B) `5`
C) `<__main__.Number object at 0x...>`
D) `TypeError`

**Your answer:** A

---

### Question 26
What must `__str__` return?

A) A string
B) Any object
C) `None`
D) `self`

**Your answer:** A

---

### Question 27
What is the output?

```python
import pandas as pd
s = pd.Series([False, False, False])
print(s.any())
```

A) `True`
B) `False`
C) `0`
D) `None`

**Your answer:** B

---

### Question 28
What is the output?

```python
import pandas as pd
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(len(df.columns))
```

A) `2`
B) `4`
C) `8`
D) `TypeError`

**Your answer:** A

---

### Question 29
How do you check if a DataFrame has ANY missing values?

A) `df.isna().sum().sum() > 0`
B) `df.has_nan()`
C) `df.missing()`
D) `len(df.isna()) > 0`

**Your answer:** A

---

### Question 30
What is the output?

```python
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
result = df[df['x'] > 1]
print(len(result))
```

A) `0`
B) `1`
C) `2`
D) `3`

**Your answer:** C

#Finish 13:02

---

## Answer Key

**STOP! Don't look at the answers until you've completed all questions.**

<details>
<summary>Click to reveal answers</summary>

### Section 1: Modules & Packages
1. C - `NameError` (math is not imported, only m is)
2. C - It can be used inside functions
3. B - `4.0` (sqrt returns float)
4. C - `from math import *`
5. B - A dictionary of already imported modules
6. A - `ImportError` or `ModuleNotFoundError`

### Section 2: Strings
7. A - `"o"` (negative indexing, -1 is last character)
8. B - `['a', 'b', 'c']` (split returns a list)
9. A - `"th"` (slice from index 2 to 4, not including 4)
10. A - All string methods return new strings (strings are immutable)
11. A - `4` (strip removes leading/trailing whitespace)
12. B - `2` (counts occurrences of "P")

### Section 3: Exceptions
13. A - `A C D` (no exception, so else runs, finally always runs)
14. B - `Success` (no exception, else block executes)
15. D - `finally`
16. A - `Out of range` (IndexError is caught by first except)
17. A - Yes, if you have `finally`
18. B - `ValueError`

### Section 4: OOP Fundamentals
19. A - `4` (class attribute accessed through instance)
20. C - `TypeError` (__init__ cannot return non-None value)
21. A - `7` (3 + 4)
22. A - They are shared among all instances
23. C - `2` (mutable class attribute shared, both appends affect same list)
24. A - `self`

### Section 5: Magic Methods & Pandas
25. A - `Number(5)` (__repr__ is used when __str__ is missing)
26. A - A string (must return str type)
27. B - `False` (.any() returns True if ANY value is True)
28. A - `2` (DataFrame has 2 columns)
29. A - `df.isna().sum().sum() > 0`
30. C - `2` (rows with x=2 and x=3 match condition)

### Scoring Guide
- **27-30 correct (90-100%):** Excellent! Ready for Week 2
- **21-26 correct (70-86%):** Good! Review weak areas
- **15-20 correct (50-66%):** Review Week 1 lessons
- **Below 15 (< 50%):** Revisit Week 1 material thoroughly

</details>

---

## Performance Tracking

**Your Score:** ___/30 (___%)

**Comparison with Exam A:**
- Exam A Score: ___/30
- Exam B Score: ___/30
- Improvement: ___

**Topics to Review:**
- [ ] Modules & Packages
- [ ] Strings
- [ ] Exceptions
- [ ] OOP Fundamentals
- [ ] Magic Methods & Pandas

**Notes:**
