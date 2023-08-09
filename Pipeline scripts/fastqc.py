import os


name = open("names.txt", "r") 

for fname  in name:  
    #print fname
    fname = fname.strip("\r\n")
    command1 = "(fastqc -o /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/FastqcResult /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/01.RawData/"+fname+"/"+fname+"_1.fq.gz)"
    command2 = "(fastqc -o /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/FastqcResult /scratch/six2h/MultiFactorialSoybeanFlowerRonsData/usftp21.novogene.com/01.RawData/"+fname+"/"+fname+"_2.fq.gz)"
    # print(command1)
    print(command2)
    os.system (command1)
    os.system (command2)

