# Name: birdCode.py
# Author: Robin Goyal
# Last-Modified: May 31, 2018
# Purpose: Generate four letter bird codes for North-American birds


def bird_code(arr):
    """
    (list) -> list

    Create list of four letter codes for common names of birds in arr.

    Examples:
    >>> bird_code(["Black-Capped Chickadee", "Common Tern"])
    ["BCCH", "COTE"]
    >>> bird_code(["Robin", "Cooper's Hawk"])
    ["ROBI", "COHA"]
    """

    # Replace all hyphens with spaces before passing to code generating function
    return [create_code(string.replace('-', ' ').split(' ')) for string in arr]


def create_code(words):
    """
    (list) -> str

    Return the four letter code for the birds name found in words.

    Rules:
        - if the bird's name has only one word, take first four letters
        - if the bird's name has two words, take first two letters of each word
        - if the bird's name has three words, take first letter of first two words
          and first two letters of third word
        - if the bird's name is four words long, take first letter of each word

    Examples:
    >>> create_code(["Black", "Capped", "Chickadeee"])
    "BCCH"
    """

    if len(words) == 1:
        code = words[0][:4]
    elif len(words) == 2:
        code = words[0][:2] + words[1][:2]
    elif len(words) == 3:
        code = words[0][0] + words[1][0] + words[2][:2]
    elif len(words) == 4:
        code = "".join(word[0] for word in words)

    return code.upper()
