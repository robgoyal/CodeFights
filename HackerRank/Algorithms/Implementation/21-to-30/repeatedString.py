# Name: repeatedString.py
# Author: Robin Goyal
# Last-Modified: November 27, 2017
# Purpose: Return the number of a's in the first n letters of an
#          infinitely repeating string


def repeatedString(s, n):
    '''
    s -> string: infinitely repeating string
    n -> int: number of letters viewed of infinite string

    return -> int: number of a's in first n letters of s
    '''

    # Mathematical equation to count number of a's
    count_a = s.count('a') * (n // len(s)) + s.count('a', 0, n % len(s))
    return count_a


def main():
    s = input().strip()
    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)


if __name__ == "__main__":
    main()
