# Name: arrayDiff.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Return the elements of a not in b


def array_diff(a, b):
    """array_diff

    Return the elements of a not in b.

    Examples:
    >>> array_diff([1, 2, 3], [2, 4, 6])
    [1, 3]
    """

    return [i for i in a if i not in b]
