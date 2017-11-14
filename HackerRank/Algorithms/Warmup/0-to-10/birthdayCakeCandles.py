# Name: birthdayCakeCandles.py
# Author: Robin Goyal
# Last-Modified: October 22, 2017
# Purpose: Return the number of candles on the birthday cake that
#          contain the max height

def birthdayCakeCandles(size, arr):

    # Find the maximum candle height
    max_candle_height = max(arr)

    # Find the number of candles with the max height
    return arr.count(max_candle_height)