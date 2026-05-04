# AlgoBacktest Core - Project Roadmap

**Goal:** Build a professional backtesting engine for scenario-based trading strategies using Python, Pandas, and NumPy.

**Stack:** Python 3.10+, Pandas, NumPy, OOP Architecture

---

## Phase 1: Foundations & Data (Weeks 1-3) ✅ COMPLETE

### Week 1: Project Setup ✅
- [x] Create package structure (`algo_backtest/`, `data/`, `engine/`, `strategies/`)
- [x] Setup `requirements.txt` (Pandas, NumPy)
- [x] Create `main.py` entry point
- [x] Version tracking in `__init__.py`

### Week 2: OOP Foundations ✅
- [x] Inheritance & Polymorphism (BaseStrategy ABC)
- [x] LevelCrossStrategy & MovingAverageStrategy
- [x] @classmethod for position sizing
- [x] `Position` class with SL/TP, PnL calculation, `should_close()`
- [x] `calculate_position_size` classmethod

### Week 3: Encapsulation & Properties ✅
- [x] `Trade` class with encapsulated PnL (using @property)
- [x] Protected/private attributes (`_protected`, `__private`)
- [x] Property decorators for controlled access
- [x] `TradeManager` class with dunder methods
- [x] Portfolio class

---

## Phase 2: The Engine (Weeks 4-6)

### Week 4: Functional Programming ✅ COMPLETE
- [x] Lambda functions & closures
- [x] map(), filter(), reduce()
- [x] Decorators with/without arguments
- [x] Signal generator with functional patterns

### Week 5: BacktestEngine & File I/O ✅ COMPLETE
- [x] `BacktestEngine` class (orchestrates Position → Trade lifecycle)
- [x] `open_position()` and `process_price()` methods
- [x] Properties: `total_pnl`, `win_rate`
- [x] `__str__` method for summary display
- [x] datetime & File I/O practice (strftime, strptime, timedelta)
- [x] Decorator fundamentals (simple, with args, stacking)

### Week 6: Position Identity & Iterator Patterns (CURRENT)
- [x] Unique `position_id` (uuid4) on every Position
- [x] Ticker-aware price processing (PositionManager + BacktestEngine)
- [x] Position ID propagation: Position → Trade (full lifecycle chain)
- [x] Fixed PositionManager removal bug (ID-based filtering)
- [x] Custom iterators with `__iter__`/`__next__` (FibonacciIterator, CountdownIterator)
- [x] Convert DataFrame rows to generator (yield row as namedtuple)
- [x] `create_price_stream()` generator function
- [x] Implement tick-by-tick simulation via generator pipeline
- [x] Parameterized decorator `@repeat(n)` (decorator factory pattern)
- [x] `sma_indicator()` generator consuming price stream (generator chaining)
- [x] Filtered price stream with `filter_func` predicate parameter

---

## Phase 3: Polish & Documentation (Weeks 7-8)

### Week 7: Logging & Standard Library ✅ COMPLETE
- [x] Add Python `logging` module
- [x] Log: Trade opened, SL hit, TP hit, Trade closed
- [x] setup_logging() in main.py — configures root logger
- [x] module-level logger = logging.getLogger(__name__) in BacktestEngine

### Week 8: Finalization (CURRENT)
- [x] Add docstrings to all core engine classes (BacktestEngine, Position, Trade done)
- [x] Run complete end-to-end backtest (main.py — 4 positions, 2 tickers, logging active)

**Extended Goals (Days 3-5):**
- [ ] R-multiple calculation on Trade: `R = pnl / (abs(entry - stop_loss) * quantity)`
- [ ] Profit factor and Sharpe ratio on BacktestEngine
- [ ] Strategy-aware Position: `strategy_id: str`, `strategy_name: str` attributes
- [ ] Per-strategy reporting: group completed_trades by strategy_id, report R, win rate, profit factor per strategy and combined

---

## Strategies Implemented

1. **LevelCrossStrategy** ✅ - Enter when price crosses level
2. **MovingAverageStrategy** ✅ - Enter on MA crossover signals

---

**Current Status:** Week 8, Day 2 - Tuesday
**Last Updated:** 2026-02-24
