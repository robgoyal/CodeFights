# Name: alphabeticShift.py
# Author: Robin Goyal
# Last-Modified: July 13, 2017
# Purpose: Return new string with each character of input string
#          shifted by 1

def alphabeticShift(inputString):

    # Use moduolo to wrap around for character z
    return "".join([chr((ord(i) - 97 + 1) % 26 + 97) for i in inputString])