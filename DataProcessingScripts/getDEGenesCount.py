import csv
import os
import pandas as pd

folder_path = '/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cuffdiff_result'
subfolders = []

for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isdir(item_path):
        subfolders.append(item)

for fname  in subfolders:  
#     #print fname
    fname = fname.strip("\r\n")
    print(fname)
    if(fname != 'logs_cuffdiff'):
        df = pd.read_csv("/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cuffdiff_result/"+fname+"/gene_exp.diff",sep='\t')
        cnt =0
        for index, row in df.iterrows():
            if(row['q_value'] <= 0.05):
                cnt = cnt+1
        print(cnt)
    # x = df[df['q_value']<=0.05].count()

    # print(x)
    # break
