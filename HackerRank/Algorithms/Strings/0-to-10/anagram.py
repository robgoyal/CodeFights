# Name: anagram.py
# Author: Robin Goyal
# Last-Modified: November 19, 2017
# Purpose: Calculate number of changes to make first half of string
#          an anagram of the second half


def anagram(s):
    '''
    Calculate number of changes to make first half of string
    an anagram of the second half

    s: string
    return: number of changes
    '''

    # Check if string isn't of even length
    if len(s) % 2 != 0:
        return -1

    # Initialize array to hold frequency of characters
    char_count = [0] * 26

    # Update frequency of characters for first half
    for i in range(len(s) // 2):
        char_count[ord(s[i]) - 97] += 1

    changes = 0
    for i in range(len(s) // 2):
        char_count[ord(s[-1 - i]) - 97] -= 1

        # Check if character in second half has less characters than first half of string
        if ((char_count[ord(s[-1 - i]) - 97]) < 0):
            changes += 1

    return changes


def main():
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = anagram(s)
        print(result)


if __name__ == "__main__":
    main()
