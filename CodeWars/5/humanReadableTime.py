# Name: humanReadableTime.py
# Author: Robin Goyal
# Last-Modified: June 11, 2018
# Purpose: Return a human-readable time format
#          given the number of seconds


def make_readable(seconds):
    """make_readable

    Return a human-readable time format given
    the number of seconds.

    Examples:
    >>> make_readable(0)
    "00:00:00"
    >>> make_readable(5)
    "00:00:05"
    >>> make_readable(86399)
    "23:59:59"
    """

    ss = seconds % 60
    mm = (seconds // 60) % 60
    hh = seconds // 3600

    return "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
