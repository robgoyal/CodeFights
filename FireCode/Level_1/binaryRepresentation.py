# Name: binaryRepresentation.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Return the binary represetation of an integer as a string
# Note: Found an improved recursive solution

def dec_to_bin(number):
    if number == 1:
        return str(number)

    else:
        return dec_to_bin(number // 2) + str(number % 2)