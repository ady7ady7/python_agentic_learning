# Feedback Archive

This file stores all completed daily feedback entries in chronological order (oldest → newest).

---

## Week 11, Day 5 — 2026-03-27

**Topic:** datetime | exceptions | OOP/MRO | generators | closures | modules | LPP Strategy
**Score:** 96% (27/28)

**Per-task breakdown:**
- T1 datetime: ✅ All correct
- T2 strptime/comparisons: ✅ All correct, strptime/strftime definitions clean
- T3 exceptions: ✅ All four correct — finally always runs, SpecificError caught by parent handler
- T4 OOP/MRO: ✅ All three correct — D→B→C→A trace, class variable shared correctly
- T5 generators: ✅ All four correct
- T6 closures/lambdas: ✅ All four correct — late binding, default arg fix, reduce, sorted key
- T7 modules: ✅ Q1-Q2. ✗ Q3 — answered A(10), correct is B(99). Python caches modules in sys.modules — re-import returns same object, mutations persist
- T8 project: Partial — LPPStrategy.prepare() complete and correct. run_backtest() restructured. Blocked on SL/TP universal contract and generate_signal() signature.

**Mentor note:** Session was too architecturally chaotic. Too many design pivots mid-session caused confusion. Next session: fix get_sl()/get_tp() contract on BaseStrategy first, nothing else until that's clean.

---

## Week 11, Day 4 — 2026-03-26

**Topic:** os.path | escape sequences | generators | closures | MRO | Project
**Score:** 100%

**Per-task breakdown:**
- T1 os.path: ✅ All correct including no trailing slash rule
- T2 escape sequences: ✅ All correct — `'\\\''` valid (prints `'`, len=1) confirmed
- T3 generators: ✅ Infinite fibonacci with while True + yield, squares with next/list/StopIteration
- T4 mixed gaps: ✅ parent-before-child, else/finally, randrange impossible value
- T5 closures: ✅ All three correct
- T6 generators: ✅ All three correct including exhausted generator returns []
- T7 MRO + closures: ✅ BCA prepend pattern correct, mutable list closure correct
- T8 project: ✅ Multi-strategy run_backtest, uuid4 strategy_id, per-strategy session filter

**Mentor correction this session:** `'\\\''` was incorrectly flagged as SyntaxError across multiple prior sessions. Confirmed valid — fixed in gaps_pcap_mock1.md, tasks.md, and memory.

---

## Week 11, Day 3 — 2026-03-25

**Topic:** repr() | os.path | errno | random | escape sequences | generators | closures | Project
**Score:** 80% (28/35)

**Per-task breakdown:**
- T1 repr(): ✅ All correct. Minor: f-string output is `an item` not `{an item}`
- T2 os.path: ✅ basename/splitext correct. ✗ dirname has no trailing slash. ✗ split() needs string quotes. ✗ Linux uses `/` not `\`
- T3 errno: ✅ All four outputs correct + MC correct
- T4 random: ✅ All three correct
- T5 escape: ✅ a,b,d,len correct. ✗ `'\\\''` is SyntaxError — persistent trap
- T6 generator: ✗ Wrote regular function with return+list. Task required `yield`+`while True` infinite generator
- T7 closures: ✅ All three parts correct
- T8 project: ✅ Full implementation — RTH filter, force_close_all, abstract session methods, 112k trades

**Persistent gaps:**
- `os.path` exact output (trailing slash, string tuple format, slash direction)
- `'\\\''` SyntaxError — appears repeatedly, still not solid
- Generator infinite pattern: `while True: yield x`

---

## Week 1, Day 1 - 2026-01-05

**Topic:** Modules, Packages & Import Mechanisms

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** Just Right / Too Hard (mixed)
- **Time Spent:** 1.5 hours

### Student Reflection
**What clicked:**
- General understanding of importing and different import patterns

**What's confusing:**
- File clutter from creating separate files for every task
- Preference for using `practice.py` as scratch workspace (PCEP methodology)
- Question about `__init__.py` relevance in 2026

**Project Progress:**
- AlgoBacktest structure is simple so far
- Concerns about file organization going forward

### Mentor Assessment

**Score: 86.25% (B+)**

**Task Breakdown:**
1. Import Variants: 90% - All styles correct, minor misunderstanding about PI overwrite direction
2. sys.path Investigation: 100% - Perfect execution
3. Circular Import: 70% - Works but missed lazy import pattern (imported from same folder instead of lazy loading)
4. AlgoBacktest Setup: 100% - `from __init__ import` was CORRECT - mentor error in task structure
5. Dependency Checker: 85% - Clean code, valid critique about importlib not being taught
6. Name Shadowing: 75% - Correct diagnosis, professional instinct to reject sys.path hack
7. Multiple Choice: 100% - Correct answer with solid reasoning
8. Lazy Import: 60% - Code works but missed core use case (startup optimization)

**Strengths:**
- Professional instincts (rejecting bad patterns)
- Clean exception handling
- Critical thinking and constructive feedback

**Areas for Improvement:**
- Understand lazy import use cases (startup time, optional features)
- Package imports should use package name, not `__init__` directly
- Practice lazy import pattern for circular dependency resolution

**Critical Corrections:**
- Task 3: Use `from broken_pkg.engine import start` INSIDE the function (lazy import)
- Task 4: Student solution was CORRECT - mentor gave bad package structure (main.py inside package folder)

**Action Items:**
- ✅ Updated CLAUDE.md to use `practice.py` workflow (no file clutter)
- ✅ Added daily assessment protocol to instructions
- Confirmed `__init__.py` is still relevant for professional projects
- Deferred importlib to Week 7 (not on PCAP exam)

---

## Week 1, Day 2 - 2026-01-06

**Topic:** Strings, Exceptions & File I/O

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** Too Hard (8/10)
- **Time Spent:** Not specified

### Student Reflection
**What clicked:**
- String methods (find/index, strip, split) edge cases
- Exception handling order (specific → general)
- Context managers for file I/O

**What's confusing/Frustrating:**
- Expected to use classes (OOP) without any prior instruction
- Advanced Pandas operations (`.isna().sum()`, `.any()`) not taught yet
- Missing test files for Task 7 (`read_config` function)
- Curriculum asks for things before teaching them

**Legitimate Complaints:**
- "You've asked me to do a lot of things we didn't learn, and expected me to use classes when we literally didn't ever learn them"
- "WE DID NOT PROPERLY LEARN THESE THINGS THAT YOU'RE EXPECTING ME TO DO YET"
- "I CANNOT REALLY TEST THAT CONFIG... it doesn't seem like a part of a proper learning process"

### Mentor Assessment

**Score: 78.75% (C+)**

**Task Breakdown:**
1. String Slicing Edge Cases: 100% - All answers correct (mentor initially wrong on #5)
2. String Methods: 100% - Excellent observations, identified `.find()` returning -1 trap
3. safe_divide Function: 95% - Clean exception handling, proper order, good docstring
4. Exception Order Debug: 100% - Identified error, fixed correctly, clear explanation
5. DataLoader Class: 70% - Functional but incomplete (missing context manager, return None on ValueError)
6. validate_data Method: 60% - Logic errors (`set(df.columns) - set(df.columns)` always empty, isna check incorrect)
7. read_config Function: 85% - Clean code, proper exception handling, missing PermissionError return statement
8. PCAP Multiple Choice: 100% - Correct answer with clear reasoning

**Bonus Task:** 90% - Clean f-string usage, missing thousands separator (`:,` format)

**Strengths:**
- String manipulation mastery (all edge cases correct)
- Exception handling order understanding
- Critical feedback and constructive criticism
- Professional code structure (type hints, docstrings)

**Critical Code Issues:**

**Task 5 (DataLoader):**
```python
# ISSUE 1: No context manager used (requirement violated)
data = pd.read_csv(self.filepath)  # Should use 'with' statement

# ISSUE 2: ValueError exception doesn't return None
except ValueError as e:
    print(f'Value Error! {str(e)}')
    # Missing: return None
```

**Task 6 (validate_data):**
```python
# ISSUE 1: Logic error - this is always empty
missing_columns = set(df.columns) - set(df.columns)  # Should be: set(req_columns) - set(df.columns)

# ISSUE 2: isna() check is incorrect
nan_values = df[req_columns].isna().sum()
if nan_values.any():  # This checks if ANY column has NaN, but doesn't fail properly
```

**Task 7 (read_config):**
```python
except PermissionError as e:
    print(f'Permission error: {str(e)}')
    # Missing: return {}
```

**Curriculum Errors Identified:**
1. **OOP Introduced Too Early:** Tasks 5-6 require class creation without teaching `__init__`, `self`, methods, or attributes first
2. **Advanced Pandas Not Taught:** Expected `.isna().sum()`, `.any()`, DataFrame boolean indexing without instruction
3. **Missing Test Files:** Task 7 requires file to test against (bad pedagogy)
4. **Prerequisite Gap:** Teaching order violated (concepts used before explained)

**Action Items:**
- ✅ Acknowledged curriculum error publicly
- ⚠️ CRITICAL: Day 3 MUST introduce OOP fundamentals (classes, `__init__`, `self`, methods) BEFORE any class-building tasks
- ⚠️ Create Pandas mini-lesson covering DataFrame operations before next data task
- ⚠️ Provide sample files for all file I/O tasks going forward
- Update curriculum to ensure teaching precedes application

**Mentor Note:** User's frustration is 100% valid. This was a significant instructional design failure. The score reflects what the student COULD know given proper instruction, not what they should have been expected to know.

---

## Week 1, Day 3 - 2026-01-07

**Topic:** OOP Fundamentals - Classes, Objects & Methods

### Student Self-Assessment
- **Tasks Completed:** 9/9 (8 main + bonus)
- **Difficulty:** Manageable (6/10)
- **Time Spent:** 1 hour 20 minutes

### Student Reflection
**What clicked:**
- Classes as blueprints vs objects as instances
- `self` parameter and object separation
- Instance vs class attributes (shared vs unique)
- Mutable class attributes trap
- Connection to mutable default parameters

**Student Feedback:**
- "This time checking our lessons/ material was sufficient to complete the tasks"
- Disagreed with `is_long()`/`is_short()` design - implemented explicit `side` parameter instead (industry standard)
- Caught own logic error: `or` vs `and` in validation (self-debugging)
- Challenged mentor's negative quantity spec (crypto-only convention, not industry standard)

**Domain Expertise Applied:**
- Futures/CFDs/stocks use positive quantity + explicit side
- Only crypto perpetuals use signed quantity
- `side` parameter is more realistic and Pythonic

### Mentor Assessment

**Score: 97.5% (A+)**

**Task Breakdown:**
1. Understanding `self`: 100% - Perfect predictions (12, 21), excellent explanation
2. Instance vs Class Attributes: 100% - All 6 predictions correct, solid conceptual understanding
3. BankAccount Class: 95% - Clean implementation, good validation, minor docstring style inconsistency (mixing single/triple quotes)
4. Mutable Class Attributes Trap: 100% - Identified bug, perfect fix, outstanding insight connecting to mutable default parameters
5. Position Class: 95% - Excellent `side` parameter decision (mentor spec was wrong), missing None checks for SL/TP edge cases
6. DataLoader Fixes: 100% - All fixes correct, Pandas `.any()` semantics issue acknowledged as teaching gap
7. PCAP Multiple Choice: 100% - Q1 typo (meant C, wrote A), Q2 correct
8. OHLCCandle Enhancement: 95% - All methods correct, minor ZeroDivisionError risk in `is_doji()` (check range==0 before division)
9. Employee Bonus: 100% - Perfect class attribute counter implementation

**Strengths:**
- **Domain expertise:** Challenged unrealistic spec with real markets knowledge
- **Self-debugging:** Caught and fixed `or` vs `and` logic error independently
- **Deep understanding:** Connected mutable class attributes to mutable default parameters
- **Practical thinking:** Chose explicit `side` over signed `quantity` (correct industry pattern)
- **Fast learning:** 1hr 20min for 9 tasks shows efficiency
- **Critical thinking:** Questioned "retarded" requirements with valid reasoning

**Critical Code Issue:**

**Task 5 - None Comparison Edge Case:**
```python
# Current code - will crash if stop_loss/take_profit is None:
if self.side == 'BUY' and current_price < self.stop_loss:  # TypeError if None
    return True

# Should check None first:
if self.side == 'BUY':
    if self.stop_loss is not None and current_price <= self.stop_loss:
        return True
    if self.take_profit is not None and current_price >= self.take_profit:
        return True
```

**Task 8 - ZeroDivisionError Risk (Minor):**
```python
# Current (division happens first):
if abs(self.close - self.open) / (self.high - self.low) < threshold:

# Should check zero first:
candle_range = self.high - self.low
if candle_range == 0:
    return True
return self.get_body_size() / candle_range < threshold
```

**Mentor Corrections:**

1. **Position Class Spec Was Wrong:** Mentor incorrectly specified negative quantity for shorts. Student's explicit `side` parameter is the correct industry standard. Score upgraded from 85% to 95%.

2. **Pandas Teaching Gap:** Task 6 `.any()` semantics issue is a teaching failure, not student error. Student's code works (Python treats `True > 0` as `True`). Score upgraded from 90% to 100%.

3. **Task 7 Question 1:** Acknowledged typo - student clearly understood concept (explanation was correct).

**Action Items:**
- ✅ Lesson structure worked - student read OOP fundamentals before attempting tasks
- ✅ Difficulty appropriate (6/10 vs previous 8/10)
- ⚠️ Create Pandas mini-lesson before next data-heavy task (promised in Day 2 feedback)
- ⚠️ Trust student's domain expertise on trading/markets design decisions
- Note: Student prefers realistic, industry-standard patterns over academic exercises

**Mentor Note:** Excellent session. Student demonstrated both technical mastery and domain expertise. The explicit `side` parameter critique shows engineering maturity - questioning specs when they don't match reality. This is exactly what senior engineers do.

---

## Week 1, Day 4 - 2026-01-08

**Topic:** Magic Methods & Pandas Essentials

### Student Self-Assessment
- **Tasks Completed:** 9/9 (8 main + bonus)
- **Difficulty:** Easy-Medium (5/10)
- **Time Spent:** Not specified

### Student Reflection
**What clicked:**
- `__str__` vs `__repr__` distinction (user-friendly vs developer-friendly)
- Magic method fallback behavior (repr used when str missing)
- Pandas `.any()` semantics fully understood
- Three different approaches to NaN checking
- Boolean indexing with proper `&` operator syntax

**Student Feedback:**
- Corrected mentor on Task 2 (TypeError IS raised, not just None return)
- Defended PEP 8 line length compliance in multi-line f-strings (Task 6)
- Identified correct error concept in Task 7 Q2 (Series ambiguity) but wrong exception type
- Validated P&L calculations ($50 not $500 for 0.005 price difference)

### Mentor Assessment

**Score: 93.5% (A)**

**Task Breakdown:**
1. `__str__` vs `__repr__` Predictions: 95% - Predictions correct, minor repr formatting issue in answer
2. Magic Method Trap: 100% - **Student corrected mentor**: `TypeError` IS raised when `__str__` returns None
3. Position Magic Methods: 85% - Functional but missing "No SL/No TP" requirement, missing ticker in `__str__`, `__name__` instead of class name in `__repr__`
4. Pandas `.any()` Understanding: 100% - All three solutions correct, perfect explanation
5. Boolean Indexing: 95% - All solutions work, minor redundancy in Series wrapping
6. Trade Class: 95% - **Student corrected mentor**: Multi-line f-string formatting is PEP 8 compliant for line length; only minor issues (redundant `== True`, missing commas in `__repr__`)
7. PCAP Multiple Choice: 75% - Q1 correct (100%), Q2 wrong exception type (50% - correct concept, wrong type: ValueError not TypeError)
8. DataLoader Enhancement: 100% - All three methods implemented perfectly
9. Bonus Trade Statistics: 95% - Class method works, minor issue accessing `_calculate_pnl()` instead of `.pnl` attribute

**Average: 93.33% → Rounded to 93.5%**

**Strengths:**
- **Critical thinking:** Corrected mentor's errors on Task 2 (TypeError) and Task 6 (PEP 8 formatting)
- **Pandas mastery:** Teaching gap officially closed - all `.any()` approaches correct
- **Self-validation:** Verified P&L math ($50 correct, mentor's $500 wrong)
- **Clean implementations:** Trade and DataLoader classes well-structured
- **Bonus completion:** Class methods understood and applied
- **Efficiency:** 5/10 difficulty shows optimal learning zone

**Mentor Corrections:**

1. **Task 2 - Mentor Was Wrong:** Student correctly identified that `TypeError: __str__ returned non-string (type NoneType)` IS raised. Mentor incorrectly said it just returns None. Student score: 100%.

2. **Task 6 - PEP 8 Compliance:** Student's multi-line f-string formatting is intentionally correct for PEP 8 line length limits (79-88 chars). Mentor critique withdrawn.

3. **Task 7 Question 2:** Student identified correct error concept (Series truth value ambiguity) but got exception type wrong (ValueError vs TypeError). Partial credit given.

**Minor Issues Identified:**

**Task 3 - Position `__str__` Requirements:**
```python
# Current: Missing ticker, "No SL/No TP" handling
return f'{self.side} {self.quantity} @ {self.entry_price} [SL = {self.stop_loss}, TP = {self.take_profit}]'

# Required:
sl_str = f"SL={self.stop_loss:.4f}" if self.stop_loss else "No SL"
tp_str = f"TP={self.take_profit:.4f}" if self.take_profit else "No TP"
return f'{self.side} {self.quantity} {self.ticker} @ {self.entry_price:.4f} [{sl_str}, {tp_str}]'
```

**Task 3 - Position `__repr__` Module Name:**
```python
# Current: Uses module name
return f'{__name__}(ticker = {self.ticker}, ...'  # __name__ = 'algo_backtest.engine.position'

# Should be:
return f'Position(ticker={self.ticker!r}, side={self.side!r}, ...)'
```

**Task 6 - Trade Minor Issues:**
```python
# Issue 1: Redundant comparison
if self.is_winner() == True:  # Just use: if self.is_winner():

# Issue 2: Missing commas in __repr__
return (f'Trade(ticker = {self.ticker!r}, side = {self.side!r},'  # comma here ✅
        f'entry_price = {self.entry_price}, exit_price = {self.exit_price}'  # missing comma ❌
        f'quantity = {self.quantity}, ...')
```

**Bonus - Trade Statistics:**
```python
# Current: Recalculates PnL
trades_profits = [trade._calculate_pnl() for trade in trades]

# Better: Use already-calculated pnl
winners = [trade for trade in trades if trade.pnl > 0]
return (len(winners) / len(trades)) * 100 if trades else 0
```

**Action Items:**
- ✅ Pandas mini-lesson delivered and mastered
- ✅ Magic methods understood (`__str__`, `__repr__`)
- ✅ Student demonstrated ability to correct mentor errors (professional maturity)
- Note: Student's Optional confusion resolved (type hints vs runtime)

**Mentor Note:** Outstanding session. Student not only completed all tasks but also caught multiple mentor errors (Task 2 TypeError, Task 6 PEP 8 formatting). This demonstrates deep understanding and professional code review skills. Difficulty rated 5/10 - in the optimal learning zone (challenging but manageable).

---

## Week 1, Day 5 - 2026-01-09

**Topic:** Week 1 Review & Integration (Friday Wrap-up)

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** Medium (5-6/10)
- **Time Spent:** 1.5 hours

### Student Reflection
**What clicked:**
- Week 1 integration and practical application of concepts
- Main.py bringing together DataLoader → Trade → PositionManager workflow
- Pandas optimization patterns and efficient filtering
- Practice session was educational with no major blockers

**Student Feedback & Corrections:**
- **Task 2 Import Critique:** User correctly stated that `from __init__ import __version__` and `import check_dependencies` are correct because main.py is INSIDE the algo_backtest folder. Mentor was wrong.
- **Task 5 Pandas Optimization:** Requested optimized Pandas patterns be added to lessons/pandas.md (completed)
- **Task 5 Q4 Logic Error:** Acknowledged close > open mistake was inattention, not conceptual misunderstanding
- **Task 5 Q1 Scoring:** Disagreed with point deduction - showing comparison between inefficient/efficient approaches has pedagogical value
- **Task 6 PositionManager Fixes:** Confirmed type hint issue fixed (returns float), list modification fixed using list comprehension

### Mentor Assessment

**Score: 93.75% (A)**

**Task Breakdown:**
1. **Quick Fire Review (6 questions):** 100%
   - Q1: String `.strip()` and `.replace()` - correct
   - Q2: Exception order (most specific first) - correct
   - Q3: Class vs instance attributes (shared vs unique) - correct
   - Q4: `__str__` vs `__repr__` purpose - correct
   - Q5: Pandas `.any()` on boolean Series - correct
   - Q6: Optional type hint purpose - correct

2. **Integration Challenge (main.py):** 100%
   - **CORRECTED:** Import paths are CORRECT. Mentor error - main.py is inside algo_backtest folder
   - Proper DataLoader → Trade → PositionManager workflow
   - Clean statistics calculation (win rate, total P&L)
   - Professional structure with `if __name__ == '__main__'`
   - Type hints and docstrings present

3. **PCAP Traps (Predict Output):** 100%
   - All 3 predictions correct with excellent explanations
   - Trap 1: Mutable class attribute list modification
   - Trap 2: `__repr__` fallback when `__str__` missing
   - Trap 3: Boolean indexing with incorrect `and` operator

4. **Exception Handling (safe_backtest_runner):** 95%
   - Complete try/except/else/finally structure
   - All four exception types handled correctly
   - Clean logging for each case
   - Minor: Could add more specific success message in `else`

5. **Pandas Advanced Filtering:** 85% → 90%
   - Q1: Filter bullish candles, calculate average close - **ADJUSTED SCORE:** Showing iterrows() (doesn't work) vs apply() (works) has pedagogical value. Deduction reduced.
   - Q2: Multi-condition filtering (high volume bullish) - correct
   - Q3: Top 3 volume rows with `.nlargest()` - correct (student used this correctly)
   - Q4: Add 'candle_type' column - **ACKNOWLEDGED:** Logic error (open > close should be close > open) is inattention, not misunderstanding
   - **ACTION:** Added optimization patterns to lessons/pandas.md per student request

6. **Project Task (PositionManager):** 90%
   - **CONFIRMED FIXED:** `get_total_pnl()` now returns float (not string)
   - **CONFIRMED FIXED:** `close_triggered_positions()` uses list comprehension (safe pattern)
   - Clean implementation of position management
   - Professional docstrings and type hints
   - All methods implemented correctly

7. **PCAP Multiple Choice:** 100%
   - Q1: Class attribute vs instance attribute modification - correct
   - Q2: Exception catching with multiple types - correct
   - Q3: Pandas boolean indexing operators - correct

8. **Code Review Challenge:** 95%
   - Found 8/8 issues in broken PositionManager
   - Rewrote cleanly with list comprehension pattern
   - Professional code quality

**Average: 93.75%**

**Strengths:**
- **Week 1 Integration Mastery:** Successfully built end-to-end backtest workflow combining all Week 1 concepts
- **Error Correction:** Caught mentor's wrong import path critique (professional code review skill)
- **Self-Awareness:** Identified logic error as inattention, not conceptual gap
- **List Safety:** Applied list comprehension pattern to avoid modification during iteration
- **Pandas Optimization Request:** Proactively requested lesson update for future reference
- **Efficiency:** Completed 8 complex integration tasks in 1.5 hours
- **Type Safety:** Fixed return type inconsistencies when identified

**Critical Code Fixes Applied:**

**PositionManager Type Hint:**
```python
def get_total_pnl(self, current_price: float) -> float:
    total_pnl = sum([position.calculate_pnl(current_price) for position in self.positions])
    if total_pnl is not None:
        return total_pnl  # FIXED: Returns float, not string
    else:
        return 0.0
```

**PositionManager List Modification:**
```python
def close_triggered_positions(self, current_price: float) -> List[Position]:
    # FIXED: List comprehension instead of modifying during iteration
    closed_positions = [p for p in self.positions if p.should_close(current_price)]
    self.positions = [p for p in self.positions if not p.should_close(current_price)]
    return closed_positions
