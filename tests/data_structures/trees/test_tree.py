import pytest

from data_structures.trees.tree import Tree


class TestPosition(Tree.Position):
    """Minimal concrete implementation of a tree position."""

    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent
        self._children = []

        if parent is not None:
            parent._children.append(self)

    def element(self):
        return self._element

    def __eq__(self, other):
        return self is other


class TestTree(Tree):
    """Minimal concrete tree implementation for testing the Tree ADT."""

    def __init__(self, empty=False):
        self._root = None
        self._size = 0

        if not empty:
            self._root = TestPosition("root")

            self.left = TestPosition("left", self._root)
            self.right = TestPosition("right", self._root)
            self.left_child = TestPosition("left_child", self.left)

            self._size = 4

    def root(self):
        return self._root

    def parent(self, p):
        return p._parent

    def num_children(self, p):
        return len(p._children)

    def children(self, p):
        return iter(p._children)

    def __len__(self):
        return self._size


@pytest.fixture
def tree():
    """Provide a small tree for testing."""
    return TestTree()


# ---------------------------------------------------------------------
# Abstract class and Position tests
# ---------------------------------------------------------------------

def test_tree_is_abstract():
    """The abstract Tree class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Tree()


def test_position_is_abstract():
    """The abstract Position class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Tree.Position()


def test_position_element(tree):
    """A concrete position should return its stored element."""
    assert tree.root().element() == "root"
    assert tree.left.element() == "left"


def test_position_equality(tree):
    """Positions should support equality and inequality comparisons."""
    assert tree.left == tree.left
    assert tree.left != tree.right

    assert not (tree.left != tree.left)
    assert not (tree.left == tree.right)


# ---------------------------------------------------------------------
# Fundamental tree operation tests
# ---------------------------------------------------------------------

def test_root(tree):
    """The root operation should return the root position."""
    assert tree.root() is not None
    assert tree.root().element() == "root"


def test_root_of_empty_tree():
    """An empty tree should have no root."""
    empty_tree = TestTree(empty=True)

    assert empty_tree.root() is None


def test_parent(tree):
    """The parent operation should return the correct parent."""
    assert tree.parent(tree.root()) is None
    assert tree.parent(tree.left) == tree.root()
    assert tree.parent(tree.left_child) == tree.left


def test_num_children(tree):
    """The number of children should be calculated correctly."""
    assert tree.num_children(tree.root()) == 2
    assert tree.num_children(tree.left) == 1
    assert tree.num_children(tree.right) == 0


def test_children(tree):
    """The children operation should return all child positions."""
    assert list(tree.children(tree.root())) == [
        tree.left,
        tree.right
    ]

    assert list(tree.children(tree.left)) == [tree.left_child]
    assert list(tree.children(tree.right)) == []


def test_len(tree):
    """The length operation should return the number of positions."""
    assert len(tree) == 4


def test_len_empty_tree():
    """An empty tree should have length zero."""
    empty_tree = TestTree(empty=True)

    assert len(empty_tree) == 0


# ---------------------------------------------------------------------
# Generic tree operation tests
# ---------------------------------------------------------------------

def test_is_root(tree):
    """is_root should correctly identify the root position."""
    assert tree.is_root(tree.root())
    assert not tree.is_root(tree.left)
    assert not tree.is_root(tree.left_child)


def test_is_leaf(tree):
    """is_leaf should correctly identify positions without children."""
    assert tree.is_leaf(tree.right)
    assert tree.is_leaf(tree.left_child)

    assert not tree.is_leaf(tree.root())
    assert not tree.is_leaf(tree.left)


def test_is_empty(tree):
    """is_empty should correctly identify whether the tree is empty."""
    assert not tree.is_empty()

    empty_tree = TestTree(empty=True)

    assert empty_tree.is_empty()


def test_depth(tree):
    """Depth should equal the number of edges to the root."""
    assert tree.depth(tree.root()) == 0
    assert tree.depth(tree.left) == 1
    assert tree.depth(tree.left_child) == 2
    assert tree.depth(tree.right) == 1


def test_height(tree):
    """Height should equal the maximum distance to a leaf."""
    assert tree.height() == 2
    assert tree.height(tree.root()) == 2
    assert tree.height(tree.left) == 1
    assert tree.height(tree.left_child) == 0
    assert tree.height(tree.right) == 0


def test_height_empty_tree():
    """An empty tree should have height zero."""
    empty_tree = TestTree(empty=True)

    assert empty_tree.height() == 0


def test_height_of_subtree(tree):
    """Height should be calculated relative to the supplied position."""
    assert tree.height(tree.left) == 1
    assert tree.height(tree.right) == 0
    assert tree.height(tree.left_child) == 0
