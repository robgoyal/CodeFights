# Name: missingNumberFrom1To10.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Find the number missing in the order of 1 to 10
# Note: Found other solutions where the sum of 1 to 10 minus the sum of the list
#       returned the missing number

def find_missing_number(list_numbers):

    # Check if the list from 1 to 10 if equal to value in list parameter
    for i in range(1, len(list_numbers) + 1):
        if list_numbers[i-1] != i:
            return i