# Name: arrayLeftRotation.py
# Author: Robin Goyal
# Last-Modified: October 30, 2017
# Purpose: Perform x left rotation operations on an array
#          i.e Left shifting the array x times


def arrayLeftRotation(inp, arr):

    # Reduce shift size larger than array size to single shift size
    shiftSize = inp[1] % inp[0]

    # Return shifted array
    return arr[shiftSize:] + arr[:shiftSize]