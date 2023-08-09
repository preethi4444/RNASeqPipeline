import csv
import os
name = open("names.txt", "r") 

for fname  in name:  
    fname = fname.strip("\r\n")
    tname = fname+".sam"
        #str1 = "(hisat2 -p 4 --dta -x "+line[2]+" -1 "+line[0]+" -2 "+line[1]+" -S sam_output/"+op_file+".sam) >& sam_output/align_"+op_file+"_log.txt &"
    str1 = "(samtools sort -@ 4 -o /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sorted_bams/"+fname+"_sorted.bam /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sam_output_edgeR/"+tname+") >& /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sorted_bams/log_sort_"+fname+" &"
        #str2 = "ln -s "+line[4]+" "+line[5]
        
    # print(str1+"\n")
        #print(str2+"\n")

    os.system (str1)
        #os.system (str2)        
