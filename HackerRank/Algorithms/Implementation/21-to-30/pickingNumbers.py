# Name: pickingNumbers.py
# Author: Robin Goyal
# Last-Modified: December 1, 2017
# Purpose: Return number of ints where the absolute difference between
#          all elements is less than or equal to 1
# Note: Hint read to reach this oslution


def pickingNumbers(arr):
    '''
    arr -> list: max element value in array is 100
    return -> int: number of elements where difference between elements is <= 1
    '''

    # Create table to
    # Range of possible values in arr is 0 < arr[i] <= 100
    freq_table = [0] * 99
    for value in arr:
        freq_table[value - 1] += 1

    max_set = 0

    # Only two consecutive elements in freq_table will have difference of 1
    for i in range(len(freq_table) - 1):
        if (freq_table[i] + freq_table[i + 1]) > max_set:
            max_set = freq_table[i] + freq_table[i + 1]

    return max_set


def main():
    a = [int(a_temp) for a_temp in input().strip().split()]

    result = pickingNumbers(a)
    print(result)


if __name__ == "__main__":
    main()
