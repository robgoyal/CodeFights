# Name: arrays.py
# Author: Robin Goyal
# Last-Modified: October 29, 2017
# Purpose: Print all integers in an array in reverse order

def arrays(arr):

    # Loop through end of list to beginning of list
    for i in range(len(arr) - 1, -1, -1):

        # Add space at end
        print(arr[i], end=" ")


def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arrays(arr)