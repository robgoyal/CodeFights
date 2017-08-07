# Name: flipIt.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Flip a matrix along its vertical axis
# Example:  1, 2, 3                 3, 2, 1
#           4, 1, 9        ==>      9, 1, 4    
#           8, 5, 10                10, 5, 8

def flip_vertical_axis(matrix):

    # Store half of row length to refrain from reduntant calculations
    row_length = len(matrix[0]) // 2

    for i in range(len(matrix)):
        for j in range(row_length):

            # One liner to swap values in row
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]

    return matrix