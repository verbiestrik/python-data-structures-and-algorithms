"""
Binary Search
=============

Problem
-------
Determine whether a target element exists in a sorted sequence of numbers.

The sequence must be sorted in ascending order.

Approach
--------
Use recursive binary search to repeatedly divide the search interval in half.

1. Initialise the search boundaries to the first and last indices.
2. Calculate the middle index.
3. Compare the middle element with the target:
   - If they are equal, return True.
   - If the target is smaller, recursively search the left half.
   - If the target is larger, recursively search the right half.
4. If the lower boundary exceeds the upper boundary, the target does not
   exist in the sequence, so return False.

The algorithm only examines elements within the current search interval.
It does not create new lists when dividing the search space.

Complexity
----------
Let n be the number of elements in the sequence.

Time:  O(log n)
       Each recursive call reduces the search interval by approximately
       half. Accessing an element by index is O(1) for Python lists.

Space: O(log n)
       The recursive call stack requires O(log n) space because the search
       interval is halved at each recursive call.

Python alternatives
-------------------
- bisect module: Provides efficient binary search functionality through
  bisect_left() and bisect_right(). These return insertion positions rather
  than directly indicating whether an element exists.
- The in operator: Can check whether an element exists in a list, but takes
  O(n) time in the worst case.

Input requirements
------------------
- The input must be a sequence supporting indexed access, such as a list
  or tuple.
- Strings and byte sequences are not accepted as input sequences.
- The sequence must already be sorted in ascending order. This requirement
  is not checked at runtime, since doing so would require O(n) time.
- Elements must support equality and ordering comparisons with the target.
"""

from collections.abc import Sequence
from typing import TypeVar


def binary_search(data: Sequence, target) -> bool:

    if not isinstance(data, Sequence) or isinstance(
        data, (str, bytes, bytearray)
    ):
        raise TypeError("Data must be a list or another indexed sequence.")

    def search(low: int, high: int) -> bool:

        # The search interval is empty: the target was not found.
        if low > high:
            return False

        mid = low + (high - low) // 2

        if data[mid] == target:
            return True

        elif target < data[mid]:
            return search(low, mid - 1)

        else:
            return search(mid + 1, high)

    return search(0, len(data) - 1)
