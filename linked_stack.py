class _Node:
    """One node in a singly linked stack."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """A stack whose top is the head of a linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        """Add an item at the head in O(1) time."""
        node = _Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        """Remove and return the head item."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def peek(self):
        """Return the head item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot peek at an empty stack.")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def __str__(self):
        values, node = [], self.head
        while node is not None:
            values.append(node.data)
            node = node.next
        return f"LinkedStack(top -> bottom): {values}"
