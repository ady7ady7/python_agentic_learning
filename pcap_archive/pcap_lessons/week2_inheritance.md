# Week 2: Advanced OOP - Inheritance

## What is Inheritance?

**Inheritance** allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). This enables code reuse and establishes a hierarchical relationship between classes.

**Key concept:** "IS-A" relationship
- A `Dog` IS-A `Animal`
- A `SavingsAccount` IS-A `BankAccount`
- A `LevelCrossStrategy` IS-A `Strategy`

---

## Basic Inheritance Syntax

```python
"""Basic inheritance example."""

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self) -> str:  # Override parent method
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Usage
dog = Dog("Buddy")
print(dog.name)  # Inherited attribute: "Buddy"
print(dog.speak())  # Overridden method: "Woof!"

cat = Cat("Whiskers")
print(cat.speak())  # "Meow!"
```

**Key points:**
- `Dog(Animal)` means Dog inherits from Animal
- Child class can **override** parent methods
- Child class inherits parent's `__init__` if not overridden

---

## The `super()` Function

`super()` calls methods from the parent class. Most commonly used in `__init__` to initialize parent attributes.

```python
"""Using super() to call parent __init__."""

class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def info(self) -> str:
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)  # Call parent __init__
        self.doors = doors  # Add child-specific attribute

    def info(self) -> str:
        parent_info = super().info()  # Call parent method
        return f"{parent_info} with {self.doors} doors"

car = Car("Toyota", 2023, 4)
print(car.brand)  # "Toyota" (from parent)
print(car.doors)  # 4 (child attribute)
print(car.info())  # "2023 Toyota with 4 doors"
```

**Why use `super()`?**
- Avoids hardcoding parent class name
- Required for multiple inheritance (Week 3 topic)
- Best practice for calling parent methods

---

## Method Overriding

Child classes can **override** (replace) parent methods with their own implementation.

```python
"""Method overriding example."""

class Shape:
    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        return 0.0  # Default implementation

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:  # Override parent method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:  # Override parent method
        return 3.14159 * self.radius ** 2

rect = Rectangle(5, 3)
print(rect.area())  # 15 (overridden method)

circle = Circle(4)
print(circle.area())  # 50.26536 (overridden method)
```

**Rules:**
- Method signature must match (same name, can have different parameters)
- Child method completely replaces parent method
- Use `super().method()` if you want to EXTEND parent behavior, not replace

---

## Abstract Base Classes (ABC)

An **Abstract Base Class** defines a blueprint that child classes MUST implement. Use `abc` module.

```python
"""Abstract Base Class example."""

from abc import ABC, abstractmethod

class Strategy(ABC):  # Inherit from ABC
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_signal(self, price: float) -> str:
        """Child classes MUST implement this."""
        pass  # No implementation in parent

class LevelCrossStrategy(Strategy):
    def __init__(self, level: float):
        super().__init__("Level Cross")
        self.level = level

    def calculate_signal(self, price: float) -> str:
        """REQUIRED implementation."""
        if price > self.level:
            return "BUY"
        elif price < self.level:
            return "SELL"
        return "HOLD"

# Cannot instantiate abstract class:
# s = Strategy("Test")  # TypeError!

# Can instantiate child that implements abstract methods:
strategy = LevelCrossStrategy(100.0)
print(strategy.calculate_signal(105))  # "BUY"
```

**Why use ABC?**
- **Enforce contracts:** Child classes MUST implement abstract methods
- **Catch errors early:** TypeError at instantiation, not runtime
- **Design clarity:** Clearly signals which methods are required

---

## `isinstance()` and `issubclass()`

Check inheritance relationships at runtime.

```python
"""Type checking with isinstance() and issubclass()."""

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()

# isinstance(object, Class) - checks if object is instance of Class
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True (Dog is subclass of Animal)
print(isinstance(dog, Cat))  # False

# issubclass(ChildClass, ParentClass) - checks class hierarchy
print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, Dog))  # True (class is subclass of itself)
print(issubclass(Animal, Dog))  # False
print(issubclass(Dog, Cat))  # False
```

