#!/usr/bin/python3
import pandas as pd

with open('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Promoter', 'r') as bed:
    with open('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Promoter.bed', 'w') as note:
        for line in bed:
            line = line.strip()
            splitted = line.split('\t')
            Chromosome = splitted[0]
            Strand = splitted[1]
            Start = splitted[2]
            End = splitted[3]
            GeneSymbol = splitted[4]

            if Strand == '+':
                Promoter_Start = str(int(Start) - 2001)
                Promoter_End = str(int(Start) - 1)
            elif Strand == '-':
                Promoter_Start = str(int(End) + 1)
                Promoter_End = str(int(End) + 2001)
            
            note.write(Chromosome + '\t' + 
                       Promoter_Start + '\t' + 
                       Promoter_End + '\t' + 
                       GeneSymbol + '\t' + 
                       'Promoter' + '\t' +
                       Strand + '\n')
            

promoter = pd.read_csv('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Promoter.bed',
                       sep='\t',
                       header=None)

promoter = promoter.sort_values(by=[0 ,1, 2])
promoter.to_csv('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Promoter.bed',
                sep='\t',
                header=None,
                index=False)
