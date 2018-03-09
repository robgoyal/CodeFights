# Name: bouncingBalls.py
# Author: Robin Goyal
# Last-Modified: March 9, 2018
# Purpose: Implement the solution to Bouncing Balls


def bouncingBall(height, bounce, window):
    """
    (int, float, int) -> int

    Preconditions: height > 0
                   0 < bounce < 1
                   height > window

    Return  the number of times a ball is visible
    from window if dropped from height where the
    height decreases by bounce at each bounce.
    Return -1 if conditions are not met.

    Examples:
    >>> bouncingBall(3, 0.66, 1.5)
    3
    >>> bouncingBall(30, 0.66, 1.5)
    15
    >>> bouncingBall(5, 1, 3)
    -1
    """

    if not(height > 0 and (0 < bounce < 1) and window > height):
        return -1

    views = 1
    height *= bounce

    # 2 views out of the window for each bounce
    while height > window:
        views += 2
        height *= bounce

    return views
