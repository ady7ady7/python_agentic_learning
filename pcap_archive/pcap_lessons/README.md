# PCAP-31-03 Lessons - Table of Contents

This directory contains all theoretical lessons organized by week and topic.

## Week 1: Foundations

### [Modules, Packages & PIP](week1_modules_packages.md)
- Module vs Package hierarchy
- Import mechanisms (absolute, selective, alias, wildcard)
- sys.path resolution
- pip essentials
- **PCAP Traps:** Circular imports, name shadowing, `__init__.py` execution

### [Strings, Exceptions & File I/O](week1_strings_exceptions.md)
- String operations & slicing
- String methods (find/index, strip, split/join)
- String formatting (%, .format(), f-strings)
- Exception hierarchy and handling
- File I/O with context managers
- **PCAP Traps:** Slicing edge cases, exception order, file handle leaks

### [OOP Fundamentals - Classes & Objects](week1_6_oop_fundamentals.md)
- What are classes and why use them
- The `__init__` constructor method
- Understanding `self` (the object reference)
- Instance attributes vs class attributes
- Methods vs functions
- Practical examples (BankAccount, OHLCCandle)
- **PCAP Traps:** Mutable class attributes, forgetting `self`, `__init__` return values

### [Magic Methods & Pandas Essentials](week1_magic_methods_pandas.md)
- `__str__` vs `__repr__` (user-friendly vs developer-friendly)
- Making objects print nicely
- Series vs DataFrame concepts
- Essential DataFrame operations (accessing, filtering, NaN handling)
- Boolean indexing and iteration
- **PCAP Traps:** Forgetting return in `__str__`, `.any()` semantics, parentheses in filters

### [Pandas Essentials](pandas.md)
- Series vs DataFrame
- Essential DataFrame operations
- Checking for missing values (NaN)
- Filtering rows (Boolean indexing)
- Advanced filtering & optimization patterns
- **PCAP Traps:** `.any()` semantics, parentheses in multiple conditions, return types

---

## Week 2: Advanced OOP

### [Inheritance & Polymorphism](week2_inheritance.md)
- Basic inheritance syntax and "IS-A" relationships
- The `super()` function for calling parent methods
- Method overriding
- Abstract Base Classes (ABC) with `@abstractmethod`
- `isinstance()` and `issubclass()` for type checking
- Method Resolution Order (MRO)
- **Polymorphism** - using objects of different types through the same interface
- Duck typing in Python
- Type-specific behavior with `isinstance()`
- Common inheritance patterns (extending behavior, template method)
- **PCAP Traps:** Forgetting `super().__init__()`, abstract methods not implemented, `isinstance()` vs `type()`, overriding vs overloading, method overloading (not supported in Python)

### [@classmethod and @staticmethod](week2_classmethod_staticmethod.md)
- Regular methods (review) - receive `self`
- `@classmethod` - receives `cls` (the class itself)
- `@staticmethod` - receives nothing automatically
- When to use which (comparison table)
- Alternative constructors with `@classmethod`
- Utility functions with `@staticmethod`
- **PCAP Traps:** Confusing `cls` and `self`, @staticmethod trying to use `cls`, first parameter naming

---

## Week 3: Encapsulation & Core Domain Models

### [Encapsulation & Properties](week3_oop_encapsulation.md)
- What is encapsulation and why it matters
- Access control conventions (`public`, `_protected`, `__private`)
- Name mangling explained
- `@property` decorator (getters, setters, deleters)
- Computed/derived properties
- Building the `Trade` class with proper encapsulation
- **PCAP Traps:** Name mangling confusion, property vs method syntax, read-only properties

### [Useful Standard Library Modules](week3_useful_modules.md)
- **random** - pseudo-random number generation, `choice()`, `sample()`
- **platform** - system/hardware information, execution layers
- **PCAP Traps:** `randint` inclusive vs `randrange` exclusive, `sample()` requires k <= len(seq)

### [Dunder (Magic) Methods](week3_dunder_methods.md)
- `__str__` vs `__repr__` - string representations
- `__len__`, `__iter__` - making objects work with len() and for loops
- `__eq__`, `__hash__` - equality and hashing for sets/dicts
- Comparison methods (`__lt__`, `__gt__`, etc.)
- Arithmetic methods (`__add__`, `__sub__`, etc.)
- `__getitem__`, `__contains__` - indexing and membership
- **PCAP Traps:** `__eq__` without `__hash__`, default identity comparison

### [Generators & Iterators](week3_generators.md)
- What is a generator and why use them
- `yield` vs `return` - the key difference
- Creating generator functions step-by-step
- Generator expressions `(x for x in items)`
- Memory efficiency (generators vs lists)
- Common patterns (filtering, transforming, infinite)
- **PCAP Traps:** Exhausted generators, `StopIteration`, generator vs list

