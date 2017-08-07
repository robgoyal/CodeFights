# Name: depositProfit.py
# Author: Robin Goyal
# Last-Modified: July 13, 2017
# Purpose: Determine how long for interest to compound and
#          the initial deposit to reach the threshold value

import math

def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(float(threshold)/deposit, 1 + rate/100.0))