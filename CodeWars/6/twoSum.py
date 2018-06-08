# Name: twoSum.py
# Author: Robin Goyal
# Last-Modified: June 7, 2018
# Purpose: Return a list of indices which sum to
#          a target number


def two_sum(numbers, target):
    """two_sum

    Return a list with two indices where two
    values in numbers sum to target.

    Examples:
    >>> two_sum([5, 2, 3, 1], 6)
    [0, 3]
    >>> two_sum([5, 3], 9)
    []
    """

    digits = {}

    for i, number in enumerate(numbers):
        try:
            j = digits[target - number]
        except KeyError:
            digits[number] = i
        else:
            return [i, j]

    return []
