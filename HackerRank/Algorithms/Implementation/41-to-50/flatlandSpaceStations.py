# Name: flatlandSpaceStations.py
# Author: Robin Goyal
# Last-Modified: January 31, 2018
# Purpose: Determine the maximum distance an astronaut will
#          have to travel to a space station


def flatlandSpaceStations(n, c):
    '''
    (int, list: int) -> int

    n is the number of cities and c is the indices at which
    a city contains a space station.

    Return the maximum distance for an astronaut to travel
    from any city to a space station.

    >>> flatlandSpaceStations(7, [1, 5, 6])
    2
    '''

    stations = sorted(c)
    max_distance = 0

    # Calculate distances for cities at ends which don't contain stations
    if stations[0] != 0:
        max_distance = max(max_distance, stations[0] - 0)

    if stations[-1] != (n - 1):
        max_distance = max(max_distance, (n - 1) - stations[-1])

    # Maximum distance for cities in between stations is halfway
    for i in range(len(stations) - 1):
        max_distance = max(max_distance, (stations[i + 1] - stations[i]) // 2)

    return max_distance
