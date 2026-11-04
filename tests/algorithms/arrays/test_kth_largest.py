import pytest

from algorithms.sequences.kth_largest import kth_largest


# Normal cases

def test_largest_element():
    assert kth_largest([4, 8, 2, 10, 6], 1) == 10


def test_second_largest():
    assert kth_largest([4, 8, 2, 10, 6], 2) == 8


def test_third_largest():
    assert kth_largest([4, 8, 2, 10, 6], 3) == 6


def test_duplicates():
    assert kth_largest([4, 4, 4, 4, 4, 5], 2) == 4


def test_duplicates_interspersed():
    assert kth_largest([5, 3, 5, 2, 3, 1], 2) == 3


def test_negative_numbers():
    assert kth_largest([-5, -2, -10, -1, -7], 2) == -2


def test_mixed_positive_and_negative_numbers():
    assert kth_largest([-5, 3, 0, 10, -2], 3) == 0


def test_float_numbers():
    assert kth_largest([1.5, 3.7, 2.1, 4.2], 2) == 3.7


def test_tuple_input():
    assert kth_largest((5, 1, 8, 3), 2) == 5


# Edge cases

def test_single_element():
    assert kth_largest([42], 1) == 42


def test_all_elements_equal():
    assert kth_largest([5, 5, 5, 5], 1) == 5


def test_all_elements_equal_and_k_too_large():
    assert kth_largest([5, 5, 5, 5], 2) is None


def test_k_larger_than_number_of_distinct_elements():
    assert kth_largest([1, 2, 2, 3], 4) is None


def test_empty_sequence():
    assert kth_largest([], 1) is None


def test_input_is_not_modified():
    numbers = [4, 1, 7, 3]
    original = numbers.copy()

    kth_largest(numbers, 2)

    assert numbers == original


# Invalid inputs

def test_zero_k():
    with pytest.raises(ValueError):
        kth_largest([1, 2, 3], 0)


def test_negative_k():
    with pytest.raises(ValueError):
        kth_largest([1, 2, 3], -1)


def test_non_integer_k():
    with pytest.raises(TypeError):
        kth_largest([1, 2, 3], 2.5)


def test_boolean_k():
    with pytest.raises(TypeError):
        kth_largest([1, 2, 3], True)


def test_invalid_sequence_type():
    with pytest.raises(TypeError):
        kth_largest(123, 1)


def test_string_input():
    with pytest.raises(TypeError):
        kth_largest("12345", 1)


def test_non_numeric_element():
    with pytest.raises(TypeError):
        kth_largest([1, 2, "three"], 1)


def test_boolean_element():
    with pytest.raises(TypeError):
        kth_largest([1, True, 3], 1)


def test_nan_element():
    with pytest.raises(ValueError):
        kth_largest([1, float("nan"), 3], 1)
