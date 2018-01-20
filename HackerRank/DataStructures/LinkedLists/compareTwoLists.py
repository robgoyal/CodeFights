# Name: compareTwoLists.py
# Author: Robin Goyal
# Last-Modified: January 19, 2018
# Purpose: Compare two linked lists


def CompareLists(headA, headB):
    '''
    (Node, Node) -> int

    Compare two linked lists by traversing through the head
    pointers, headA and headB. Return 0 if they are not the same
    and return 1 if they are the same.

    Examples:
    - headA -> 1 -> None, headB -> 1 -> None ===> 1
    - headA -> 0 -> 2 -> None, headB -> 0 -> None ===> 0
    '''

    # Create traversal pointers for the head pointers
    currentA = headA
    currentB = headB

    # Loop until either traversal pointer reaches end
    while currentA and currentB:
        if currentA.data != currentB.data:
            return 0

        currentA = currentA.next
        currentB = currentB.next

    # Check if either pointer didn't reach end
    if currentA != currentB:
        return 0

    return 1
