# Name: persistentBugger.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return the number of times digits of int must be multiplied
#          until a single digit is reached


from operator import mul
from functools import reduce


def persistence(n):
    """persistence(n)

    (int) -> int

    Return the number of times the digits of n must be multiplied
    until a single digit is reached.
    """

    count = 0

    while (len(str(n)) != 1):
        count += 1
        n = reduce(mul, map(int, str(n)))

    return count
