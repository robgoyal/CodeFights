# Name: palindromeRearranging.py
# Author: Robin Goyal
# Last-Modified: July 10, 2017
# Purpose: Check if a string's character can be rearranged
#          to form a palindrome 

def palindromeRearranging(inp):

    # Store occurrences of each character in input string in dictionary
    occurences = dict((letter, inp.count(letter)) for letter in set(inp))

    # Determine number of odd occurences of characters
    odd_count = 0
    for key in occurences.values():
        if key % 2 != 0:
            odd_count += 1

    # Palindrome can't be created if number of odd occurences is greater than 1
    return odd_count <= 1
