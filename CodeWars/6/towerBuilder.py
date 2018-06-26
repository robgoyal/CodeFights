# Name: towerBuilder.py
# Author: Robin Goyal
# Last-Modified: June 25, 2018
# Purpose: Build a tower given an integer


def tower_builder(n):
    """tower_builder

    Build a tower given the number of floors, n.

    Examples:
    >>> tower_builder(3)
      *
     ***
    *****
    """

    return ["{}{}{}".format((n - 1 - i) * ' ', (2 * i + 1) * '*',
                            (n - 1 - i) * ' ') for i in range(n)]
