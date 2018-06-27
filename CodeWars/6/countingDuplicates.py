# Name: countingDuplicates.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Return the number of reoccurring characters in string


def duplicate_count(text):
    """duplicate_count

    Return the number of recurring characters in a string.

    Examples:
    >>> duplicate_count("aAbbcdef")
    2
    """

    text = text.lower()

    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    count = len(list(filter(lambda x: x > 1, freq.values())))
    return count