**PCAP traps:**
- `isinstance(obj, Class)` - object vs class
- `issubclass(Child, Parent)` - class vs class
- Every class is a subclass of itself

---

## Method Resolution Order (MRO)

Python searches for methods in a specific order: **Child → Parent → Grandparent**.

```python
"""Method Resolution Order example."""

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(B):
    pass  # Doesn't override method

obj = C()
print(obj.method())  # "B" (finds method in parent B first)

# Check MRO
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

**Key rule:** Python looks for methods from LEFT to RIGHT, BOTTOM to TOP.

---

### Multiple Inheritance and C3 Linearization

**CRITICAL PCAP TRAP:** When a class inherits from multiple parents, Python uses **C3 Linearization** to determine MRO. The order of parents in the class definition matters!

#### The Diamond Problem

```python
"""Multiple inheritance - the diamond problem."""

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # D inherits from BOTH B and C
    pass

# Which method does D use?
obj = D()
print(obj.method())  # "B" (NOT "C"!)
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

**Why "B" and not "C"?**

In `class D(B, C)`, the **leftmost parent has priority**. Python's MRO follows these rules:

1. **Left-to-right order:** Parents listed first come first in MRO
2. **Depth-first, left-to-right:** Visit leftmost parent tree completely before right parents
3. **Preserve monotonicity:** No class appears before its parent

**MRO Order:** D → B → C → A → object

**COMMON MISTAKE:** Thinking the "last written" class or "rightmost" parent takes precedence. **THIS IS WRONG!**

---

#### Visualizing the Diamond

```
        A
       / \
      B   C
       \ /
        D
```

When `D` calls `method()`, Python searches:
1. Check `D` (not found)
2. Check `B` (found! returns "B")
3. (Never reaches C because B had the method)

---

#### Practical Example: PCAP Exam Trap

```python
"""PCAP trap - predict the output."""

class Animal:
    def speak(self):
        return "generic sound"

class Mammal(Animal):
    def speak(self):
        return "mammal sound"

class Bird(Animal):
    def speak(self):
        return "chirp"

class Bat(Mammal, Bird):  # Leftmost = Mammal
    pass

class Platypus(Bird, Mammal):  # Leftmost = Bird
    pass

bat = Bat()
platypus = Platypus()

print(bat.speak())       # "mammal sound" (Mammal is leftmost)
print(platypus.speak())  # "chirp" (Bird is leftmost)

# Check MRO
print(Bat.__mro__)
# (Bat, Mammal, Bird, Animal, object)

print(Platypus.__mro__)
# (Platypus, Bird, Mammal, Animal, object)
```

**Key Insight:** **The order you list parent classes determines priority!**

---

#### How to Check MRO

```python
"""Always use __mro__ or .mro() to verify."""

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Method 1: __mro__ attribute (tuple)
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# Method 2: .mro() method (list)
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

#### PCAP Exam Questions About MRO

**Type 1: "What is the output?"**
```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C):
    pass

print(D().method())  # What prints?
```

**Answer:** `"B"` (leftmost parent B is checked first)

---

**Type 2: "What is the MRO?"**
```python
class X: pass
class Y(X): pass
class Z(X): pass
class W(Y, Z): pass

print(W.__mro__)  # Predict the order
```

**Answer:** `(W, Y, Z, X, object)` (W → leftmost Y → then Z → common parent X)

---

**Type 3: "Will this raise an error?"**
```python
class A:
    pass

class B(A):
    pass

class C(A, B):  # Try to inherit from A before B (but B inherits from A!)
    pass
