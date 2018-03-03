# Name: returningStrings.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement the returning strings challenge


def greet(name):
    """
    (str) -> str

    Implement a function that will return a greeting using name.

    Examples:
    >>> greet("Robin")
    Hello, Robin how are you doing today?
    """

    return "Hello, {} how are you doing today?".format(name)
