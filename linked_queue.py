class _Node:
    """One node in a singly linked queue."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """A FIFO queue using head and tail references."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        """Add an item at the tail in O(1) time."""
        node = _Node(item)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        """Remove and return the item at the head."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return item

    def peek_front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot peek at an empty queue.")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def __str__(self):
        values, node = [], self.head
        while node is not None:
            values.append(node.data)
            node = node.next
        return f"LinkedQueue(front -> rear): {values}"
