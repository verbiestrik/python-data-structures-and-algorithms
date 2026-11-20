"""
Dynamic Array
=============

Problem:
    Implement a dynamic array that stores references to Python objects in
    a contiguous block of memory. The array automatically increases its
    capacity when it runs out of available space.

Approach:
    - Allocate an initial array with capacity 1 using ctypes.py_object.
    - Keep track of the number of stored elements (_n) and the allocated
      capacity (_capacity).
    - When append() is called on a full array, allocate a new array with
      twice the previous capacity and copy the existing references.
    - Support integer indexing, including negative indices, and assignment.

Time Complexity:
    - Indexing (__getitem__): O(1)
    - Assignment (__setitem__): O(1)
    - Length (__len__): O(1)
    - Append: O(1) amortised; O(n) when resizing is required.
    - Resizing: O(n), where n is the number of stored elements.

Space Complexity:
    - O(n), where n is the number of stored elements.
      The capacity doubles when necessary, so the allocated memory remains
      proportional to the number of stored elements.

Python Alternatives:
    - list is Python's built-in dynamic array implementation and should
      generally be preferred in production code.
    - array.array provides a more memory-efficient alternative for
      homogeneous numeric data.
    - operator.index() is used to support integer-like index objects,
      rather than checking only for instances of int.
"""

import ctypes
from operator import index


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        k = self._normalize_index(k)
        return self._A[k]

    def __setitem__(self, k, value):
        k = self._normalize_index(k)
        self._A[k] = value

    def append(self, element):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = element
        self._n += 1

    def _normalize_index(self, k):
        """Validate an index and convert negative indices to positive ones."""
        k = index(k)

        if k < 0:
            k += self._n

        if not 0 <= k < self._n:
            raise IndexError("dynamic array index out of range")

        return k

    def _resize(self, new_capacity):
        """Allocate a larger array and copy the existing references."""
        new_array = self._make_array(new_capacity)

        for i in range(self._n):
            new_array[i] = self._A[i]

        self._A = new_array
        self._capacity = new_capacity

    def _make_array(self, capacity):
        """Create a low-level array of Python object references."""
        return (ctypes.py_object * capacity)()
