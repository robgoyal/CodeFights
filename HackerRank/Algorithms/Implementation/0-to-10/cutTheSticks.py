# Name: cutTheSticks.py
# Author: Robin Goyal
# Last-Modified: October 24, 2017
# Purpose: Determine the number of sticks cut with the cut length
#          being the minimum height of the sticks

def cutTheSticks(size, arr):
    while len(arr) > 0:

        # Print number of elements in arr
        print(len(arr))
        cut = min(arr)

        # Cut the sticks which aren't the minimum cut length
        # Remove the ones that are the minimum cut length
        arr = [x - cut for x in arr if x != cut]

cutTheSticks(4, [1, 3, 4, 1])