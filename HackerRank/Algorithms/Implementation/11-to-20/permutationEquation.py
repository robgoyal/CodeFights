# Name: permutationEquation.py
# Author: Robin Goyal
# Last-Modified: November 16, 2017
# Purpose: Find any value of y for all values in 1 <= x <= n 
#          which satisfies p[p[y]] == x

def permutationEquation(n, p):
    ''' 
    n: size of sequence
    p: sequence of values
    
    output: Print y which satisfies p[p[y]] == x
    '''

    # Construct dictionary
    d = {p[i-1]: (p.index(i) + 1) for i in range(1, len(p) + 1)}

    for i in range(1, len(p) + 1):
        print(d[i])

def main():

    # Get inputs
    n = int(input())
    p = list(map(int, input().strip().split()))

    permutationEquation(n, p)

if __name__ == "__main__":
    main()