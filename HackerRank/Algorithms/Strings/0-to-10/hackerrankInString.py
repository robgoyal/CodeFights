# Name: hackerrankInString.py
# Author: Robin Goyal
# Last-Modified: November 17, 2017
# Purpose: Determine if 'hackerrank' is in a string in the correct order

def hackerrankInString(s):
    '''
    s: string 
    return: "YES" or "NO"

    YES if hackerrank is in s in the order of the characters
    in hackerrank
    '''

    index = 0
    string_to_match = "hackerrank"

    for char in s:

        # Only increment index if it matches in order
        if char == string_to_match[index]:
            index += 1

        # Break out if string has been matched
        if index == len(string_to_match):
            return "YES"

    return "NO"


def main():

    q = int(input().strip())

    for a0 in range(q):
        s = input().strip()

        result = hackerrankInString(s)
        print(result)

if __name__ == "__main__":
    main()