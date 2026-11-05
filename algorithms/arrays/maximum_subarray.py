"""
Find the maximum sum of a contiguous subarray.

Problem description
-------------------
Given a sequence of integers or floats, find the maximum possible sum
of a non-empty contiguous subarray.

The subarray must consist of consecutive elements from the original
sequence. The entire sequence is also a valid subarray.

Approach
--------
Use Kadane's algorithm.

1. Initialise max_ending and max_sum with the first element.
2. Iterate through the remaining elements.
3. At each position, decide whether to:
   - Extend the previous subarray by including the current element.
   - Start a new subarray at the current element.
4. Update max_sum whenever a larger subarray sum is found.
5. Return max_sum.

Complexity analysis
-------------------
Let n represent the length of the input sequence.

- Time complexity: O(n), since each element is processed exactly once.
- Auxiliary space complexity: O(1), since only two variables are
  maintained independently of the input size.

Python alternatives
-------------------
- max() is used to select between extending the current subarray
  and starting a new one.
"""


def maximum_sum_cont_subarr(numbers: list | tuple) -> int | float:
    """Return the maximum sum of a non-empty contiguous subarray."""

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    if not numbers:
        raise ValueError("Input sequence cannot be empty.")

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise TypeError("All elements must be integers or floats.")

    max_sum = numbers[0]
    max_ending = numbers[0]

    for number in numbers[1:]:
        max_ending = max(number, max_ending + number)
        max_sum = max(max_sum, max_ending)

    return max_sum
