import pytest

from algorithms.number_systems.base_conversion import (
    binary_to_decimal,
    binary_to_hexadecimal,
    decimal_to_hexadecimal,
    hexadecimal_to_decimal,
    hexadecimal_to_binary,
    decimal_to_binary,
    convert_base,
)


# --------------------------------------------------
# Binary conversions
# --------------------------------------------------

def test_binary_to_decimal():
    assert binary_to_decimal("11010") == 26


def test_binary_to_hexadecimal():
    assert binary_to_hexadecimal("11010") == "1A"


def test_binary_with_leading_zeros():
    assert binary_to_hexadecimal("00001111") == "F"


# --------------------------------------------------
# Decimal conversions
# --------------------------------------------------

def test_decimal_to_binary():
    assert decimal_to_binary(26) == "11010"


def test_decimal_to_hexadecimal():
    assert decimal_to_hexadecimal(26) == "1A"


# --------------------------------------------------
# Hexadecimal conversions
# --------------------------------------------------

def test_hexadecimal_to_decimal():
    assert hexadecimal_to_decimal("1F") == 31


def test_hexadecimal_to_binary():
    assert hexadecimal_to_binary("1F") == "11111"


def test_lowercase_hexadecimal():
    assert hexadecimal_to_decimal("1f") == 31


# --------------------------------------------------
# Arbitrary base conversions
# --------------------------------------------------

def test_binary_to_base_36():
    assert convert_base("11010", 2, 36) == "Q"


def test_base_36_to_binary():
    assert convert_base("Q", 36, 2) == "11010"


def test_hexadecimal_to_base_8():
    assert convert_base("FF", 16, 8) == "377"


def test_base_8_to_hexadecimal():
    assert convert_base("377", 8, 16) == "FF"


def test_same_base_conversion():
    assert convert_base("11010", 2, 2) == "11010"


# --------------------------------------------------
# Zero and negative numbers
# --------------------------------------------------

def test_zero_conversions():
    assert decimal_to_binary(0) == "0"
    assert decimal_to_hexadecimal(0) == "0"
    assert binary_to_decimal("0") == 0


def test_negative_decimal_to_binary():
    assert decimal_to_binary(-26) == "-11010"


def test_negative_binary_to_decimal():
    assert binary_to_decimal("-11010") == -26


def test_negative_hexadecimal_to_binary():
    assert hexadecimal_to_binary("-1F") == "-11111"


# --------------------------------------------------
# Leading zeros and signs
# --------------------------------------------------

def test_leading_zeros():
    assert binary_to_decimal("00011010") == 26
    assert hexadecimal_to_decimal("0001F") == 31


def test_positive_sign():
    assert binary_to_decimal("+11010") == 26


# --------------------------------------------------
# Invalid inputs
# --------------------------------------------------

def test_invalid_binary():
    with pytest.raises(ValueError):
        binary_to_decimal("10201")


def test_invalid_hexadecimal():
    with pytest.raises(ValueError):
        hexadecimal_to_decimal("1G")


def test_empty_input():
    with pytest.raises(ValueError):
        binary_to_decimal("")


def test_invalid_base_too_low():
    with pytest.raises(ValueError):
        convert_base("101", 1, 10)


def test_invalid_base_too_high():
    with pytest.raises(ValueError):
        convert_base("101", 2, 37)


def test_non_integer_decimal():
    with pytest.raises(TypeError):
        decimal_to_binary(10.5)


def test_invalid_character_for_base():
    with pytest.raises(ValueError):
        convert_base("102", 2, 16)
