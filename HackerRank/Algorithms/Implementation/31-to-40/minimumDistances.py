# Name: minimumDistances.py
# Author: Robin Goyal
# Last-Modified: December 3, 2017
# Purpose: Calculate the minimum distance between two elements in array with same value


def minimumDistances(arr):
    '''
    arr -> list: list of integers
    return -> int: value representing minimum distance between same values,
                   -1 if no same values

    Notes: a value in the array only appears max of twice
    '''

    # Hold indices of arr values
    locations = {}

    # Hold distances between same value
    distances = []

    # Populate dictionary with indices of same key (elements in arr)
    for i in range(len(arr)):

        # Calculate distance if key already exists with first index
        if arr[i] in locations:
            distances.append(i - locations[arr[i]])

        else:
            locations[arr[i]] = i

    # Return minimum value if distances list isn't empty
    if len(distances) > 0:
        return min(distances)

    return -1


def main():
    A = [int(A_temp) for A_temp in input().strip().split(' ')]

    result = minimumDistances(A)
    print(result)


if __name__ == "__main__":
    main()
