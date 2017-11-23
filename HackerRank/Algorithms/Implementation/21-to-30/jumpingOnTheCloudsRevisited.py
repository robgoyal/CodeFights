# Name: jumpingOnTheCloudsRevisited.py
# Author: Robin Goyal
# Last-Modified: November 23, 2017
# Purpose: Calculate the remaining energy level after jumping over clouds


def jumpingOnTheCloudsRevisited(n, k, clouds):
    '''
    n -> int: number of clouds
    k -> int: jump size
    clouds -> list: clouds of value 0 or 1

    return -> int: remaining energy level

    Calculate the remaining energy level, starting from 100.
    If the cloud landed is a 1, decrease by 3 energy,
    Else, decrease by 1 energy
    '''

    energy = 100

    for i in range(0, n, k):
        if clouds[i] == 1:
            energy -= 3
        else:
            energy -= 1

    return energy


def main():
    n, k = list(map(int, input().strip().split(' ')))
    clouds = [int(c_temp) for c_temp in input().strip().split(' ')]

    result = jumpingOnTheCloudsRevisited(n, k, clouds)
    print(result)
