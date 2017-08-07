# Name: chessBoardCellColor.py
# Author: Robin Goyal
# Last-Modified: July 13, 2017
# Purpose: Check if two cells of a chess board are the same color

def chessBoardCellColor(cell1, cell2):

    # Check if both colors are the same
    return color(cell1) == color(cell2)

def color(cell):
    ''' Return the color of the cell
        True = Dark Cell
        False = Light Cell '''

    if (ord(cell[0]) - ord('A')) % 2 == 0:
        return int(cell[1]) % 2 == 1
    else:
        return int(cell[1]) % 2 == 0