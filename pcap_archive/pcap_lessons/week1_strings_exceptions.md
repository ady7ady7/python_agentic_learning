
---

### Professional Standards Recap

**For Project Code (AlgoBacktest):**
- ✅ Always use type hints: `def load_data(file_path: str) -> pd.DataFrame:`
- ✅ Add docstrings: Module, class, and function level
- ✅ Follow PEP 8: `snake_case` for functions, `PascalCase` for classes
- ✅ Use absolute imports for clarity
- ✅ Meaningful names: `price_dataframe` not `df`

**For PCAP Drills:**
- Focus on pure Python behavior and edge cases
- Understand import mechanics deeply (when/how code executes)
- Know the traps and gotchas listed above

---

## Week 1 (Continued): Strings, Exceptions & File I/O

**Learning Objectives:**
- Master string operations and formatting (slicing, methods, f-strings)
- Understand exception hierarchy and custom exceptions  
- Handle file I/O safely with context managers
- Apply these concepts to build the DataLoader class

### Theory

**1. String Operations & Slicing:**

```python
"""String manipulation essentials."""

text = "Python PCAP"

# Slicing [start:stop:step]
print(text[0:6])      # "Python"
print(text[7:])       # "PCAP"
print(text[::-1])     # "PACP nohtyP" (reverse)
print(text[::2])      # "Pto CA" (every 2nd char)

# Negative indexing
print(text[-4:])      # "PCAP"
print(text[:-5])      # "Python"

# String immutability
# text[0] = 'J'  # TypeError: 'str' object does not support item assignment
```

**PCAP Trap:** Strings are **immutable**. Methods like `.replace()`, `.upper()` return NEW strings.

```python
original = "hello"
modified = original.upper()
print(original)  # "hello" (unchanged!)
print(modified)  # "HELLO"
```

---

**2. String Methods (PCAP Favorites):**

```python
"""Critical string methods for the exam."""

s = "  Python3.10  "

# Whitespace removal
s.strip()       # "Python3.10"
s.lstrip()      # "Python3.10  "
s.rstrip()      # "  Python3.10"

#Lstrip/rstrip can also be used to remove selected characters e.g.
print("www.cisco.com".lstrip("w.")) # cisco.com
print("pythoninstitute.org".lstrip(".org")) #pythoninstitute.org - No change here!

# Case manipulation
s.lower()       # "  python3.10  "
s.upper()       # "  PYTHON3.10  "
s.capitalize()  # "  python3.10  " (only first char)
s.title()       # "  Python3.10  " (each word)
s.swapcase() -  print("I know that I know nothing.".swapcase()) #i KNOW THAT i KNOW NOTHING.
s.title() - print("I know that I know nothing.".title()) #I Know That I Know Nothing. Part 1.


# Searching
s.find('3')     # 8 (index of first occurrence, -1 if not found)
s.index('3')    # 8 (raises ValueError if not found)
s.count('o')    # 1 

# Boolean checks
s.isdigit()     # Checks for NUMBERS
s.isalpha()     # Checks for LETTERS
s.isalnum()     # Checks if given string is ALL numbers
"123".isdigit() # True

s.islower() # Checks for lowercase letters only
s.isupper() # Checks for uppercase letters only
s.isspace() #Checks for whitespaces only

#SPLITTING - IT'S A REVERSED JOIN
"a,b,c".split(',')       # ['a', 'b', 'c']
print("phi       chi\npsi".split())   -> #['phi', 'chi', 'psi']

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split() ['Where', 'are', 'the', 'snows', 'of', 'yesteryear']

#JOINING - IT'S A REVERSED SPLIT
",".join(['a', 'b', 'c']) # "a,b,c"
print(",".join(["omicron", "pi", "rho"])) #omicron,pi,rho

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list) #Where*are*the*snows?

#REPLACING
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) #www.pythoninstitute.org
print("This is it!".replace("is", "are")) #Thare are it!
print("Apple juice".replace("juice", "")) #Apple

print("This is it!".replace("is", "are", 1))  #Thare is it - the third argument makes it so that only the first occurence is replaced
print("This is it!".replace("is", "are", 2)) #Thare are it - here two occurences are replaced, thanks to the thid argument
```

**PCAP Trap:** `.find()` returns `-1` if not found, `.index()` raises `ValueError`.

---

**3. String Formatting (Modern Python):**

