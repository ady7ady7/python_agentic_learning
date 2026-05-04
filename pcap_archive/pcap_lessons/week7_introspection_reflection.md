# Week 7: Introspection & Reflection

---

## PART 1 — What Are These?

**Introspection** — the ability to *examine* an object's type or properties at runtime.
**Reflection** — goes further: the ability to *manipulate* an object's properties and functions at runtime.

Both work on **any** object, regardless of where it came from. You don't need to know the class in advance.

The key insight: in Python, attributes have *names* (strings), and you can work with those names programmatically. That's what makes introspection and reflection possible.

---

## PART 2 — The Core Tools

### `__dict__` — the attribute registry

Every object stores its instance attributes in a dictionary called `__dict__`. The keys are attribute names (strings), the values are the attribute values.

```python
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = "hello"
obj.c = 3.14

print(obj.__dict__)
# {'a': 1, 'b': 'hello', 'c': 3.14}
```

**PCAP trap:** `__dict__` contains *instance* attributes only. Class-level attributes (defined in the class body) live in the *class's* `__dict__`, not the instance's.

```python
class Dog:
    species = "Canis lupus"   # class attribute → Dog.__dict__

    def __init__(self, name):
        self.name = name      # instance attribute → instance.__dict__

d = Dog("Rex")
print(d.__dict__)          # {'name': 'Rex'}   — no 'species'
print(Dog.__dict__)        # {..., 'species': 'Canis lupus', ...}
```

---

### `getattr(obj, name)` — introspection (read)

Retrieves the value of an attribute by its **string name**. Equivalent to `obj.name`, but the name is a variable.

```python
class Point:
    pass

p = Point()
p.x = 10
p.y = 20

attr_name = 'x'
print(getattr(p, attr_name))   # 10
print(p.x)                     # 10 — identical result
```

**With a default** — avoids `AttributeError` if the attribute doesn't exist:

```python
print(getattr(p, 'z', None))   # None — 'z' doesn't exist, no crash
print(getattr(p, 'z'))         # AttributeError — no default given
```

**Why not just use `obj.name`?** Because `name` is a *variable* here — you don't know it at write time. This is introspection: inspecting attributes dynamically.

---

### `setattr(obj, name, value)` — reflection (write)

Sets an attribute by its string name. Equivalent to `obj.name = value`, but the name is a variable.

```python
p = Point()
setattr(p, 'x', 42)
print(p.x)   # 42
```

Creates the attribute if it doesn't exist. Overwrites it if it does.

---

### `hasattr(obj, name)` — introspection (existence check)

Returns `True` if the attribute exists, `False` otherwise. Safer than a `try/except AttributeError`.

```python
print(hasattr(p, 'x'))    # True
print(hasattr(p, 'z'))    # False
```

**PCAP trap:** `hasattr()` uses `getattr()` internally and catches `AttributeError`. So it also returns `True` for methods, properties, and inherited attributes — not just instance attributes.

---

### `delattr(obj, name)` — reflection (delete)

Deletes an attribute by its string name. Equivalent to `del obj.name`.

```python
p.x = 10
delattr(p, 'x')
print(hasattr(p, 'x'))   # False
```

---

### `isinstance(obj, type)` — introspection (type check)

Returns `True` if `obj` is an instance of `type` (or any subclass of it).

```python
print(isinstance(42, int))        # True
print(isinstance(42, float))      # False
print(isinstance(42, (int, str))) # True — accepts a tuple of types
```

**vs `type(obj) == int`:**

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(type(d) == Animal)       # False — exact type only
print(isinstance(d, Animal))   # True  — includes subclasses
```

For PCAP: prefer `isinstance()` when you want to include subclasses. Use `type()` when you need the *exact* type.

---

## PART 3 — The Canonical Example

This is the example from Edube, annotated line by line:

```python
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():       # iterate over attribute names (strings)
        if name.startswith('i'):           # filter: name must start with 'i'
            val = getattr(obj, name)       # introspect: get current value
            if isinstance(val, int):       # introspect: check it's an int
                setattr(obj, name, val + 1)  # reflect: write new value


print(obj.__dict__)
# {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}

incIntsI(obj)