```

**Mentor Corrections:**

1. **Task 2 - Import Paths CORRECT:** Mentor incorrectly critiqued `from __init__ import __version__` and `import check_dependencies`. When main.py is INSIDE algo_backtest folder, these relative imports are appropriate. Student was right, mentor was wrong. Score upgraded to 100%.

2. **Task 5 - Pandas Optimization:** Added comprehensive "Advanced Filtering & Optimization Patterns" section to lessons/pandas.md per student request, covering:
   - Efficient filtering with aggregation (avoid NumPy wrapping)
   - `.loc[]` patterns for filtered column access
   - Direct Series methods vs unnecessary conversions
   - Top-N selection with `.nlargest()`/`.nsmallest()`
   - Vectorized operations vs `.apply()` vs `.iterrows()` performance

3. **Task 5 Q1 - Scoring Adjustment:** Recognized pedagogical value in showing comparison between inefficient approach (iterrows) and efficient approach (apply). Partial credit restored.

**Action Items:**
- ✅ Week 1 complete - all core concepts covered (modules, strings, exceptions, OOP, magic methods, Pandas)
- ✅ AlgoBacktest functional with DataLoader, Trade, Position, PositionManager classes
- ✅ Pandas optimization patterns documented in lessons/pandas.md
- ✅ Student demonstrated ability to correct mentor errors (professional maturity)
- 📝 Ready for Week 1 summary commit
- 📝 Generate 2 PCAP mock exams for weekend study

**Week 1 Summary:**
Student successfully completed all 5 days (40 tasks total) covering foundational Python topics and OOP. Project milestones achieved:
- Project structure established (packages, modules, imports)
- Data pipeline created (DataLoader with Pandas)
- Trading entities implemented (Position, Trade classes)
- Position management system (PositionManager)
- End-to-end backtest execution (main.py)

Average Week 1 Score: (86.25% + 78.75% + 97.5% + 93.5% + 93.75%) / 5 = **89.95% (B+)**

**Mentor Note:** Excellent Week 1 completion. Student not only mastered technical content but also demonstrated professional code review skills by correcting multiple mentor errors throughout the week (import paths, TypeError behavior, PEP 8 formatting). The 1.5-hour completion time for 8 integration tasks shows strong efficiency and deep understanding. Ready for Week 2 (Advanced OOP & Inheritance).

---

## Week 2, Day 1 - 2026-01-13

**Topic:** Inheritance Fundamentals

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 5/10
- **Time Spent:** 66 minutes

### Student Reflection
**What clicked:**
"Generally everything I think, but it all needs refinement and regular practice"

**Question asked:**
"Are these attributes or parameters? What is the difference between attribute and parameter?"

**Answer provided:** Parameters are variables in function/method definitions (e.g., `def __init__(self, owner, balance)` - `owner` and `balance` are parameters). Attributes are variables attached to an object (e.g., `self.owner`, `self.balance` are attributes).

### Mentor Assessment

**Score: 94% (A)**

**Task Breakdown:**

1. **PCAP Warm-up - Predict Output:** 100%
   - Correctly predicted: `Buddy` and `Woof`
   - Excellent explanation of inheritance and method overriding
   - Minor note: Actual output doesn't have quotes, but understanding is perfect

2. **SavingsAccount Class:** 85%
   - ✅ Correct inheritance syntax
   - ✅ Proper use of `super().__init__(owner, balance)`
   - ✅ `add_interest()` logic correct
   - ✅ Good docstrings
   - ❌ Line 84: Redundant `self.balance = balance` (already set by parent)
   - ❌ Line 87: Formatting inconsistency (extra spaces, need to multiply rate by 100 for percentage display)
   - ❌ Line 91: Unnecessary return value in `add_interest()`

3. **Strategy Pattern:** 100%
   - Perfect implementation of parent and child classes
   - Correct use of `super().__init__('Level Cross')`
   - Clean method overriding with if/elif/else logic
   - All test cases pass

4. **PCAP Trap Hunt:** 100%
   - ✅ Correctly identified AttributeError
   - ✅ Explained missing `super().__init__(brand, year)`
   - ✅ Provided correct fix

5. **isinstance/issubclass Practice:** 87.5%
   - 7/8 correct predictions
   - ❌ **F: `issubclass(Dog, Animal)`** - Answered False, should be True (transitive inheritance: Dog → Mammal → Animal)
   - ✅ Correct explanations for D (everything inherits from `object`) and G (every class is subclass of itself)

6. **BaseStrategy ABC:** 100%
   - Perfect ABC implementation
   - Correct use of `@abstractmethod`
   - Type hints on all methods
   - Docstrings present
   - Minor suggestions: module docstring placement, `__init__` docstring, clarify "inherited" wording in `get_name()` docstring

7. **Multiple Choice:** 100%
   - Q1: B ✅ (`super().__init__()` calls parent's `__init__`)
   - Q2: A ✅ (inherits method from parent)
   - Q3: B ✅ (child classes must implement abstract methods)

8. **Code Review:** 95%
   - Identified all 8 issues correctly:
     1. ✅ Uncapitalized class name
     2. ✅ Missing `__` around `init`
     3. ✅ Local scope `name = name` instead of `self.name`
     4. ✅ Undefined `HOLD` variable
     5. ✅ Missing `super().__init__(name)`
     6. ✅ Logic issues (no SELL signal)
     7. ✅ Class instantiated without required parameter
     8. ✅ Missing type hints and docstrings
   - ❌ Corrected code has one issue: `signal()` method in parent missing `price` parameter

**Weighted Score: 94%**

**Strengths:**
- ✅ Strong conceptual understanding of inheritance
- ✅ Correct `super()` usage in all tasks
- ✅ Excellent method overriding implementation
- ✅ Perfect ABC understanding and implementation
- ✅ All multiple choice correct
- ✅ Identified all code review issues
- ✅ Clean, readable code with good structure

**Areas for Improvement:**
1. **Avoid redundant assignments** after `super().__init__()` - parent already sets those attributes
2. **String formatting precision** - match exact specifications (`.2f` for decimals, multiply rates by 100 for percentages)
3. **Remember transitive inheritance** - Dog → Mammal → Animal means `issubclass(Dog, Animal)` is True
4. **Method signatures** - when fixing code, preserve parameter lists

**Key Learning:**
When you call `super().__init__()`, the parent's constructor runs completely. All `self.attribute = value` statements in the parent execute. You don't need to (and shouldn't) reassign those attributes in the child class.

**Project Progress:**
- Created `BaseStrategy` ABC in `algo_backtest/strategies/`
- Established abstract method pattern for strategy implementations
- Foundation ready for concrete strategy classes (Week 2 Days 2-4)

**Next Steps:**
- Day 2: Polymorphism and multiple strategies
- Day 3: Method Resolution Order (MRO) and complex inheritance
- Day 4: Strategy pattern implementation with real backtesting
- Day 5: Week 2 review and integration

**Mentor Note:** Excellent first day of Week 2! Student demonstrated strong grasp of inheritance fundamentals with a 94% score. The few minor errors were implementation details (formatting, redundant code) rather than conceptual misunderstandings. The question about attributes vs parameters shows active learning and desire for clarity. Ready for more advanced OOP topics.

---

## Week 2, Day 2 - 2026-01-13

**Topic:** Polymorphism & Multiple Strategies

### Student Self-Assessment
- **Tasks Completed:** 8/8 (Task 9 bonus not completed)
- **Difficulty:** 5/10
- **Time Spent:** 90 minutes

### Student Reflection
**What clicked:**
"I understand the concept in general. I definitely need to practice this regularly to get a hang of it, and also I need to get a more scaffolded approach to be able to think and figure out some things on my own, but overall difficulty is 5/10 today."

**Student Questions:**
"I also want you to explain the __init__.py file that we extended, what does it mean, why do we use it and what does this mean exactly? `__all__ = ['BaseStrategy', 'LevelCrossStrategy']` Is it an industry standard for Mid/Senior devs to do that? Why and what do we achieve by this?"

**Answer provided:** Comprehensive explanation of `__init__.py` (marks directory as package), `__all__` (controls `from package import *`), confirmed this IS industry standard, explained benefits (explicit public API, clean imports, IDE support).

**Student Corrections:**
- **Task 3:** Student self-corrected MovingAverageStrategy to use slicing instead of `.remove()` for performance
- **Task 3:** Fixed `generate_signal()` to add price internally and handle all BUY/SELL/HOLD cases
- **Task 5:** Mentor error - referenced non-existent `get_level()` and `get_name()` methods. Student correctly used `.name`, `.level`, `.ma_period` attributes directly
- **Task 9:** Student requested bonus tasks not count toward base 100% score

### Mentor Assessment

**Score: 86.25% (B)**

**Task Breakdown:**

1. **Polymorphism Prediction:** 80% (4/5)
   - Predicted output: 43.42
   - Correct output: 43.56636 (15 + 12.56636 + 16)
   - ✅ Explanation of polymorphism correct

2. **LevelCrossStrategy:** 100%
   - ✅ Perfect implementation with proper inheritance
   - ✅ `super().__init__('Level Cross Strategy')`
   - ✅ All three signal cases handled
   - ✅ Type hints and docstrings
   - ✅ `get_level()` method implemented

3. **MovingAverageStrategy:** 100% (after student fixes)
   - ✅ Fixed to use slicing: `self.price_history[-self.ma_period:]`
   - ✅ `generate_signal()` now adds price internally
   - ✅ All three cases (BUY/SELL/HOLD) handled properly
   - ✅ Clean logic flow
   - **Excellent self-correction - production-quality code**

4. **Polymorphism Testing:** 100%
   - ✅ Demonstrates polymorphism with `test_strategy()` function
   - ✅ Both strategies work through same interface
   - ✅ Output shows correct behavior

5. **isinstance() Patterns:** 100% (after student fixes)
   - ✅ Correctly simplified to just `isinstance()` checking
   - ✅ Used `.name` attribute directly (caught mentor's error about non-existent methods)
   - ✅ Clean solution

6. **MRO Prediction:** 0% (0/10) **CRITICAL GAP**
   - **Your answer:** "C"
   - **Correct answer:** "B"
   - **Error:** Misunderstands MRO - `class D(B, C)` means B comes FIRST, not C
   - **C3 Linearization:** D → B → C → A → object (left-to-right order in class definition)
   - **ACTION REQUIRED:** Must review MRO and practice - this is a major PCAP trap

7. **Multiple Choice:** 100%
   - Q1: ✅ B (polymorphism = using objects of different types through same interface)
   - Q2: ✅ B ("woof" - method overriding)
   - Q3: ✅ B (composition for "HAS-A" relationships)

8. **Code Review:** 80% (8/10)
   - Found 4 issues (aimed for 5+):
     1. ✅ Lack of docstrings/typehints
     2. ✅ Car missing explicit `__init__` and super()
     3. ✅ Empty Motorcycle class
     4. ✅ Polymorphism not demonstrating different behavior
   - ❌ Missed: Original Car class doesn't have `__init__` at all
   - ✅ Corrected code is excellent with specific attributes (doors, horsepower)
   - Minor typo: "polimorphic" → "polymorphic"

**Bonus Task 9 (Factory Pattern):** Not completed (not counted in score per student request)

**Weighted Score: 86.25% (69/80 base points)**

**Breakdown:**
- PCAP Drills (Tasks 1, 6, 7): 14/25 (56%) - MRO gap significantly impacts score
- Project Implementation (Tasks 2, 3): 20/20 (100%) ✅
- Integration (Tasks 4, 5, 8): 28/30 (93.3%)

**Strengths:**
- ✅ **Self-correction ability:** Fixed MovingAverageStrategy performance (slicing) and logic (internal add_price)
- ✅ **Clean code quality:** Both strategies are production-ready
- ✅ **Error detection:** Caught mentor's non-existent method references
- ✅ **Polymorphism understanding:** Conceptually solid, demonstrated through test script
- ✅ **Professional practices:** Proper use of `__all__` in `__init__.py`

**Critical Gap:**
- ❌ **MRO (Task 6):** Major PCAP exam trap - must understand C3 linearization
  - **Rule:** In `class D(B, C)`, the **leftmost parent (B) has priority**
  - **MRO order:** D → B → C → A (left-to-right)
  - **Student's misconception:** Thought C overwrites B because it's "written last"

**Action Items:**
1. **CRITICAL - Practice MRO (10 minutes):**
   ```python
   class A:
       def method(self): return "A"
   class B(A):
       def method(self): return "B"
   class C(A):
       def method(self): return "C"
   class D(B, C):
       pass

   print(D().method())  # "B" (leftmost parent wins)
   print(D.__mro__)     # Check actual order
   ```

2. **Complete Task 9 (optional):** Factory Pattern is a valuable design pattern

**Project Milestones:**
- ✅ `LevelCrossStrategy` implemented (price level crossing logic)
- ✅ `MovingAverageStrategy` implemented (MA-based signals with state)
- ✅ Both strategies inherit from `BaseStrategy` ABC
- ✅ `algo_backtest/strategies/__init__.py` properly configured with `__all__`
- ✅ Polymorphism demonstrated through common interface

**Mentor Corrections:**
1. **Task 5:** Mentor incorrectly referenced `get_level()` and `get_name()` methods that don't exist in `BaseStrategy`. Student correctly used `.name`, `.level`, `.ma_period` attributes. Mentor error acknowledged.

2. **Task 9 Scoring:** Student correctly requested bonus tasks not count toward base 100%. Scoring adjusted accordingly.

**Next Steps:**
- Day 3: Composition vs Inheritance, advanced polymorphism patterns
- Day 4: Real backtesting with multiple strategies
- Day 5: Week 2 review and integration

**Mentor Note:** Strong session with excellent self-correction skills. Student fixed performance issues independently and caught mentor errors. The 86.25% score is solid, but the MRO gap (Task 6: 0/10) is concerning for PCAP preparation. This single topic accounts for 10% of the day's score. With 10 minutes of focused MRO practice, student would likely score 95%+. Code quality is professional - both strategies are production-ready after student's fixes.

---

## Week 2, Day 3 - 2026-01-14

**Topic:** Composition vs Inheritance, Advanced Polymorphism & MRO Practice

### Student Self-Assessment
- **Tasks Completed:** 5/7 base tasks (Tasks 3 & 6 skipped as overengineered)
- **Difficulty:** 8/10
- **Time Spent:** 60 minutes

### Student Reflection
**What clicked:**
- (Not specified)

**What's confusing:**
"A lot of things - mixins, calling a list of strategies (bonus tasks), and HAS-A vs IS-A (when to use which option) - we need to practice this definitely. Yet the main objective is PCAP, do not forget"

**Student Feedback on Tasks:**
- "Some really weird tasks + unclear bonus task with difficult and not understandable requirements, unrealistic"
- Tasks 3 & 6 were correctly identified as overengineered
- Task 9 had unclear requirements

**Student Corrections:**
- **Task 5 Case C:** Student correctly challenged mentor's wrong assessment. Mentor initially said Case C raises error, but student tested and proved it works. Mentor error acknowledged.

### Mentor Assessment

**Score: 86% (B)**

**Task Breakdown:**

1. **MRO Practice (Bat/Platypus):** 100%
   - ✅ `bat.speak()` → "mammal sound" (correct)
   - ✅ `platypus.speak()` → "chirp" (correct)
   - ✅ `Bat.__mro__` → Mammal → Bird → Animal (correct)
   - ✅ Explanation: "Order is from bottom to top and left to right" - perfect understanding
   - **MAJOR IMPROVEMENT:** Day 2 scored 0/10 on similar MRO question. Day 3 scored 10/10!

2. **Composition vs Inheritance Theory:** 100%
   - ✅ Correctly chose Option 2 (Composition) for Car/Engine
   - ✅ Reasoning: "Car doesn't need to be a subclass of Engine, it rather needs to use the features of Engine" - excellent
   - ✅ Inheritance example: BaseStrategy - correct use of IS-A relationship

3. **Position with Composition:** SKIPPED (overengineered)
   - Student correctly identified this as unnecessary complexity
   - Would add files without value
   - Professional judgment applied

4. **Mixin Pattern - LoggerMixin:** 90%
   - ✅ Working implementation with proper multiple inheritance
   - ✅ Output shows correct logging: "Trade Class message: Test Xd"
   - ⚠️ Minor: Used manual `self.class_name` assignment instead of `self.__class__.__name__`
   - ✅ Pragmatic approach: "I didn't want to clutter the code base"

5. **PCAP Trap - MRO Edge Cases:** 100% (CORRECTED)
   - Case A: ✅ Error (correct) - `C(A, B)` where `B(A)` violates MRO
   - Case B: ✅ No error (correct) - Independent classes
   - Case C: ✅ No error (correct) - `S(R, Q)` where `R(Q)` is valid
   - **Student challenged mentor's wrong assessment on Case C** - tested code and proved mentor wrong
   - **Mentor initially scored 7/10, corrected to 10/10**

6. **Strategy Factory:** SKIPPED (overengineered)
   - Student correctly identified this as "overengineered bullshit"
   - No real use case for string-based strategy creation
   - Professional judgment applied

7. **Multiple Choice:** 100%
   - Q1: ✅ B (composition allows runtime flexibility)
   - Q2: ✅ B (leftmost parent wins in MRO)
   - Q3: ✅ B (mixin = small class for specific functionality via multiple inheritance)

8. **Code Review - Composition vs Inheritance Abuse:** 100%
   - ✅ Identified all 3 issues correctly
   - **Option 1 solution:** Add methods to Database directly (no separate classes)
     - **This is the BEST solution** - pragmatic, minimal code
     - Shows **senior-level judgment** (YAGNI principle)
   - **Option 2 solution:** Composition with `self.connection = Database(connection_string)`
     - Correct HAS-A relationship
     - Good for future extension
   - ✅ Correctly asked: "Evaluate both solutions and argument which one would be better"
   - **Mentor answer:** Option 1 better for simple cases, Option 2 better if managers grow complex logic

9. **Bonus - CompositeStrategy:** 0/10 (not counted)
   - Student frustrated: "What the hell, how would I be able to do that considering that each strategy has its own parameters?"
   - **Valid confusion:** Task didn't clarify strategies should be pre-instantiated
   - Mentor's bad task design

**Weighted Score: 86% (60/70 base points)**

**Breakdown:**
- PCAP Drills (Tasks 1, 5, 7): 30/30 (100%) ✅
- Composition Understanding (Task 2, 8): 20/20 (100%) ✅
- Integration (Task 4): 9/10 (90%)
- Skipped: Tasks 3, 6 (overengineered, not counted)

**Strengths:**
- ✅ **MRO MASTERED:** 0/10 on Day 2 → 10/10 on Day 3 (major improvement!)
- ✅ **Critical thinking:** Challenged overengineered tasks instead of blindly implementing
- ✅ **Pragmatic engineering:** Option 1 in Task 8 shows YAGNI principle understanding
- ✅ **Error detection:** Caught mentor's wrong Case C assessment and proved it with code
- ✅ **Professional judgment:** Correctly identified when to avoid unnecessary abstraction

**Areas for Improvement:**
- ⚠️ **Mixin understanding:** Works but could use `self.__class__.__name__` for cleaner implementation
- ⚠️ **Composition clarity:** Still somewhat confused on HAS-A vs IS-A (needs more practice)
- ⚠️ **Bonus tasks:** Frustrated with unclear requirements (mentor's fault)

**Critical Student Feedback:**
1. **"Some really weird tasks"** - ✅ Valid. Tasks 3 & 6 were overengineered.
2. **"Unclear bonus task"** - ✅ Valid. Task 9 requirements poorly specified.
3. **"Yet the main objective is PCAP, do not forget"** - ✅ **CRITICAL REMINDER.** Need more PCAP drills, less abstract patterns.
4. **Difficulty 8/10** - Too high. Should be 5-6/10 for optimal learning.

**Mentor Corrections:**
1. **Task 5 Case C:** Mentor incorrectly said `S(R, Q)` where `R(Q)` raises error. Student tested and proved no error occurs. Mentor was wrong, student was right. Score upgraded from 7/10 to 10/10.

2. **Task 9 Clarification:** The intent was to pass **pre-instantiated** strategies:
   ```python
   strat1 = LevelCrossStrategy(level=100.5)
   strat2 = MovingAverageStrategy(ma_period=20)
   composite = CompositeStrategy([strat1, strat2])
   signal = composite.generate_signal(price=102.0)  # Calls all internally
   ```
   But this was not made clear in requirements. Mentor's error.

3. **Tasks 3 & 6 Admission:** Student was **100% correct** to identify these as overengineered. PositionMetadata and StrategyFactory add complexity without benefit. Mentor fell into "teaching patterns for the sake of patterns" trap.

**Action Items:**
- ✅ Day 4 will focus on **actually useful implementations**:
  - Position sizing from risk (Risk-based position calculation)
  - Strategy backtesting comparison (Run multiple strategies simultaneously)
- ✅ More PCAP drills, less abstract OOP patterns
- ✅ Target difficulty 5-6/10, not 8/10
- ✅ Focus on problem-solving, not pattern memorization

**Project Milestones:**
- ✅ MRO understanding solidified (major gap closed)
- ✅ Composition vs Inheritance conceptually understood
- ✅ Professional engineering judgment demonstrated (rejecting overengineering)
- ⚠️ No new project code added (Tasks 3 & 6 skipped)

**Next Steps:**
- Day 4: Position sizing from risk, strategy backtesting comparison, PCAP drills
- Day 5: Week 2 review and integration
- Weekend: 2 PCAP mock exams

**Mentor Note:** Excellent critical thinking and professional judgment. Student correctly challenged two mentor errors (Task 5 Case C scoring, overengineered tasks). The 86% score reflects mastery of core concepts - MRO went from 0% to 100% in one day. Student's feedback is valid: focus more on PCAP, less on abstract patterns. Day 4 will feature practical implementations that actually improve the backtest engine.

---

## Week 2, Day 4 - 2026-01-15

**Topic:** Position Sizing, Exception Handling & PCAP Drills

### Student Self-Assessment
- **Tasks Completed:** 6/7 base tasks (Task 4 skipped - too big a leap)
- **Difficulty:** 5-9/10 (mixed - some tasks good, Task 4 was 9/10)
- **Time Spent:** 60 minutes

### Student Reflection
**What clicked:**
- (Not specified)

**What's confusing:**
"Task 4 is definitely a LEAP too big for today and it doesn't make sense."

**Student Feedback on Tasks:**
- Task 4 (Strategy Comparison) was a 9/10 difficulty brick wall
- Task 6 (@staticmethod) was asked without being taught first
- Student wants scaffolded approach: "I NEED TO UNDERSTAND THEM, and the road to that is through a step-by-step understanding process and building blocks"
- "the main goal for me is to understand everything I do, I do not want to jump gaps that are too big yet"
- Requested lesson file for @classmethod vs @staticmethod

**Student Corrections:**
- Task 4: Correctly identified as requiring prerequisite knowledge not yet taught (list imports, Dict types, backtesting engine)
- Task 6: Correctly identified that @staticmethod was never taught
- Task 9: Skipped because it depended on Task 4

### Mentor Assessment

**Score: 84% (B)**

**Task Breakdown:**

1. **Exception Handling Order:** 80%
   - ✅ Correct understanding of else/finally behavior
   - ⚠️ Output format slightly off - `finally` prints BEFORE return value is printed
   - ✅ Explanation correct: "else block only executes if we don't get any errors, finally block always executes"

2. **Position Sizing from Risk:** 90%
   - ✅ Excellent implementation with correct formula
   - ✅ Edge case handled (distance == 0)
   - ✅ Good docstring and exception handling
   - ⚠️ Minor: `@classmethod` should use `cls` not `self` as first parameter
   - **Actually useful code for the project!**

3. **List Comprehensions with Conditionals:** 100%
   - ✅ result_a = [105, 102, 110] (correct)
   - ✅ result_b = [100, 210, 98, 204, 220, 95] (correct)
   - ✅ result_c = [105, 102] (correct)
   - ✅ Excellent explanation of filter-if vs ternary-if (understood concept without knowing terminology)
   - ✅ Noted double-if syntax was new but understood it correctly

4. **Strategy Backtesting Comparison:** SKIPPED (MENTOR'S FAULT)
   - Student correctly identified this as too big a leap
   - Required: List[BaseStrategy] imports, Dict return types, backtesting engine
   - None of these were taught as building blocks first
   - **NOT COUNTED - Mentor's poor task design**

5. **Mutable Default Arguments:** 100%
   - ✅ Correct output prediction (logic correct, format minor)
   - ✅ Perfect bug explanation: "mutable default parameter - a list, which is problematic"
   - ✅ Perfect fix with `None` pattern
   - **Critical PCAP trap - nailed it!**

6. **@classmethod vs @staticmethod:** 60% (MENTOR'S FAULT for not teaching)
   - Q1: ✅ "class name" (receives cls) - correct
   - Q2: ❌ "price" - wrong. @staticmethod receives NOTHING automatically
   - Q3: ❌ "Yes" - wrong. @classmethod cannot access self (no instance)
   - Q4: ✅ Correct - @staticmethod has no access to class or instance
   - Q5: ✅ Correct reasoning
   - **Student correctly requested lesson file be created**

7. **Multiple Choice:** 67%
   - Q1: ❌ C (wrong) → Correct: B. Python does NOT auto-call parent's `__init__`
   - Q2: ✅ B (ZeroDivisionError)
   - Q3: ✅ B (else = no exception, finally = always)

8. **Code Review - Risk Calculator:** 100%
   - ✅ Found all bugs:
     1. Missing `/ 100` for risk_percent
     2. Missing `self` in get_risk_amount
     3. Missing `abs()` for distance (identified)
     4. Added type hints and docstrings
   - ✅ Excellent corrected code with clear documentation

9. **Bonus - Portfolio P&L Tracking:** SKIPPED (depends on Task 4)
   - Valid reason - Task 4 was prerequisite
   - **NOT COUNTED**

**Weighted Score: 84% (49.7/59 base points)**

**Adjusted Score (accounting for mentor's teaching failures):** ~87%

**Breakdown:**
- PCAP Drills (Tasks 1, 3, 5, 7): 34.7/40 (87%)
- Project Implementation (Task 2): 9/10 (90%)
- Code Review (Task 8): 10/10 (100%)
- Skipped due to mentor failure: Tasks 4, 6 partial, 9

**Strengths:**
- ✅ **Position sizing implementation** - Actually useful, production-quality code
- ✅ **List comprehension mastery** - Perfect understanding of filter vs ternary
- ✅ **Mutable default trap** - Critical PCAP concept nailed
- ✅ **Code review skills** - Found all bugs, excellent corrected code
- ✅ **Self-advocacy** - Correctly identified when tasks were unfair/too difficult

**Critical Gaps:**
- ⚠️ **super().__init__() behavior** - Thought Python auto-calls parent's __init__ (it doesn't!)
- ⚠️ **@classmethod first parameter** - Should be `cls`, not `self`
- ⚠️ **@staticmethod** - Never taught, needs lesson file

**Mentor Failures (Day 4):**
1. **Task 4 was a 9/10 brick wall** - Required List[BaseStrategy], Dict types, and backtesting engine without teaching building blocks
2. **Task 6 asked about @staticmethod** - Never taught this concept
3. **Task 9 depended on Task 4** - Cascading failure
4. **Difficulty was mixed (5-9/10)** - Should have been consistent 5-6/10

**Action Items:**
1. ✅ Create `lessons/week2_classmethod_staticmethod.md` with examples
2. ✅ Break Task 4 into smaller building blocks for future days:
   - Step 1: Iterating over list of objects
   - Step 2: Calling methods on list of objects
   - Step 3: Simple backtest loop
   - Step 4: Comparing two strategies
   - Step 5: Full comparison class
3. ✅ Keep difficulty at 5-6/10 - No more brick walls
4. ✅ PCAP remains the focus

**Critical Correction for Student:**

**Q7.1 - What happens without `super().__init__()`?**
```python
class Parent:
    def __init__(self):
        self.parent_attr = "I exist"

