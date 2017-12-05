# Name: lisasWorkbook.py
# Author: Robin Goyal
# Last-Modified: December 4, 2017
# Purpose: Calculate the number of special problems Lisa has in her workbook


def lisasWorkbook(n, k, t):
    '''
    n -> int: number of chapters
    k -> int: number of problems per page
    t -> list: list containing number of problems per chapter

    return -> int: number of special problems

    A problem is special if the problem number is equal to the current page number.
    Page and problems number are 1-indexed.
    '''

    pages = 1
    special = 0

    for problems in t:
        for problem in range(1, problems + 1):
            if pages == problem:
                special += 1

            if (problem % k == 0) or (problem == problems):
                pages += 1

    return special


def main():
    n, k = [int(i) for i in input().strip().split()]
    t = [int(i) for i in input().strip().split()]

    result = lisasWorkbook(n, k, t)
    print(result)


if __name__ == "__main__":
    main()
