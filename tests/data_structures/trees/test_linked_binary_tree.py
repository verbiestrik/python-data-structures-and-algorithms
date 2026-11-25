import pytest

from data_structures.trees.linked_binary_tree import LinkedBinaryTree


@pytest.fixture
def tree():
    """Provide a binary tree with several levels."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    left = tree._add_left(root, "left")
    right = tree._add_right(root, "right")

    tree._add_left(left, "left_left")
    tree._add_right(left, "left_right")

    return tree


# ---------------------------------------------------------------------
# Initialization and basic operations
# ---------------------------------------------------------------------

def test_initialization():
    """A new tree should be empty."""
    tree = LinkedBinaryTree()

    assert len(tree) == 0
    assert tree.is_empty()
    assert tree.root() is None


def test_add_root():
    """Adding a root should initialize the tree."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")

    assert root.element() == "root"
    assert tree.root() == root
    assert len(tree) == 1
    assert not tree.is_empty()


def test_add_root_to_nonempty_tree():
    """Adding a second root should raise ValueError."""
    tree = LinkedBinaryTree()

    tree._add_root("root")

    with pytest.raises(ValueError):
        tree._add_root("another_root")


def test_len(tree):
    """The length should equal the number of nodes."""
    assert len(tree) == 5


# ---------------------------------------------------------------------
# Position and validation tests
# ---------------------------------------------------------------------

def test_position_equality(tree):
    """Positions referring to the same node should be equal."""
    root = tree.root()
    another_root = tree.root()

    assert root == another_root
    assert not (root != another_root)


def test_position_inequality(tree):
    """Positions referring to different nodes should not be equal."""
    root = tree.root()
    left = tree.left(root)

    assert root != left
    assert not (root == left)


def test_validate_invalid_type(tree):
    """Validation should reject objects that are not positions."""
    with pytest.raises(TypeError):
        tree._validate("not a position")

    with pytest.raises(TypeError):
        tree.left(None)


def test_validate_foreign_position(tree):
    """Validation should reject positions belonging to another tree."""
    another_tree = LinkedBinaryTree()
    another_root = another_tree._add_root("another_root")

    with pytest.raises(ValueError):
        tree._validate(another_root)


def test_validate_deleted_position():
    """Validation should reject positions that have been deleted."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    tree._delete(root)

    with pytest.raises(ValueError):
        tree._validate(root)


# ---------------------------------------------------------------------
# Root, parent and child access tests
# ---------------------------------------------------------------------

def test_root(tree):
    """The root operation should return the root position."""
    assert tree.root().element() == "root"


def test_parent(tree):
    """The parent operation should return the correct parent."""
    root = tree.root()
    left = tree.left(root)
    right = tree.right(root)

    assert tree.parent(root) is None
    assert tree.parent(left) == root
    assert tree.parent(right) == root


def test_left(tree):
    """The left operation should return the correct left child."""
    root = tree.root()
    left = tree.left(root)

    assert left.element() == "left"
    assert tree.left(left).element() == "left_left"
    assert tree.left(tree.right(root)) is None


def test_right(tree):
    """The right operation should return the correct right child."""
    root = tree.root()
    left = tree.left(root)

    assert tree.right(root).element() == "right"
    assert tree.right(left).element() == "left_right"
    assert tree.right(tree.right(root)) is None


def test_num_children(tree):
    """The number of children should be calculated correctly."""
    root = tree.root()
    left = tree.left(root)
    right = tree.right(root)

    assert tree.num_children(root) == 2
    assert tree.num_children(left) == 2
    assert tree.num_children(right) == 0


def test_children(tree):
    """The children iterator should return left before right."""
    root = tree.root()
    left = tree.left(root)

    assert list(tree.children(root)) == [
        left,
        tree.right(root)
    ]

    assert list(tree.children(left)) == [
        tree.left(left),
        tree.right(left)
    ]

    assert list(tree.children(tree.right(root))) == []


# ---------------------------------------------------------------------
# Adding children tests
# ---------------------------------------------------------------------

def test_add_left():
    """Adding a left child should update the tree correctly."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    left = tree._add_left(root, "left")

    assert left.element() == "left"
    assert tree.left(root) == left
    assert tree.parent(left) == root
    assert tree.num_children(root) == 1
    assert len(tree) == 2


def test_add_right():
    """Adding a right child should update the tree correctly."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    right = tree._add_right(root, "right")

    assert right.element() == "right"
    assert tree.right(root) == right
    assert tree.parent(right) == root
    assert tree.num_children(root) == 1
    assert len(tree) == 2


def test_add_left_when_child_exists(tree):
    """Adding a second left child should raise ValueError."""
    with pytest.raises(ValueError):
        tree._add_left(tree.root(), "another_left")


def test_add_right_when_child_exists(tree):
    """Adding a second right child should raise ValueError."""
    with pytest.raises(ValueError):
        tree._add_right(tree.root(), "another_right")


# ---------------------------------------------------------------------
# Replace tests
# ---------------------------------------------------------------------

def test_replace(tree):
    """Replacing an element should return the original element."""
    root = tree.root()

    old_element = tree._replace(root, "new_root")

    assert old_element == "root"
    assert root.element() == "new_root"
    assert len(tree) == 5


# ---------------------------------------------------------------------
# Delete tests
# ---------------------------------------------------------------------

def test_delete_leaf():
    """Deleting a leaf should remove it from the tree."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    left = tree._add_left(root, "left")

    deleted_element = tree._delete(left)

    assert deleted_element == "left"
    assert tree.left(root) is None
    assert tree.num_children(root) == 0
    assert len(tree) == 1


