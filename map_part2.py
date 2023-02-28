
"""map.py"""

import sys
import os
#file_name = os.path.basename(os.getenv('map_input_file'))

#print (file_name)
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    file_name1 = os.getenv('map_input_file')
    file_name = os.path.basename(file_name1)    
    line = line.strip()
    # split the line into words
    words = line.split()
    circle=words[0]   
 # increase counters
    count=0
    for word in words:
        count=count+1
        #file_name = os.path.basename(os.getenv('map_input_file'))    
        #line = line.strip()            
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print (file_name+","+","+words+","+circle+"\t"+ str(count))