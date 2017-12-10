# Name: manasaAndStones.py
# Author: Robin Goyal
# Last-Modified: December 10, 2017
# Purpose: Calculate the final possible values of a stone
# Note: Original solution iterated over all possible permutations
#       and used bitwise operations to calculate possible final
#       values. This solution was adapted from discussion in forum


def manasaAndStones(n, a, b):
    '''
    n -> int: number of stones
    a -> int: possible difference between two stones
    b -> int: possible difference between two stones
    return -> list: possible values for final stone in sorted order

    If the first stone has a value of 0, calculate the unique values
    for the final stone. If n = 3, the possible unique values are:
        - 0 + a + a
        - 0 + a + b
        - 0 + b + b

    If a != b and a < b, this will start with the minimum values for the final
    stone and grow. As we decrease a, we increase b
    '''

    stones = []

    # Only one possible final value if a == b
    if a == b:
        return [(n - 1) * a]
    else:
        for i in range(n):
            stones.append((n - 1 - i) * min(a, b) + i * max(a, b))

    return stones


def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())

        res = manasaAndStones(n, a, b)
        for stone in res:
            print(stone, end=" ")
        print()


if __name__ == "__main__":
    main()
