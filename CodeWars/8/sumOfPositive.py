# Name: sumOfPositive.py
# Author: Robin Goyal
# Last-Modified: May 30, 2018
# Purpose: Return the sum of positive numbers in a list


def sumOfPositive(arr):
    """
    (list) -> int

    Return the sum of all positive
    integers in arr.

    Examples:
    >>> sumOfPositive([1, -5, 4, 6])
    11
    """

    return sum(num for num in arr if num > 0)
