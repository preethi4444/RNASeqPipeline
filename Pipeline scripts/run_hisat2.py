import os
import glob

name = open("names.txt", "r") 

for fname  in name:  
    #print fname
    fname = fname.strip("\r\n")


    command = "(hisat2 -p 4 --dta-cufflinks -x refgenome_soybean/Glycine_max.Glycine_max_v2.1.dna.toplevel -1 /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/Trimmed_data_03_16_2023/"+fname+"_1_val_1.fq.gz -2  /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/Trimmed_data_03_16_2023/"+fname+"_2_val_2.fq.gz -S /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sam_output_edgeR/"+fname+".sam) >& /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sam_output_edgeR/"+fname+"_hisat_log.txt &"



    print(command)
    os.system (command)
