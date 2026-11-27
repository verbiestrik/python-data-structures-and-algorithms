
"""Tests for the merge sort implementation."""

import pytest

from algorithms.sorting.merge_sort import merge_sort


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
def test_merge_sort(numbers, expected):
    result = merge_sort(numbers)

    assert numbers == expected
    assert result is None


def test_merge_sort_is_stable():
    """Elements with equal keys should retain their original order."""

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

    merge_sort(records)

    assert [(record.key, record.identifier) for record in records] == [
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
        (3, 1, 2),
        "321",
    ],
)
def test_merge_sort_rejects_non_lists(invalid_input):
    with pytest.raises(TypeError, match="numbers must be a list"):
        merge_sort(invalid_input)
