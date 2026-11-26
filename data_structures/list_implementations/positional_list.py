"""
Positional list implementation using a doubly linked list.

Problem:
    Implement a positional list in which elements are accessed through
    position objects rather than numerical indices.

    Support accessing the first and last positions, navigating between
    positions, inserting elements relative to existing positions,
    deleting positions, and replacing their elements.

Approach:
    PositionalList extends the internal _DoublyLinkedList template.

    Each Position stores:
        - _container: A reference to the positional list.
        - _node: A reference to the corresponding internal node.

    The Position class provides an abstraction over the internal nodes,
    preventing users from directly depending on the linked structure.

    _validate() checks that positions have the correct type, belong to
    the current list, and have not been invalidated by deletion.

    _make_position() converts internal nodes into Position objects.
    Sentinel nodes are never exposed as valid positions.

    Insertion operations reuse the parent's _insert_between() method,
    while deletion reuses its _delete_node() method.

Complexity:
    Let n be the number of elements in the list.

    - __len__: O(1)
    - is_empty: O(1)
    - first, last: O(1)
    - before, after: O(1)
    - _validate, _make_position: O(1)
    - add_first, add_last: O(1)
    - add_before, add_after: O(1)
    - delete, replace: O(1)
    - __iter__: O(n) time and O(1) auxiliary space.
    - Space: O(n), including one node per element.

Alternatives:
    - A Python list supports positional access through integer indices,
      but inserting or deleting elements can require O(n) time.
    - collections.deque provides efficient operations at both ends,
      but does not provide positional navigation.

    This implementation demonstrates how a positional abstraction can
    be built on top of a reusable linked-list implementation.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from data_structures.list_implementations.doubly_linked_list import (
    _DoublyLinkedList,
)


class PositionalList(_DoublyLinkedList):
    """Positional list implemented using a doubly linked list."""

    class Position:
        """Abstraction representing the location of an element."""

        def __init__(self, container: PositionalList, node: _DoublyLinkedList._Node):
            self._container = container
            self._node = node

        def element(self) -> Any:
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other_position: object) -> bool:
            """Return whether two positions refer to the same node."""
            return (
                type(self) is type(other_position)
                and self._node is other_position._node
            )

        def __ne__(self, other_position: object) -> bool:
            """Return whether two positions are different."""
            return not (self == other_position)

    def _validate(self, position: Position) -> _DoublyLinkedList._Node:
        """
        Validate a position and return its corresponding node.

        Raises:
            TypeError: If the position has an incorrect type.
            ValueError: If the position belongs to another list,
                        refers to a sentinel, or has been deleted.
        """
        if not isinstance(position, self.Position):
            raise TypeError(
                "position is not of the appropriate Position type"
            )

        if position._container is not self:
            raise ValueError("position does not belong to this container")

        node = position._node

        if (
            node is self._header
            or node is self._trailer
            or node._next is None
        ):
            raise ValueError("position is no longer valid")

        return node

    def _make_position(
        self,
        node: _DoublyLinkedList._Node | None,
    ) -> Position | None:
        """Return a Position object for a node, or None for a sentinel."""
        if (
            node is None
            or node is self._header
            or node is self._trailer
        ):
            return None

        return self.Position(self, node)

    def first(self) -> Position | None:
        """Return the first position, or None if the list is empty."""
        return self._make_position(self._header._next)

    def last(self) -> Position | None:
        """Return the last position, or None if the list is empty."""
        return self._make_position(self._trailer._previous)

    def before(self, position: Position) -> Position | None:
        """Return the position immediately before the given position."""
        node = self._validate(position)
        return self._make_position(node._previous)

    def after(self, position: Position) -> Position | None:
        """Return the position immediately after the given position."""
        node = self._validate(position)
        return self._make_position(node._next)

    def __iter__(self) -> Iterator[Any]:
        """Iterate over the elements in the list from first to last."""
        position = self.first()

        while position is not None:
            yield position.element()
            position = self.after(position)

    def _insert_between(
        self,
        element: Any,
        predecessor: _DoublyLinkedList._Node,
        successor: _DoublyLinkedList._Node,
    ) -> Position:
        """Insert an element and return its corresponding position."""
        new_node = super()._insert_between(
            element,
            predecessor,
            successor,
        )

        return self._make_position(new_node)

    def add_first(self, element: Any) -> Position:
        """Insert an element at the beginning of the list."""
        return self._insert_between(
            element,
            self._header,
            self._header._next,
        )

    def add_last(self, element: Any) -> Position:
        """Insert an element at the end of the list."""
        return self._insert_between(
            element,
            self._trailer._previous,
            self._trailer,
        )

    def add_before(self, position: Position, element: Any) -> Position:
        """Insert an element immediately before a given position."""
        original_node = self._validate(position)

        return self._insert_between(
            element,
            original_node._previous,
            original_node,
        )

    def add_after(self, position: Position, element: Any) -> Position:
        """Insert an element immediately after a given position."""
        original_node = self._validate(position)

        return self._insert_between(
            element,
            original_node,
            original_node._next,
        )

    def delete(self, position: Position) -> Any:
        """Delete a position and return its stored element."""
        original_node = self._validate(position)
        return self._delete_node(original_node)

    def replace(self, position: Position, element: Any) -> Any:
        """Replace the element at a position and return the old element."""
        original_node = self._validate(position)

        original_element = original_node._element
        original_node._element = element

        return original_element
