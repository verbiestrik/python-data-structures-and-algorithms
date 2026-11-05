import pytest

from algorithms.matrices.sum_and_transpose import sum_and_transpose


# Normal cases

def test_rectangular_matrix():
    matrix = [[1, 2, 3], [4, 5, 6]]

    assert sum_and_transpose(matrix) == (
        [6, 15],
        [[1, 4], [2, 5], [3, 6]]
    )


def test_square_matrix():
    matrix = [[1, 2], [3, 4]]

    assert sum_and_transpose(matrix) == (
        [3, 7],
        [[1, 3], [2, 4]]
    )


def test_float_elements():
    matrix = [[1.5, 2.5], [3.5, 4.5]]

    assert sum_and_transpose(matrix) == (
        [4.0, 8.0],
        [[1.5, 3.5], [2.5, 4.5]]
    )


def test_negative_numbers():
    matrix = [[-1, 2], [-3, -4]]

    assert sum_and_transpose(matrix) == (
        [1, -7],
        [[-1, -3], [2, -4]]
    )


# Edge cases

def test_single_element():
    assert sum_and_transpose([[5]]) == ([5], [[5]])


def test_single_row():
    assert sum_and_transpose([[1, 2, 3]]) == (
        [6],
        [[1], [2], [3]]
    )


def test_single_column():
    assert sum_and_transpose([[1], [2], [3]]) == (
        [1, 2, 3],
        [[1, 2, 3]]
    )


def test_empty_rows():
    assert sum_and_transpose([[], []]) == ([0, 0], [])


def test_input_matrix_is_not_modified():
    matrix = [[1, 2], [3, 4]]
    original = [row.copy() for row in matrix]

    sum_and_transpose(matrix)

    assert matrix == original


# Invalid inputs

def test_empty_matrix():
    with pytest.raises(ValueError):
        sum_and_transpose([])


def test_non_rectangular_matrix():
    with pytest.raises(ValueError):
        sum_and_transpose([[1, 2], [3, 4, 5]])


def test_non_list_input():
    with pytest.raises(TypeError):
        sum_and_transpose((1, 2, 3))


def test_non_list_row():
    with pytest.raises(TypeError):
        sum_and_transpose([[1, 2], (3, 4)])


def test_non_numeric_element():
    with pytest.raises(TypeError):
        sum_and_transpose([[1, 2], [3, "four"]])
