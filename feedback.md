# Feedback - Current Session

<!-- Drafted by Claude - correct, add or delete anything that does not match. -->

**Date:** 2026-09-09
**Session:** ML Phase - Week 3 Day 3 (pullback statistics: normaltest, Mann-Whitney, baselines)
**Score:** 78%
**Difficulty:** 5/10 (Adrian's rating)
**Time:** 1h 30min

---

**What went well:**

- Task 1: correctly identified from the shape (mean >> median, huge max vs 75th percentile)
  that the distribution is bounded-at-zero and right-skewed - good instinct going into the
  normality test rather than assuming.
- Task 2: correctly restated H0/H1 in plain terms before running anything, and correctly
  reasoned through what a p=0.30 result would have meant ("wouldn't trust the gap") -
  answered before seeing the actual result, as asked.
- Task 2 windows (hour 3-4 for EU, hour 10-11 for RTH) are CORRECT - they cover 3:00-5:00
  and 10:00-12:00 ET exactly as intended (the last M15 candle in each range closes at the
  5:00/12:00 boundary). I initially flagged these as off-by-one and was wrong - confirmed
  and retracted after checking the boundary logic on paper.
- Task 3: found and fixed a real bug independently once flagged - EU/RTH train/test slices
  were being cut from the wrong (unfiltered) dataframe using the filtered dataframe's
  length, which silently produced near-identical EU/RTH baselines despite the two groups
  having genuinely different medians (confirmed by the Task 2 test itself).
- Task 4: good instinct questioning the boxplot's active-hour pattern against local vs ET
  timezone rather than assuming the result was correct.

---

**What was wrong, and resolved during the session:**

- Task 1/2: used `.sample(200)` before both `normaltest` and `mannwhitneyu`, reasoning that
  large samples always reject normality and that the full dataset would show an even
  stronger (harder to trust) EU/RTH gap. Checked this empirically together:
  - Full-data Mann-Whitney: p ≈ 0.000000 (far below any threshold)
  - Same test on 5 different `.sample(200, random_state=seed)` draws: p ranged from
    0.0001 to 0.0090 - a 90x spread depending purely on which 200 points got drawn
  - Adrian's predicted *direction* (full data would show a stronger effect) was correct.
    But the point of the exercise: sample size should never be chosen to produce a
    preferred test outcome, and here there was no computational reason to subsample at
    all (Mann-Whitney on 5,278 rows runs instantly) - so subsampling only added risk
    (a weaker true effect could have landed on either side of 0.05 depending on the
    random seed) without any benefit. Fixed by rerunning on the full filtered groups.

---

**What to reinforce next:**

- When to subsample (data too large to process, or deliberately simulating a smaller
  study) vs when there's no reason to (small enough dataset, no compute cost) - test
  results should never be shaped by tuning sample size toward an expected outcome
- Consistent filtering when building train/test slices from a subset (Task 3's bug: cutting
  the full dataframe by a filtered dataframe's length)

---

**Anything else:**


---

**Update after resubmission:**

Sampling removed from both `normaltest` and `mannwhitneyu` as discussed. Verified the
corrected code independently: same Mann-Whitney U statistic (81286.5) as when I ran it,
p ≈ 2.56e-08 - confirms the fix is correct. Only remaining nitpick: the printed comment
next to the code still shows the old sampled result (p=0.0056) rather than the new one -
cosmetic, not a logic error, worth updating for a clean record.
