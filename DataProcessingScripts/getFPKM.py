import csv
import os
import pandas as pd
name = open("names.txt", "r") 
re = pd.DataFrame(columns=['gene_id'])
cnt = 1
for fname  in name:  
    fname = fname.strip("\r\n")
    df = pd.read_csv("/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cufflinks_result/"+fname+"/genes.fpkm_tracking",sep='\t')
    if(cnt == 1):
        re[['gene_id',fname]] = df[['gene_id','FPKM']]
    else:
        re = re.merge(df[['gene_id','FPKM']], on=['gene_id'])
        re.rename(columns = {'FPKM':fname}, inplace = True)
        # print(re)

    cnt = cnt +1
# re[['gene_id']] = re['gene_id'].str.split(':').str[1]
re.to_csv('./FPKMResult.csv', sep='\t', encoding='utf-8', index=False)
print(re)



