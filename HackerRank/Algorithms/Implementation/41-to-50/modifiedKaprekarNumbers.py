# Name: modifiedKaprekarNumbers.py
# Author: Robin Goyal
# Last-Modified: January 11, 2018
# Purpose: Print all the kaprekar numbers between a range


def is_kaprekar(n):
    '''
    int -> boolean

    Return a boolean indicating if the number n is a kaprekar number.
    A kaprekar number occurs when the left half plus the right half
    of the square of the number equal the original number.

    Examples:
        - is_kaprekar(45) ===> True
            45 ** 2 = 2025
            20 + 25 = 45
        - is_kaprekar(55) ===> True
            55 ** 2 = 3025
            30 + 25 = 55
        - is_kaprekar(1) ===> True
            Special case where the left half is equal to 0
            1 ** 2 = 1
            1 + 0 = 1
        - is_kaprekar(15) ===> False
            15 ** 2 = 225
            25 + 2 = 27
    '''

    len_n = len(str(n))
    sqr_n = str(n ** 2)

    # Get right half of digits equivalent to number of digits for n
    right = sqr_n[len(sqr_n) - len_n:]

    # Get remaining digits of left side
    left = sqr_n[0: len(sqr_n) - len_n]

    if right == '':
        right = 0
    if left == '':
        left = 0

    return (int(left) + int(right)) == n


def kaprekar_numbers(p, q):
    '''
    (int, int) -> list

    Return a list of all kaprekar numbers between the range of p and q

    Examples:
        - kaprekar_numbers(1, 100) ===> [1, 9, 45, 55, 99]
        - kaprekar_numbers(100, 200) ===> []
    '''

    kaprekars = []

    for i in range(p, q + 1):
        if is_kaprekar(i):
            kaprekars.append(i)

    return kaprekars


def main():
    p = int(input().strip())
    q = int(input().strip())

    result = kaprekar_numbers(p, q)

    if len(result) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
