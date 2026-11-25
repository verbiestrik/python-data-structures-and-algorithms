"""
Linked implementation of a binary tree data structure.

A binary tree is a hierarchical data structure in which each node has
at most two children: a left child and a right child.

Approach
--------
The LinkedBinaryTree class implements the BinaryTree abstract class
using linked nodes.

Each node stores:
- Its element.
- A reference to its parent.
- A reference to its left child.
- A reference to its right child.

The nested Position class provides a public abstraction over the
internal nodes. It stores a reference to the tree containing the
position and the corresponding node.

The implementation includes operations for:
- Validating positions and creating position objects.
- Accessing the root, parent and children.
- Adding a root or a left/right child.
- Replacing and deleting elements.
- Attaching two independent binary trees as subtrees.

When a node is deleted, its parent reference is set to itself. This
serves as an invalidation marker, allowing _validate() to detect
positions that no longer belong to the tree.

When another tree is attached, its nodes are transferred rather than
copied. The original trees are consequently emptied.

Complexity
----------
Let n denote the number of nodes in the tree.

- root(): O(1) time.
- parent(), left(), right(): O(1) time.
- num_children(): O(1) time.
- __len__(): O(1) time.
- _validate() and _make_position(): O(1) time.
- _add_root(), _add_left(), _add_right(): O(1) time.
- _replace(): O(1) time.
- _delete(): O(1) time.
- _attach(): O(1) time, excluding no traversal or copying.

The tree requires O(n) space for its nodes and their references.
Position objects require O(1) space each.

Python alternatives
-------------------
The built-in len() function invokes __len__(), while isinstance()
and type() are used for position and tree type validation.

The __slots__ attribute restricts the attributes that can be assigned
to node instances, reducing their memory overhead compared with
ordinary Python objects that maintain an instance dictionary.

This implementation uses explicit references instead of Python
lists or dictionaries to represent the tree structure.
"""

from data_structures.trees.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked implementation of a binary tree."""

    class _Node:
        """Lightweight node storing an element and its relationships."""

        __slots__ = (
            "_element",
            "_parent",
            "_left_child",
            "_right_child"
        )

        def __init__(
            self,
            element,
            parent=None,
            left_child=None,
            right_child=None
        ):
            self._element = element
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child

    class Position(BinaryTree.Position):
        """Abstraction representing a node's position in a tree."""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return whether two positions refer to the same node."""
            return (
                type(other) is type(self)
                and other._node is self._node
            )

    def _validate(self, position):
        """
        Validate a position and return its corresponding node.

        Raises:
            TypeError: If the position has an incorrect type.
            ValueError: If the position belongs to another tree or
                        refers to a node that has been deleted.
        """
        if not isinstance(position, self.Position):
            raise TypeError("position must be of the proper Position type")

        if position._container is not self:
            raise ValueError("position does not belong to this container")

        if position._node._parent is position._node:
            raise ValueError("position is no longer valid")

        return position._node

    def _make_position(self, node):
        """Return a Position object for a node, or None if absent."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the number of nodes in the tree."""
        return self._size

    def root(self):
        """Return the root position, or None if the tree is empty."""
        return self._make_position(self._root)

    def parent(self, position):
        """Return the parent of a position, or None if it is the root."""
        node = self._validate(position)
        return self._make_position(node._parent)

    def left(self, position):
        """Return the left child of a position, or None if absent."""
        node = self._validate(position)
        return self._make_position(node._left_child)

    def right(self, position):
        """Return the right child of a position, or None if absent."""
        node = self._validate(position)
        return self._make_position(node._right_child)

    def num_children(self, position):
        """Return the number of children of a position."""
        node = self._validate(position)

        children_count = 0

        if node._left_child is not None:
            children_count += 1

        if node._right_child is not None:
            children_count += 1

        return children_count

    def _add_root(self, element):
        """Add a root to an empty tree and return its position."""
        if self._root is not None:
            raise ValueError("tree is not empty")

        self._size = 1
        self._root = self._Node(element)

        return self._make_position(self._root)

    def _add_left(self, position, element):
        """Add a left child to a position and return its position."""
        node = self._validate(position)

        if node._left_child is not None:
            raise ValueError("left child already exists")

        node._left_child = self._Node(element, parent=node)
        self._size += 1

        return self._make_position(node._left_child)

    def _add_right(self, position, element):
        """Add a right child to a position and return its position."""
        node = self._validate(position)

        if node._right_child is not None:
            raise ValueError("right child already exists")

        node._right_child = self._Node(element, parent=node)
        self._size += 1

        return self._make_position(node._right_child)

    def _replace(self, position, element):
        """Replace the element at a position and return the old element."""
        node = self._validate(position)

        old_element = node._element
        node._element = element

        return old_element

    def _delete(self, position):
        """
        Delete a position with at most one child.

        The existing child, if any, takes the place of the deleted node.
        The deleted node is marked as invalid.
        """
        node = self._validate(position)

        if self.num_children(position) == 2:
            raise ValueError("node at position has two children")

        # Select the existing child, if there is one.
        child = (
            node._left_child
            if node._left_child is not None
            else node._right_child
        )

        if child is not None:
            child._parent = node._parent

        # Update the root or the appropriate parent reference.
        if node is self._root:
            self._root = child
        else:
            parent = node._parent

            if node is parent._left_child:
                parent._left_child = child
            else:
                parent._right_child = child

        self._size -= 1

        # Mark the deleted node as invalid.
        node._parent = node

        return node._element

    def _attach(self, position, tree1, tree2):
        """
        Attach two trees as the left and right subtrees of a leaf.

        The donor trees must be of exactly the same type as this tree.
        Their nodes are transferred without copying, and both donor
        trees are emptied after attachment.
        """
        node = self._validate(position)

        if not self.is_leaf(position):
            raise ValueError("node at given position has to be a leaf")

        if type(self) is not type(tree1) or type(self) is not type(tree2):
            raise TypeError("all trees need to have the same type")

        # Prevent self-attachment and attaching the same tree twice.
        if tree1 is self or tree2 is self or tree1 is tree2:
            raise ValueError("trees to attach must be distinct from each other")

        self._size += len(tree1) + len(tree2)

        if not tree1.is_empty():
            tree1._root._parent = node
            node._left_child = tree1._root

            tree1._root = None
            tree1._size = 0

        if not tree2.is_empty():
            tree2._root._parent = node
            node._right_child = tree2._root

            tree2._root = None
            tree2._size = 0
