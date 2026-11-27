
"""
Quick Sort (In-Place)
=====================

Problem:
    Sort a list of mutually comparable elements in ascending order
    using the quick sort algorithm. The original list is modified
    in place.

Approach:
    Implement recursive quick sort using the Lomuto partition scheme.

    1. Select the last element as the pivot.
    2. Partition the list so that elements smaller than or equal to
       the pivot appear before it, and larger elements appear after it.
    3. Recursively sort the two resulting partitions.

    To limit recursion stack space, recursively sort the smaller
    partition and continue sorting the larger partition iteratively.

    The algorithm is not stable, meaning equal elements are not
    guaranteed to retain their original relative order.

Complexity:
    Time:
        O(n log n) in the best and average cases, assuming reasonably
        balanced partitions.
        O(n^2) in the worst case, when the pivot repeatedly produces
        highly unbalanced partitions (e.g. already sorted or reverse
        sorted input).

    Auxiliary space:
        O(log n) for the recursion stack, even in the worst case,
        because recursion is restricted to the smaller partition.
        O(1) additional space for partitioning.

Built-in alternatives:
    - sorted(numbers) returns a new sorted list.
    - numbers.sort() sorts the original list in place.
    Both use Python's highly optimised Timsort implementation.

    This implementation demonstrates quick sort without relying on
    Python's built-in sorting algorithms.
"""

from typing import TypeVar

T = TypeVar("T")


def partition(numbers: list[T], low: int, high: int) -> int:
    """Partition numbers around the last element and return its index."""
    pivot = numbers[high]
    lower_boundary = low - 1

    for j in range(low, high):
        if numbers[j] <= pivot:
            lower_boundary += 1
            numbers[lower_boundary], numbers[j] = (
                numbers[j],
                numbers[lower_boundary],
            )

    pivot_index = lower_boundary + 1
    numbers[pivot_index], numbers[high] = (
        numbers[high],
        numbers[pivot_index],
    )

    return pivot_index


def _quick_sort(numbers: list[T], low: int, high: int) -> None:
    """Recursively sort the smaller partition and iterate over the larger."""
    while low < high:
        pivot_index = partition(numbers, low, high)

        # Recursively sort the smaller partition to limit stack space.
        if pivot_index - low < high - pivot_index:
            _quick_sort(numbers, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quick_sort(numbers, pivot_index + 1, high)
            high = pivot_index - 1


def quick_sort(numbers: list[T]) -> None:
    """Sort numbers in ascending order using in-place quick sort."""
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    _quick_sort(numbers, 0, len(numbers) - 1)
