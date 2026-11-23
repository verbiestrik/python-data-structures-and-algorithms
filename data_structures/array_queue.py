"""
Array-based queue implementation using a circular array.

Problem:
    Implement a FIFO (First-In, First-Out) queue using a circular array.
    The queue must support adding elements at the rear and removing elements
    from the front, while using a dynamically resizing array to accommodate
    an arbitrary number of elements.

Approach:
    The queue stores elements in a Python list and uses three attributes:
        - _queue_data: The underlying array.
        - _size: The number of elements currently stored.
        - _front: The index of the first element.

    Circular indexing allows the queue to reuse positions freed by dequeue
    operations without shifting existing elements. When the array becomes
    full, its capacity is doubled and the elements are copied into a new
    array in their logical FIFO order. The front index is then reset to zero.

Complexity:
    Let n be the number of elements and C the current array capacity.

    - __len__: O(1)
    - is_empty: O(1)
    - first: O(1)
    - dequeue: O(1)
    - enqueue: O(1) amortized; O(n) when resizing is required.
    - _resize: O(n)
    - Space: O(C), with O(n) space for stored elements.

Alternatives:
    - collections.deque provides efficient O(1) append and pop operations
      at both ends and is generally preferable for production queue usage.
    - queue.Queue provides a thread-safe queue with synchronization support.
    - A regular Python list supports append(), but using pop(0) for
      dequeueing requires O(n) time because the remaining elements shift.

    This implementation provides a practical exercise in circular indexing,
    dynamic arrays, and amortized time complexity.
"""

from typing import Any


class Empty(Exception):
    """Exception raised when attempting to access an empty queue."""


class ArrayQueue:
    """FIFO queue implemented using a dynamically resizing circular array."""

    def __init__(self, initial_capacity: int = 8) -> None:
        if isinstance(initial_capacity, bool) or not isinstance(initial_capacity, int):
            raise TypeError("Initial capacity must be an integer.")

        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be positive.")

        self._queue_data: list[Any] = [None] * initial_capacity
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the queue contains no elements."""
        return self._size == 0

    def first(self) -> Any:
        """Return the first element without removing it."""
        if self.is_empty():
            raise Empty("Queue is empty.")

        return self._queue_data[self._front]

    def dequeue(self) -> Any:
        """Remove and return the first element."""
        if self.is_empty():
            raise Empty("Queue is empty.")

        first_element = self._queue_data[self._front]

        # Clear the reference to allow the object to be garbage-collected.
        self._queue_data[self._front] = None

        self._size -= 1
        self._front = (self._front + 1) % len(self._queue_data)

        return first_element

    def enqueue(self, element: Any) -> None:
        """Add an element to the rear of the queue."""
        if self._size == len(self._queue_data):
            self._resize(2 * len(self._queue_data))

        # Calculate the next available position using circular indexing.
        insert_position = (
            self._front + self._size
        ) % len(self._queue_data)

        self._queue_data[insert_position] = element
        self._size += 1

    def _resize(self, capacity: int) -> None:
        """Resize the underlying array while preserving FIFO order."""
        if capacity < self._size or capacity <= 0:
            raise ValueError("Capacity must be positive and at least the queue size.")

        old_queue = self._queue_data
        old_capacity = len(old_queue)

        new_queue = [None] * capacity

        # Copy elements in their logical queue order, starting at the front.
        for i in range(self._size):
            old_index = (self._front + i) % old_capacity
            new_queue[i] = old_queue[old_index]

        self._queue_data = new_queue
        self._front = 0
