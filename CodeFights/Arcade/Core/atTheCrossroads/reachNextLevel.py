# Name: reachNextLevel.py
# Author: Robin Goyal
# Last-Modified: September 30, 2017
# Purpose: Calculate if the reward earned by killing the monster provides
#          enough experience to level up

def reachNextLevel(experience, threshold, reward):
    return (experience + reward) >= threshold