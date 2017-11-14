# Name: staircase.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Print an upward-rising staircase of a specific height

def staircase(height):

    # print row 
    for i in range(height):
        print(" " * (height - i + 1) + "#" * (i + 1))