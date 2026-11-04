import pytest

from algorithms.heaps.find_k_most_frequent_elements import (
    find_k_most_frequent_elements,
)


METHODS = [
    "repeated_max",
    "sorting",
    "full_heap",
    "bounded_heap",
]


@pytest.mark.parametrize("method", METHODS)
def test_basic_example(method):
    elements = [
        1, 3, 4, 3, 2, 3, 5, 6, 7,
        8, 1, 8, 2, 8, 7, 8, 3, 8
    ]

    assert find_k_most_frequent_elements(
        elements, 3, method
    ) == [(8, 5), (3, 4), (1, 2)]


@pytest.mark.parametrize("method", METHODS)
def test_multiple_tied_frequencies(method):
    assert find_k_most_frequent_elements(
        [2, 1, 2, 1, 3], 2, method
    ) == [(2, 2), (1, 2)]


@pytest.mark.parametrize("method", METHODS)
def test_k_larger_than_distinct_elements(method):
    assert find_k_most_frequent_elements(
        [1, 2, 1, 3, 2], 10, method
    ) == [(1, 2), (2, 2), (3, 1)]


@pytest.mark.parametrize("method", METHODS)
def test_k_equal_to_one(method):
    assert find_k_most_frequent_elements(
        [1, 2, 2, 3, 3, 3], 1, method
    ) == [(3, 3)]


@pytest.mark.parametrize("method", METHODS)
def test_k_equal_to_zero(method):
    assert find_k_most_frequent_elements(
        [1, 2, 3], 0, method
    ) == []


@pytest.mark.parametrize("method", METHODS)
def test_empty_input(method):
    assert find_k_most_frequent_elements([], 3, method) == []


@pytest.mark.parametrize("method", METHODS)
def test_all_elements_equally_frequent(method):
    assert find_k_most_frequent_elements(
        [4, 3, 2, 1], 3, method
    ) == [(4, 1), (3, 1), (2, 1)]


@pytest.mark.parametrize("method", METHODS)
def test_negative_numbers(method):
    assert find_k_most_frequent_elements(
        [-1, -2, -1, -2, -1], 2, method
    ) == [(-1, 3), (-2, 2)]


def test_negative_k():
    with pytest.raises(ValueError):
        find_k_most_frequent_elements([1, 2, 3], -1)


def test_non_integer_k():
    with pytest.raises(TypeError):
        find_k_most_frequent_elements([1, 2, 3], 2.5)


def test_invalid_method():
    with pytest.raises(ValueError):
        find_k_most_frequent_elements(
            [1, 2, 3], 2, "invalid"
        )
