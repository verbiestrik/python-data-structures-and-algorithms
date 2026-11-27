
"""Tests for the quick sort implementation."""

import pytest

from algorithms.sorting.quick_sort import quick_sort
from data_structures.queues.linked_queue import LinkedQueue


def make_queue(elements):
    """Create a LinkedQueue containing the given elements."""
    queue = LinkedQueue()

    for element in elements:
        queue.enqueue(element)

    return queue


def queue_to_list(queue):
    """Remove all elements from a queue and return them as a list."""
    elements = []

    while not queue.is_empty():
        elements.append(queue.dequeue())

    return elements


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([4, 2, 7, 4, 6, 4, 3, 5, 6, 8, 3, 2, 9, 1, 57, 4, 11],
         [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 8, 9, 11, 57]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-3, 0, -1, 2, -3], [-3, -3, -1, 0, 2]),
        ([7, 7, 7, 7], [7, 7, 7, 7]),
        ([3, 1, 2, 1, 3, 2], [1, 1, 2, 2, 3, 3]),
    ],
)
def test_quick_sort(numbers, expected):
    queue = make_queue(numbers)
    original_size = len(queue)

    quick_sort(queue)

    assert len(queue) == original_size
    assert queue_to_list(queue) == expected
    assert queue.is_empty()


def test_quick_sort_is_stable():
    """Elements with equivalent keys should retain their original order."""

    class Record:
        def __init__(self, key, identifier):
            self.key = key
            self.identifier = identifier

        def __lt__(self, other):
            return self.key < other.key

    records = [
        Record(2, "first"),
        Record(1, "second"),
        Record(2, "third"),
        Record(1, "fourth"),
        Record(2, "fifth"),
    ]

    queue = make_queue(records)
    quick_sort(queue)

    result = queue_to_list(queue)

    assert [(record.key, record.identifier) for record in result] == [
        (1, "second"),
        (1, "fourth"),
        (2, "first"),
        (2, "third"),
        (2, "fifth"),
    ]


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        [],
        (),
        "numbers",
    ],
)
def test_quick_sort_rejects_non_linked_queues(invalid_input):
    with pytest.raises(TypeError, match="numbers must be a LinkedQueue"):
        quick_sort(invalid_input)
