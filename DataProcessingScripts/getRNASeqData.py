import os
import glob
import csv
import pandas as pd
import math


re = pd.DataFrame(columns=['gene','p_value','q_value','significant','foldchange'])


df = pd.read_csv("/scratch/six2h/MultiFactorialSoybeanLeafRonsData/usftp21.novogene.com/cuffdiff_result/WD_vs_CT/gene_exp.diff",sep='\t')
cnt =0
for index, row in df.iterrows():
    if(row['q_value']<=0.05):
        cnt = cnt+1
        re.loc[index,'significant'] = "YES"
    else:
        re.loc[index,'significant'] = "NO"


    re.loc[index,'gene'] = row['gene_id']
    re.loc[index,'p_value'] = row['p_value']
    re.loc[index,'q_value'] = row['q_value']

    if(row['log2(fold_change)'] == math.inf or row['log2(fold_change)']== -math.inf):
        if(row['value_1'] == 0):
            c1 = math.log2((row['value_2']+1))
            re.loc[index,'foldchange'] = c1
        else:
            x = row['value_1']+1
            y = math.log2((1/x))
            re.loc[index,'foldchange'] = y
    else:
        re.loc[index,'foldchange'] = row['log2(fold_change)']


re.to_csv('./Leaf/RNAseq.csv', sep='\t', encoding='utf-8', index=False)

# print(cnt)
# print(re)