# Name: betweenTwoSets.py
# Author: Robin Goyal
# Last-Modified: November 12, 2017
# Purpose: Count the number of times a value is a multiple of all elements
#          in list A and a factor of all elements in list B

def main():

    n, m = list(map(int, input().strip().split(' ')))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    print(get_total(a, b))

def get_total(A, B):
    '''
    a: list of numbers
    b: list of numbers

    x must be a multiple of all elements in A and a factor
    of all elements in B
    
    output: return the number of x's that meet the conditions
    '''

    count_x = 0

    # Only the max value in A could be a multiple of all elements in A
    # Only the min value of B could be a factor of all elements in B
    for i in range(max(A), min(B) + 1, max(A)):

        # List of T/F values which meet the conditions
        cond_a = list(map(lambda elem: i % elem == 0, A))
        cond_b = list(map(lambda elem: elem % i == 0, B))

        # Check if any values in lists didnt meet this condition
        if not(False in cond_a or False in cond_b):
            count_x += 1

    return count_x