# Name: marsExploration.py
# Author: Robin Goyal
# Last-Modified: November 6, 2017
# Purpose: Determine the number of changed characters from a repeated SOS string

def marsExploration(inp):

    diffs = 0

    for i in range(len(inp) // 3):

        # Count the number of diffs in each 3 character substring
        if inp[3*i] != "S":
            diffs += 1
        if inp[3*i + 1] != "O":
            diffs += 1
        if inp[3*i + 2] != "S":
            diffs += 1

    return diffs