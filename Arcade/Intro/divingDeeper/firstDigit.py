# Name: firstDigit.py
# Author: Robin Goyal
# Last-Modified: July 18, 2017
# Purpose: Find the leftmost digit in a string

import re

def firstDigit(inputString):
    return re.search("\d", inputString).group(0)