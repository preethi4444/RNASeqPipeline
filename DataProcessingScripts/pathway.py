import os
import glob
import csv
import pandas as pd
import math

# df = pd.read_csv('https://rest.kegg.jp/list/ath',sep = '\t')

df1 = pd.read_csv('https://rest.kegg.jp/link/ath/pathway',sep = '\t')
df2 = pd.read_csv('https://rest.kegg.jp/list/pathway/ath',sep = '\t')
# df1 = pd.read_csv('pathway.csv',sep = '\t')
# re = pd.DataFrame(columns=['gene','keggId','Description','PathwayId','PathwayName'])
# y =0
# df.loc[len(df.index)] = df.columns

# df.columns =['GeneId', 'Description','complement','xy']
# df[['kegg_id', 'B']] = df['xy'].str.split(';', 1, expand=True)
# for index, row in df1.iterrows():
#     if(pd.notna(row['name'])):
#         if(df['kegg_id'].str.contains(row['name']).any()):
#             print(index)
#             tt = df[df['kegg_id'].str.contains(row['name'])]
#             print(tt)
#             for ind,r in tt.iterrows():
#                 print(r['GeneId'].split(':')[1])
#                 df1.loc[index,'kegg_id'] = r['GeneId'].split(':')[1]
#                 break

# # print(df1.iloc[[0]])

# # t1 = df.merge(df1, on='GeneId', how='left')
# # t2 = t1.merge(df2, on='PathwayId', how='left')
# # tt = pd.merge(df3,t2,on='GeneId',how='outer')

# writer = pd.ExcelWriter('output.xlsx')
# # write dataframe to excel
# df1.to_excel(writer)
# # save the excel
# writer.save()
# df1.to_csv('test.csv', sep='\t', encoding='utf-8', index=False)

af = pd.read_csv('miRNA_EdgeR_CPM.csv',sep = ',')
af1 = pd.read_csv('miRNA_EdgeR.csv',sep = ',')
print(af)
t2 = af.merge(af1, on='Sample', how='left')
writer = pd.ExcelWriter('miRNA data.xlsx')
# write dataframe to excel
t2.to_excel(writer)
# save the excel
writer.save()
# df1.loc[len(df1.index)] = df1.columns
# df1.columns =['PathwayId', 'GeneId']
# df2.loc[len(df2.index)] = df2.columns
# df2.columns =['PathwayId', 'PathwayName']

# df1[['x', 'gene_id']] = df1['GeneId'].str.split(':', 1, expand=True)
# df = pd.read_csv('gene list.csv',sep = '\t')
# t2 = df.merge(df1, on='gene_id', how='left')
# t3 = t2.merge(df2, on='PathwayId', how='left')

# print(t3)
# writer = pd.ExcelWriter('kegg pathway.xlsx')
# # write dataframe to excel
# t3.to_excel(writer)
# # save the excel
# writer.save()
# t3.to_csv('test.csv', sep='\t', encoding='utf-8', index=False)


