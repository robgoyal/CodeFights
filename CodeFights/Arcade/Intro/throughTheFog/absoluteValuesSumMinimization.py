# Name: absoluteValuesSumMinimization.py
# Author: Robin Goyal
# Last-Modified: July 14, 2017
# Purpose: Return the smallest x from an array of integers which satisfies the
#          equation: abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.len -1] -x)

def absoluteValuesSumMinimization(a):
    ''' Since the array is in sorted order, it'll always be the middle value.
        If it's even, it'll be the element below the middle. '''
        
    return a[(len(a) - 1)/2]