# python script to split alpha missense file. The idea is to be used on hospital computer without prior installation. Python can be used through anaconda distribution for example.
# file can be accessed here : https://console.cloud.google.com/storage/browser/dm_alphamissense;tab=objects?pli=1&prefix=&forceOnObjectsSortingFiltering=false
# https://console.cloud.google.com/storage/browser/_details/dm_alphamissense/AlphaMissense_hg19.tsv.gz

# usage
# with Anaconda PowerShell Prompt (in my case)
# cd C:\Users\u637660\Documents\AlphaMissense
# python splitFile.py

# Define the input and output file paths
input_file = 'AlphaMissense_hg19.tsv'
output_files = {}  # Dictionary to store output file objects

# Read the input file and process lines
with open(input_file, 'r') as f:
    for line in f:

        # Split the line into columns based on the tab delimiter
        columns = line.strip().split('\t')

        # Extract the value from column 1
        value_in_column_1 = columns[0]

        # Check if the line is a comment
        if line.startswith('#'):
            value_in_column_1 = 'header'

        # Check if an output file already exists for this value
        if value_in_column_1 not in output_files:
            # Create a new output file
            output_files[value_in_column_1] = open(f'{value_in_column_1}.txt', 'w')
            output_files[value_in_column_1].write('CHROM	POS	REF	ALT	genome	uniprot_id	transcript_id	protein_variant	am_pathogenicity	am_class\r')

        # Write the line to the corresponding output file
        output_files[value_in_column_1].write(line)

# Close all output files
for file in output_files.values():
    file.close()
