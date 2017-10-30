# Name: dynamicArray.py
# Author: Robin Goyal
# Last-Modified: October 30, 2017
# Purpose: Perform dynamic operations on an array 

def main():

    # Retrieve basic inputs regarding number of queries and size of sequence
    inp = list(map(int, raw_input().split()))
    arr = [[] for x in range(inp[0])]

    for i in range(inp[1]):

        # Query input
        query = list(map(int, raw_input().split()))
        
        # Different query operations
        if query[0] == 1:
            seq = (query[1] ^ lastAns) % len(arr)
            arr[seq].append(query[2])
            
        else:
            seq = (query[1] ^ lastAns) % len(arr)
            lastAns = arr[seq][query[2] % len(arr[seq])]
            print lastAns