# Use to look for a given genomic position or a genomic range (in the same chromosome). The idea is to used the previously split files (one file per chromosomes).

# usage
# with Anaconda PowerShell Prompt
# cd C:\Users\u637660\Documents\AlphaMissense
# python queryGene.py MECP2

import sys
from queryFile import queryAlphaMissense

# define variables
gene = sys.argv[1]

# Specify path to file
file_path = 'ucsc_ncbiRefSeqSelect_hg19.txt'

# Initialize a list to store the matching lines
matching_lines = []

# Open the TSV file for reading
with open(file_path, 'r') as file:
    # get header
    header = file.readline().strip('\n')

    # define column position
    column_gene = header.split('\t').index('name2')
    column_chrom = header.split('\t').index('chrom')
    column_txStart = header.split('\t').index('txStart')
    column_txEnd = header.split('\t').index('txEnd')
    
    # Iterate through each line in the file
    for line in file:
        # Split the line into columns using the tab character as the separator
        columns = line.strip().split('\t')

        if gene == columns[column_gene]:
            # If it does, add the entire line to the matching_lines list
            matching_lines = line.strip().replace('chr','').split('\t')
            matching_lines
            result = list( matching_lines[i] for i in [column_chrom, column_txStart, column_txEnd]) #column_gene
            # [column_gene, column_chrom, column_txStart, column_txEnd]
            continue

if matching_lines == []:
    print('no results')
else:
    # Print the matching lines
    print("hg19 coordinates")
    # print(['column_gene', 'column_chrom', 'column_txStart', 'column_txEnd'])
    # print(result)

    queryAlphaMissense(result[0], result[1], result[2])
