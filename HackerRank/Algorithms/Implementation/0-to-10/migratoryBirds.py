# Name: migratoryBirds.py
# Author: Robin Goyal
# Last-Modified: October 27, 2017
# Purpose: Return the ID of the most frequent type of birds in a flock
#          Return lowest ID if two types have highest frequencies

def migratoryBirds(size, flock):

    # Initialize array of length 'size' with 0's
    bird_count = [0] * size

    # Count frequency of each bird type
    for bird in flock:
        bird_count[bird - 1] += 1

    # Return lowest index of max frequency
    return bird_count.index(max(bird_count)) + 1