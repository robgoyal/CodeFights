# Name: findDigits.py
# Author: Robin Goyal
# Last-Modified: November 25, 2017
# Purpose: Calculate the number of times an int is divisible by its digits


def findDigits(n):
    '''
    n -> int
    return -> int

    Calculate the number of times n is divisible by its digits.
    Ignore 0 for ZeroDivisionError
    '''

    # Create list of digits as ints
    digits = list(map(int, str(n)))

    # Create list of 1's for number of digits which meet the criteria and return sum
    count = sum([1 for digit in digits if digit != 0 and n % digit == 0])
    return count


def main():
    tests = int(input().strip())

    for test in range(tests):
        n = int(input().strip())

        result = findDigits(n)
        print(result)


if __name__ == "__main__":
    main()
