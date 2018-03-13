# Name: randomCase.py
# Author: Robin Goyal
# Last-Modified: March 12, 2018
# Purpose: Implement a function to randomly upper and lower
#          characters in a string


from random import choice


def random_case(x):
    """
    (str) -> str

    Return a string which has random upper and lower
    characters of string x.
    """

    return "".join([choice((chr.upper(), chr.lower())) for chr in x])