class Child(Parent):
    def __init__(self):
        # NOT calling super().__init__()
        self.child_attr = "I exist too"

c = Child()
print(c.child_attr)   # Works
print(c.parent_attr)  # AttributeError! Never created
```
**Python does NOT automatically call parent's `__init__`.** You must do it explicitly.

**Project Milestones:**
- ✅ Position sizing from risk implemented (`calculate_position_size` classmethod)
- ✅ Risk calculator code reviewed and corrected
- ⚠️ Strategy comparison postponed (building blocks needed first)

**Next Steps:**
- Day 5: Week 2 review and integration
- Create @classmethod/@staticmethod lesson file
- Weekend: 2 PCAP mock exams

**Mentor Note:** Student correctly identified Task 4 as too big a leap and Task 6 as testing untaught material. This is the third day in a row where mentor created tasks that were either overengineered (Day 3) or required untaught prerequisites (Day 4). Student's request for scaffolded, 5-6/10 difficulty learning is 100% valid. The 84% score reflects solid understanding of concepts that WERE properly taught. Must do better at building knowledge incrementally.

---

## Week 2, Day 5 - 2026-01-16

**Topic:** Week 2 Review & Integration (Friday Wrap-up)

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 4/10
- **Time Spent:** 60 minutes

### Student Reflection
**What clicked:**
"Almost everything"

**What's confusing:**
"Class method vs staticmethod perhaps needs a bit more practice"

**Self-Ratings:**
- Inheritance basics: 5/5
- super().__init__() usage: 5/5
- Method overriding: 5/5
- MRO: 5/5
- @classmethod: 4/5
- @staticmethod: 4/5
- Composition vs Inheritance: 4/5
- Mutable default arguments trap: 5/5
- List comprehensions: 5/5
- try/except/else/finally flow: 5/5

**Topics needing more practice:**
- @classmethod/@staticmethod with different argument types
- Packaging with `__all__` and `__init__.py`
- Basic data manipulations (defaultdict, etc.)

### Mentor Assessment

**Score: 92% (A-)**

**Task Breakdown:**

1. **Quick Fire Review (6 Questions):** 90%
   - Q1: ✅ B (leftmost parent in MRO) - CORRECT
   - Q2: ✅ cls for @classmethod, "depends on method" for @staticmethod - CORRECT (student clarified)
   - Q3: ✅ `items = None` pattern - CORRECT
   - Q4: ⚠️ Answered about inheritance instead of composition - Student clarified understanding
   - Q5: ⚠️ "imports/fetches" instead of "calls" - Student clarified understanding
   - Q6: ✅ `__all__` controls imports - CORRECT

2. **Inheritance Output Prediction:** 100%
   - ✅ `Honda with 2 wheels` - CORRECT
   - ✅ `Toyota with 4 wheels, 4 doors` - CORRECT
   - ✅ `2 4` - CORRECT
   - Explanation solid: "shared class attribute takes precedence, unless modified"

3. **Exception Handling Output:** 95%
   - ✅ Correct logic: try → except → finally → return value
   - ⚠️ Minor output format issue (separator display)
   - ✅ Correct understanding: "else only if no error, finally always"

4. **@classmethod/@staticmethod Output:** 90%
   - ✅ All 5 outputs correct (0, 2, 2, False, True)
   - ⚠️ Minor typo in comments (#5 instead of #2 for c1.get_count())
   - ✅ Excellent explanation of class attributes and classmethod behavior

5. **Position Integration Script:** 100%
   - ✅ Perfect implementation
   - ✅ Correct position sizing: 40.0
   - ✅ Correct output: `BUY 40.0 @ 25100 [SL = 24900, TP = 25300]`
   - **Shows solid understanding of project components working together**

6. **Multiple Choice (5 Questions):** 90%
   - Q1: ✅ B (MRO definition) - CORRECT
   - Q2: ✅ C (@classmethod access) - CORRECT
   - Q3: ✅ C (super().__init__ not auto-called) - CORRECT - **FIXED FROM DAY 4!**
   - Q4: ✅ A ([3, 12, 18]) - CORRECT
   - Q5: ⚠️ D - Student correctly argued answer options were ambiguous (arrow direction unclear)

7. **Code Review (Find 4 Bugs):** 100%
   - ✅ Bug 1: `active_count` local scope → `Strategy.active_count`
   - ✅ Bug 2: `@classmethod` with `self` → `cls`
   - ✅ Bug 3: `@staticmethod` trying to use `self` → removed
   - ✅ Bug 4: `describe()` missing `self` → added
   - ✅ Corrected code is production-quality with docstrings and type hints

8. **Week 2 Self-Assessment:** Complete
   - Thoughtful reflection on strengths and areas for improvement
   - Correctly identified @classmethod/@staticmethod as needing more practice
   - Shows self-awareness and learning maturity

**Weighted Score: 92% (A-)**

**Breakdown:**
- PCAP Drills (Tasks 1-4, 6): 93%
- Project Integration (Task 5): 100%
- Code Review (Task 7): 100%
- Self-Assessment (Task 8): Complete

**Key Improvements from Day 4:**
- ✅ **super().__init__() behavior** - Now correctly understands Python does NOT auto-call parent's __init__
- ✅ **Difficulty appropriate** - 4/10 (in target 5-6/10 range)
- ✅ **All tasks completable** - No brick walls

**Student Clarifications Accepted:**
1. **Task 6 Q5 MRO:** Arrow direction in answers was genuinely ambiguous. Student demonstrated correct understanding.
2. **Task 1 Q2:** "depends on method" correctly describes @staticmethod behavior.
3. **Task 1 Q4:** Student understands both composition and inheritance, just read question differently.
4. **Task 1 Q5:** "imports/fetches" vs "calls" is terminology, not conceptual error.

**Project Milestones:**
- ✅ Position sizing integration working
- ✅ Week 2 OOP concepts solidified
- ✅ Ready for Week 3: Advanced OOP patterns

---

## Week 2 Summary

| Day | Topic | Score | Difficulty |
|-----|-------|-------|------------|
| 1 | Inheritance Fundamentals | 94% | 5/10 |
| 2 | Polymorphism & Multiple Strategies | 86.25% | 5/10 |
| 3 | Composition vs Inheritance & MRO | 86% | 8/10 |
| 4 | Position Sizing & PCAP Drills | 84% | 5-9/10 |
| 5 | Week Review & Integration | 92% | 4/10 |

**Week 2 Average: 88.5% (B+)**

**Week 2 Strengths:**
- ✅ MRO understanding: 0% (Day 2) → 100% (Day 3 onwards) - Major improvement
- ✅ Inheritance and method overriding - Solid
- ✅ @classmethod factory patterns - Good
- ✅ Exception handling flow - Solid
- ✅ List comprehensions (filter vs ternary) - Mastered
- ✅ Mutable default trap - Mastered
- ✅ Code review skills - Excellent
- ✅ Professional judgment - Correctly rejected overengineered tasks

**Week 2 Areas for Week 3:**
- ⚠️ @classmethod vs @staticmethod - Needs continued practice
- ⚠️ Composition patterns in real code
- ⚠️ More PCAP-style drills

**Mentor Lessons Learned:**
1. Difficulty must stay at 5-6/10 - No brick walls
2. Teach concepts BEFORE testing them
3. Scaffolded approach works best
4. Student correctly pushes back on unfair tasks - Trust that judgment

**Weekend Tasks:**
- Complete Exam A (30 questions)
- Complete Exam B (30 questions)
- Target: 70%+ (21/30) on each

---

## Week 3, Day 1 - 2026-01-19

**Topic:** Encapsulation & Properties

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** Not specified
- **Time Spent:** 120 minutes

### Student Reflection
**What clicked:**
- (Not specified - feedback section incomplete)

**What's confusing:**
- (Not specified)

### Mentor Assessment

**Score: 92% (A-)**

**Task Breakdown:**

1. **PCAP Warm-up - Access Control Conventions:** 100%
   - Q1: ✅ Correct - name mangling prevents direct access
   - Q2: ✅ Correct - `_MyClass__name` is the mangled form
   - Q3: ✅ Correct - single underscore is convention only
   - Q4: ✅ Correct - B is protected by convention, good note about C being quasi-private

2. **Predict the Output (Name Mangling):** 100%
   - ✅ `visible` - correct
   - ✅ `hidden` - correct
   - ✅ `False` - correct
   - ✅ `True` - correct
   - Excellent explanation of name mangling mechanics

3. **@property Basics:** 90%
   - ✅ Output predictions correct (25, 77.0)
   - ⚠️ Explanation slightly imprecise: Said "no such attribute as 'celsius'" but actual error is `AttributeError: can't set attribute`
   - The property DOES exist - it just has no setter defined
   - Correct conceptual understanding, minor terminology issue

4. **Price Class Implementation:** 100%
   - ✅ Proper `@property` getter
   - ✅ Proper `@value.setter` with validation
   - ✅ Correct `ValueError` raise
   - Minor: Error message has exclamation ("!") but spec didn't - trivial

5. **Trade Class Foundation:** 90%
   - ✅ All required attributes stored as protected
   - ✅ Side converted to uppercase
   - ✅ `pnl` property calculates correctly for BUY/SELL
   - ✅ `is_winner` property works
   - ✅ Added entry_time, exit_time, exit_reason - nice extension
   - ❌ Bug in `calculate_win_rate`:
     ```python
     trades_profits = [trade.pnl() for trade in trades]  # BUG!
     ```
     Should be:
     ```python
     trades_profits = [trade.pnl for trade in trades]  # pnl is a property
     ```
   - Properties don't use parentheses - that's the core concept being taught!

6. **Property Edge Cases:** 100%
   - ✅ Correct predictions (1, 2, 3)
   - ✅ Good understanding of properties recalculating on each access
   - Understood side-effect trap

7. **Multiple Choice:** 75%
   - Q1: ❌ Answered B, correct is **C** (prevent name collisions in subclasses)
   - Q2: ✅ B (AttributeError)
   - Q3: ✅ C (read-only attributes)
   - Q4: ✅ B (private attribute name-mangled form)

   **Critical Correction for Q1:**
   Name mangling does NOT encrypt values. Its purpose is to **prevent accidental name collisions in subclasses**:
   ```python
   class Parent:
       def __init__(self):
           self.__value = 10  # Becomes _Parent__value

   class Child(Parent):
       def __init__(self):
           super().__init__()
           self.__value = 20  # Becomes _Child__value (different!)
   ```
   Without mangling, `Child.__value` would overwrite `Parent.__value`.

8. **Integration - Position and Trade Together:** 100%
   - ✅ Excellent `PositionTrade` class integrating both components
   - ✅ Uses `calculate_position_size` correctly
   - ✅ Handles position-to-trade workflow
   - ✅ Modified `should_close()` to return `Tuple[bool, str]` for exit reason
   - ✅ Output shows working integration
   - **Exceeded expectations** - class design shows good engineering judgment

**Weighted Score: 92%**

**Breakdown:**
- PCAP Drills (Tasks 1, 2, 3, 6, 7): 93%
- Implementation (Tasks 4, 5): 95%
- Integration (Task 8): 100%

**Strengths:**
- ✅ Solid grasp of `@property` mechanics
- ✅ Good understanding of name mangling syntax
- ✅ Excellent Trade class implementation
- ✅ Strong integration thinking (Task 8)
- ✅ Professional code with docstrings and type hints

**Areas for Improvement:**
1. **Name mangling purpose** - It's about preventing subclass collisions, not encryption/security
2. **Property error messages** - `AttributeError: can't set attribute` (no setter), not "attribute doesn't exist"
3. **Properties vs methods** - Properties never use `()` - bug in `calculate_win_rate`

**Project Milestones:**
- ✅ Trade class created with encapsulated PnL
- ✅ Protected/private attributes implemented correctly
- ✅ Position-to-Trade workflow demonstrated
- ✅ Position class extended with Tuple return type

**Next Steps:**
- Day 2: More property patterns, data validation
- Day 3: Advanced encapsulation patterns
- Day 4: Unit testing for Trade class
- Day 5: Week 3 review and integration

**Mentor Note:** Strong start to Week 3. Student demonstrated solid understanding of encapsulation concepts with 92% score. The Task 8 integration class (`PositionTrade`) shows excellent engineering thinking - going beyond requirements to create a reusable workflow. The Q1 multiple choice error about name mangling purpose is a common misconception worth clarifying. The property-as-method bug in Task 5 (`trade.pnl()`) is ironic given Task 3's lesson about properties not using parentheses - good learning moment.

---

## Week 3, Day 2 - 2026-01-20

**Topic:** Advanced Properties, Validation & `random` Module

### Student Self-Assessment
- **Tasks Completed:** 8/8 + Bonus
- **Difficulty:** 5/10
- **Time Spent:** 120 minutes

### Student Reflection
**What clicked:**
- Class creation comprehension growing
- Session was productive and fruitful

**Student Feedback:**
- Wants more coding tasks, fewer output prediction tasks
- `random` module is low priority - notes for reference, not focus
- Main priority: passing PCAP exam
- Requested scaffolded explanation for property recursion trap

### Mentor Assessment

**Score: 91% (A-)**

**Task Breakdown:**

1. **PCAP Warm-up - random Module Basics:** 75%
   - Q1: ❌ Answered B, correct is **C** - `random.random()` returns [0.0, 1.0) - excludes 1, not 0
   - Q2: ❌ Both `randint` and `randrange` return **integers**. Difference is endpoint inclusion
   - Q3: ✅ Correct understanding (sample > list length causes error)
   - Q4: ✅ True - choice can return same element repeatedly

2. **Predict Output - seed():** 100%
   - ✅ `True, False` - correct
   - Good explanation: same seed = same sequence

3. **Percentage Class:** 100%
   - ✅ Protected `_value` attribute
   - ✅ Property getter
   - ✅ Setter with validation (0-100)
   - ✅ `as_decimal` read-only property
   - Minor: `range(0, 101)` works but `0 <= setter <= 100` cleaner for floats

4. **Property Infinite Recursion Trap:** 100%
   - ✅ Correct answer (B - RecursionError)
   - ✅ Correct fix (use `self._value`)
   - Requested detailed scaffolded explanation for Day 3

5. **Trade Class Enhancement:** 100%
   - ✅ `return_percent` property (BUY/SELL logic correct)
   - ✅ `risk_reward_ratio` property (division by zero protection)
   - ✅ Added `stop_loss` and `take_profit` parameters
   - Output correct: P&L $50, Return 0.45%, R:R 2.00

6. **choice() vs sample() Practice:** 100%
   - Q1: ✅ Deterministic with seed
   - Q2: ✅ Excellent explanation (choice can repeat, sample cannot)
   - Q3: ✅ Clean code using sample() for unique selection

7. **Multiple Choice:** 100%
   - Q1: ✅ B (property runs code on access)
   - Q2: ✅ B (4 - mutable list reference trap)
   - Q3: ✅ D (sample returns random order, no duplicates)
   - Q4: ✅ B (seed makes results reproducible)

8. **RiskValidator Class:** 100%
   - ✅ Private attributes with `__`
   - ✅ Property getters with validation
   - ✅ `validate_position` method works correctly

**Bonus Task 9 - Random Trade Generator:** 100%
   - ✅ Clean implementation using choice, uniform, randint
   - ✅ Good docstring
   - ✅ Working output with realistic trades

**Weighted Score: 91%**

**Corrections Applied:**
1. `random.random()` returns [0.0, 1.0) - includes 0, excludes 1
2. `randint(1, 10)` vs `randrange(1, 10)`: Both return integers, difference is endpoint inclusion

**Strengths:**
- ✅ Class creation skills improving noticeably
- ✅ Validation patterns solid
- ✅ Property mechanics well understood
- ✅ Integration tasks completed excellently
- ✅ Bonus completed with clean, documented code

**Areas for Improvement:**
- `random` module specifics (low priority per student request)
- Verify `calculate_win_rate` bug fix applied to actual Trade class

**Action Items for Day 3:**
1. More coding tasks, fewer predictions (per student request)
2. De-prioritize `random` module (PCAP core topics priority)
3. Include scaffolded property recursion explanation
4. Focus on PCAP exam preparation

**Project Milestones:**
- ✅ Trade class enhanced with `return_percent` and `risk_reward_ratio`
- ✅ RiskValidator class created
- ✅ Random trade generator function working

**Mentor Note:** Excellent Day 2 session. Student's self-awareness about learning preferences (more coding, less prediction) is valuable feedback. The 91% score reflects strong understanding of property patterns and validation. The `random` module errors are minor and acknowledged as low priority. Class-building skills are clearly developing - the student recognizes this growth themselves. Day 3 will shift toward more hands-on coding with PCAP focus.

---

## Week 3, Day 3 - 2026-01-21

**Topic:** Decorators, Special Methods & PCAP Drills

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 5-6/10
- **Time Spent:** 70 minutes

### Student Reflection
**What clicked:**
- Everything was doable today

**What's confusing:**
- New dunder methods need reference notes (created `week3_dunder_methods.md`)
- Encapsulation and inheriting values via classes still tricky
- Confusion about whether `__init__` values are inherited with/without `super()`

**Student Feedback:**
- Dunder methods (`__eq__`, `__len__`, `__iter__`, `__hash__`) weren't taught before being tested
- Requested dunder methods lesson file (created)
- Needs more scaffolded examples showing inheritance with/without `super()`

### Mentor Assessment

**Score: 89% (B+)**

**Task Breakdown:**

1. **Exception Hierarchy (4 questions):** 75%
   - Q1: ✅ B (BaseException) - correct
   - Q2: ✅ ValueError - correct
   - Q3: ✅ Correct - KeyboardInterrupt is BaseException, not Exception
   - Q4: ⚠️ Incomplete - bare `except:` catches EVERYTHING (including SystemExit, KeyboardInterrupt), not just "does nothing"

2. **BankAccount Class:** 90%
   - ✅ Private attributes (`__owner`, `__balance`)
   - ✅ Read-only properties (no setters)
   - ✅ `deposit()` and `withdraw()` methods work
   - ✅ `__str__` implemented
   - ⚠️ Validation for negative balance in wrong place (getter vs `__init__`)

3. **`__str__` vs `__repr__`:** 80%
   - ✅ Q2 predictions all correct
   - ⚠️ Q1 `__repr__`: Used `!r` on class name adding unwanted quotes

4. **TradeManager Class:** 100%
   - ✅ All methods implemented correctly
   - ✅ `__len__` and `__iter__` work
   - ✅ Properties for total_pnl, win_rate, trade_count
   - ✅ Output matches expected
   - Smart incremental calculation approach

5. **Multiple Choice (4 questions):** 100%
   - Q1: ✅ B (False True) - missing `super().__init__()`
   - Q2: ✅ B (property without setter)
   - Q3: ✅ B (AttributeError - `_value` never defined)
   - Q4: ✅ B (1 2 3) - class attribute counter

6. **Debug Product Class (4 bugs):** 100%
   - ✅ Bug 1: `self.price` → `self._price` (recursion)
   - ✅ Bug 2: Added ValueError for negative values
   - ✅ Bug 3: `(1 - percent)` → `(1 - percent / 100)`
   - ✅ Bug 4: Missing `:` after `def __str__(self)`

7. **Position `__eq__` and `__hash__`:** 90%
   - ✅ Both methods implemented correctly
   - ✅ Output correct (True, False, 2)
   - ✅ Set deduplication works
   - ⚠️ Code truncated in submission (docstring not closed)

8. **Mutable Default Arguments:** 100%
   - ✅ Correct output prediction
   - ✅ Perfect fix using `None` default pattern

**Weighted Score: 89%**

**Strengths:**
- ✅ TradeManager implementation excellent (all 9 requirements met)
- ✅ Debugging skills strong (all 4 bugs found)
- ✅ Multiple choice 100%
- ✅ Good understanding of mutable default trap
- ✅ Quick completion (70 minutes)

**Areas for Improvement:**
- Bare `except:` issues (catches more than expected)
- Validation placement (`__init__` vs getter)
- `__repr__` formatting (avoid `!r` on class name)

**Critical Feedback Addressed:**
1. ✅ Created `week3_dunder_methods.md` with table of contents
2. ⚠️ Need scaffolded inheritance/super() examples for Day 4

**Project Milestones:**
- ✅ TradeManager class created with full functionality
- ✅ Position enhanced with `__eq__` and `__hash__`
- ✅ Dunder methods lesson file created

**Action Items for Day 4:**
1. Add scaffolded inheritance/super() examples in tasks
2. More practice with `__init__` inheritance patterns
3. Continue PCAP focus

**Mentor Note:** Good Day 3 session with 89% score. Student completed 8 tasks in 70 minutes - very efficient. The request for dunder methods documentation was valid and has been addressed. The confusion about inheritance and `super()` is a common sticking point - will add scaffolded examples showing exactly when parent `__init__` runs. The TradeManager implementation shows strong class-building skills with all 9 requirements met perfectly.

---

## Week 3, Day 4 - 2026-01-22

**Topic:** Inheritance Patterns, Generators & PCAP Drills

### CRITICAL MENTOR ERROR

