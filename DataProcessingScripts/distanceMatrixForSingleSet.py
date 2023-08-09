import math
import pandas as pd
import os
import plotly.graph_objects as go
import numpy as np
# create two sample dataframes
df = pd.read_csv('FlowerDistanceMatrixInput1.csv',sep = '\t')

flowerclmns = list(df.columns.values)

flowerVal = []

for i in flowerclmns:
    sum_col = df[i].sum()
    print(sum_col)
    k =sum_col
    k = k/len(flowerclmns)
    flowerVal.append(k)

euclidean_distance = []
for j in flowerVal:
	li = []
	for i in flowerVal:
		li.append(np.linalg.norm(i - j))
		# li.append(math.sqrt(math.pow(i-j,2)))
	euclidean_distance.append(li)
	
data = [
    go.Heatmap(
        z=euclidean_distance,
        x=flowerclmns,
        y=flowerclmns,
        colorscale='YlOrRd',
        colorbar=dict(
        title="Distance",
        titleside="bottom")
    )
]

layout = go.Layout(
    title="Distance Matrix for Top 100 Genes of Leaf",
    width=950,
    height=800,
    xaxis=dict(constrain="domain", autorange=True, tickangle=-35, automargin=True),
    yaxis=dict(scaleanchor="x", scaleratio=1, autorange=True, automargin=True)
)

fig = go.Figure(data=data, layout=layout)
fig.write_image("flower1.png", engine="kaleido")