# Name: phoneCall.py
# Author: Robin Goyal
# Last-Modified: September 28, 2017
# Purpose: Calculate the number of minutes you can use a phone call 
#          for based off of the amount of change provided
# Notes: This is a very inefficient algorithm and its brute force
#        since I just wanted to complete it

def phoneCall(min1, min2_10, min11, s):

    minutes = 0

    # Check for the 1st minute
    if s>= min1:
        s = s - min1
        minutes += 1

    # Check for minutes 2 to 10
    if s >= min2_10:
        minutes += (min(s // min2_10, 9))
        s = s - (min2_10 * 9)

    # Calculate number of remaining minutes possible
    if s>= min11:
        minutes += (s // min11)

    return minutes