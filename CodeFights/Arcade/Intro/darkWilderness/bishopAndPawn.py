# Name: bishopAndPawn.py
# Author: Robin Goyal
# Last-Modified: July 21, 2017
# Purpose: Determine whether a bishop can capture a pawn in one move

def bishopAndPawn(bishop, pawn):

    # Take differences between two positions
    letter = abs(ord(bishop[0]) - ord(pawn[0]))
    number = abs(int(bishop[1]) - int(pawn[1]))

    # Position differences are not in same row or column
    # Third condition verifies they're diagonal
    return letters >= 1 and number >= 1 and letter % 2 == number % 2