
"""Tests for the in-place quick sort implementation."""

import pytest

from algorithms.sorting.quick_sort_in_place import quick_sort, partition


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
    result = quick_sort(numbers)

    assert numbers == expected
    assert result is None


def test_quick_sort_modifies_original_list():
    numbers = [4, 2, 7, 1, 3]
    original_id = id(numbers)

    quick_sort(numbers)

    assert id(numbers) == original_id
    assert numbers == [1, 2, 3, 4, 7]


def test_partition():
    numbers = [3, 7, 2, 5, 1, 4]
    pivot = numbers[-1]

    pivot_index = partition(numbers, 0, len(numbers) - 1)

    assert numbers[pivot_index] == pivot
    assert all(value <= pivot for value in numbers[:pivot_index])
    assert all(value > pivot for value in numbers[pivot_index + 1:])


def test_quick_sort_large_list():
    numbers = list(range(1000, 0, -1))

    quick_sort(numbers)

    assert numbers == list(range(1, 1001))


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        (3, 1, 2),
        "321",
    ],
)
def test_quick_sort_rejects_non_lists(invalid_input):
    with pytest.raises(TypeError, match="numbers must be a list"):
        quick_sort(invalid_input)
