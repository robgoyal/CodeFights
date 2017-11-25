# Name: twoCharacters.py
# Author: Robin Goyal
# Last-Modified: November 25, 2017
# Purpose: Return length of string with two alternating characters


def isValidString(copy):
    '''
    copy -> string
    return -> boolean

    Test to see if copy consists of alternating characters only
    '''

    for i in range(len(copy) - 1):
        if copy[i] == copy[i + 1]:
            return False

    return True


def twoCharacters(s):
    '''
    s -> string
    return -> int

    Delete all occurrences of letters to test if string
    contains two distinct alternating characters. Return max string
    length which meets the condition
    '''

    # Initialize with 0 to account for zero valid strings
    valid_strings = [0]
    unique = list(set(s))

    # Account for all permutations with only viewing two chars at a time
    for i in unique:
        for j in unique:

            # Don't view the same characters
            if i != j:

                # Modify copy of string
                copy = s[:]
                for k in unique:

                    # Only replace characters that aren't i or j
                    if i != k and j != k:
                        copy = copy.replace(k, '')

                # Append length of copy if valid string
                if (isValidString(copy)):
                    valid_strings.append(len(copy))

    return max(valid_strings)


def main():
    s = input().strip()

    result = twoCharacters(s)
    print(result)


if __name__ == "__main__":
    main()
