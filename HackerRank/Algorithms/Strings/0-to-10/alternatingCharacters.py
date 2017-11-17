# Name: alternatingCharacters.py
# Author: Robin Goyal
# Last-Modified: November 16, 2017
# Purpose: Calculate the number of deletions required for no consecutive characters
# Note: Not the cleanest solution

def alternatingCharacters(s):
    '''
    s: string
    return: int

    Calculate the deletions required by determining the number of consecutive
    characters in the string
    '''

    # Initialize variables
    deletions, temp = 0,  0
    current = s[0]

    for i in range(len(s)):

        # Check if character is equal to current value
        if s[i] == current:

            # Increment count indicating consecutive char
            temp += 1
        
        # Set current value to char
        else:
            current = s[i]

            # Increase delete if consecutive chars occurred
            if temp > 0:
                deletions += (temp - 1)
            temp = 1

    # Check if temp is greater than 0 in case characters at end of list 
    # were consecutive
    if temp > 0:
        deletions += (temp - 1)

    return deletions
def main():

    q = int(input().strip())

    for a0 in range(q):
        s = input().strip()
        result = alternatingCharacters(s)
        print(result)

if __name__ == "__main__":
    main()