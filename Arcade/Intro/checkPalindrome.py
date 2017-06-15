# Name: checkPalindrome.py
# Author: Robin Goyal
# Last-Modified: May 15, 2017
# Purpose: Check if a string is a palindrome

def checkPalindrome(inputString):
    
    for i in range(len(inputString)/2):
        if inputString[i] != inputString[-1-i]:
            return False
    return True