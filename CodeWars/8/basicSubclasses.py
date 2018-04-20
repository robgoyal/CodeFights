# Name: basicSubclasses.py
# Author: Robin Goyal
# Last-Modified: April 19, 2018
# Purpose: Implement basic subclassing


def God():
    """
    None -> list: objects

    Returns a list of a Man and Woman objects.

    Examples:
    >>> God()
    [Man(), Woman()]
    """

    return [Man(), Woman()]


class Human(object):
    pass


class Man(Human):
    def __repr__(self):
        return "Man()"


class Woman(Human):
    def __repr__(self):
        return "Woman()"
