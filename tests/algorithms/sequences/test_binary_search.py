import pytest

from algorithms.searching.binary_search import binary_search


def test_target_in_middle():

    data = [1, 3, 5, 7, 9, 11, 13]

    assert binary_search(data, 7) is True


def test_target_at_beginning():

    data = [1, 3, 5, 7, 9, 11, 13]

    assert binary_search(data, 1) is True


def test_target_at_end():

    data = [1, 3, 5, 7, 9, 11, 13]

    assert binary_search(data, 13) is True


def test_target_not_present():

    data = [1, 3, 5, 7, 9, 11, 13]

    assert binary_search(data, 8) is False


def test_target_smaller_than_all_elements():

    data = [2, 4, 6, 8]

    assert binary_search(data, 1) is False


def test_target_larger_than_all_elements():

    data = [2, 4, 6, 8]

    assert binary_search(data, 10) is False


def test_empty_sequence():

    assert binary_search([], 5) is False


def test_single_element_found():

    assert binary_search([5], 5) is True


def test_single_element_not_found():

    assert binary_search([5], 3) is False


def test_two_elements():

    data = [3, 7]

    assert binary_search(data, 3) is True
    assert binary_search(data, 7) is True
    assert binary_search(data, 5) is False


def test_duplicate_elements():

    data = [1, 2, 2, 2, 3, 4]

    assert binary_search(data, 2) is True


def test_tuple_input():

    data = (1, 3, 5, 7, 9)

    assert binary_search(data, 5) is True


@pytest.mark.parametrize(
    "data",
    [
        None,
        123,
        3.14,
        "12345",
        b"12345",
        bytearray(b"12345")
    ]
)
def test_invalid_input_sequence(data):

    with pytest.raises(TypeError):
        binary_search(data, 3)
