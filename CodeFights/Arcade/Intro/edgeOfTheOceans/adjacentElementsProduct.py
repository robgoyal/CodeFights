# Name: adjacentElementsProduct.py
# Author: Robin Goyal
# Last-Modified: June 14, 2017
# Purpose: Return the largest adjacent product
# Notes: This couldve been done with list comprehension but I 
#        saw other solutions so I didn't want to use an answer I saw

def adjacentElementsProduct(inputArray):
    ''' Initialized max value to negative infinity
        since negative max products can occur '''

    max = float("-inf")
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if product > max:
            max = product
    return max