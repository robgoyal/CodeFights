# Name: fibonacci.py
# Author: Robin Goyal
# Last-Modified: August 7, 2017
# Purpose: Calculate the nth number in the fibonacci sequence using recursion
# Note: Inefficient solution if n is too large

def fib(n):

    # The first two numbers in the fibonacci sequence are 0, 1
    if n < 2:
        return n

    else:
        return fib(n-1) + fib(n-2)