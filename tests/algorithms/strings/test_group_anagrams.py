import pytest

from algorithms.strings.group_anagrams import group_anagrams


# Normal cases

def test_basic_grouping():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    assert group_anagrams(words) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ]


def test_original_example():
    words = ["tan", "eat", "tea", "ant", "ate", "nat", "bat"]

    assert group_anagrams(words) == [
        ["tan", "ant", "nat"],
        ["eat", "tea", "ate"],
        ["bat"]
    ]


def test_case_insensitive():
    words = ["Listen", "silent", "ENLIST", "hello"]

    assert group_anagrams(words) == [
        ["Listen", "silent", "ENLIST"],
        ["hello"]
    ]


def test_ignore_punctuation_and_whitespace():
    words = ["a!b!c", "C b a", "abc", "xyz"]

    assert group_anagrams(words) == [
        ["a!b!c", "C b a", "abc"],
        ["xyz"]
    ]


def test_ignore_digits():
    words = ["a1b2c3", "3c2b1a", "abc", "xyz"]

    assert group_anagrams(words) == [
        ["a1b2c3", "3c2b1a", "abc"],
        ["xyz"]
    ]


def test_unicode_characters():
    words = ["café", "éfac", "hello"]

    assert group_anagrams(words) == [
        ["café", "éfac"],
        ["hello"]
    ]


def test_unicode_casefolding():
    words = ["Straße", "STRASSE", "hello"]

    assert group_anagrams(words) == [
        ["Straße", "STRASSE"],
        ["hello"]
    ]


# Edge cases

def test_empty_sequence():
    assert group_anagrams([]) == []


def test_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]


def test_all_words_are_anagrams():
    words = ["abc", "bca", "cab", "acb"]

    assert group_anagrams(words) == [
        ["abc", "bca", "cab", "acb"]
    ]


def test_no_anagrams():
    words = ["cat", "dog", "fish"]

    assert group_anagrams(words) == [
        ["cat"],
        ["dog"],
        ["fish"]
    ]


def test_duplicate_words():
    words = ["abc", "abc", "bca"]

    assert group_anagrams(words) == [
        ["abc", "abc", "bca"]
    ]


def test_empty_strings():
    words = ["", "hello", ""]

    assert group_anagrams(words) == [
        ["", ""],
        ["hello"]
    ]


def test_only_non_alphabetic_characters():
    words = ["123", "!!!", "...", "abc"]

    assert group_anagrams(words) == [
        ["123", "!!!", "..."],
        ["abc"]
    ]


def test_tuple_input():
    words = ("eat", "tea", "bat")

    assert group_anagrams(words) == [
        ["eat", "tea"],
        ["bat"]
    ]


def test_input_is_not_modified():
    words = ["eat", "tea", "bat"]
    original = words.copy()

    group_anagrams(words)

    assert words == original


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        group_anagrams(123)


def test_string_input():
    with pytest.raises(TypeError):
        group_anagrams("hello")


def test_non_string_element():
    with pytest.raises(TypeError):
        group_anagrams(["hello", 123])


def test_mixed_valid_and_invalid_elements():
    with pytest.raises(TypeError):
        group_anagrams(["eat", "tea", None])
