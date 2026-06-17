# Tasks — Week 7 Day 4

---

## Part 1 — Pandas practice (finish from yesterday, in practice.py)

### Task 1 — tier extraction (forgotten lambda)

Yesterday you used `submodel_name` instead of `tier` because you forgot the lambda. The pattern:

```python
df['tier'] = df.apply(lambda row: row['submodel_name'].replace(row['generation_name'], '').strip(), axis=1)
df['tier'] = df['tier'].replace('', 'Base')
```

Add this to the practice setup, then redo T4 and T6 using `tier` instead of `submodel_name`.

### Task 2 — idxmax / idxmin (fix the multi-level issue)

Your attempt returned a single global result, not one per brand. The correct pattern for one result per brand:

```python
df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().groupby('brand').idxmax()
```

This chains two groupbys — the inner aggregates to brand+tier, the outer picks the best tier per brand. The result is a Series of `(brand, tier)` tuples. Chain `.str[1]` to get just the tier name.

### Task 3 — rank() on aggregated data (fix)

`transform('rank')` ranks individual rows within a group, not per-tier averages. Your output had one rank per row, not one per tier. The correct approach: aggregate first, then rank:

```python
tier_avg = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().reset_index()
tier_avg['retention_rank'] = tier_avg.groupby('brand')['price_pct_of_launch'].rank(ascending=False)
```

---

## Part 2 — Notebook review (tasks 4-5 from Day 3, not reached)

### Task 4 — All-brands 1-year retention barplot

Per-brand retention barplots already exist earlier in the notebook. Does the all-brands version add something on top, or is it now redundant? Make a call and either keep it with a clear reason or remove it.

### Task 5 — Remaining sections review

- Boxplot: observation still accurate?
- Sales pipeline markdown: still accurate after grade filter removal?
- Key findings: anything outdated or missing given all the changes this week?

---

**Total: 5 tasks (3 pandas, 2 notebook)**
