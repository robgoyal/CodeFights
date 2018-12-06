class Node(object):
    """Node

    Implement the Node for a doubly linked list.
    """

    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.prev = previous
        self.next = succeeding


class LinkedList(object):
    """LinkedList

    Implement a doubly linked list.
    """

    def __init__(self):
        self.head = None
        self.tail = self.head

    def push(self, value):
        """push

        LinkedList, any -> None

        Add a Node with value to the end of the linked list.

        >>> lst = LinkedList()
        >>> lst.push(5)
        >>> lst.push(10)
        """

        new = Node(value, succeeding=None, previous=self.tail)
        if self.head is None:
            self.head = new
        else:
            new.prev.next = new
        self.tail = new

    def pop(self):
        """pop

        LinkedList -> any

        Remove and return the last element in the linked list.
        Assumptions: Linked list is not empty

        >>> lst = LinkedList()
        >>> lst.push(5)
        >>> lst.unshift(10)
        >>> lst.pop()
        5
        """

        popped = self.tail.value

        if not self.tail.prev:
            self.tail = None
            self.head = self.tail
        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None

        return popped

    def shift(self):
        """shift

        LinkedList -> any

        Remove and return the first element in the linked list.
        Assumptions: Linked list is not empty

        >>> lst = LinkedList()
        >>> lst.push(5)
        >>> lst.unshift(10)
        >>> lst.shift()
        10
        """

        shifted = self.head.value

        if not self.head.next:
            self.head = None
            self.tail = self.head
        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None

        return shifted

    def unshift(self, value):
        """unshift

        LinkedList, any -> None

        Add a Node with value to the front of the list.

        >>> lst = LinkedList()
        >>> lst.unshift(10)
        """

        new = Node(value, succeeding=self.head, previous=None)
        if self.head is None:
            self.tail = new
        else:
            new.next.prev = new
        self.head = new

    def __len__(self):
        """__len__

        LinkedList -> int

        Return the number of elements in the linked list.

        >>> lst = LinkedList()
        >>> lst.push(5)
        >>> lst.unshift(25)
        >>> len(lst)
        2
        """

        counter = 0
        trav = self.head

        while trav:
            trav = trav.next
            counter += 1

        return counter

    def __iter__(self):
        self.start = self.head
        return self

    def __next__(self):
        current = self.start
        if current:
            self.start = current.next
            return current.value
        else:
            raise StopIteration