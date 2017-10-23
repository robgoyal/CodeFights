# Name: miniMaxSum.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Determine the minimum and maximum sums for each set of
#          4 integers in a 5 integer array

def miniMaxSum(arr):

    # Find the maximum possible sum of array
    max_sum = sum(arr)
    sums = []

    # Determine sum of 4 elements by subtracting max from current element
    for i in range(len(arr)):
        sums.append(max_sum - arr[i])

    print("{} {}".format(min(sums), max(sums)))