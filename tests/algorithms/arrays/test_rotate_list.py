import pytest

from algorithms.arrays.rotate_list import rotate_list


# Normal cases

def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]


def test_rotate_by_full_length():
    assert rotate_list([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_rotate_more_than_list_length():
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]


def test_rotate_negative_more_than_list_length():
    assert rotate_list([1, 2, 3, 4, 5], -7) == [3, 4, 5, 1, 2]


# Edge cases

def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_empty_list():
    assert rotate_list([], 5) == []


def test_single_element():
    assert rotate_list([42], 10) == [42]


def test_two_elements():
    assert rotate_list([1, 2], 1) == [2, 1]


def test_list_with_duplicates():
    assert rotate_list([1, 2, 2, 3], 1) == [3, 1, 2, 2]


def test_list_with_different_data_types():
    assert rotate_list([1, "hello", 3.5], 1) == [3.5, 1, "hello"]


def test_input_list_is_not_modified():
    items = [1, 2, 3, 4]
    original = items.copy()

    rotate_list(items, 2)

    assert items == original


# Invalid inputs

def test_non_list_input():
    with pytest.raises(TypeError):
        rotate_list((1, 2, 3), 1)


def test_non_integer_rotation():
    with pytest.raises(TypeError):
        rotate_list([1, 2, 3], 1.5)


def test_string_rotation():
    with pytest.raises(TypeError):
        rotate_list([1, 2, 3], "2")
