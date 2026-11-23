import pytest

from data_structures.deque.linked_deque import LinkedDeque, Empty


def test_new_deque_is_empty():
    deque = LinkedDeque()

    assert len(deque) == 0
    assert deque.is_empty()


def test_insert_first():
    deque = LinkedDeque()

    deque.insert_first(10)
    deque.insert_first(20)
    deque.insert_first(30)

    assert len(deque) == 3
    assert deque.first() == 30
    assert deque.last() == 10


def test_insert_last():
    deque = LinkedDeque()

    deque.insert_last(10)
    deque.insert_last(20)
    deque.insert_last(30)

    assert len(deque) == 3
    assert deque.first() == 10
    assert deque.last() == 30


def test_first_and_last_do_not_remove_elements():
    deque = LinkedDeque()

    deque.insert_first(10)
    deque.insert_last(20)

    assert deque.first() == 10
    assert deque.last() == 20

    assert len(deque) == 2
    assert not deque.is_empty()


def test_delete_first():
    deque = LinkedDeque()

    deque.insert_last(10)
    deque.insert_last(20)
    deque.insert_last(30)

    assert deque.delete_first() == 10
    assert deque.delete_first() == 20

    assert len(deque) == 1
    assert deque.first() == 30


def test_delete_last():
    deque = LinkedDeque()

    deque.insert_last(10)
    deque.insert_last(20)
    deque.insert_last(30)

    assert deque.delete_last() == 30
    assert deque.delete_last() == 20

    assert len(deque) == 1
    assert deque.last() == 10


def test_delete_only_element():
    deque = LinkedDeque()

    deque.insert_first(10)

    assert deque.delete_first() == 10
    assert deque.is_empty()
    assert len(deque) == 0

    assert deque._header._next is deque._trailer
    assert deque._trailer._previous is deque._header


def test_delete_last_element():
    deque = LinkedDeque()

    deque.insert_last(10)

    assert deque.delete_last() == 10
    assert deque.is_empty()
    assert len(deque) == 0

    assert deque._header._next is deque._trailer
    assert deque._trailer._previous is deque._header


def test_first_on_empty_deque_raises_exception():
    deque = LinkedDeque()

    with pytest.raises(Empty):
        deque.first()


def test_last_on_empty_deque_raises_exception():
    deque = LinkedDeque()

    with pytest.raises(Empty):
        deque.last()


def test_delete_first_from_empty_deque_raises_exception():
    deque = LinkedDeque()

    with pytest.raises(Empty):
        deque.delete_first()


def test_delete_last_from_empty_deque_raises_exception():
    deque = LinkedDeque()

    with pytest.raises(Empty):
        deque.delete_last()


def test_interleaved_insertions_and_deletions():
    deque = LinkedDeque()

    deque.insert_first(2)
    deque.insert_last(3)
    deque.insert_first(1)
    deque.insert_last(4)

    assert deque.first() == 1
    assert deque.last() == 4

    assert deque.delete_first() == 1
    assert deque.delete_last() == 4

    deque.insert_first(0)
    deque.insert_last(5)

    assert deque.first() == 0
    assert deque.last() == 5
    assert len(deque) == 4


def test_deque_accepts_none_as_a_valid_element():
    deque = LinkedDeque()

    deque.insert_first(None)

    assert len(deque) == 1
    assert not deque.is_empty()
    assert deque.first() is None
    assert deque.last() is None
    assert deque.delete_first() is None
    assert deque.is_empty()


def test_deque_accepts_different_element_types():
    deque = LinkedDeque()

    elements = [10, "hello", None, 3.14, False]

    for element in elements:
        deque.insert_last(element)

    assert len(deque) == len(elements)

    for element in elements:
        assert deque.delete_first() == element

    assert deque.is_empty()


def test_multiple_deques_are_independent():
    deque_a = LinkedDeque()
    deque_b = LinkedDeque()

    deque_a.insert_first(10)
    deque_b.insert_first(20)

    deque_a.insert_last(30)

    assert deque_a.first() == 10
    assert deque_a.last() == 30

    assert deque_b.first() == 20
    assert deque_b.last() == 20


def test_large_number_of_insertions_and_deletions():
    deque = LinkedDeque()

    for value in range(1000):
        deque.insert_last(value)

    assert len(deque) == 1000

    for value in range(500):
        assert deque.delete_first() == value

    for value in reversed(range(500, 1000)):
        assert deque.delete_last() == value

    assert deque.is_empty()
    assert len(deque) == 0
