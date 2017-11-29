# Name: jumpingOnTheClouds.py
# Author: Robin Goyal
# Last-Modified: November 28, 2017
# Purpose: Calculate the minimum number of jumps required to reach the end


def jumpingOnTheClouds(n, clouds):
    '''
    n -> int: number of clouds
    clouds -> list: 0's and 1's representing normal and thunderclouds, respectively

    return -> int: number of jumps required to jump over all the clouds

    Thunderclouds are dangerous clouds. Can jump to cloud c[i+1] or c[i+2].
    '''

    index = 0
    jumps = 0

    # Loop until we have reached end of clouds
    while (index < n - 1):

        # Catch index error meaning we have reached near the end of the clouds
        try:
            # Minimize jumps by checking if we can skip a cloud
            if clouds[index + 2] == 0:
                index += 2
            else:
                index += 1
        except IndexError:
            index += 1

        jumps += 1

    return jumps


def main():
    n = int(input().strip())
    c = [int(c_temp) for c_temp in input().strip().split(' ')]

    result = jumpingOnTheClouds(n, c)
    print(result)


if __name__ == "__main__":
    main()