```

**Answer:** `TypeError: Cannot create a consistent method resolution order (MRO)`

**Why?** Python can't satisfy "A before B" (from `A, B` order) AND "B before A" (from B's inheritance). This violates monotonicity.

---

#### C3 Linearization Rules (Summary)

1. **Children before parents:** A class always comes before its parents in MRO
2. **Left-to-right:** Parents are visited in the order they're listed
3. **Parents only once:** Each class appears exactly once in MRO
4. **Preserve order from all parents:** If B comes before C in one parent's MRO, B must come before C in child's MRO

**For PCAP:** Remember the simple rule: **In `class D(B, C)`, B has priority over C (leftmost wins).**

---

#### When to Use Multiple Inheritance

**✅ Good use cases:**
- Mixins (small classes that add specific functionality)
- Interface implementation (like Java interfaces)
- Combining unrelated behaviors

**❌ Avoid when:**
- Creates confusing MRO
- Diamond inheritance with complex logic
- Can be solved with composition instead

**Python philosophy:** "Explicit is better than implicit." If MRO is confusing, use composition.

---

## Common Inheritance Patterns

### 1. Extending Parent Behavior (not replacing)

```python
"""Extend parent method with super()."""

class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message: str) -> None:
        super().log(message)  # Call parent first
        print(f"[TIMESTAMP] 2026-01-12 13:30:00")  # Add extra behavior

logger = TimestampLogger()
logger.log("User logged in")
# Output:
# [LOG] User logged in
# [TIMESTAMP] 2026-01-12 13:30:00
```

### 2. Template Method Pattern

Parent defines algorithm structure, children fill in details.

```python
"""Template method pattern."""

class DataProcessor(ABC):
    def process(self, data: list) -> list:
        """Template method - defines algorithm structure."""
        data = self.load(data)
        data = self.transform(data)
        data = self.save(data)
        return data

    @abstractmethod
    def load(self, data: list) -> list:
        pass

    @abstractmethod
    def transform(self, data: list) -> list:
        pass

    @abstractmethod
    def save(self, data: list) -> list:
        pass

class CSVProcessor(DataProcessor):
    def load(self, data: list) -> list:
        print("Loading CSV...")
        return data

    def transform(self, data: list) -> list:
        print("Transforming CSV...")
        return [x.upper() for x in data]

    def save(self, data: list) -> list:
        print("Saving CSV...")
        return data

processor = CSVProcessor()
result = processor.process(["a", "b", "c"])
# Loading CSV...
# Transforming CSV...
# Saving CSV...
```

---

## PCAP Traps & Common Mistakes

### Trap 1: Forgetting `super().__init__()`

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        # BUG: Forgot super().__init__(x)
        self.y = y

c = Child(10, 20)
print(c.x)  # AttributeError! self.x was never set
```

**Fix:** Always call `super().__init__()` if parent has `__init__`.

### Trap 2: Overriding vs Overloading

Python doesn't support **method overloading** (multiple methods with same name, different signatures).

```python
class Test:
    def method(self, x):
        return x

    def method(self, x, y):  # This REPLACES the first method!
        return x + y

t = Test()
t.method(5)  # TypeError! method() requires 2 arguments
```

**Python behavior:** Last method definition wins.

### Trap 3: `isinstance()` vs `type()`

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(type(dog) == Dog)  # True
print(type(dog) == Animal)  # False (type is exact match)

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True (considers inheritance)
```

**Rule:** Use `isinstance()` for inheritance-aware checks, `type()` for exact type match.

### Trap 4: Abstract method not implemented

```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def required_method(self):
        pass

class Child(Base):
    pass  # Forgot to implement required_method

c = Child()  # TypeError: Can't instantiate abstract class Child
```

**Rule:** ALL abstract methods must be implemented by child classes.

---

## Polymorphism

**Polymorphism** means "many forms" - the ability to use objects of different types through the same interface. In Python, polymorphism allows you to treat different objects uniformly if they share a common interface (methods with the same name).

### What is Polymorphism?

```python
"""Polymorphism allows different objects to be used interchangeably."""

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action - same interface, different implementations
shapes = [Rectangle(5, 3), Circle(2), Rectangle(4, 4)]

