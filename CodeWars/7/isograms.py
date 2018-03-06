# Name: isograms.py
# Author: Robin Goyal
# Last-Modified: March 5, 2018
# Purpose: Implement the isograms challenge
# Note: Could've used set theory to test if any chars repeated


def is_isogram(string):
    """
    (str) -> bool

    Return True iff string doesn't contain any
    repeating characters irrespective of case.

    Examples:
    >>> is_isogram("robin")
    True
    >>> is_isogram("moose")
    False
    >>> is_isogram("Ampersand")
    False
    >>> is_isogram("")
    True
    """

    # Construct frequency array for characters
    char_frequencies = [0] * 26
    for char in string:
        char_frequencies[ord(char.lower()) - 97] += 1

    # Check if any frequencies are greater than 1
    for frequency in char_frequencies:
        if frequency >= 2:
            return False

    return True
