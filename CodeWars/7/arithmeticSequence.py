# Name: arithmeticSequence.py
# Author: Robin Goyal
# Last-Modified: March 3, 2019


def nthterm(first, n, c):
    """nthterm
    (int, int, int) -> int

    Return the nth term of the sequence
    f(n) = f(n-1) + c where the sequence
    begins with first.

    Examples:
    >>> nthterm(1, 3, 4)
    13
    """

    if n == 0:
        return first

    return nthterm(first + c, n - 1, c)
