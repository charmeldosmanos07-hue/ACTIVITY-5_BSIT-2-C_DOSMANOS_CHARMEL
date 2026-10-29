class ArrayQueue:
    """A fixed-size circular queue implemented with an array."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        """Add an item at the rear, wrapping around when needed."""
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue.")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1

    def dequeue(self):
        """Remove and return the item at the front."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = 0
            self.rear = -1
        return item

    def peek_front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot peek at an empty queue.")
        return self.items[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def __str__(self):
        values = [self.items[(self.front + i) % self.capacity] for i in range(self.size)]
        return f"CircularArrayQueue(front -> rear): {values} (array={self.items}, capacity={self.capacity})"
