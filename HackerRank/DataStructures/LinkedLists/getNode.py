# Name: getNode.py
# Author: Robin Goyal
# Last-Modified: January 17, 2018
# Purpose: Return the node at a position within the list


def GetNode(head, position):
    '''
    (Node, integer) -> integer

    Return the data at position from the tail of the linked list
    which is pointed to by head.

    Examples:
        - GetNode(head, 1)
          head = 5 -> 2 -> 1 -> None ===> 2
    '''

    # Store data in all nodes of linked list
    values = []

    current = head
    while current is not None:
        values.append(current.data)
        current = current.next

    # Access element at position by -ve indexing
    return values[-1 - position]
