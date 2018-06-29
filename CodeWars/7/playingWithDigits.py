# Name: playingWithDigits.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Implement solution to Playing with Digits challenge


def dig_pow(n, p):
    """dig_pow(n, p)

    (int, int) -> int

    Return an integer k, if it exists where the square of the
    individual digits of n divided by p equal k.

    Examples:
    >>> dig_pow(89, 1)
    1
    >>> dig_pow(92, 1)
    -1
    """

    powsum = sum(int(dig) ** (p + i) for i, dig in enumerate(str(n)))

    factor = powsum / n
    if factor.is_integer():
        return int(factor)
    return -1
