from algorithms.arrays.merge_two_sorted_lists import merge_two_sorted_lists


def test_basic_merge():
    assert merge_two_sorted_lists(
        [2, 6, 8, 9, 16],
        [1, 2, 5, 6, 17]
    ) == [1, 2, 2, 5, 6, 6, 8, 9, 16, 17]


def test_first_list_empty():
    assert merge_two_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_second_list_empty():
    assert merge_two_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_lists_empty():
    assert merge_two_sorted_lists([], []) == []


def test_different_lengths():
    assert merge_two_sorted_lists(
        [1, 5],
        [2, 3, 4, 6, 7]
    ) == [1, 2, 3, 4, 5, 6, 7]


def test_negative_numbers():
    assert merge_two_sorted_lists(
        [-5, -2, 3],
        [-4, -1, 2]
    ) == [-5, -4, -2, -1, 2, 3]


def test_duplicate_elements():
    assert merge_two_sorted_lists(
        [1, 1, 2],
        [1, 2, 2]
    ) == [1, 1, 1, 2, 2, 2]


def test_original_lists_unchanged():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    merge_two_sorted_lists(list1, list2)

    assert list1 == [1, 3, 5]
    assert list2 == [2, 4, 6]
