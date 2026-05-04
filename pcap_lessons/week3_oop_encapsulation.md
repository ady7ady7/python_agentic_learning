# Week 3: Encapsulation & Properties

**Learning Objectives:**
- Understand encapsulation and why it matters
- Master name mangling (`_protected`, `__private`)
- Use `@property` for controlled attribute access
- Implement getters, setters, and deleters
- Build the `Trade` class with proper encapsulation

---

## Theory

### 1. What is Encapsulation?

Encapsulation is one of the four pillars of OOP (along with Inheritance, Polymorphism, and Abstraction). It means:

1. **Bundling data and methods** that operate on that data within a class
2. **Controlling access** to internal state (hiding implementation details)
3. **Protecting data integrity** (preventing invalid states)

**Why it matters:**
```python
# WITHOUT encapsulation - anyone can break the object
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(1000)
account.balance = -999999  # Disaster! No validation!
```

```python
# WITH encapsulation - controlled access
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "Protected" - don't touch directly

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount

account = BankAccount(1000)
#account._balance = -999999  # Convention says: don't do this!
account.withdraw(500)  # Proper way - with validation
```

---

### 2. Python's Access Control Conventions

Python doesn't have true private/protected keywords like Java or C++. Instead, it uses **naming conventions**:

| Convention | Meaning | Example |
|------------|---------|---------|
| `name` | Public - use freely | `self.price` |
| `_name` | Protected - internal use, but accessible | `self._balance` |
| `__name` | Private - name mangled, hard to access | `self.__secret` |

#### Public Attributes (no prefix)
```python
class Position:
    def __init__(self, entry_price):
        self.entry_price = entry_price  # Public - anyone can read/write
```

#### Protected Attributes (single underscore `_`)
```python
class Position:
    def __init__(self, entry_price):
        self._entry_price = entry_price  # "Protected" - internal use

# Convention: external code SHOULD NOT access _attributes directly
# But Python doesn't prevent it - it's just a warning to other developers
pos = Position(100)
print(pos._entry_price)  # Works, but you're "breaking the contract"
```

#### Private Attributes (double underscore `__`)
```python
class Position:
    def __init__(self):
        self.__secret_pnl = 0  # Name mangled to _Position__secret_pnl

pos = Position()
# print(pos.__secret_pnl)  # AttributeError! Name doesn't exist as-is
print(pos._Position__secret_pnl)  # Works - but you're really trying hard to break it

#IMPORTANT!!!!
If you'd create an instance variable for a given class instance e.g.

pos = Position()
pos.__random_variable = 3 #THIS IS FULLY PERMISSIBLE AND POSSIBLE BTW!

This __random_variable WOULDN'T BE NAME MANGLED.
You could do print(pos.__random_variable) and get its value!
```

**Name Mangling:** Python transforms `__name` to `_ClassName__name` to prevent accidental access/override in subclasses.



---

### 3. The `@property` Decorator

`@property` allows you to define methods that act like attributes. This gives you:
- **Computed attributes** (calculate value on access)
- **Validation on assignment** (via setters)
- **Backward compatibility** (change implementation without changing interface)

