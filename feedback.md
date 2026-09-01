# Feedback - Current Session

<!-- Drafted by Claude - correct, add or delete anything that does not match. -->

**Date:** 2026-08-25
**Session:** ML Phase - Week 2 Day 2 (quantile regression, corrected)
**Score:** 88%
**Difficulty:** ?
**Time:** 56 min (12:35 - 13:31) - first session under the 60 min target

---

**What went well:**

- Warm-up bucket table written from memory, correctly, on the fourth attempt. Per-row
  MAE and bias, groupby with five aggregates, no notes. This was the thing I could not
  do in the weekend quiz.
- Quantile coverage finally landed where it should: q50 50.9%, q80 77.4%, q90 88.3%.
- Sliced the prediction vectors correctly this time ([-15:] instead of .mean()).
- Extended task 3 to q50 on my own initiative.
- Task 2 answer on stop placement - explained what each number is for rather than just
  picking one.

---

**What I got wrong:**

- Linear regression coverage: compared it against the quantile predictions instead of
  against y_test, so I measured how often one model sits below another rather than how
  often reality stayed under the prediction. Corrected after: 54.1%.

---

**What was unclear in the task or the explanation:**

- The coverage formula was given as bare code without breaking down what it does.
  I need the reasoning, not just the line - what each step means and why. This keeps
  coming up and it matters to me: I want to understand what I am doing and why, not
  just get output.

---

**Questions I raised during the session:**

- Why alpha=0 changes the result so much (default alpha=1.0 over-regularises and the
  model predicts almost a constant)
- Whether coverage of 1.0 for linear regression was an error (no - wrong comparison)
- Whether the model can tell in advance which quantile a day will fall into
  (no - it gives a per-day boundary, not a class; that boundary is what a stop needs)

---

**What to reinforce next:**

- Quantile regression as a finished, usable output
- Walk-forward validation - does the coverage hold over time or only on this one split

---

**Anything else:**

