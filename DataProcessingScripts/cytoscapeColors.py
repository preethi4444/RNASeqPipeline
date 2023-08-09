import os
import glob
import csv
import pandas as pd

import math
df = pd.read_csv("flowerfivestressgenie3input.csv",sep='\t') 
df1 = pd.read_csv("TFlist_soybean.csv",sep='\t') 
df2 = pd.read_csv("FlowerFiveStressFoldchange.csv",sep='\t') 
 
re = pd.DataFrame(columns=['targetGene','Segregate'])
cnt =0
for index, row in df.iterrows():
    i=row['targetGene']
    re.loc[index,'targetGene'] =i
#     if(df2['Gene_ID'].str.contains(i).any() and i == '' or ''){
#         >o and <0
#  =2 and 3
#     }
#     else{
#          = 1
#     }
#     if()
    if(df1['Gene_ID'].str.contains(i).any() and df2['Gene_ID'].str.contains(i).any()):
        cnt = cnt+1
        tt2 = df2[df2['Gene_ID'].str.contains(i)]
        for ind2,r2 in tt2.iterrows():
            val1 = r2['foldChange']
            if(val1>0):
                re.loc[index,'Segregate'] =4
            else:
                re.loc[index,'Segregate'] =5
    elif(df1['Gene_ID'].str.contains(i).any()):
        re.loc[index,'Segregate'] =1
        # tt = df1[df1['Gene_ID'].str.contains(i)]
        # for ind,r in tt.iterrows():
        #     df.loc[index,'TFFamilyName'] = r['Family']
    elif(df2['Gene_ID'].str.contains(i).any()):
        tt1 = df2[df2['Gene_ID'].str.contains(i)]
        for ind1,r1 in tt1.iterrows():
            val = r1['foldChange']
            if(val>0):
                re.loc[index,'Segregate'] =2
            else:
                re.loc[index,'Segregate'] =3
    else:
        re.loc[index,'Segregate'] =6
print(cnt)


print(re)
re.to_csv('Flower Colors.csv', sep='\t', encoding='utf-8', index=False)


