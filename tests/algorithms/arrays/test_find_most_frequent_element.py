from algorithms.arrays.find_most_frequent_element import (
    find_most_frequent_element,
)


def test_single_most_frequent_element():
    elements = [1, 3, 4, 3, 2, 3, 5, 6, 7, 8, 1, 8, 2, 8, 7, 8, 3]

    assert find_most_frequent_element(elements) == {3, 8}


def test_multiple_tied_elements():
    assert find_most_frequent_element([1, 2, 1, 2]) == {1, 2}


def test_ties_disabled():
    assert find_most_frequent_element(
        [1, 2, 1, 2],
        include_ties=False
    ) == {1}


def test_unique_most_frequent_with_ties_disabled():
    assert find_most_frequent_element(
        [1, 2, 2, 3],
        include_ties=False
    ) == {2}


def test_all_elements_equally_frequent():
    assert find_most_frequent_element([1, 2, 3, 4]) == {1, 2, 3, 4}


def test_empty_input():
    assert find_most_frequent_element([]) == set()


def test_single_element():
    assert find_most_frequent_element([5]) == {5}


def test_negative_numbers():
    assert find_most_frequent_element([-1, -2, -1, -2, -1]) == {-1}


def test_float_numbers():
    assert find_most_frequent_element([1.5, 2.5, 1.5, 2.5]) == {1.5, 2.5}
