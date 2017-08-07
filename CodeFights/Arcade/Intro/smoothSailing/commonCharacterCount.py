# Name: commonCharacterCount.py
# Author: Robin Goyal
# Last-Modified: June 21, 2017
# Purpose: Return the number of common characters between two strings
# Note: Only found out about the set data structure after viewing solutions
#       which couldve resulted in a far simpler solution

def commonCharacterCount(s1, s2):

    # Use dictionary to hold characters
    s1Chars = dict()
    s2Chars = dict()
    
    # Count occurence of each character in strings
    for i in s1:
        if i not in s1Chars:
            s1Chars[i] = 0
        s1Chars[i] += 1
    
    for i in s2:
        if i not in s2Chars:
            s2Chars[i] = 0
        s2Chars[i] += 1
    
    # Calculate the common characters in both strings 
    # by summing the minimum values from each dictionary
    commonChars = 0
    for key in s1Chars:
        if key in s2Chars:
            commonChars += min(s1Chars[key], s2Chars[key])
    
    return commonChars