```python
"""String formatting methods - know all 3 for PCAP."""

name = "Alice"
age = 30

# 1. Old-style (%)
msg1 = "Name: %s, Age: %d" % (name, age)

# 2. .format() method
msg2 = "Name: {}, Age: {}".format(name, age)
msg3 = "Name: {n}, Age: {a}".format(n=name, a=age)

# 3. f-strings (Python 3.6+) - PREFERRED
msg4 = f"Name: {name}, Age: {age}"
msg5 = f"Next year: {age + 1}"  # Expressions allowed!

# Formatting numbers
pi = 3.14159
print(f"Pi: {pi:.2f}")  # "Pi: 3.14"
```

---

**4. Exception Handling:**

```python
"""Exception hierarchy and handling patterns."""

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")

# Exception hierarchy matters!
try:
    risky_operation()
except FileNotFoundError:  # Specific first
    handle_missing_file()
except IOError:            # General later
    handle_io_error()
except Exception:          # Catch-all last
    handle_unknown()

# else and finally
try:
    file = open('data.txt')
except FileNotFoundError:
    print("File not found")
else:
    # Runs if NO exception occurred
    data = file.read()
    file.close()
finally:
    # ALWAYS runs (cleanup code)
    print("Cleanup complete")
```

**PCAP Exception Hierarchy:**
```
BaseException
├── Exception
│   ├── ArithmeticError
│   │   ├── ZeroDivisionError
│   │   └── OverflowError
│   ├── LookupError
│   │   ├── IndexError
│   │   └── KeyError
│   ├── ValueError
│   ├── TypeError
│   └── IOError (OSError)
│       ├── FileNotFoundError
│       └── PermissionError
└── KeyboardInterrupt
```

---

**5. File I/O & Context Managers:**

```python
"""File handling - ALWAYS use context managers."""

# WRONG - manual close (can leak if exception occurs)
file = open('data.txt', 'r')
data = file.read()
file.close()

# CORRECT - context manager (auto-closes)
with open('data.txt', 'r') as file:
    data = file.read()
# File automatically closed here, even if exception occurred

# File modes
'r'   # Read (default)
'w'   # Write (overwrites)
'a'   # Append
'r+'  # Read + Write
'rb'  # Read binary

# Reading methods
with open('data.txt', 'r') as f:
    content = f.read()        # Entire file as string
    lines = f.readlines()     # List of lines
    line = f.readline()       # Single line

    # Iterate line by line (memory efficient)
    for line in f:
        process(line.strip())

# Writing
with open('output.txt', 'w') as f:
    f.write("Hello\n")
    f.writelines(['Line 1\n', 'Line 2\n'])
```

---

### PCAP TRAPS & GOTCHAS

**Trap 1: String Slicing Edge Cases**
```python
"""Slicing never raises IndexError - it adjusts."""

s = "Python"

print(s[100:])    # "" (empty, not error!)
print(s[-100:])   # "Python" (starts from beginning)
print(s[2:1])     # "" (start > stop = empty)
```

---

**Trap 2: Exception Catching Order**
```python
"""Order matters! Specific exceptions MUST come first."""

# WRONG - will never catch ValueError
try:
    int("abc")
except Exception:      # Catches everything
    print("Generic")
except ValueError:     # Unreachable code!
    print("Value error")

# CORRECT
try:
    int("abc")
except ValueError:     # Specific first
    print("Value error")
except Exception:      # General last
    print("Generic")
```

---

**Trap 3: File Handle Leaks**
```python
"""Without context manager, file stays open on exception."""

# BAD - file never closes if error occurs during read()
def read_data():
    f = open('data.txt')
    data = f.read()  # If this raises exception, f.close() never runs
    f.close()
    return data

# GOOD - context manager guarantees cleanup
def read_data():
    with open('data.txt') as f:
        return f.read()  # File closes even if exception occurs
```

---

### Exam Tips

**Critical Concepts for PCAP:**

1. **String slicing never raises IndexError** - returns empty string or adjusts
2. **Exception order:** Specific → General (ValueError before Exception)
3. **`else` in try/except:** Runs ONLY if no exception occurred
4. **`finally`:** ALWAYS runs (even with return/break in try block)
5. **Context managers:** `with` statement auto-calls `__enter__` and `__exit__`

**Common PCAP Questions:**
- "What is the output?" with string slicing edge cases
- Exception handling order (which except block runs?)
- File mode differences ('r' vs 'w' vs 'a')

---
