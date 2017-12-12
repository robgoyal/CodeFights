# Name: libraryFine.py
# Author: Robin Goyal
# Last-Modified: December 11, 2017
# Purpose: Calculate the fine due for returning a library book


def libraryFine(Da, Ma, Ya, De, Me, Ye):
    '''
    Da, Ma, Ya -> int, int, int: Actual date of return for the library book
    De, Me, Ye -> int, int, int: Expected date of return for the library book

    Late by a year: fixed fine of 10000
    Same year, late by months: fine of 500 * (# of late months)
    Same year, same month, few days: fine of 15 * (# of late days)
    Returned before deadline: no fine
    '''

    fine = 0

    if Ya > Ye:
        fine = 10000
    elif Ya == Ye and Ma > Me:
        fine = ((Ma - Me) * 500)
    elif Ya == Ye and Ma == Me and Ma > Me:
        fine = ((Da - De) * 15)

    return fine


def main():

    Da, Ma, Ya = [int(i) for i in input().strip().split()]
    De, Me, Ye = [int(i) for i in input().strip().split()]

    result = libraryFine(Da, Ma, Ya, De, Me, Ye)
    print(result)


if __name__ == "__main__":
    main()
