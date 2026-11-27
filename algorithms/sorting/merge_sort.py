
"""
Merge Sort
==========

Problem:
    Sort a list of mutually comparable elements in ascending order using
    the merge sort algorithm. The original list is modified in place.

Approach:
    Implement recursive, top-down merge sort.

    1. Divide the list into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves into a shared auxiliary array.
    4. Copy the merged elements back into the original list.

    A single auxiliary array is allocated and reused throughout the
    recursion. This avoids repeatedly creating sliced lists and reduces
    unnecessary memory allocations.

    The algorithm is stable: when two elements are equal, the element
    from the left half is selected first, preserving their original
    relative order.

    Merging is skipped when the two sorted halves are already in order.

Complexity:
    Time:
        O(n log n) in the best, average and worst cases.
        Each recursion level performs at most O(n) merging work, and
        there are O(log n) recursion levels.

    Auxiliary space:
        O(n) for the shared auxiliary array.
        O(log n) for the recursion stack.
        Total auxiliary space complexity: O(n).

Built-in alternatives:
    - sorted(numbers) returns a new sorted list.
    - numbers.sort() sorts the original list in place.
    Both use Python's highly optimised Timsort implementation and are
    generally preferable in production code. This implementation
    demonstrates the underlying merge sort algorithm.
"""

from typing import TypeVar

T = TypeVar("T")


def _merge(
    numbers: list[T],
    auxiliary: list[T],
    low: int,
    middle: int,
    high: int,
) -> None:
    """Merge two sorted sections of numbers into the original list."""
    left = low
    right = middle
    output = low

    # Merge the two sections into the auxiliary array.
    while left < middle and right < high:
        # Select the left element when equal to preserve stability.
        if not numbers[right] < numbers[left]:
            auxiliary[output] = numbers[left]
            left += 1
        else:
            auxiliary[output] = numbers[right]
            right += 1

        output += 1

    # Copy any remaining elements from the left section.
    while left < middle:
        auxiliary[output] = numbers[left]
        left += 1
        output += 1

    # Copy any remaining elements from the right section.
    while right < high:
        auxiliary[output] = numbers[right]
        right += 1
        output += 1

    # Copy the merged section back into the original list.
    for index in range(low, high):
        numbers[index] = auxiliary[index]


def _merge_sort(
    numbers: list[T],
    auxiliary: list[T],
    low: int,
    high: int,
) -> None:
    """Recursively sort the elements between low and high."""
    if high - low < 2:
        return

    middle = (low + high) // 2

    _merge_sort(numbers, auxiliary, low, middle)
    _merge_sort(numbers, auxiliary, middle, high)

    # Skip merging if the two sorted sections are already in order.
    if not numbers[middle] < numbers[middle - 1]:
        return

    _merge(numbers, auxiliary, low, middle, high)


def merge_sort(numbers: list[T]) -> None:
    """Sort numbers in ascending order using merge sort."""
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    if len(numbers) < 2:
        return

    # Allocate one auxiliary array and reuse it throughout recursion.
    auxiliary = numbers.copy()

    _merge_sort(numbers, auxiliary, 0, len(numbers))
