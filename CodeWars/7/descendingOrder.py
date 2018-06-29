# Name: descendingOrder.py
# Author: Robin Goyal
# Last-Modified: June 28, 2018
# Purpose: Return an integer in descending order


def Descending_Order(num):
    """Descending_Order(num)

    (int) -> int

    Return num, an integer in reversing order.

    Examples:
    >>> Descending_Order(15235)
    53251
    """

    return int("".join(sorted(str(num), reverse=True)))
