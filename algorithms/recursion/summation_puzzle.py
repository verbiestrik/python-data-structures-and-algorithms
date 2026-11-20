"""
Summation Puzzle Solver
=======================

Problem
-------
Solve a summation puzzle (also known as a cryptarithm) by assigning a unique
digit from 0 to 9 to every distinct letter, such that the resulting
arithmetic equation is correct.

For example:

    POT + PAN = BIB

Every occurrence of the same letter must represent the same digit, and
different letters must represent different digits.

Leading zeros are not allowed.

Approach
--------
Use recursive backtracking to enumerate possible digit assignments.

1. Extract all distinct letters occurring in the puzzle.
2. Identify the letters that appear at the beginning of a word. These
   letters cannot be assigned zero.
3. Maintain:
   - An assignment dictionary mapping letters to digits.
   - A set of currently unused digits.
4. Recursively assign an available digit to the next unassigned letter:
   - Add the assignment to the dictionary.
   - Remove the digit from the set of unused digits.
   - If all letters have been assigned, evaluate the arithmetic equation.
   - Otherwise, recursively assign a digit to the next letter.
5. Backtrack by removing the assignment and returning the digit to the
   set of unused digits.
6. Store every assignment satisfying the equation.

All possible assignments are explored, so the algorithm finds every
solution rather than stopping after the first one.

Complexity
----------
Let:
    m = number of distinct letters (m <= 10).
    C = total number of characters across all words.
    S = number of valid solutions.

Time:
    O(C * P(10, m))

    There are at most P(10, m) distinct assignments of m letters to
    ten digits, where P(10, m) = 10! / (10-m)!.

    Each complete assignment requires O(C) time to evaluate the equation.

Space:
    O(m) auxiliary space for the recursive call stack, assignment
    dictionary and other working data.

    The returned solutions require O(S * m) additional space.

Python alternatives
-------------------
- itertools.permutations(): Can generate assignments of distinct digits
  without repetitions, but would not naturally demonstrate the recursive
  backtracking process.
- set: Efficiently tracks the digits that remain available.
- dict: Stores the current letter-to-digit assignment.
- sum(): Calculates the sum of the resulting terms.

Input requirements
------------------
- terms must be a non-empty sequence of strings.
- result must be a string.
- Words may contain ASCII letters only (case-insensitive).
- At most ten distinct letters may occur across the puzzle.
- Leading zeros are not permitted.

Returns
-------
A list of dictionaries, where each dictionary represents a valid
letter-to-digit assignment.

An empty list is returned when no solution exists.
"""

from collections.abc import Sequence


def solve_summation_puzzle(
    terms: Sequence[str],
    result: str
) -> list[dict[str, int]]:

    if not isinstance(terms, Sequence) or isinstance(terms, (str, bytes)):
        raise TypeError("terms must be a sequence of strings.")

    if not terms:
        raise ValueError("At least one addend is required.")

    if not isinstance(result, str):
        raise TypeError("Result must be a string.")

    # Normalise words and validate their contents.
    def validate_word(word: str) -> str:

        if not isinstance(word, str):
            raise TypeError("Every word must be a string.")

        if not word or not word.isascii() or not word.isalpha():
            raise ValueError("Words must contain ASCII letters only.")

        return word.upper()

    terms = [validate_word(word) for word in terms]
    result = validate_word(result)

    words = terms + [result]

    # Extract distinct letters while preserving their order of appearance.
    letters = []
    seen_letters = set()

    for word in words:
        for letter in word:
            if letter not in seen_letters:
                letters.append(letter)
                seen_letters.add(letter)

    if len(letters) > 10:
        raise ValueError("A puzzle cannot contain more than 10 distinct letters.")

    # The first letter of every word must represent a non-zero digit.
    leading_letters = {word[0] for word in words}

    # S: Current letter-to-digit assignment.
    assignment = {}

    # U: Digits that have not yet been assigned.
    unused_digits = set(range(10))

    solutions = []

    # Convert a word into its numerical representation.
    def word_to_number(word: str) -> int:

        number = 0

        for letter in word:
            number = number * 10 + assignment[letter]

        return number

    # Recursively assign digits to the letters.
    def puzzle_solve(k: int) -> None:

        # The next letter to be assigned.
        letter = letters[len(letters) - k]

        for digit in range(10):

            # Skip digits that are already in use.
            if digit not in unused_digits:
                continue

            # Leading zeros are not allowed.
            if digit == 0 and letter in leading_letters:
                continue

            # Add the digit to the current configuration.
            assignment[letter] = digit
            unused_digits.remove(digit)

            if k == 1:

                # All letters have been assigned: test the configuration.
                terms_total = sum(
                    word_to_number(word) for word in terms
                )

                result_value = word_to_number(result)

                if terms_total == result_value:
                    solutions.append(assignment.copy())

            else:

                # Recursively assign digits to the remaining letters.
                puzzle_solve(k - 1)

            # Backtrack: undo the current assignment.
            del assignment[letter]
            unused_digits.add(digit)

    puzzle_solve(len(letters))

    return solutions
