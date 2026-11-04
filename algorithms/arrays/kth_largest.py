"""
Find the kth largest distinct element in a sequence of numbers.

Problem description
-------------------
Given a sequence of numbers and a positive integer k, return the kth
largest distinct value.

Duplicate values are counted only once. For example, the second-largest
distinct element of [4, 4, 4, 5] is 4.

Return None if the sequence contains fewer than k distinct values.

Approach
--------
Maintain a sorted list containing at most the k largest distinct values.

For each input number:
1. Find its correct insertion position in the sorted list.
2. Ignore it if it is already present.
3. Insert it if its position is among the k largest values.
4. Remove the smallest value if the list exceeds k elements.

The list is maintained in descending order, so its final kth element
is the desired result.

Complexity analysis
-------------------
Let n represent the number of input elements and k the requested rank.

- Time complexity: O(nk), since each element may require a linear search
  and insertion into a list of at most k elements.
- Auxiliary space complexity: O(k), since only the k largest distinct
  values are stored.

Python alternatives
-------------------
- sorted(set(numbers), reverse=True)[k - 1] is a concise alternative.
  It has O(n log n) time and O(n) auxiliary space complexity.
- heapq.nlargest(k, set(numbers)) provides a standard-library alternative
  with approximately O(n + u log k) time, where u is the number of
  distinct input values.

This implementation avoids sorting the entire input and is particularly
useful when k is small relative to the input size. When k is not small 
relative to the input size, heaps can be used
(see the 'find_k_most_frequent_elements.py').
"""

from collections.abc import Sequence
from numbers import Real


def kth_largest(numbers: Sequence[Real], k: int) -> Real | None:
    """Return the kth largest distinct value, or None if it does not exist."""

    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k < 1:
        raise ValueError("k must be a positive integer.")

    if not isinstance(numbers, Sequence) or isinstance(numbers, (str, bytes)):
        raise TypeError("Input must be a sequence of numbers.")

    largest_values = []

    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, Real):
            raise TypeError("All sequence elements must be real numbers.")

        if number != number:
            raise ValueError("NaN values are not supported.")

        # Find the insertion position in descending order.
        i = 0
        while i < len(largest_values) and largest_values[i] > number:
            i += 1

        # Ignore duplicates.
        if i < len(largest_values) and largest_values[i] == number:
            continue

        # Insert only if the number belongs among the k largest values.
        if i < k:
            largest_values.insert(i, number)

            # Maintain at most k elements.
            if len(largest_values) > k:
                largest_values.pop()

    if len(largest_values) < k:
        return None

    return largest_values[k - 1]
