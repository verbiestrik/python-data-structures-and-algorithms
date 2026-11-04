import pytest

from algorithms.strings.valid_anagram import valid_anagram


# Normal cases

def test_simple_anagram():
    assert valid_anagram("listen", "silent") is True


def test_different_character_order():
    assert valid_anagram("abcde", "edcba") is True


def test_case_insensitive():
    assert valid_anagram("Listen", "SILENT") is True


def test_ignore_punctuation_and_whitespace():
    assert valid_anagram("Dormitory!!", "Dirty room...") is True


def test_ignore_digits():
    assert valid_anagram("a1b2c3", "c3b2a1") is True


def test_unicode_characters():
    assert valid_anagram("café", "éfac") is True


def test_unicode_casefolding():
    assert valid_anagram("Straße", "STRASSE") is True


# Non-anagrams

def test_different_lengths():
    assert valid_anagram("hello", "hell") is False


def test_different_characters():
    assert valid_anagram("hello", "world") is False


def test_different_character_frequencies():
    assert valid_anagram("aabbcc", "abcdee") is False


def test_same_characters_but_different_frequencies():
    assert valid_anagram("aabc", "abcc") is False


def test_extra_character():
    assert valid_anagram("abc", "abcd") is False


# Edge cases

def test_empty_strings():
    assert valid_anagram("", "") is True


def test_one_empty_string():
    assert valid_anagram("hello", "") is False


def test_only_non_alphabetic_characters():
    assert valid_anagram("123 !!!", "... 456") is True


def test_single_character():
    assert valid_anagram("a", "A") is True


def test_repeated_characters():
    assert valid_anagram("aaaaab", "baaaaa") is True


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        valid_anagram(123, "123")


def test_list_input():
    with pytest.raises(TypeError):
        valid_anagram(["a", "b"], "ab")


def test_second_input_is_not_string():
    with pytest.raises(TypeError):
        valid_anagram("abc", 123)
