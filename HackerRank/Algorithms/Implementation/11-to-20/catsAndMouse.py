# Name: catsAndMouse.py
# Author: Robin Goyal
# Last-Modified: November 17, 2017
# Purpose: Determine which cat will reach the mouse first

def catAndMouse(a, b, c):
    '''
    a: position of cat A
    b: position of cat B
    c: position of mouse C

    result: "Cat A" if cat A reaches mouse first
            "Cat B" if cat B reaches mouse first
            "Mouse C" if both reach at the same time
    '''

    # Check for absolute locations in case mouse is in between the cats
    if abs(a - c) < abs(b - c):
        print("Cat A")
    elif abs(a - c) > abs(b - c):
        print("Cat B")
    else:
        print("Mouse C")

def main():

    q = int(input().strip())

    for a0 in range(q):
        x, y, z = list(map(int, input().strip().split(' ')))

        result = catAndMouse(x, y, z)
        print(result)


if __name__ == "__main__":
    main()