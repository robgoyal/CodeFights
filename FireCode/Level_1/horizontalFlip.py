# Name: horizontalFlip.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Flip an MxN matrix by the middle row
# Example:  1, 2, 3                     10, 5, 2
#           4, 6, 9         ====>       4, 6, 9
#           10, 5, 2                    1, 2, 3

def flip_horizontal_axis(matrix):

    # Iterate through half of matrix
    for i in range(len(matrix) // 2):

        # One liner to swap values
        matrix[i], matrix[-1-i] = matrix[-1-i], matrix[i]

    return matrix