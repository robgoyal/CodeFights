# Name: findOddInt.py
# Author: Robin Goyal
# Last-Modified: March 13, 2018
# Purpose: Find the number with odd number of occurrences in list


def find_it(seq):
    """
    (list: int) -> int

    Return the integer in seq which contains an odd number
    of occurrences in seq. Only a single element will have
    an odd number of occurrences.

    Examples:
    >>> find_it([1, 2, 3, 2, 3, 4, 1])
    4
    """

    groups = {}

    # Group ints with respect to their frequencies
    for num in seq:
        groups[num] = groups.get(num, 0) + 1

    for num, freq in groups.items():
        if freq % 2 == 1:
            return num
