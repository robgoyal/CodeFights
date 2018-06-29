# Name: tribonacciSequence.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return a list of tribonacci numbers given a sequence


def tribonacci(signature, n):
    """tribonacci(signature, n)

    (list, int) -> list

    Return a list of the n first tribonacci given
    the first 3 numbers in signature.

    Examples:
    >>> tribonacci([1, 1, 1], 5)
    [1, 1, 1, 3, 5]
    """

    l = []
    for i in range(n):
        if i < 3:
            l.append(signature[i])
        else:
            l.append(sum(l[i - 3:i]))
    return l
