# Name: bouncingBall.py
# Author: Robin Goyal
# Last-Modified: March 3, 2018
# Purpose: Implement the bouncing ball challenge


def bouncingBall(initial, proportion):
    """
    (int, float) -> int

    Return the number of bounces required for the
    ball to reach a height less than 1 with an
    initial height and a proportion the height decreases by.

    Examples:
    >>> bouncingBall(4, 0.5)
    2
    >>> bouncingBall(10, 0.1)
    1
    >>> bouncingBall(5, 0.3)
    2
    """

    bounces, height = 0, initial

    while height > 1:
        bounces += 1
        height *= proportion

    return bounces
