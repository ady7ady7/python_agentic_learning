# Week 1, Day 4: Magic Methods & Pandas Essentials

**Learning Objectives:**
- Master `__str__` and `__repr__` for object string representations
- Understand essential Pandas DataFrame operations
- Learn Series vs DataFrame concepts
- Apply professional object representation in trading classes

---

## Part 1: Magic Methods - Making Your Objects Print Nicely

### What Are Magic Methods?

**Magic methods** (also called **dunder methods** - "double underscore") are special methods that Python calls automatically in certain situations.

```python
"""Understanding magic methods."""

class Counter:
    def __init__(self, value: int) -> None:
        self.value = value

    # No __str__ defined yet

counter = Counter(10)
print(counter)  # <__main__.Counter object at 0x7f8b1c3d4e80>
# Ugly! Just prints memory address
```

**The problem:** Without magic methods, printing objects gives you useless memory addresses.

---

## `__str__` vs `__repr__`: User-Friendly vs Developer-Friendly

### `__str__` - For End Users (Human-Readable)

Called by `print()` and `str()`. Should be **readable and friendly**.

```python
"""Using __str__ for user-friendly output."""

class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        """Return user-friendly string representation."""
        return f"Account({self.owner}): ${self.balance:.2f}"


account = BankAccount("Alice", 1500.50)
print(account)  # Account(Alice): $1500.50
# Clean, readable, user-friendly
```

### `__repr__` - For Developers (Unambiguous)

Called by `repr()` and in interactive shell. Should be **unambiguous and ideally recreate the object**.

```python
"""Using __repr__ for developer-friendly output."""

class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def __repr__(self) -> str:
        """Return unambiguous representation (ideally recreates object)."""
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

    def __str__(self) -> str:
        """Return user-friendly representation."""
        return f"Account({self.owner}): ${self.balance:.2f}"


account = BankAccount("Alice", 1500.50)

print(str(account))   # Account(Alice): $1500.50 (calls __str__)
print(repr(account))  # BankAccount(owner='Alice', balance=1500.5) (calls __repr__)
print(account)        # Account(Alice): $1500.50 (print uses __str__)

# In interactive shell:
# >>> account
# BankAccount(owner='Alice', balance=1500.5)  # Uses __repr__
```

**Key Differences:**

| Feature | `__str__` | `__repr__` |
|---------|-----------|------------|
| **Purpose** | User-friendly display | Developer debugging |
| **Called by** | `print()`, `str()` | `repr()`, interactive shell, `f"{obj!r}"` |
| **Goal** | Readable | Unambiguous (ideally recreates object) |
| **Fallback** | Falls back to `__repr__` if not defined | Required (has default) |

---

### Best Practices

1. **Always define `__repr__`** - It's your debugging friend
2. **Define `__str__` for user-facing classes** - Makes output pretty
3. **`__repr__` should ideally allow recreation:**
   ```python
   def __repr__(self) -> str:
       return f"ClassName(arg1={self.arg1!r}, arg2={self.arg2!r})"
   ```
4. **Use `!r` in f-strings for `__repr__` to show strings with quotes:**
   ```python
   name = "Alice"
   f"{name}"   # Alice (no quotes)
   f"{name!r}" # 'Alice' (with quotes - unambiguous)
   ```

---

### Practical Example: Position Class

```python
"""Professional Position class with string representations."""

from typing import Optional


class Position:
    """Represents a trading position."""

    def __init__(
        self,
        ticker: str,
        side: str,
        entry_price: float,
        quantity: float,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> None:
        self.ticker = ticker
        self.side = side.upper()
        self.entry_price = entry_price
        self.quantity = quantity
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def __repr__(self) -> str:
        """Unambiguous representation for debugging."""
        return (
            f"Position(ticker={self.ticker!r}, side={self.side!r}, "
            f"entry_price={self.entry_price}, quantity={self.quantity}, "
            f"stop_loss={self.stop_loss}, take_profit={self.take_profit})"
        )

    def __str__(self) -> str:
        """User-friendly representation."""
        sl_str = f"SL={self.stop_loss:.2f}" if self.stop_loss else "No SL"
        tp_str = f"TP={self.take_profit:.2f}" if self.take_profit else "No TP"
        return (
            f"{self.side} {self.quantity} {self.ticker} @ {self.entry_price:.2f} "
            f"[{sl_str}, {tp_str}]"
        )


# Usage
position = Position("EURUSD", "BUY", 1.0850, 10000, stop_loss=1.0800, take_profit=1.0950)

print(position)
# BUY 10000 EURUSD @ 1.09 [SL=1.08, TP=1.10]

print(repr(position))
# Position(ticker='EURUSD', side='BUY', entry_price=1.085, quantity=10000, stop_loss=1.08, take_profit=1.095)
```

---

## PCAP Traps with Magic Methods

**Trap 1: Forgetting return values**

```python
class Broken:
    def __str__(self):
        print("Hello")  # WRONG - prints instead of returning
        # Returns None implicitly


obj = Broken()
print(obj)  # None (because __str__ returned None)
```

**Fix:** Always `return` a string

```python
class Fixed:
    def __str__(self) -> str:
        return "Hello"  # ✅ Returns string


obj = Fixed()
print(obj)  # Hello
```

---

**Trap 2: Circular references in `__repr__`**

```python
class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner

    def __repr__(self) -> str:
        return f"Account: {self}"  # Calls __repr__ again! Infinite loop!
```

**Fix:** Don't call `str()` or `repr()` on `self` inside magic methods

---
**Next Steps:**
Now you can make your Position and Trade classes print beautifully, and you understand the Pandas operations you've been using!

**Magic Methods - EXAM TIPS:**
- `__str__` must return a string (not print!)
- `__repr__` is for debugging, `__str__` is for users
- If only `__repr__` defined, it's used for both
- Don't reference `self` inside `__repr__` (infinite loop)
