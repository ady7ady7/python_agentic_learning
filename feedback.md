# Feedback - Current Session

<!-- Drafted by Claude from Adrian's spoken feedback - correct or add anything that is off. -->

**Date:** 2026-08-24
**Session:** ML Phase - Week 2 Day 1 (quantile regression)
**Score:** 62%
**Difficulty:** ?
**Time:** ~90 min (13:00 - 14:53, with breaks)

---

**What went wrong in how the task was written:**

- Task 1 said "use the us_range setup from Day 3". I do not remember which columns were
  dropped a week ago. Just describe what we are predicting and from what, in plain words -
  e.g. "predict the EU session range from previous sessions only, nothing from today".
  If something needs normalising, say that and explain why.

- "Vector" was used without explanation. I have gaps in maths and terms like this are not
  obvious to me. This is exactly what the learning is for - I need to understand what I am
  doing and why, not just get it working.

- Be precise and give me the chance to actually understand. Be a teacher: leave room for me
  to think and try, but do not assume I can produce something I have never been shown.

- Keep the explanations coming as we go - short asides, parentheses, whatever keeps the
  flow of understanding while I read. And keep repeating things across sessions rather
  than assuming one pass was enough.

---

**What I got wrong myself:**

- Task 2: built the comparison table without y_test in it, so I was measuring the distance
  between two predictions instead of error against reality. Fundamental mistake - I did not
  think it through, and I still do not fully have this reflex.

- Task 3: used .mean() on the predictions, which collapsed them to a single number.

---

**What worked:**

- Quantile regression as a concept makes sense - q90 as a "range will not be exceeded"
  estimate is clearly the useful one for stops. I suggested q95 for more safety, which
  feels right.

- I flagged that the coverage numbers contradicted what was promised rather than bending
  the interpretation to fit. Turned out the cause was raw prices left in the features.

---

**What to do next session:**

- Rerun quantiles with a clean feature set and see coverage land where it should
- Keep drilling the bucket/bias table - still not automatic

---

**Anything else:**

