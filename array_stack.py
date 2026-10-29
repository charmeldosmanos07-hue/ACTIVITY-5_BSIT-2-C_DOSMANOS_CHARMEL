class ArrayStack:
    """A stack implemented with a fixed-size array."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        """Add an item to the top of the stack."""
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack.")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot peek at an empty stack.")
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def __str__(self):
        return f"ArrayStack(bottom -> top): {self.items[:self.top + 1]} (capacity={self.capacity})"
