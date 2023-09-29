# Use to look for a given genomic position or a genomic range (in the same chromosome). The idea is to used the previously split files (one file per chromosomes).

# usage
# with Anaconda PowerShell Prompt
# cd C:\Users\u637660\Documents\AlphaMissense
# python queryPosition.py 1 34330247
# python queryPosition.py 1 34330247 34330250
# python queryPosition.py X 153287023 153363174

import sys
from queryFile import queryAlphaMissense

# define variables
chr = sys.argv[1]
pos1 = sys.argv[2]
if len(sys.argv) > 3:
    pos2 = sys.argv[3]

queryAlphaMissense(chr, pos1, pos2)
