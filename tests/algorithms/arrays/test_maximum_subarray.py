import pytest

from algorithms.arrays.maximum_subarray import maximum_sum_cont_subarr


# Normal cases

def test_classic_example():
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_sum_cont_subarr(numbers) == 6


def test_all_positive_numbers():
    assert maximum_sum_cont_subarr([1, 2, 3, 4, 5]) == 15


def test_all_negative_numbers():
    assert maximum_sum_cont_subarr([-8, -3, -6, -2, -5, -4]) == -2


def test_mixed_positive_and_negative_numbers():
    assert maximum_sum_cont_subarr([5, -2, 3, -1, 2]) == 7


def test_negative_numbers_between_positive_sequences():
    assert maximum_sum_cont_subarr([1, 2, -10, 4, 5]) == 9


def test_float_numbers():
    assert maximum_sum_cont_subarr([1.5, -0.5, 2.0, -1.0]) == 3.0


def test_tuple_input():
    assert maximum_sum_cont_subarr((-2, 1, -3, 4, -1, 2, 1)) == 6


# Edge cases

def test_single_element():
    assert maximum_sum_cont_subarr([5]) == 5


def test_single_negative_element():
    assert maximum_sum_cont_subarr([-5]) == -5


def test_all_zeros():
    assert maximum_sum_cont_subarr([0, 0, 0, 0]) == 0


def test_one_positive_element():
    assert maximum_sum_cont_subarr([-5, -3, 10, -8, -2]) == 10


def test_maximum_subarray_at_start():
    assert maximum_sum_cont_subarr([5, 4, -10, 1, 2]) == 9


def test_maximum_subarray_at_end():
    assert maximum_sum_cont_subarr([-10, 1, 2, 5, 4]) == 12


def test_maximum_subarray_is_entire_sequence():
    assert maximum_sum_cont_subarr([1, 2, -1, 3]) == 5


def test_input_is_not_modified():
    numbers = [-2, 1, -3, 4, -1, 2, 1]
    original = numbers.copy()

    maximum_sum_cont_subarr(numbers)

    assert numbers == original


# Invalid inputs

def test_empty_sequence():
    with pytest.raises(ValueError):
        maximum_sum_cont_subarr([])


def test_integer_input():
    with pytest.raises(TypeError):
        maximum_sum_cont_subarr(123)


def test_string_input():
    with pytest.raises(TypeError):
        maximum_sum_cont_subarr("123")


def test_non_numeric_element():
    with pytest.raises(TypeError):
        maximum_sum_cont_subarr([1, 2, "three"])


def test_mixed_valid_and_invalid_elements():
    with pytest.raises(TypeError):
        maximum_sum_cont_subarr([1, 2.5, None])
