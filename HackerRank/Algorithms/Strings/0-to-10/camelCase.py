# Name: camelCase.py
# Author: Robin Goyal
# Last-Modified: November 6, 2017
# Purpose: Count the number of words in a camel case string

def camelCase(str):

    words = 1
    for letter in str:
        if letter.isupper():
            words += 1

    return words