# Name: arrayMaxConsecutiveSum.py
# Author: Robin Goyal
# Last-Modified: July 18, 2017
# Purpose: Find the maximum sum of k consecutive elements in an array of ints
# Note: This algorithm took a long time to understand and took a lot of research
#       but it got to an O(n) operation

def arrayMaxConsecutiveSum(arr, k):

    # Initialize with sum of first k elements
    sums = [sum(arr[0:k])]

    for i in range(len(arr) - k):

        # Add the (k+i)th element and remove the ith element
        sums.append(sums[i] + arr[i+k] - arr[i])

    # Get max of list
    return max(sums)