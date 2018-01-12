# Name: deleteNode.py
# Author: Robin Goyal
# Last-Modified: January 12, 2018
# Purpose: Delete a node from a linked list


def Delete(head, position):
    '''
    head -> pointer: pointer to the head of the linked list
    position -> int: position of node to delete
    return -> pointer: head of linked list

    Delete a node at the desired position.

    Examples:
        - Delete(head, 0): Empty List ===> Error
        - Delete(head, 5): 1 -> 3 -> 2 ===> Error
        - Delete(head, 1): 5 -> True -> 2.0 ===> 5 -> 2.0
        - Delete(head, 0): 1 -> 3 ===> 3
    '''

    # Empty List
    if head is None:
        print("Empty List!")

    # Point head to next element in list
    elif position == 0:
        head = head.next

    else:
        current = head
        count = 0

        while(count < position):

            # Previous pointer to remain one position behind current
            prev = current
            current = current.next

            # Position greater than number of elements in list
            if current is None:
                print("Position out of range!")
                return head

            count += 1

        # Point previous element to next element pointed by current
        prev.next = current.next

    return head
