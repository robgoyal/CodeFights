# Name: findMissingLetter.py
# Author: Robin Goyal
# Last-Modified: June 25, 2018
# Purpose: Find the missing letter in a series of consecutive characters


def find_missing_letter(chars):
    """find_missing_letter

    Return the missing letter in a series of chars from
    a list.

    Examples:
    >>> find_missing_letters(['a', 'b', 'd'])
    c
    """

    for i in range(len(chars)):
        if (ord(chars[i + 1]) - ord(chars[i])) != 1:
            return chr(ord(chars[i]) + 1)