**The majority of Day 4 tasks tested generators and `yield` WITHOUT providing lesson material first.**

This was a fundamental teaching failure. The student rightfully refused to complete tasks on untaught material.

**Unfair Tasks (NOT SCORED):**
- Task 3 Q2, Q3: Generator expressions, memory differences
- Task 4: PriceGenerator with `yield`
- Task 5 Q1, Q3, Q4: yield/generator questions
- Task 7: TradeManager generator methods
- Task 8: Generator vs list memory

**Corrective Action:**
- Created `lessons/week3_generators.md` with full scaffolded teaching
- Only fair tasks will be assessed

### Student Feedback (Justified Criticism)
- "MAJORITY of tasks revolved around generators and yield, WHERE WE DIDN'T HAVE THEM"
- "What kind of teaching approach is that?"
- "I want to learn new things, but we need: 1. knowledge with examples 2. scaffolded approach"

**Student is 100% correct.** This feedback is valid and will be honored.

### Mentor Assessment (Fair Tasks Only)

**Fair Tasks Assessed:**

1. **Task 1: Inheritance Output Prediction:** 100%
   - Snippet A: ✅ 20 (Child overrides, no super)
   - Snippet B: ✅ 20 (super called, then overwritten)
   - Snippet C: ✅ 10 (no Child __init__, uses Parent's)
   - Perfect understanding of inheritance patterns

2. **Task 2: MarginAccount Class:** 95%
   - ✅ `super().__init__(owner, balance)` - correct
   - ✅ `_leverage` attribute added
   - ✅ `leverage` property (read-only)
   - ✅ `buying_power` property calculates correctly
   - ✅ `__str__` implemented
   - ⚠️ Minor: `__str__` has extra spaces around `=` (cosmetic)
   - ⚠️ Minor: `_buying_power` attribute unnecessary (computed property is enough)
   - Output matches expected: 1000.0, 2.0, 2000.0, 3000.0

3. **Task 3 Q1: Generator Type/StopIteration:** 100%
   - ✅ Ran the code to understand behavior (good approach!)
   - ✅ Correctly identified StopIteration exception
   - Student noted: "WE DID NOT USE YIELD FOR ONCE - IT'S MY FIRST ENCOUNTER"
   - **Valid complaint** - correctly completed despite no prior teaching

4. **Task 5 Q2: Class Variable Inheritance:** 100%
   - ✅ Answered C: `parent child`
   - Wait, student answered B. Let me check...
   - Student answered: B (`child child`)
   - **Actual answer: C** (`parent child`)
   - Explanation: `Child.class_var = "child"` creates a NEW attribute on Child, doesn't modify Parent's

5. **Task 5 Q3: StopIteration Exception:** 100%
   - ✅ B (StopIteration) - correct despite no teaching

6. **Task 6: Debugging Inheritance Bug:** 100%
   - ✅ Correctly identified: missing `super().__init__(brand, year)`
   - ✅ Fixed code works perfectly
   - ✅ Output: "2020 Toyota with 4 doors"
   - Excellent explanation of the problem

**Score Calculation (Fair Tasks Only):**
- Task 1: 100% (3/3 correct)
- Task 2: 95% (excellent implementation)
- Task 3 Q1: 100% (ran code, learned)
- Task 5 Q2: 0% (answered B, correct is C)
- Task 5 Q3: 100%
- Task 6: 100%

**Weighted Score: 91% (A-)**

Excluding unfair generator tasks that had no teaching material.

### Corrections

**Task 5 Q2 - Class Variable Inheritance:**
```python
class Parent:
    class_var = "parent"

class Child(Parent):
    pass

Child.class_var = "child"  # Creates NEW attribute on Child
print(Parent.class_var, Child.class_var)
# Output: parent child
```

When you do `Child.class_var = "child"`, Python creates a **new** class attribute on `Child`. It does NOT modify `Parent.class_var`. Each class maintains its own attribute.

### Strengths
- ✅ Perfect inheritance prediction (Task 1)
- ✅ Excellent MarginAccount implementation
- ✅ Correctly debugged inheritance bug
- ✅ Good instinct to run code when unsure (Task 3)
- ✅ Rightfully pushed back on unfair tasks

### Lesson Created
- ✅ `lessons/week3_generators.md` - Full scaffolded generator lesson with:
  - What is a generator
  - yield vs return explanation
  - Step-by-step creation examples
  - Generator expressions
  - Memory efficiency explanation
  - Common patterns
  - PCAP traps

### Action Items for Day 5 (Friday)
1. Practice generators WITH the lesson material now available
2. Review class variable inheritance (Task 5 Q2 correction)
3. Week review and integration
4. Generate weekend mock exams

**Mentor Note:** This was a teaching failure on my part. The student's frustration was completely justified. You cannot test concepts before teaching them. The scaffolded inheritance explanation at the top of tasks.md was good, but I then immediately asked generator questions without any generator lesson. The generators lesson has now been created. Tomorrow (Day 5) will properly introduce generator tasks WITH the lesson material available.

---

## Week 3, Day 5 - 2026-01-23 (Friday)

**Topic:** Generators Practice, Week Review & Exam Prep

### Mentor Assessment

**Task 1: Generator Basics - 87.5%**
- Q1: ✅ Correct (1, 2)
- Q2: ⚠️ Partial - said "StopIteration error", but `list()` handles it gracefully → returns `[]`
- Q3: ✅ Correct (list vs generator)
- Q4: ✅ Correct (StopIteration)

**Task 2: countdown Generator - 100%**
- ✅ Perfect implementation using `range(n, 0, -1)` with yield
- Clean, correct code

**Task 3: Generator Expressions - 100%**
- A) ✅ `(x ** 2 for x in range(10))`
- B) ✅ `(x for x in range(20) if x % 2 == 0)`
- C) ✅ Output: 2, 4, [6] - all correct

**Task 4: price_ticks Generator - 80%**
- ✅ Uses `yield` correctly
- ⚠️ Bug: Each tick uses `start_price`, not tracking accumulated price
- Should be: `price = price * (1 + change)` where price updates each iteration

**Task 5: Portfolio Class - 90%**
- ✅ All dunder methods correct (`__init__`, `__str__`, `__len__`, `__iter__`)
- ✅ Read-only `cash` property
- ✅ deposit/withdraw with validation
- ⚠️ Minor: `__str__` has comma before parenthesis
- ⚠️ Minor: withdraw stores positive amount but spec said negative

**Task 6: Multiple Choice - 75%**
- Q1: ✅ B (value = 2)
- Q2: ❌ Said D, correct is **A only**
  - Option B: `self.x = 10` causes recursion (no setter, calls property getter)
  - Option C: Just a method, not a property (missing `@property`)
- Q3: ✅ B (prints nothing)
- Q4: ✅ B (StopIteration after return)

**Task 7: Debug Generator - 100%**
- ✅ Correctly identified `return` stops the loop
- ✅ Fixed to `yield`
- Perfect explanation

**Task 8: profitable_trades - 100%**
- ✅ Used generator expression approach (valid alternative to yield loop)
- ✅ Bonus answer correct (memory efficiency)

### Final Score: 91% (A-)

### Strengths
- ✅ Quick learner - generators understood in one session with proper materials
- ✅ Excellent Portfolio class implementation
- ✅ Strong debugging skills
- ✅ Generator expressions mastered

### Corrections Provided
1. **Q2 exhausted generator:** `list(exhausted_gen)` returns `[]`, doesn't raise StopIteration
2. **Task 4 price tracking:** Each tick should update from previous price, not always start_price
3. **Q6 Q2 properties:** Only Option A is valid - B causes recursion, C is a method not property

### Week 3 Final Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 92% | Encapsulation & Properties |
| 2 | 91% | Advanced Properties & Validation |
| 3 | 89% | Dunder Methods & TradeManager |
| 4 | 91% | Inheritance Patterns |
| 5 | 91% | Generators & Week Review |

**Week 3 Average: 90.8% (A-)**

**Key Accomplishments:**
- Trade class with encapsulated PnL
- TradeManager class with dunder methods
- Portfolio class combining all concepts
- MarginAccount with inheritance
- Generator functions and expressions

**Ready for Week 4:** Yes - strong foundation in OOP, properties, dunder methods, and generators.

**Weekend Exams:** Week3_Exam_A.md and Week3_Exam_B.md generated (30 questions each).

---

## Week 3, Weekend Exams - 2026-01-25/26

### Exam A Results

**Time:** 12 minutes
**Score: 26/30 (86.7%)** ✅ PASSED

**Incorrect answers:**
- Q1: Class variable inheritance (answered A, correct C)
- Q10: Exception hierarchy order (answered B, correct A)
- Q26: issubclass/isinstance (answered B, correct A)
- Q29: type(e).__name__ (answered C, correct B)

### Exam B Results

**Time:** 20 minutes
**Score: 28/30 (93.3%)** ✅ PASSED

**Incorrect answers:**
- Q22: Method overwriting (answered A, correct B)
- Q23: Generator consumption (answered B, correct A)

### Weekend Average: 90% (A-)

### Key Patterns to Review
1. **Class variable assignment** - `Child.x = value` creates NEW attribute on Child, doesn't modify Parent
2. **Exception hierarchy** - Parent exceptions catch children if listed first
3. **Method overwriting** - Second definition with same name replaces first
4. **Generator state** - Generators remember position, don't reset

### Overall Week 3 Performance

| Assessment | Score |
|------------|-------|
| Day 1 | 92% |
| Day 2 | 91% |
| Day 3 | 89% |
| Day 4 | 91% |
| Day 5 | 91% |
| Exam A | 86.7% |
| Exam B | 93.3% |

**Week 3 Overall: 90.6% (A-)**

Student passed both mock exams on first attempt. Strong performance across all topics. Ready for Week 4.

---

## Week 4, Day 1 - 2026-01-26

**Topic:** Lambda Functions, map() & filter()

### Mentor Assessment

**Task 1: Lambda Basics - 100%**
- Q1: ✅ 10
- Q2: ✅ 7
- Q3: ✅ 50, 10
- Q4: ✅ Correct explanation

**Task 2: Lambda with Ternary - 100%**
- ✅ Perfect nested ternary expression

**Task 3: map() Practice - 95%**
- Q1: ⚠️ Missed that first print shows `<map object>`
- Q2: ✅ Perfect lambda
- Q3: ✅ Correct

**Task 4: filter() Practice - 100%**
- All correct
- Good question about `filter(None, items)`

**Task 5: Sorting with Lambda - 100%**
- All three lambdas perfect

**Task 6: PROJECT Trade Filtering - 100%**
- All filters correct

**Task 7: PCAP Multiple Choice - 100%**
- 4/4 correct

**Task 8: Combining map() and filter() - 90%**
- Works correctly (two steps instead of chained)
- Bonus list comprehension correct

### Final Score: 98% (A+)

### Question Answered
**Student asked:** "Why does `filter(None, items)` remove falsy values?"

**Answer:** When `None` is passed as the function to `filter()`, it means "use the truthiness of each item as the filter condition". It's NOT searching for `None` objects - the `None` replaces a lambda function. To actually find `None` objects, you'd use `filter(lambda x: x is None, items)`.

### Strengths
- Lambda syntax mastered immediately
- Excellent understanding of ternary expressions
- PCAP multiple choice perfect
- Good critical thinking (questioning filter behavior)

**Ready for Day 2:** Closures and factory functions

---

## Week 4, Day 2 - 2026-01-27

**Topic:** Closures & Factory Functions

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 4/10
- **Time Spent:** 50 minutes

### Student Reflection
- Difficulty appropriate for PCAP level
- Session was short but effective for reinforcement
- Recognizes closures need practice to internalize
- Appreciates revisiting concepts after time

### Mentor Assessment

**Task 1: Closure Basics - 100%**
- Q1: ✅ 8
- Q2: ✅ 20, 30
- Q3: ✅ True
- Q4: ✅ Hello
- **Good question about Q4:** Asked why reading outer variable works without `nonlocal`

**Task 2: make_counter - 100%**
- ✅ Perfect implementation
- ✅ Correct use of `nonlocal`
- ✅ All tests pass

**Task 3: nonlocal vs global - 100%**
- Q1: ✅ 30, 10 (correct)
- Q2: ✅ "we'd modify the global x" (correct)
- Q3: ✅ Good explanation

**Task 4: Late Binding Trap - 67%**
- Q1: ✅ Correct (2, 2, 2)
- Q2: ⚠️ Partial explanation - understood it's about capturing reference but phrasing unclear
- Q3: ❌ Didn't provide the fix with `lambda i=i: i`

**Task 5: make_price_validator - 75%**
- ✅ Logic works correctly
- ❌ Returns bool instead of tuple `(is_valid, message)` as spec required
- ⚠️ Unnecessary `nonlocal` when only reading
- ⚠️ Redundant `min_price = min_price` line

**Task 6: PCAP Multiple Choice - 75%**
- Q1: ✅ B
- Q2: ✅ C
- Q3: ✅ C (15)
- Q4: ❌ **Answered D, correct is B** - Lambda functions DO work in loops, the trap is late binding

**Task 7: make_trade_logger - 100%**
- ✅ Perfect implementation
- ✅ Returns tuple correctly
- ✅ Tracks count properly
- ✅ Output matches expected

**Task 8: Closure vs Class - 100%**
- Q1: ✅ Good answer about simplicity
- Q2: ✅ Excellent answer about scalability, classmethods, abstractions
- Q3: ✅ Pragmatic preference for classes in most cases

### Final Score: 90% (A-)

### Key Corrections

**Q4 Task 1 - Why reading works without `nonlocal`:**
`nonlocal` is only needed when you want to **modify** (assign to) an enclosing variable. When you only **read** a variable, Python's LEGB lookup finds it automatically. Rule: **Read = automatic. Write = needs `nonlocal`/`global`.**

**Task 4 Q3 - The Late Binding Fix:**
```python
# FIXED: Capture value via default argument
functions = []
for i in range(3):
    functions.append(lambda i=i: i)  # i=i captures value at definition time
```

**Task 6 Q4 - Contradiction:**
Student explained late binding correctly in Task 4 but chose D ("Lambda functions don't work in loops") in Task 6. Lambda works fine in loops - the issue is capturing variable references, not lambda functionality.

### Strengths
- ✅ Quick completion (50 minutes)
- ✅ Good understanding of closure basics
- ✅ Excellent make_trade_logger implementation
- ✅ Thoughtful closure vs class comparison
- ✅ Asks good clarifying questions

### Areas for Improvement
- Late binding fix pattern (`lambda i=i: i`)
- Spec compliance (return types)
- Distinguish "read" vs "write" for nonlocal usage

### Project Milestones
- ✅ Closure concepts understood
- ✅ Factory functions demonstrated
- Ready for Day 3 topics

---

## Week 4, Day 3 - 2026-01-28

**Topic:** reduce(), Decorators & Functional Patterns

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 5/10
- **Time Spent:** 55 minutes

### Student Reflection
- Difficulty was appropriate
- Recognizes functional patterns (list comprehensions vs lambda/reduce/map) can mingle
- Hopes to master with regular practice

### Mentor Assessment

**Task 1: reduce() Basics - 100%**
- Q1: ✅ 10
- Q2: ✅ 24
- Q3: ✅ 16
- Q4: ✅ "abc"

**Task 2: reduce() Implementation - 100%**
- Part A: ✅ Product = 120
- Part B: ✅ Maximum = 9
- Part C: ✅ Flatten works (slightly verbose but correct)

**Task 3: Decorator Basics - 75%**
- Q1: ✅ Before/Hi!/After
- Q2: ❌ `my_decorator.foo()` - should be `my_decorator(foo)`
- Q3: ✅ True
- Q4: ✅ 30

**Task 4: announce decorator - 80%**
- ⚠️ Bug: Calls function TWICE (once discarded, once returned)
- Should only call `return func(*args, **kwargs)` once
- Concept understood, noted needs practice

**Task 5: PROJECT Trade Stats - 100%**
- Part A: ✅ Total PnL with initializer
- Part B: ✅ Win count
- Part C: ✅ Best trade
- **Key insight noted:** Initializer crucial when reducing dicts to numbers

**Task 6: PCAP Multiple Choice - 75%**
- Q1: ✅ B (reduce definition)
- Q2: ✅ C (finds max = 5)
- Q3: ✅ B (12 + 10 = 22)
- Q4: ❌ Answered D, correct is **B** (decorators replace function)

**Task 7: log_call decorator - 80%**
- ✅ Works and logs function calls
- ⚠️ Output format differs from expected (uses set unpacking)
- Concept understood

**Task 8: Combining map/filter/reduce - 100%**
- ✅ All steps correct
- ✅ **Caught mentor's calculation error!**
- Correct: 4 winners, $1050 (not 3 winners, $950)

### Final Score: 89% (B+)

### Key Corrections

**Task 3 Q2 - Decorator shorthand:**
```python
@my_decorator
def foo():
    pass
# Equivalent to:
foo = my_decorator(foo)  # NOT my_decorator.foo()
```

**Task 4 - Double function call bug:**
```python
# Bug: calls function twice
func(*args, **kwargs)           # Result discarded
return func(*args, **kwargs)    # Called again

# Fix: only call once
return func(*args, **kwargs)
```

**Task 6 Q4 - Decorators CAN access arguments:**
That's how `log_call` decorator works - via `*args, **kwargs`.

**Task 8 - Mentor error acknowledged:**
GOOGL SELL: (2800-2750)*5 = $250 (winner). Correct totals: 4 winners, $1050.

### Strengths
- ✅ reduce() mechanics understood quickly
- ✅ Good insight about initializer necessity
- ✅ Caught mentor's calculation error
- ✅ Good self-awareness about needing practice

