# Name: taumAndBday.py
# Author: Robin Goyal
# Last-Modified: December 8, 2017
# Purpose: Calculate the minimum cost for buying two different types of gifts


def taumAndBday(b, w, x, y, z):
    '''
    b -> int: number of black gifts to buy
    w -> int: number of white gifts to buy
    x -> int: cost of a black gift
    w -> int: cost of a white gift
    z -> int: cost of converting a black gift to white and vice-versa

    return -> int: minimum cost of buying b black gifts and w white gifts

    The minimum cost is the cost of the gift or the exchange rate
    '''

    return min(x, y + z) * b + min(y, x + z) * w


def main():
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]

        result = taumAndBday(b, w, x, y, z)
        print(result)


if __name__ == "__main__":
    main(0)
