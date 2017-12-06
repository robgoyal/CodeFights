# Name: savePrisoner.py
# Author: Robin Goyal
# Last-Modified: December 5, 2017
# Purpose: Print the ID number of the prisoner who received the poisoned sweet


def saveThePrisoner(n, m, s):
    '''
    n -> int: number of prisoners
    m -> int: number of sweets
    s -> int: ID of first prisoner to receive sweet

    return -> int: ID of prisoner to receive final sweet

    The distribution order of the sweets are (s, s+1, s+2, ... , n-1, n, 1, 2, 3, ...)
    '''
    return (m + s - 2) % n + 1


def main():
    t = int(input().strip())
    for a0 in range(t):
        n, m, s = input().strip().split(' ')
        n, m, s = [int(n), int(m), int(s)]
        result = saveThePrisoner(n, m, s)
        print(result)


if __name__ == "__main__":
    main()
