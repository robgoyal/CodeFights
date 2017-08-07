# Name: addBorder.py
# Author: Robin Goyal
# Last-Modified: June 22, 2017
# Purpose: Add a border around a rectangular matrix
#          of equal length strings

def addBorder(picture):

    string_len = len(picture[0])

    # Add initial row of string_len + 2 border
    picture.insert(0, "*" * string_len + 2)

    # Add 1 * around each string element
    for i in range(len(picture) - 1):
        picture[i + 1] = "*" + picture[i + 1] + "*"

    # Add final row of * of string_len + 2
    picture.append("*" * string_len + 2)    

    return picture