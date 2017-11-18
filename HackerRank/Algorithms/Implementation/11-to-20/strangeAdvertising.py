# Name: strangeAdvertising.py
# Author: Robin Goyal
# Last-Modified: November 18, 2017
# Purpose: Determine the number of likes received by a viral
#          advertising company

import math


def strangeAdvertising(n):
    '''
    n: number of days
    return: number of people who liked the advertisement over the n days
    '''

    # Initialize variables to accumulate likes
    people = 5
    likes = 0

    for i in range(n):

        # Half the people like the post and share to three friends
        people = math.floor(people / 2) * 3

        # Number of people who liked the post in the current day
        likes += (people // 3)

    return likes


def main():

    days = int(input().strip())
    result = strangeAdvertising(days)
    print(result)


if __name__ == "__main__":
    main()
