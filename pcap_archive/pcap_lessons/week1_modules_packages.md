# PCAP-31-03 Lessons Archive

---

## Week 1: Modules, Packages & PIP

**Learning Objectives:**
- Understand the module/package hierarchy in Python
- Master import mechanisms (import, from...import, as)
- Navigate sys.path and package resolution
- Use pip for dependency management
- Recognize namespace collision traps

### Theory

**1. Modules vs Packages:**
- **Module**: A single `.py` file containing Python code
- **Package**: A directory containing `__init__.py` + multiple modules
- **Namespace Package** (PEP 420): Directories without `__init__.py` (Python 3.3+)

**2. Import Mechanisms:**

```python
"""Demonstration of Python import mechanisms."""

# Absolute Import (Most Explicit)
import math
print(math.sqrt(16))  # 4.0

# Selective Import (Import only what you need)
from math import sqrt, pi
print(sqrt(16))  # 4.0

# Alias Import (Industry standard for common libraries)
import numpy as np  # Convention: np for NumPy
import pandas as pd  # Convention: pd for Pandas
from collections import Counter as C

# Wildcard Import (AVOID in production! PEP 8 discourages this)
from math import *  # Pollutes namespace, unclear dependencies
```

**PEP 8 Best Practice:** Use absolute imports. Avoid wildcards except in interactive sessions.

**3. sys.path Resolution:**
Python searches for modules in this order:
1. Current directory
2. PYTHONPATH environment variable
3. Standard library directories
4. Site-packages (pip installs)

```python
import sys
print(sys.path)  # View search paths
```

**4. Package Structure:**
```
my_package/
├── __init__.py      # Makes it a package (can be empty or contain initialization)
├── module_a.py      # Regular module
└── subpackage/
    ├── __init__.py
    └── module_b.py
```

**Example `__init__.py`:**
```python
"""My Package - A professional Python package."""

__version__ = "1.0.0"
__author__ = "Your Name"

# Optionally expose key functions at package level
from .module_a import key_function  # Relative import within package
```

**Importing from packages:**
```python
"""Example of importing from a package structure."""

from my_package import module_a  # Import module
from my_package.subpackage import module_b  # Import from subpackage
from my_package import key_function  # Import exposed function
```

**5. pip Essentials:**
```bash
pip install pandas          # Install
pip install pandas==2.0.0   # Specific version
pip freeze > requirements.txt  # Export dependencies
pip install -r requirements.txt  # Install from file
```

---

### PCAP TRAPS & GOTCHAS

**Trap 1: Circular Imports**
```python
# module_a.py
"""Module A with circular dependency issue."""

from module_b import func_b


def func_a() -> str:
    """Function that depends on module_b."""
    return func_b()


# module_b.py
"""Module B with circular dependency issue."""

from module_a import func_a  # ERROR! Circular dependency


def func_b() -> str:
    """Function that depends on module_a."""
    return func_a()
```

**Solutions:**
1. **Restructure:** Move shared logic to a third module
2. **Lazy Import:** Import inside the function
```python
def func_a() -> str:
    """Lazy import to break circular dependency."""
    from module_b import func_b  # Import at runtime, not module load
    return func_b()
```
3. **Type Hints Only:** Use `from __future__ import annotations` (Python 3.7+)

---

**Trap 2: Shared Mutable State in `__init__.py`**
```python
# __init__.py
"""Package with shared mutable state - DANGEROUS!"""

cache = []  # WARNING: Shared across ALL imports!


# module_a.py
"""Module A modifying shared state."""

from my_package import cache

cache.append(1)  # Modifies the shared list


# module_b.py
"""Module B observing shared state."""

from my_package import cache

print(cache)  # [1] - Surprise! State from module_a persists
```

**Best Practice:** Avoid mutable globals. Use proper state management patterns (Singleton, dependency injection) or configuration objects.

---

**Trap 3: Name Shadowing (Module Name Collision)**
```python
# BAD: Naming your file "random.py" in your project
# random.py
"""Custom random utilities - SHADOWS stdlib module!"""


def my_func() -> None:
    """Some custom function."""
    pass


# main.py
"""Main script that tries to use stdlib random."""

import random  # Imports YOUR random.py from current directory, not stdlib!

print(random.randint(1, 10))  # AttributeError: module has no attribute 'randint'
```

**PEP 8 Warning:** Never name your modules after standard library modules (`random`, `string`, `math`, `sys`, etc.). This shadows stdlib and breaks imports.

**Fix:** Rename your module to something descriptive like `custom_random_utils.py`

---

### Namespace Coexistence (Important Concept!)

While Trap 3 shows what happens when you **shadow** a module name, here's the key insight: **your namespace and a module's namespace can coexist perfectly** when you use `import module` (not `from module import *`).

**Example 1: Your functions vs module functions**
```python
"""Your namespace and math's namespace coexist without conflict."""

import math


def sin(x):
    """Your custom sin function - lives in YOUR namespace."""
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14  # Your pi - lives in YOUR namespace

print(sin(pi / 2))           # 0.99999999 - calls YOUR sin with YOUR pi
print(math.sin(math.pi / 2)) # 1.0 - calls math's sin with math's pi
```

**Why this works:**
- `sin` and `pi` exist in **your module's namespace**
- `math.sin` and `math.pi` exist in **math's namespace** (accessed via `math.`)
- No collision because they're in separate namespaces!

**Example 2: Same name, different namespaces**
```python
"""Demonstrating how import keeps namespaces separate."""

import random

random_number = 42  # Your variable named 'random_number'
random_list = [1, 2, 3]  # Your variable named 'random_list'

# No conflict! 'random' is the module, your variables are separate
print(random.choice(random_list))  # Uses module's choice() on your list
print(random_number)               # Your variable, untouched


```

