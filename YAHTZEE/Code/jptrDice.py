# %%
import pandas as pd
import numpy as np
import altair as alt
import csv
import datadotworld as dw
# %%
df = pd.read_csv('sortedDice.csv')

print (df)

# %%
ghRoll = pd.DataFrame(df, columns = ["dice1", "dice2", "dice3", "dice4", "dice5", "ID"])

ghRoll["count"] = 1
ghRoll = ghRoll.groupby(["dice1", "dice2", "dice3", "dice4", "dice5", "ID"])["count"].count().reset_index()

print(ghRoll.sort_values("count", ascending=False).reset_index().head(10).to_markdown())
print()

print(ghRoll.sort_values("count", ascending=False).reset_index())

print()

print(ghRoll["count"].mean())

ghRoll = ghRoll.sort_values("count", ascending=False).reset_index().head(10)

ghRoll

# %%
top_rolls = alt.Chart(ghRoll).mark_bar(size = 15).encode(
    x= alt.X("ID:N", sort = "-y"),
    y = "count",
    color = alt.value("darkseagreen")
)

top_rolls
# %%
