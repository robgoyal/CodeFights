# Name: numberPeopleInBus.py
# Author: Robin Goyal
# Last-Modified: June 7, 2018
# Purpose: Calculate the remaining number of people
#          on the bus after the last stop


def number(bus_stops):
    """bus_stops

    Return the remaining number of people
    on the bus after the last stop.

    Examples:
    >>> number([[10, 0], [5, 3], [2, 4], [7, 4]])
    13
    >>> number([[5, 0], [5, 5], [3, 6], [0, 2]])
    0
    """

    hop_ons = sum(stop[0] for stop in bus_stops)
    hop_offs = sum(stop[1] for stop in bus_stops)

    return hop_ons - hop_offs
