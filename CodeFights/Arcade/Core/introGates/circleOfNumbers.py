# Name: circleOfNumbers.py
# Author: Robin Goyal
# Last-Modified: May 15, 2017
# Purpose: For a circle of size n, return the number
#          that is opposite firstNumber

def circleOfNumbers(n, firstNumber):
    return (firstNumber + n / 2) % n