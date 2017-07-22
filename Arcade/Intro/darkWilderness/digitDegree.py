# Name: digitDegree.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: Find the number of steps it takes to replace a number 
#          with the sum of its digits until it gets to one digit
#          91 -> 9 + 1 = 10 -> 1 + 0 = 1 --------> 2 steps

def digitDegree(n):

    degree = 0

    # Sum digits of integer until single digit
    while (n > 9):
        n = sum([int(i) for i in str(n)])
        degree += 1

    return degree