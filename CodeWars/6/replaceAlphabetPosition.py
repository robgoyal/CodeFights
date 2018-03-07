# Name: replaceAlphabetPosition.py
# Author: Robin Goyal
# Last-Modified: March 7, 2018
# Purpose: Implement the Replace with Alphabet Position challenge


def alphabet_position(text):
    """
    (str) -> str

    Replace every character in text with its position
    in the alphabet ignoring non-alphanumeric characters.

    Examples:
    >>> alphabet_position("abc")
    "1 2 3"
    >>> alphabet_position("call a cab")
    "3 1 12 12 1 3 1 2"
    """

    positions = [str(ord(char.lower()) - 96) for char in text if char.isalpha()]
    return " ".join(positions)