print(obj.__dict__)
# {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 6}
```

**What qualified for increment?**
- `i = 3` → name starts with `i`, value is `int` ✅ → becomes 4
- `ireal = 3.5` → name starts with `i`, but value is `float` ❌ → unchanged
- `integer = 4` → name starts with `i`, value is `int` ✅ → becomes 5
- `a`, `b`, `z` → names don't start with `i` ❌ → not touched

**The power:** `incIntsI()` works on *any* object of *any* class. It doesn't import it, doesn't know its structure in advance. It discovers and manipulates at runtime.

---

## PART 4 — `type()` and `__name__`

```python
print(type(42))           # <class 'int'>
print(type(42).__name__)  # 'int'  — just the string name

class Foo:
    pass

f = Foo()
print(type(f))            # <class '__main__.Foo'>
print(type(f).__name__)   # 'Foo'
```

`type()` with one argument returns the object's type. Useful for introspection when you want the exact class (not including subclasses).

---

## PART 5 — `dir()` — What Does an Object Have?

`dir(obj)` returns a sorted list of all attribute and method names available on an object — including inherited ones.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def fetch(self):
        pass

d = Dog()
print(dir(d))
# [..., 'fetch', 'speak', '__class__', '__dict__', '__init__', ...]
```

**Use case:** Quick discovery of what's available on an unknown object. Not typically used in production code, but invaluable for exploration and debugging.

**PCAP trap:** `dir()` includes *everything* — dunder methods, inherited methods, class attributes, instance attributes. It is NOT the same as `__dict__`.

---

## PART 6 — Practical Patterns

### Pattern 1: Safe attribute access with default

```python
value = getattr(obj, 'price', 0.0)   # returns 0.0 if 'price' doesn't exist
```

### Pattern 2: Dynamic attribute setting from a dictionary

```python
config = {'level': 'DEBUG', 'format': 'json', 'output': 'file'}

class Settings:
    pass

settings = Settings()
for key, value in config.items():
    setattr(settings, key, value)

print(settings.level)   # 'DEBUG'
```

### Pattern 3: Filter and process attributes by type

```python
def get_numeric_attrs(obj) -> dict:
    """Return all attributes whose values are int or float."""
    return {
        name: val
        for name, val in obj.__dict__.items()
        if isinstance(val, (int, float))
    }
```

### Pattern 4: Check before getting

```python
if hasattr(obj, 'stop_loss'):
    sl = getattr(obj, 'stop_loss')
    # use sl safely
```

---

## PART 7 — PCAP Traps

1. **`__dict__` is instance attributes only** — class attributes are in the class's `__dict__`, not the instance's
2. **`getattr(obj, 'x')` raises `AttributeError`** if `x` doesn't exist and no default is given
3. **`getattr(obj, 'x', default)`** never raises — returns default if attribute is missing
4. **`isinstance()` includes subclasses** — `type(obj) == X` does not
5. **`isinstance(obj, (A, B))`** accepts a tuple of types — tests against all of them
6. **`hasattr(obj, name)`** also returns `True` for methods and inherited attributes, not just instance attributes
7. **`dir()` ≠ `__dict__`** — `dir()` includes everything (inherited + dunders); `__dict__` is instance attributes only
8. **`setattr()` creates the attribute** if it doesn't exist — it does not raise
9. **`delattr(obj, name)`** raises `AttributeError` if the attribute doesn't exist
10. **`type(obj).__name__`** gives you the class name as a plain string — useful in formatting and comparisons

---

## Quick Reference

```python
# Introspection — examine
obj.__dict__              # instance attribute dictionary
type(obj)                 # exact type
type(obj).__name__        # type name as string
isinstance(obj, SomeClass)  # is obj an instance of SomeClass (or subclass)?
hasattr(obj, 'name')      # does attribute 'name' exist?
getattr(obj, 'name')      # get attribute by string name (raises if missing)
getattr(obj, 'name', default)  # get with fallback
dir(obj)                  # all available names (attrs + methods + inherited)

# Reflection — manipulate
setattr(obj, 'name', value)   # set attribute by string name
delattr(obj, 'name')          # delete attribute by string name
```
