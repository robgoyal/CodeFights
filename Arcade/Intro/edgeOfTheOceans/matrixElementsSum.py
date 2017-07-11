# Name: matrixElementsSum.py
# Author: Robin Goyal
# Last-Modified: June 20, 2017
# Purpose: Return the price of the rooms which aren't
#          inhabited by ghosts. Ghosts are marked by a 0 price
#          and any room below a 0 shouldn't be included in the price

def matrixElementsSum(matrix):
    
    # List to store the indices of ghosts
    indices = []
    price = 0

    for row in matrix:
        for i in range(len(array)):

            # Ignore prices of rooms with ghosts above you
            if i not in indices:
                price += array[i]

        # Store the indices where there was a 0 in the row
        if 0 in array:
            [indices.append(i) for i, j in enumerate(array) if j == 0]    