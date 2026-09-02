# Feedback - Current Session

<!-- Drafted by Claude - correct, add or delete anything that does not match. -->

**Date:** 2026-08-26
**Session:** ML Phase - Week 2 Day 3 (walk-forward validation)
**Score:** 88%
**Difficulty:** ?
**Time:** 80 min (13:08 - 14:28)

---

**What went well:**

- Warm-up coverage lines written from memory instantly, no hesitation.
- Walk-forward loop understood and implemented correctly on the first attempt - the
  slicing (train window ending at start, test window beginning at start) made sense, BUT quite honestly I had to look up the code from the concept, as it's definitely difficult at this point. I know the slicing rules for Python, but getting this done in this context and not mixing things up is difficult - definitely needs reinforcing, trying, repetitions.
- Task 2 written as a loop over the quantile list with f-string naming, instead of three
  copy-pasted blocks like the previous sessions. Noted it as "interesting task to practice
  Python a bit".
- Chose 300/300 windows over the suggested 600/125 and gave a reason: shorter training
  window means learning from data closer to the period being predicted, which matters when
  the market regime shifts.
- Pushed back on the "target" column in Task 2 as redundant - the model names already carry
  that information. Correct, the instruction was unnecessary.

---

**Results:**

```
model     mean     min      max
q50      0.487    0.480    0.497
q80      0.797    0.767    0.827
q90      0.904    0.870    0.923
linreg   0.634    0.620    0.660
```

All three quantile models held their targets across every fold. Yesterday's 88.3% from a
single split turned out to be real, not luck.

---

**What I got wrong:**

- `test_start` recorded `train.index.min()` instead of `test.index.min()`, so the column
  showed where training began rather than where testing began - and the Task 3 chart had
  its time axis shifted by 300 days. Fixed.
- Task 3 asked me to check `us_range` per year in the data rather than guess about market
  conditions. I answered from the chart alone and skipped the data check, as I wasn't sure how to do that check quite honestly.

---

**Open point:**

- Three folds is a small sample for judging stability. 300/125 would have given nine folds
  from the same data - shorter test blocks mean more measurements. Worth considering next
  time the question is "is this model reliable" rather than "how good is it".

---

**What to reinforce next:**


---

**Anything else:**