---

## Week 4: Functional Programming & The Backtesting Engine

### [Lambda Functions, Closures & Functional Programming](week4_lambda_closures.md)
- Lambda syntax and rules (single expression only)
- Lambda use cases (sorting keys, quick functions)
- `map()` - apply function to all items
- `filter()` - select items by condition
- Closures - functions that remember their environment
- `nonlocal` keyword for modifying enclosing scope
- Factory functions and data hiding with closures
- `reduce()` from functools - cumulative reduction
- Decorators - closures in action, wrapping functions
- `functools.wraps` - preserving decorated function metadata
- **PCAP Traps:** Lambda can't have statements, late binding in loops, map/filter return iterators

### [pip, Packages & Environment Management](week4_pip_packages.md) *(Reference)*
- Locating Python on your system (Windows `py` launcher, Linux/macOS)
- Python version management and switching
- pip fundamentals (`install`, `uninstall`, `list`, `show`, `freeze`)
- pip flags (`-U`, `-r`, `-e`, `--user`, `--no-cache-dir`, etc.)
- Virtual environments (`venv`) - creation, activation, workflow
- `requirements.txt` format and version specifiers
- Common troubleshooting scenarios
- **PCAP Notes:** Module vs Package distinction, PyPI, pip conceptual questions

---

## Week 5: datetime, File I/O & Decorators

### [Standard Library, File I/O & Logging](week3_5_7_stdlib_fileio.md)
- `datetime` and `time` modules → see [week9_datetime_time_calendar.md](week9_datetime_time_calendar.md)
- File modes: `'w'` (write), `'a'` (append), `'r'` (read), `'x'` (exclusive create)
- File read methods: `read()`, `readline()`, `readlines()`
- Context managers (`with` statement)
- Decorators: simple, with arguments, stacking, `@wraps`
- **Week 7 — `logging` module:** levels (DEBUG/INFO/WARNING/ERROR/CRITICAL), `basicConfig()`, named loggers, handlers, formatters, hierarchy, propagation
- **PCAP Traps:** File cursor position, `%y` vs `%Y`, decorator stacking order, `basicConfig()` one-shot, default WARNING level, `logging` vs `warnings`

---

## Week 6: The Iterator Protocol & Advanced Generators

### [The Iterator Protocol, Advanced Generators & `__new__`](week6_iterators_generators_advanced.md)
- The iterator protocol (`__iter__`, `__next__`)
- Building custom iterable classes
- `iter()` two-argument form, `next()` with default
- The `__new__` method: object creation vs initialization
- Singleton pattern
- `yield from` for generator delegation
- Generator pipelines
- Named tuples (`collections.namedtuple`)
- Generator vs Iterator vs Iterable distinctions
- **PCAP Traps:** `next()` on iterable vs iterator, `__new__` return type, generator exhaustion

---

## Week 7: Standard Library & Logging

### [Introspection & Reflection](week7_introspection_reflection.md)
- Introspection vs Reflection — examine vs manipulate at runtime
- `__dict__` — instance attribute registry (instance vs class `__dict__`)
- `getattr()`, `setattr()`, `hasattr()`, `delattr()` — dynamic attribute access
- `isinstance()` vs `type()` — subclass-aware vs exact type check
- `dir()` — full name discovery (vs `__dict__`)
- Practical patterns: safe access, dynamic config, attribute filtering
- **PCAP Traps:** `__dict__` instance-only, `getattr` default, `isinstance` includes subclasses, `dir` vs `__dict__`

### [Standard Library, datetime, File I/O & Logging](week3_5_7_stdlib_fileio.md) *(see Week 5 entry above — extended)*
- `logging` module fundamentals
- Five log levels: DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
- `basicConfig()`, named loggers, `StreamHandler`, `FileHandler`
- Formatters and format string placeholders
- Logger hierarchy and propagation
- `logging.warning()` vs `warnings.warn()`
- Project integration: adding logging to BacktestEngine
- **PCAP Traps:** default WARNING level, basicConfig one-shot, numeric level values, lazy `%s` formatting

---

## Week 8: Exam Crunch & Documentation

### [Exam Crunch & Documentation](week8_exam_crunch.md)
- PCAP-31-03 exam section map and weights
- Master trap list: scope, raise, exceptions, generators, __name__, OOP, logging, floats, mutability, slicing
- Full dunder method protocol reference
- isinstance vs type — exact vs subclass-aware
- Google-style docstring reference for project finalisation
- PCAP exam technique (time management, elimination strategy)
- **Quick-Reference Card:** all recurring traps in one place

---

## Week 9: Stream Errors & errno

