# Name: printReverse.py
# Author: Robin Goyal
# Last-Modified: January 16, 2018
# Purpose: Print the linked list elements in reverse


def ReversePrint(head):
    '''
    head -> None

    Print all of the elements pointed to by head in reverse.

    head is a pointer of type Node with the following definition:
    class Node(object):
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
    '''

    # Node values in linked list
    values = []

    # Populate values list with values in linked list
    current = head
    while current is not None:
        values.append(current.data)
        current = current.next

    # Print all elements in reverse order
    for value in values[::-1]:
        print(value)
