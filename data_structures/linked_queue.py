"""
Linked-list-based queue implementation.

Problem:
    Implement a FIFO (First-In, First-Out) queue using a singly linked list.
    The queue must support adding elements at the rear and removing elements
    from the front, as well as retrieving the first element without removing it.

Approach:
    The queue maintains references to both the head and tail of a singly
    linked list, together with its current size. Each node stores:
        - _element: The value stored in the node.
        - _next: A reference to the next node.

    The head represents the front of the queue, while the tail represents
    the rear. New elements are inserted after the tail, and elements are
    removed from the head.

    Maintaining both head and tail references allows enqueue and dequeue
    operations to run in constant time without traversing the linked list.

    When the last element is removed, both head and tail are reset to None
    to ensure the empty queue maintains a consistent state.

    The nested _Node class uses __slots__ to reduce per-node memory overhead
    by avoiding the creation of a separate instance __dict__.

Complexity:
    Let n be the number of elements in the queue.

    - __len__: O(1)
    - is_empty: O(1)
    - first: O(1)
    - enqueue: O(1)
    - dequeue: O(1)
    - Space: O(n), with one node allocated per element.

Alternatives:
    - collections.deque provides efficient O(1) append() and popleft()
      operations and is generally preferable for production queue usage.
    - queue.Queue provides a thread-safe queue with synchronization support.

    This implementation provides a practical exercise in singly linked lists,
    node references, and FIFO queue operations.
"""

from typing import Any


class Empty(Exception):
    """Exception raised when attempting to access an empty queue."""


class LinkedQueue:
    """FIFO queue implemented using a singly linked list."""

    class _Node:
        """Lightweight node storing an element and a reference to the next node."""

        __slots__ = "_element", "_next"

        def __init__(self, element: Any, next_node: Any) -> None:
            self._element = element
            self._next = next_node

    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None

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

        return self._head._element

    def dequeue(self) -> Any:
        """Remove and return the first element."""
        if self.is_empty():
            raise Empty("Queue is empty.")

        first_element = self._head._element

        # Move the head to the next node, removing the previous head.
        self._head = self._head._next
        self._size -= 1

        # Reset the tail when the last element has been removed.
        if self.is_empty():
            self._tail = None

        return first_element

    def enqueue(self, element: Any) -> None:
        """Add an element to the rear of the queue."""
        new_node = self._Node(element, None)

        if self.is_empty():
            # The new node becomes both the head and the tail.
            self._head = new_node
        else:
            # Link the new node after the current tail.
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1
