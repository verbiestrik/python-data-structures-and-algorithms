import pytest

from algorithms.longest_word import longest_word


# Normal cases

def test_longest_word_list():
    words = ["anb", "asggfvbv", "dfhvj", "kh"]
    assert longest_word(words) == "asggfvbv"


def test_longest_word_sentence():
    text = "The quick brown fox jumps over the lazy dog."
    assert longest_word(text) == "quick"


def test_longest_word_tuple():
    words = ("cat", "elephant", "dog")
    assert longest_word(words) == "elephant"


# Edge cases

def test_single_word():
    assert longest_word(["elephant"]) == "elephant"


def test_first_word_is_longest():
    assert longest_word(["elephant", "cat", "dog"]) == "elephant"


def test_last_word_is_longest():
    assert longest_word(["cat", "dog", "elephant"]) == "elephant"


def test_equal_length_words():
    assert longest_word(["apple", "grape", "melon"]) == "apple"


def test_punctuation_and_numbers():
    text = "Hello! This is a test123, with punctuation."
    assert longest_word(text) == "punctuation"


def test_unicode_characters():
    text = "The café serves excellent pâtisserie."
    assert longest_word(text) == "pâtisserie"


# Invalid inputs

def test_empty_string():
    with pytest.raises(ValueError):
        longest_word("")


def test_text_without_words():
    with pytest.raises(ValueError):
        longest_word("123 !!! ...")


def test_empty_list():
    with pytest.raises(ValueError):
        longest_word([])


def test_empty_word():
    with pytest.raises(ValueError):
        longest_word(["hello", ""])


def test_whitespace_only_word():
    with pytest.raises(ValueError):
        longest_word(["hello", "   "])


def test_non_string_element():
    with pytest.raises(TypeError):
        longest_word(["hello", 123])


def test_invalid_input_type():
    with pytest.raises(TypeError):
        longest_word(123)


def test_set_is_not_supported():
    with pytest.raises(TypeError):
        longest_word({"hello", "world"})
