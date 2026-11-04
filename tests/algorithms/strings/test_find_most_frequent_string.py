import pytest

from algorithms.strings.find_most_frequent_string import (
    find_most_frequent_string,
)


def test_single_most_frequent_string():
    strings = ["apple", "banana", "apple", "orange", "apple"]

    assert find_most_frequent_string(strings) == ["apple"]


def test_multiple_tied_strings():
    strings = ["pear", "apple", "pear", "apple", "banana"]

    assert find_most_frequent_string(strings) == ["apple", "pear"]


def test_ties_disabled():
    strings = ["pear", "apple", "pear", "apple", "banana"]

    assert find_most_frequent_string(
        strings, include_ties=False
    ) == ["apple"]


def test_unique_most_frequent_with_ties_disabled():
    strings = ["banana", "apple", "banana", "orange"]

    assert find_most_frequent_string(
        strings, include_ties=False
    ) == ["banana"]


def test_all_strings_equally_frequent():
    strings = ["pear", "banana", "apple"]

    assert find_most_frequent_string(strings) == [
        "apple", "banana", "pear"
    ]


def test_empty_input():
    assert find_most_frequent_string([]) == []


def test_single_string():
    assert find_most_frequent_string(["hello"]) == ["hello"]


def test_generator_input():
    strings = (s for s in ["cat", "dog", "cat"])

    assert find_most_frequent_string(strings) == ["cat"]


def test_case_sensitive_strings():
    strings = ["Apple", "apple", "Apple"]

    assert find_most_frequent_string(strings) == ["Apple"]
