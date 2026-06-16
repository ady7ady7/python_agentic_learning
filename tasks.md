# Tasks — Week 7 Day 3

---

## Part 1 — Price decay in % section cleanup (manual, in notebook)

The USD decay section is the model to follow: one chart per brand, a small number of carefully chosen lines, clean and readable. The % decay section currently has the same problem the per-generation charts had — too many lines, too much noise.

### Task 1 — Simplify the all-brands combined decay chart (cell 37)

Currently shows all base models per brand as one aggregated line each. This is actually fine — keep it. Just verify the annotations aren't overlapping and the chart breathes well.

### Task 2 — Replace the iPhone 13 submodels chart

Currently shows all submodels of iPhone 13 as separate lines — too cluttered. Replace with a simpler comparison: **iPhone 13 vs iPhone 13 Pro Max only**. These are the two most interesting endpoints of the lineup. Two lines, clean, readable. Update the observation accordingly.

### Task 3 — Simplify the tier decay charts (Apple, Samsung, Google)

Each currently shows every tier as a separate line. Apply the same logic as the USD section:

- **Apple**: keep Base and Pro Max. These are the most meaningful comparison — best retention vs most popular flagship.
- **Samsung**: keep Base, Ultra, and Edge. Ultra as the premium anchor, Edge as the cautionary tale.
- **Google**: keep Base, Pro, and Pro Fold. Same logic — useful contrast between the three positions.

Update the observations to match the simplified view.

---

## Part 2 — Pandas groupby practice (in practice.py)

Short exercises — write the code from scratch, don't look it up. Goal is to get comfortable extracting specific scalar values out of grouped data, not just viewing tables.

Use the phone dataset if you want real data, or make up a small DataFrame — your choice.

### Task 4 — idxmax / idxmin

Given a DataFrame with columns `['brand', 'tier', 'price_pct_of_launch']`, find:
- The tier with the highest average `price_pct_of_launch` per brand
- The tier with the lowest average per brand

The result should be a Series, not a full table. One line per brand, value is the tier name.

Pattern to practice: `groupby().mean().idxmax()`

### Task 5 — Extracting a scalar from a group

Given the same data:
- What is the average `price_pct_of_launch` for Samsung's Ultra tier specifically?
- Extract it as a single float, not a DataFrame or Series

Two ways to do it — try both:
1. `groupby().mean().loc[]`
2. Boolean filter then `.mean()`

### Task 6 — rank() within groups

Add a new column `retention_rank` that ranks each tier within its brand by average `price_pct_of_launch`, from highest (rank 1) to lowest. The result stays in a DataFrame — one row per brand+tier combination.

Pattern: `groupby().transform('rank', ascending=False)` — but think about whether transform is the right tool here or whether you need something else first.

---

**Total: 6 tasks (3 notebook, 3 pandas practice)**