# We can call .area() on ANY shape without knowing its exact type
total_area = sum(shape.area() for shape in shapes)
print(total_area)  # 44.56636
```

**Key concept:** The `area()` method behaves differently for Rectangle vs Circle, but we can use them interchangeably because they share the same interface.

---

### Duck Typing - Python's Polymorphism

Python uses **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck."

You don't need inheritance for polymorphism in Python - objects just need to have the right methods.

```python
"""Duck typing - polymorphism without inheritance."""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Car:
    def speak(self):
        return "Beep beep!"

# No common parent class, but all have speak() method
def make_it_speak(thing):
    """This function works with ANY object that has a speak() method."""
    return thing.speak()

print(make_it_speak(Dog()))  # "Woof!"
print(make_it_speak(Cat()))  # "Meow!"
print(make_it_speak(Car()))  # "Beep beep!"
```

**Advantage:** Flexible and Pythonic.
**Disadvantage:** No compile-time type checking (can fail at runtime if object doesn't have the method).

---

### Polymorphism with Abstract Base Classes

ABCs enforce a contract - all children MUST implement the interface.

```python
"""Using ABC to ensure polymorphism works correctly."""

from abc import ABC, abstractmethod

class Strategy(ABC):
    """All strategies must implement generate_signal."""

    @abstractmethod
    def generate_signal(self, price: float) -> str:
        pass

class LevelCrossStrategy(Strategy):
    def __init__(self, level: float):
        self.level = level

    def generate_signal(self, price: float) -> str:
        if price > self.level:
            return "BUY"
        elif price < self.level:
            return "SELL"
        return "HOLD"

class MovingAverageStrategy(Strategy):
    def __init__(self, period: int):
        self.period = period
        self.prices = []

    def generate_signal(self, price: float) -> str:
        self.prices.append(price)
        if len(self.prices) < self.period:
            return "HOLD"
        ma = sum(self.prices[-self.period:]) / self.period
        return "BUY" if price > ma else "SELL" if price < ma else "HOLD"

# Polymorphism - function works with ANY Strategy
def test_strategy(strategy: Strategy, prices: list[float]) -> None:
    """Test any strategy - polymorphism in action."""
    for price in prices:
        signal = strategy.generate_signal(price)
        print(f"Price {price}: {signal}")

# Different strategies, same interface
strat1 = LevelCrossStrategy(100.0)
strat2 = MovingAverageStrategy(3)

test_strategy(strat1, [95, 100, 105])
test_strategy(strat2, [95, 100, 105])
```

**Benefits:**
- **Type safety:** ABC ensures all strategies implement `generate_signal()`
- **Documentation:** ABC makes the interface explicit
- **IDE support:** Better autocomplete and type hints

---

### Polymorphism Example: Payment Processing

```python
"""Real-world polymorphism example - payment methods."""

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float) -> bool:
        print(f"Charging ${amount} to card {self.card_number[-4:]}")
        return True

class PayPal(PaymentMethod):
    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal ({self.email})")
        return True

class BankTransfer(PaymentMethod):
    def __init__(self, account: str):
        self.account = account

    def process_payment(self, amount: float) -> bool:
        print(f"Transferring ${amount} from account {self.account}")
        return True

# Checkout function doesn't care WHICH payment method - polymorphism!
def checkout(payment_method: PaymentMethod, total: float) -> None:
    """Process checkout with any payment method."""
    print(f"Total: ${total}")
    if payment_method.process_payment(total):
        print("Payment successful!\n")

