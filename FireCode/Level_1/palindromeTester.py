# Name: palindromeTester.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Test if a string is a palindrome
# Note: Palindrome is when the reverse of the string is equal to the string.
#       I could've used the string reverse function to test equality but that
#       felt like cheating

def is_palindrome(input_string):

    # Iterate through half of string
    for i in range(len(input_string) // 2):

        # Test if value at ith index is equal to value at len(string) - ith index
        if input_string[i] != input_string[-1-i]:
            return False

    return True