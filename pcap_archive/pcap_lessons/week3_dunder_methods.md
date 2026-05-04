# Week 3: Dunder (Magic) Methods

Dunder methods (double underscore methods) are special methods that Python calls automatically in certain situations. They let you define how your objects behave with built-in operations.

```python
# "Dunder" = Double UNDERscore
__init__  # Called when creating an object
__str__   # Called by print() and str()
```

---

## Table of Contents

| Method | Purpose | Line |
|--------|---------|------|
| [`__init__`](#__init__---constructor) | Object initialization | ~30 |
| [`__str__`](#__str__---string-representation) | User-friendly string | ~55 |
| [`__repr__`](#__repr__---developer-representation) | Developer/debug string | ~85 |
| [`__len__`](#__len__---length) | `len(obj)` support | ~120 |
| [`__iter__`](#__iter__---iteration) | `for x in obj` support | ~150 |
| [`__eq__`](#__eq__---equality) | `==` comparison | ~185 |
| [`__hash__`](#__hash__---hashing) | `hash(obj)`, set/dict keys | ~220 |
| [`__lt__`, `__gt__`, etc.](#comparison-methods) | `<`, `>`, `<=`, `>=` | ~260 |
| [`__add__`, `__sub__`, etc.](#arithmetic-methods) | `+`, `-`, `*`, `/` | ~295 |
| [`__getitem__`](#__getitem__---indexing) | `obj[key]` access | ~330 |
| [`__contains__`](#__contains__---membership) | `in` operator | ~360 |

---

## `__init__` - Constructor

Called automatically when you create a new object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)  # __init__ called with x=3, y=5
```

**Key points:**
- First parameter is always `self`
- Must NOT return anything (implicitly returns `None`)
- Used to initialize instance attributes

---

## `__str__` - String Representation

Called by `print()`, `str()`, and f-strings. Should return a **user-friendly** string.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point at ({self.x}, {self.y})"

p = Point(3, 5)
print(p)        # Point at (3, 5)
print(str(p))   # Point at (3, 5)
print(f"{p}")   # Point at (3, 5)
```

**Key points:**
- Must return a `str`
- If not defined, Python uses `__repr__` as fallback
- Focus on readability for end users

---

## `__repr__` - Developer Representation

Called by `repr()`, in lists/dicts, and in the REPL. Should return an **unambiguous** string, ideally one that could recreate the object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 5)
print(repr(p))   # Point(x=3, y=5)
print([p])       # [Point(x=3, y=5)]  <- lists use __repr__
print(f"{p!r}")  # Point(x=3, y=5)   <- !r forces __repr__
```

**Key points:**
- Must return a `str`
- Used as fallback if `__str__` not defined
- Convention: return something that looks like valid Python code

**When each is used:**

| Context | Method Called |
|---------|---------------|
| `print(obj)` | `__str__` |
| `str(obj)` | `__str__` |
| `f"{obj}"` | `__str__` |
| `repr(obj)` | `__repr__` |
| `f"{obj!r}"` | `__repr__` |
| `[obj]` (in list) | `__repr__` |

---

## `__len__` - Length

Called by `len()`. Must return a non-negative integer.

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist()
playlist.add("Song A")
playlist.add("Song B")
print(len(playlist))  # 2
```

**Key points:**
- Must return an `int >= 0`
- Makes your object work with `len()`
- Also enables truthiness testing (empty = False, non-empty = True)

---

## `__iter__` - Iteration

Called when you use `for ... in`. Must return an iterator.

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __iter__(self):
        return iter(self.songs)  # Delegate to list's iterator

playlist = Playlist()
playlist.add("Song A")
playlist.add("Song B")

for song in playlist:  # __iter__ called
    print(song)
# Song A
# Song B
```

**Key points:**
- Return `iter(self.some_list)` to delegate to a list
- Or return `self` and implement `__next__` for custom iteration
- Makes your object work in `for` loops

---

## `__eq__` - Equality

Called by `==`. Returns `True` or `False`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

p1 = Point(3, 5)
p2 = Point(3, 5)
p3 = Point(1, 2)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

**Key points:**
- Check `isinstance(other, YourClass)` first
- Return `NotImplemented` (not `False`) if types don't match
- Without `__eq__`, Python compares by identity (`is`)

**PCAP Trap:** Without `__eq__`, two objects with same data are NOT equal:
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

p1 = Point(3, 5)
p2 = Point(3, 5)
print(p1 == p2)  # False! (compares memory addresses)
```

---

## `__hash__` - Hashing

Called by `hash()`. Required for objects to be used as dict keys or in sets.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(3, 5)
p2 = Point(3, 5)

# Can use in sets (duplicates removed)
points = {p1, p2}
print(len(points))  # 1 (p1 and p2 are equal, same hash)

# Can use as dict keys
distances = {p1: 5.83}
print(distances[p2])  # 5.83 (p2 is equal to p1)
```

**Key points:**
- If you define `__eq__`, you SHOULD also define `__hash__`
- Objects that compare equal MUST have the same hash
- Use `hash((attr1, attr2, ...))` to combine multiple attributes
- Mutable objects should NOT be hashable (or be careful)

**PCAP Trap:** If you define `__eq__` but not `__hash__`, your object becomes unhashable:
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p = Point(3, 5)
{p}  # TypeError: unhashable type: 'Point'
```

---

## Comparison Methods

For `<`, `>`, `<=`, `>=` comparisons.

| Method | Operator |
|--------|----------|
| `__lt__(self, other)` | `<` |
| `__le__(self, other)` | `<=` |
| `__gt__(self, other)` | `>` |
| `__ge__(self, other)` | `>=` |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        # Compare by distance from origin
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

p1 = Point(1, 1)
p2 = Point(3, 4)
print(p1 < p2)  # True (1.41 < 5.0)
```

**Tip:** Use `@functools.total_ordering` to auto-generate the others from `__eq__` and `__lt__`.

---

## Arithmetic Methods

For `+`, `-`, `*`, `/` operations.

| Method | Operator |
|--------|----------|
| `__add__(self, other)` | `+` |
| `__sub__(self, other)` | `-` |
| `__mul__(self, other)` | `*` |
| `__truediv__(self, other)` | `/` |
| `__floordiv__(self, other)` | `//` |
| `__mod__(self, other)` | `%` |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Point(4, 6)
```

---

## `__getitem__` - Indexing

Called when you use `obj[key]`.

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist()
playlist.add("Song A")
playlist.add("Song B")
print(playlist[0])   # Song A
print(playlist[-1])  # Song B
```

**Related:**
- `__setitem__(self, key, value)` - for `obj[key] = value`
- `__delitem__(self, key)` - for `del obj[key]`

---

## `__contains__` - Membership

Called by the `in` operator.

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __contains__(self, song):
        return song in self.songs

playlist = Playlist()
playlist.add("Song A")
print("Song A" in playlist)  # True
print("Song X" in playlist)  # False
```

---

## Quick Reference

| Method | Triggered By | Returns |
|--------|--------------|---------|
| `__init__` | `Class()` | `None` |
| `__str__` | `print()`, `str()` | `str` |
| `__repr__` | `repr()`, lists | `str` |
| `__len__` | `len()` | `int` |
| `__iter__` | `for x in obj` | iterator |
| `__eq__` | `==` | `bool` |
| `__hash__` | `hash()`, sets, dicts | `int` |
| `__lt__` | `<` | `bool` |
| `__add__` | `+` | new object |
| `__getitem__` | `obj[key]` | element |
| `__contains__` | `in` | `bool` |

---

## PCAP Traps

1. **`__str__` must return a string** - returning `None` or `int` raises `TypeError`
2. **`__eq__` without `__hash__`** - makes object unhashable (can't use in sets/dicts)
3. **Equal objects must have equal hashes** - if `a == b`, then `hash(a) == hash(b)`
4. **`__repr__` is fallback for `__str__`** - if `__str__` not defined, `print()` uses `__repr__`
5. **Default `__eq__` compares identity** - without custom `__eq__`, `a == b` is like `a is b`
