# Name: divisibleSumPairs.py
# Author: Robin Goyal
# Last-Modified: October 23, 2017
# Purpose: Return the number of pairs in the array whose sum is divisible
#          by an integer

def divisibleSumPairs(size, divisor, arr):

    # Initialize pairs counter
    pairs = 0

    # Loop through size - 1 elements (ignoring final element)
    for i in range(len(arr) - 1):

        # Loop through subset of array which doesnt include 0 to i
        for j in range(i + 1, len(arr)):

            # Check if sum of ith and jth is divisible by k
            if (arr[i] + arr[j]) % k == 0:
                pairs += 1

    return pairs