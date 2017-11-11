# Name: gameOfThrones.py
# Author: Robin Goyal
# Last-Modified: November 11, 2017
# Purpose: Check if an anagram of the string can be a palindrome

def gameOfThrones(inp):

    char_count = {}

    # Populate dictionary with count of number of chars
    for char in inp:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Count number of odd values in dictionary
    odd_count = sum(list(reduce(lambda x: x % 2 == 1, char_count.values())))

    # Number of chars with odd count must be less than or equal to 1
    if odd_count > 1:
        return "NO"
    return "YES"