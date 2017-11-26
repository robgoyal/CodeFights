# Name: extraLongFactorials.py
# Author: Robin Goyal
# Last-Modified: November 26, 2017
# Purpose: Return the factorial of a number


def factorial(n):
    '''
    n -> int:
    return -> int: 1 if n == 1, else n * factorial of n-1
    '''

    if n == 1:
        return 1

    return n * factorial(n - 1)


def main():
    n = int(input().strip())
    result = factorial(n)
    print(result)


if __name__ == "__main__":
    main()
