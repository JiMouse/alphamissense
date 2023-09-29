# Use to look for a given genomic position or a genomic range (in the same chromosome). The idea is to used the previously split files (one file per chromosomes).

# usage
# with Anaconda PowerShell Prompt
# cd C:\Users\u637660\Documents\AlphaMissense
# python queryFile.py 1 34330247
# python queryFile.py 1 34330247 34330250

import sys

# define variables
chr = sys.argv[1]
pos1 = sys.argv[2]
if len(sys.argv) > 3:
    pos2 = sys.argv[3]

# Specify path to file
file_path = 'chr'+ chr + '.txt'

# Initialize a list to store the matching lines
matching_lines = []

# Open the TSV file for reading
with open(file_path, 'r') as file:
    # get header
    first_line = file.readline().strip('\n')

    # Iterate through each line in the file
    for line in file:
        # Split the line into columns using the tab character as the separator
        columns = line.strip().split('\t')

        if len(sys.argv) == 3:
            # Check if the second column contains the search string : exact match == | partial match in 
            if pos1 == columns[1]:
                # If it does, add the entire line to the matching_lines list
                matching_lines.append(line.strip())
        else:
            if columns[1] >= pos1 and columns[1] <= pos2:
                matching_lines.append(line.strip())

if matching_lines == []:
    print('no results')
else:
    # Print the matching lines
    print("hg19 coordinates")
    print(first_line) #header
    for matching_line in matching_lines:
        print(matching_line)
