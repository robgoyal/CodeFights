# Name: isItANumber.py
# Author: Robin Goyal
# Last-Modified: July 07, 2018
# Purpose: Return True if a string is a number


def isDigit(string):
    """isDigit(string)

    (str) -> bool

    Return True if a string is a valid number. False otherwise.

    Examples:
    >>> isDigit("3")
    True
    >>> isDigit("-2.4")
    True
    >>> isDigit("zero")
    False
    """

    try:
        temp = float(string)
    except:
        return False

    return True
