# Name: encryption.py
# Author: Robin Goyal
# Last-Modified: February 16, 2018
# Purpose: Encrypt a string

import math


def encryption(s):
    """
    (str) -> str

    Return a string by encrypting a string s using
    the following encryption scheme.

    Split s into rows (floor(sqrt(s)) and cols (ceil(sqrt(s))).
    Create words from letters in each column and split separate
    the words by a string.

    Examples:
    >>> encryption("haveaniceday")
    hae and via ecy
    >>> encryption("feedthedog")
    fto ehg ee dd
    >>> encryption("chillout")
    clu hlt io
    """

    # Initialize rows and cols for the grid
    rows = math.floor(math.sqrt(len(s)))
    cols = math.ceil(math.sqrt(len(s)))

    # Increment rows if grid size is < size of s
    if rows * cols < len(s):
        rows += 1

    # Create grid for encryption scheme
    grid = [s[i:i + cols] for i in range(0, len(s), cols)]

    encrypted_msg = ""
    for i in range(cols):
        for j in range(rows):

            # Access letter if index exists
            try:
                encrypted_msg += grid[j][i]
            except IndexError:
                pass

        # Separate words with space
        encrypted_msg += " "

    return encrypted_msg
