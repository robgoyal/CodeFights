# Name: yourOrderPlease.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Sort a given string


def order(sentence):
    """order(sentence)

    Return a string sorted. Each word in the string
    contains a number and it should be sorted based
    off of the numbers.

    Examples:
    >>> order("is2 Thi1s T4est 3a")
    Thi1s is2 3a T4est
    """

    words = sentence.split()
    l = [None] * len(words)

    for word in words:
        for char in word:
            if char.isdigit():
                l[int(char) - 1] = word

    return " ".join(l)
