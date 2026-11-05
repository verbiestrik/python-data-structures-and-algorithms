"""
Calculate the moving averages of a sequence of numbers.

Problem description
-------------------
Given a sequence of numbers and a positive integer k, return a list
containing the average of every consecutive window of k elements.

Only complete windows are considered.

Approach
--------
1. Calculate the sum of the first k elements.
2. Calculate their average and store it.
3. Slide the window one position to the right:
   - Subtract the element leaving the window.
   - Add the new element entering the window.
4. Calculate and store the new average.
5. Repeat until no complete window remains.

Complexity analysis
-------------------
Let n represent the length of the input sequence.

- Time complexity: O(n), since each element is processed at most once.
- Auxiliary space complexity: O(1), excluding the output list.

Python alternatives
-------------------
- sum() can calculate the sum of each window, but recalculating every
  window independently would result in O(n*k) time complexity.
- statistics.mean() provides a convenient alternative for calculating
  individual averages, but does not implement the sliding window
  optimisation.
"""


def moving_average(numbers: list | tuple, k: int) -> list[float]:
    """Return the averages of all consecutive windows of size k."""

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise TypeError("All elements must be integers or floats.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k <= 0:
        raise ValueError("k must be positive.")

    n = len(numbers)

    if k > n:
        return []

    # Calculate the sum of the first window.
    window_sum = sum(numbers[i] for i in range(k))
    averages = [window_sum / k]

    # Slide the window through the remaining elements.
    for i in range(k, n):
        window_sum += numbers[i] - numbers[i - k]
        averages.append(window_sum / k)

    return averages
