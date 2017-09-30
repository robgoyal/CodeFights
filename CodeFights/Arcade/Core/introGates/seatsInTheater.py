# Name: seatsInTheater.py
# Author: Robin Goyal
# Last-Modified: May 15, 2017
# Purpose: Return the number of seats behind and 
#          to the left of your seat

def seatsInTheater(nCols, nRows, col, row):
    return (nCols - col + 1) * (nRows - row)