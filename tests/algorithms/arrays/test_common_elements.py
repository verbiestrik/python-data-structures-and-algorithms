import pytest

from algorithms.arrays.common_elements import common_elements


# Normal cases

def test_common_elements():
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
    numbers2 = [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]

    assert common_elements(numbers1, numbers2) == [1, 3, 5, 7, 9]


def test_preserve_first_sequence_order():
    assert common_elements([5, 3, 1, 4], [1, 3, 5]) == [5, 3, 1]


def test_duplicates_in_both_sequences():
    assert common_elements([1, 1, 2, 2, 3], [1, 1, 1, 2, 2]) == [1, 2]


def test_negative_numbers():
    assert common_elements([-1, -2, 3, -4], [-4, -2, 5]) == [-2, -4]


def test_float_numbers():
    assert common_elements([1.5, 2.5, 3.5], [3.5, 1.5]) == [1.5, 3.5]


def test_mixed_integers_and_floats():
    assert common_elements([1, 2.5, 3], [3.0, 1.0]) == [1, 3]


def test_tuple_inputs():
    assert common_elements((1, 2, 3), (2, 3, 4)) == [2, 3]


# Edge cases

def test_no_common_elements():
    assert common_elements([1, 2, 3], [4, 5, 6]) == []


def test_empty_first_sequence():
    assert common_elements([], [1, 2, 3]) == []


def test_empty_second_sequence():
    assert common_elements([1, 2, 3], []) == []


def test_both_sequences_empty():
    assert common_elements([], []) == []


def test_single_common_element():
    assert common_elements([1, 2, 3], [3]) == [3]


def test_all_elements_common():
    assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_all_elements_repeated():
    assert common_elements([5, 5, 5], [5, 5]) == [5]


def test_inputs_are_not_modified():
    numbers1 = [1, 2, 3, 4]
    numbers2 = [2, 3, 5]

    original1 = numbers1.copy()
    original2 = numbers2.copy()

    common_elements(numbers1, numbers2)

    assert numbers1 == original1
    assert numbers2 == original2


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        common_elements(123, [1, 2, 3])


def test_string_input():
    with pytest.raises(TypeError):
        common_elements("123", [1, 2, 3])


def test_non_numeric_element():
    with pytest.raises(TypeError):
        common_elements([1, 2, "3"], [1, 2, 3])


def test_mixed_valid_and_invalid_elements():
    with pytest.raises(TypeError):
        common_elements([1, 2.5, None], [1, 2, 3])
