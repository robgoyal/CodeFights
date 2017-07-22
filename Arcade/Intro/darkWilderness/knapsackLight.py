# Name: knapsackLight.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: Check the total weight your knapsack can hold from 
#          the weight of two different items
# Note: Forced solution

def knapsackLight(value1, weight1, value2, weight2, maxW):

    if (weight1 + weight2) <= maxW:
        return value1 + value2
    elif weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    elif weight1 <= maxW and weight2 > maxW:
        return value1
    elif weight2 <= maxW and weight1 > maxW:
        return value2
    else:
        return 0