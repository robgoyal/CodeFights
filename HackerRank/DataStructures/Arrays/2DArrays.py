# Name: 2DArrays.py
# Author: Robin Goyal
# Last-Modified: October 29, 2017
# Purpose: Return the maximum sum of hourglasses in 6x6 array

def main():
    arr = []

    # Read input for 6 rows of matrix
    for arr_i in xrange(6):
        arr_temp = list(map(int, raw_input().strip().split(' ')))
        arr.append(arr_temp)

    # Calculate max hourglass in matrix
    maxHourglass(arr)

def maxHourglass(arr):

    # Initialize hourglass array
    hourglasses = []
    for x in range(4):
        for y in range(4):

            # Calculate hourglass sum
            hourglassSum = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            hourglasses.append(hourglassSum)

    return max(hourglasses)