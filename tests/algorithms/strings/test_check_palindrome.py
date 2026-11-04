import pytest

from algorithms.strings.check_palindrome import check_palindrome


# Normal cases

def test_simple_palindrome():
    assert check_palindrome("radar") is True


def test_case_insensitive():
    assert check_palindrome("RaceCar") is True


def test_sentence_palindrome():
    assert check_palindrome("Never odd or even???") is True


def test_palindrome_with_numbers():
    assert check_palindrome("A1b2b1a") is True


def test_non_palindrome():
    assert check_palindrome("hello") is False


def test_non_palindrome_sentence():
    assert check_palindrome("This is not a palindrome.") is False


# Edge cases

def test_empty_string():
    assert check_palindrome("") is True


def test_single_character():
    assert check_palindrome("a") is True


def test_single_non_alphabetic_character():
    assert check_palindrome("!") is True


def test_only_non_alphabetic_characters():
    assert check_palindrome("123 !!! ...") is True


def test_palindrome_with_unicode_characters():
    assert check_palindrome("Ésope reste ici et se repose") is True


def test_two_different_characters():
    assert check_palindrome("ab") is False


# Invalid inputs

def test_integer_input():
    with pytest.raises(TypeError):
        check_palindrome(123)


def test_list_input():
    with pytest.raises(TypeError):
        check_palindrome(["a", "b"])
