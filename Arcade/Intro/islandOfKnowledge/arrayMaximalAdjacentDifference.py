# Name: arrayMaximalAdjacentDifference.py
# Author: Robin Goyal
# Last-Modified: July 10, 2017
# Purpose: Find the maximal difference between adjacent elements

def arrayMaximalAdjacentDifference(inputArray):

    maxAdj = 0

    for i in range(len(inputArray) - 1):

        # Hold difference between adjacent elements
        temp = abs(inputArray[i+1] - inputArray[i])

        # Replace maxAdj with new max
        if temp > maxAdj:
            maxAdj = temp

    return maxAdj