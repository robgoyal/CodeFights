# Name: insertNode.py
# Author: Robin Goyal
# Last-Modified: January 6, 2018
# Purpose: Insert a node at the end of the list


def Insert(head, data):
    '''
    head -> pointer to the head of the list
    data -> integer to store in the new node

     class Node(object):
       def __init__(self, data, node=None):
           self.data = data
           self.next = node

    '''

    temp = Node(data)

    # Linked List is empty
    if head is None:
        head = temp

    else:
        # Pointer to traverse through list
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = temp

    return head
