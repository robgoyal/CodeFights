# Name: designerPDFViewer.py
# Author: Robin Goyal
# Last-Modified: November 22, 2017
# Purpose: Find the area for a highlighted word


def designerPDFViewer(heights, word):
    '''
    Calculate the area of a word which will be highlighted. The width of
    a single letter is 1 mm and the height for each letter is located in the
    heights input

    heights: area of heights for each lowercase letter in the alphabet
    word: string of lowercase letters

    return: int regarding the area of the word
    '''

    max_letter_height = 0

    for letter in word:

        # Check if height of current letter is greater than max height
        if heights[ord(letter) - 97] > max_letter_height:
            max_letter_height = heights[ord(letter) - 97]

    area = max_letter_height * len(word)
    return area


def main():

    h = list(map(int, input().strip().split(' ')))
    word = input().strip()

    result = designerPDFViewer(h, word)
    print(result)
