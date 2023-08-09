import os
import glob
import csv
import pandas as pd
import math

df = pd.read_csv('https://rest.kegg.jp/list/gmx',sep = '\t')

df1= pd.read_csv('https://rest.kegg.jp/link/gmx/pathway',sep = '\t')
df2 = pd.read_csv('https://rest.kegg.jp/list/pathway/gmx',sep = '\t')
df3 = pd.read_csv('anther drought genes.csv')
re = pd.DataFrame(columns=['gene','keggId','Description','PathwayId','PathwayName'])
y =0
df.loc[len(df.index)] = df.columns
df1.loc[len(df1.index)] = df1.columns
df2.loc[len(df2.index)] = df2.columns
df.columns =['GeneId', 'Description']
df1.columns =['PathwayId', 'GeneId']
df2.columns =['PathwayId', 'PathwayName']
#print(df1)

t1 = df.merge(df1, on='GeneId', how='left')
t2 = t1.merge(df2, on='PathwayId', how='left')
tt = pd.merge(df3,t2,on='GeneId',how='outer')


tt.to_csv('result.csv', sep='\t', encoding='utf-8', index=False)
