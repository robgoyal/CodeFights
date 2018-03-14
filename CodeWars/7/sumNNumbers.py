# Name: sumNNumbers.py
# Author: Robin Goyal
# Last-Modified: March 13, 2018
# Purpose: Return the sum of the first n numbers


def f(n):
    """
    (int) -> int or None

    Return None if n is a positive integer, else
    return the sum of the first n numbers.

    Examples:
    >>> f(100)
    5050
    >>> f(-5)
    None
    >>> f(6.0)
    None
    """

    return n * (n + 1) // 2 if (type(n) == int and n > 0) else None
