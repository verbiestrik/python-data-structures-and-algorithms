"""
Find the distinct common elements of two sequences of numbers.

Problem description
-------------------
Given two sequences of integers or floats, return a list containing
the elements that occur in both sequences.

Each common element is returned only once, and the order follows
the first occurrence in the first input sequence.

Approach
--------
1. Validate that both inputs are sequences of numbers.
2. Convert the second sequence into a set for efficient membership checks.
3. Iterate through the first sequence.
4. If an element is present in the set, append it to the result
   and remove it from the set to prevent duplicates.
5. Return the resulting list.

Complexity analysis
-------------------
Let n and m represent the lengths of the two input sequences.

- Time complexity: O(n + m) expected.
- Auxiliary space complexity: O(m), for the set.

Python alternatives
-------------------
- set(numbers1) & set(numbers2) provides a concise alternative,
  but does not preserve the order of the first input sequence.
- collections.Counter can be used when element frequencies matter.
"""

from collections.abc import Sequence


def common_elements(numbers1: Sequence, numbers2: Sequence) -> list:
    """Return distinct common elements, preserving the order of numbers1."""

    # Validate inputs.
    for numbers in (numbers1, numbers2):
        if not isinstance(numbers, Sequence):
            raise TypeError("Inputs must be sequences.")

        if not all(isinstance(number, (int, float)) for number in numbers):
            raise TypeError("All elements must be integers or floats.")

    numbers2_set = set(numbers2)
    result = []

    for number in numbers1:
        if number in numbers2_set:
            result.append(number)
            numbers2_set.remove(number)

    return result
