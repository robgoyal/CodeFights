# Name: utopianTree.py
# Author: Robin Goyal
# Last-Modified: November 24, 2017
# Purpose: Calculate the height of a tree after growth cycles


def utopianTree(cycles):
    '''
    cycles: number of growth cycles for the tree
    return: height of the tree after growth cycles

    A spring cycle (odd cycle) doubles the height of the tree and
    summer cycles (even cycle) increases the height of the tree by 1
    '''

    height = 1

    for i in range(1, cycles + 1):

        # If spring cycle
        if i % 2 == 1:
            height *= 2
        else:
            height += 1

    return height


def main():

    tests = int(input().strip())

    for test in range(tests):
        cycles = int(input().strip())

        result = utopianTree(cycles)
        print(result)
