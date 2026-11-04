import pytest

from algorithms.numbers.find_primes import find_primes


# Normal cases

def test_primes_up_to_10():
    assert find_primes(10) == [2, 3, 5, 7]


def test_primes_up_to_20():
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_primes_up_to_100():
    assert find_primes(100) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97
    ]


def test_prime_upper_limit():
    assert find_primes(13) == [2, 3, 5, 7, 11, 13]


def test_composite_upper_limit():
    assert find_primes(12) == [2, 3, 5, 7, 11]


# Edge cases

def test_zero():
    assert find_primes(0) == []


def test_one():
    assert find_primes(1) == []


def test_two():
    assert find_primes(2) == [2]


def test_three():
    assert find_primes(3) == [2, 3]


# Invalid inputs

def test_negative_input():
    with pytest.raises(ValueError):
        find_primes(-10)


def test_float_input():
    with pytest.raises(TypeError):
        find_primes(10.5)


def test_string_input():
    with pytest.raises(TypeError):
        find_primes("100")
