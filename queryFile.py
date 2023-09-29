def queryAlphaMissense(chr, pos1, pos2): 
    # Specify path to file
    file_path = 'chr'+ chr + '.txt'

    print(file_path)

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

            if not pos2:
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