def test_delete_node_with_left_child():
    """Deleting a node with a left child should promote that child."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    left = tree._add_left(root, "left")
    left_child = tree._add_left(left, "left_child")

    deleted_element = tree._delete(left)

    assert deleted_element == "left"
    assert tree.left(root) == left_child
    assert tree.parent(left_child) == root
    assert len(tree) == 2


def test_delete_node_with_right_child():
    """Deleting a node with a right child should promote that child."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    right = tree._add_right(root, "right")
    right_child = tree._add_right(right, "right_child")

    deleted_element = tree._delete(right)

    assert deleted_element == "right"
    assert tree.right(root) == right_child
    assert tree.parent(right_child) == root
    assert len(tree) == 2


def test_delete_root_with_one_child():
    """Deleting a root with one child should promote that child."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")
    left = tree._add_left(root, "left")

    deleted_element = tree._delete(root)

    assert deleted_element == "root"
    assert tree.root() == left
    assert tree.parent(left) is None
    assert len(tree) == 1


def test_delete_root_without_children():
    """Deleting the only node should leave the tree empty."""
    tree = LinkedBinaryTree()

    root = tree._add_root("root")

    deleted_element = tree._delete(root)

    assert deleted_element == "root"
    assert tree.root() is None
    assert tree.is_empty()
    assert len(tree) == 0


def test_delete_node_with_two_children(tree):
    """Deleting a node with two children should raise ValueError."""
    root = tree.root()

    with pytest.raises(ValueError):
        tree._delete(root)

    assert tree.root() == root
    assert len(tree) == 5


# ---------------------------------------------------------------------
# Attach tests
# ---------------------------------------------------------------------

def test_attach_two_nonempty_trees():
    """Attaching two trees should transfer both subtrees correctly."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    tree1 = LinkedBinaryTree()
    left_root = tree1._add_root("left_root")
    tree1._add_left(left_root, "left_child")

    tree2 = LinkedBinaryTree()
    right_root = tree2._add_root("right_root")
    tree2._add_right(right_root, "right_child")

    tree._attach(root, tree1, tree2)

    assert tree.left(root).element() == "left_root"
    assert tree.right(root).element() == "right_root"

    assert tree.parent(tree.left(root)) == root
    assert tree.parent(tree.right(root)) == root

    assert len(tree) == 5
    assert len(tree1) == 0
    assert len(tree2) == 0

    assert tree1.is_empty()
    assert tree2.is_empty()


def test_attach_two_empty_trees():
    """Attaching empty trees should leave the original tree unchanged."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    tree1 = LinkedBinaryTree()
    tree2 = LinkedBinaryTree()

    tree._attach(root, tree1, tree2)

    assert tree.left(root) is None
    assert tree.right(root) is None
    assert len(tree) == 1
    assert tree1.is_empty()
    assert tree2.is_empty()


def test_attach_one_nonempty_tree():
    """Attaching one nonempty tree should add only that subtree."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    tree1 = LinkedBinaryTree()
    left_root = tree1._add_root("left_root")

    tree2 = LinkedBinaryTree()

    tree._attach(root, tree1, tree2)

    assert tree.left(root).element() == "left_root"
    assert tree.right(root) is None
    assert tree.parent(tree.left(root)) == root

    assert len(tree) == 2
    assert tree1.is_empty()
    assert tree2.is_empty()


def test_attach_to_non_leaf(tree):
    """Attaching to a position with children should raise ValueError."""
    tree1 = LinkedBinaryTree()
    tree1._add_root("tree1")

    tree2 = LinkedBinaryTree()
    tree2._add_root("tree2")

    with pytest.raises(ValueError):
        tree._attach(tree.root(), tree1, tree2)


def test_attach_different_tree_types():
    """Attaching trees of different types should raise TypeError."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    with pytest.raises(TypeError):
        tree._attach(root, object(), object())


def test_attach_same_tree_twice():
    """The same donor tree cannot be attached as both subtrees."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    donor = LinkedBinaryTree()
    donor._add_root("donor")

    with pytest.raises(ValueError):
        tree._attach(root, donor, donor)

    assert len(donor) == 1
    assert tree.left(root) is None
    assert tree.right(root) is None


def test_attach_tree_to_itself():
    """A tree cannot be attached to itself."""
    tree = LinkedBinaryTree()
    root = tree._add_root("root")

    donor = LinkedBinaryTree()
    donor._add_root("donor")

    with pytest.raises(ValueError):
        tree._attach(root, tree, donor)

    assert len(tree) == 1
    assert len(donor) == 1
