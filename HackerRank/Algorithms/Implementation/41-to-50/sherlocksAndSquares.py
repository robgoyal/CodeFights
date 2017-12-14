# Name: sherlocksAndSquares.py
# Author: Robin Goyal
# Last-Modified: December 14, 2017
# Purpose: Calculate the number of squares in between a range

import math


def sherlocksAndSquares(A, B):
    '''
    A -> int: start of range
    B -> int: end of range

    return -> int: number of squares in between [A, B]
    '''

    # Obtain a value whose square is greater than A
    start = math.ceil(math.sqrt(A))
    end = start

    # Increment end to test number of values which are squared are less than B
    while (end ** 2 <= B):
        end += 1

    return (end - start)


def main():
    tests = int(input().strip())

    for test in range(tests):
        A, B = [int(i) for i in input().strip().split()]

        result = sherlocksAndSquares(A, B)
        print(result)
