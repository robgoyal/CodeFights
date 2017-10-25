# Name: circularArrayRotation.py
# Author: Robin Goyal
# Last-Modified: October 25, 2017
# Purpose: Perform k circular array rotations and strip 

# Obtain inputs regarding size, rotations, queries and array
size, rotations, queries = list(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))

# Calculate position to flip array at after "rotations" number of rotations
pos = abs((size - rotations) % size)
arr = arr[pos:] + arr[:pos]

# Queries for array
for i in range(queries):
    index = int(input().strip())
    print(arr[index])