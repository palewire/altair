"""
Iowa's renewable energy boom
----------------------------
This example is a fully developed stacked chart using the sample dataset of Iowa's electricity sources.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(
    source,
    title=alt.Title("Iowa's green energy boom", subtitle="A growing share of the state's energy has come from renewable sources")
).mark_area().encode(
    x=alt.X(
        "year:T",
        title="Year"
    ),
    y=alt.Y(
        "net_generation:Q",
        stack="normalize",
        title="Share of net generation",
        axis=alt.Axis(format=".0%"),
    ),
    color=alt.Color(
        "source:N",
        legend=alt.Legend(title="Electricity source"),
    )
)
