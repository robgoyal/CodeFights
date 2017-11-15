# Name: beautifulBinaryString.py
# Author: Robin Goyal
# Last-Modified: November 14, 2017
# Purpose: Calculate the number of changes required for a binary string to not
#          include the pattern '010'

def main():

    n = int(input().strip())
    B = input().strip()
    result = minSteps(n, B)
    print(result)

def minSteps(n, B):
    '''
    n: length of string
    B: binary string 

    return: number of changes to make it not contain '010'
    '''

    # Convert string to list for mutable capability
    s = list(B)
    changes = 0

    for i in range(len(s) - 2):

        # Convert list indexing to string
        if "".join(s[i:i+3]) == '010':

            # Bitwise not for a single value
            s[i+2] = str(not(int(s[i+2])))
            changes +=1 

    return changes

if __name__=="__main__":
    main()