# Name: circleOfNumbers.py
# Author: Robin Goyal
# Last-Modified: July 13, 2017
# Purpose: Given a circular radius n and an input number,
#          find the number which is opposite the input number

def circleOfNumbers(n, firstNumber):
    return (firstNumber + n / 2) % n