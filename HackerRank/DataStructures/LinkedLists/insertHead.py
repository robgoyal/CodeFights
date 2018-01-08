# Name: insertHead.py
# Author: Robin Goyal
# Last-Modified: January 8, 2018
# Purpose: Insert node at the beginning of the linked list


def Insert(head, data):
    '''
    head -> pointer: pointer to first node in linked list
    data -> data to store in new node

    return -> pointer: pointer to head in linked list

    Class definition for Node:
    class Node(object):
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next = next_node
    '''

    if head is None:
        head = Node(data)
    else:
        head = Node(data, head)

    return head
