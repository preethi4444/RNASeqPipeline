import math
import pandas as pd
import os
import plotly.graph_objects as go

# create two sample dataframes
df = pd.read_csv('GLYMA_flower.csv',sep = '\t')
df1 = pd.read_csv('flower_top100.csv',sep = '\t')
df2 = pd.read_csv('flowerfoldchangeval.csv',sep = '\t')

clms = list(df1.columns.values)
re = pd.DataFrame(columns=clms)
for i in clms:
    x=df1[i].values
    y=df[i].values
    column_data = []  # Create an empty list to store boolean values for the column
    for gene in x:
        if gene in y:
            value = df2.loc[df2['gene_id'] == gene, i].iloc[0]
            # print(f"Gene: {gene}, Column: {i}, Value: {value}")
            # print(value)
            # break
            column_data.append(value)  # Append True if there is a match
        else:
            column_data.append(0)  # Append False if there is no match
    re[i] = column_data  
    
print(re)
re.to_csv('FlowerDistanceMatrixInput1.csv', sep='\t', encoding='utf-8', index=False)
