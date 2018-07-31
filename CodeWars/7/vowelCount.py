# Name: vowelCount.py
# Author: Robin Goyal
# Last-Modified: July 30, 2018
# Purpose: Return the number of vowels in a string


def vowel_count(string):
    """Returns the number of vowels in string

    Examples:
    >>> vowel_count("abracadabra")
    5
    >>> vowel_count("Bob the builder")
    5
    """

    return sum(char in "aeiouAEIOU" for char in string)
