"""
Linked-list-based stack implementation.

Problem:
    Implement a LIFO (Last-In, First-Out) stack using a singly linked list.
    The stack must support adding elements to and removing elements from
    the top, as well as retrieving the top element without removing it.

Approach:
    The stack maintains a reference to the head of a singly linked list,
    which represents its top element. Each node stores:
        - _element: The value stored in the node.
        - _next: A reference to the next node.

    New elements are inserted at the head of the linked list. Removing an
    element simply updates the head to reference the next node. This avoids
    shifting elements and allows all fundamental stack operations to run
    in constant time.

    The nested _Node class uses __slots__ to reduce per-node memory overhead
    by avoiding the creation of a separate instance __dict__.

Complexity:
    Let n be the number of elements in the stack.

    - __len__: O(1)
    - is_empty: O(1)
    - push: O(1)
    - top: O(1)
    - pop: O(1)
    - Space: O(n), with one node allocated per element.

Alternatives:
    - A Python list supports append() and pop() at the end, both with
      amortized O(1) time complexity, and is generally preferable when
      implementing a stack for production use.
    - collections.deque provides efficient append() and pop() operations
      at either end and is another suitable alternative.

    This implementation provides a practical exercise in linked lists,
    node references, and stack operations.
"""

from typing import Any


class Empty(Exception):
    """Exception raised when attempting to access an empty stack."""


class LinkedStack:
    """LIFO stack implemented using a singly linked list."""

    class _Node:
        """Lightweight node storing an element and a reference to the next node."""

        __slots__ = "_element", "_next"

        def __init__(self, element: Any, next_node: Any) -> None:
            self._element = element
            self._next = next_node

    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the stack contains no elements."""
        return self._size == 0

    def push(self, element: Any) -> None:
        """Add an element to the top of the stack."""
        # Insert the new node at the head of the linked list.
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self) -> Any:
        """Return the top element without removing it."""
        if self.is_empty():
            raise Empty("No top element; stack is empty!")

        return self._head._element

    def pop(self) -> Any:
        """Remove and return the top element."""
        if self.is_empty():
            raise Empty("No top element; stack is empty!")

        top_element = self._head._element

        # Move the head to the next node, removing the previous head.
        self._head = self._head._next
        self._size -= 1

        return top_element
