#!/usr/bin/python3

with open('/media/src/hg19/01.Methylation/00.Bed/CGI.bed', 'r') as bed:
    with open('/media/src/hg19/01.Methylation/00.Bed/CpG.Island.bed', 'w') as note:
        for line in bed:
            line = line.strip()
            splitted = line.split('\t')
            Chromosome = splitted[0]
            Start = splitted[1]
            End = splitted[2]

            Island_Start = Start
            Island_End = End

            note.write(Chromosome + '\t' + Island_Start + '\t' + Island_End + '\t' + 'NA' + '\t' + 'CpG_Island' + '\t' + '*' + '\n')

            Shore_Start_1 = str(int(Island_Start) - 2001)
            Shore_End_1 = str(int(Island_Start) -1)

            note.write(Chromosome + '\t' + Shore_Start_1 + '\t' + Shore_End_1 + '\t' + 'NA' + '\t' + 'CpG_Shore' + '\t' + '*' + '\n')

            Shore_Start_2 = str(int(Island_End) + 1)
            Shore_End_2 = str(int(Island_End) + 2001)

            note.write(Chromosome + '\t' + Shore_Start_2 + '\t' + Shore_End_2 + '\t' + 'NA' + '\t' + 'CpG_Shore' + '\t' + '*' + '\n')

            Shelf_Start_1 = str(int(Shore_Start_1) - 2001)
            Shelf_End_1 = str(int(Shore_Start_1) -1)

            note.write(Chromosome + '\t' + Shelf_Start_1 + '\t' + Shelf_End_1 + '\t' + 'NA' + '\t' + 'CpG_Shelf' + '\t' + '*' + '\n')

            Shelf_Start_2 = str(int(Shore_End_2) + 1)
            Shelf_End_2 = str(int(Shore_End_2) + 2001)

            note.write(Chromosome + '\t' + Shelf_Start_2 + '\t' + Shelf_End_2 + '\t' + 'NA' + '\t' + 'CpG_Shelf' + '\t' + '*' + '\n')
