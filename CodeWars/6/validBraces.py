# Name: validBraces.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Check if string is a valid pair of braces


def validBraces(string):
    """validBraces

    Return True if a strinng has a valid set of parentheses.

    Examples:
    >>> validBraces("[{{}}()]")
    True
    >>> validBraces("{[)]}")
    False
    """

    stack = []

    opened = ["(", "{", "["]
    pairs = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}

    for c in string:
        if c in opened:
            stack.append(c)
        else:
            try:
                popped = stack.pop()
                if pairs[popped] != c:
                    return False
            except IndexError:
                return False

    return len(stack) == 0
