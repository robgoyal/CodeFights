# Name: sockMerchant.py
# Author: Robin Goyal
# Last-Modified: October 25, 2017
# Purpose: Calculate the number of pairs of socks that can be sold so
#          long as there are matching socks

def sockMerchant(n, arr):

    # Store number of socks for each color
    socks = {}

    for color in arr:

        # Update number of socks of each color by 1
        if color in socks:
            socks[color] += 1

        # Initialize color key
        else:
            socks[color] = 1

    # Count the total number of valid pairs from all colors
    pairs = 0
    for color in socks:

        # Ignore single sock pairs
        pairs += socks[color] // 2

    return pairs