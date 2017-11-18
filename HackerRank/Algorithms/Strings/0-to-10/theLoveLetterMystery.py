# Name: theLoveLetterMystery.py
# Author: Robin Goyal
# Last-Modified: November 18, 2017
# Purpose: Calculate the number of changes required to transform
#          a string into a palindrome

def theLoveLetterMystery(s):
    '''
    s: string
    return: changes to make s into palindrome
    '''

    changes = 0

    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:

            # Calculate the positional difference between the characters
            changes += abs(ord(s[i]) - ord(s[-1-i]))

    return changes

def main():

    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = theLoveLetterMystery(s)
        print(result)

if __name__ == "__main__":
    main()