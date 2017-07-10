# Name: areSimilar.py
# Author: Robin Goyal
# Last-Modified: July 10, 2017
# Purpose: Determine if a single swap can make two lists equal
# Note: I was hung up on this question for a while and the solution 
#       is quite inefficient

def areSimilar(a, b):

    # Dictionary used to store index and values of both lists
    diffs = {}

    # Add differences to dictionary
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs[i] = [a[i], b[i]]

    # No swaps necessary
    if len(diffs) == 0:
        return True

    # Check if a single swap of 2 differences is equal
    elif len(diffs) == 2:
        values = list(diffs.values())
        return set(values[0]) == set(values[1])

    # 1 or more than 2 differences
    else:
        return False