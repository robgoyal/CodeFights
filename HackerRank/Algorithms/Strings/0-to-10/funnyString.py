# Name: funnyString.py
# Author: Robin Goyal
# Last-Modified: November 13, 2017
# Purpose: Determine if a string is funny 
#          Funny -> if s[i] - s[i-1] == r[i] - r[i-1] for all i from 1 to n-1
#          r -> reverse of s


def main():

    num_tests = int(input().strip())

    for test in range(num_tests):
        s = input().strip()
        result = funnyString(s)
        print(result)

def funnyString(s):
    '''
    s: string

    return: string determining if s meets condition
    '''

    # Reverse string
    r = s[::-1]

    for i in range(1, len(s)):
        # Print 'Not Funny' if condition is not met
        cond = abs(ord(s[i]) - ord(s[i-1])) == abs(ord(r[i]) - ord(r[i-1]))
        if not(cond):
            return "Not Funny"

    return "Funny"

if __name__=="__main__":
    main()