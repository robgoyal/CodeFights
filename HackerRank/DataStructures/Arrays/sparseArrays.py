# Name: sparseArrays.py
# Author: Robin Goyal
# Last-Modified: October 30, 2017
# Purpose: Calculate the number occurrences of a query in a series of strings

def sparseArrays(n, arr, queries):
    for i in range(queries):

        # Get query and print the number of occurrences in the arr
        print arr.count(input())