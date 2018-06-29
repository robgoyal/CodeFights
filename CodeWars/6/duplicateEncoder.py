# Name: duplicateEncoder.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Implement solution to Duplicate Encoder challenge


def duplicate_encode(word):
    """duplicate_encode

    Return a new string where each character in the nwe string
    is '(' if that char appears only once in the original string
    or ')' if it appears more than once.

    Examples:
    >>> duplicate_encode("din")
    "((("
    >>> duplicate_encode("Success")
    ")()))())"
    """

    word = word.lower()

    # Create frequency dictionary
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1

    encoded = [")" if freq.get(char) > 1 else "(" for char in word]
    return "".join(encoded)
