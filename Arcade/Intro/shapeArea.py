# Name: shapeArea.py
# Author: Robin Goyal
# Last-Modified: June 16, 2017
# Purpose: Calculate the area of an n-interesting polygon.
# Notes: Initially the solution I came up with used recursion but since
#        the inputs can be up to 10^4, the stack space used would be too
#        large which resulted in an overflow. Eventually I had to brush up
#        on my sequences skills and derive an equation from sequences. 

def shapeArea(n):
    return 2*math.pow(n, 2) - 2*n + 1