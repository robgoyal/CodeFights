# Name: areEquallyStrong.py
# Author: Robin Goyal
# Last-Modified: July 10, 2017
# Purpose: Determine if the combined weighting capabilities of your
#          arms are equal to your friends arms

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return set([yourLeft, yourRight]) == set([friendsLeft, friendsRight])