import os
import glob

# name = open("soybeanNames.txt", "r") 

name = open("names.txt", "r") 

for fname  in name:  
    #print fname
    fname = fname.strip("\r\n")

    command = "(trim_galore --output_dir /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/Trimmed_data_03_16_2023 --paired /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/01.RawData/"+fname+"/"+fname+"_1.fq.gz /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/01.RawData/"+fname+"/"+fname+"_2.fq.gz) >& /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/log_trim/log_"+fname+"_trim.txt &"

    print(command)
    os.system (command)
