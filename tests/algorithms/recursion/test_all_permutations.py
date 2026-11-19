import pytest

from algorithms.recursion.all_permutations import all_permutations


def test_standard_string():

    result = all_permutations("alg")

    expected = [
        "agl",
        "alg",
        "gal",
        "gla",
        "lag",
        "lga"
    ]

    assert result == expected


def test_string_with_repeated_characters():

    result = all_permutations("aab")

    expected = [
        "aab",
        "aba",
        "baa"
    ]

    assert result == expected


def test_string_with_all_identical_characters():

    result = all_permutations("aaa")

    assert result == ["aaa"]


def test_single_character():

    result = all_permutations("a")

    assert result == ["a"]


def test_empty_string():

    result = all_permutations("")

    assert result == [""]


def test_all_permutations_have_correct_length():

    word = "abcd"

    result = all_permutations(word)

    assert all(len(permutation) == len(word) for permutation in result)


def test_all_permutations_are_unique():

    result = all_permutations("aabc")

    assert len(result) == len(set(result))


def test_correct_number_of_unique_permutations():

    # There are 4! / 2! = 12 unique permutations.
    result = all_permutations("aabc")

    assert len(result) == 12


@pytest.mark.parametrize(
    "word",
    [
        None,
        123,
        3.14,
        ["a", "b"],
        ("a", "b"),
        {"a", "b"}
    ]
)
def test_invalid_input(word):

    with pytest.raises(TypeError):
        all_permutations(word)
