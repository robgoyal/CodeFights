# Name: chocolateFeast.py
# Author: Robin Goyal
# Last-Modified: December 6, 2017
# Purpose: Calculate the number of chocolates eaten on a trip


def chocolateFeast(n, c, m):
    '''
    n -> int: number of dollars to buy chocolate
    c -> int: cost of a single chocolate
    m -> int: minimum number of wrappers returned to gain a piece of chocolate

    return -> int: number of chocolates ate

    Initially, n / c chocolates are purchased but each chocoalate produces
    one wrapper which could be used to get more chocolates depending on the
    value of m
    '''

    chocolates = n // c
    wrappers = chocolates

    # Loop since wrappers returned for chocolates produces more wrappers
    # Minimum number of wrappers to earn chocolates is m
    while (wrappers >= m):

        # wrappers // m is the number of chocolates earned from return wrappers
        chocolates += (wrappers // m)

        # wrappers % m is in case any wrappers remained after swapping chocolates
        wrappers = wrappers // m + wrappers % m

    return chocolates


def main():
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]

        result = chocolateFeast(n, c, m)
        print(result)


if __name__ == "__main__":
    main()
