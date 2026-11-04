import pytest

from algorithms.strings.longest_substring import longest_substring


# Normal cases

def test_all_unique_characters():
    assert longest_substring("abcdefg") == 7


def test_repeated_characters():
    assert longest_substring("abcabcbb") == 3


def test_long_repeated_sequence():
    assert longest_substring("abcdefgabcdeabcdabc") == 7


def test_example_pwwkew():
    assert longest_substring("pwwkew") == 3


def test_repeated_characters_at_start():
    assert longest_substring("aab") == 2


def test_repeated_characters_at_end():
    assert longest_substring("abcc") == 3


def test_case_sensitive():
    assert longest_substring("aAbB") == 4


# Edge cases

def test_empty_string():
    assert longest_substring("") == 0


def test_single_character():
    assert longest_substring("a") == 1


def test_all_characters_identical():
    assert longest_substring("aaaaaaaa") == 1


def test_two_distinct_characters():
    assert longest_substring("abababab") == 2


def test_repeated_character_outside_current_window():
    assert longest_substring("abba") == 2


def test_whitespace_and_punctuation():
    assert longest_substring("a b!a") == 4


def test_unicode_characters():
    assert longest_substring("caféabc") == 7


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        longest_substring(123)


def test_list_input():
    with pytest.raises(TypeError):
        longest_substring(["a", "b"])
