import math
import pandas as pd
import os
import plotly.graph_objects as go

# create two sample dataframes
df = pd.read_csv('flowerDistanceMatrix2.csv',sep = '\t')
df1 = pd.read_csv('leafDistanceMatrix2.csv',sep = '\t')
# flowerclmns = ['A1F','A2F','A3F','AD1F','AD2F','AD3F','ADLP1F','ADLP2F','ADLP3F','ALP1F','ALP2F','ALP3F','C1F','C2F','C3F','Cd1F','Cd2F','Cd3F','D1F','D2F','D3F','LP1F','LP2F','LP3F','LPD1F','LPD2F','LPD3F','S1F','S2F','S3F','SA1F','SA2F','SA3F','SAD1F','SAD2F','SAD3F','SALP1F','SALP2F','SALP3F','SD1F','SD2F','SD3F','SDLP1F','SDLP2F','SDLP3F','SLP1F','SLP2F','SLP3F','ST41F','ST42F','ST43F','ST51F','ST52F','ST53F']
# leafclmns = ['C1','C2','C3','S1','S2','S3','LP1','LP2','LP3','A1','A2','A3','D1','D2','D3','Cd1','Cd2','Cd3','SA1','SA2','SA3','SD1','SD2','SD3','SLP1','SLP2','SLP3','AD1','AD2','AD3','ALP1','ALP2','ALP3','LPD1','LPD2','LPD3','SAD1','SAD2','SAD3','SALP1','SALP2','SALP3','SDLP1','SDLP2','SDLP3','ADLP1','ADLP2','ADLP3','E4ST1','E4ST2','E4ST3','E5ST1','E5ST2','E5ST3']

flowerclmns = list(df.columns.values)
leafclmns = list(df1.columns.values)
xclmns = flowerclmns+leafclmns

flowerVal = []
leafVal = []

# for i in flowerclmns:
#     sum_col = df[i].sum()
#     print(sum_col)
#     k =sum_col
#     k = k/len(flowerclmns)
#     flowerVal.append(k)



for i in leafclmns:
    sum_col = df1[i].sum()
    print(sum_col)
    k =sum_col
    k = k/len(leafclmns)
    flowerVal.append(k)
# print(flowerVal)

euclidean_distance = []
for j in flowerVal:
	li = []
	for i in flowerVal:
		li.append(math.sqrt(math.pow(i-j,2)))
	euclidean_distance.append(li)
# print(euclidean_distance)
# for(var j = 0; j < value.length; j++){
# 		li = [];
# 		for(var i = 0; i < value.length; i++){
# 			li.push(Math.sqrt(Math.pow(value[i]-value[j],2)));
# 		}
# 		euclidean_distance.push(li);
# 	}
data = [
    go.Heatmap(
        z=euclidean_distance,
        x=leafclmns,
        y=leafclmns,
        colorscale='YlOrRd',
        colorbar=dict(
        title="Distance",
        titleside="bottom")
    )
]

layout = go.Layout(
    title="Common Genes Distance Matrix for leaf Excluding Cd",
    width=950,
    height=800,
    xaxis=dict(constrain="domain", autorange=True, tickangle=-35, automargin=True),
    yaxis=dict(scaleanchor="x", scaleratio=1, autorange=True, automargin=True)
)

fig = go.Figure(data=data, layout=layout)
fig.write_image("my_plot.png", engine="kaleido")