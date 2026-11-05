import pytest

from algorithms.arrays.two_sum import two_sum


# Normal cases

def test_basic_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_pair_in_middle():
    assert two_sum([1, 3, 8, 5, 7], 13) == (2, 4)


def test_pair_at_end():
    assert two_sum([1, 2, 3, 4, 5], 9) == (3, 4)


def test_negative_numbers():
    assert two_sum([-3, 4, 2, 5], 1) == (0, 2)


def test_float_numbers():
    assert two_sum([1.5, 2.5, 3.0, 4.0], 7.0) == (2, 3)


def test_mixed_integers_and_floats():
    assert two_sum([1, 2.5, 3, 4.5], 7.0) == (1, 3)


def test_duplicate_numbers():
    assert two_sum([3, 3], 6) == (0, 1)


def test_first_pair_found():
    assert two_sum([1, 4, 2, 3], 5) == (0, 1)


# Edge cases

def test_no_valid_pair():
    assert two_sum([1, 2, 3], 10) is None


def test_empty_sequence():
    assert two_sum([], 5) is None


def test_single_element():
    assert two_sum([5], 10) is None


def test_element_cannot_be_used_twice():
    assert two_sum([5, 1, 2], 10) is None


def test_two_identical_elements():
    assert two_sum([5, 5], 10) == (0, 1)


def test_zero_target():
    assert two_sum([-2, 2, -1, 1], 0) == (0, 1)


def test_tuple_input():
    assert two_sum((2, 7, 11, 15), 9) == (0, 1)


# Invalid inputs

def test_non_sequence_input():
    with pytest.raises(TypeError):
        two_sum(123, 5)


def test_string_input():
    with pytest.raises(TypeError):
        two_sum("123", 5)


def test_non_numeric_element():
    with pytest.raises(TypeError):
        two_sum([1, 2, "3"], 4)


def test_invalid_target():
    with pytest.raises(TypeError):
        two_sum([1, 2, 3], "4")
