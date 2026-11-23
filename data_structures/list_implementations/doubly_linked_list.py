"""
Doubly linked list implementation using sentinel nodes.

Problem:
    Implement the underlying structure of a doubly linked list, where each
    node maintains references to both its predecessor and successor.
    Support inserting a node between two existing nodes and deleting a
    specified node.

Approach:
    The list uses two sentinel nodes:
        - _header: Sentinel marking the beginning of the list.
        - _trailer: Sentinel marking the end of the list.

    Each node stores:
        - _element: The value stored in the node.
        - _previous: A reference to the preceding node.
        - _next: A reference to the following node.

    The sentinel nodes eliminate the need for special cases when inserting
    or deleting nodes at the boundaries of the list.

    insert_between() creates a new node between two adjacent nodes and
    updates their references.

    delete_node() removes a specified node by reconnecting its predecessor
    and successor. The removed node's references are cleared afterwards.

    The nested _Node class uses __slots__ to reduce per-node memory overhead
    by avoiding the creation of a separate instance __dict__.

Complexity:
    Let n be the number of elements in the list.

    - __len__: O(1)
    - is_empty: O(1)
    - insert_between: O(1)
    - delete_node: O(1), assuming the supplied node belongs to this list.
    - Space: O(n), with two additional sentinel nodes.

Alternatives:
    - collections.deque provides efficient O(1) insertion and removal at
      both ends and is generally preferable for production use when a full
      linked-list implementation is unnecessary.
    - A regular Python list supports efficient insertion and removal at
      the end, but operations at the beginning require O(n) time.

    This implementation provides a practical exercise in doubly linked
    lists, sentinel nodes, and pointer manipulation.
"""

from typing import Any


class DoublyLinkedList:
    """Doubly linked list implemented using sentinel nodes."""

    class _Node:
        """Node storing an element and references to its neighbours."""

        __slots__ = "_element", "_previous", "_next"

        def __init__(self, element: Any, previous, next_node) -> None:
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

    def insert_between(self, element: Any, predecessor: _Node, successor: _Node) -> _Node:
        """Insert an element between two adjacent nodes and return its node."""
        if (
            predecessor._next is not successor
            or successor._previous is not predecessor
        ):
            raise ValueError("Predecessor and successor must be adjacent nodes.")

        new_node = self._Node(element, predecessor, successor)

        predecessor._next = new_node
        successor._previous = new_node

        self._size += 1

        return new_node

    def delete_node(self, node: _Node) -> Any:
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

        # Clear references to detach the removed node completely.
        node._previous = None
        node._next = None
        node._element = None

        return element
