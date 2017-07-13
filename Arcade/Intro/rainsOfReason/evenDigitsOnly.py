# Name: evenDigitsOnly.py
# Author: Robin Goyal
# Last-Modified: July 12, 2017
# Purpose: Check if all digits of an integer are even

def evenDigitsOnly(n):
    return all(i % 2 == 0 for i in [int(j) for j in str(n)])