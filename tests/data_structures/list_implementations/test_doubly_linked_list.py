import pytest

from data_structures.list_implementations.doubly_linked_list import (
    DoublyLinkedList,
)


def test_new_list_is_empty():
    linked_list = DoublyLinkedList()

    assert len(linked_list) == 0
    assert linked_list.is_empty()

    assert linked_list._header._next is linked_list._trailer
    assert linked_list._trailer._previous is linked_list._header


def test_insert_between_header_and_trailer():
    linked_list = DoublyLinkedList()

    node = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    assert len(linked_list) == 1
    assert not linked_list.is_empty()

    assert linked_list._header._next is node
    assert linked_list._trailer._previous is node

    assert node._element == 10
    assert node._previous is linked_list._header
    assert node._next is linked_list._trailer


def test_insert_multiple_nodes():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    second = linked_list.insert_between(
        20,
        first,
        linked_list._trailer,
    )

    third = linked_list.insert_between(
        30,
        second,
        linked_list._trailer,
    )

    assert len(linked_list) == 3

    assert linked_list._header._next is first
    assert first._next is second
    assert second._next is third
    assert third._next is linked_list._trailer

    assert linked_list._trailer._previous is third
    assert third._previous is second
    assert second._previous is first
    assert first._previous is linked_list._header


def test_insert_between_existing_nodes():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    third = linked_list.insert_between(
        30,
        first,
        linked_list._trailer,
    )

    second = linked_list.insert_between(20, first, third)

    assert len(linked_list) == 3

    assert first._next is second
    assert second._previous is first

    assert second._next is third
    assert third._previous is second


def test_insert_none_as_valid_element():
    linked_list = DoublyLinkedList()

    node = linked_list.insert_between(
        None,
        linked_list._header,
        linked_list._trailer,
    )

    assert len(linked_list) == 1
    assert node._element is None


def test_insert_between_non_adjacent_nodes_raises_value_error():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    second = linked_list.insert_between(
        20,
        first,
        linked_list._trailer,
    )

    with pytest.raises(ValueError):
        linked_list.insert_between(15, first, linked_list._trailer)

    assert len(linked_list) == 2
    assert first._next is second


def test_delete_middle_node():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    last = linked_list.insert_between(
        30,
        first,
        linked_list._trailer,
    )

    middle = linked_list.insert_between(20, first, last)

    assert linked_list.delete_node(middle) == 20

    assert len(linked_list) == 2
    assert first._next is last
    assert last._previous is first


def test_delete_first_node():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    last = linked_list.insert_between(
        20,
        first,
        linked_list._trailer,
    )

    assert linked_list.delete_node(first) == 10

    assert len(linked_list) == 1
    assert linked_list._header._next is last
    assert last._previous is linked_list._header


def test_delete_last_node():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    last = linked_list.insert_between(
        20,
        first,
        linked_list._trailer,
    )

    assert linked_list.delete_node(last) == 20

    assert len(linked_list) == 1
    assert linked_list._trailer._previous is first
    assert first._next is linked_list._trailer


def test_delete_only_node():
    linked_list = DoublyLinkedList()

    node = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    assert linked_list.delete_node(node) == 10

    assert len(linked_list) == 0
    assert linked_list.is_empty()

    assert linked_list._header._next is linked_list._trailer
    assert linked_list._trailer._previous is linked_list._header


def test_delete_node_clears_its_references():
    linked_list = DoublyLinkedList()

    node = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    linked_list.delete_node(node)

    assert node._element is None
    assert node._previous is None
    assert node._next is None


@pytest.mark.parametrize("sentinel_name", ["_header", "_trailer"])
def test_delete_sentinel_node_raises_value_error(sentinel_name):
    linked_list = DoublyLinkedList()
    sentinel = getattr(linked_list, sentinel_name)

    with pytest.raises(ValueError):
        linked_list.delete_node(sentinel)

    assert linked_list.is_empty()


def test_delete_detached_node_raises_value_error():
    linked_list = DoublyLinkedList()

    node = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    linked_list.delete_node(node)

    with pytest.raises(ValueError):
        linked_list.delete_node(node)

    assert linked_list.is_empty()


def test_insert_and_delete_preserve_bidirectional_links():
    linked_list = DoublyLinkedList()

    first = linked_list.insert_between(
        10,
        linked_list._header,
        linked_list._trailer,
    )

    second = linked_list.insert_between(
        20,
        first,
        linked_list._trailer,
    )

    third = linked_list.insert_between(
        30,
        second,
        linked_list._trailer,
    )

    linked_list.delete_node(second)

    # Verify forward links.
    assert linked_list._header._next is first
    assert first._next is third
    assert third._next is linked_list._trailer

    # Verify backward links.
    assert linked_list._trailer._previous is third
    assert third._previous is first
    assert first._previous is linked_list._header

    assert len(linked_list) == 2


def test_large_number_of_insertions_and_deletions():
    linked_list = DoublyLinkedList()

    nodes = []

    for value in range(1000):
        node = linked_list.insert_between(
            value,
            linked_list._trailer._previous,
            linked_list._trailer,
        )
        nodes.append(node)

    assert len(linked_list) == 1000

    for value, node in enumerate(nodes):
        assert node._element == value

    for node in nodes:
        assert linked_list.delete_node(node) == node._element if False else True

    assert linked_list.is_empty()
    assert len(linked_list) == 0
