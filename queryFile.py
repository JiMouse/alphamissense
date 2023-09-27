# to look for a given variation. The idea is to used the previously split files (one file per chromosomes)

# usage
# with Anaconda PowerShell Prompt
# cd C:\Users\u637660\Documents\AlphaMissense
# python queryFile.py chr pos
# python queryFile.py 1 34330247

import sys

# Define the string you want to search for in column 1
# chr = '1'
# pos = '34330247' #POS

# or using sys
chr = sys.argv[1]
pos = sys.argv[2]

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

        # Check if the second column contains the search string : exact match == | partial match in 
        if pos == columns[1]:
            # If it does, add the entire line to the matching_lines list
            matching_lines.append(line.strip())

if matching_lines == []:
    print('no results')
else:
    # Print the matching lines
    print(first_line) #header
    for matching_line in matching_lines:
        print(matching_line)
