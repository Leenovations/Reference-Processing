#!/usr/bin/python3

import pandas as pd

with open('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.hg19.bed' , 'r') as ref:
    with open('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Exon.Intron.numbering.bed', 'w') as note:
        for line in ref:
            line = line.strip()
            splitted = line.split('\t')
            Chromosome = splitted[0]
            Strand = splitted[1]
            TxStart = splitted[2].split(',')
            TxStart.pop(-1)
            TxEnd = splitted[3].split(',')
            TxEnd.pop(-1)
            GeneSymbol = splitted[4]
            if Strand =='+':
                for num in range(len(TxStart)):
                    if len(TxStart) - num != 1:
                        note.write(Chromosome + '\t' + TxStart[num] + '\t' + TxEnd[num] + '\t' + GeneSymbol + '\t' + 'Exon' + f'_{str(num)}' + '\t' + Strand + '\n')
                        note.write(Chromosome + '\t' + str(int(TxEnd[num]) + 1) + '\t' + str(int(TxStart[num+1]) - 1) + '\t' + GeneSymbol + '\t' + 'Intron' + f'_{str(num)}' + '\t' + Strand + '\n')
                    elif len(TxStart) - num == 1:
                        note.write(Chromosome + '\t' + TxStart[num] + '\t' + TxEnd[num] + '\t' + GeneSymbol + '\t' + 'Exon' + f'_{str(num)}' + '\t' + Strand + '\n')

            elif Strand =='-':
                for num in range(len(TxStart)):
                    number = list(range(len(TxStart)))[::-1][num]
                    if len(TxStart) - number == 1:
                        note.write(Chromosome + '\t' + TxStart[num] + '\t' + TxEnd[num] + '\t' + GeneSymbol + '\t' + 'Exon' + f'_{str(number)}' + '\t' + Strand + '\n')
                    elif len(TxStart) - number != 1:
                        note.write(Chromosome + '\t' + str(int(TxEnd[num -1]) + 1) + '\t' + str(int(TxStart[num]) - 1) + '\t' + GeneSymbol + '\t' + 'Intron' + f'_{str(number)}' + '\t' + Strand + '\n')
                        note.write(Chromosome + '\t' + TxStart[num] + '\t' + TxEnd[num] + '\t' + GeneSymbol + '\t' + 'Exon' + f'_{str(number)}' + '\t' + Strand + '\n')

promoter = pd.read_csv('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Exon.Intron.numbering.bed',
                       sep='\t',
                       header=None)

promoter = promoter.sort_values(by=[0 ,1, 2])
promoter.to_csv('/media/src/hg19/01.Methylation/00.Bed/NCBI.RefSeq.Selected.Exon.Intron.numbering.bed',
                sep='\t',
                header=None,
                index=False)
