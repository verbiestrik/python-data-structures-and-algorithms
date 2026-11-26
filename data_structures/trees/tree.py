"""
Abstract base class representing a general tree data structure.

A tree is a hierarchical data structure consisting of nodes (positions)
connected by parent-child relationships. Each node, except the root, has
exactly one parent. A node may have zero or more children.

Approach
--------
The Tree class defines an abstract interface that concrete tree
implementations must provide:

- root(): Return the root position.
- parent(p): Return the parent of position p.
- num_children(p): Return the number of children of position p.
- children(p): Return an iterator over the children of position p.
- __len__(): Return the total number of positions in the tree.

The nested Position class defines the interface for accessing and
comparing positions. Concrete implementations must provide element()
and __eq__().

General-purpose tree operations are implemented using these fundamental
operations:

- is_root(p): Determine whether p is the root.
- is_leaf(p): Determine whether p has no children.
- is_empty(): Determine whether the tree contains any positions.
- depth(p): Calculate the distance from p to the root.
- height(p): Calculate the maximum distance from p to a leaf.

Tree traversals:
- __iter__(): Iterate over the elements in preorder.
- preorder(): Visit positions in preorder.
- postorder(): Visit positions in postorder.
- breadthfirst(): Visit positions level by level.
- positions(): Return an iterator over the positions, using preorder
  as the default traversal.

Complexity
----------
Let n denote the number of positions in the tree, h its height, and w
its maximum width (the maximum number of positions at any level).

- is_root(p): O(1), assuming constant-time root access and comparison.
- is_leaf(p): O(1), assuming constant-time child counting.
- is_empty(): O(1), assuming constant-time length retrieval.
- depth(p): O(h) time and O(1) auxiliary space.
- height(p): O(n) time and O(h) recursion-stack space.
- preorder(): O(n) time and O(h) auxiliary space.
- postorder(): O(n) time and O(h) auxiliary space.
- breadthfirst(): O(n) time and O(w) auxiliary space.
- __iter__(): O(n) time and O(h) auxiliary space.
- positions(): O(n) time for a complete traversal.

The recursive traversals use O(h) stack space. Breadth-first traversal
uses a queue to store positions that have not yet been visited.

Python alternatives
-------------------
The abc module provides ABC and abstractmethod for defining abstract
base classes.

The built-in len() function invokes __len__(), while max() determines
the height of a subtree.

The custom LinkedQueue implementation is used for breadth-first
traversal. Python's collections.deque provides an alternative with
efficient append() and popleft() operations.

The yield keyword allows traversals to produce positions lazily,
without constructing intermediate lists.

Position validation and storage are deliberately left to concrete
implementations, allowing different tree representations to reuse
this common interface.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator

from data_structures.queues.linked_queue import LinkedQueue


class Tree(ABC):
    """Abstract base class representing a general tree."""

    class Position(ABC):
        """Abstract representation of a position in a tree."""

        @abstractmethod
        def element(self) -> object:
            """Return the element stored at this position."""
            raise NotImplementedError(
                "must be implemented by the subclass"
            )

        @abstractmethod
        def __eq__(self, other: object) -> bool:
            """Return whether this position equals another position."""
            raise NotImplementedError(
                "must be implemented by the subclass"
            )

        def __ne__(self, other: object) -> bool:
            """Return whether this position differs from another."""
            return not (self == other)

    @abstractmethod
    def root(self) -> Position | None:
        """Return the root position, or None if the tree is empty."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    @abstractmethod
    def parent(self, p: Position) -> Position | None:
        """Return the parent of position p, or None if p is the root."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    @abstractmethod
    def num_children(self, p: Position) -> int:
        """Return the number of children of position p."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    @abstractmethod
    def children(self, p: Position) -> Iterator[Position]:
        """Return an iterator over the children of position p."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    @abstractmethod
    def __len__(self) -> int:
        """Return the total number of positions in the tree."""
        raise NotImplementedError(
            "must be implemented by the subclass"
        )

    def is_root(self, p: Position) -> bool:
        """Return whether position p is the root."""
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """Return whether position p has no children."""
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """Return whether the tree contains no positions."""
        return len(self) == 0

    def depth(self, p: Position) -> int:
        """
        Return the depth of position p.

        The depth is the number of edges between p and the root.
        An iterative implementation avoids recursive function calls.
        """
        depth = 0

        while not self.is_root(p):
            p = self.parent(p)
            depth += 1

        return depth

    def _height(self, p: Position) -> int:
        """Recursively calculate the height of the subtree rooted at p."""
        return max(
            (1 + self._height(child) for child in self.children(p)),
            default=0
        )

    def height(self, p: Position | None = None) -> int:
        """
        Return the height of the tree or the subtree rooted at p.

        If p is None, calculate the height of the entire tree.
        An empty tree has height zero.
        """
        if p is None:
            p = self.root()

        if p is None:
            return 0

        return self._height(p)

    def __iter__(self) -> Iterator[object]:
        """Iterate over the elements stored in the tree, using preorder."""
        for position in self.positions():
            yield position.element()

    # -----------------------------------------------------------------
    # Preorder traversal
    # -----------------------------------------------------------------

    def preorder(self) -> Iterator[Position]:
        """
        Generate positions in preorder.

        Visit the current position before recursively visiting its
        children.
        """
        root = self.root()

        if root is not None:
            yield from self._subtree_preorder(root)

    def _subtree_preorder(self, position: Position) -> Iterator[Position]:
        """Generate positions in preorder within a subtree."""
        yield position

        for child in self.children(position):
            yield from self._subtree_preorder(child)

    # -----------------------------------------------------------------
    # Postorder traversal
    # -----------------------------------------------------------------

    def postorder(self) -> Iterator[Position]:
        """
        Generate positions in postorder.

        Recursively visit all children before visiting the current
        position.
        """
        root = self.root()

        if root is not None:
            yield from self._subtree_postorder(root)

    def _subtree_postorder(self, position: Position) -> Iterator[Position]:
        """Generate positions in postorder within a subtree."""
        for child in self.children(position):
            yield from self._subtree_postorder(child)

        yield position

    # -----------------------------------------------------------------
    # Breadth-first traversal
    # -----------------------------------------------------------------

    def breadthfirst(self) -> Iterator[Position]:
        """
        Generate positions in breadth-first order.

        Visit positions level by level, using a queue to keep track
        of positions that still need to be visited.
        """
        root = self.root()

        if root is not None:
            positions = LinkedQueue()
            positions.enqueue(root)

            while not positions.is_empty():
                position = positions.dequeue()
                yield position

                for child in self.children(position):
                    positions.enqueue(child)

    # -----------------------------------------------------------------
    # Positions iterator
    # -----------------------------------------------------------------

    def positions(self) -> Iterator[Position]:
        """
        Return an iterator over the tree's positions.

        Preorder is used as the default traversal. Concrete subclasses
        can override this method to provide a different default order.
        """
        return self.preorder()
