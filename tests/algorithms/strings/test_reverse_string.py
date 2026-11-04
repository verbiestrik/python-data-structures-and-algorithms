import pytest

from algorithms.reverse_string import reverse_string


# Normal cases

def test_reverse_string():
    assert reverse_string("Maddalena") == "analeddaM"


def test_reverse_sentence():
    assert reverse_string("Hello world!") == "!dlrow olleH"


def test_reverse_numbers_and_punctuation():
    assert reverse_string("123!abc?") == "?cba!321"


# Edge cases

def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("a") == "a"


def test_two_characters():
    assert reverse_string("ab") == "ba"


def test_palindrome():
    assert reverse_string("radar") == "radar"


def test_preserve_whitespace():
    assert reverse_string("  hello  ") == "  olleh  "


def test_unicode_characters():
    assert reverse_string("café") == "éfac"


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        reverse_string(123)


def test_list_input():
    with pytest.raises(TypeError):
        reverse_string(["a", "b"])
