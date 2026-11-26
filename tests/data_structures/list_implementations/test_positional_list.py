import pytest

from data_structures.list_implementations.positional_list import (
    PositionalList,
)


@pytest.fixture
def positional_list():
    """Provide a positional list containing three elements."""
    linked_list = PositionalList()

    linked_list.add_last("A")
    linked_list.add_last("B")
    linked_list.add_last("C")

    return linked_list


# ---------------------------------------------------------------------
# Initialization and basic operations
# ---------------------------------------------------------------------

def test_new_list_is_empty():
    linked_list = PositionalList()

    assert len(linked_list) == 0
    assert linked_list.is_empty()
    assert linked_list.first() is None
    assert linked_list.last() is None
    assert list(linked_list) == []


def test_len(positional_list):
    assert len(positional_list) == 3


def test_is_empty(positional_list):
    assert not positional_list.is_empty()


# ---------------------------------------------------------------------
# Position tests
# ---------------------------------------------------------------------

def test_position_element(positional_list):
    assert positional_list.first().element() == "A"
    assert positional_list.last().element() == "C"


def test_position_equality(positional_list):
    first = positional_list.first()
    another_first = positional_list.first()

    assert first == another_first
    assert not (first != another_first)


def test_position_inequality(positional_list):
    first = positional_list.first()
    last = positional_list.last()

    assert first != last
    assert not (first == last)


# ---------------------------------------------------------------------
# Validation tests
# ---------------------------------------------------------------------

def test_validate_invalid_type(positional_list):
    with pytest.raises(TypeError):
        positional_list.before("not a position")


def test_validate_foreign_position(positional_list):
    another_list = PositionalList()
    foreign_position = another_list.add_first("X")

    with pytest.raises(ValueError):
        positional_list.before(foreign_position)


def test_validate_deleted_position(positional_list):
    position = positional_list.first()

    positional_list.delete(position)

    with pytest.raises(ValueError):
        positional_list.after(position)


def test_validate_sentinel_position(positional_list):
    """Sentinel nodes must never be accepted as valid positions."""
    header_position = PositionalList.Position(
        positional_list,
        positional_list._header,
    )

    with pytest.raises(ValueError):
        positional_list.before(header_position)


# ---------------------------------------------------------------------
# First and last tests
# ---------------------------------------------------------------------

def test_first(positional_list):
    assert positional_list.first().element() == "A"


def test_last(positional_list):
    assert positional_list.last().element() == "C"


def test_first_and_last_single_element():
    linked_list = PositionalList()
    position = linked_list.add_first("A")

    assert linked_list.first() == position
    assert linked_list.last() == position


# ---------------------------------------------------------------------
# Before and after tests
# ---------------------------------------------------------------------

def test_before(positional_list):
    first = positional_list.first()
    second = positional_list.after(first)

    assert positional_list.before(second) == first


def test_after(positional_list):
    first = positional_list.first()
    second = positional_list.after(first)

    assert positional_list.after(first) == second


def test_before_first_returns_none(positional_list):
    assert positional_list.before(positional_list.first()) is None


def test_after_last_returns_none(positional_list):
    assert positional_list.after(positional_list.last()) is None


# ---------------------------------------------------------------------
# Iteration tests
# ---------------------------------------------------------------------

def test_iteration(positional_list):
    assert list(positional_list) == ["A", "B", "C"]


def test_iteration_with_none_element():
    linked_list = PositionalList()

    linked_list.add_first(None)

    assert len(linked_list) == 1
    assert list(linked_list) == [None]


# ---------------------------------------------------------------------
# Insertion tests
# ---------------------------------------------------------------------

def test_add_first():
    linked_list = PositionalList()

    position = linked_list.add_first("A")

    assert position.element() == "A"
    assert linked_list.first() == position
    assert linked_list.last() == position
    assert len(linked_list) == 1


def test_add_last():
    linked_list = PositionalList()

    position = linked_list.add_last("A")

    assert position.element() == "A"
    assert linked_list.first() == position
    assert linked_list.last() == position
    assert len(linked_list) == 1


def test_add_multiple_first():
    linked_list = PositionalList()

    linked_list.add_first("C")
    linked_list.add_first("B")
    linked_list.add_first("A")

    assert list(linked_list) == ["A", "B", "C"]


def test_add_multiple_last():
    linked_list = PositionalList()

    linked_list.add_last("A")
    linked_list.add_last("B")
    linked_list.add_last("C")

    assert list(linked_list) == ["A", "B", "C"]


def test_add_before(positional_list):
    second = positional_list.after(positional_list.first())

    new_position = positional_list.add_before(second, "X")

    assert new_position.element() == "X"
    assert list(positional_list) == ["A", "X", "B", "C"]
    assert len(positional_list) == 4


def test_add_after(positional_list):
    second = positional_list.after(positional_list.first())

    new_position = positional_list.add_after(second, "X")

    assert new_position.element() == "X"
    assert list(positional_list) == ["A", "B", "X", "C"]
    assert len(positional_list) == 4


def test_add_before_invalid_position(positional_list):
    another_list = PositionalList()
    foreign_position = another_list.add_first("X")

    with pytest.raises(ValueError):
        positional_list.add_before(foreign_position, "Y")


def test_add_after_invalid_position(positional_list):
    another_list = PositionalList()
    foreign_position = another_list.add_first("X")

    with pytest.raises(ValueError):
        positional_list.add_after(foreign_position, "Y")


# ---------------------------------------------------------------------
# Delete tests
# ---------------------------------------------------------------------

def test_delete_first(positional_list):
    first = positional_list.first()

    assert positional_list.delete(first) == "A"

    assert list(positional_list) == ["B", "C"]
    assert len(positional_list) == 2
    assert positional_list.first().element() == "B"


def test_delete_last(positional_list):
    last = positional_list.last()

    assert positional_list.delete(last) == "C"

    assert list(positional_list) == ["A", "B"]
    assert len(positional_list) == 2
    assert positional_list.last().element() == "B"


def test_delete_middle(positional_list):
    middle = positional_list.after(positional_list.first())

    assert positional_list.delete(middle) == "B"

    assert list(positional_list) == ["A", "C"]
    assert len(positional_list) == 2


def test_delete_only_element():
    linked_list = PositionalList()
    position = linked_list.add_first("A")

    assert linked_list.delete(position) == "A"

    assert linked_list.is_empty()
    assert len(linked_list) == 0
    assert linked_list.first() is None
    assert linked_list.last() is None


def test_delete_invalidated_position(positional_list):
    position = positional_list.first()

    positional_list.delete(position)

    with pytest.raises(ValueError):
        positional_list.delete(position)


# ---------------------------------------------------------------------
# Replace tests
# ---------------------------------------------------------------------

def test_replace(positional_list):
    first = positional_list.first()

    old_element = positional_list.replace(first, "X")

    assert old_element == "A"
    assert first.element() == "X"
    assert list(positional_list) == ["X", "B", "C"]
    assert len(positional_list) == 3


def test_replace_with_none(positional_list):
    first = positional_list.first()

    assert positional_list.replace(first, None) == "A"

    assert first.element() is None
    assert list(positional_list) == [None, "B", "C"]
