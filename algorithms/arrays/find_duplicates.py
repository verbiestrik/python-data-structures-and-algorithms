"""
Problem: Find Duplicates

Given a sequence of numbers, return all numbers that appear 
more than once. Each duplicate should only appear once in
the result.

Approach:
Use two sets (for O(1) average lookup time per lookup):
- 'seen' stores numbers encountered so far.
- 'duplicates' stores numbers encountered more than once.

Iterate through the sequence. If a number is already in
'seen', add it to 'duplicates'. Otherwise, add it to 'seen'.

Complexity Analysis:
- Time Complexity: O(n) average.
  Each element is processed once, and set operations take
  O(1) average time.

- Space Complexity: O(n).
  In the worst case, both sets can grow proportionally
  to the number of input elements.

Example:
Input:  [1, 2, 3, 4, 5, 5, 6, 1]
Output: {1, 5}
"""

from collections.abc import Iterable

def find_duplicates(numbers: Iterable[int | float]) -> set[int | float]:
    """Return all numbers that occur more than once."""

    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return duplicates
