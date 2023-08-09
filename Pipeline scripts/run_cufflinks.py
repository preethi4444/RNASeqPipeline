import csv
import os

# with open("sortedbam_list.txt",'r') as name_file:
name = open("names.txt", "r") 
 
for fname  in name:  
    #print fname
    fname = fname.strip("\r\n")
    tname = fname + "_sorted.bam"
    str1 = "(cufflinks -p 4 -G /home/six2h/MFSSoybeanPipeline/refgenome_soybean/Glycine_max.Glycine_max_v2.1.51.gff3 /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sorted_bams/"+tname+" -o /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cufflinks_result/"+fname+") >& /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/cufflinks_result/log_cuff_"+fname+".txt &"

        
    print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)        
