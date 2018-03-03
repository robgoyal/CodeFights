# Name: binaryAddition.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement binary addition


def add_binary(a, b):
    """
    (int, int) -> str

    Return the sum of a and b in its binary representation

    Examples:
    >>> add_binary(2, 3)
    101
    >>> add_binary(10, 3)
    1011
    >>> add_binary(0, 1)
    1
    """

    return bin(a + b)[2:]
