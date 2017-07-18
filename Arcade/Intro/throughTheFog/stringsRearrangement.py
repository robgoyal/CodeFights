# Name: stringsRearrangement.py
# Author: Robin Goyal
# Last-Modified: July 18, 2017
# Purpose: Check to see if a rearrangement of a list of strings is possible
#          where each consecutive position would differ by exactly one character
# Note: This is a brute force solution which took me far too long to figure out

import itertools    

def stringsRearrangement(arr):
    
    # Generate a list of permutations based off of the length of the input array
    perms = itertools.permutations(range(len(arr)))

    # Iterate through each permutation and determine if the permutation
    # can satisy the order of strings
    for i in perms:
        flag = True
        for j in range(len(i) - 1):

            # Set flag to False if a pair of consecutive elements in the
            # permutation does not satisfy the similarity condition
            if not(similar(arr[i[j]], arr[i[j+1]])):
                flag = False
                break
        
        # If flag is still True, then the permutation satisfied the goal
        if flag:
            return True

    # Permutations were exhausted 
    return False


def similar(input1, input2):
    ''' Count the number of differences between two strings.
        True if number of differences is equal to 1.
        False if not. '''
        
    diffs = 0
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            diffs += 1

    return (diffs == 1)

stringsRearrangement(["aba", "bbb", "bab"])