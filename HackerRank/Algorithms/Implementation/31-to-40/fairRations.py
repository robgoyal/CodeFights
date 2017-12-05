# Name: fairRations.py
# Author: Robin Goyal
# Last-Modified: December 5, 2017
# Purpose: Calculate the number of loaves to distribute so everyone has even loaves


def fairRations(N, B):
    '''
    N -> int: number of subjects in bread line
    B -> list: number of loaves for each subject

    return -> int: number of loaves distributed

    Each subject must have an even number of loaves but distributing a loaf of
    bread to subject i in array means you must distribute a loaf to subject
    i+1 or subject i-1
    '''

    loaves = 0
    for i in range(N - 1):

        # Provide loaf to subject i and i + 1 if subject i has odd number
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            loaves += 2

    # Check if final subject has an even number of loaves
    if B[N - 1] % 2 == 0:
        return loaves

    return "NO"


def main():
    N = int(input().strip())
    B = [int(B_temp) for B_temp in input().strip().split(' ')]

    result = fairRations(N, B)
    print(result)


if __name__ == "__main__":
    main()
