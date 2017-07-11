# Name: alternatingSums.py
# Author: Robin Goyal
# Last-Modified: June 22, 2017
# Purpose: Return an array of two integers where each element
#          is the sum of the weights of each team. Every alternating
#          index in input array is a member of the same team

def alternatingSums(a):

    weights = [0, 0]

    for i in range(len(a)):
        weights[i % 2] += a[i]

    return weights