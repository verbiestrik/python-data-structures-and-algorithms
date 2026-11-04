import pytest

from algorithms.heaps.find_k_most_frequent_strings import (
    find_k_most_frequent_strings,
)


METHODS = [
    "repeated_max",
    "sorting",
    "full_heap",
    "bounded_heap",
]


@pytest.mark.parametrize("method", METHODS)
def test_basic_example(method):
    strings = [
        "apple", "banana", "apple", "orange",
        "banana", "apple", "pear", "banana",
        "apple", "pear"
    ]

    assert find_k_most_frequent_strings(
        strings, 3, method
    ) == [
        ("apple", 4),
        ("banana", 3),
        ("pear", 2)
    ]


@pytest.mark.parametrize("method", METHODS)
def test_alphabetical_tie_breaking(method):
    strings = [
        "pear", "banana", "apple",
        "pear", "banana", "apple"
    ]

    assert find_k_most_frequent_strings(
        strings, 3, method
    ) == [
        ("apple", 2),
        ("banana", 2),
        ("pear", 2)
    ]


@pytest.mark.parametrize("method", METHODS)
def test_tie_at_k_boundary(method):
    strings = [
        "dog", "cat", "bird",
        "dog", "cat", "bird"
    ]

    assert find_k_most_frequent_strings(
        strings, 2, method
    ) == [
        ("bird", 2),
        ("cat", 2)
    ]


@pytest.mark.parametrize("method", METHODS)
def test_k_equal_to_one(method):
    strings = ["apple", "banana", "banana", "orange"]

    assert find_k_most_frequent_strings(
        strings, 1, method
    ) == [("banana", 2)]


@pytest.mark.parametrize("method", METHODS)
def test_k_larger_than_distinct_strings(method):
    strings = ["apple", "banana", "apple", "orange"]

    assert find_k_most_frequent_strings(
        strings, 10, method
    ) == [
        ("apple", 2),
        ("banana", 1),
        ("orange", 1)
    ]


@pytest.mark.parametrize("method", METHODS)
def test_all_strings_equally_frequent(method):
    strings = ["pear", "banana", "apple"]

    assert find_k_most_frequent_strings(
        strings, 3, method
    ) == [
        ("apple", 1),
        ("banana", 1),
        ("pear", 1)
    ]


@pytest.mark.parametrize("method", METHODS)
def test_k_equal_to_zero(method):
    assert find_k_most_frequent_strings(
        ["apple", "banana"], 0, method
    ) == []


@pytest.mark.parametrize("method", METHODS)
def test_empty_input(method):
    assert find_k_most_frequent_strings([], 3, method) == []


@pytest.mark.parametrize("method", METHODS)
def test_case_sensitive_strings(method):
    strings = ["Apple", "apple", "Apple", "banana"]

    assert find_k_most_frequent_strings(
        strings, 3, method
    ) == [
        ("Apple", 2),
        ("apple", 1),
        ("banana", 1)
    ]


def test_negative_k():
    with pytest.raises(ValueError):
        find_k_most_frequent_strings(["apple"], -1)


def test_non_integer_k():
    with pytest.raises(TypeError):
        find_k_most_frequent_strings(["apple"], 2.5)


def test_invalid_method():
    with pytest.raises(ValueError):
        find_k_most_frequent_strings(
            ["apple"], 1, "invalid"
        )


def test_generator_input():
    strings = (s for s in ["apple", "banana", "apple"])

    assert find_k_most_frequent_strings(
        strings, 2, "sorting"
    ) == [
        ("apple", 2),
        ("banana", 1)
    ]
