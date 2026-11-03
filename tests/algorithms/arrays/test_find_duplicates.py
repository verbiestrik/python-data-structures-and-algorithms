from algorithms.arrays.find_duplicates import find_duplicates

def test_multiple_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5, 5, 6, 1]) == {1, 5}


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == set()


def test_empty_input():
    assert find_duplicates([]) == set()


def test_number_appearing_multiple_times():
    assert find_duplicates([1, 1, 1, 1]) == {1}


def test_negative_and_float_numbers():
    assert find_duplicates([-1, 2.5, -1, 2.5]) == {-1, 2.5}
