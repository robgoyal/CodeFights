# Name: birthdayBar.py
# Author: Robin Goyal
# Last-Modified: October 27, 2017
# Purpose: Determine the number of matches the chocolate bar has

def birthdayBar(pieces, bar, day, month):

    matches = 0
    
    # Iterate over subset of bar as we're viewing sections at a time
    for i in range(len(bar) - month + 1):

        # Increment matches if sum of section equals day
        if sum(bar[i : i + month]) == day:
            matches += 1

    return matches