# Name: makingAnagrams.py
# Author: Robin Goyal
# Last-Modified: November 26, 2017
# Purpose: Calculate number of deletions required to make two strings anagrams


def makingAnagrams(s1, s2):
    '''
    s1 -> string
    s2 -> string
    return -> int

    Number of deletions required to make s1 and s2 anagrams
    of each other. s1 and s2 can be of unequal length
    '''

    # Initialize arrays for frequencies of letters
    s1_freq, s2_freq = [0] * 26, [0] * 26
    deletions = 0

    # Update index of array from string character frequencies
    for char in s1:
        s1_freq[ord(char) - 97] += 1

    for char in s2:
        s2_freq[ord(char) - 97] += 1

    # Absolute difference over each index of frequency arrays is
    # number of deletions required for that character
    for i in range(len(s1_freq)):
        deletions += abs(s1_freq[i] - s2_freq[i])

    return deletions


def main():
    s1 = input().strip()
    s2 = input().strip()
    result = makingAnagrams(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
