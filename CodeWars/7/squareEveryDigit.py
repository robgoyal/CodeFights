# Name: squareEveryDigit.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement the square every digit challenge


def square_digits(number):
    """
    (int) -> int

    Return the square of every digit in the integer.

    Examples:
    >>> square_digits(9119)
    811181
    >>> square_digits(25)
    410
    """

    # Get the squares of each digit
    squares = [int(digit) for digit in str(number)]
    return int("".join(str(square) for square in squares))
