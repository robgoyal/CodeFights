# Name: strangeCode.py
# Author: Robin Goyal
# Last-Modified: January 29, 2018
# Purpose: Calculate the value displayed by a counter at time t

import math


def strange_code(t):
    '''
    (int) -> int

    Precondition: 1 <= t <= 10**12

    Calculate the value displayed a strange counter
    at time t.

    At time t = 1, the counter displays 3. As t increases, the
    value decreases. Once the counter displays 1, the value
    increases by a factor of 2 from it's original value.

    Example: Time, Value
                1, 3        4, 6        10, 12
                2, 2        5, 5        11, 11
                3, 1        6, 4        12, 10
                            7, 3        13, 9
                            8, 2        14, 8
                            9, 1        15, 7
                                        .....

    >>> strange_code(5)
    5
    >>> strange_code(21)
    1
    >>> strange_code(13)
    9
    '''

    # Current cycle of time
    cycle = math.floor(math.log((t + 2) / 3, 2) + 1)

    # Initial value at current cycle
    cycle_initial_time = 3 * math.pow(2, cycle - 1) - 2
    diff = t - cycle_initial_time

    return int(cycle_initial_time + 2 - diff)


if __name__ == "__main__":
    t = int(input().strip())
    result = strange_code(t)
    print(result)
