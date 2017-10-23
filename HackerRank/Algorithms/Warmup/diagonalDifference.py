# Name: diagonalDifference.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Return the absolute difference between the primary
#          diagonal and secondary diagonal

def diagonalDifference(arr):

    # Calculate primary and secondary diagonals using iterators
    prim_diag = sum(arr[i][i] for i in range(len(a)))
    sec_diag = sum(arr[i][n-i-1] for i in range(len(a)))

    # Return the absolute difference
    return abs(prim_diag - sec_diag)