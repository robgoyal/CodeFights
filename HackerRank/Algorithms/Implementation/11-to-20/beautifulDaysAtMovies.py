# Name: beautifulDaysAtMovies.py
# Author: Robin Goyal
# Last-Modified: November 14, 2017
# Purpose: Calculate the number of beautiful days that occur in a range
#          beautiful day -> if the absolute value of the day minus reverse of day
#                           is divisible by another integer


def main():

    i, j, k = map(int, input().strip().split())
    result = beautiful(i, j, k)
    print(result)


def beautiful(i, j, k):
    '''
    i: start of possible day to go to the movie
    j: end of days to go to the movies
    k: integer to divide by

    return: number of beautiful days
    '''

    beautiful_days = 0

    for day in range(i, j + 1):

        # Check if day is beautiful
        if abs(day - int(str(day)[::-1])) % k == 0:
            beautiful_days += 1

    return beautiful_days


if __name__ == "__main__":
    main()
