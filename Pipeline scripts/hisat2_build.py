import os
import glob

command = "(hisat2-build refgenome_arabidopsisthaliana/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  Arabidopsis_thaliana.TAIR10.dna.toplevel) "



print(command)
os.system (command)