# Name: largest5NumbersInSeries.py
# Author: Robin Goyal
# Last-Modified: April 19, 2018
# Purpose: Return the largest 5 digit number in a series


def solution(digits):
    """
    (str) -> int

    Return the largest 5 digit number in a series.

    Examples:
    >>> solution("4523879")
    52387
    """

    return max(int(digits[i:i + 5]) for i in range(len(digits) - 4))
