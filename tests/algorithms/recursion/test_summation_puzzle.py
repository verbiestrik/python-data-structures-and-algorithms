import pytest

from algorithms.recursion.summation_puzzle import solve_summation_puzzle


def test_unique_solution():

    solutions = solve_summation_puzzle(["I", "BB"], "ILL")

    assert solutions == [
        {"I": 1, "B": 9, "L": 0}
    ]


def test_multiple_solutions():

    # A + A = B
    solutions = solve_summation_puzzle(["A", "A"], "B")

    expected = [
        {"A": 1, "B": 2},
        {"A": 2, "B": 4},
        {"A": 3, "B": 6},
        {"A": 4, "B": 8}
    ]

    assert solutions == expected


def test_no_solution():

    # A + A = A has no valid solution because A must be non-zero.
    solutions = solve_summation_puzzle(["A", "A"], "A")

    assert solutions == []


def test_case_insensitive_input():

    solutions = solve_summation_puzzle(["i", "bb"], "ill")

    assert solutions == [
        {"I": 1, "B": 9, "L": 0}
    ]


def test_all_solutions_use_unique_digits():

    solutions = solve_summation_puzzle(["A", "B"], "C")

    for solution in solutions:

        assert len(solution.values()) == len(set(solution.values()))


def test_all_solutions_satisfy_equation():

    terms = ["A", "B"]
    result = "C"

    solutions = solve_summation_puzzle(terms, result)

    for solution in solutions:

        terms_total = sum(
            int("".join(str(solution[letter]) for letter in word))
            for word in terms
        )

        result_value = int(
            "".join(str(solution[letter]) for letter in result)
        )

        assert terms_total == result_value


def test_no_leading_zeros():

    # I + BB = ILL has a unique solution with L = 0.
    # However, the first letters I and B cannot be zero.
    solutions = solve_summation_puzzle(["I", "BB"], "ILL")

    for solution in solutions:

        assert solution["I"] != 0
        assert solution["B"] != 0
        assert solution["I"] == 1


def test_repeated_letters():

    solutions = solve_summation_puzzle(["AAB"], "AAC")

    # Repeated occurrences of a letter must use the same digit.
    for solution in solutions:

        assert len(solution) == 3
        assert len(set(solution.values())) == 3


def test_too_many_distinct_letters():

    with pytest.raises(ValueError):
        solve_summation_puzzle(["ABCDEFGHIJK"], "ABCDEFGHIJK")


@pytest.mark.parametrize(
    "terms, result, exception",
    [
        ([], "A", ValueError),
        ("A", "B", TypeError),
        (None, "A", TypeError),
        ([123], "A", TypeError),
        ([""], "A", ValueError),
        (["ABC"], "", ValueError),
        (["A B"], "C", ValueError),
        (["A1"], "B", ValueError),
        (["A"], None, TypeError),
        (["A"], 123, TypeError)
    ]
)
def test_invalid_input(terms, result, exception):

    with pytest.raises(exception):
        solve_summation_puzzle(terms, result)
