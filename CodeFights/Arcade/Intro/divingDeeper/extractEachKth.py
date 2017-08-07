# Name: extractEachKth.py
# Author: Robin Goyal
# Last-Modified: July 18, 2017
# Purpose: Remove each kth element from array of integers

def extractEachKth(arr, k):
    return [arr[i] for i in range(len(arr)) if (i + 1) % k != 0]