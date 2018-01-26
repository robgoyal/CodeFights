# Name: happyLadybugs.py
# Author: Robin Goyal
# Last-Modified: January 26, 2018
# Purpose: Determine if the ladybugs will be happy


def happy_ladybugs(board):
    '''
    (str) -> bool

    Return True if the ladybugs on the board will be happy.

    A ladybug is happy iff the ladybug to left or right of
    her is the same color ladybug.

    Rules:
        - Colors are represented by an uppercase character.
        - If spaces, represented by _ exist, a swap can be made.

    >>> happy_ladybugs("X_Y_X")
    False
    >>> happy_ladybugs("B_RRBR")
    True
    >>> happy_ladybugs("ABAB")
    False
    >>> happy_ladybugs("AAAA")
    True
    '''

    color_frequencies = {}

    # Populate dictionary with frequencies of each color
    for cell in board:
        color_frequencies[cell] = color_frequencies.get(cell, 0) + 1

    # Initialize conditionals to check if ladybugs are happy
    is_space = color_frequencies.get('_', 0) != 0
    is_single_color = False
    is_already_happy = True

    # Check if ladybugs are happy if no spaces
    if not is_space:
        for i in range(1, len(board) - 1):
            if board[i] != board[i - 1] and board[i] != board[i + 1]:
                is_already_happy = False

    # Check if no matching colors
    for color, frequency in color_frequencies.items():
        if color != '_' and frequency == 1:
            is_single_color = True

    if is_single_color or not is_already_happy:
        return False
    return True


if __name__ == "__main__":
    tests = int(input().strip())

    for test in range(tests):
        length = int(input().strip())
        board = input().strip()

        if happy_ladybugs(board):
            print("YES")
        else:
            print("NO")
