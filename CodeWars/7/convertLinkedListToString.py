class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    """stringify

    Node -> str

    Produce a string representation of the linked list.

    >>> stringify(None)
    "None"
    >>> stringify(Node(1))
    "1 -> None"
    >>> stringify(Node(1, Node(2)))
    "1 -> 2 -> None"
    """

    if node == None:
        return "None"

    return str(node.data) + " -> " + stringify(node.next)