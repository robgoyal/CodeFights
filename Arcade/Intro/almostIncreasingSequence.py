# Name: almostIncreasingSequence.py
# Author: Robin Goyal
# Last-Modified: June 20, 2017
# Purpose: Determine if removing a single element
#          can create a sorted array

def almostIncreasingSequence(arr):

    for i in range(len(arr) - 1):

        # Check if removing the current element or the next element
        # will return a sorted array
        if arr[i+1] <= arr[i]:
            if not((sorted(arr[0:i] + arr[i+1:])) or \
                   (sorted(arr[0:i+1] + arr[i+2:]))):
            return False
    return True

# Check if array is sorted
def sorted(arr):
    return all(arr[i] < arr[i+1] for i in xrange(len(arr) - 1))