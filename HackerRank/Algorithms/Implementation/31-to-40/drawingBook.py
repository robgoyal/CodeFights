# Name: drawingBook.py
# Author: Robin Goyal
# Last-Modified: December 7, 2017
# Purpose: Calculate the minimum number of page turns to reach a specific page


def drawingBook(n, p):
    '''
    n -> int: number of pages in book
    p -> int: page number to turn to

    return -> int: number of page flips

    Always begin turning from page 1 which is on the right side
    when the book opens
    '''

    frontTurns = p // 2

    # If number of pages is even, we have to increase page numbers by 1 for
    # accurate number of page turns
    if p % 2 == 1 and n % 2 == 0:
        backTurns = (n + 1 - p) // 2
    else:
        backTurns = (n - p) // 2

    return min(frontTurns, backTurns)


def main():
    n = int(input().strip())
    p = int(input().strip())

    result = drawingBook(n, p)
    print(result)


if __name__ == "__main__":
    main()
