# Name: isBeautifulString.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: A string is beautiful if theres an increasing number 
#          of characters in alphabetical order

def isBeautifulString(inputString):

    # Initialize array of 26 elements with 0
    chars = [0] * 26

    # Store number of occurrences of each character
    for i in inputString:
        pos = ord(i) - ord('a')
        chars[pos] += 1

    # Return false if previous index has more elements than next 
    # index in string
    for i in range(len(chars) - 1):
        if chars[i+1] > chars[i]:
            return False

    return True