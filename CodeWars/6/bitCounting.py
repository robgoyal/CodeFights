# Name: bitCounting.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Return the number of set bits in a number


def countBits(n):
    """countBits

    Return the number of set bits in a number.

    Examples:
    >>> countBits(5)
    2
    """

    return bin(n).count('1')
