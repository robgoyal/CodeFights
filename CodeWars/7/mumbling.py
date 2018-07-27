# Name: mumbling.py
# Author: Robin Goyal
# Last-Modified: July 26, 2018
# Purpose: Implement solution to mumbling


def accum(s):
    """Returns the mumbling version of s

    :param s: string to mumble
    :type s: str
    :returns: mumbled version of s
    :rtype: str

    Examples:
    >>> accum("Zasdfa")
    "Z-Aa-Sss-Dddd-Fffff-Aaaaaa"
    """

    return '-'.join([(char.upper() + char.lower() * index)
                     for index, char in enumerate(s)])
