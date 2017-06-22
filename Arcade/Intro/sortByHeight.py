# Name: sortByHeight.py
# Author: Robin Goyal
# Last-Modified: June 22, 2017
# Purpose: Sort the humans standing in a row maintaining
#          the index of the trees which is represented by -1

def sortByHeight(a):
    
    # Store the indices of the trees
    trees = [i for i, j in enumerate(a) if j == -1]
    
    # Sort row of people ignoring trees
    a.sort()
    a = a[len(trees):]

    # Insert trees from stored indices
    for i in trees:
        a.insert(i, -1)
    
    return a