### [`time` vs `datetime` vs `calendar` — Full Reference](week9_datetime_time_calendar.md)
- `time` module: `time()`, `ctime()`, `localtime()`, `gmtime()`, `mktime()`, `strftime()`, `strptime()`, `sleep()`, `perf_counter()`
- `datetime` module: `date`, `time`, `datetime`, `timedelta` classes
- Unix timestamp ↔ datetime conversion (`fromtimestamp`, `.timestamp()`)
- `strftime` (format) vs `strptime` (parse) — mnemonic and examples
- Date arithmetic with `timedelta` — `.days` vs `.total_seconds()`
- Side-by-side comparison: same task in both modules
- `calendar` module: day constants (`MONDAY`–`SUNDAY` = 0–6), `weekday()`, `monthrange()`, `isleap()`, `leapdays()`, `prmonth()`, `prcal()`, `TextCalendar`, `HTMLCalendar`
- **PCAP Traps:** `from datetime import time` shadows the module, `timedelta.seconds` vs `.total_seconds()`, `calendar` constants match `weekday()` not `isoweekday()`, `prcal()` returns `None`

### [File Streams, open() & Diagnosing Errors with errno](week9_errno_fileio.md)
- Files and streams — open before use, close after processing
- Three open modes: read, write, update
- `open()` syntax: `file_name`, `mode`, `encoding`
- `BufferedIOBase` (binary) vs `TextIOBase` (text) stream classes
- Predefined streams: `sys.stdin`, `sys.stdout`, `sys.stderr`
- `IOError.errno` attribute — reading OS error codes from exceptions
- The `errno` module and its symbolic constants
- 8 key constants: `ENOENT`, `EACCES`, `EEXIST`, `EFBIG`, `EISDIR`, `EMFILE`, `EBADF`, `ENOSPC`
- `OSError` / `IOError` / `EnvironmentError` — all aliases in Python 3
- Named subclasses (Python 3.3+): `FileNotFoundError`, `PermissionError`, `FileExistsError`, `IsADirectoryError`
- Branching on `errno` vs catching named subclasses
- `bytearray` — mutable byte sequence for binary I/O buffers
- Writing binary data with `open('f', 'wb')` and `write(bytearray)`
- Reading binary data with `readinto()` — fills existing array, returns bytes read
- `os.strerror()` — converting errno codes to human-readable strings
- `bytearray` vs `bytes` — mutable vs immutable
- **Text vs binary reading — full comparison table**
- Text: `read()`, `read(n)`, `readline()` (includes `\n`), `readlines()` → `list[str]`, iteration
- Binary: `read()` → `bytes`, `bytearray(f.read())`, `read(n)` → n bytes, `readinto(buf)` → fills in-place
- Complete write + readinto + bytearray(read()) worked example
- **PCAP Traps:** `IOError is OSError` (True), `exc.errno` can be `None`, parent-before-child ordering with `OSError` subclasses, `open('x', 'x')` raises `FileExistsError`, forgetting `close()` → `EMFILE`, binary mode requires `'b'` flag, `bytearray` elements are `int` not `str`, `bytearray(n)` fills with zeros, `readline()` includes `\n`, `read()` on exhausted stream returns `""` not error, `readinto()` not available on text streams, `read(n)` counts chars vs bytes depending on mode

---

## Week 10: PCAP Review

### [Mock 1 Gap Closure](gaps_pcap_mock1.md)
- Multiple `except` — at most one runs; first match wins
- Bare `except:` must be last or SyntaxError
- `for line in open(...)` — file objects are iterable, yields lines with `\n`
- `randint` (inclusive both ends) vs `randrange` (stop excluded) vs `choice` (picks from sequence only)
- String escape trap: `'\\\''` is a SyntaxError — string never closed
- `chr()` / `ord()` — character ↔ integer code point (`ord('p')` = 112, `chr(114)` = `'r'`)
- `sys.stderr` → screen by default (not null device)
- `hasattr(Class, attr)` — checks the class, not instances; `self.x` from `__init__` is not on the class
- `__name__` → `'__main__'` when run directly, module name when imported

---

## Week 11: MRO & super() Deep Dive

### [MRO & `super()` — How the Chain Actually Works](week11_mro_super.md)
- Why `super()` means "next in MRO", not "my parent"
- Full step-by-step trace of diamond inheritance `D(B, C)`
- Call order vs return order — why the stack unwinds in reverse
- append (`super().f() + "X"`) vs prepend (`"X" + super().f()`) — different outputs
- `__init__` chain — why A runs once in a diamond (not twice)
- What happens when one class breaks the chain (no `super()` call)
- Linear vs diamond chain comparison
- **PCAP Traps:** `super()` uses MRO of actual object, silent chain break, `ACB` not `ABC`

---

**Navigation Tip:** Use your IDE's file search (Ctrl+P / Cmd+P) to quickly jump to specific lessons!
