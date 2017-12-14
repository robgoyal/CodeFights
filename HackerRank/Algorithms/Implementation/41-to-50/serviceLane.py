# Name: serviceLane.py
# Author: Robin Goyal
# Last-Modified: December 13, 2017
# Purpose: Print the largest vehicle type that can pass through the service lane


def serviceLane(i, j, width):
    '''
    i -> int: entrance segment on highway
    j -> int: exit segment on highway
    width -> list: max width of vehicle allowed on each segment

    return -> int: width of vehicle (1, 2, or 3)

    Given i and j, return the maximum width of a vehicle allowed on a highway.
    The values are 1: bike, 2: car, 3: truck.
    '''

    return min(width[i: j + 1])


def main():
    n, t = [int(i) for i in input().strip().split()]
    width = [int(i) for i in input().strip().split()]

    for a0 in range(t):
        i, j = [int(i) for i in input().strip().split()]

        result = serviceLane(i, j, width)
        print(result)


if __name__ == "__main__":
    main()
