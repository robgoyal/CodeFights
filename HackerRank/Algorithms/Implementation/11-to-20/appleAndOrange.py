# Name: appleAndOrange.py
# Author: Robin Goyal
# Last-Modified: November 12, 2017
# Purpose: Check the number of apples and oranges that hit Sam's tree


def main():

    s, t = list(map(int, input().strip().split(' ')))
    a, b = list(map(int, input().strip().split(' ')))

    # Pointless line but the challenge included it
    m, n = list(map(int, input().strip().split(' ')))

    apples_dist = list(map(int, input().strip().split(' ')))
    oranges_dist = list(map(int, input().strip().split(' ')))

    print(num_hits(s, t, a, apples_dist))
    print(num_hits(s, t, b, oranges_dist))


def num_hits(start, end, tree_dist, fruit_dists):
    '''
    start: starting location of house
    end: ending location of house
    tree_dist: location of fruit tree
    fruit_dists: locations of fallen fruit relative to tree_dist

    output: count of the number of fruits that hit the house
    '''

    count_hits = 0

    for loc in fruit_dists:

        # Check if fallen fruit is within the range of the house location
        if start <= (loc + tree_dist) <= end:
            count_hits += 1

    return count_hits


main()
