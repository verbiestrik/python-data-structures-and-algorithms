import pytest

from data_structures.singly_linked_list import (
    SinglyLinkedList,
    reverse_linked_list,
)


def create_list(values):
    linked_list = SinglyLinkedList()
    nodes = []

    for value in values:
        nodes.append(linked_list.add_last(value))

    return linked_list, nodes


def test_initialization():
    linked_list = SinglyLinkedList()

    assert list(linked_list) == []
    assert linked_list._head is None
    assert linked_list._tail is None


def test_add_first():
    linked_list = SinglyLinkedList()

    linked_list.add_first(2)
    linked_list.add_first(1)

    assert list(linked_list) == [1, 2]


def test_remove_first():
    linked_list, _ = create_list([1, 2, 3])

    assert linked_list.remove_first() == 1
    assert list(linked_list) == [2, 3]


def test_add_last():
    linked_list, _ = create_list([1, 2])

    linked_list.add_last(3)

    assert list(linked_list) == [1, 2, 3]


def test_remove_last():
    linked_list, _ = create_list([1, 2, 3])

    assert linked_list.remove_last() == 3
    assert list(linked_list) == [1, 2]


def test_remove_last_single_node():
    linked_list, _ = create_list([1])

    assert linked_list.remove_last() == 1
    assert list(linked_list) == []

    linked_list.add_last(2)
    assert list(linked_list) == [2]


def test_add_before():
    linked_list, nodes = create_list([1, 3])

    linked_list.add_before(nodes[1], 2)

    assert list(linked_list) == [1, 2, 3]


def test_add_before_head():
    linked_list, nodes = create_list([2, 3])

    linked_list.add_before(nodes[0], 1)

    assert list(linked_list) == [1, 2, 3]


def test_remove_before():
    linked_list, nodes = create_list([1, 2, 3])

    assert linked_list.remove_before(nodes[2]) == 2
    assert list(linked_list) == [1, 3]


def test_remove_before_head_successor():
    linked_list, nodes = create_list([1, 2, 3])

    assert linked_list.remove_before(nodes[1]) == 1
    assert list(linked_list) == [2, 3]


def test_add_after():
    linked_list, nodes = create_list([1, 3])

    linked_list.add_after(nodes[0], 2)

    assert list(linked_list) == [1, 2, 3]


def test_add_after_tail():
    linked_list, nodes = create_list([1, 2])

    linked_list.add_after(nodes[1], 3)

    assert list(linked_list) == [1, 2, 3]


def test_remove_after():
    linked_list, nodes = create_list([1, 2, 3])

    assert linked_list.remove_after(nodes[0]) == 2
    assert list(linked_list) == [1, 3]


def test_remove_after_tail():
    linked_list, nodes = create_list([1, 2])

    with pytest.raises(ValueError):
        linked_list.remove_after(nodes[1])


def test_reverse():
    linked_list, _ = create_list([1, 2, 3, 4])

    reverse_linked_list(linked_list)

    assert list(linked_list) == [4, 3, 2, 1]


def test_reverse_empty_list():
    linked_list = SinglyLinkedList()

    reverse_linked_list(linked_list)

    assert list(linked_list) == []


def test_reverse_single_node():
    linked_list, _ = create_list([1])

    reverse_linked_list(linked_list)

    assert list(linked_list) == [1]
    assert linked_list._head is linked_list._tail


def test_reverse_twice():
    linked_list, _ = create_list([1, 2, 3])

    reverse_linked_list(linked_list)
    reverse_linked_list(linked_list)

    assert list(linked_list) == [1, 2, 3]


def test_remove_first_empty_list():
    linked_list = SinglyLinkedList()

    with pytest.raises(IndexError):
        linked_list.remove_first()


def test_remove_last_empty_list():
    linked_list = SinglyLinkedList()

    with pytest.raises(IndexError):
        linked_list.remove_last()


def test_foreign_node():
    list1, _ = create_list([1, 2])
    list2, nodes = create_list([3, 4])

    with pytest.raises(ValueError):
        list1.add_after(nodes[0], 5)


def test_detached_node():
    linked_list, nodes = create_list([1, 2])

    linked_list.remove_first()

    with pytest.raises(ValueError):
        linked_list.add_after(nodes[0], 3)


def test_remove_before_head():
    linked_list, nodes = create_list([1, 2])

    with pytest.raises(ValueError):
        linked_list.remove_before(nodes[0])


def test_tail_after_removing_last():
    linked_list, _ = create_list([1, 2, 3])

    linked_list.remove_last()

    assert linked_list._tail._value == 2
    assert linked_list._tail._next is None


def test_tail_after_reversal():
    linked_list, _ = create_list([1, 2, 3])

    reverse_linked_list(linked_list)

    assert linked_list._tail._value == 1
    assert linked_list._tail._next is None
