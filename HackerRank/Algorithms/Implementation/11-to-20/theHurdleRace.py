# Name: theHurdleRace.py
# Author: Robin Goyal
# Last-Modified: November 19, 2017
# Purpose: Determine how many magic beverages must be drank to overcome
#          the tallest hurdles


def theHurdleRace(n, k, heights):
    '''
    Dan can jump each hurdle with a max height of k.
    If a hurdle is too tall for Dan, he must drink
    a magic beverage which increases his height by 1

    n: number of hurdles
    k: max jump height
    heights: heights of hurdles

    return: number of magic beverages Dan must drink
    '''

    max_height = max(heights)

    if k >= max_height:
        return 0

    # Find difference in heights
    return max_height - k


def main():
    n, k = list(map(int, input().strip().split(' ')))
    heights = list(map(int, input().strip().split(' ')))

    result = theHurdleRace(n, k, heights)
    print(result)