#### Basic Property (Getter Only)
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius of the circle."""
        return self._radius

    @property
    def diameter(self):
        """Computed property - calculated on access."""
        return self._radius * 2

    @property
    def area(self):
        """Another computed property."""
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)    # 5 - accessed like attribute, not radius()
print(c.diameter)  # 10 - computed on the fly
print(c.area)      # 78.54... - computed on the fly

c.radius = 10  # AttributeError! No setter defined - read-only property
```

#### Property with Setter
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

c = Circle(5)
c.radius = 10  # Works - goes through setter
c.radius = -5  # ValueError: Radius must be positive
```

#### Full Property (Getter, Setter, Deleter)
```python
class Position:
    def __init__(self, entry_price):
        self._entry_price = entry_price

    @property
    def entry_price(self):
        """Get the entry price."""
        return self._entry_price

    @entry_price.setter
    def entry_price(self, value):
        """Set entry price with validation."""
        if value <= 0:
            raise ValueError("Entry price must be positive")
        self._entry_price = value

    @entry_price.deleter
    def entry_price(self):
        """Delete entry price (rarely used)."""
        print("Deleting entry price...")
        del self._entry_price

pos = Position(100)
print(pos.entry_price)  # 100 (getter)
pos.entry_price = 150   # (setter)
del pos.entry_price     # (deleter)
```

---

### 4. When to Use Properties

**Use `@property` when:**
1. You need to validate data on assignment
2. You want computed/derived values
3. You need to maintain backward compatibility
4. You want to log/track attribute access

**DON'T use `@property` when:**
1. Simple attribute access is sufficient
2. You're over-engineering (YAGNI - You Ain't Gonna Need It)
3. The computation is expensive (consider caching)

---

### 5. Encapsulation in Practice: Trade Class

Here's how we'll build the `Trade` class with proper encapsulation:

```python
from datetime import datetime
from typing import Optional

class Trade:
    """
    Represents a completed trade with encapsulated PnL calculation.

    Attributes are protected - use properties for controlled access.
    """

    def __init__(
        self,
        ticker: str,
        side: str,
        entry_price: float,
        exit_price: float,
        quantity: float,
        entry_time: datetime,
        exit_time: Optional[datetime] = None
    ):
        self._ticker = ticker
        self._side = side.upper()
        self._entry_price = entry_price
        self._exit_price = exit_price
        self._quantity = quantity
        self._entry_time = entry_time
        self._exit_time = exit_time or datetime.now()

        # Private - calculated once, cached
        self.__pnl: Optional[float] = None

    @property
    def ticker(self) -> str:
        """Read-only ticker symbol."""
        return self._ticker

    @property
    def side(self) -> str:
        """Read-only trade side (BUY/SELL)."""
        return self._side

    @property
    def pnl(self) -> float:
        """
        Calculate and cache PnL.

        Uses lazy evaluation - only calculates once.
        """
        if self.__pnl is None:
            if self._side == "BUY":
                self.__pnl = (self._exit_price - self._entry_price) * self._quantity
            else:
                self.__pnl = (self._entry_price - self._exit_price) * self._quantity
        return self.__pnl

    @property
    def is_winner(self) -> bool:
        """Computed property - True if trade was profitable."""
        return self.pnl > 0

    @property
    def duration(self) -> float:
        """Duration in seconds."""
        return (self._exit_time - self._entry_time).total_seconds()

    def __str__(self) -> str:
        status = "WIN" if self.is_winner else "LOSS"
        return f"{self._side} {self._ticker}: {self.pnl:+.2f} ({status})"

    def __repr__(self) -> str:
        return (f"Trade(ticker='{self._ticker}', side='{self._side}', "
                f"entry={self._entry_price}, exit={self._exit_price}, "
                f"qty={self._quantity})")
```

**Key Design Decisions:**
1. `_ticker`, `_side` etc. are protected - internal use
2. `__pnl` is private - truly hidden, calculated lazily
3. Properties expose controlled read-only access
4. Computed properties (`is_winner`, `duration`) derive from other data
5. PnL is cached - expensive calculation done only once

---

## PCAP Traps & Gotchas

### Trap 1: Name Mangling Confusion
```python
class Parent:
    def __init__(self):
        self.__value = 10  # Becomes _Parent__value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 20  # Becomes _Child__value (different!)

c = Child()
print(c._Parent__value)  # 10 - Parent's private
print(c._Child__value)   # 20 - Child's private
# They're DIFFERENT attributes!
```

### Trap 2: Property vs Method Confusion
```python
class Example:
    @property
    def value(self):
        return 42

e = Example()
print(e.value)    # 42 - Correct! No parentheses
print(e.value())  # TypeError! 42 is not callable
```

### Trap 3: Property Without Setter
```python
class Example:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x

e = Example()
print(e.x)  # 10 - Works
e.x = 20    # AttributeError: can't set attribute (no setter!)
```

### Trap 4: Forgetting to Use Property in Class
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        # BUG: Using _radius directly instead of property
        return 3.14 * self._radius ** 2  # Works, but bypasses any validation

        # Better: Use the property
        return 3.14 * self.radius ** 2
```

### Trap 5: Property Recursion Trap

### The Problem Code
```python
class BadExample:
    def __init__(self, value):
        self.value = value  # Line A

    @property
    def value(self):
        return self.value   # Line B

    @value.setter
    def value(self, new_value):
        self.value = new_value  # Line C
```

### What Happens Step-by-Step

**Step 1:** You call `BadExample(10)`
**Step 2:** Python runs `__init__(self, 10)`
**Step 3:** Line A executes: `self.value = value` (which is `self.value = 10`)
**Step 4:** Python sees `self.value = ...` and thinks: "Is there a setter for `value`?"
**Step 5:** YES! The `@value.setter` exists. Python calls it.
**Step 6:** The setter runs Line C: `self.value = new_value`
**Step 7:** Python sees `self.value = ...` again → calls the setter again
**Step 8:** Infinite loop → RecursionError

### The Key Insight

The **property name** (`value`) and the **storage attribute** must be DIFFERENT:
- Property name: `value` (what users access)
- Storage attribute: `_value` (where data actually lives)

### The Fix
```python
class GoodExample:
    def __init__(self, value):
        self._value = value  # Store in _value (different name!)

    @property
    def value(self):
        return self._value   # Return from _value

    @value.setter
    def value(self, new_value):
        self._value = new_value  # Store in _value
```

Now `self.value = 10` calls the setter, which stores in `self._value` (no recursion).

---

## Exam Tips

**PCAP-31-03 Property Questions:**

1. **Property access syntax:**
   ```python
   obj.property_name  # NOT obj.property_name()
   ```

2. **Setter syntax:**
   ```python
   @property_name.setter
   def property_name(self, value):
       ...
   ```

3. **Name mangling transformation:**
   - `__attr` becomes `_ClassName__attr`
   - Prevents accidental access, not security

4. **Read-only property = no setter defined**

5. **Common error:** `AttributeError: can't set attribute`
   - Means: property exists but has no setter

---

## Quick Reference

| Concept | Syntax | Use Case |
|---------|--------|----------|
| Public | `self.name` | External interface |
| Protected | `self._name` | Internal use (convention) |
| Private | `self.__name` | Prevent subclass conflicts |
| Property (getter) | `@property` | Computed/validated read |
| Property (setter) | `@name.setter` | Validated write |
| Property (deleter) | `@name.deleter` | Cleanup logic |

---

*Next: Week 3 Day 1 tasks will practice these concepts with PCAP drills and building the Trade class.*
