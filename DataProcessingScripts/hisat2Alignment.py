import csv
import os
name = open("names.txt", "r") 
output = open("hisat2AlignmentRatesForFlower.txt","w")
for fname  in name:  
    fname = fname.strip("\r\n")
    with open('/scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/sam_output_edgeR/'+fname+'_hisat_log.txt', 'r') as f:
        last_line = f.readlines()[-1]
        print(last_line)
        output.write(fname)
        output.write("\r\n")
        output.write(last_line)
        output.write("\r\n")
    
