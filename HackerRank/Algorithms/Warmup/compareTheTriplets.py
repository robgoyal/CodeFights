# Name: compareTheTriplets.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Compare the points Alice and Bob have and print the number
#          of times either has beat the other in points

def compareTheTriplets(A, B):

    # Calculate points each has earned over the other
    wins_A = sum(list(A[i] > B[i] for i in range(len(arr))))
    wins_B = sum(list(B[i] > A[i] for i in range(len(arr))))

    print("{} {}".format(wins_A, wins_B))