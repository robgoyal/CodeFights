# Name: commonDenominators.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Return a list of rationals with their common denominators

from functools import reduce

def gcd(a, b):
    """gcd

    Return the common denominator
    of two numbers.

    Examples:
    >>> gcd(5, 10)
    5
    >>> gcd(6, 14)
    2
    """

    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """lcm

    Return the lowest common multiple
    of two numbers.

    Examples:
    >>> lcm(5, 2)
    10
    >>> lcm(10, 5)
    20
    """

    return (a * b) // gcd(a, b)

def convertFracts(lst):
    """convertFracts

    Return a list of fractions with
    common denominators.

    Examples:
    >>> convertFracts([[1, 2], [1, 3], [1, 4]])
    [[6, 12], [4, 12], [3, 12]]
    """

    denoms = [frac[1] for frac in lst]
    res = reduce(lcm, denoms)
    return [[res // frac[1] * frac[0], res] for frac in lst]
