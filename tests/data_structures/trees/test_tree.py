import pytest

from data_structures.trees.linked_binary_tree import LinkedBinaryTree


@pytest.fixture
def tree():
    """
    Construct the following binary tree:

             A
           /   \
          B     C
         / \     \
        D   E     F
    """
    tree = LinkedBinaryTree()

    root = tree._add_root("A")

    left = tree._add_left(root, "B")
    right = tree._add_right(root, "C")

    tree._add_left(left, "D")
    tree._add_right(left, "E")

    tree._add_right(right, "F")

    return tree


def elements(positions):
    """Return the elements stored at a sequence of positions."""
    return [position.element() for position in positions]


# ---------------------------------------------------------------------
# Preorder traversal
# ---------------------------------------------------------------------

def test_preorder(tree):
    """Preorder should visit the parent before its children."""
    assert elements(tree.preorder()) == [
        "A", "B", "D", "E", "C", "F"
    ]


def test_preorder_empty_tree():
    """Preorder of an empty tree should yield no positions."""
    tree = LinkedBinaryTree()

    assert list(tree.preorder()) == []


# ---------------------------------------------------------------------
# Postorder traversal
# ---------------------------------------------------------------------

def test_postorder(tree):
    """Postorder should visit children before their parent."""
    assert elements(tree.postorder()) == [
        "D", "E", "B", "F", "C", "A"
    ]


def test_postorder_empty_tree():
    """Postorder of an empty tree should yield no positions."""
    tree = LinkedBinaryTree()

    assert list(tree.postorder()) == []


# ---------------------------------------------------------------------
# Inorder traversal
# ---------------------------------------------------------------------

def test_inorder(tree):
    """Inorder should visit left subtree, parent, then right subtree."""
    assert elements(tree.inorder()) == [
        "D", "B", "E", "A", "C", "F"
    ]


def test_inorder_empty_tree():
    """Inorder of an empty binary tree should yield no positions."""
    tree = LinkedBinaryTree()

    assert list(tree.inorder()) == []


# ---------------------------------------------------------------------
# Breadth-first traversal
# ---------------------------------------------------------------------

def test_breadthfirst(tree):
    """Breadth-first should visit positions level by level."""
    assert elements(tree.breadthfirst()) == [
        "A", "B", "C", "D", "E", "F"
    ]


def test_breadthfirst_empty_tree():
    """Breadth-first traversal of an empty tree should yield no positions."""
    tree = LinkedBinaryTree()

    assert list(tree.breadthfirst()) == []


# ---------------------------------------------------------------------
# Default positions iterator
# ---------------------------------------------------------------------

def test_positions(tree):
    """The positions method should use preorder by default."""
    assert elements(tree.positions()) == [
        "A", "B", "D", "E", "C", "F"
    ]


def test_positions_empty_tree():
    """The positions iterator of an empty tree should be empty."""
    tree = LinkedBinaryTree()

    assert list(tree.positions()) == []


# ---------------------------------------------------------------------
# Tree iteration
# ---------------------------------------------------------------------

def test_iter(tree):
    """Iterating over a tree should yield its elements in preorder."""
    assert list(tree) == [
        "A", "B", "D", "E", "C", "F"
    ]


def test_iter_empty_tree():
    """Iterating over an empty tree should yield no elements."""
    tree = LinkedBinaryTree()

    assert list(tree) == []


# ---------------------------------------------------------------------
# Single-node tree
# ---------------------------------------------------------------------

def test_traversals_single_node():
    """All traversal methods should work on a tree with one node."""
    tree = LinkedBinaryTree()
    tree._add_root("A")

    assert elements(tree.preorder()) == ["A"]
    assert elements(tree.postorder()) == ["A"]
    assert elements(tree.inorder()) == ["A"]
    assert elements(tree.breadthfirst()) == ["A"]
    assert elements(tree.positions()) == ["A"]
    assert list(tree) == ["A"]
