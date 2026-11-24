import pytest

from data_structures.trees.binary_tree import BinaryTree
from data_structures.trees.tree import Tree


class SamplePosition(Tree.Position):
    """Concrete position implementation for testing."""

    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent
        self._left = None
        self._right = None

    def element(self):
        return self._element

    def __eq__(self, other):
        return self is other


class SampleBinaryTree(BinaryTree):
    """Concrete binary tree implementation for testing."""

    def __init__(self, empty=False):
        self._root = None
        self._size = 0

        if not empty:
            self._root = SamplePosition("root")

            self.left = SamplePosition("left", self._root)
            self.right = SamplePosition("right", self._root)

            self.left_left = SamplePosition("left_left", self.left)
            self.left_right = SamplePosition("left_right", self.left)

            self._root._left = self.left
            self._root._right = self.right

            self.left._left = self.left_left
            self.left._right = self.left_right

            self._size = 5

    def root(self):
        return self._root

    def parent(self, position):
        return position._parent

    def num_children(self, position):
        return sum(
            child is not None
            for child in (position._left, position._right)
        )

    def __len__(self):
        return self._size

    def left(self, position):
        return position._left

    def right(self, position):
        return position._right


@pytest.fixture
def binary_tree():
    """Provide a binary tree for testing."""
    return SampleBinaryTree()


# ---------------------------------------------------------------------
# Abstract class tests
# ---------------------------------------------------------------------

def test_binary_tree_is_abstract():
    """The abstract BinaryTree class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        BinaryTree()


# ---------------------------------------------------------------------
# Left and right child tests
# ---------------------------------------------------------------------

def test_left(binary_tree):
    """The left operation should return the correct left child."""
    assert binary_tree.left(binary_tree.root()) == binary_tree.left
    assert binary_tree.left(binary_tree.left) == binary_tree.left_left
    assert binary_tree.left(binary_tree.right) is None


def test_right(binary_tree):
    """The right operation should return the correct right child."""
    assert binary_tree.right(binary_tree.root()) == binary_tree.right
    assert binary_tree.right(binary_tree.left) == binary_tree.left_right
    assert binary_tree.right(binary_tree.right) is None


# ---------------------------------------------------------------------
# Sibling tests
# ---------------------------------------------------------------------

def test_sibling(binary_tree):
    """The sibling operation should return the other child."""
    assert binary_tree.sibling(binary_tree.left) == binary_tree.right
    assert binary_tree.sibling(binary_tree.right) == binary_tree.left

    assert binary_tree.sibling(binary_tree.left_left) == binary_tree.left_right
    assert binary_tree.sibling(binary_tree.left_right) == binary_tree.left_left


def test_sibling_of_root(binary_tree):
    """The root has no sibling."""
    assert binary_tree.sibling(binary_tree.root()) is None


def test_sibling_without_existing_sibling(binary_tree):
    """A position without a sibling should return None."""
    assert binary_tree.sibling(binary_tree.left) == binary_tree.right

    # The right child has no children in this tree.
    assert binary_tree.sibling(binary_tree.right) == binary_tree.left


def test_sibling_of_only_child():
    """A position with no sibling should return None."""
    tree = SampleBinaryTree(empty=True)

    root = SamplePosition("root")
    child = SamplePosition("child", root)
    root._left = child

    tree._root = root
    tree._size = 2

    assert tree.sibling(child) is None


# ---------------------------------------------------------------------
# Children tests
# ---------------------------------------------------------------------

def test_children(binary_tree):
    """The children operation should return both children in order."""
    assert list(binary_tree.children(binary_tree.root())) == [
        binary_tree.left,
        binary_tree.right
    ]

    assert list(binary_tree.children(binary_tree.left)) == [
        binary_tree.left_left,
        binary_tree.left_right
    ]


def test_children_with_only_left_child():
    """The children operation should handle a missing right child."""
    tree = SampleBinaryTree(empty=True)

    root = SamplePosition("root")
    left = SamplePosition("left", root)
    root._left = left

    assert list(tree.children(root)) == [left]


def test_children_with_only_right_child():
    """The children operation should handle a missing left child."""
    tree = SampleBinaryTree(empty=True)

    root = SamplePosition("root")
    right = SamplePosition("right", root)
    root._right = right

    assert list(tree.children(root)) == [right]


def test_children_of_leaf(binary_tree):
    """A leaf should have an empty children iterator."""
    assert list(binary_tree.children(binary_tree.right)) == []
    assert list(binary_tree.children(binary_tree.left_left)) == []
    assert list(binary_tree.children(binary_tree.left_right)) == []
