"""
Abstract base class representing a binary tree data structure.

A binary tree is a tree in which each position has at most two children:
a left child and a right child. Each position can therefore have zero,
one, or two children.

Approach
--------
BinaryTree extends the general Tree abstract class and introduces
two additional abstract operations:

- left(position): Return the left child of a position.
- right(position): Return the right child of a position.

Two operations are implemented directly:

- sibling(position): Return the sibling of a position, if one exists.
- children(position): Return an iterator over the existing children,
  visiting the left child before the right child.

All other tree operations are inherited from Tree.

Complexity
----------
Assuming constant-time parent, left, right and position equality
operations:

- left(position): Depends on the concrete implementation.
- right(position): Depends on the concrete implementation.
- sibling(position): O(1) time and O(1) auxiliary space.
- children(position): O(1) time and O(1) auxiliary space, since a
  binary tree position can have at most two children.

Python alternatives
-------------------
The abc module provides abstractmethod to enforce the implementation
of left() and right() in concrete subclasses.

The yield keyword provides a memory-efficient way to iterate over
the children without constructing an intermediate list.
"""

from abc import abstractmethod
from collections.abc import Iterator

from data_structures.trees.tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree."""

    @abstractmethod
    def left(self, position: Tree.Position) -> Tree.Position | None:
        """Return the left child of a position, or None if absent."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    @abstractmethod
    def right(self, position: Tree.Position) -> Tree.Position | None:
        """Return the right child of a position, or None if absent."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    def sibling(self, position: Tree.Position) -> Tree.Position | None:
        """Return the sibling of a position, or None if absent."""
        parent_position = self.parent(position)

        if parent_position is None:
            return None

        if position == self.left(parent_position):
            return self.right(parent_position)

        return self.left(parent_position)

    def children(self, position: Tree.Position) -> Iterator[Tree.Position]:
        """Yield the existing children, left child before right child."""
        left_child = self.left(position)

        if left_child is not None:
            yield left_child

        right_child = self.right(position)

        if right_child is not None:
            yield right_child
