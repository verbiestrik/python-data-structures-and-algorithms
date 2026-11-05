import pytest

from algorithms.sequences.moving_average import moving_average


# Normal cases

def test_basic_moving_average():
    assert moving_average([2, 4, 6, 8, 10], 3) == [4.0, 6.0, 8.0]


def test_window_size_two():
    assert moving_average([1, 3, 5, 7], 2) == [2.0, 4.0, 6.0]


def test_window_size_one():
    assert moving_average([1, 2, 3, 4], 1) == [1.0, 2.0, 3.0, 4.0]


def test_window_size_equals_sequence_length():
    assert moving_average([1, 2, 3, 4], 4) == [2.5]


def test_float_numbers():
    assert moving_average([1.5, 2.5, 4.0], 2) == [2.0, 3.25]


def test_negative_numbers():
    assert moving_average([-2, 0, 2, 4], 2) == [-1.0, 1.0, 3.0]


def test_tuple_input():
    assert moving_average((1, 2, 3, 4), 2) == [1.5, 2.5, 3.5]


# Edge cases

def test_empty_sequence():
    assert moving_average([], 3) == []


def test_window_larger_than_sequence():
    assert moving_average([1, 2, 3], 5) == []


def test_all_elements_equal():
    assert moving_average([5, 5, 5, 5], 2) == [5.0, 5.0, 5.0]


def test_input_is_not_modified():
    numbers = [1, 2, 3, 4]
    original = numbers.copy()

    moving_average(numbers, 2)

    assert numbers == original


# Invalid inputs

def test_zero_window_size():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)


def test_negative_window_size():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], -1)


def test_float_window_size():
    with pytest.raises(TypeError):
        moving_average([1, 2, 3], 2.5)


def test_non_sequence_input():
    with pytest.raises(TypeError):
        moving_average(123, 2)


def test_non_numeric_element():
    with pytest.raises(TypeError):
        moving_average([1, 2, "three"], 2)