# All payment methods work the same way
checkout(CreditCard("1234-5678-9012-3456"), 99.99)
checkout(PayPal("user@example.com"), 49.99)
checkout(BankTransfer("ACC-12345"), 199.99)
```

---

### Type Checking with isinstance()

Sometimes you need to know the exact type of an object for polymorphism to work correctly.

```python
"""Using isinstance() to handle different types."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def fetch(self):
        return "Fetching ball..."

class Cat(Animal):
    def speak(self):
        return "Meow!"

    def scratch(self):
        return "Scratching post..."

def interact_with_animal(animal: Animal) -> None:
    """Interact with animal - uses polymorphism + type checking."""
    # Polymorphism - works for ALL animals
    print(animal.speak())

    # Type-specific behavior
    if isinstance(animal, Dog):
        print(animal.fetch())
    elif isinstance(animal, Cat):
        print(animal.scratch())

dog = Dog()
cat = Cat()

interact_with_animal(dog)  # Woof! Fetching ball...
interact_with_animal(cat)  # Meow! Scratching post...
```

**When to use isinstance():**
- ✅ When different types need different additional behavior
- ✅ When handling edge cases for specific types
- ❌ Don't overuse - defeats the purpose of polymorphism

---

### PCAP Trap: Polymorphism vs Overloading

**Python does NOT support method overloading** (multiple methods with same name, different parameters).

```python
class Calculator:
    def add(self, a):
        return a + 10

    def add(self, a, b):  # This REPLACES the first add!
        return a + b

calc = Calculator()
calc.add(5)  # TypeError! add() requires 2 arguments
```

**Python behavior:** Last method definition wins.

**Solution:** Use default parameters or `*args`:
```python
class Calculator:
    def add(self, a, b=0):  # Default parameter
        return a + b

    # OR
    def add_all(self, *args):
        return sum(args)

calc = Calculator()
calc.add(5)      # 5 (uses default b=0)
calc.add(5, 3)   # 8
calc.add_all(1, 2, 3, 4)  # 10
```

---

## When to Use Inheritance

**✅ Good use cases:**
- Clear "IS-A" relationship (Dog IS-A Animal)
- Shared behavior across multiple classes
- Template method pattern
- **Polymorphism** - using different objects through same interface

**❌ Bad use cases:**
- "HAS-A" relationship (use composition instead: Car HAS-A Engine)
- Single-use inheritance (just use one class)
- Deep inheritance hierarchies (>3 levels gets messy)

**Alternative: Composition over Inheritance**
```python
# BAD: Inheritance for HAS-A
class Car(Engine):  # Car IS-A Engine? No!
    pass

# GOOD: Composition for HAS-A
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
```

---

## Quick Reference

```python
# Basic inheritance
class Child(Parent):
    pass

# Call parent __init__
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

# Override method
class Child(Parent):
    def method(self):
        return "Child implementation"

# Extend parent method
class Child(Parent):
    def method(self):
        result = super().method()  # Call parent first
        return result + " extended"

# Abstract Base Class
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def required_method(self):
        pass

# Type checking
isinstance(obj, Class)  # Object is instance of Class?
issubclass(Child, Parent)  # Child inherits from Parent?
```

---

## Exam Tips

**Inheritance:**
- `super()` calls parent class methods
- Child can override parent methods
- `isinstance(obj, Class)` checks if obj is instance of Class (inheritance-aware)
- `issubclass(A, B)` checks if A inherits from B
- Abstract methods MUST be implemented by child classes
- MRO: Python searches Child → Parent → Grandparent
- Every class inherits from `object` (implicit)

**Polymorphism:**
- Objects of different types can be used through the same interface
- Duck typing: "If it has the method, you can call it"
- Use ABCs to enforce polymorphic contracts
- `isinstance()` for type-specific behavior within polymorphic functions
- Python does NOT support method overloading (last definition wins)
- Polymorphism enables flexible, reusable code

**Common PCAP questions:**
- "What is the output?" with inheritance hierarchies
- "Which method is called?" (MRO questions)
- "Can you instantiate this class?" (abstract class questions)
- "`isinstance()` vs `type()`" traps
- "What is polymorphism?" (definition and examples)
- "Does this demonstrate polymorphism?" (code analysis)

---
