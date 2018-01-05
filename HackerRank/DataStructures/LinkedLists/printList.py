# Name: printList.py
# Author: Robin Goyal
# Last-Modified: January 5, 2018
# Purpose: Print all elements of the linked list
# Note: Node object already exists


def print_list(head):
    '''
    head -> pointer: pointer to the front of the linked list

    Print the data in each node
    '''

    # Pointer to traverse through list
    current = head

    # Traverse through list until last node is reached
    while (current is not None):
        print(current.data)
        current = current.next
