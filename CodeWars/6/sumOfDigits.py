# Name: sumOfDigits.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Return the recursive sum of all of the digits in a number


def digital_root(n):
    """digital_root

    Return the recursive sum of all of the digits in a number.

    Examples:
    >>> 45
    9
    >>> 378
    9
    """

    while (len(str(n))) != 1:
        n = sum(int(i) for i in str(n))

    return n
