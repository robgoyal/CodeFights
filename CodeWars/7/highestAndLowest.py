# Name: highestAndLowest.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return the highest and lowest numbers in a string of numbers


def high_and_low(numbers):
    """high_and_low(numbers)

    (str) -> str

    Return the highest and lowest ints in a string, numbers.

    Examples:
    >> high_and_low("1 2 5 6 10 -1 -2")
    "10 -2"
    """

    l = list(map(int, numbers.split()))
    return "{} {}".format(max(l), min(l))
