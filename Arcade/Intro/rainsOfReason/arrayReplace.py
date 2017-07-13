# Name: arrayReplace.py
# Author: Robin Goyal
# Last-Modified: July 12, 2017
# Purpose: Replace all occurences of elemToReplace with substitutionElem
#          in list of integers

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]