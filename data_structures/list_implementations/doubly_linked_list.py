"""
Internal doubly linked list implementation using sentinel nodes.

Problem:
    Provide the underlying structure of a doubly linked list for use by
    higher-level data structures. Each node maintains references to its
    predecessor and successor.

Approach:
    The list uses two sentinel nodes:
        - _header: Sentinel marking the beginning of the list.
        - _trailer: Sentinel marking the end of the list.

    Each node stores:
        - _element: The value stored in the node.
        - _previous: A reference to the preceding node.
        - _next: A reference to the following node.

    The sentinel nodes eliminate special cases when inserting or
    deleting nodes at the boundaries.

    The class is intended as an internal implementation template.
    Its structural operations are therefore prefixed with underscores.

    _insert_between() creates a new node between two adjacent nodes.
    _delete_node() removes a specified node by reconnecting its
    predecessor and successor. The removed node's references are
    cleared afterwards.

    The nested _Node class uses __slots__ to reduce per-node memory
    overhead.

Complexity:
    Let n be the number of elements in the list.

    - __len__: O(1)
    - is_empty: O(1)
    - _insert_between: O(1)
    - _delete_node: O(1), assuming the supplied node belongs to the list.
    - Space: O(n), with two additional sentinel nodes.

Alternatives:
    - collections.deque provides efficient O(1) insertion and removal
      at both ends.
    - A regular Python list supports efficient insertion and removal
      at the end, but operations at the beginning require O(n) time.

    This implementation provides a foundation for linked data
    structures such as positional lists.
"""

from __future__ import annotations

from typing import Any


class _DoublyLinkedList:
    """Internal doubly linked list template using sentinel nodes."""

    class _Node:
        """Node storing an element and references to its neighbours."""

        __slots__ = "_element", "_previous", "_next"

        def __init__(
            self,
            element: Any,
            previous: _DoublyLinkedList._Node | None,
            next_node: _DoublyLinkedList._Node | None,
        ) -> None:
            self._element = element
            self._previous = previous
            self._next = next_node

    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)

        self._header._next = self._trailer
        self._trailer._previous = self._header

        self._size = 0

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self) -> bool:
        """Return True if the list contains no elements."""
        return self._size == 0

    def _insert_between(
        self,
        element: Any,
        predecessor: _DoublyLinkedList._Node,
        successor: _DoublyLinkedList._Node,
    ) -> _DoublyLinkedList._Node:
        """Insert an element between two adjacent nodes and return its node."""
        if (
            predecessor._next is not successor
            or successor._previous is not predecessor
        ):
            raise ValueError(
                "Predecessor and successor must be adjacent nodes."
            )

        new_node = self._Node(element, predecessor, successor)

        predecessor._next = new_node
        successor._previous = new_node

        self._size += 1

        return new_node

    def _delete_node(self, node: _DoublyLinkedList._Node) -> Any:
        """Remove a node, reconnect its neighbours, and return its element."""
        if node is self._header or node is self._trailer:
            raise ValueError("Cannot delete a sentinel node.")

        predecessor = node._previous
        successor = node._next

        if (
            predecessor is None
            or successor is None
            or predecessor._next is not node
            or successor._previous is not node
        ):
            raise ValueError("Node is detached or not correctly linked.")

        predecessor._next = successor
        successor._previous = predecessor

        self._size -= 1

        element = node._element

        # Completely detach the removed node.
        node._previous = None
        node._next = None
        node._element = None

        return element
