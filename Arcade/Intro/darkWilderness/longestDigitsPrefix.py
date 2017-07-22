# Name: longestDigitsPrefix.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: Output the prefix of a string which contains only digits
import re

def longestDigitsPrefix(inputString):

    # Find the first match of a number
    prefix = re.match("\d+", inputString)

    # Empty string if no match
    if prefix == None:
        return ""
    else:
        return prefix.group(0)