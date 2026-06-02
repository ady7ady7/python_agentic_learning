# Tasks — Week 5 Day 2

## Annotation practice on 2 charts

Goal: learn matplotlib annotations by applying them to real charts.
Each task has a specific analytical point to highlight — not decorative, story-driven.

---

### Task 1 — Annotate the all-brands decay chart (Cell 9) [5 pts]

Add the following to the existing all-brands lineplot:

1. Shaded band for the "first year" window:
```python
plt.axvspan(0, 365, alpha=0.07, color='blue', label='First year')
```

2. Annotate where Samsung crosses the 50% line (~500 days):
```python
plt.annotate(
    'Samsung crosses 50%\nat ~500 days',
    xy=(500, 50),
    xytext=(600, 60),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=9, color='gray'
)
```

3. Annotate where Apple crosses 50% (~900 days):
```python
plt.annotate(
    'Apple crosses 50%\nat ~900 days',
    xy=(900, 50),
    xytext=(1000, 60),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=9, color='gray'
)
```

4. Adjust `xy` and `xytext` values by looking at the actual chart —
   the numbers above are approximate. Move the text boxes so they
   don't overlap the lines.

Does the annotation make the chart tell a clearer story?
Add 1 sentence in the markdown cell below about what the shaded band highlights.


fig, ax = plt.subplots(figsize=(12, 6))
pd_chart_1d = sns.lineplot(data=all_brands_decay_df, x='days_rounded', y='price_pct_of_launch',
    hue='brand', ax=ax)
ax.axhline(50, color='red', linestyle='dotted', linewidth=2)
ax.set_title('Price decay — all base models by brand')
ax.set_xlabel('Days since launch')
ax.set_ylabel('Price as % of launch price')
plt.tight_layout()

#annotations
plt.axvspan(0, 365, alpha = 0.33, color = 'lightblue', label = 'First year')
plt.annotate(
    'Samsung crosses 50%\n at 500~ days',
    xy=(530, 50),
    xytext=(850, 70),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=9, color='gray'
)
plt.annotate(
    'Apple crosses 50%\nat 900~ days',
    xy=(920, 50),
    xytext=(1200, 70),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=9, color='gray'
)
plt.annotate(
    'Google crosses 50%\nat 420~ days',
    xy=(420, 50),
    xytext=(650, 80),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=9, color='gray'
)
plt.show()


1. Definitely, it does make it a lot more clear.
2. The light blue shaded area highlights the first year after launch.

I'm also wondering if we could highlight one line or another by making it wider or maybe also putting down the alpha of the other lines by a bit, wdyt?
And whether we could circle one area to mark it with a red circle or something like that.



---

### Task 2 — Annotate the 1-year retention barplot (Cell 22) [5 pts]

The Pixel 5 anomaly is the most interesting finding in this chart.
Highlight it with an annotation:

1. First find the x-position of Pixel 5 in the barplot.
   The bars are ordered by retention value descending — check
   `retention_1yr_df['generation_name'].tolist()` to find the index.

2. Add annotation:
```python
plt.annotate(
    'Pixel 5: discontinued early,\ncreating supply scarcity',
    xy=(pixel5_x, pixel5_y),       # tip of arrow — on the bar
    xytext=(pixel5_x + 2, pixel5_y + 8),  # text position
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=9
)
```

3. Add a horizontal reference line for Apple's average retention:
```python
plt.axhline(apple_retention, color='steelblue', linestyle='--',
    linewidth=1, alpha=0.6, label=f'Apple avg: {round(apple_retention, 1)}%')
plt.legend()
```

4. Getting the exact xy coordinates: run the chart once first,
   visually estimate the bar position, then adjust.



plt.annotate(
    text = 'Pixel 5: discontinued early,\ncreating supply scarcity',
    xy=(0, 92),
    xytext=(1, 87), color = 'gray',
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=9
)

plt.show()



As for Apple's average retention, that's an overkill and it doesn't look good, as I've tested it, and I don't want it.





---

**Total: 10 pts**
