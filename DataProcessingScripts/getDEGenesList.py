import csv
import os
import pandas as pd


folder_path = '/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cuffdiff_result'
subfolders = []

for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isdir(item_path):
        subfolders.append(item)
re = pd.DataFrame() 
for fname  in subfolders:
    #print fname
    fname = fname.strip("\r\n")
    if(fname != 'logs_cuffdiff'):
        df = pd.read_csv("/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cuffdiff_result/"+fname+"/gene_exp.diff",sep='\t')
        cnt =0
        tt= df[df['q_value']<=0.05]['gene_id']
        print(type(tt))
        print(type(df))
        tt = tt.rename(fname)
    # tt.rename(columns = {'gene_id':fname})
    # tt.rename
    # print(len(tt))
        re = pd.concat([re, tt], axis=1) 
    # re[fname] = tt
    # for index, row in df.iterrows():
    #     if(row['q_value'] <= 0.05):
            
# x = df[df['q_value']<=0.05].count()
# x = df[df['q_value']<=0.05 and df['']].count()
re.to_csv('./Flower/DEGenesList.csv', sep='\t', encoding='utf-8', index=False)
print(re)

