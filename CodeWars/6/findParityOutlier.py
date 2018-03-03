# Name: findParityOutlier.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement the find parity outlier challenge


def find_outlier(integers):
    """
    (list: int) -> int

    Preconditions: len(integers) >= 3

    A list, integers contains exclusively even or
    odd numbers except for one integer of the other
    type. Return the outlying integer.

    Examples:
    >>> find_outlier([3, 6, 8, 16, 2, 4])
    3
    >>> find_outlier([4, 3, 1, 9, 15])
    4
    """

    odd_even = {'odd': [], 'even': []}

    for integer in integers:
        if integer % 2 == 0:
            odd_even['even'].append(integer)
        else:
            odd_even['odd'].append(integer)

    return min(odd_even.values())[0]
