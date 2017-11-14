# Name: breakingTheRecords.py
# Author: Robin Goyal
# Last-Modified: October 25, 2017
# Purpose: Calculate the number of times Maria breaks her record for lowest
#          and highest points scored

def breakingTheRecords(scores):

    # Initialize low and high scores
    low, high = scores[0], scores[0]

    # Initialize number of times low and high scores were broken
    low_break, high_break = 0, 0

    for score in scores:

        # Update low score and count for breaking her low record
        if score < low:
            low_break += 1
            low = score

        # Update high score and count for breaking high record
        elif score > high:
            high_break += 1
            high = score

    return high_break, low_break