# Name: isIPv4Address.py
# Author: Robin Goyal
# Last-Modified: July 11, 2017
# Purpose: Check if a string is of form IPv4

def isIPv4Address(inputString):

    # Return false for empty values or non-digit values
    try:
        addresses = [int(x) for x in inputString.split('.')]
    except:
        return False

    # Verify 4 items in list and each item is in 8-bit unsigned int range
    return len(addresses) == 4 and all(0 <= item <= 255 for item in addresses)
