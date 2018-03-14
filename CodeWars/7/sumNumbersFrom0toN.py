# Name: sumNumbersFrom0toN.py
# Author: Robin Goyal
# Last-Modified: March 13, 2018
# Purpose: Return the sequence for the sum of the first N numbers


def show_sequence(n):
    """
    (int) -> str

    Return the sequence for the sum of the first n numbers.

    Examples:
    >>> show_sequence(-1)
    "-1<0"
    >>> show_sequence(0)
    "0=0"
    >>> show_sequence(5)
    "0+1+2+3+4+5 = 10"
    """

    if n < 0:
        return "{}<0".format(n)
    elif n == 0:
        return "0=0"

    sum_of_n = n * (n + 1) // 2
    digits = [str(i) for i in range(n + 1)]

    return "{} = {}".format("+".join(digits), sum_of_n)
