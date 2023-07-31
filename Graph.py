import pandas as pd
import plotly.express as ex
import csv 

df = pd.read_csv("Average Distance of Sports.csv")

fig = ex.bar(df, x = "Sports", y = "Distance(Km)")

fig.show()
