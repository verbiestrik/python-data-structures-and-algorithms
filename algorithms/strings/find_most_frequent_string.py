"""
Problem: Find the Most Frequent String

Given a sequence of strings, find the string(s) that occur
most frequently.

The optional argument include_ties determines whether all
equally frequent strings are returned or only the
alphabetically first one.

Approach:
1. Build a dictionary containing the frequency of each string.
2. Find the highest frequency.
3. Collect all strings having that frequency.
4. Sort the result alphabetically if include_ties=True.
   Otherwise, return only the alphabetically first string.

Empty input returns an empty list.

Alphabetical ordering:
Uses Python's case-sensitive lexicographical string ordering.

Complexity Analysis:
Let n be the number of input strings, m the number of
distinct strings, and t the number of strings sharing the
highest frequency.

- Time Complexity: O(n + m + t*log(t)).
  Building the frequency dictionary takes O(n).
  Finding the highest frequency and collecting matching
  strings takes O(m).
  Sorting the result takes O(t*log(t)).

  Worst case: O(n + m*log(m)).

- Space Complexity: O(m).
  The frequency dictionary and result can contain up to
  m distinct strings.

Python Alternative:
collections.Counter provides the most_common() method.
For example, Counter(strings).most_common(1) returns the
most frequent string and its frequency. Additional handling
is required to retrieve all ties alphabetically.
"""

from collections.abc import Iterable


def find_most_frequent_string(
    strings: Iterable[str],
    include_ties: bool = True
) -> list[str]:

    counts = {}

    for string in strings:
        counts[string] = counts.get(string, 0) + 1

    if not counts:
        return []

    highest_frequency = max(counts.values())

    most_frequent = [
        string
        for string, frequency in counts.items()
        if frequency == highest_frequency
    ]

    if include_ties:
        return sorted(most_frequent)

    return [min(most_frequent)]
