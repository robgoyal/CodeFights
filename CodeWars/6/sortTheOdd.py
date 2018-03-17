# Name: sortTheOdd.py
# Author: Robin Goyal
# Last-Modified: March 17, 2018
# Purpose: Implement solution to Sort the Odd


def sort_array(arr):
    """
    (list: int) -> list: int

    Return an array of the odd numbers in sorted order
    while the even numbers remain in place.

    Examples:
    >>> sort_array([5, 3, 2, 1, 5, 4, 8, 7])
    [1, 3, 2, 5, 5, 4, 8, 7]
    """

    odds = sorted([i for i in arr if i % 2 == 1])
    index = 0
    sorted_arr = []

    for i, value in enumerate(arr):
        if value % 2 == 1:
            sorted_arr.append(odds[index])
            index += 1
        else:
            sorted_arr.append(value)

    return sorted_arr
