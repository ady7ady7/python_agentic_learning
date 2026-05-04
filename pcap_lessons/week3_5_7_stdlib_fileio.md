# Weeks 3-5: Standard Library Modules & File I/O

This lesson covers essential modules from Python's standard library. These are **built-in** - no installation required.

---

## Table of Contents

| Module | Description |
|--------|-------------|
| [`random`](#the-random-module) | Pseudo-random number generation |
| [`platform`](#the-platform-module) | System and hardware information |
| [`sys`](#the-sys-module) | Python interpreter interaction |
| [`os`](#the-os-module) | Operating system interaction |
| [`datetime`](#the-datetime-module) | Date and time manipulation |
| [File I/O](#file-io) | Reading and writing files |

---

## The `random` Module

The `random` module provides functions for generating pseudo-random numbers and making random selections.

```python
import random
```

---

### `random.random()` - Float between 0 and 1

Returns a random float in the range `[0.0, 1.0)` (includes 0, excludes 1).

```python
import random

print(random.random())  # e.g., 0.7134589023
print(random.random())  # e.g., 0.2918374651
```

---

### `random.seed()` - Reproducible Results

The `seed()` function initializes the random number generator. Using the same seed produces the same sequence of "random" numbers.

```python
import random

random.seed(42)
print(random.random())  # Always: 0.6394267984578837

random.seed(42)
print(random.random())  # Always: 0.6394267984578837 (same!)
```

**Use case:** Testing - when you need predictable "random" values for debugging.

---

### `random.randint(a, b)` - Random Integer (Inclusive)

Returns a random integer N such that `a <= N <= b` (both endpoints included).

```python
import random

print(random.randint(1, 6))   # Dice roll: 1, 2, 3, 4, 5, or 6
print(random.randint(0, 100)) # Random percentage: 0 to 100
```

**PCAP Trap:** Both `a` and `b` are **inclusive**. `randint(1, 6)` can return 6.

---

### `random.randrange(start, stop, step)` - Random from Range

Returns a random element from `range(start, stop, step)`. The `stop` value is **excluded** (like `range()`).

```python
import random

print(random.randrange(10))        # 0 to 9 (stop only)
print(random.randrange(1, 7))      # 1 to 6 (like randint but stop excluded)
print(random.randrange(0, 100, 5)) # 0, 5, 10, 15, ..., 95
```

**Key difference from `randint`:**
- `randint(1, 6)` → can return 1, 2, 3, 4, 5, **6**
- `randrange(1, 7)` → can return 1, 2, 3, 4, 5, 6 (same result, different syntax)

---

### `random.choice(sequence)` - Pick One Element

Returns a single random element from a non-empty sequence.

```python
from random import choice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))  # e.g., 4

colors = ['red', 'green', 'blue']
print(choice(colors))   # e.g., 'green'

word = "Python"
print(choice(word))     # e.g., 'h'
```

---

### `random.sample(sequence, k)` - Pick Multiple Unique Elements

Returns a list of `k` unique elements chosen from the sequence. The elements are placed in **random order**.

```python
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))       # e.g., 4
print(sample(my_list, 5))    # e.g., [3, 1, 8, 9, 10]
print(sample(my_list, 10))   # e.g., [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
```

**Critical rule:** `k` must not be greater than `len(sequence)`.

```python
sample(my_list, 15)  # ValueError: Sample larger than population
```

**Key property:** `sample()` returns **unique** elements - no duplicates. This is different from calling `choice()` multiple times, which can return the same element twice.

```python
# choice() can repeat:
[choice(my_list) for _ in range(5)]  # e.g., [3, 3, 7, 1, 3]

# sample() never repeats:
sample(my_list, 5)                    # e.g., [3, 7, 1, 9, 2] (all unique)
```

---

### `random` Quick Reference

| Function | Returns | Range/Behavior |
|----------|---------|----------------|
| `random()` | float | [0.0, 1.0) |
| `seed(n)` | None | Sets generator state |
| `randint(a, b)` | int | a <= N <= b (inclusive) |
| `randrange(start, stop, step)` | int | Like range(), stop excluded |
| `choice(seq)` | element | Single random element |
| `sample(seq, k)` | list | k unique elements, random order |

### `random` PCAP Traps

1. **`randint` is inclusive on both ends** - `randint(1, 10)` can return 10
2. **`randrange` excludes stop** - `randrange(1, 10)` cannot return 10
3. **`sample(seq, k)` requires `k <= len(seq)`** - otherwise ValueError
4. **`sample()` returns unique elements** - no duplicates possible
5. **`random()` excludes 1.0** - range is [0.0, 1.0), never exactly 1.0

---

## The `platform` Module

The `platform` module provides access to information about the underlying system - the hardware, OS, and Python interpreter.

```python
import platform
```

### Understanding the Execution Layers

When your Python code runs, it goes through several layers:

```
┌─────────────────────────────┐
│      Your Python Code       │  ← You write this
├─────────────────────────────┤
│    Python Interpreter       │  ← Executes your code
├─────────────────────────────┤
│    Operating System (OS)    │  ← Windows, Linux, macOS
├─────────────────────────────┤
│         Hardware            │  ← CPU, RAM, etc.
└─────────────────────────────┘
```

The `platform` module lets you query information from each of these layers. This is useful when:
- Writing cross-platform code that behaves differently on Windows vs Linux
- Debugging environment-specific issues
- Logging system information for diagnostics

**Note:** You may not need this module often, but understanding how your code interacts with the system is valuable knowledge.

---

### `platform.platform()` - Full System Description

Returns a single string identifying the underlying platform with as much useful information as possible.

```python
import platform

print(platform.platform())
# Example outputs:
# Windows: 'Windows-10-10.0.19041-SP0'
# Linux:   'Linux-5.4.0-42-generic-x86_64-with-glibc2.31'
# macOS:   'macOS-12.0-arm64-arm-64bit'
```

**Parameters:**
- `aliased` (default `False`) - If `True`, uses common aliases (e.g., "Windows" instead of "Windows-10")
- `terse` (default `False`) - If `True`, returns minimal information

```python
print(platform.platform(aliased=True))   # May use aliases
print(platform.platform(terse=True))     # Minimal output
```

---

### Common `platform` Functions

```python
import platform

# Operating System
print(platform.system())        # 'Windows', 'Linux', 'Darwin' (macOS)
print(platform.release())       # '10' (Windows 10), '5.4.0' (Linux kernel)
print(platform.version())       # Detailed OS version string

# Hardware
print(platform.machine())       # 'AMD64', 'x86_64', 'arm64'
print(platform.processor())     # CPU info (may be empty on some systems)

# Python Interpreter
print(platform.python_version())           # '3.10.4'
print(platform.python_implementation())    # 'CPython', 'PyPy', etc.
print(platform.python_version_tuple())     # ('3', '10', '4')
```

---

### Practical Example: Cross-Platform Code

```python
import platform

if platform.system() == 'Windows':
    path_separator = '\\'
    clear_command = 'cls'
else:
    path_separator = '/'
    clear_command = 'clear'

print(f"Running on {platform.system()}")
print(f"Python version: {platform.python_version()}")
```

---

### `platform` Quick Reference

| Function | Returns | Example |
|----------|---------|---------|
| `platform()` | Full platform string | 'Windows-10-10.0.19041-SP0' |
| `system()` | OS name | 'Windows', 'Linux', 'Darwin' |
| `release()` | OS release | '10', '5.4.0' |
| `machine()` | Hardware architecture | 'AMD64', 'x86_64' |
| `processor()` | CPU info | 'Intel64 Family 6...' |
| `python_version()` | Python version string | '3.10.4' |
| `python_implementation()` | Interpreter type | 'CPython' |

---

## The `sys` Module

The `sys` module provides access to variables and functions that interact with the **Python interpreter** itself. It's essential for understanding how Python runs your code.

```python
import sys
```

### Key Use Cases

1. **Command-line arguments** - Access arguments passed to your script
2. **Module search path** - Control where Python looks for imports
3. **Standard streams** - Access stdin, stdout, stderr
4. **Interpreter information** - Version, platform, recursion limits
5. **Script termination** - Exit the program with a status code

---

### `sys.argv` - Command Line Arguments

A list containing the script name and any arguments passed to it.

```python
# script.py
import sys

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Total args: {len(sys.argv)}")

# Run: python script.py hello world 123
# Output:
# Script name: script.py
# Arguments: ['hello', 'world', '123']
# Total args: 4
```

**PCAP Trap:** `sys.argv[0]` is always the script name, actual arguments start at index 1.

---

### `sys.path` - Module Search Path

A list of directories where Python looks for modules when you use `import`.

```python
import sys

# See where Python looks for modules
for path in sys.path:
    print(path)

# Add a custom directory (temporarily)
sys.path.append('/my/custom/modules')

# Now Python will also search there for imports
```

**Windows Paths - Backslash Escaping:**

On Windows, paths use backslashes (`\`). Since `\` is normally used to escape characters in strings (e.g., `\n` = newline, `\t` = tab), you must **escape the backslash** with another backslash:

```python
# WRONG - \U and \p are interpreted as escape sequences
sys.path.append('C:\Users\user\py\modules')  # SyntaxError or wrong path!

# CORRECT - Double backslash escapes properly
sys.path.append('C:\\Users\\user\\py\\modules')

# ALTERNATIVE - Raw string (prefix with r)
sys.path.append(r'C:\Users\user\py\modules')
```

**How Python resolves imports:**
1. Current directory (usually first)
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages (third-party packages)

---

### `sys.exit()` - Exit the Program

Terminates the script with an optional exit code.

```python
import sys

def main():
    if some_error:
        print("Error occurred!", file=sys.stderr)
        sys.exit(1)  # Non-zero = error

    print("Success!")
    sys.exit(0)  # Zero = success (optional, default)
```

**Exit codes:**
- `0` = Success (default)
- `1-255` = Error (convention: different codes for different errors)

---

### `sys.stdin`, `sys.stdout`, `sys.stderr` - Standard Streams

The three standard I/O streams:

```python
import sys

# Normal output (what print() uses)
sys.stdout.write("Hello\n")

# Error output (separate stream)
sys.stderr.write("Error message\n")

# Read input (what input() uses)
data = sys.stdin.readline()
```

**Why separate stderr?** Allows redirecting normal output while keeping errors visible:
```bash
python script.py > output.txt  # stdout to file, stderr still on screen
```

---

### `sys.version` and `sys.version_info` - Python Version

```python
import sys

print(sys.version)
# '3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0]'

print(sys.version_info)
# sys.version_info(major=3, minor=10, micro=4, releaselevel='final', serial=0)

# Check minimum version
if sys.version_info < (3, 8):
    sys.exit("Python 3.8+ required")
```

---

### `sys.getrecursionlimit()` / `sys.setrecursionlimit()` - Recursion Control

```python
import sys

print(sys.getrecursionlimit())  # Default: usually 1000

# Increase if needed (be careful!)
sys.setrecursionlimit(2000)
```

**Warning:** Setting too high can crash Python with a stack overflow.

---

### `sys` Quick Reference

| Function/Variable | Description | Example |
|-------------------|-------------|---------|
| `sys.argv` | Command-line arguments | `['script.py', 'arg1']` |
| `sys.path` | Module search paths | `['/home/user', ...]` |
| `sys.exit(code)` | Exit program | `sys.exit(1)` |
| `sys.version` | Python version string | `'3.10.4 ...'` |
| `sys.version_info` | Version as named tuple | `(3, 10, 4, ...)` |
| `sys.stdin/stdout/stderr` | Standard I/O streams | File-like objects |
| `sys.getrecursionlimit()` | Max recursion depth | `1000` |

---

## The `os` Module

The `os` module provides functions for interacting with the **operating system**. It's essential for file/directory operations and environment variables.

```python
import os
```

### Key Use Cases

1. **File/directory operations** - Create, delete, rename, list
2. **Path manipulation** - Join paths, get file info
3. **Environment variables** - Access system configuration
4. **Process management** - Run commands, get current directory

---

### `os.getcwd()` and `os.chdir()` - Working Directory

```python
import os

# Get current working directory
print(os.getcwd())  # '/home/user/project'

# Change directory
os.chdir('/home/user/other_folder')
print(os.getcwd())  # '/home/user/other_folder'
```

---

### `os.listdir()` - List Directory Contents

```python
import os

# List files and folders in current directory
files = os.listdir('.')
print(files)  # ['file1.py', 'folder1', 'data.csv']

# List specific directory
files = os.listdir('/home/user/documents')
```

---

### `os.mkdir()` and `os.makedirs()` - Create Directories

```python
import os

# Create single directory
os.mkdir('new_folder')

# Create nested directories (like mkdir -p)
os.makedirs('parent/child/grandchild', exist_ok=True)
# exist_ok=True prevents error if already exists
```

---

### `os.remove()` and `os.rmdir()` - Delete Files/Directories

```python
import os

# Delete a file
os.remove('unwanted_file.txt')

# Delete an EMPTY directory
os.rmdir('empty_folder')

# For non-empty directories, use shutil.rmtree()
import shutil
shutil.rmtree('folder_with_contents')
```

---

### `os.path` - Path Manipulation (Submodule)

The `os.path` submodule is crucial for cross-platform path handling:

```python
import os

# Join paths (handles OS-specific separators)
path = os.path.join('folder', 'subfolder', 'file.txt')
# Windows: 'folder\\subfolder\\file.txt'
# Linux:   'folder/subfolder/file.txt'

# Check if path exists
os.path.exists('some_file.txt')  # True/False

# Check if it's a file or directory
os.path.isfile('data.csv')      # True if it's a file
os.path.isdir('my_folder')      # True if it's a directory

# Get file name from path
os.path.basename('/home/user/file.txt')  # 'file.txt'

# Get directory from path
os.path.dirname('/home/user/file.txt')   # '/home/user'

# Split into directory and filename
os.path.split('/home/user/file.txt')  # ('/home/user', 'file.txt')

# Get file extension
os.path.splitext('data.csv')  # ('data', '.csv')

# Get absolute path
os.path.abspath('relative/path')  # '/full/absolute/path'
```

---

### `os.environ` - Environment Variables

```python
import os

# Get an environment variable
home = os.environ.get('HOME')  # '/home/user' (Linux/Mac)
path = os.environ.get('PATH')  # System PATH variable

# Get with default if not set
debug = os.environ.get('DEBUG', 'False')

# Set an environment variable (for this process only)
os.environ['MY_VAR'] = 'some_value'
```

**Common environment variables:**
- `HOME` / `USERPROFILE` - User's home directory
- `PATH` - Executable search paths
- `PYTHONPATH` - Additional Python module paths

---

### `os.name` - Operating System Name

```python
import os

print(os.name)
# 'nt'     - Windows
# 'posix'  - Linux, macOS, Unix
```

---

### Practical Example: Cross-Platform Script

```python
import os
import sys

def setup_project():
    # Get project directory (where script is located)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create data directory if it doesn't exist
    data_dir = os.path.join(script_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Check if config file exists
    config_path = os.path.join(script_dir, 'config.ini')
    if not os.path.exists(config_path):
        print(f"Warning: {config_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Project setup complete in {script_dir}")

if __name__ == '__main__':
    setup_project()
```

---

### `os` Quick Reference

| Function | Description | Example |
|----------|-------------|---------|
| `os.getcwd()` | Get current directory | `'/home/user'` |
| `os.chdir(path)` | Change directory | `os.chdir('/tmp')` |
| `os.listdir(path)` | List directory contents | `['file1', 'file2']` |
| `os.mkdir(path)` | Create directory | `os.mkdir('new')` |
| `os.makedirs(path)` | Create nested directories | `os.makedirs('a/b/c')` |
| `os.remove(path)` | Delete file | `os.remove('file.txt')` |
| `os.rmdir(path)` | Delete empty directory | `os.rmdir('empty')` |
| `os.path.join()` | Join path components | `'a/b/c'` or `'a\\b\\c'` |
| `os.path.exists()` | Check if path exists | `True/False` |
| `os.path.isfile()` | Check if it's a file | `True/False` |
| `os.path.isdir()` | Check if it's a directory | `True/False` |
| `os.environ` | Environment variables dict | `os.environ['HOME']` |
| `os.name` | OS type | `'nt'`- Windows or `'posix' - Unix or 'java' - if code is written in sth like Jython` |


FOR UNIX/LINUX
| os.uname()) |  information about the current operating system | systemname / nodename, release, version, machine (e.g. x86_64)


---

> **`datetime` and `time` modules** have been moved to a dedicated lesson: [`week9_datetime_time_calendar.md`](week9_datetime_time_calendar.md)

---

## File I/O

### Opening Files - The `with` Statement

```python
# ALWAYS use context manager (auto-closes file)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here

# WITHOUT context manager (NOT recommended)
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### File Modes

```python
'r'   # Read (default) - file must exist
'w'   # Write - creates new or TRUNCATES existing
'a'   # Append - creates new or appends to existing
'x'   # Exclusive create - fails if file exists

'rb'  # Read binary
'wb'  # Write binary

'r+'  # Read and write (file must exist)
'w+'  # Write and read (truncates)


```

### Reading Files

```python
# Read entire file as string
with open('file.txt', 'r') as f:
    content = f.read()

# Read specific number of characters
with open('file.txt', 'r') as f:
    chunk = f.read(100)  # First 100 chars

# Read one line (includes \n!)
with open('file.txt', 'r') as f:
    line = f.readline()

# Read all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()  # ['line1\n', 'line2\n', ...]

# Iterate line by line (MEMORY EFFICIENT!)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Remove trailing \n
```

### Writing Files

```python

#We can create an empty file like that - using w.write() WOULD cause a TypeError
with open(self.filepath, 'w') as w:
    pass

# Write string
#Also remember that 'w' mode OVERWRITES previous data - so we might consider using append if we want to add content
with open('file.txt', 'w') as f:
    f.write('Hello, World!\n')

# Write multiple lines
with open('file.txt', 'w') as f:
    lines = ['line1\n', 'line2\n', 'line3\n']
    f.writelines(lines)  # Does NOT add \n automatically!

# Append to file
with open('file.txt', 'a') as f:
    f.write('Appended line\n')
```

### File Position

```python
with open('file.txt', 'r') as f:
    pos = f.tell()  # Get current position (0 at start)

    f.read(10)
    pos = f.tell()  # Now 10

    f.seek(0)       # Go back to start
    f.seek(0, 2)    # Go to end (offset 0 from end)
```

### PCAP Traps - File I/O

```python
# TRAP 1: read() vs readline() vs readlines()
f.read()       # Entire file as ONE string
f.readline()   # ONE line (with \n)
f.readlines()  # ALL lines as list

# TRAP 2: writelines() does NOT add newlines
f.writelines(['a', 'b', 'c'])  # Writes 'abc', not 'a\nb\nc\n'

# TRAP 3: 'w' mode TRUNCATES existing files
with open('existing.txt', 'w') as f:  # File is now EMPTY
    f.write('new content')

# TRAP 4: readline() includes \n
line = f.readline()  # 'hello\n'
line = line.strip()  # 'hello' (use strip() to remove)
```

### File I/O Quick Reference

| Function | Description | Returns |
|----------|-------------|---------|
| `open(path, mode)` | Open file | File object |
| `f.read()` | Read entire file | String |
| `f.read(n)` | Read n characters | String |
| `f.readline()` | Read one line | String (with \n) |
| `f.readlines()` | Read all lines | List of strings |
| `f.write(s)` | Write string | Number of chars |
| `f.writelines(lst)` | Write list of strings | None |
| `f.tell()` | Get position | Integer |
| `f.seek(pos)` | Move to position | New position |
| `f.close()` | Close file | None |

---

## PCAP Traps - All Modules

1. **`sys.argv[0]`** is the script name, not the first argument
2. **`sys.exit()`** without argument exits with code 0 (success)
3. **`os.path.join()`** is preferred over string concatenation for paths
4. **`os.makedirs()`** creates all intermediate directories, `os.mkdir()` doesn't
5. **`os.rmdir()`** only works on EMPTY directories
6. **`os.environ.get()`** is safer than `os.environ[]` (returns None vs raises KeyError)
7. **`strftime`** = format (dt→str), **`strptime`** = parse (str→dt)
8. **`f.read()`** reads entire file, **`f.readline()`** reads ONE line
9. **`f.writelines()`** does NOT add newlines automatically
10. **`'w'` mode TRUNCATES** existing files - use `'a'` to append

---

---

# Week 7: The `logging` Module

---

## PART 1 — WHY does `logging` exist?

You already know `print()`. So why learn another tool?

Run this in `practice.py` and look at the output:

```python
print("Trade opened")
print("SL hit")
print("Trade opened")
print("Prices: 100, 101, 99, 98, 97, 96...")  # 500 of these
```

**The problem:** After two weeks of running backtests, you have 5000 `print()` lines filling your terminal. Now you want to find only the SL hits. You can't filter. You don't know when they happened. You can't turn off the price noise without deleting code. You can't write it to a file without rewriting everything.

**`logging` solves all of this** by separating three concerns:
1. **What** to record (the message + severity level)
2. **Where** to send it (console, file, both, neither)
3. **How** to format it (with or without timestamps, names, etc.)

Each concern is handled by a separate object. That's why the API feels unfamiliar at first — it has moving parts by design.

---

## PART 2 — The Three Objects You Need to Know

Before any code: understand these three things conceptually.

### The Logger
**WHAT it is:** The object your code talks to. You call `logger.info("msg")` or `logger.warning("msg")`. The Logger decides: is this message important enough to forward? (based on its level threshold). If yes, it passes the message to its Handlers.

**Analogy:** The Logger is your receptionist. You give it a message. It checks if the message is urgent enough to bother anyone. If yes, it passes it on.

### The Handler
**WHAT it is:** The object that actually *delivers* the message somewhere. A `StreamHandler` prints to the console. A `FileHandler` writes to a file. One Logger can have multiple Handlers — so the same message can go to both console AND file simultaneously.

**Analogy:** The Handler is the delivery person. The receptionist (Logger) hands them the message, and they deliver it to the destination (console, file, etc.). You can have multiple delivery people for the same message.

### The Formatter
**WHAT it is:** The object that controls what the final text looks like. Without a Formatter, you get bare text. With one, you get timestamps, severity labels, file names, etc.

**Analogy:** The Formatter is the envelope template. It decides whether the message arrives as `"SL hit"` or `"2026-02-16 14:23:01 [WARNING ] engine: SL hit"`.

### The Flow — All Together

```
Your code calls:  logger.warning("SL hit")
                        │
                   Logger checks:
                   Is WARNING >= my level threshold?
                        │
                   YES → passes to Handler(s)
                        │
                   Handler checks:
                   Is WARNING >= MY level threshold?
                        │
                   YES → applies Formatter → sends to destination
```

**This two-gate system is the most important concept in this lesson.**

---

## PART 3 — Start Minimal, Build Up

### Step 0: The zero-config case

Run this and observe:

```python
import logging

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
```

**Expected output:**
```
WARNING:root:warning message
ERROR:root:error message
```

**Why only two lines?** Python has a default threshold of WARNING. `debug` and `info` are silenced. The format `WARNING:root:warning message` is Python's built-in last-resort format: `LEVEL:logger_name:message`. The logger name is `root` because we used the global `logging` module directly.

**Key insight:** You did NOT need to configure anything. Logging works out of the box for WARNING and above. This is intentional — a library you import shouldn't flood your console with debug noise unless you ask for it.

---

### Step 1: Change the threshold with `basicConfig()`

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
```

**Expected output:**
```
DEBUG:root:debug message
INFO:root:info message
WARNING:root:warning message
```

`basicConfig()` configures the **root logger** (the global one). Now all five levels are visible.

**The one-shot rule:** `basicConfig()` only works if the root logger has NO handlers yet. Call it once, at the start of your script. Any subsequent call is silently ignored.

```python
logging.basicConfig(level=logging.DEBUG)   # ← this one takes effect
logging.basicConfig(level=logging.WARNING) # ← this is silently ignored
logging.debug("hello")  # still appears — first call won
```

---

### Step 2: Add a timestamp with `basicConfig()`

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
)

logging.info("Price stream started")
logging.warning("SL hit for AAPL")
```

**Expected output:**
```
14:23:01 [INFO] Price stream started
14:23:01 [WARNING] SL hit for AAPL
```

You control the format with placeholders. The useful ones:

| Placeholder | Produces |
|-------------|----------|
| `%(asctime)s` | Timestamp |
| `%(levelname)s` | `DEBUG`, `INFO`, `WARNING`, etc. |
| `%(message)s` | Your actual message |
| `%(name)s` | The logger's name |
| `%(filename)s` | The source .py file |
| `%(lineno)d` | Line number |

---

### Step 3: Named loggers — why not just use `logging.warning()` everywhere?

`logging.warning("msg")` uses the root logger. That's fine for a single script. In a project with 10 files, you lose track of where messages come from.

```python
import logging

# In engine/backtest.py:
logger = logging.getLogger('engine.backtest')
logger.warning("SL hit")

# Output (with basicConfig):
# WARNING:engine.backtest:SL hit
```

Now you know the message came from `engine.backtest`, not `strategies.moving_average`.

**The standard pattern:**
```python
logger = logging.getLogger(__name__)
```

`__name__` is automatically the full module path (`algo_backtest.engine.backtest`). This is the professional standard — use it in every module.

**The singleton rule:** `logging.getLogger('same_name')` always returns the **exact same object**. Loggers are stored in a global registry. This means:
- Call `getLogger('engine')` in module A and module B → same logger
- Configure it once (in `main.py`) → affects all code using that logger name
- No need to pass logger objects around as parameters

---

### Step 4: Handlers — multiple destinations

Here is where the Logger/Handler split pays off.

**Scenario:** You want WARNING and above on the console (so you notice problems), but DEBUG and above in a log file (for detailed post-run analysis).

```python
import logging
import sys

logger = logging.getLogger('trading')
logger.setLevel(logging.DEBUG)       # Logger gate: pass everything

# Console handler — only WARNING and above
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.WARNING)

# File handler — everything from DEBUG up
file_h = logging.FileHandler('backtest.log', mode='a')
file_h.setLevel(logging.DEBUG)

# Formatter
fmt = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')
console.setFormatter(fmt)
file_h.setFormatter(fmt)

# Attach handlers to the logger
logger.addHandler(console)
logger.addHandler(file_h)

# Now use it:
logger.debug("tick: AAPL 150.23")    # → file only
logger.info("position opened")        # → file only
logger.warning("SL approaching")      # → console AND file
logger.error("position close failed") # → console AND file
```

**The two-gate rule visualised:**

```
logger.debug("tick: AAPL 150.23")
    │
    Logger gate: DEBUG(10) >= DEBUG(10)? YES → passes on
    │
    ├── Console gate: DEBUG(10) >= WARNING(30)? NO → blocked
    └── File gate:    DEBUG(10) >= DEBUG(10)? YES → written to file

logger.warning("SL approaching")
    │
    Logger gate: WARNING(30) >= DEBUG(10)? YES → passes on
    │
    ├── Console gate: WARNING(30) >= WARNING(30)? YES → printed
    └── File gate:    WARNING(30) >= DEBUG(10)? YES → written to file
```

**Critical insight:** If the Logger's level is stricter than any Handler's level, the Handler's permissiveness doesn't matter — the message never reaches it. The Logger is always the first gate.

---

### Step 5: How to test your logger

This is what was missing from Day 1. Run this directly in `practice.py`:

```python
import logging
import sys

# --- Build a logger from scratch ---
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('[%(levelname)s] %(name)s: %(message)s')) #Inaczej level błędu - INFO/DEBUG ITD. / PLIK / MSG
logger.addHandler(handler)

# --- Test every level ---
logger.debug("This is DEBUG")
logger.info("This is INFO")
logger.warning("This is WARNING")
logger.error("This is ERROR")
logger.critical("This is CRITICAL")
```

**Expected output:**
```
[DEBUG   ] test_logger: This is DEBUG
[INFO    ] test_logger: This is INFO
[WARNING ] test_logger: This is WARNING
[ERROR   ] test_logger: This is ERROR
[CRITICAL] test_logger: This is CRITICAL
```

If you see all five lines: your logger + handler + formatter are working.

**Test the two-gate filter:**
```python
# Change handler level to WARNING — DEBUG and INFO should disappear
handler.setLevel(logging.WARNING)

logger.debug("should NOT appear")
logger.info("should NOT appear")
logger.warning("SHOULD appear")
```

**Test the singleton:**
```python
a = logging.getLogger('test_logger')
b = logging.getLogger('test_logger')
print(a is b)  # True — same object
```

---

## PART 4 — The Five Levels

Every log call has a severity. You choose which one based on what the message means:

| Level | Numeric | Use when... |
|-------|---------|-------------|
| `DEBUG` | 10 | Detailed trace: "tick received: AAPL 150.23" |
| `INFO` | 20 | Normal event: "position opened", "backtest complete" |
| `WARNING` | 30 | Unexpected but recoverable: "SL not set", "price data gap" |
| `ERROR` | 40 | Operation failed: "can't close position", "file not found" |
| `CRITICAL` | 50 | System can't continue: "database unreachable", "config missing" |

The numeric values matter for PCAP: **10, 20, 30, 40, 50**.

---

## PART 5 — `logging` vs `warnings` (PCAP Trap)

These are two completely separate Python modules that happen to have overlapping names:

```python
import logging
import warnings

# logging.warning() — part of the logging system
# → Produces a log record at WARNING level
# → Goes through Logger → Handler → output destination
# → Does NOT raise anything
logging.warning("SL not set on position")

# warnings.warn() — Python's built-in deprecation/advisory system
# → Triggers a Python Warning (like a lightweight exception)
# → By default prints to stderr once
# → Can be filtered, turned into errors, or silenced
# → Used by library authors to say "this usage is deprecated"
warnings.warn("This method will be removed in v2", DeprecationWarning)
```

**When to use which:**
- In your running application (trade opened, SL hit, price spike) → `logging.warning()`
- In a library, to tell developers their usage is outdated → `warnings.warn()`

**PCAP pattern:** If the question says `logging.warning()` → it logs a record, nothing more. No exceptions raised.

---

## PART 6 — `basicConfig()` vs Manual Setup

Two valid approaches depending on context:

### Approach 1: `basicConfig()` — for simple scripts

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logging.info("Script started")
```

**When to use:** Quick scripts, notebooks, throwaway code. One call, done.

**Limitation:** Can't have different levels for console vs file. Once called, can't be changed.

### Approach 2: Manual setup — for projects

```python
import logging
import sys

def setup_logging(level: int = logging.INFO) -> None:
    root = logging.getLogger()
    root.setLevel(level)

    fmt = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    root.addHandler(console)

# Call once in main.py before anything else
setup_logging(level=logging.DEBUG)
```

Then in every module:
```python
# algo_backtest/engine/backtest.py
import logging

logger = logging.getLogger(__name__)   # No configuration here — just get the logger

class BacktestEngine:
    def open_position(self, ...):
        ...
        logger.info("Position opened: %s %s @ %.2f", side, ticker, price)
```

**Why `%s` not f-strings?** Lazy evaluation. With `%s`, the string is only formatted if the message actually gets emitted. With f-strings, the string is always built — even if DEBUG is filtered out and nobody ever sees it.

---

## PART 7 — PCAP Traps Summary

1. **Default level is WARNING** — `debug()` and `info()` produce no output without configuration
2. **Default output format** is `LEVEL:logger_name:message` — not bare text
3. **`basicConfig()` is one-shot** — second call is silently ignored (no error)
4. **Level numbers: DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50**
5. **Two-gate rule** — logger level AND handler level must both pass. Stricter one always wins
6. **`getLogger('same_name')` → same object** — loggers are global singletons by name
7. **`logging.warning()` ≠ `warnings.warn()`** — different modules, different mechanisms
8. **`logging.exception()`** — logs at ERROR level AND appends current traceback automatically. Use only inside `except` blocks
9. **`FileHandler` default mode is `'a'`** (append)
10. **`%s` preferred over f-strings** in log calls for lazy evaluation

---

## Quick Reference

```python
import logging
import sys

# ── Minimal (scripts) ──────────────────────────────────────────
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.warning("something unexpected")

# ── Manual (projects) ──────────────────────────────────────────
logger = logging.getLogger(__name__)          # get/create named logger
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)   # where output goes
handler.setLevel(logging.DEBUG)               # handler's own filter
handler.setFormatter(
    logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
)
logger.addHandler(handler)

# ── Log calls ──────────────────────────────────────────────────
logger.debug("detailed trace")
logger.info("normal event")
logger.warning("unexpected but ok")
logger.error("operation failed")
logger.critical("system down")
logger.exception("error with traceback")   # inside except only
```

---

## PART 8 — `%s` in Log Calls vs `%(name)s` in Formatters

These look similar but are **completely different mechanisms**. This trips everyone up.

### Formatter placeholders — `%(name)s` with parentheses

Used only when defining a `Formatter`. These pull metadata about the log record:

```python
logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
#                  ^^^^^^^^^^^  ^^^^^^^^^^^^^  ^^^^^^^^  ^^^^^^^^^^^
#                  timestamp    level string   logger    your message
```

You cannot use these in your actual log call — they are only for the Formatter template.

### Log call placeholders — `%s`, `%d`, `%.2f`

Used in the **message string** passed to `logger.info()`, `logger.warning()` etc. They work exactly like old-style Python string formatting (`'hello %s' % value`):

```python
# Syntax: logger.level("template with %s", value1, value2, ...)
logger.info("Position opened: %s %s @ %.2f", side, ticker, price)
logger.warning("Bad value: %s (expected int)", bad_input)
logger.error("Division failed: %s / %s", a, b)
logger.debug("Processing %d ticks for %s", count, ticker)
```

**Why this syntax and not f-strings?**

With f-strings, the string is *always* built — even if the message level is filtered out and nobody ever sees it:
```python
# Always builds the string, even if DEBUG is silenced:
logger.debug(f"Tick {price:.2f} for {ticker}")

# Lazy — string only built if the message passes both gates:
logger.debug("Tick %.2f for %s", price, ticker)
```

For high-frequency log calls (like per-tick DEBUG messages), lazy evaluation is a real performance win.

**In practice — both work.** f-strings are readable and fine for most project code. The `%s` style is the logging module's native convention and appears in PCAP questions. Know both.

| Style | Syntax | Notes |
|-------|--------|-------|
| f-string | `logger.info(f"result={x}")` | Readable, always evaluated |
| `%s` | `logger.info("result=%s", x)` | Lazy, logging convention |
| Formatter | `'%(levelname)s: %(message)s'` | Metadata only, not for log calls |

