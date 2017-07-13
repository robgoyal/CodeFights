# Name: variableName.py
# Author: Robin Goyal
# Last-Modified: July 13, 2017
# Purpose: Check if a string is a valid identifier

import re

def variableName(name):

    # Search for any non word character
    match = re.search(r'\W', name)

    # If match is returned or first character is a digit, return true
    if (name[0].isdigit() or match):
        return False
    return True