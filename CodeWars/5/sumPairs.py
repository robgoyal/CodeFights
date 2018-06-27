# Name: sumPairs.py
# Author: Robin Goyal
# Last-Modified: June 27, 2018
# Purpose: Implement solution to Sum of Pairs challenge


def sum_pairs(ints, s):
    """sum_pairs

    Return the first two values in ints
    which sum to s.

    Examples:
    >>> sum_pairs([11, 3, 7, 5], 10)
    [3, 7]
    """

    pairs = {}

    for i, int in enumerate(ints):
        diff = s - int
        if diff in pairs:
            pairs[diff].append(i)
        else:
            pairs[int] = [i]

    pairs = {key: value for (key, value) in pairs.items() if len(value) == 2}

    if not pairs:
        return None

    i, j = pairs[min(pairs, key=lambda x: pairs.get(x)[1])]
    return [ints[i], ints[j]]
