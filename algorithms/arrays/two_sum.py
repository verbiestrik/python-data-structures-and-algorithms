"""
Find two indices whose corresponding elements sum to a target value.

Problem description
-------------------
Given a sequence of numbers and a target value, return the indices of
the first pair of distinct elements whose sum equals the target.

The same element cannot be used twice.

If no valid pair exists, return None.

The first pair is defined by a left-to-right traversal: the pair whose
second index is encountered first is returned.

Approach
--------
1. Create a dictionary mapping previously encountered numbers to indices.
2. Iterate through the input sequence.
3. For each number, calculate its complement (target - number).
4. Check whether the complement exists in the dictionary.
5. If it does, return the two corresponding indices.
6. Otherwise, store the current number and its index, provided the
   number has not already been stored.

Complexity analysis
-------------------
Let n represent the length of the input sequence.

- Time complexity: O(n) expected, since dictionary lookups and insertions
  take O(1) time on average.
- Auxiliary space complexity: O(n), for the dictionary.

Python alternatives
-------------------
- A nested loop can check every possible pair, but requires O(n²) time.
- itertools.combinations can generate all possible pairs, but also
  requires O(n²) time when all pairs are examined.
"""


def two_sum(numbers: list | tuple, target: int | float) -> tuple[int, int] | None:
    """Return the indices of the first pair summing to target, or None."""

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise TypeError("All elements must be integers or floats.")

    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer or float.")

    previous_indices = {}

    for i, number in enumerate(numbers):
        complement = target - number

        if complement in previous_indices:
            return previous_indices[complement], i

        # Keep the first occurrence of each number.
        if number not in previous_indices:
            previous_indices[number] = i

    return None
