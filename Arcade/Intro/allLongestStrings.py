# Name: allLongestStrings.py
# Author: Robin Goyal
# Last-Modified: June 21, 2017
# Purpose: Return all longest strings in the array

def allLongestStrings(inputArray):

    # Dictionary to hold length as key and strings as values
    strings = dict()

    for i in inputArray:
        if len(i) in strings:
            strings[len(i)].append(i)
        else:
            strings[len(i)] = [i]

    return strings[max(strings.keys())]