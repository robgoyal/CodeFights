# Name: kangaroo.py
# Author: Robin Goyal
# Last-Modified: October 26, 2017
# Purpose: Given the initial position and velocities(jumps) of two kangaroos,
#          determine if they'll ever meet

def kangaroo(x1, v2, x2, v2):

    # Test for division by zero (same velocities)
    try:
        jumps = (x2 - x1)/(v1 - v2)
    except:

        # Starting at the same location
        if (x1 == x2):
            return "YES"

    if hops >= 0 and hops.is_integer():
        return "YES"

    return "NO"

def main():
    x1, v1, x2, v2 = list(map(int, input().strip().split(' ')))
    result = kangaroo(x1, v1, x2, v2)
    print(result)