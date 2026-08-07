# Tasks — Week 11 Day 1

---

## Task 1 — Feature engineering

- [ ] Add `gap_to_range_ratio = abs(gap_size) / london_range`
- [ ] Add lag features: `prev_day_bullish`, `prev_day_range`, `prev_london_bullish`
- [ ] Add rolling volatility: 5-day rolling mean of daily_range
- [ ] Final feature matrix — drop NaNs, check shape

## Task 2 — Train/test split

- [ ] Time-based split (not random) — last 20% of dates as test
- [ ] Document why time-based split matters for financial data

---

**Total: 2 tasks**
