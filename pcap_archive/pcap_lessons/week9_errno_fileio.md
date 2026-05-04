# Week 9: File Streams, open() & Diagnosing Errors with `errno`

This lesson covers the full file I/O model — streams, open modes, binary vs text,
predefined streams, the `open()` function — and how Python exposes OS-level error
codes through `IOError.errno` and the `errno` module.

---

## Table of Contents

- [Files and streams](#files-and-streams)
- [Open modes](#open-modes)
- [Binary streams vs text streams](#binary-streams-vs-text-streams)
- [The open() function](#the-open-function)
- [Predefined streams](#predefined-streams)
- [Why errno exists](#why-errno-exists)
- [Reading errno from an exception](#reading-errno-from-an-exception)
- [The errno module](#the-errno-module)
- [Common errno constants](#common-errno-constants)
- [Practical pattern: branching on errno](#practical-pattern-branching-on-errno)
- [PCAP Traps](#pcap-traps)
- [bytearray and binary files](#bytearray-and-binary-files)
- [Text vs binary reading — full comparison](#text-vs-binary-reading--full-comparison)

---

## Files and streams

Before a program can process a file, the file must be **opened**. When you open a
file, Python associates it with a **stream** — an abstract representation of the
physical data stored on the media. When processing is finished, the file must be
**closed** to flush buffers and release the OS file descriptor.

```
Physical file on disk  ←→  Stream object in Python  ←→  Your program
```

The stream is the interface your code works with. You never touch the disk directly —
all reads and writes go through the stream.

---

## Open modes

Three open modes exist:

| Mode | Description |
|---|---|
| **read mode** | Only read operations are allowed. The file must already exist. |
| **write mode** | Only write operations are allowed. Creates the file if it doesn't exist; truncates if it does. |
| **update mode** | Both reads and writes are allowed. |

In `open()` these map to the `mode` argument:

| `mode` string | Meaning |
|---|---|
| `'r'` | Read (text). File must exist. |
| `'w'` | Write (text). Truncates or creates. |
| `'a'` | Append (text). Writes at end; creates if needed. |
| `'x'` | Exclusive create (text). Fails with `FileExistsError` if file exists. |
| `'r+'` | Update (read + write). File must exist. |
| `'rb'`, `'wb'`, `'ab'` | Binary equivalents of the above. |

---

## Binary streams vs text streams

Python uses two different class families depending on the file content:

| Class | Used for | What it handles |
|---|---|---|
| `BufferedIOBase` | **Binary streams** | Any file — images, executables, raw bytes |
| `TextIOBase` | **Text streams** | Human-readable text files divided into lines by newline markers |

When you call `open("file.txt", "r")` you get a `TextIOWrapper` (subclass of `TextIOBase`).
When you call `open("file.bin", "rb")` you get a `BufferedReader` (subclass of `BufferedIOBase`).

```python
f = open("data.txt", "r")
print(type(f))   # <class '_io.TextIOWrapper'>

g = open("data.bin", "rb")
print(type(g))   # <class '_io.BufferedReader'>
```

**Key rule:** Text streams handle encoding/decoding automatically and translate
newlines (`\n` ↔ `\r\n` on Windows). Binary streams pass raw bytes unchanged.

---

## The open() function

Full syntax:

```python
open(file_name, mode=open_mode, encoding=text_encoding)
```

- `file_name` — path to the file (string or path-like object)
- `mode` — open mode string (default: `'r'`)
- `encoding` — text encoding (default: platform-dependent, usually `'utf-8'`); only relevant for text mode

On success, `open()` returns a **stream object** and associates it with the named file.
On failure, it raises an `IOError` (which is `OSError`).

```python
# Always use a context manager — it closes the file automatically
with open("prices.csv", "r", encoding="utf-8") as f:
    content = f.read()
# File is guaranteed closed here, even if an exception occurred
```

Without `with`, you must call `f.close()` manually. Forgetting it leaks a file
descriptor — on long-running programs this causes `errno.EMFILE` (too many open files).

---

## Predefined streams

Three streams are already open when any Python program starts. They come from `sys`:

| Stream | Name | Default | Description |
|---|---|---|---|
| `sys.stdin` | Standard input | keyboard | `input()` reads from here |
| `sys.stdout` | Standard output | terminal | `print()` writes here |
| `sys.stderr` | Standard error | terminal | Error messages and tracebacks go here |

```python
import sys

sys.stdout.write("hello\n")   # same as print("hello")
sys.stderr.write("error!\n")  # goes to stderr, not stdout

line = sys.stdin.readline()   # reads one line from keyboard
```

These can be **redirected** at the OS level (e.g., `python script.py > output.txt`)
or reassigned in Python:

```python
import sys

sys.stdout = open("log.txt", "w")  # redirect all print() to a file
print("this goes to log.txt")
```

**PCAP note:** `sys.stdin`, `sys.stdout`, `sys.stderr` are text streams
(instances of `TextIOWrapper`). They are opened automatically — you never call
`open()` for them.

---

## Why errno exists

When an OS call fails (opening a file, writing to a stream, etc.), the operating system
sets a numeric error code describing what went wrong. Python surfaces this code through
the `errno` attribute on `OSError` (and its aliases `IOError`, `EnvironmentError`).

Knowing the exact numeric code lets you **branch your error handling** — responding
differently to "file not found" vs "permission denied" vs "disk full".

---

## Reading errno from an exception

```python
try:
    # Some stream operation
    with open("secret.txt", "w") as f:
        f.write("data")
except IOError as exc:
    print(exc.errno)      # integer error code, e.g. 13
    print(exc.strerror)   # human-readable message, e.g. "Permission denied"
    print(exc.filename)   # the file name involved, if any
```

`IOError` is an **alias** for `OSError` in Python 3 — they are the same class.
`EnvironmentError` is also an alias. All three catch the same exceptions.

```python
print(IOError is OSError)          # True
print(EnvironmentError is OSError) # True
```

---

## The errno module

```python
import errno
```

The `errno` module exposes symbolic constants that map to the OS numeric codes.
You compare `exc.errno` against these constants instead of hard-coding integers.

```python
import errno

try:
    open("missing.txt")
except IOError as exc:
    if exc.errno == errno.ENOENT:
        print("File does not exist — handle gracefully")
    elif exc.errno == errno.EACCES:
        print("No permission — inform the user")
    else:
        raise  # re-raise anything we don't specifically handle
```

---

## Common errno constants

| Constant | Value (Linux) | Meaning |
|---|---|---|
| `errno.EACCES` | 13 | **Permission denied** — tried to open a read-only file for writing, or access without rights |
| `errno.EBADF` | 9 | **Bad file number** — operating on a stream that is not open |
| `errno.EEXIST` | 17 | **File exists** — tried to create/rename a file to a name that already exists |
| `errno.EFBIG` | 27 | **File too large** — tried to write a file exceeding the OS maximum size |
| `errno.EISDIR` | 21 | **Is a directory** — used a directory path where an ordinary file was expected |
| `errno.EMFILE` | 24 | **Too many open files** — exceeded the OS limit on simultaneously open file descriptors |
| `errno.ENOENT` | 2 | **No such file or directory** — tried to access a path that does not exist |
| `errno.ENOSPC` | 28 | **No space left on device** — disk is full |

> **Note:** Numeric values differ between operating systems (Windows vs Linux vs macOS).
> Always use the **symbolic constant** (`errno.ENOENT`), never the raw integer.

---

## Practical pattern: branching on errno

```python
import errno

def safe_read(filepath: str) -> str | None:
    """Read a file and return its content, or None on known errors."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except IOError as exc:
        if exc.errno == errno.ENOENT:
            print(f"File not found: {filepath}")
        elif exc.errno == errno.EACCES:
            print(f"Permission denied: {filepath}")
        elif exc.errno == errno.EISDIR:
            print(f"Path is a directory, not a file: {filepath}")
        else:
            print(f"Unexpected IO error [{exc.errno}]: {exc.strerror}")
        return None
```

The `else` branch re-raises (or logs) anything not explicitly handled —
this is the **safe default**. Never silently swallow unknown errors.

---

## PCAP Traps

### Trap 1: `IOError`, `OSError`, `EnvironmentError` are the same class

```python
try:
    open("x.txt")
except OSError as exc:
    print(type(exc))  # <class 'FileNotFoundError'>
```

`FileNotFoundError` is a **subclass** of `OSError`. Catching `OSError` catches it.
Catching `IOError` also catches it. They are all the same parent.

Hierarchy (simplified):
```
BaseException
└── Exception
    └── OSError  (= IOError = EnvironmentError)
        ├── FileNotFoundError   (errno.ENOENT)
        ├── PermissionError     (errno.EACCES)
        ├── FileExistsError     (errno.EEXIST)
        ├── IsADirectoryError   (errno.EISDIR)
        └── BlockingIOError     (errno.EAGAIN)
```

Python 3.3+ introduced these **named subclasses** so you can catch them directly
without checking `errno` at all:

```python
# Modern Python 3.3+ style — preferred
try:
    open("missing.txt")
except FileNotFoundError:
    print("Not found")
except PermissionError:
    print("No access")
```

```python
# Classic style — still valid, required knowledge for PCAP
try:
    open("missing.txt")
except IOError as exc:
    if exc.errno == errno.ENOENT:
        print("Not found")
```

**PCAP tests both styles. Know them both.**

---

### Trap 2: `errno` attribute vs the `errno` module

These are two different things with the same name:

```python
import errno                  # the MODULE with symbolic constants

try:
    open("x.txt")
except IOError as exc:
    print(exc.errno)          # the ATTRIBUTE on the exception (an int)
    print(errno.ENOENT)       # the CONSTANT from the module (also an int)
    print(exc.errno == errno.ENOENT)  # True — this is how you compare
```

---

### Trap 3: `exc.errno` can be `None`

Not every `OSError` subclass sets `errno`. If the exception was raised manually
(e.g., `raise OSError("custom message")`), `exc.errno` is `None`.
Always guard if writing generic handlers:

```python
except IOError as exc:
    if exc.errno is not None and exc.errno == errno.ENOENT:
        ...
```

---

### Trap 4: except ordering with OSError subclasses

The same parent-before-child rule applies here. If you catch `OSError` before
`FileNotFoundError`, the child clause is **never reached**:

```python
# WRONG — FileNotFoundError is never reached
try:
    open("x.txt")
except OSError:
    print("OSError")          # catches FileNotFoundError here
except FileNotFoundError:
    print("FileNotFoundError")  # dead code

# CORRECT
try:
    open("x.txt")
except FileNotFoundError:
    print("FileNotFoundError")  # specific first
except OSError:
    print("OSError")            # generic fallback
```

---

### Trap 5: `open()` with mode `'x'` raises `FileExistsError`

```python
try:
    open("existing.txt", "x")  # exclusive create — fails if file exists
except FileExistsError:
    print("Already exists")    # errno.EEXIST under the hood
```

---

## Quick-reference card

```
errno constant      Named subclass (Py 3.3+)    Cause
─────────────────────────────────────────────────────────────────────────
errno.ENOENT   →  FileNotFoundError          File/dir does not exist
errno.EACCES   →  PermissionError            No read/write permission
errno.EEXIST   →  FileExistsError            File already exists
errno.EISDIR   →  IsADirectoryError          Dir used where file expected
errno.EBADF    →  (no direct subclass)       Operating on closed stream
errno.EFBIG    →  (no direct subclass)       File exceeds OS size limit
errno.EMFILE   →  (no direct subclass)       Too many open file descriptors
errno.ENOSPC   →  (no direct subclass)       Disk full
```

---

## bytearray and binary files

### What is amorphous data?

**Amorphous data** is data with no specific shape or form — just a series of bytes.
It may represent meaningful content (a bitmap image, a compressed archive, a binary
protocol packet) but at the point of reading or writing, you either cannot or do not
need to interpret it as text, numbers, or any other typed structure.

Amorphous data cannot be stored in a string (strings require valid text encoding) or
a plain list (too general, no binary semantics). Python provides a dedicated container
for it: `bytearray`.

---

### bytearray — the container

`bytearray` is a **mutable sequence of bytes**, where each element is an integer in
the range `0–255`.

```python
data = bytearray(10)   # creates 10 bytes, all initialised to zero
print(data)            # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print(len(data))       # 10
```

You can also initialise it with content:

```python
data = bytearray([65, 66, 67])   # from a list of ints
print(data)                       # bytearray(b'ABC')

data = bytearray(b'hello')        # from a bytes literal
```

Individual elements are integers, not characters:

```python
data = bytearray(3)
data[0] = 255
data[1] = 0
data[2] = 128
print(data[0])   # 255  (int, not str)
```

`bytearray` is **mutable** — you can assign to individual indices, unlike `bytes`
which is immutable.

---

### Writing a bytearray to a binary file

Binary files are opened with the `'b'` flag in the mode string (`'wb'`, `'rb'`, `'ab'`).

```python
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i   # fill with values 10, 11, 12, ..., 19

with open('file.bin', 'wb') as bf:
    bytes_written = bf.write(data)

print(bytes_written)   # 10
```

Key points:

- `write()` takes a `bytearray` (or any bytes-like object) and writes it to the file
- `write()` returns the **number of bytes successfully written**
- If the return value differs from `len(data)`, a write error occurred
- The `'wb'` mode creates the file if it doesn't exist, or truncates it if it does

---

### Reading bytes from a binary file with `readinto()`

Binary reading uses `readinto()` — it fills a **pre-existing** `bytearray` rather
than creating a new object.

```python
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bytes_read = bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')   # 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
```

Key points:

- `readinto()` does **not** create a new object — it writes into the bytearray you pass
- It returns the **number of bytes read**
- If the file has more data than the bytearray can hold, reading stops when the array is full
- If the file has fewer bytes than the array, only those bytes are written; the rest
  of the array retains its previous values
- `strerror(e.errno)` from the `os` module converts an errno code to a human-readable
  string — a clean alternative to `exc.strerror`

---

### `os.strerror()` — another way to read errno

The `os` module provides `strerror()` which maps an errno integer to a text description:

```python
import os
import errno

print(os.strerror(errno.ENOENT))   # No such file or directory
print(os.strerror(errno.EACCES))   # Permission denied
print(os.strerror(errno.ENOSPC))   # No space left on device
```

This is equivalent to accessing `exc.strerror` on a caught `IOError`, but can be
called anywhere — useful when you have only the error number and not the exception object.

---

### bytearray vs bytes — when to use which

| | `bytes` | `bytearray` |
|---|---|---|
| Mutable? | No | Yes |
| Created with | `b'...'` literals, `bytes()` | `bytearray()` |
| Use for | Read-only binary data, dict keys | Binary I/O buffers, in-place modification |
| `readinto()` accepts | No | Yes |

---

### PCAP Traps — bytearray and binary I/O

**Trap 1: binary mode requires `'b'` in the mode string**

```python
# WRONG — opens in text mode, write() rejects bytearray
with open('file.bin', 'w') as f:
    f.write(bytearray(10))   # TypeError

# CORRECT
with open('file.bin', 'wb') as f:
    f.write(bytearray(10))   # OK
```

**Trap 2: `readinto()` fills, not creates**

```python
data = bytearray(10)
bf = open('file.bin', 'rb')
n = bf.readinto(data)
# data now contains the bytes read; n tells you how many were actually read
# if n < 10, the file had fewer than 10 bytes — the rest of data is unchanged
```

**Trap 3: elements of bytearray are integers, not characters**

```python
data = bytearray(b'ABC')
print(data[0])          # 65  (not 'A')
print(type(data[0]))    # <class 'int'>
```

**Trap 4: `bytearray(n)` fills with zeros, not garbage**

```python
data = bytearray(5)
print(list(data))   # [0, 0, 0, 0, 0]  — always zeros
```

---

---

## Text vs binary reading — full comparison

This is the section to read before any exam question involving file reading methods.
The split between text streams and binary streams determines which methods you call
and what Python returns.

---

### Side-by-side overview

| | **Text mode** (`'r'`) | **Binary mode** (`'rb'`) |
|---|---|---|
| Stream class | `TextIOWrapper` | `BufferedReader` |
| Unit returned | `str` | `bytes` or fills `bytearray` |
| Newlines | `\r\n` → `\n` (auto) | Raw bytes, no translation |
| `read()` | Returns full file as `str` | Returns full file as `bytes` |
| `read(n)` | Returns next `n` **characters** as `str` | Returns next `n` **bytes** as `bytes` |
| `readline()` | Returns one line as `str` (includes `\n`) | Returns one line as `bytes` (includes `b'\n'`) |
| `readlines()` | Returns `list[str]` | Returns `list[bytes]` |
| `readinto(buf)` | **Not available** | Fills pre-existing `bytearray`, returns count |

---

### Text reading methods

#### `read()` — entire file as one string

```python
with open("notes.txt", "r") as f:
    content = f.read()       # one big str
    print(type(content))     # <class 'str'>
```

#### `read(n)` — next n characters

```python
with open("notes.txt", "r") as f:
    chunk = f.read(5)        # first 5 characters
    rest  = f.read()         # everything after the cursor
```

The file has a **cursor**. Every read advances it. Reading past the end returns `""`.

#### `readline()` — one line at a time

```python
with open("notes.txt", "r") as f:
    line1 = f.readline()     # "hello\n"   ← includes newline
    line2 = f.readline()     # "world\n"
    line3 = f.readline()     # ""          ← empty string = end of file
```

Key rule: `readline()` **includes the `\n`** at the end of each line.
When the file is exhausted, it returns `""` (empty string), NOT `StopIteration`.

#### `readlines()` — all lines as a list

```python
with open("notes.txt", "r") as f:
    lines = f.readlines()    # ['hello\n', 'world\n', 'last line\n']
    print(type(lines))       # <class 'list'>
```

Each element is a `str` and includes its `\n`. Use `.strip()` to remove it:

```python
lines = [line.strip() for line in f.readlines()]
```

#### Iterating directly — the Pythonic way

```python
with open("notes.txt", "r") as f:
    for line in f:           # same as calling readline() repeatedly
        print(line.strip())  # f is its own iterator
```

---

### Binary reading methods

#### `read()` — entire file as `bytes`

```python
with open("file.bin", "rb") as f:
    raw = f.read()           # returns bytes object
    print(type(raw))         # <class 'bytes'>
```

Wrap in `bytearray()` to get a mutable buffer:

```python
with open("file.bin", "rb") as f:
    data = bytearray(f.read())   # mutable copy of all bytes
```

This is the pattern from the PCAP material — `bytearray(bf.read())` reads all bytes
and wraps them in a mutable container in one step.

#### `read(n)` — next n bytes

```python
with open("file.bin", "rb") as f:
    header = f.read(4)       # first 4 bytes as bytes object
    body   = f.read()        # the rest
```

#### `readline()` on binary stream — reads until `b'\n'`

```python
with open("file.bin", "rb") as f:
    line = f.readline()      # reads until b'\n' or EOF
    print(type(line))        # <class 'bytes'>
```

Usually only useful on binary files that happen to be line-delimited. For true
binary data (images, compiled files) use `read(n)` or `readinto()`.

#### `readinto(buffer)` — fill a pre-existing bytearray

```python
from os import strerror

data = bytearray(10)   # pre-allocate exactly how many bytes you want

try:
    with open("file.bin", "rb") as bf:
        n = bf.readinto(data)   # fills data in-place, returns count
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
```

Contrast with `bytearray(f.read())`:

| | `bytearray(f.read())` | `f.readinto(buf)` |
|---|---|---|
| Allocates new object? | Yes — `bytes` then `bytearray` | No — fills existing buffer |
| Memory efficiency | Two copies briefly | One copy |
| Control over size | Reads everything | Reads exactly `len(buf)` bytes |
| Returns | `bytearray` | number of bytes read (int) |

---

### Complete worked example: write then read

```python
from os import strerror

# --- WRITE ---
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i   # values: 10, 11, 12, ..., 19

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# --- READ with readinto() ---
data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()
    for b in data:
        print(hex(b), end=' ')   # 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# --- READ with bytearray(read()) ---
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())  # reads all, wraps in mutable bytearray
    bf.close()
    for b in data:
        print(hex(b), end=' ')   # same output
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
```

---

### PCAP traps — reading methods

**Trap 1: `readline()` includes `\n`, `read()` does not strip anything**

```python
with open("f.txt", "w") as f:
    f.write("abc")          # no newline written

with open("f.txt", "r") as f:
    line = f.readline()     # "abc"  — no \n because none was written
    rest = f.read()         # ""     — cursor is at end, nothing left
```

**Trap 2: `readlines()` returns a list, NOT a string**

```python
lines = open("f.txt").readlines()
print(type(lines))   # <class 'list'>  — not str
```

**Trap 3: `read()` on exhausted stream returns `""` / `b""`, not an error**

```python
with open("f.txt", "r") as f:
    f.read()             # consume everything
    again = f.read()     # "" — no StopIteration, no exception
```

**Trap 4: `readinto()` is binary-only — not available on text streams**

```python
with open("f.txt", "r") as f:
    buf = bytearray(10)
    f.readinto(buf)      # AttributeError — text stream has no readinto
```

**Trap 5: `read(n)` counts characters in text mode, bytes in binary mode**

```python
# "é" is 1 character but 2 bytes in UTF-8
with open("f.txt", "r", encoding="utf-8") as f:
    print(len(f.read(1)))   # 1 — one character

with open("f.txt", "rb") as f:
    print(len(f.read(1)))   # 1 — one byte (may not be a complete character)
```

---

*Next: Apply `errno` knowledge in exception-handling exercises (Week 9 Day 3+).*