**Key Takeaway:**
- `import math` → Access via `math.sin`, `math.pi` (namespaced)
- `from math import sin, pi` → Brings `sin`, `pi` directly into YOUR namespace (can cause collisions!)
- `from math import *` → **DANGEROUS** - imports everything, high collision risk

**PCAP Exam Tip:** When you see `import module`, the module's contents are accessed via `module.name`. When you see `from module import name`, `name` is now directly in your namespace and can shadow your own definitions.

**Example 3: Order matters with selective imports (PCAP TRAP!)**
```python
"""Selective import gets overwritten by later definitions."""

from math import sin, pi

print(sin(pi / 2))  # 1.0 - uses math.sin and math.pi

pi = 3.14  # Overwrites imported pi


def sin(x):  # Overwrites imported sin
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))  # 0.99999999 - uses YOUR sin and YOUR pi

# Output:
# 1.0
# 0.99999999
```

**Why this happens:**
1. `from math import sin, pi` → Brings `sin` and `pi` into YOUR namespace
2. First `print(sin(pi / 2))` → Uses imported `sin` and `pi` (math's versions)
3. `pi = 3.14` → **Overwrites** the imported `pi` with your value
4. `def sin(x):` → **Overwrites** the imported `sin` with your function
5. Second `print(sin(pi / 2))` → Uses YOUR `sin` and YOUR `pi`

**Critical insight:** With `from module import name`, the imported names live in YOUR namespace. Any later assignment to those names **replaces** them - Python doesn't know or care that they came from an import.

**Contrast with `import module`:** If you used `import math`, then `math.sin` and `math.pi` would remain untouched regardless of what you define, because they're in a separate namespace.

**Example 4: Aliased imports (PCAP Exam Favorite!)**
```python
"""Aliased imports - original names become inaccessible."""

from math import pi as PI, sin as sine

print(sine(PI / 2))  # 1.0 - works with aliases
print(sin(PI / 2))   # NameError! 'sin' doesn't exist
print(pi)            # NameError! 'pi' doesn't exist
```

**Two key rules:**
1. **Original names become inaccessible:** After `from math import pi as PI`, only `PI` exists in your namespace - `pi` is NOT defined. Using the original name raises `NameError`.
2. **Multiple aliases in one import:** You can alias multiple items in a single import statement using commas: `from math import pi as PI, sin as sine, cos as cosine`

**General syntax:**
```python
from module import name as alias
from module import name1 as alias1, name2 as alias2, name3 as alias3
```

**Same rule applies to module aliases:**
```python
import math as m

print(m.pi)     # 3.14159... - works
print(math.pi)  # NameError! 'math' doesn't exist after aliasing
```

**PCAP Trap:** The exam loves to test whether you know that the original name is gone after aliasing. If you see `import X as Y` followed by code using `X`, it's a `NameError`.

---

**Trap 4: `__init__.py` Execution Behavior**
```python
# __init__.py
"""Package initialization code runs ONCE on first import."""

print("Package initialized!")  # Runs on FIRST import only


# main.py
"""Demonstrating __init__.py execution behavior."""

import my_package  # Prints "Package initialized!"
import my_package  # (Silent - module already in sys.modules cache)
```

**Key Concept:** Python caches imported modules in `sys.modules`. The `__init__.py` executes only once, even with multiple imports.

**Professional Use:** Place initialization logic here (logging setup, configuration loading), but keep it lightweight!

---

**Trap 5: Relative vs Absolute Imports**
```python
# Inside package/subpackage/module.py
"""Demonstrating import styles within a package."""

# Absolute Import (PREFERRED by PEP 8)
from package.module_a import func  # Clear, explicit, works everywhere


# Relative Import (Use with caution)
from ..module_a import func  # ".." means parent package
from .sibling_module import other_func  # "." means current package

# DANGER: Relative imports fail if module is run directly as script
# python package/subpackage/module.py  # ValueError: attempted relative import
```

**PEP 8 Recommendation:**
- Use **absolute imports** for clarity and maintainability
- Relative imports are acceptable for complex package hierarchies
- Never run package modules directly; use `python -m package.subpackage.module`

**Type Hint Import Pattern:**
```python
"""Module showing type hint import best practice."""

from typing import List, Dict
from package.models import User  # Absolute import for type hints


def process_users(users: List[User]) -> Dict[str, int]:
    """Process users with proper type hints."""
    return {user.name: user.id for user in users}
```

---

### Exam Tips

**Critical Concepts for PCAP:**
1. **`sys.modules`**: Dictionary of already-imported modules (cached)
   ```python
   import sys
   print('math' in sys.modules)  # Check if math is imported
   ```

2. **`__name__` == "__main__"`**: Guard for executable scripts
   ```python
   """Module that can be imported or run directly."""

   def main() -> None:
       """Entry point when run as script."""
       print("Running as script")


   if __name__ == "__main__":
       main()  # Only runs when executed directly, not when imported
   ```

3. **`dir(module)`**: Lists all attributes/functions in a module
   ```python
   import math
   print(dir(math))  # Shows all available functions/constants

    for name in dir(math):
        print(name, end="\t")

    #OUTPUT:
    __doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	atan2	atanh	ceil	copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	factorial	floor	fmod	frexp	fsum	gamma	hypot	isfinite	isinf	isnan	ldexp	lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	


   ```

4. **Dotted imports**: `from a.b.c import d` - Know the lookup order!
   - Python searches in order: current dir → PYTHONPATH → stdlib → site-packages

