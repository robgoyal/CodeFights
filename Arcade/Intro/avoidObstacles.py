# Name: avoidObstacles.py
# Author: Robin Goyal
# Last-Modified: July 11, 2017
# Purpose: Determine the minimum length needed to avoid all the obstacles
#          in the array

def avoidObstacles(inputArray):

    jumpLen = 1
    while(True):

        # Check if the jump value is divisible by any elements in array
        # If divisible, it means it cannot avoid obstacle
        if all(x % jumpLen != 0 for x in inputArray):
            break
        jumpLen += 1

    return jumpLen