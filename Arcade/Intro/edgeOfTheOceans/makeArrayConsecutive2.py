# Name: makeArrayConsecutive2.py
# Author: Robin Goyal
# Last-Modified: June 16, 2017
# Purpose: Return the number of additional statues needed to make 
#          a consecutive array. Example input: [6, 2, 3, 8], output: 3.
#          Since, a consecutive array would be, [2, 3, 4, 5, 6, 7, 8]. 
#          It would require 3 additional statues. 

def makeArrayConsecutive2(statues):

    # Create a consecutive list
    additional = [x for x in range(min(statues), max(statues)+1)]

    # Subtract sizes to return additional status
    return len(additional) - len(statues)