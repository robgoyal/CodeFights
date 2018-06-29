# Name: IQTest.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return which of the given numbers differs from the others


def iq_test(numbers):
    """iq_test(numbers)

    Return the given number that differs from the others.

    Examples:
    >>> iq_test([1, 2, 4, 10, 2])
    1
    >>> iq_test([3, 5, 9, 7, 2, 13])
    2
    """

    numbers = list(map(int, numbers.split()))
    freq = {0: [], 1: []}

    for i, num in enumerate(numbers):
        freq[num % 2].append(i + 1)

    if len(freq[0]) == 1:
        return freq[0][0]

    return freq[1][0]
