# Name: equalityInArray.py
# Author: Robin Goyal
# Last-Modified: November 29, 2017
# Purpose: Calculate minimum number of elements to remove to equalize the array


def equalityInArray(n, arr):
    '''
    n -> int: number of elements in arr
    arr -> list: list of ints

    return -> int: number of elements to delete to make array elements equal
    '''

    elem_freq = {}
    for i in arr:
        elem_freq[i] = elem_freq.get(i, 0) + 1

    return n - max(elem_freq.values())


def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    result = equalityInArray(n, arr)
    print(result)


if __name__ == "__main__":
    main()
