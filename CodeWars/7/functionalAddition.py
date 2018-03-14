# Name: functionalAddition.py
# Author: Robin Goyal
# Last-Modified: March 14, 2018
# Purpose: Implement a function which always adds
#          n to any number


def add(n):
    """
    (int) -> func

    Return a function which increments
    a number by n.

    Examples:
    >>> add_one = add(5)
    >>> add_one(3)
    8
    """

    return lambda x: x + n
