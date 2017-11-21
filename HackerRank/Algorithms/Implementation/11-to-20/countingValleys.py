# Name: countingValleys.py
# Author: Robin Goyal
# Last-Modified: November 20, 2017
# Purpose: Count the number of valleys Gary travels through


def countingValleys(steps):
    '''
    steps: string containing U or D:
            - U: 1 step up
            - D: 1 step down

    return: number of valleys travelled:
            - valley is a sequence of steps which go below sea level
              and back to sea level
    '''

    height, start, valleys = 0, 0, 0

    for i in range(len(steps)):

        # Increment or Decrement height depending on step
        if steps[i] == 'U':
            height += 1
        else:
            height -= 1

        # If Gary has returned to sea level
        if height == 0:

            # Check if Gary stepped below sea level in range
            if steps.index('D', start, i + 1) < steps.index('U', start, i + 1):
                valleys += 1
            start = i + 1

    return valleys


def main():

    n = int(input().strip())
    steps = input().strip()

    result = countingValleys(steps)
    print(result)
