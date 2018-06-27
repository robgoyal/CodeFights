# Name: buildPileCubes.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Implement solution to Build a Pile of Cubes challenge


def find_nb(m):
    """find_nb

    Find the number of cubes you'll have to build given the
    total volume of the building, m.
    """

    total, i = 0, 0
    while (total < m):
        i += 1
        total += (i ** 3)

    return i if total == m else -1
