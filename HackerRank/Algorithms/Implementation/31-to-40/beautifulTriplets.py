# Name: beautifulTriplets.py
# Author: Robin Goyal
# Last-Modified: December 2, 2017
# Purpose: Calculate the number of beautiful triplets in the array


def beautifulTriplets(d, arr):
    '''
    d -> int: difference to look for in value
    arr -> list: increasing sequence of integers
    return -> int: number of beautiful triplets

    A beautiful triplet exists if arr[k] - arr[j] = d,
    arr[j] - arr[i] = d, and k > j > i
    '''

    triplet_dict = {}

    for elem in arr:

        # Increment elem - d in dict
        if (elem - d) in triplet_dict:
            triplet_dict[elem - d] += 1

        # Increment elem - 2d in dict
        if (elem - 2 * d) in triplet_dict:
            triplet_dict[elem - 2 * d] += 1

        triplet_dict[elem] = 1

    return list(triplet_dict.values()).count(3)


def main():
    n, d = [int(i) for i in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]

    result = beautifulTriplets(d, arr)
    print(result)


if __name__ == "__main__":
    main()
