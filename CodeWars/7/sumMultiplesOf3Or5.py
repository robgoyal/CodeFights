# Name: sumMultiplesOf3Or5.py
# Author: Robin Goyal
# Last-Modified: March 16, 2018
# Purpose: Find sum of all multiples of 3 or 5


def find(n):
    """
    (int) -> int

    Return the sum of numbers from 1 to n
    if a multiple of 3 or 5.

    Examples:
    >>> find(10)
    33
    >>> find(5)
    8
    """

    return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
