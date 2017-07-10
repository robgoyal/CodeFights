# Name: arrayChange.py
# Author: Robin Goyal
# Last-Modified: July 10, 2017
# Purpose: Calculate number of moves to create an increasing
#          array sequence

def arrayChange(inputArray):

    moves = 0

    for i in range(len(inputArray) - 1):
        if inputArray[i+1] <- inputArray[i]:

            # Calculate difference required to make current value
            # one greater than previous value
            difference = abs(inputArray[i] - inputArray[i+1] +1)

            # Increment current value and number of moves
            moves += temp
            inputArray[i+1] += temp

    return moves