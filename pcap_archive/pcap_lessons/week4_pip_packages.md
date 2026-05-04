# Python Environment Management: pip, Packages & Version Control

> **Purpose:** Practical reference guide for managing Python installations, pip, and packages.
> **Note:** This is a reference document, not a task-based lesson.

---

## Table of Contents

1. [Locating Python on Your System](#1-locating-python-on-your-system)
2. [Python Version Management](#2-python-version-management)
3. [pip Fundamentals](#3-pip-fundamentals)
4. [pip Flags & Options](#4-pip-flags--options)
5. [Virtual Environments](#5-virtual-environments)
6. [requirements.txt](#6-requirementstxt)
7. [Common Scenarios & Troubleshooting](#7-common-scenarios--troubleshooting)
8. [PCAP Exam Notes](#8-pcap-exam-notes)

---

## 1. Locating Python on Your System

### Windows

```powershell
# Find all Python installations
where python

# Check Python version
python --version
python -V

# Use the py launcher (Windows-specific, very useful!)
py --list              # List all installed Python versions
py -3.10 --version     # Check specific version
py -3.11 --version

# Find Python executable path
python -c "import sys; print(sys.executable)"
```

### Linux/macOS

```bash
# Find Python location
which python
which python3

# Check version
python3 --version

# Find all Python installations
whereis python
ls -la /usr/bin/python*

# Get executable path
python3 -c "import sys; print(sys.executable)"
```

### Understanding Your Python Path

```python
import sys

# Where is this Python installed?
print(sys.executable)
# Example: C:\Users\You\AppData\Local\Programs\Python\Python311\python.exe

# Where does it look for packages?
print(sys.path)

# What version is running?
print(sys.version)
print(sys.version_info)  # Named tuple: (major, minor, micro, releaselevel, serial)
```

---

## 2. Python Version Management

### Windows: The `py` Launcher

The `py` launcher is your best friend on Windows. It's installed with Python and helps manage multiple versions.

```powershell
# Run specific Python version
py -3.10 script.py
py -3.11 script.py
py -3.12 script.py

# Run latest Python 3
py -3 script.py

# Run latest Python 2 (if installed, legacy)
py -2 script.py

# List installed versions
py --list
py -0p          # Show paths too

# Use specific version's pip
py -3.10 -m pip install pandas
py -3.11 -m pip install pandas
```

### Linux/macOS: Explicit Version Commands

```bash
# Most systems have versioned commands
python3.10 script.py
python3.11 script.py

# Or use update-alternatives (Debian/Ubuntu)
sudo update-alternatives --config python3

# macOS with Homebrew
brew install python@3.11
brew install python@3.12
```

### When to Use Which Version?

| Scenario | Recommendation |
|----------|----------------|
| New project | Use latest stable (3.11 or 3.12 as of 2024) |
| Existing project | Match project's requirements |
| PCAP study | 3.x (exam uses Python 3) |
| Legacy code | Whatever version it was written for |
| Library compatibility issues | Check library docs for supported versions |

---

## 3. pip Fundamentals

### Which pip Am I Using?

**CRITICAL:** `pip` might not match your `python`!

```powershell
# Check which pip
pip --version
# pip 23.2.1 from C:\Python311\Lib\site-packages\pip (python 3.11)

# SAFEST: Always use python -m pip
python -m pip --version
py -3.10 -m pip --version
py -3.11 -m pip --version
```

**Rule:** Always use `python -m pip` instead of just `pip` to guarantee you're installing to the right Python.

### Basic Commands

```powershell
# Install a package
python -m pip install pandas

# Install specific version
python -m pip install pandas==2.0.0
python -m pip install "pandas>=2.0,<3.0"

# Uninstall
python -m pip uninstall pandas

# List installed packages
python -m pip list

# Show package details
python -m pip show pandas

# Check for outdated packages
python -m pip list --outdated

# Search (deprecated, use PyPI website)
# python -m pip search pandas  # No longer works
```

---

## 4. pip Flags & Options

### Installation Flags

| Flag | Full Form | Purpose | Example |
|------|-----------|---------|---------|
| `-U` | `--upgrade` | Upgrade to latest version | `pip install -U pandas` |
| `-r` | `--requirement` | Install from requirements file | `pip install -r requirements.txt` |
| `-e` | `--editable` | Install in editable/development mode | `pip install -e .` |
| `--user` | | Install to user directory (no admin) | `pip install --user pandas` |
| `--no-cache-dir` | | Don't use cached packages | `pip install --no-cache-dir pandas` |
| `--pre` | | Include pre-release versions | `pip install --pre pandas` |
| `--force-reinstall` | | Reinstall even if up-to-date | `pip install --force-reinstall pandas` |
| `-t` | `--target` | Install to specific directory | `pip install -t ./libs pandas` |
| `--no-deps` | | Don't install dependencies | `pip install --no-deps pandas` |

### Commonly Used Examples

```powershell
# Upgrade pip itself (DO THIS REGULARLY!)
python -m pip install -U pip

# Upgrade a package
python -m pip install -U pandas

# Upgrade all outdated packages (Windows PowerShell)
python -m pip list --outdated --format=freeze | ForEach-Object { python -m pip install -U $_.Split('==')[0] }

# Install from requirements.txt
python -m pip install -r requirements.txt

# Install package in development mode (for your own packages)
python -m pip install -e .

# Install without using cache (useful for troubleshooting)
python -m pip install --no-cache-dir pandas

# Install to user directory (when you don't have admin rights)
python -m pip install --user pandas
```

### Output & Information Flags

```powershell
# Verbose output
python -m pip install -v pandas
python -m pip install -vvv pandas  # Even more verbose

# Quiet output
python -m pip install -q pandas

# Dry run (see what would happen)
python -m pip install --dry-run pandas

# Show package info
python -m pip show pandas
python -m pip show -f pandas  # Include file list
```

### Freeze & Export

```powershell
# Export installed packages to requirements.txt
python -m pip freeze > requirements.txt

# Export with hashes (for security)
python -m pip freeze --all > requirements.txt
```

---

## 5. Virtual Environments

### Why Virtual Environments?

- **Isolation:** Each project has its own packages
- **Version Control:** Different projects can use different package versions
- **Clean System:** Don't pollute global Python installation
- **Reproducibility:** Easy to recreate environment

### Creating & Using venv (Built-in)

```powershell
# Create virtual environment
python -m venv venv
python -m venv .venv          # Hidden folder (common convention)
py -3.11 -m venv venv         # Use specific Python version

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Windows CMD)
.\venv\Scripts\activate.bat

# Activate (Linux/macOS)
source venv/bin/activate

# Your prompt changes:
# (venv) PS C:\project>

# Verify you're in venv
where python              # Should point to venv folder
python -m pip --version   # Should show venv path

# Deactivate
deactivate
```

### Virtual Environment Workflow

```powershell
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create venv
python -m venv venv

# 3. Activate
.\venv\Scripts\Activate.ps1

# 4. Upgrade pip first
python -m pip install -U pip

# 5. Install packages
python -m pip install pandas numpy matplotlib

# 6. Freeze requirements
python -m pip freeze > requirements.txt

# 7. Work on your project...

# 8. Deactivate when done
deactivate
```

### Recreating an Environment

```powershell
# On a new machine or fresh install:

# 1. Create venv
python -m venv venv

# 2. Activate
.\venv\Scripts\Activate.ps1

# 3. Install from requirements
python -m pip install -r requirements.txt

# Done! Same environment as original
```

### .gitignore for Virtual Environments

```gitignore
# Virtual environments
venv/
.venv/
env/
.env/

# Don't commit these!
```

---

## 6. requirements.txt

### Basic Format

```text
# requirements.txt
pandas==2.0.3
numpy>=1.24.0
matplotlib>=3.7,<4.0
requests
```

### Version Specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `==` | Exact version | `pandas==2.0.3` |
| `>=` | Minimum version | `pandas>=2.0.0` |
| `<=` | Maximum version | `pandas<=2.1.0` |
| `>` | Greater than | `pandas>2.0.0` |
| `<` | Less than | `pandas<3.0.0` |
| `~=` | Compatible release | `pandas~=2.0.3` (>=2.0.3, <2.1.0) |
| `!=` | Exclude version | `pandas!=2.0.2` |

### Combining Specifiers

```text
# Multiple conditions
pandas>=2.0.0,<3.0.0
numpy>=1.24,!=1.24.2
```

### requirements.txt Best Practices

```text
# requirements.txt

# Core dependencies
pandas==2.0.3
numpy==1.24.3

# Development only (consider separate dev-requirements.txt)
pytest==7.4.0
black==23.7.0

# Comments explain non-obvious choices
requests==2.31.0  # Pinned due to breaking change in 2.32
```

### Multiple Requirements Files

```text
# requirements.txt - production
pandas==2.0.3
numpy==1.24.3

# requirements-dev.txt - development
-r requirements.txt
pytest==7.4.0
black==23.7.0
mypy==1.4.0
```

```powershell
# Install dev requirements (includes production)
python -m pip install -r requirements-dev.txt
```

---

## 7. Common Scenarios & Troubleshooting

### Scenario 1: "pip installs to wrong Python"

```powershell
# Problem: You run pip install but package not found when you run python

# Solution: ALWAYS use python -m pip
python -m pip install pandas  # Guarantees correct Python

# Or use py launcher on Windows
py -3.11 -m pip install pandas
```

### Scenario 2: "Module not found" after install

```powershell
# Check if you're in the right environment
python -c "import sys; print(sys.executable)"

# Check if package is installed
python -m pip show pandas

# If using venv, make sure it's activated!
.\venv\Scripts\Activate.ps1
```

### Scenario 3: "Permission denied" during install

```powershell
# Option 1: Use --user flag
python -m pip install --user pandas

# Option 2: Use virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install pandas

# Option 3: Run as admin (NOT recommended for system Python)
```

### Scenario 4: Package conflicts

```powershell
# See what depends on what
python -m pip show pandas  # Check "Requires" and "Required-by"

# Force reinstall with dependencies
python -m pip install --force-reinstall pandas

# Nuclear option: fresh venv
deactivate
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Scenario 5: "I need package X but it requires Python 3.10 and I have 3.11"

```powershell
# Option 1: Check if newer package version supports 3.11
python -m pip install package_name --upgrade

# Option 2: Create venv with correct Python version
py -3.10 -m venv venv310
.\venv310\Scripts\Activate.ps1
python -m pip install package_name
```

### Scenario 6: Upgrading all packages

```powershell
# List outdated
python -m pip list --outdated

# Upgrade specific package
python -m pip install -U pandas

# Upgrade all (PowerShell)
python -m pip list --outdated --format=freeze | ForEach-Object {
    $pkg = $_.Split('==')[0]
    python -m pip install -U $pkg
}
```

---

## 8. PCAP Exam Notes

The PCAP exam tests **conceptual understanding** of pip and packages, not command-line memorization.

### Key Concepts for PCAP

1. **pip is the standard package installer for Python**
2. **PyPI (Python Package Index)** is the default repository
3. **pip install** downloads from PyPI by default
4. **pip freeze** outputs installed packages in requirements format
5. **Virtual environments** isolate project dependencies

### Likely Exam Questions

```python
# Q: What does pip stand for?
# A: "pip installs packages" (recursive acronym)

# Q: What command installs a package?
# A: pip install package_name

# Q: What command shows installed packages?
# A: pip list

# Q: What command exports installed packages?
# A: pip freeze

# Q: Where does pip download packages from by default?
# A: PyPI (Python Package Index) - pypi.org
```

### Module vs Package (PCAP Important!)

```python
# Module: Single .py file
# my_module.py

# Package: Directory with __init__.py
# my_package/
#     __init__.py
#     module1.py
#     module2.py

# Import differences
import my_module           # Module
from my_package import module1  # Package
```

---

## Quick Reference Card

```powershell
# ===== ESSENTIALS =====

# Check Python version & location
python --version
python -c "import sys; print(sys.executable)"

# Check pip
python -m pip --version

# ===== INSTALL/UNINSTALL =====

python -m pip install pandas           # Install
python -m pip install pandas==2.0.0    # Specific version
python -m pip install -U pandas        # Upgrade
python -m pip uninstall pandas         # Remove
python -m pip install -r requirements.txt  # From file

# ===== INFORMATION =====

python -m pip list                     # All packages
python -m pip list --outdated          # Outdated packages
python -m pip show pandas              # Package details
python -m pip freeze                   # Export format

# ===== VIRTUAL ENVIRONMENTS =====

python -m venv venv                    # Create
.\venv\Scripts\Activate.ps1            # Activate (Windows PS)
source venv/bin/activate               # Activate (Linux/Mac)
deactivate                             # Deactivate

# ===== WINDOWS PY LAUNCHER =====

py --list                              # List Python versions
py -3.11 script.py                     # Run with specific version
py -3.11 -m pip install pandas         # pip for specific version
```

---

*Last updated: Week 4 - Reference Document*
