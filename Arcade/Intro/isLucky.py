# Name: isLucky.py
# Author: Robin Goyal
# Last-Modified: June 21, 2017
# Purpose: Return true if the sum of the left half of digits
#          equals the right half of digits

def isLucky(n):
    
    # Split number into digits
    digits = [int(n) for n in str(n)]

    return sum(digits[:len(digits)/2]) == sum(digits[len(digits)/2:]):
    