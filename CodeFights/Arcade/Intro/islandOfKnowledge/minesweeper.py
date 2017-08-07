# Name: minesweeper.py
# Author: Robin Goyal
# Last-Modified: July 12, 2017
# Purpose: Give an array of true and false values with true indicating a mine
#          return an array of the same length indicating number of surrounding
#          mines at each position
# Note: Could've optimized the solution but a pure brute force implementation

def minesweeper(matrix):
    grid = []

    for row in range(len(matrix)):
        gridRow = []
        for col in range(len(matrix[0])):
            count = 0

            # Top Row
            if (row == 0): 
                if (col == 0):                    # Top-Left corner
                    count = [matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]].count(True)

                elif (col == len(matrix[0]) - 1): # Top-Right corner
                    count = [matrix[row][col-1], matrix[row+1][col], matrix[row+1][col-1]].count(True)

                else:                             # Middle Columns in top Row
                    count = [matrix[row][col-1], matrix[row][col+1]].count(True) \
                            + matrix[row+1][col-1:col+2].count(True)

            # Bottom Row
            elif (row == len(matrix) -1):
                if (col == 0):                    # Bottom-Left corner
                    count = [matrix[row][col+1], matrix[row-1][col], matrix[row-1][col+1]].count(True)

                elif (col == len(matrix[0]) - 1): # Bottom-Right corner
                    count = [matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1]].count(True)

                else:                             # Middle Columns in bottom Row
                    count = [matrix[row][col-1], matrix[row][col+1]].count(True) \
                            + matrix[row-1][col-1:col+2].count(True)

            # Middle Rows
            else:
                if (col == 0):                    # Left most column
                    count = matrix[row-1][col:col+2].count(True) +  [matrix[row][col+1]].count(True) \
                            + matrix[row+1][col:col+2].count(True)

                elif (col == len(matrix[0]) -1):  # Right most column
                    count = matrix[row-1][col-1:col+1].count(True) + [matrix[row][col-1]].count(True) \
                            + matrix[row+1][col-1:col+1].count(True)

                else:                             # Middle columns
                    count = matrix[row-1][col-1:col+2].count(True) + matrix[row+1][col-1:col+2].count(True) + \
                            [matrix[row][col-1], matrix[row][col+1]].count(True)

            gridRow.append(count)
        grid.append(tempRow)

    return grid