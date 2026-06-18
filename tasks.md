# Tasks — Week 7 Day 5

---

## Part 1 — Sales chart annotations (in notebook)

Three things to highlight across the sales section. Do these manually.

### Task 1 — Q4 sales spike

On the brand-level monthly sales chart, add a vertical shaded band or annotation marking Q4 (Oct-Dec) for each year visible in the data. Make it obvious that all three brands spike here. A light `axvspan` per Q4 window works well, or a single `ax.annotate` pointing at the clearest spike.

### Task 2 — New iPhone launch effect on predecessor sales

On the iPhone base models over time chart, the existing vertical lines already mark September launches. Add a short annotation near the most visible example (e.g. iPhone 15 launch in Sep 2024 → iPhone 14 or 13 uptick) labelling it something like "new launch drives predecessor demand". One annotation is enough — the pattern repeats visually.

### Task 3 — Weak model callouts

On the Samsung and Google tier sales charts, add a small annotation pointing to Edge (Samsung) and Pro Fold (Google) confirming their consistently low volume. One `ax.annotate` per chart, pointing at the flattest line.

---

## Part 2 — Launch prices barplot highlights

### Task 4 — Three highlights on the submodel barplot

The all-submodels barplot (cell 16 area) needs three callouts:

- **Pixel 9 Pro Max** — most expensive phone in the dataset, annotate directly on the bar
- **Flagship parity** — add a horizontal line or shaded band around the $1100-1300 range where Samsung Ultra and iPhone Pro Max cluster together, with a short label
- **Budget zone** — `axhline` at ~$500 with a label marking the Pixel 'a' series price floor

Use `ax.annotate` for the Pixel 9 Pro Max bar, `axhline` for the two zones. Keep it minimal.

---

## Part 3 — Pandas quick fix (5 min)

### Task 5 — Fix idxmax groupby order

In `practice.py`, swap `['tier', 'brand']` to `['brand', 'tier']` in the T2 groupby so the tuple output is `(brand, tier)` and `.str[1]` correctly extracts the tier name. Verify the output changes accordingly.

---

**Total: 5 tasks**
