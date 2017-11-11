# Name: pangrams.py
# Author: Robin Goyal
# Last-Modified: November 11, 2017
# Purpose: Check if a string is a pangram

def pangrams(inp):

    # Initialize array to hold all chars
    chars = []

    for char in inp:

        # Check if a character is alphabetical
        if char.isalpha():

            # Convert to lowercase character
            char = char.lower()

            if char not in chars:
                chars.append(char)

    # Test if there are 26 characters in the list
    if len(chars) == 26:
        print("pangram")
    else:
        print("not pangram")
