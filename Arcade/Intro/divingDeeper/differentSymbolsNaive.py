# Name: differentSymbolsNaive.py
# Author: Robin Goyal
# Last-Modified: July 18, 2017
# Purpose: Given a string, find the number of different characters in it

def differentSymbolsNaive(s):

    # Dictionary comprehension
    chars = {i: True for i in s}
    return len(chars.keys())
