# Name: equalSidesOfArray.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return an index sum of left side equals right side


def find_even_index(arr):
    """find_even_index(arr)

    (list) -> int

    Return an index where the sum of the left
    side of the list equals the right side.

    Examples:
    >>> find_even_index([1, 2, 3, 4, 3, 2, 1])
    3
    """

    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i

    return -1
