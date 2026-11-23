"""
Deque implementation using a doubly linked list.

Problem:
    Implement a deque (double-ended queue) supporting insertion and removal
    of elements at both the front and rear. Both ends must support constant-
    time operations.

Approach:
    The LinkedDeque class inherits from DoublyLinkedList, reusing its
    underlying doubly linked list implementation, including:
        - Sentinel nodes (_header and _trailer).
        - Node insertion through insert_between().
        - Node removal through delete_node().
        - Size tracking through __len__() and is_empty().

    The deque provides six operations:
        - first(): Returns the first element without removing it.
        - last(): Returns the last element without removing it.
        - insert_first(): Inserts an element at the front.
        - insert_last(): Inserts an element at the rear.
        - delete_first(): Removes and returns the first element.
        - delete_last(): Removes and returns the last element.

    Inheriting from DoublyLinkedList avoids duplicating the underlying
    node management and pointer manipulation logic.

Complexity:
    Let n be the number of elements in the deque.

    - __len__: O(1), inherited.
    - is_empty: O(1), inherited.
    - first: O(1).
    - last: O(1).
    - insert_first: O(1).
    - insert_last: O(1).
    - delete_first: O(1).
    - delete_last: O(1).
    - Space: O(n), inherited from the doubly linked list implementation.

Alternatives:
    - collections.deque provides an efficient, production-ready deque
      implementation with O(1) insertion and removal at both ends.
    - A regular Python list supports efficient insertion and removal at
      the rear, but operations at the front require O(n) time.

    This implementation demonstrates how inheritance and a doubly linked
    list can be combined to implement a deque efficiently.
"""

from typing import Any

from data_structures.list_implementations.doubly_linked_list import (
    DoublyLinkedList,
)


class Empty(Exception):
    """Exception raised when attempting to access an empty deque."""


class LinkedDeque(DoublyLinkedList):
    """Deque implemented using an inherited doubly linked list."""

    def first(self) -> Any:
        """Return the first element without removing it."""
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self._header._next._element

    def last(self) -> Any:
        """Return the last element without removing it."""
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self._trailer._previous._element

    def insert_first(self, element: Any) -> None:
        """Insert an element at the front of the deque."""
        self.insert_between(
            element,
            self._header,
            self._header._next,
        )

    def insert_last(self, element: Any) -> None:
        """Insert an element at the rear of the deque."""
        self.insert_between(
            element,
            self._trailer._previous,
            self._trailer,
        )

    def delete_first(self) -> Any:
        """Remove and return the first element."""
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self.delete_node(self._header._next)

    def delete_last(self) -> Any:
        """Remove and return the last element."""
        if self.is_empty():
            raise Empty("Deque is empty.")

        return self.delete_node(self._trailer._previous)
