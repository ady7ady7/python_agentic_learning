I've named all charts with relevant names (e.g. ms charts are named ms_chart_{chart_number}, price decay charts are named pd_chart_{chart_number}) - you can audit 04_interactive_charts.ipynb for yourself.
However, I don't year treat this as a final form.

There are fundamental things that need fixing:

For almost all charts - we need to properly name x/y axes - but I wasn't sure how.

ms_chart_6 - . We must somehow resize it properly so that we can clearly see the labels of the vertical lines, as now Xmas, BF and Launch labels are blended with each other, and they're unreadable. We definitely need to make it interactive so I can select a Model from a list preferably, and that would also include Samsung and Google phones. Not sure if this is difficult to do or achievable with Seaborn/Plotly. If not, and/or very difficult, we have to figure out a different approach for that.
ms_chart_5 - we need to adjust the visible range or make more labels on monthly_sold chart. We must somehow resize it properly so that we can clearly see the labels of the vertical lines, as now Xmas, BF and Launch labels are blended with each other, and they're unreadable. This has to be VERY clear. I'd also like to have this data for Samsung/Google!
ms_chart_4 - same, this loooks clearer, but we still need to adjust the visible range a bit.
ms_chart_3 - same issue.


pd_chart_1 - probably remove iPhone 17 as it was released recently and it has weird spikes - that would also have to be labeled/described properly as a part of the process in case_study_issues. Add a similar chart for Samsung/Google and one more chart for all brands to compare them, without distinction on product grade - so a general line plot, or a different type of plot.
pd_chart_2 - looks great - I'd also like to see this interactive so I can select a model from a list preferably, and that would also include Samsung and Google models. Also needs proper labels as everywhere else.
pd_chart_7 - looks alright, but maybe we'd also have a boxplot there? Also WE MUST verify Pixel 5, as it looks a bit too strong and I'm wondering if we have relevant amount of data here. That would also have to be labeled/described properly as a part of the processin case_study_issues.
pd_chart_8 - this type of chart looks really weird for this particular data - we'd need something better than that to show a range or something like that - kde plot? boxplot? I don't know, maybe something different, but this one looks a bit weird to me.


KPI Summary - quite a few issues here:

1. While the numbers seem to be aligned in equal 2 rows, price records number is written in a smaller font, which makes it look weird.
As for the labels/titles of each KPI fig, these are really fucking weird - they interfere and blend with each other, their font size is the same, but also EVERY text and number on this KPI summary has the same color and no other space delimiters. It looks like a cluttered, unreadable chaos with some numbers and unreadable text.
My goal here would be to make it properly aesthethical, with some space delimiters, table-like structure with maybe some lines, colour distinction (with taste, not too much),
with text being properly spaced and sized, so that every label and number is clear, readable and pleasure to watch.