### Areas for Improvement
- Decorator syntax: `decorator(func)` not `decorator.func()`
- Don't call wrapped function twice in decorator wrapper
- Decorators CAN access arguments via *args/**kwargs

### Project Milestones
- ✅ reduce() for trade statistics
- ✅ Decorator concept demonstrated
- ✅ Combined map/filter/reduce pipeline

---

## Week 4, Day 4 - 2026-01-29

**Topic:** Week 4 Review & PCAP Drills (Pre-Exam)

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 5/10
- **Time Spent:** 80 minutes

### Student Reflection
- Concepts like map/filter don't seem friendly compared to list comprehensions
- Worried about forgetting them without regular use
- Asked if they're commonly used in industry

### Mentor Assessment

**Task 1: Quick Fire Review - 80%**
- Q1: ❌ Answered D, correct is **C** (lambda returns a function, not True/False)
- Q2-Q9: ✅ All correct
- Q10: ⚠️ Avoided the question (used list comprehension instead of fixing lambda)

**Task 2: Output Predictions - 100%**
- A: ✅ 15, 10
- B: ✅ 1, 4
- C: ✅ 16, 8
- D: ✅ PCAP
- E: ✅ Hello, World
- F: ✅ 0 2 4

**Task 3: Debug Decorator - 90%**
- ✅ Fixed correctly with *args
- ⚠️ Bug description imprecise (both bugs are same issue)

**Task 4: Closure Stats Tracker - 80%**
- ✅ Works using defaultdict
- ❌ Bug: `elif` should be `if` (first value doesn't set max)
- Output shows max=0 when first value is 10

**Task 5: PCAP Multiple Choice - 100%**
- All 8 questions correct
- **Great question about filter(None, ...)** - explained

**Task 6: Functional Trade Processor - 100%**
- ✅ All parts working correctly
- ✅ Good use of reduce for statistics
- Modified trades in-place (valid approach)

**Task 7: functools.wraps - 100%**
- ✅ Understood wrapper loses metadata
- ✅ Correct answers for with/without @wraps

**Task 8: Integration Concepts - 100%**
- ✅ Good reasoning for list comprehensions preference
- ✅ Pragmatic view on closures vs classes
- ✅ Understood decorator advantages

### Final Score: 89% (B+)

### Key Corrections

**Task 1 Q1 - Lambda returns a FUNCTION:**
```python
f = lambda x: x > 5  # f is a function object
print(type(f))       # <class 'function'>
print(f(10))         # True - NOW it returns True/False
```

**Task 1 Q10 - Late binding fix with lambda:**
```python
functions = [lambda i=i: i for i in range(3)]  # i=i captures value
```

**Task 4 - elif bug:**
```python
if number < tracker['min']:
    tracker['min'] = number
if number > tracker['max']:  # Separate if, not elif!
    tracker['max'] = number
```

**filter(None, ...) explained:**
`None` as function means "use truthiness of each item", NOT "find None objects".

### Student Question: map/filter in industry
- List comprehensions ARE preferred (Guido agrees)
- map/filter useful when: named functions exist, FP codebases, reading libraries
- **For PCAP:** Must know them
- **For career:** List comprehensions 90% of the time

### Strengths
- ✅ Excellent output predictions
- ✅ Perfect PCAP multiple choice
- ✅ Complete trade processor implementation
- ✅ Good conceptual understanding

### Areas for Improvement
- Lambda returns a function, not the result
- Late binding fix: `lambda i=i: i` not "use list comprehension"
- Watch for elif vs if when both conditions can be true

### Week 4 Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 98% | Lambda, map(), filter() |
| 2 | 90% | Closures & Factory Functions |
| 3 | 89% | reduce(), Decorators |
| 4 | 89% | Week Review & PCAP Drills |

**Week 4 Average: 91.5% (A-)**

### Weekend Tasks
- PCAP Mock Exam A (30 questions)
- PCAP Mock Exam B (30 questions)
- Target: 70%+ (21/30) on each

---

## Week 4, Day 5 - 2026-01-30 (Friday)

**Topic:** Final Functional Programming Review & Exam Prep

### Student Self-Assessment
- **Tasks Completed:** 8/8
- **Difficulty:** 5-7/10
- **Time Spent:** 90 minutes

### Student Reflection
- map/filter functions still feel unnatural compared to list comprehensions
- Would use list comprehensions 9/10 times if given choice
- Wants more practice on functional patterns
- Honest self-ratings showing areas of uncertainty

### Mentor Assessment

**Task 1: Lambda Expression Mastery - 100%**
- Q1: ✅ 7 (1 + 2*3)
- Q2: ✅ 12, 12, 12 (late binding trap)
- Q3: ✅ 10, 11, 12 (late binding fix with i=i)
- Q4: ✅ B (lambda can't have return/assignment/multiple statements)
- Q5: ✅ 10 (nested lambda IIFE)
- Q6: ✅ 10 (*args with sum)
- **Perfect score on lambda fundamentals!**

**Task 2: Closure Deep Dive - 100%**
- Q1: ✅ 24 (4² + 2³ = 16 + 8)
- Q2: ✅ 1, 2, 2 (inc twice, get returns current)
- Q3: ✅ 20 (i=2 captured, 10*2)
- Q4: ✅ 15, 105, 20 (separate closures maintain state)
- **Perfect closure tracing!**

**Task 3: map/filter/reduce Pipeline - 90%**
- ✅ Part A: Excellent use of spread operator `{**t, 'net_amount': ...}`
- ✅ Part B: filter() correct
- ✅ Part C: reduce() with initializer correct
- ⚠️ Minor: `new_trades` loop is redundant (could use `result` directly)
- Valid comment about list comprehension being simpler approach

**Task 4: Decorator with Arguments - 100%**
- ✅ Perfect three-level implementation: repeat(times) → decorator(func) → wrapper(*args)
- ✅ Returns last result correctly
- Student noted difficulty - wants more practice (valid)

**Task 5: PCAP Multiple Choice - 75%**
- Q1: ✅ B (map returns map object)
- Q2: ✅ A (10-2-3 = 5)
- Q3: ❌ **Answered D, correct is C (20)**
- Q4: ✅ A (global x = 10)
- Q5: ❌ **Answered A, correct is B** (`x % 2` returns 1 for odd = truthy)
- Q6: ✅ C (closure definition)
- Q7: ✅ C (15)
- Q8: ✅ B (['A', 'B', 'C'])

**Task 6: PROJECT Signal Generator - 100%**
- ✅ Closure `make_level_detector` implemented correctly
- ✅ price_pairs using map - correct approach
- ✅ Signal logic correct (BUY on cross up, SELL on cross down)
- ✅ filter() for action signals
- ✅ reduce() for counting
- **Student CORRECTLY challenged mentor's expected output!**
  - My expected signals were wrong
  - Price going from 108→106 stays ABOVE 105, doesn't cross it = HOLD
  - Student's output ['HOLD', 'BUY', 'SELL', 'BUY', ...] is CORRECT
  - Mentor error acknowledged

**Task 7: Decorator Stacking Order - 0%**
- Q1: ❌ **Answered B, correct is A** (`<b><i>Hello, World</i></b>`)
- Q2: ❌ **Answered A, correct is B** (italic applied first, then bold)
- Q3: ❌ Should be `<i><b>Hello, World</b></i>`

**Task 8: Self-Assessment - Complete**
- Honest self-ratings across all Week 4 topics
- Correctly identified weak spots (decorators, late binding fix, factory functions with nesting)
- Valid feedback about wanting more practice

### Final Score: 85% (B+)

### Critical Corrections

**Task 5 Q3 - Stacked Decorators:**
```python
@deco
@deco
def five():
    return 5
```
This means: `five = deco(deco(five))`
- Inner deco: wrapper returns `five() * 2` = 5 * 2 = 10
- Outer deco: wrapper returns `inner_wrapper() * 2` = 10 * 2 = 20
- **Answer: C (20)**

**Task 5 Q5 - filter() with modulo:**
```python
filter(lambda x: x % 2, nums)  # [1, 2, 3, 4, 5]
```
- 1 % 2 = 1 (truthy) → kept
- 2 % 2 = 0 (falsy) → filtered out
- 3 % 2 = 1 (truthy) → kept
- **Result: [1, 3, 5]** (odd numbers)

**Task 7 - Decorator Stacking Order:**
```python
@bold
@italic
def greet(name):
    return f"Hello, {name}"
```
- **Application order (bottom-up):** italic first, then bold
- **Execution order (top-down):** bold wrapper runs first, calls italic wrapper
- `greet = bold(italic(greet))`
- **Output:** `<b><i>Hello, World</i></b>`

If reversed to `@italic @bold`:
- `greet = italic(bold(greet))`
- **Output:** `<i><b>Hello, World</b></i>`

**Key rule:** Decorators wrap from bottom-up, execute from top-down. The innermost function result gets wrapped by outer decorators.

### Strengths
- ✅ Perfect lambda fundamentals (Task 1: 100%)
- ✅ Perfect closure tracing (Task 2: 100%)
- ✅ Solid decorator implementation with arguments
- ✅ **Caught mentor error on signal generator** - excellent critical thinking
- ✅ Honest self-assessment showing learning maturity

### Areas for Improvement
- ⚠️ Decorator stacking order (0% - needs practice)
- ⚠️ Stacked decorator output prediction
- ⚠️ filter() with truthy/falsy (not `== 0` but truthiness)

### Student Feedback Addressed

**"map/filter feel unnatural"**
Your instinct is correct. List comprehensions ARE more Pythonic for most cases. Guido himself prefers them. For PCAP, you must know map/filter. For industry, list comprehensions 90% of the time. Your preference is valid.

**"Decorators need more practice"**
Agreed. Task 7 showed this gap. For weekend study:
1. Practice: `@a @b def f()` = `f = a(b(f))`
2. Execution: outer wrapper runs first, calls inner
3. Draw the wrapping visually if needed

### Week 4 Final Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 98% | Lambda, map(), filter() |
| 2 | 90% | Closures & Factory Functions |
| 3 | 89% | reduce(), Decorators |
| 4 | 89% | Week Review & PCAP Drills |
| 5 | 85% | Final Review & Exam Prep |

**Week 4 Average: 90.2% (A-)**

### Weekend Tasks
- Week4_Exam_A.md (30 questions)
- Week4_Exam_B.md (30 questions)
- Target: 70%+ (21/30) on each
- Focus areas: decorator stacking, filter() truthiness

---

## Week 5, Day 1 - 2026-02-02

**Topic:** datetime Module & File I/O Basics

### Mentor Assessment

**Score: 89% (B+)**

**Task Breakdown:**

| Task | Score | Notes |
|------|-------|-------|
| 1. datetime basics | 100% | All 6 questions correct |
| 2. File reading methods | 60% | Used `/n` instead of `\n`, missed list format for readlines() |
| 3. File writing practice | 100% | Correct use of 'w', 'a' modes and context managers |
| 4. File mode traps | 100% | Perfect understanding of 'w' vs 'a' and FileNotFoundError |
| 5. TradeLogger class | 85% | Functional but format deviations, includes `\n` in output |
| 6. PCAP multiple choice | 100% | All 8 correct, including write() return value |
| 7. Context managers | 70% | Incomplete exception explanation, missing variable assignment |
| 8. datetime edge cases | 100% | Leap year and default values correct |

### Detailed Corrections

**Task 2 - File Reading Methods:**

1. **Notation:** Use `\n` (backslash), not `/n` (forward slash)
2. **readline():** Returns `'line1\n'` - includes the newline character
3. **readlines():** Returns a **LIST**: `['line1\n', 'line2\n', 'line3']`
4. **Memory efficiency:** Iterating over file object is BEST:
   ```python
   for line in f:  # Reads one line at a time
       process(line)
   ```

**Task 5 - TradeLogger:**

1. **Timestamp format:** Use `.strftime()` to avoid microseconds:
   ```python
   datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   ```
2. **get_trades():** Strip newlines:
   ```python
   trade_list.append(line.strip())
   ```
3. **Format string:** Used `||` instead of spec's `|` (minor)

**Task 6 Q2 Explanation:**
`f.write('Hello')` returns `5` because `write()` returns the number of characters written. This is useful for verifying writes or tracking file position.

**Task 7 - Context Managers:**

1. **Q2 incomplete:** File IS closed despite exception, THEN exception propagates. `'start'` is written, `'end'` is not.
2. **Q3 missing assignment:**
   ```python
   with open('data.txt', 'r') as f:
       content = f.read()  # You wrote just f.read()
   ```

### Strengths
- ✅ Excellent datetime understanding (strftime/strptime distinction)
- ✅ Perfect file mode knowledge (PCAP traps nailed)
- ✅ Strong PCAP multiple choice (100%)
- ✅ TradeLogger is fully functional
- ✅ Edge cases handled well (leap year, defaults)

### Areas for Improvement
- ⚠️ File method return types (especially readlines → list)
- ⚠️ Context manager exception behavior (file closes THEN exception raises)
- ⚠️ Including `\n` in strings from file reads

### Student Feedback Addressed

**"More practice-based tasks"**
Day 2 will include:
- Hands-on datetime manipulation exercises
- File I/O coding challenges (not just theory)
- Build on TradeLogger with new features
- Integration with past concepts (closures, properties)

**"datetime needs reinforcement"**
Agreed. Day 2 will focus on practical datetime scenarios used in trading systems.

---

## Week 5, Day 2 - 2026-02-03

**Topic:** datetime Practice & File I/O Applications

### Mentor Assessment

**Score: 78% (C+)**

**Task Breakdown:**

| Task | Score | Notes |
|------|-------|-------|
| 1. datetime coding | 100% | All 3 functions perfect |
| 2. File I/O coding | 70% | Missing read_non_empty_lines, microseconds in log |
| 3. Closure + datetime | 85% | Works, should use .total_seconds() |
| 4. TradeLogger | 75% | Type confusion: dt already datetime, can't strptime |
| 5. PCAP MC | 100% | All 6 correct |
| 6. ConfigManager | 60% | _load_config doesn't parse, setter incomplete |
| 7. Decorator | 50% | 'w' vs 'a', double func call, format mismatch |
| 8. timedelta | 85% | December edge case, missing () on weekday |

### Detailed Corrections

**Task 2 - read_non_empty_lines (missing):**
```python
def read_non_empty_lines(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]
```

**Task 4 - get_trades_since bug:**
```python
# WRONG: dt is already datetime!
converted_dt = datetime.strptime(dt, '%Y-%m-%d')

# CORRECT: Compare directly
if datetime_date > dt:
```

**Task 6 - _load_config should parse:**
```python
def _load_config(self):
    try:
        with open(self.filepath, 'r') as r:
            for line in r:
                key, value = line.strip().split('=')
                if key == 'debug_mode':
                    self._debug_mode = value == 'True'
                elif key == 'max_trades':
                    self._max_trades = int(value)
    except FileNotFoundError:
        pass
```

**Task 7 - Decorator (3 bugs):**
1. Use `'a'` mode (append), not `'w'` (overwrite)
2. Call `func(*args, **kwargs)` ONCE, store in `result`
3. Format: `f'{timestamp} | {func.__name__}{args} -> {result}'`

```python
def log_to_file(filepath: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # ONE call
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filepath, 'a') as f:  # APPEND
                f.write(f'{timestamp} | {func.__name__}{args} -> {result}\n')
            return result
        return wrapper
    return decorator
```

**Task 8 Q1 - December edge case:**
```python
if month == 12:
    last_day = date(year, 12, 31)
else:
    last_day = date(year, month + 1, 1) - timedelta(1)
```

### Strengths
- ✅ datetime fundamentals now solid (100% on Task 1)
- ✅ PCAP theory maintained at 100%
- ✅ Closure concepts well understood
- ✅ Good debugging instincts (identified decorator issues)
- ✅ Code is readable and follows PEP 8

### Areas for Improvement
- ⚠️ File mode: 'w' overwrites, 'a' appends (critical for logging!)
- ⚠️ Type hints are contracts: if param is `datetime`, don't parse it
- ⚠️ DRY: don't duplicate _save_config logic in setters
- ⚠️ Edge cases: December, empty files, etc.

### Student Feedback

**"Decorator was overwhelming"**
Decorators with arguments have 3 layers:
1. **Outer function** (`log_to_file`) - receives decorator arguments
2. **Middle function** (`decorator`) - receives the function to wrap
3. **Inner function** (`wrapper`) - replaces the original function

Key patterns to memorize:
- Store result ONCE: `result = func(*args, **kwargs)`
- Use append mode for logging: `'a'`
- `@wraps(func)` preserves function metadata

**"Practice-heavy day"**
This was intentional per your feedback. The 78% reflects realistic complexity—these are the kinds of bugs you'll encounter in real projects. Day 3 will reinforce the decorator pattern.

---

## Week 5, Day 3 - 2026-02-04

**Topic:** Decorator Mastery & File Modes Deep Dive

### Mentor Assessment

**Score: 91% (A-)**

**Task Breakdown:**

| Task | Score | Notes |
|------|-------|-------|
| 1. File mode drill | 100% | All 4 correct - 'w' vs 'a' mastered |
| 2. Decorator bug fixes | 100% | Both parts with clear explanations |
| 3. log_to_file | 95% | Works, return inside with block (minor) |
| 4. Type hint contracts | 70% | Q3 correct, Q1/Q2 task poorly designed |
| 5. BacktestEngine | 90% | Missing `return position` in open_position |
| 6. PCAP MC | 83% | Q4 wrong (A not C) |
| 7. read_non_empty_lines | 90% | Works, minor cleanup needed |
| 8. rate_limiter | 100% | Perfect nonlocal usage |

### Detailed Corrections

**Task 4 - Type Hint Contracts:**
The task was poorly designed. The student correctly noted the code works when passing a string. The intended lesson was about type hint consistency (hint says `datetime` but code expects `str`), but this wasn't clearly communicated.

**Task 5 - BacktestEngine:**
Missing return statement:
```python
def open_position(...) -> Position:
    position = Position(...)
    self.position_manager.add_position(position)
    return position  # Add this!
```

**Task 6 Q4 - Decorator with Arguments:**
Option A is correct, not C.
- A: `deco(arg)` returns a function that receives `func` → decorator WITH arguments
- C: `deco` receives `func`, returns `wrapper(arg)` → regular decorator

The 3-layer pattern for decorator with arguments:
```python
def decorator_with_args(arg):      # Layer 1: receives decorator args
    def decorator(func):            # Layer 2: receives function
        def wrapper(*args):         # Layer 3: replaces function
            return func(*args)
        return wrapper
    return decorator
```

**Task 7 - Cleanup suggestions:**
```python
# Instead of:
if content is not None and content != '':

# Use:
if content:  # Truthy check
```

### Strengths
- ✅ File mode distinction now solid
- ✅ Decorator pattern: single function call, append mode
- ✅ nonlocal keyword used correctly
- ✅ BacktestEngine properly integrates existing classes
- ✅ Good code organization and readability

### Areas for Improvement
- ⚠️ Remember to return values when method signature indicates it
- ⚠️ Decorator with arguments pattern: 3 layers, outer receives args
- ⚠️ Pythonic truthy checks: `if content:` instead of `if content != ''`

### Student Feedback Addressed

**"Decorators need more practice"**
Agreed. The rate_limiter is a great real-world pattern. Other useful patterns to practice:
- `@cache` / `@memoize` - store results
- `@retry` - retry on failure
- `@timer` - measure execution time

**"2 hours was long"**
Day 4 will be lighter. Friday is exam prep day.

---

## Week 5, Day 4 - 2026-02-05

**Topic:** Review & Consolidation (Lighter Day)

### Mentor Assessment

**Score: 93% (A)**

**Task Breakdown:**

| Task | Score | Notes |
|------|-------|-------|
| 1. Decorator pattern | 100% | Correctly identified A, good explanation |
| 2. @timer decorator | 100% | Working implementation |
| 3. PCAP Quick Fire | 87.5% | Q3 wrong - strftime returns string |
| 4. BacktestEngine fix | 100% | Return statement added |
| 5. Test BacktestEngine | 100% | Correct PnL: $30,900 |
| 6. Mutable default | 90% | Correct fix, output format slightly off |

### Corrections

**Task 3 Q3:**
`strftime` ALWAYS returns a string, regardless of format:
```python
datetime.now().strftime("%Y")  # "2026" (string)
type(...)  # <class 'str'>
```

**Task 6 Q2:**
Output format is the full list each time:
```
['a']
['a', 'b']
```

### Week 5 Progress

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 89% | datetime & File I/O Basics |
| 2 | 78% | datetime Practice & Applications |
| 3 | 91% | Decorator Mastery & File Modes |
| 4 | 93% | Review & Consolidation |

**Running Average: 87.75%**

### Ready for Friday
- BacktestEngine working and tested
- Decorator patterns solid
- File modes mastered
- datetime fundamentals good

Tomorrow: Final review + Weekend Mock Exams

---

## Week 5, Day 5 - 2026-02-06

**Topic:** Week Review & Exam Prep

### Mentor Assessment

**Score: 88% (B+)**

**Task Breakdown:**

| Task | Score | Notes |
|------|-------|-------|
| 1. PCAP warm-up | 100% | Shallow copy + nonlocal perfect |
| 2. @retry decorator | 100%* | Code correct, needed AI assistance |
| 3. filter_log_by_date | 85% | Boundary (`>` vs `>=`), missing strip() |
| 4. PCAP simulation | 70% | Q5, Q6, Q7 wrong (7/10) |
| 5. BacktestEngine __str__ | 100% | Clean implementation |
| 7. Decorator stacking | 75% | Correct order, wrong content/tags |
| 8. Exception + File I/O | 85% | `{text}` = set, should be `text` |

### Key Corrections

**Q5 (@wraps):** `@wraps` preserves `__name__`, `__doc__`, `__module__`, `__qualname__`, `__annotations__`. It does NOT copy `__code__`.

**Q6 (Exception hierarchy):**
```
IOError (alias for OSError)
  └── FileNotFoundError
```
`except IOError` catches FileNotFoundError because parent catches child. Put specific exceptions FIRST.

**Q7 (strftime):** `%y` = 2-digit year (26), `%Y` = 4-digit year (2026).

**Q10:** Mentor error — options B and C were identical.

### Week 5 Final Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 89% | datetime & File I/O Basics |
| 2 | 78% | datetime Practice & Applications |
| 3 | 91% | Decorator Mastery & File Modes |
| 4 | 93% | Review & Consolidation |
| 5 | 88% | Week Review & Exam Prep |

**Week 5 Average: 87.8% (B+)**

### Strengths Observed
- File modes fully mastered ('w'/'a'/'r'/'x')
- datetime fundamentals solid (strftime/strptime/timedelta)
- Closures and nonlocal understood
- Properties comfortable (5/5)
- BacktestEngine integrated with existing codebase
- Honest self-assessment and willingness to flag weak areas

### Recurring Gaps
- Decorators with complex logic (retry, rate_limiter) still challenging
- Exception hierarchy order (parent catches child)
- strftime format codes: `%y` vs `%Y`, return type always string
- Small Python details: `{x}` = set, boundary conditions (inclusive)

### Project Progress
- BacktestEngine created and tested
- __str__ method added
- Position → Trade lifecycle working
- PnL calculations verified ($30,900 test case)

### Readiness for Next Week
- Strong foundation for Week 6 (Generators & Iterators)
- Decorators need continued scaffolded practice (1 task/day)
- Exception hierarchy needs drilling
- Student self-assessment aligns with mentor observations

### Student Self-Assessment (Comfort 1-5)
- Decorators (no args): 4
- Decorators (with args): 3 (complex: 2)
- File modes: 5
- File read methods: 4
- datetime: 4
- timedelta: 5
- Closures: 5
- Properties: 5

### Weekend Tasks
- Week5_Exam_A.md (30 questions)
- Week5_Exam_B.md (30 questions)
- Focus: decorators, exception hierarchy, strftime codes

---

## Week 6, Day 1 - 2026-02-09

**Topic:** The Iterator Protocol & Advanced Generators
**Time Spent:** 60 minutes
**Difficulty:** 6-7/10

### Mentor Assessment

**Score: 81% (revised from 76% after student feedback)**

| Task | Score | Notes |
|------|-------|-------|
| 1. PCAP Warm-up | 100% | Iterator/generator identity understood |
| 2. Decorator Trace | 70% | Flow understood, output errors: param_name vs value, :.2f format |
| 3. FibonacciIterator | 55% | Protocol correct, hardcoded list (lesson gap acknowledged), off-by-one |
| 4. __new__ vs __init__ | 90% | Singleton gotcha nailed |
| 5. yield from + Pipeline | 75% | Pipeline correct, flatten followed lesson pattern (task wording unclear) |
| 6. MRO Trace | 100% | Both perfect — recurring gap officially CLOSED |
| 7. Position IDs (Project) | 75% | UUID correct, critical bug in removal line |
| 8. PCAP Simulation | 80% | 4/5, __init__ receives original args not __new__ transform |

**Score revision:** Student correctly noted Task 2 trace graded too harshly (PCAP doesn't test step-by-step decomposition), Task 3 lesson didn't teach two-variable Fibonacci state pattern, Task 5 flatten approach matched lesson's chain example.

### Key Issues
- Hardcoded Fibonacci list instead of computing dynamically with state variables
- PositionManager.close_triggered_positions removal line doesn't filter by ticker (removes all triggered positions regardless)
- Decorator trace: confused param_name (closure variable "price") with actual argument (-50.0)
- f-string :.2f = 2 decimal places (recurring issue since Week 5)
- __init__ receives original arguments, __new__ transforms the object itself

### Strengths
- MRO with super() — 100% on both questions, gap closed after 3 weeks
- __new__ / Singleton pattern understood (was untaught before, now grasped)
- Iterator vs generator identity distinction clear
- Project: uuid integration clean, ticker-aware architecture correct (minus the bug)
- Good forward thinking: noted Trade needs position_id propagation

### Project Progress
- Position now has unique position_id (uuid4)
- PositionManager and BacktestEngine are ticker-aware
- Bug to fix: removal line in close_triggered_positions needs ticker filter
- Next: Propagate position_id to Trade class

---

## Week 6, Day 2 - 2026-02-10

**Topic:** Iterator Mastery, Bug Fixes & Trade ID Propagation
**Score:** 95% (A) | **Time:** 60 minutes | **Difficulty:** 5-6/10

### Task Breakdown

| Task | Score | Details |
|------|-------|---------|
| 1: PCAP warm-up | 92% | Both correct; Q1 reset mechanism understanding shaky |
| 2: Decorator fill-in-blanks | 100% | All 5 blanks correct, output verified |
| 3: FibonacciIterator rewrite | 100% | Perfect dynamic state implementation |
| 4: __new__/__init__ args | 100% | Both predictions correct — Day 1 gap closed |
| 5: PositionManager bug fix | 90% | Correct ID-based fix; self-caught first attempt bug |
| 6: Trade position_id | 100% | Clean implementation, good design choices |
| 7: CountdownIterator | 100% | All tests pass |
| 8: PCAP simulation | 80% | 4/5 — Q2 iterable vs iterator confusion |

### Gaps Closed from Day 1
- Fibonacci hardcoding → proper `a, b = b, a+b` state pattern
- `__init__` receives original args, not __new__-transformed values
- PositionManager ticker bug fixed using position_id filtering

### Remaining Gaps
- **Iterable vs Iterator pattern:** When `__iter__` uses `yield`, each `iter()` call creates a new independent generator (iterable pattern). When `__iter__` returns `self`, same object (iterator pattern).
- **`__iter__` reset mechanism:** Understands output but not the WHY behind resettable iterators
- `__dict__` attribute not yet taught — student correctly flagged this

### Strengths
- Decorator understanding now solid (Day 1 trace → Day 2 blanks → all correct)
- Strong debugging instinct (self-caught PositionManager bug before confirmation)
- Good engineering judgment (required vs optional position_id, str conversion at source)
- Day-over-day improvement: 81% → 95%

### Project Progress
- PositionManager ticker bug FIXED (ID-based removal)
- Trade class now carries position_id (read-only property)
- Position stores str(uuid4) directly
- BacktestEngine passes position_id in Trade creation
- __repr__ and __str__ updated across Position and Trade

---

## Week 6, Day 3 - 2026-02-11

**Topic:** Iterable vs Iterator, Decorator Writing & Price Stream Generator
**Score:** 93% (A) | **Time:** 80 minutes | **Difficulty:** 6/10

### Task Breakdown

| Task | Score | Details |
|------|-------|---------|
| 1: Iterable vs Iterator warm-up | 95% | Both correct; understanding improved |
| 2: Decorator from scratch | 100% | Perfect — scaffolding Day 3 complete |
| 3: NumberRange iterable | 100% | Clean yield-in-__iter__ pattern |
| 4: Generator edge cases | 95% | All 3 correct (return value, yield from, partial) |
| 5: PriceTick + create_price_stream | 95% | Working generator with ticker filter |
| 6: Tick-by-tick backtest | 90% | First generator-powered backtest; minor style |
| 7: Generator expressions | 88% | 2/3 T/F — "always faster" misconception |
| 8: PCAP simulation | 80% | 4/5 — Q1 iterable pattern in exam context |

### Remaining Gaps
- **Iterable recognition in exam context:** Knows the rule when prompted (Tasks 1-3 correct), reverts to one-shot thinking in multiple choice (Task 8 Q1). Recognition issue, not knowledge issue.
- **"Generators always faster" misconception:** Less memory ≠ faster. List comprehensions can outperform generators on small data due to cache friendliness and no suspend/resume overhead.

### Strengths
- Decorator scaffolding COMPLETE: trace → blanks → write from scratch in 3 days
- Generator lazy evaluation understood (Q2 with mutated source list — tricky, nailed it)
- First generator-powered backtest working end-to-end
- Consistent A-range: 81% → 95% → 93%

### Project Progress
- PriceTick namedtuple defined
- create_price_stream() generator working (loads CSV via DataLoader, yields PriceTick per row, optional ticker filter)
- Tick-by-tick backtest demonstrated (position opened → stream consumed → TP hit → trade closed)
- Code in practice.py — not yet integrated into project package

---

## Week 6, Day 4 - 2026-02-12

**Topic:** Advanced Generators, Parameterized Decorators & Context Recognition
**Score:** 85% (B+) | **Time:** N/A (completed with external AI) | **Difficulty:** 6-7/10

### Task Breakdown

| Task | Score | Details |
|------|-------|---------|
| 1: Iterator vs Iterable Recognition Drill | 95% | All 3 correct; Q3 understanding gap on WHY yield-in-__iter__ isn't exhausted |
| 2: Parameterized @repeat(n) decorator | 100% | Perfect — decorator factory with three nested functions |
| 3: Generator Performance (when lists win) | 95% | Correct analysis of both scenarios; bug identified |
| 4: Generator Return/send()/yield from | 60% | Q1 correct (B); Q2-Q3 unanswered (send() not taught) |
| 5: Filtered Price Stream | 0% | Skipped |
| 6: SMA Indicator | 85% | Working implementation; yields SMA=0.00 before window fills; uses list.pop(0) instead of deque |
| 7: Tricky Iterator Questions | 55% | Q1 WRONG (C not A — missed reset + increment-before-return), Q2 correct, Q3 WRONG (C not A — confused independent generators) |
| 8: PCAP Simulation (5 Qs) | 40% | Q1 WRONG (@wraps stacking), Q2 WRONG (iter identity), Q3 WRONG (in on generators), Q4 WRONG (closure __name__), Q5 correct |

### Critical Gaps Exposed (Day 4 Tasks 7-8)
1. **Resettable iterators:** Didn't see that `__iter__` resets `self.current = 0` AND that increment-before-return yields 1,2,3 not 0,1,2
2. **Independent generators:** `g1 = gen(); g2 = gen()` creates two separate objects — answered as if they shared state
3. **@wraps on stacked decorators:** Both layers print the original name, not "wrapper" then "foo"
4. **iter(obj) is obj:** When `__iter__` returns `iter(self.items)`, the result is NOT the object itself → False
5. **`in` on generators:** Consumes elements sequentially; `0 in gen` is True (not False)
6. **Closure `__name__`:** Returns inner function's def name ("multiplier"), not the outer function name

### Strengths
- Parameterized decorator mastered (Day 4 of decorator scaffolding complete)
- Generator performance trade-offs understood
- Iterator vs Iterable recognition improving in isolation (Task 1 all correct)

### Project Progress
- SMA indicator working (needs deque refactor and window-fill guard)
- Filtered price stream task skipped

---

## Week 6 — End of Week Summary

### Score Progression
| Day | Score | Topic |
|-----|-------|-------|
| Day 1 | 81% (B) | Iterator Protocol & Advanced Generators |
| Day 2 | 95% (A) | Iterator Mastery & Trade ID Propagation |
| Day 3 | 93% (A) | Iterable vs Iterator & Price Stream Generator |
| Day 4 | 85% (B+) | Advanced Generators & Parameterized Decorators |
| Day 5 | 95% (A) | Exam Gap Closure |
| **Average** | **89.8%** | |

### Strengths This Week
- **Decorator scaffolding complete:** trace → blanks → from scratch → parameterized in 4 days
- **Project momentum:** Position ID chain, PositionManager bug fix, PriceTick generator, SMA indicator — all working
- **Self-correction instinct:** Caught PositionManager filter bug before confirmation (Day 2)
- **Generator fundamentals solid:** yield, yield from, exhaustion, lazy evaluation all understood
- **Strong Day 2-3 performance:** 95% and 93% show deep concept mastery in guided practice

### Recurring Weaknesses
- **PCAP multiple choice under pressure:** Concepts understood in isolation but misapplied in timed exam context (Day 4 Tasks 7-8 were 55% and 40%)
- **Iterator identity patterns:** `iter(obj) is obj`, resettable iterators, independent generator instances — all tripped up when presented as exam questions
- **`in` operator on generators:** Didn't recognize sequential consumption behavior
- **`__name__` confusion:** Conflates variable name, outer function name, and inner function name
- **@wraps stacking:** Doesn't yet see that @wraps propagates __name__ through multiple decorator layers

### Project Progress Assessment
- Phase 2 (The Engine) nearly complete
- All Week 6 roadmap items checked off
- SMA indicator needs refactoring (deque, window guard) — assigned as Day 5 Task 6
- Generator pipeline pattern demonstrated but not yet integrated into project package

### Readiness for Week 7
- **PCAP Theory:** 7/10 — concepts are there, exam application needs drilling
- **Project:** 8/10 — strong foundation, ready for logging/polish phase
- **Recommendation:** Day 5 focuses entirely on the 6 exam gaps from Day 4. Weekend exams will test retention.

---

## Week 6, Day 5 - 2026-02-13

**Topic:** Exam Gap Closure — Iterator Identity, `in` on Generators, @wraps Stacking, Closure Names
**Score:** 95% (A) | **Time:** 40 minutes | **Difficulty:** 7/10

### Task Breakdown

| Task | Score | Details |
|------|-------|---------|
| 1: `in` operator on generators | 100% | All 3 correct — gap closed |
| 2: iter(obj) is obj identity | 100% | All 6 sub-answers correct — Day 4 Q8 Q2 gap closed |
| 3: Resettable iterators | 100% | [1,2,3] twice + [1,2,3]/[] both correct — Day 4 Q7 Q1 gap closed |
| 4: `__name__` and @wraps stacking | 100% | B, greeter, add, "Called foo twice" — Day 4 Q8 Q1/Q4 gaps closed |
| 5: Independent generators | 78% | Q1/Q3 correct; Q2: `iter(generator)` twice is SAME object (True, not False) |
| 6: PCAP simulation (6 Qs timed) | 100% | A A B B A A — all correct. Massive improvement from Day 4's 40-55% |
| 7: Concept map (10 blanks) | 90% | 9/10 — Item 2: swapped __iter__ and __next__ for iterable definition |

### Corrections
1. **Task 5 Q2:** Wrote the rule correctly ("iter(generator) twice → same object") then answered False. `iter(g)` on a generator returns `g` itself → `x is y` is True; `next(y)` is 20 not 10.
2. **Task 7 Item 2:** Backwards — iterable has `__iter__` NOT `__next__`. (Said "iterable has next but not iter".)

### Strengths
- Day 4's 6 PCAP exam gaps: 5 out of 6 fully closed in one session
- Timed simulation (Task 6): 6/6 — complete reversal of Day 4 performance
- `in` on generators: immediately understood and applied correctly
- @wraps stacking and closure __name__: both now solid

### Week 6 Final Average
| Day | Score |
|-----|-------|
| Day 1 | 81% |
| Day 2 | 95% |
| Day 3 | 93% |
| Day 4 | 85% |
| Day 5 | 95% |
| **Average** | **89.8%** |

**Readiness for Week 7:** Strong. PCAP application under pressure has gone from 40% to 100% in one day. The remaining microscopic gaps (iter-on-generator identity, iterable vs iterator exact wording) are noted for weekend exam consolidation.

---


## Week 7, Day 1 — 2026-02-16

**Topic:** The `logging` Module — Fundamentals to Project Integration
**Score:** 62% on answered tasks (Tasks 6 & 7 fully excused) | **Time:** 60 minutes

---

### Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Level predictions | 2/3 | Swapped ERROR(40)/CRITICAL(50); missed default format includes `WARNING:root:` prefix |
| 2 — Theory | 2/3 | Correct on source identification; missed logger singleton (same name = same object) |
| 3 — Two-stage filtering | 1/3 | Mental model not yet formed — guessed rather than traced |
| 4 — setup_logger() | 8/10 | Correct structure; missing duplicate-handler guard (`if logger.handlers: return logger`) |
| 5 — logging vs warnings | 2.5/3 | Q1/Q2 correct; Q3 ambiguous answer |
| 6 — PROJECT | excused | Premature — project integration before mental model formed |
| 7 — PROJECT | excused | Same reason |
| 8 — PCAP simulation | 2/5 | Two-stage filtering (Q3), exception() misconception (Q4), singleton (Q5) |

**Raw score on answered tasks: ~62%**

---

### Key Corrections

- **ERROR=40, CRITICAL=50** — not swapped. Full table: DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50
- **Default output format** without basicConfig: `WARNING:root:message` — not bare text
- **Logger singleton** — `getLogger('same_name')` returns the same global object every time
- **Two-gate rule** — message must pass BOTH logger level AND handler level. Stricter gate always wins
- **`logging.exception()`** — does NOT raise. Logs at ERROR AND appends traceback. Use only inside except blocks

---

### Student Feedback & Action Taken

Tasks 6/7 correctly refused as premature. Student requested scaffolded approach with WHAT/WHY/HOW structure and testable examples. Lesson rewritten accordingly (PART 1–7 structure). Day 2 tasks follow the stepped approach: observe → predict → build → test.

---

### Gaps for Day 2

1. Two-stage filtering (Tasks 3 and 8 Q3)
2. Logger singleton/registry (Task 2 Q3 and Task 8 Q5)
3. `logging.exception()` vs `logging.error()` (Task 8 Q4)
4. Default output format with `WARNING:root:` prefix (Task 1 Q1)

---

## Week 7, Day 2 — 2026-02-17

**Topic:** `logging` — Observe, Predict, Build (Scaffolded)
**Score:** 88% (B+) | **Time:** 50 minutes | **Difficulty:** 5/10 (appropriate)

---

### Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Observe (4 snippets) | 3/3 | All outputs correct; explanations solid |
| 2 — Two gates | 2.5/3 | Output + fix correct; Q1 explanation slightly passive ("logger just receives") — both gates are active filters |
| 3 — Singleton | 3/3 | True/False/True correct; explanations on-point |
| 4 — Predict then verify | 3/3 | All three predictions correct; Q2/Q3 explanations show two-gate understanding |
| 5 — Build from scratch | 8/10 | Steps 1-3 correct; Step 4 had 3 bugs (logging.info vs logging.INFO, guard always-True, addHandler takes 1 arg) — all self-corrected after feedback |
| 6 — PCAP drill | 4/5 | Q1-Q3 Q5 correct (Day 1 gaps closed); Q4 still wrong: logging.exception() appends traceback, does NOT raise |

**Total: ~88%**

---

### Key Wins

- Two-gate filtering now understood and applied correctly under prediction pressure
- Logger singleton confirmed by running `a is b` — concept is now empirical, not abstract
- Built a full logger (StreamHandler + FileHandler + Formatter) from scratch without looking at lesson
- Three Day 1 gaps fully closed: default format, two-gate rule, singleton

### Remaining Gap

**`logging.exception()`** — wrong for second session. Answer is C (appends traceback), not A (raises). Use only inside `except` blocks. It logs at ERROR level AND adds the traceback below automatically.

### Student Feedback

"Way better and smoother experience than yesterday — 5/10 difficulty, appropriately scaffolded." Concepts of Logger vs Handler vs Formatter now understood functionally. Verified self-corrections on Task 5 bugs after assessment.

---

## Week 7, Day 3 — 2026-02-18

**Topic:** logging — Closing Gaps + Introspection Touch + Project Integration
**Score:** 90% (A-) [revised after valid disputes] | **Time:** 50 minutes | **Difficulty:** 5/10

---

### Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — logging.exception() | 2/4 | Q1 observed correctly; Q2 wrong (doesn't raise/stop); Q3 wrong (logs at ERROR not separate sphere); Q4 correct |
| 2 — PCAP simulation | 5/5 | All correct — two-gate, levels, basicConfig one-shot all solid |
| 3 — Introspection | 6.5/7 | All correct; print() wrappers accepted (valid verification); Q4 minor: default should be 0.0 not string |
| 4 — BacktestEngine logging | 9.5/10 | Structure correct; f-strings in message bodies accepted (not taught with object attrs); orphan formatter was task design fault |
| 5 — setup_logging() | 7/10 | Works; __main__ logger used instead of root — BacktestEngine messages won't propagate. Self-corrected after feedback. |
| 6 — PCAP warm-up | 2/3 | Q1/Q2 correct; Q3 wrong: __name__ = full dotted path, not just filename |

**Total: ~90% (A-)**

---

### Key Corrections

- **logging.exception()**: logs at ERROR (40), does NOT raise, does NOT stop. Appends traceback only. Must be locked in for exam.
- **Root logger**: `logging.getLogger()` (no args) = root. Configure root in setup_logging() so all child loggers inherit via propagation.
- **__name__ in modules**: full dotted import path — `algo_backtest.engine.backtest`, not `backtest`.
- **%s vs f-strings in log calls**: covered properly in Day 4 with practice.

### Disputes Upheld

- Task 3 prints: valid verification technique during learning
- Task 4 f-strings: not taught with object attributes — teaching point not a deduction
- Task 4 orphan formatter: task instruction was contradictory — student correctly flagged it

### Student Preference

Wants ~10-20% more coding. Day 4 adjusted with one extra coding task.

---

## Week 7, Day 4 — 2026-02-19

**Topic:** logging Gaps + PCAP Crunch (60/40 coding/theory)
**Score:** 95% (A) after disputes | **Time:** 70 minutes | **Difficulty:** 6/10

### Student Self-Assessment
- Fruitful and satisfying session
- Found "%s only" instruction misleading in decorator contexts where the pattern was not taught
- Needed extra support for logging inside decorator wrappers

### Mentor Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Quick-fire gaps | 2/4 | Q1 correct (TypeError); Q2 WRONG — reading outer vars works without nonlocal; Q3 correct; Q4 correct |
| 2 — Gap-closer warm-up | 5/5 | All predict-and-fix correct with %s style |
| 3 — safe_divide() | 9/10 | ValueError not caught at call site (inside function, not caller); f-strings accepted (pattern not taught) |
| 4 — Decorator + logging | 9/10 | Missing raise after logger.exception(); orphan formatter correctly flagged — task design fault |
| 5 — BacktestEngine logging | 9.5/10 | Correct structure; f-strings accepted after dispute |
| 6 — setup_logging() | 9/10 | Self-corrected root vs named logger after guidance |
| 7 — PCAP simulation | 7/8 | Q2 wrong (raise "string" is TypeError at runtime); Q5 wrong (reading outer vars needs no nonlocal) |

**Total: 95% (A) after disputes**

### Key Corrections
- **raise "string"**: TypeError at RUNTIME — strings are not valid exception types
- **nonlocal for reading**: NOT required; LEGB lookup finds outer variables automatically; nonlocal only needed for assignment/rebinding
- **logging.exception()**: GAP CLOSED — confirmed via observe task that execution continues after the call
- **Root logger**: `logging.getLogger()` (no args) = root; child loggers propagate to it

### Disputes Upheld
- f-strings in log call bodies: the %s-with-object-attributes pattern was never explicitly taught
- Orphan formatter in backtest.py: task placed a formatter with no attached handler — dead code was a task design fault

---

## Week 7, Day 5 — 2026-02-20

**Topic:** Week 7 Review + PCAP Full Simulation
**Score:** 83% (B) | **Time:** 45 minutes | **Difficulty:** 6/10

### Student Self-Assessment
- Relaxing yet useful session — reinforced concepts well
- Noted PCAP should be the main focus going forward

### Mentor Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Quick-fire gaps (no code) | 2/4 | Q1 WRONG (raise "error" is TypeError, not silent); Q2 WRONG (reading outer var works fine, no nonlocal); Q3 correct; Q4 correct |
| 2 — safe_divide() corrected | 9/10 | Both bugs fixed (ValueError caught at call site, %s style used); clean logger factory; all three paths demonstrated |
| 3 — audit_object() | 7/10 | Correct introspection logic but used print() throughout instead of returning a dict — function returns None |
| 4 — Predict + Fix (two traps) | 7/10 | Q1 correct (exception order A then C); Q2 wrong — bug is silent swallow returning None, not doubled output |
| 5 — make_validator() closure | 10/10 | Clean factory; correct closure capture (no nonlocal needed for reading); all 6 test values correct |
| 6 — PCAP Full Simulation | 7/10 | Q1 C correct; Q2 WRONG (iter(generator) returns same object); Q3 B correct; Q4 A correct; Q5 B correct; Q6 B correct; Q7 B correct; Q8 C correct; Q9 WRONG (__name__ = full dotted path); Q10 B correct |

**Total: 83% (B)**

### Key Corrections

- **Task 1 Q1 — raise "string"**: B is correct — TypeError at RUNTIME. Strings are not valid exception types. This is the 2nd occurrence of this gap.
- **Task 1 Q2 — reading outer vars**: B is correct — LEGB lookup finds the variable automatically. No nonlocal needed for reading. This is the 3rd+ occurrence.
- **Task 3 — audit_object()**: Must return the dict. Prints are fine for debugging but the function signature says `-> dict`. The function returned None.
- **Task 4 Q2 — decorator bug**: The bug is NOT doubled output. The wrapper catches the exception and swallows it — `result` is None because the wrapper returns nothing on error. The fix: add `raise` after `logging.exception(...)`.
- **Task 6 Q2 — iter(generator)**: Answer B is correct — `iter(obj)` on a generator returns the SAME generator object (generators implement both `__iter__` and `__next__`). This is the 5th+ occurrence of this gap.
- **Task 6 Q9 — __name__**: Answer C is correct — `__name__` equals the FULL dotted module path when imported: `algo_backtest.engine.backtest`. Only equals `"__main__"` when run directly. This is the 3rd occurrence.

### Persistent Gaps Entering Exams
1. `iter(generator) is generator` → True (5+ occurrences — must lock in for weekend)
2. `__name__` = full dotted path when imported (3rd occurrence)
3. `raise "string"` → TypeError at runtime (2nd occurrence)
4. reading outer variable in closure → works fine, no nonlocal (3rd+ occurrence)

---

---

## Week 7 — End of Week Summary

**Dates:** 2026-02-16 to 2026-02-20
**Topic:** Standard Library, Logging & Introspection
**Average Score:** (62% + 88% + 90% + 95% + 83%) / 5 = **83.6% (B)**

---

### Daily Scores

| Day | Topic | Score | Notes |
|-----|-------|-------|-------|
| 1 | logging Introduction | 62% | Tasks 6/7 excused — premature project integration |
| 2 | Scaffolded logging (Observe → Build) | 88% | Two-gate model clicked; singleton confirmed |
| 3 | logging + Introspection intro | 90% | Disputes upheld; print wrappers and f-strings accepted |
| 4 | logging Gaps + PCAP Crunch | 95% | logging.exception() gap finally closed |
| 5 | Week 7 Review + Full Simulation | 83% | iter/generator and __name__ still wrong |

---

### Strengths Observed

- **Two-gate filtering**: Locked in by Day 2, applied correctly under prediction pressure
- **Logger singleton**: Confirmed empirically with `is`/`id()` — understood conceptually
- **safe_divide()**: Correctly structured logging at caller site with %s style by Day 5
- **make_validator() closure**: Clean factory function, correct capture semantics, no nonlocal confusion for reading
- **Exception order trap**: Caught correctly (more general before specific = first match wins)
- **finally return**: Correctly predicted that `finally` return overrides `try` return (Day 5 Q3)
- **Late-binding lambda trap**: Correctly predicted `2 2 2` (Day 5 Q7)
- **Project integration**: BacktestEngine and setup_logging() built correctly after self-correction on root logger

---

### Recurring Gaps — Priority Targets for Weekend Exams

1. **`iter(generator) is generator` → True** (5+ occurrences)
   - Generators implement both `__iter__` and `__next__`; `iter()` just calls `__iter__` which returns `self`
   - Appeared in Weeks 6 and 7 multiple times — must be locked in before exam

2. **`__name__` = full dotted path when imported** (3rd occurrence)
   - `algo_backtest.engine.trade` when imported, `__main__` only when run directly
   - Confused with just the filename stem every time

3. **`raise "string"` → TypeError at runtime** (2nd occurrence)
   - Not a SyntaxError (parsed fine), not silent — TypeError when the raise statement executes
   - Both exams contain a question on this

4. **Reading outer variables needs no `nonlocal`** (3+ occurrences)
   - LEGB lookup works automatically for reads; nonlocal only required for assignment/rebinding

5. **`audit_object()` returned None instead of dict** (Day 5)
   - Using print() is fine for debugging but always honour the declared return type

---

### Project Progress (Week 7)

- `algo_backtest/engine/backtest.py`: logging added — `logger = logging.getLogger(__name__)`, INFO on open/close, DEBUG on tick
- `main.py`: `setup_logging()` added — configures root logger (self-corrected from named logger)
- Architecture is clean: module-level logger with propagation to root; no hardcoded `StreamHandler` in engine code

---

### Readiness for Week 8

- **Strong:** Two-gate filtering, logger singleton, basicConfig one-shot, propagation hierarchy, introspection basics
- **Must fix before exam:** iter(generator), __name__ when imported, raise "string"
- **Week 8 focus:** Exam crunch + documentation (docstrings, final charts)
- **Recommended weekend drill:** Both exams back-to-back; flag every question involving generators, __name__, and closures

---

## Week 8, Day 1 — 2026-02-23

**Topic:** Exam Crunch & Documentation
**Score:** ~82% (B) after disputes | **Time:** 2 hours | **Difficulty:** 5/10

### Student Notes
- Long and tiring session but completed all tasks
- Found two sim questions on untaught topics (__slots__, context managers)
- Correctly challenged both — __slots__ not PCAP, context managers not taught

### Mentor Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Gauntlet | 6/8 | Q1: print(x) fires once → [1,2]; Q3: result is 10+i not i |
| 2 — Scope drills | 3/3 | All correct |
| 3 — Exceptions | 5.5/7 | Hierarchy correct; __str__ hardcoded 99.0; catch should use `print(e)` |
| 4 — Docstrings | 7/10 | Dead code removed; prose style accepted; steps still in process_price |
| 5 — PCAP sim | 6/8 scored | 2 excused; Q6 *args is tuple; Q7 __repr__ default ≠ __str__ fallback |
| 6 — Decorator debug | 8/10 | Missed wrapper(*args, **kwargs) — only *args |
| 7 — Full backtest | 10/10 | Clean run, 4 positions, correct PnL and win_rate |

**Total: ~82% (B)**

### Key Corrections

- **Task 1 Q1**: `print(x)` fires ONCE at the end. `x` and `lst` are the same object (mutable default). After `f(1)` and `f(2)`, the list is `[1, 2]`. Only one print.
- **Task 1 Q3**: Default capture `i=i` works. But `x=10` is also passed. `fns[0](10)` = `10+0=10`, not `0`. Output: `10 11 12`.
- **Task 3 Q3 __str__**: Should use `self.price` dynamically, not hardcoded `99.0`.
- **Task 5 Q6**: `*args` is always `tuple`, never list.
- **Task 5 Q7**: `__repr__` default returns `<ClassName object at 0x...>`. `__str__` falls back to `__repr__`, not the other way around.
- **Task 6**: Third bug = `wrapper(*args)` missing `**kwargs`. Decorator doesn't forward keyword arguments.

### Disputes Upheld
- __slots__ excused (not in PCAP-31-03 syllabus)
- Context managers excused (not previously taught — added to lesson now)
- Validation in BacktestEngine: SRP argument accepted — validation belongs in Position

---

## Week 8, Day 2 — 2026-02-24

**Topic:** OOP Deep Drills + PCAP Simulation
**Score:** ~88% (B+) after disputes | **Time:** 2 hours | **Difficulty:** 6/10

### Student Notes
- Long session, 2 hours
- PCAP sim felt solid — metaclass question handled by reasoning
- Iterator protocol doesn't feel fully rooted yet
- Task 7 was redundant — files already documented

### Mentor Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Predict | 6.5/8 | Q6: circular list, a.next.next = a, val = 1 not None |
| 2 — OOP debug | 7/10 | Bug 1 identified; fix introduced positional order error in GuideDog super() call |
| 3 — PCAP sim | 12/12 | Perfect — all correct including untaught metaclass by reasoning |
| 4 — Iterator | 9/10 | Protocol correct; reset() print is side-effect code smell |
| 5 — Refactor | 8/10 | with + specific exceptions good; print() in utility = code smell; missed re-raise option |
| 6 — Trap | 10/10 | Class vs instance mutation fully understood |
| 7 — Docstrings | 10/10 | Excused — files already documented |

**Total: ~88% (B+)**

### Key Corrections
- **Q6 circular list**: `a.next.next` wraps back to `a` via the cycle; `.val` = 1
- **GuideDog super() args**: `super().__init__(name, breed, sound)` should be `super().__init__(name, sound, breed)` — positional order must match parent signature
- **print() in utility functions**: use logging or re-raise; callers shouldn't see stdout from helper functions

### Disputes Upheld
- Task 7 excused — Position and Trade already have docstrings

### Project Roadmap (noted for Days 3-5)
- R-multiple calculation: R = pnl / (abs(entry - sl) * qty)
- Strategy-aware Position: strategy_id + strategy_name attributes
- Per-strategy reporting grouped by strategy_id

---

## Week 8, Day 3 — 2026-02-25

**Topic:** R-Multiples & Strategy-Aware Positions
**Score:** ~83% (B) | **Time:** 2 hours | **Difficulty:** 7/10

### Mentor Assessment

| Task | Score | Notes |
|------|-------|-------|
| 1 — Warm-up | 4/5 | Q4 missing; Q6 excused (__iadd__ not taught) and correct; all others right |
| 2 — Project fix | 10/10 | stray print + .lower() on exit_reason — clean |
| 3 — R-multiple | 8/10 | Works; used __pnl backing var instead of self.pnl property — fragile, fixed by mentor |
| 4 — strategy_id | 9/10 | Works; trailing comma on line 42 made strategy_id a tuple — fixed by mentor |
| 5 — PCAP sim | 7/10 | Q5 zip pads with None (wrong: stops at shortest); Q6 *b is list not tuple; Q7 raise from __cause__ is TypeError |
| 6 — Traps | 7/9 | map exhaustion correct; *-unpacking types correct; None == None is True (not False) |

**Total: ~83% (B)**

### Key Corrections
- **zip**: stops at shortest iterable — no None padding. Use `itertools.zip_longest` for padding.
- **`*b` in assignment**: always produces a list, even when unpacking a tuple
- **`raise X from Y`**: `e.__cause__` is `Y` — the TypeError in this case
- **`None == None`**: True — `is None` is the convention because `==` can be overridden, not because it fails

### Bugs fixed by mentor
- `self.strategy_id = strategy_id,` → trailing comma → tuple. Removed.
- `r_multiple` used `self.__pnl` (None until pnl property called) → changed to `self.pnl`

---

---

## Week 8, Day 4 - 2026-02-26

**Topic:** Per-Strategy Reporting + Final PCAP Crunch
**Student Self-Report:** ~90 minutes | Difficulty: 5-6/10

### Mentor Assessment

**Overall Score: ~86%**

#### Task 1 — PCAP Warm-up (5.5/6)
- Q1: Correct (logic right, formatting not penalised)
- Q2: WRONG — `sorted(key=lambda x: -x)` sorts by negated key but returns ORIGINAL values → `[9, 5, 4]` not `[-9, -5, -4]`
- Q3: Correct (f(4) = 10)
- Q4: Correct (zip / zip(*zip))
- Q5: Correct (reduce product = 24)
- Q6: Correct ([C(1), C(2), C(3)])

#### Task 2 — trades_by_strategy() + strategy_report() (9.5/10)
Working implementation. Sound architecture.
- (strategy_id, strategy_name) tuple as dict key — correctly separates two DAXI strategies with different IDs
- Single source of truth respected (portfolio total uses self.completed_trades directly)
- Minor: `return None` vs `return {}` — type inconsistency with annotation, but does not crash
- Minor: strategy name/ID label inverted in print header (cosmetic)

#### Task 3 — PCAP Simulation (8.5/10)
- Q1: Correct (NoneType — format nuance, not penalised)
- Q2: Excused — property(getter, setter) classic syntax was never taught; answered A, full credit given
- Q3-Q7: All correct
- Q8: WRONG — isinstance(b, A) is True when B inherits from A. Correct answer: A (True True True)
- Q9-Q10: Correct

#### Task 4 — __str__ fix (10/10)
`__class__.__name__` works correctly in class method scope. Verified output correct.

#### Task 5 — PCAP Traps (10/10)
- Snippet A: Correct ([1,2,3] — rebinding creates new list object)
- Snippet B: Correct ([1,2,3,4] — += mutates in place)
- Snippet C: Correct given ambiguity (f(1) → 1, base case)

### Key Rules Confirmed This Session
- Format/cosmetic differences in predicted output → NEVER penalised
- Logic correct = full credit
- Two real mistakes to remember:
  1. `sorted(key=lambda x: -x)` → returns original values, sorted by negated key
  2. `isinstance(child, Parent)` → True (inheritance flows upward)

### Architecture Notes
- `completed_trades` flat list as single source of truth confirmed — correct design for Monte Carlo, per-strategy slicing, and portfolio-level analysis
- `trades_by_strategy()` derives groupings on demand without adding class attributes — clean and extensible


---

## Week 8, Day 5 - 2026-02-27

**Topic:** Final PCAP Crunch + Week 8 Review
**Student Self-Report:** ~45 minutes | Difficulty: 3/10

### Mentor Assessment

**Overall Score: ~97% — Strongest day of the program.**

#### Task 1 — Sort & isinstance warm-up (4/4)
All correct. Both Day 4 gaps drilled and closed:
- sorted(key=lambda x: -x) returns original values — confirmed correct understanding with explanation
- isinstance follows full inheritance chain — confirmed

#### Task 2 — Trap Gauntlet (6/6)
All 6 snippets correct. Notable: Snippet E (generator `in` exhaustion) — correctly predicted False + [] because 3 is never produced by range(5)*2.

#### Task 3 — PCAP Simulation (10/10)
Perfect. Includes Q2: iter(generator) is generator → True — gap closed after 5+ prior failures.

#### Task 4 — __repr__ on BacktestEngine (10/10)
Correct. __repr__ calls self.__str__(). Verified output matches.

#### Task 5 — Decorators + Exception flow (5/5)
All correct. Stacking order (@deco_a @deco_b) solid: A in → B in → hello → B out → A out.

#### Task 6 — Self-Assessment
Honest and accurate. Identified: complex inheritance edge cases, generators edge cases, and basic built-ins (lambda, etc.) as weakest areas. Aligns with observed performance history.

---

## Week 8 End-of-Week Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 82% | Exam Crunch & Documentation |
| 2 | 88% | OOP Deep Drills + PCAP Simulation |
| 3 | 83% | R-Multiples & Strategy-Aware Positions |
| 4 | 86% | Per-Strategy Reporting |
| 5 | 97% | Final PCAP Crunch |

**Week 8 Average: ~87.2% (B+)**

### Strengths Observed
- PCAP theory now sharp under timed conditions (3 perfect simulations this week)
- Project architecture decisions are professional-grade (single source of truth, on-demand grouping)
- Stacked decorators, closures, exception flow — all solid
- Takes disputes seriously and argues with evidence

### Recurring Mistakes This Week
- sorted(key=lambda x: -x) — original values not negated values (closed Day 5)
- isinstance(child, Parent) → True (closed Day 5)
- iter(generator) is generator → True (closed Day 5 after 5+ failures)

### Project Progress Assessment
- BacktestEngine: working, logging integrated, per-strategy reporting, __str__/__repr__
- Position/Trade: R-multiples, strategy_id/name propagation, encapsulation correct
- Architecture: ready for real data integration in Week 9

### Gaps Entering Week 9 / Weekend Exams
- Complex inheritance edge cases (MRO in diamond + super() chain)
- Generator protocol edge cases (resettable iterators, yield from on strings)
- PCAP basic built-ins: lambdas, sorted, filter, map, reduce under exam pressure
- OOP dunders: self-rated 3.5/5 — needs more reps

### Readiness Assessment
**Exam not yet ready — needs Week 9.** Strong B+ average but PCAP requires 70%+ consistently under exam conditions. The weekend exams will reveal remaining gaps. Week 9 plan: PCAP-heavy, drilling identified weak spots with official PCAP site material integration.


---

## Week 8 Exams — 2026-03-02

**Exam A: 28/30 = 93%** | 12 minutes
**Exam B: 23/30 = 77%** | 11 minutes
**Combined: 51/60 = 85%**

Exam A was outstanding — only 2 misses, both subtle name-mangling and MRO traps.
Exam B exposed a cluster of gaps under time pressure. All gaps logged and targeted for Week 9.

Both exams pass the 70% PCAP threshold. Week 9 focus: close the 7 Exam B gaps + PCAP-heavy drilling with official syllabus material.


---

## Week 9, Day 1 - 2026-03-02

**Topic:** Exam B Gap Closure
**Score: ~80%** | Short session, exhausted day

### Mentor Assessment

#### Task 1 — Warm-up (4.5/5)
Q1-Q4 all correct. Q5 wrong: format is `%(levelname)s:%(message)s`, call is `logging.warning(...)` → output is `WARNING:watch out`, not `DEBUG:watch out`. Minor level-name slip.

#### Task 2 — Name mangling (10/10)
Perfect. Both snippets correct. Exam A Q19 gap fully closed.

#### Task 3 — Simulation (4/6)
- Q1 A: Correct (+ creates new list, A.data untouched)
- Q2 B: Correct
- Q3 A: Wrong — level=INFO blocks DEBUG. Answer B (`INFO - started` only)
- Q4 A: Wrong — `*xs` → args tuple `(1,2)`, `**d` → kwargs dict `{'a':3}`. Return is `((1,2),{'a':3})`. Answer B
- Q5 D: Correct (both B and C cause RecursionError)
- Q6 A: Correct (D→B wins, E→C wins)

#### Task 4 — Self-check (6/10)
1. Partially correct — "parent class" misses the key point: same list object, .append mutates in place
2. Correct in spirit — imprecise on mechanism (should say: getter calls getter, not "self referencing each other")
3. Wrong framing — f(*a, *b) passes 4 integers; f(a, b) passes 2 lists. Not about "freedom of assignment"

### Key notes
- Logging level trap recurring under pressure — must read threshold carefully
- *xs, **d unpacking type distinction (tuple vs list) still not solid


---

## Week 9, Day 2 - 2026-03-03

**Topic:** PCAP Heavy: Unpacking, Logging, Strings & Exception Traps
**Score: ~83%** | ~30 minutes | Difficulty: moderate

### Mentor Assessment

#### Task 1 — Logging + Unpacking (6/6)
All correct including Q6 (basicConfig one-shot, first call wins at DEBUG). Both Day 1 gaps closed.

#### Task 2 — String Gauntlet (5.5/6)
Snippet A: `"hello world"[2:8:2]` → indices 2,4,6 = l,o,w → `low` not `lo w`.

#### Task 3 — Simulation (8/10)
- Q6: Wrong — `f() is None` → True (answer B, not A)
- Q8: Wrong — `n = n+1` → n=6 before inner returned; closure captures 6; `6*2=12` (answer B, not C)

#### Task 4 — Exception Hierarchy (7/10)
- Q1: Hierarchy correct, direction disputed — full credit
- Q2: Wrong — `except Exception` before `except ValueError` → Exception catches first. Parent-before-child means parent wins.
- Q3: Correct (logic right — type(e).__name__ = MyError, logic scored)
- Q4: Wrong — `except IOError` before `except FileNotFoundError` → IOError catches first. Same mistake as Q2.
- Q5: Correct

**Critical rule to memorise:** In `except` chains, always order most-specific FIRST. If parent appears before child, parent catches everything matching it.

#### Task 5 — Scope (3.5/4)
Snippet A: `UnboundLocalError`, not `AttributeError`. Python pre-scans function and marks `x` as local because of the assignment `x = "local"`. Reading `x` before assignment → UnboundLocalError.

#### Task 6 — Project (10/10)
Trivial fix done correctly. Output verified and correct.


---

## Week 9, Day 3 — 2026-03-04 | Score: ~85%

**Topic:** Gap Closure — except ordering, UnboundLocalError, closures + DataLoader wiring

### Task 1 — Warm-up (4/6)
- Q1 ✓ Exception (parent catches first — understands why)
- Q2 ✗ Answered FileNotFoundError; OSError appears before it and catches first → OSError
- Q3 ✓ UnboundLocalError
- Q4 ✓ 10 then 20
- Q5 ✗ Answered 40; make_adder(3): n=3 → n=3*10=30 → fn(1)=1+30=31. Arithmetic trace incomplete.
- Q6 ✓ [4, 4, 4]

### Task 2 — except ordering (4/4) — GAP CLOSED
All correct. Rule stated cleanly. Parent-before-child trap fully internalised.

### Task 3 — UnboundLocalError (3.5/4)
- Q1-Q3 ✓
- Q4 ✗ counter() without global: `count += 1` makes `count` local, reading before assignment → UnboundLocalError. Not "no output, would be 1". Same trap as Task 1 Q3 from a different angle.
- Explanation of mechanism: correct intuition about pre-scan. Precise wording: Python compiler marks any assigned name as local throughout the function at compile time, before runtime begins.

### Task 4 — PCAP Simulation (8/10)
- Q1-Q4 ✓ (args/kwargs, class var shared mutation, send(), shallow copy)
- Q5 ✗ Logging two-gate: logger.setLevel(DEBUG) passes debug messages from logger, but basicConfig(WARNING) sets root handler to WARNING. Handler blocks debug. Answer B, not A. **3rd session with same error.**
- Q6-Q10 ✓ (name mangling, mutable default, exception variable str(), iterator state, nonlocal)

### Task 5 — Closure capture (3/3) — GAP CLOSED
All three snippets correct. Default-arg snapshot fix pattern fully understood.

### Task 6 — Project: DataLoader
Full credit. User's architectural decisions:
- self.columns populated from actual CSV header → schema-agnostic. Correct.
- Column validation removed — correct: no fixed schema to validate against.
- get_close_series() declined — correct: which column feeds the engine is a caller decision, not DataLoader's.
- NaN check and high/low sanity check retained — correct: data integrity, not schema checks.
User also flagged EOBI tick data as future direction: tick-level feeds would resolve same-candle SL/TP ambiguity.

### Remaining Gaps for Day 4
1. Logging two-gate — PRIORITY (3 sessions, same error)
2. UnboundLocalError in augmented assignment without global
3. Closure arithmetic: full trace of enclosing-scope mutations before closure is called

---

## Week 9, Day 4 - 2026-03-05

**Topic:** Logging two-gate (3rd session), UnboundLocalError, closure arithmetic

### Mentor Assessment — Score: ~88%

---

### Task 1 — Logging two-gate (5.5/6)

- Q1 ✓ Both messages print (basicConfig DEBUG → root handler passes all)
- Q2 ✓ Only error (logger.ERROR gate blocks warn before handler)
- Q3 ✓ Only warn and error (logger passes all, handler blocks debug/info)
- Q4 ✓ Only warn (basicConfig one-shot, first call at WARNING wins)
- Q5 ✓ Both print — CORRECT. Child level=DEBUG passes info, propagates to parent's handler (level=DEBUG). Both messages reach the handler.
- Q6 ✓ warn prints (LastResort handler at WARNING level, bare format)

**Note on Q5:** Initially you stated "parent's rules work for the handler here and pass both messages" — correct outcome, but phrasing suggests the parent's logger level gates the child's messages. It does not when child has its own setLevel(). The child's level gates first, then propagation sends to parent's handler directly.

---

### Task 2 — UnboundLocalError on augmented assignment (4.5/5)

- Q1 ✓ UnboundLocalError — total += n contains assignment → total is local → read before assign
- Q2 ✓ [1] — items.append(x) contains no assignment to items → LEGB finds it in enclosing/global scope → no error
- Q3 — Partial credit. You said "lists behave differently" (0.5/1). The real mechanism: the presence or absence of an ASSIGNMENT STATEMENT to the name in the function. `total += n` is assignment. `items.append(x)` is a method call — no assignment to `items`. Python decides local vs non-local at compile time, not runtime. The type (list vs int) is irrelevant.
- Q4 ✓ 2 — global counter fixes the binding
- Q5 ✓ UnboundLocalError — x += 1 in inner() → x is local to inner → read before assign

**Gap closed:** You correctly identified both UnboundLocalError cases (Q1, Q5). The mechanism explanation was the only gap.

---

### Task 3 — Closure arithmetic (4/4) — GAP CLOSED

- Q1 ✓ n=12, f(2)=24
- Q2 ✓ result=14, fn()=14
- Q3 ✓ val=30, g()=30
- Q4 ✓ n=30, h()=31 — closure captures reference, not snapshot; n=n*10 runs before step1 is ever called

**Your observation on Q4:** Flagged as bad code smell (PEP 8/readability). Correct. In real code review, defining a closure before mutating the variable it captures is an anti-pattern. The Python semantics are correct but unintuitive. This IS a real trap — it appears in PCAP because it tests whether you understand late binding vs snapshot semantics.

---

### Task 4 — PCAP Simulation (7.5/10)

- Q1 ✓ A — ValueError
- Q2 ✓ A — True <class 'NoneType'>
- Q3 ✗ B answered. Correct: A — `a, *b, c = (1,2,3)` → b=[2] (list). **`*b` in starred unpacking ALWAYS produces a list regardless of source type.**
- Q4 ✓ C — AttributeError after del a.x
- Q5 ✗ B answered. Correct: D. logger "app" has its own handler (level=ERROR) + propagates to root (basicConfig INFO handler). `info` → blocked by app handler but passes to root handler (INFO level) → 1 line. `error` → passes app handler AND root handler → 2 lines. Total: 2 lines, info from root, error from both. **This is the hardest logging variant.**
- Q6 ✗ A answered. Correct: B — `0.1 + 0.2 == 0.3` → **False** (IEEE 754 floating point). `0.1 + 0.2 = 0.30000000000000004`.
- Q7 ✓ A — args=(2,3), b=99, kwargs={'c':4,'d':5}
- Q8 ✓ C — Base+Child
- Q9 — Correct answer (False, [9,16]) not in options. You caught this. The generator exhausts UP TO AND INCLUDING the first element ≥ 3 that matches — `3 in gen` checks 0→1→4→ (no 3 found, exhausts up to 9 at x=3 which gives 9... wait: x=0→0, x=1→1, x=2→4 (no match), x=3→9 (no match for 3 in [0,1,4,9,16]). `3 in gen` → False (3 never appears). Generator consumed through x=4 (value 16). list(gen) → []. So answer is False, []. None of the options match. Full credit for catching the error.
- Q10 ✓ C — `raise X from None` suppresses chaining, __cause__=None

---

### Task 5 — errno & binary I/O (3.5/4)

- Q1 ✓ exc.errno = integer OS error code on the exception instance; errno.ENOENT = symbolic constant (value=2) for "no such file or directory"
- Q2 ✓ True, True — IOError and EnvironmentError are aliases for OSError in Python 3
- Q3 ✗ Stated Exception → OSError → FileNotFoundError (most-general first). Question asked most-specific first. Correct: **FileNotFoundError → OSError → Exception**. Most specific first in except clauses — or Python catches the parent class and never reaches the child.
- Q4 ✓ readinto() fills a pre-existing bytearray in-place and returns the number of bytes read (no new object created); read() returns a new bytes/str object

---

### Task 6 — Project: main.py DataLoader wiring (full credit)

Working output confirmed:
- DataLoader loaded 50 rows from ohlc_mock_data.csv
- Columns printed, row count printed, head(3) printed
- iterrows() loop over head(10) printing close prices
- Engine block kept commented out

User initiative: used head(10) instead of head(5) — minor deviation, no deduction.

---

### Remaining Gaps for Day 5
1. **Logging double-propagation** — named handler + root handler both fire when propagate=True (T4 Q5, now 4th session)
2. **`*b` starred unpacking** → always list even from tuple source (T4 Q3)
3. **IEEE 754** — `0.1 + 0.2 == 0.3` → False (T4 Q6, classic PCAP trap)
4. **except clause ordering** — most-specific first (T5 Q3)


---

## Week 10, Day 1 - 2026-03-17

**Topic:** PCAP Review warm-up — mutable defaults, MRO, basicConfig one-shot

### Mentor Assessment — Score: ~83% (2.5/3)

**Exercise 1 — Mutable default argument (0.5/1)**
- `[1, 2]` ✓ and `[3]` ✓ — both correct
- `f(4)` answered `[3, 4]` ✗ — correct answer `[1, 2, 4]`. `f(3, [])` uses a fresh explicit list and does not touch the shared default. Default after f(1) and f(2) is `[1, 2]`. f(4) appends to it → `[1, 2, 4]`.

**Exercise 2 — MRO + super() (1/1)**
- `ACB` ✓ and `D → B → C → A` ✓
- User requested explanation. Delivered: C3 linearisation rule — left-to-right depth-first, no class before all its subclasses appear. super() follows MRO of the actual object, not the declaring class's direct parent. This is why B.super() hits C, not A.
- User noted this feels like an edge case — correct. Real code avoids diamond inheritance. Still testable on PCAP.

**Exercise 3 — basicConfig one-shot (1/1)**
- Identified root cause correctly: first basicConfig call wins, second is silently ignored.
- Fix correct: one call with level=DEBUG.
- User feedback: logging is not prominently on the PCAP syllabus they studied. Agreed — logging questions in review week will be minimal (1-2 per set, most testable patterns only).

### Session Notes
- Light session by design (busy day). 3 exercises only.
- Week 10 = full PCAP review week. Target: sit exam next weekend.
- Day 2 onwards: full task sets covering all PCAP sections systematically.

---

## Week 10, Day 2 - 2026-03-18

**Topic:** PCAP Full Review — exceptions, OOP, scope, generators, functional, strings, simulation

### Mentor Assessment — Score: 95% (37/39)

**Task 1 — Exceptions (5/5)**
All correct. finally overriding return, bare raise re-raising, nested try/except routing all clean.

**Task 2 — OOP (5.5/6)**
Q1-Q5 all correct. Q6 miss: `print([a])` → `[repr_A]` not `[str_A]`.
Rule: containers display elements via `__repr__`. Only `print(a)` and f-strings use `__str__`.
Also: `print(f"{a}")` → `str_A` (not `{repr_A}` — no braces in output, f-string calls __str__).

**Task 3 — Scope (5/5)**
Late binding (Q4) and default-arg snapshot (Q5) both correct. These were recurring gaps — now closed.

**Task 4 — Generators (5/5)**
All correct including exhausted generator returning `[]` on second list(), custom iterator protocol,
yield from chaining. User noted decorator execution order intuition — correct observation.

**Task 5 — Functional (5/5)**
All correct. Stacked decorators (Q5) correct — outer before/after wraps already-decorated function.

**Task 6 — Strings (4.5/5)**
Q1-Q4 all correct. Q5: `123` and `cab` correct. f-string alignment `f"{'hello':>10}"` unknown.
Answer: right-aligns in field of 10 chars → `     hello`. Operators: `<` left, `>` right, `^` centre.
This IS on PCAP syllabus.

**Task 7 — Simulation (7/8)**
Q5 miss: `bool("0")` → True. Any non-empty string is truthy regardless of content.
Only `""` is falsy. `"0"`, `"False"`, `"None"` are all True.
All other 7 correct including shallow copy (Q8), dict mutation safety (Q6), parameter ordering (Q7).

### Session Notes
~60 minutes. Strong performance across all sections. Two small gaps remain:
1. `__repr__` vs `__str__` in container context
2. Truthy strings — non-empty = always True

---

## Week 10, Day 2 - 2026-03-18

**Topic:** PCAP Full Review — Exceptions, OOP, Scope, Generators, Functional, Strings

### Mentor Assessment — Score: ~95% (37/39)

**Task 1 — Exceptions (5/5)**
All correct. Q3 (finally overrides return → 3) and Q4 (bare raise re-raises, "done" never printed) both clean.

**Task 2 — OOP (5.5/6)**
Q1-Q5 ✓. Q6 ✗ partial:
- print([a]) → [repr_A] not [str_A]. Containers call __repr__ on elements.
- f"{a}" → str_A not {repr_A}. F-strings call __str__. Output has no braces.
Rule: print()/f-strings → __str__. Any container ([a], {a}, (a,)) → __repr__ on elements.

**Task 3 — Scope (5/5)**
Late binding [3,3,3,3] ✓ and default-arg snapshot [0,1,2,3] ✓. Gap fully closed.

**Task 4 — Generators (5/5)**
All correct. Custom iterator protocol, yield from, exhausted generator all clean.

**Task 5 — Functional (5/5)**
Stacked decorators (before/before/hello/after/after), reduce with initial value. All correct.
User observation on decorator execution order noted — correct intuition (func() runs and prints as side effect before "after" prints).

**Task 6 — Strings (4.5/5)**
Q1-Q4 ✓. Q5: 123 ✓, cab ✓. f"{'hello':>10}" unknown — noted as PCAP relevant.
Format spec: < left-align, > right-align, ^ centre. Field width follows the symbol. Know all three.

**Task 7 — Simulation (7/8)**
Q1-Q4 ✓, Q6-Q8 ✓. Q5 ✗: answered B (True False True), correct A (True True True).
bool("0") = True. Non-empty string is always truthy regardless of content. Only "" is falsy.

**Day 3 plan:** PCAP module drills — File I/O, os, datetime, time, calendar.

---

## Week 10, Day 3 - 2026-03-19

**Topic:** Mock 1 gap drill, File I/O, os, datetime/time/calendar, PCAP simulation

### Mentor Assessment — Score: ~84% (29.5/40)

**Task 1 — Mock 1 gap drill (8/10)**
Q1-Q3 ✓, Q5-Q9 ✓, Q10 ✓.
Q4 ✗: answered D (reads line by line). Correct: C (FileNotFoundError). open() raises before iteration begins if file doesn't exist. Iterability is irrelevant when open() itself fails.
Q3 ✓: bare except before typed clause = SyntaxError. Confirmed correct understanding.

**Task 2 — File I/O (4.5/6)**
Q1 ✓ (2, 'hello\n'). Q4 ✓ ('x' mode). Q6 ✓ ('' on exhausted).
Q2 ✗: wrote 'abc' with quotes. print(f.read()) output has no quotes — quotes are repr() not str().
Q3 ✗: wrote 'hello ' with space and quotes. f.read(5) on 'hello world' = 'hello' (no space, no quotes). f.tell() = 5 ✓.
Q5 ✗ partial: wrote line1\n without quotes. Question asked repr(line) — repr adds quotes: 'line1\n'.

**Task 3 — os module (4/6)**
Q3 ✓ (basename/dirname/splitext). Q4 ✓ (os.name = 'nt'/'posix').
Q1 partial: type(os.environ) is os._Environ not plain dict.
Q2 partial: os.mkdir requires ALL parents to exist — fails with FileNotFoundError if any parent is missing. os.makedirs creates whole path including parents.
Q5 ✗: os.path.join with relative components has no leading slash. Output: 'algo_backtest/data/prices.csv' (Linux) or 'algo_backtest\data\prices.csv' (Windows).
Q6 ✗: os.rmdir fails most likely because directory is NOT EMPTY. If it didn't exist: FileNotFoundError. Non-empty: OSError.

**Task 4 — datetime/time/calendar (6/8)**
Q1-Q3 ✓, Q5-Q8 ✓.
Q4 ✗: type(t).__name__ = 'struct_time' not 'time'. tm_wday=2 for Wednesday ✓.

**Task 5 — PCAP simulation (7/10)**
Q1-Q4 ✓, Q7 ✓, Q9-Q10 ✓.
Q5 ✗ (3rd time): tuple += creates new tuple. x=(1,2,3) unchanged, y=(1,2,3,4).
Q6 ✗ (3rd time): str(e) = 'v' not 'ValueError: v'. print() calls str(), not repr().
Q8 ✗ (4th time): *b always list. a, *b, c = [1,2,3,4,5] → b=list [2,3,4], not tuple.

**3 gaps must close before exam:**
1. *b unpacking → list always
2. tuple += → new object, original unchanged
3. str(exception) → message only

---

## Week 10, Day 4 - 2026-03-20

**Topic:** Persistent gap elimination + module drill + PCAP simulation

### Mentor Assessment — Score: ~88% (29/33)

**Task 1 — *b → list (5/5) — GAP CLOSED**
All correct. Q4: x, *y, z = [99] → ValueError (needs ≥2 elements). Correct conclusion, correct reasoning.

**Task 2 — tuple += (5/5) — GAP CLOSED**
All correct. Q4 key insight delivered: t += (99,) inside f() creates new tuple bound to local name t — discarded on return, x in outer scope unchanged. Q5: list += mutates in-place → x in outer scope IS affected.

**Task 3 — str(exception) (4.5/5) — GAP CLOSED**
Q1 partial: repr(ValueError("msg")) = ValueError('msg') — parentheses and single quotes, NOT "ValueError: msg". Colon format is traceback display only. Q2-Q5 all correct.

**Task 4 — Module drill (6.5/8)**
Q1 ✓ seed() reproducibility. Q4 ✓ os.path.exists returns False. Q5 ✓ abcdef. Q6 ✓ writelines no newlines → 1 line.
Q2 ✗: random.choice([]) → ValueError not IndexError. Python validates non-empty before indexing.
Q3 partial: os.path.split returns ('/home/user/project', 'main.py') — no trailing slash on dir component.
Q7 partial: os.path.dirname returns 'data/raw' not 'data/raw/' — same trailing slash issue.
Q8 ✗: exist_ok=True → both calls run silently (B), not D. Second call does nothing AND raises no error — B and D say the same thing about the second call, but B correctly describes both calls.

**Task 5 — Simulation (8/10)**
Q1 ✓ ValueError. Q2-Q3 ✓ gaps closed. Q4 ✓ WEDNESDAY=2, Thursday=3. Q5-Q6 ✓ struct_time. Q7-Q10 ✓.
Trailing slash issue appeared again in simulation.

**Day 5 plan:** Code-writing tasks (no ABCD), + project: load real FDAX data, implement VWAPStrategy, wire into run_backtest(), print strategy_report().

---

## Week 10, Day 5 - 2026-03-21

**Topic:** Code writing drills + Project: VWAPStrategy + real FDAX data
**Score: ~82% (B)**

---

**Task 1 — flatten() — 7/10**
Logic correct, works for all cases. Missed the requirement: use a list comprehension (one line body). Used a for loop with .append() instead.
Correct one-liner: `return [el for item in nested for el in ([item] if not isinstance(item, list) else item)]`

**Task 2 — BoundedList — 7/10**
Architecture correct (composition, not inheritance). Three issues:
- `values` returns `self._items` directly (reference leak) — must return `list(self._items)` (copy)
- `average` implemented as @property, task required `average() -> float` (method)
- No empty guard in average — `ZeroDivisionError` on empty list

**Task 3 — Timer — Skipped (agreed)**
Context managers not on PCAP syllabus. Deferred to post-PCAP project work.

**Task 4 — Bug fixes — mixed**
- Snippet A: 4/10. Misread the bug — original crashes with ZeroDivisionError on empty input. Fix should guard for empty, not rewrite to running average. New implementation still crashes on empty (`UnboundLocalError` on `moving_avg`).
- Snippet B: 10/10. Perfect diagnosis and fix.
- Snippet C: 10/10. Correct. Good note on try-except-else alternative.

**Task 5 — Real FDAX data — 10/10**
216,932 rows, 10 NaN values. Pipeline confirmed working. Assessment: 10 missing in 216k M1 bars is negligible — correct call.

**Task 6 — VWAPStrategy — 8/10**
Correct inheritance, correct signals, docstrings present. Two issues:
- Missing `else: signal = 'HOLD'` for close == vwap case → `UnboundLocalError` if triggered
- `get_name()` override is identical to parent — delete it (dead code)

**Task 7 — run_backtest() — 9/10 (execution) + strong architecture thinking**
Working end-to-end on real 216k-row data. Using strategy object as dict key is creative and works.
One inconsistency: signal generated on `row['open']` but `process_price` called with `data.iloc[idx]['close']` — mixing open/close. Pick one column consistently.

**Roadmap analysis (honest):**
- RTH datetime filtering: excellent, correct next step
- Multi-strategy in parallel: architecture already correct with current_positions dict — one step away
- Portfolio equity curve via sorted trade timestamps: sound approach, standard in backtesting
- Sharpe/Monte Carlo: premature until equity curve is working — build foundation first
- Needs: `exit_datetime` on Trade object for equity curve reconstruction

**Week 10 Summary (all 5 days):**
| Day | Score | Topic |
|-----|-------|-------|
| 1 | ~83% | Light warm-up: mutable defaults, MRO, basicConfig |
| 2 | ~95% | Full PCAP review — exceptions, OOP, scope, generators |
| 3 | ~84% | Mock 1 gap drill, File I/O, os, datetime/calendar |
| 4 | ~88% | Persistent gap elimination (*b, tuple+=, str(e)) |
| 5 | ~82% | Code writing + VWAPStrategy + real FDAX data |

**Week 10 Average: ~86% (B+)**

**PCAP readiness:** Strong. All major topic gaps closed across the week. Persistent triples (*b→list, tuple+=, str(e)) confirmed closed on Day 4. Exam target next weekend — achievable.

---

## Week 10, Day 5 - 2026-03-21

**Topic:** Code writing drills + VWAPStrategy + real FDAX data
**Score:** ~82%

### Task Assessment

**Task 1 — flatten():** Correct. List comprehension approach clean and Pythonic.

**Task 2 — BoundedList:** Needed hints. Initial approach tried inheriting from `list` while also managing `self.__values` — two conflicting models. Fixed to internal `_items: list[float]`. Also caught `self.remove([0])` (searches by value) vs correct `self._items.pop(0)`. Final result correct.

**Task 3 — Timer context manager:** Skipped by agreement. `__enter__`/`__exit__` not on PCAP syllabus, never drilled.

**Task 4 — Bug fixes:** All 3 correct.
- Snippet A: `running_average([])` — ZeroDivisionError, guard with `if not values: return 0.0`
- Snippet B: mutable `items = []` class attribute — moved to `__init__` as `self.items = []`
- Snippet C: `find_csvs` unhandled `FileNotFoundError` — wrapped in try/except

**Task 5 — Real FDAX data:** Full success. 216,932 rows, 10 NaN values (acceptable for 11 months of M1 data). DataLoader pipeline confirmed working with schema-agnostic column loading.

**Task 6 — VWAPStrategy:** Clean implementation. Inherits BaseStrategy correctly. BUY/SELL/HOLD logic correct. Minor: added `signal = None` guard before if/elif to avoid potential `UnboundLocalError` on HOLD path — good defensive coding.

**Task 7 — run_backtest():** Exceeded task spec. Used `current_positions = {vwap_strategy: None}` dict instead of simple `current_position = None` flag — correct architectural decision enabling multi-strategy support. Pipeline ran 206k trades, confirmed working. Strategy report output clean.

**Roadmap confirmed:**
1. RTH session filtering (time-of-day condition on signals)
2. Multi-strategy parallel testing
3. Equity curve (trade datetime + PnL → sorted df)
4. Metrics: Sharpe, Profit Factor, Monte Carlo

---

## Week 9 Weekend Exam Session - 2026-03-22/23

**Exam A Score: 84.6% | Exam B Score: 80% | Combined: ~82%**

### Exam A Breakdown (26 counted questions, 4 discarded as non-PCAP)

Discarded by user (correct call — not on PCAP syllabus): Q15 (__slots__), Q17 (generator.close()), Q24 (logging), Q25 (logging).

**Wrong answers:**
- Q2: `os.path.exists("/")` — returns True not False. exists() checks presence, not emptiness.
- Q3: `__init__.py` is OPTIONAL in Python 3 (namespace packages). Answer B, not A.
- Q26: `IOError is OSError` evaluates to True — they are aliases. Answer B, not A.
- Q28: `bytearray(3)` → `[0, 0, 0]` as integers. Answer A, not C.

**Strong areas:** strings, exceptions, generators, functional, closures, scope — all correct.

### Exam B Breakdown (30 questions, all PCAP-relevant after swap)

**Wrong answers:**
- Q3: `__all__ = [foo, bar]` — no quotes, variable refs → NameError. Strings required. Answer A.
- Q8: bare `raise` re-raises; outer `except ValueError` catches it. Both `caught` and `outer` print. Answer C.
- Q11: `int("abc")` → `ValueError` not `TypeError`. Answer A.
- Q12: MRO `D(B,C)` → `[D,B,C,A]`. String builds on unwind: A→AC→ACB. Answer B.
- Q16: `Circle` doesn't implement `area()` → `TypeError: Can't instantiate abstract class`. Answer B.
- Q17: `yield` anywhere in function body → always a generator function. `return` before `yield` just makes it exhaust immediately. Answer A (`generator`, `[]`).

### Week 11 Gap Targets
1. MRO string trace (ACB not ABC) — lesson created: week11_mro_super.md
2. ABC: must implement ALL abstract methods
3. bare `raise` behaviour — re-raises, outer handler still fires
4. `yield` + early `return` = still a generator
5. `__init__.py` optional in Python 3
6. `IOError is OSError` = True (aliases)
7. `bytearray(n)` elements are integers, not bytes repr

---

## Week 11, Day 1 - 2026-03-23

**Topic:** MRO & super() | ABC | Exam gap closure
**Score:** 86% (6/7)

**T1 — MRO mixed trace (CAB):** Correct. Good — mixed prepend/append pattern handled properly.
**T2 — __init__ chain:** Correct. Print order A→C→B→D and len=0 both right.
**T3 — Chain break:** Correct. BC, A unreachable because B has no super() call.
**T4 — ABC:** Correct (TypeError), excluded from score — user correctly identified ABC not on PCAP syllabus.
**T5 — yield + early return:** WRONG. Answered [1,2]. Correct: []. `return` fires before any yield. The `yield` keywords make it a generator function, but the body exhausts immediately on first next() — list(g) = [].
**T6 — bare raise:** Correct. Re-raises propagate to outer handler.
**T7 — IOError vs OSError:** WRONG. Answered C (False). Correct: B (True). IOError is a direct alias for OSError in Python 3 — same class, same object. `except IOError` catches it, `.errno` is populated with ENOENT=2.
**T8 — __init__.py:** Correct. Optional in Python 3 (namespace packages), B.

**User feedback:** Session too short, wants heavier volume Day 2. Requested: file I/O, os module, datetime, generators + gap targets. PCAP only.

---

## Week 11, Day 2 - 2026-03-24

**Topic:** File I/O | os module | datetime | Generators | Gap closure
**Score:** 82% (27/33)

**T1 — yield+early return:** ✅ CLOSED. Both variants correct: `generator`/`[]` and `[None]`.
**T2 — IOError is OSError:** ✅ CLOSED. All three `True` correct.
**T3 — readlines() + repr():** ✗ Missing quotes and `\n` in repr output. `repr('line1\n')` = `"'line1\n'"` — repr always shows escape sequences literally.
**T4 — read(n) cursor:** ✗ Two errors: `read(3)` twice on `"hello"` = `'hel'` then `'lo'` (not `'llo'`); exhausted stream = `''` not `' '`.
**T5 — readline():** ✅
**T6 — os.path functions:** ✅ partial. basename/dirname correct. split() tuple answer missing leading slash and string quotes. splitext unknown — returns `('/path/file', '.ext')`.
**T7 — os.path.join Linux:** ✗ Answered A (Windows backslash). On Linux `os.path.join` uses `/`. It is platform-aware — this is PCAP relevant.
**T8 — datetime arithmetic:** ✅
**T9 — timedelta:** ✅ (total_seconds arithmetic excluded — unjustified to penalise)
**T10 — strftime:** ✅
**T11 — generator partial consumption:** ✅ Correctly identified remaining items after partial next() calls.
**T12 — yield from:** ✅
**T13 — exhausted generator:** ✅ StopIteration correct.
**T14 — errno + FileNotFoundError:** Partial. Type (`FileNotFoundError`) correct. Missed that `e.errno` = `2` (ENOENT) prints first.
**T15 — UnboundLocalError + nonlocal:** ✅ Correct diagnosis and clean fix.

**Gaps closed this session:** yield+early return, IOError is OSError alias
**Remaining/new gaps:** repr() shows quotes+escapes literally, read(n) cursor arithmetic, os.path.join is platform-aware (Linux=/), splitext tuple format, errno numeric value (ENOENT=2)

## Week 12, Day 1 — 2026-03-30

**Topic:** Exceptions + ALL real exam gaps (type(e), bare except, custom __str__, __bases__/__mro__/__dict__, lambdas, list comp order, open() modes, 2. float, name mangling)
**Score:** 88% (7/8)

**Mentor Assessment:**

T1 — Perfect. `type(e)` trap fully understood. Dog-in-animal-cage model is solid.

T2 — Part A correct. Part B incomplete — student stated confusion rather than tracing. The key insight missed: `assert m != 0` fires BEFORE the inner try, AssertionError is NOT ArithmeticError, so bare `except` catches it → m=1. This exact mechanism needs more drills.

T3 — A correct. C correct (valid code, correct output). B: good question from student — the difference is `e.args`: WITH super().__init__() args is populated, WITHOUT it's empty tuple. `__str__` output looks identical, but args is the hidden difference.

T4 — B correct. One error in A: `'y' in A.__dict__` is False — y is an instance attribute set in __init__, lives on instances not the class. This is a critical distinction that WILL appear on the retake.

T5 — All correct. Student confused about parameter vs argument terminology — clarified. Lambda-as-argument naming trap now understood.

T6 — All correct. List comp order and open() modes both solid.

T7 — B and C correct. Student correctly flagged that octal/hex validity drills are overkill for PCAP. Adjusted scope for future: float trap + underscore sep + bytes/bytearray.

T8 — Perfect. Name mangling inheritance fully understood including accessing _C__VarA directly.

**Code quality note:** `InvalidPriceError` implementation is correct. Minor: no need for redundant parentheses around `(a)`.

**Patterns to address in upcoming days:**
1. assert/propagation chains — needs more drills (T2B gap)
2. class `__dict__` vs instance `__dict__` — one more drill needed
3. platform + os module functions — expand coverage
4. bytes/bytearray — add to T7-style tasks

## Week 12, Day 2 — 2026-03-31

**Topic:** OOP internals, assert propagation, __dict__, isinstance/type, name mangling, MRO, platform/os, bytes/bytearray
**Score:** 90% (7 PCAP tasks)

**Mentor Assessment:**

T1 — Perfect. Propagation chain rule locked in across all 3 patterns.

T2 — Perfect. Shadow case (a.x=2, A.x=1) correct. __dict__ class vs instance now solid.

T3 — Perfect. isinstance(True, int)=True and type(True) is int=False both correct. Bool/int subclass trap understood.

T4 — One error: hasattr(Top, 'reveal') is True, not False. hasattr checks the full MRO. To check only the class's own namespace use 'reveal' in Top.__dict__. Worth drilling once more.

T5 — Perfect. MRO trace correct. TypeError explanation correct.

T6 — Perfect. All platform and os functions identified correctly.

T7 — Mostly correct. b"hello"[0] returns integer 104 (correct). b"abc" == bytearray(b"abc") is True (compare by value) — not False as answered. Noted: ASCII value questions dropped from future drills; focus on TYPE returned (int) and mutability distinction only. list(bytearray) = list of ints, not chars — correctly understood.

T8 — Project not completed (debugging session). Three bugs diagnosed:
(1) break before inner loop = dead code
(2) no one-trade-per-day constraint = unlimited re-entry
(3) newly_closed references wrong strategy variable
Fix planned for Day 3.

**Patterns to continue drilling:**
- hasattr vs __dict__ membership distinction
- bytes == bytearray value equality
- One more lambda-as-argument pattern

## Week 12, Day 3 — 2026-04-01

**Topic:** Strings, closures/nonlocal, generators, hasattr vs __dict__, finally/return, run_backtest fixes
**Score:** 90% (7/7 PCAP tasks + T8 project working)

**Mentor Assessment:**

T1 — Correct. rindex added to next string drills per user request.

T2 — Correct. \r mental model solid. All escape sequence lengths correct.

T3 — Correct. Loop-closure pattern known — removed from future drills. nonlocal pattern confirmed solid.

T4 — Correct. Generator pause/resume, early return, loop-based generator all correct.

T5 — Perfect. hasattr vs __dict__ gap closed from Day 2.

T6 — All 5 PCAP simulation questions correct. Mutable default arg, generator exhaustion, closure scope, slicing, finally all solid.

T7 — Correct. finally + raise clarified: finally runs between except handler finishing and return leaving — only overrides if finally itself has return.

T8 — LPP strategy working end-to-end. 93 trades, 48.4% win rate, +$137 PnL. Two issues queued:
(1) PositionManager not iterable — for position in self.position_manager → needs .positions
(2) Trade inspection output for manual verification

**User feedback for future drills:**
- [:3:] trailing colon trap (same as [:3]) — add to string tasks
- 'REPTILE'[-1] + 'REPTILE'[-2::-1] reverse-slice pattern — add to string tasks
- rindex vs rfind distinction — add to string tasks
- finally/return: only drill the finally-has-return override, not basic flow
- Remove loop-closure lambda trap — already internalized

## Week 12, Day 4 — 2026-04-02

**Topic:** String slicing traps, rindex/rfind, sys/os modules, exception propagation chains, str.join/startswith/endswith, PositionManager fix + 2-strategy run
**Score:** 85% (6.83/8)

**Mentor Assessment:**

T1 — Perfect. All slice patterns correct including reverse-slice construction.

T2 — Perfect. All 4 methods (find/rfind/index/rindex) correct. rfind('b') on "abcabc" = 4 correct.

T3 — A correct. B wrong: answered for own environment instead of the given scenario (script.py foo bar) — argv[0]='script.py', argv[1]='foo', len=3. C: plausible but the number of 'os'-containing module keys in sys.modules is greater than 2 in practice (posixpath, genericpath, etc.). Partial.

T4 — Perfect. All os.path functions, remove vs rmdir, linesep correct.

T5 — A correct. B: got right answer after testing but initial reasoning had wrong order. Rule: finally runs INSIDE the function before exception propagates out → inner finally always before outer handler. C wrong: raise X from Y — outer handler catches X (ValueError), __cause__ holds Y (ZeroDivisionError). Answered both as ZeroDivisionError.

T6 — All 5 MC correct.

T7 — Perfect. join, startswith/endswith including tuple form all correct.

T8 — Two-strategy run working. PositionManager fix applied. exit_reason "still open" is a minor display bug — should_close() called after position already removed from manager. Doesn't affect PnL. Queue for tomorrow.

**For tomorrow:**
- raise X from Y + __cause__ dedicated drill
- String comparison (user request): 'aa' vs 'aaa', upper vs lower
- Harder slice patterns
- sys.argv scenario-based (not "what does YOUR script print")
- Trade exit_reason bug fix

## Week 12, Day 5 — 2026-04-03

**Topic:** String comparisons, raise X from Y, finally execution order, 20Q gap sweep, PCAP simulation
**Score:** 92% (6 tasks, T6 excluded)

**Mentor Assessment:**

T1 — Perfect. All 9 comparison results correct. Sort order and sorted() output correct.

T2 — Perfect. raise X from Y now understood. __cause__ vs __context__ distinction noted — low probability on PCAP exam, not worth drilling further.

T3 — Perfect. All 3 snippets traced correctly. B (two-function call stack) traced correctly. finally execution order fully solid.

T4 — 19/20. One error: Q12 — hasattr checks the full MRO chain, so hasattr(Child, 'method') is True even if method is only defined in Parent. This is the same pattern from Day 2. Needs one more exposure.

T5 — Perfect. All comparisons, sorted() on mixed-case list, min/max all correct.

T6 — Excluded. Approach chosen was correct (return (pos, reason) tuples). position_manager.py updated. backtest_engine.py process_price loop not updated to unpack — fix is: `for position, exit_reason in closed_positions` + remove should_close call.

T7 — All 5 PCAP sim questions correct.

**Week 12 summary:**
- D1: 88% — type(e), bare except, custom __str__, __bases__/__mro__
- D2: 90% — assert propagation, class vs instance __dict__, isinstance vs type, name mangling
- D3: 90% — strings, closures, generators, run_backtest 3-bug fix
- D4: 85% — slice traps, rindex/rfind, sys/os, exception chains, 2-strategy backtest
- D5: 92% — string comparison, raise-from, finally order, full gap sweep
- Average: 89%

Student is ready for retake. Main remaining gap: hasattr vs __dict__ membership (appears twice across sessions).

## Week 13, Day 1 — 2026-04-07

**Topic:** Custom __str__, open() modes, random module, select-two, hasattr vs __dict__
**Score:** 74% (3.7/5)

T1 partial: repr(e) is ClassName(args) regardless of __str__. e.args is populated from super().__init__() — not empty. C wrong: e.args != ().
T2 perfect.
T3 partial: random.random() < 1 is ALWAYS True — student answered False.
T4 partial: Q2 wrong — rfind returns -1 not raises (mirror of find, not index).
T5 partial: X.__dict__ is the class's own namespace, not the instance's. Correct phrasing: "defined directly in X's own namespace (not inherited)".

## Week 13, Day 2 — 2026-04-08

**Topic:** repr(e)/e.args deep drill, rfind/rindex, name mangling, assert propagation, string comparison + list comp, select-two sim, type(e)+isinstance
**Score:** 92% (6.4/7)

T1 — Perfect. All repr/args/str combinations correct across 4 variants.
T2 — Perfect. rfind/rindex locked in.
T3 — Partial. hasattr(Z, 'show') answered False — correct is True (inherited via MRO). Third consecutive session this gap appears. Must drill explicitly tomorrow.
T4 — Perfect. All 3 assert propagation variants traced correctly including "result stays 0" insight for variant 3.
T5 — Perfect. String comparisons and list comp order all correct.
T6 — Partial. Q4: lambda default args (C) is valid — student confused it with no-param lambda. Both C and D are valid Python; C is PCAP-intended answer for "can be defined without parameters" knowledge.
T7 — Perfect. type(e) vs isinstance distinction solid.

**Persistent gap: hasattr vs __dict__ — appears 3 sessions in a row. One dedicated closing drill tomorrow.**
