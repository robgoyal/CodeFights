# Name: repeatedElementsInArray.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Return all the duplicate elements in an array
# Example: [1, 2, 4, 7, 1, 2] -> [1, 2]
# Note: O(nlogn) solution from sorted function call

def duplicate_items(list_numbers):

    duplicates = []
    sorted_list = sorted(list_numbers)

    # Iterate through sorted list and check if there
    # are similar elements in consecutive order
    for i in range(len(sorted_list) - 1):
        if sorted_list[i+1] == sorted_list[i]:
            duplicates.append(sorted_list[i])

    # Turning the list into a set removes all elements which had occurrences 
    # greater than 3 in the original list
    return list(set(duplicates))