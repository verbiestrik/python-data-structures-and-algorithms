"""
Array-Based Stack
=================

Problem:
    Implement a stack (Last-In, First-Out) data structure using a Python
    list as its underlying storage. Note that a list also has other
    functionalities that are not included in the stack abstract data type,
    so this implementation is simply an illustration of how abstract
    data types can be defined by using a more general data type and
    hiding functionality that is not supported by the (less general)
    abstract data type.

Approach:
    - Store elements in a Python list (_stack).
    - push() adds an element to the end of the list.
    - pop() removes and returns the last element.
    - top() returns the last element without removing it.
    - is_empty() checks whether the stack contains any elements.
    - Raise a custom Empty exception when attempting to access or remove
      an element from an empty stack.

Time Complexity:
    - Length (__len__): O(1)
    - is_empty(): O(1)
    - push(): O(1) amortised; O(n) when the underlying list resizes.
    - top(): O(1)
    - pop(): O(1) amortised.

Space Complexity:
    - O(n), where n is the number of elements stored in the stack.

Python Alternatives:
    - list is Python's built-in dynamic array and provides efficient
      append() and pop() operations at the end.
    - collections.deque provides an alternative with efficient
      insertion and removal at both ends.
    - queue.LifoQueue provides a thread-safe stack implementation.
"""

class Empty(Exception):
    """Exception raised when accessing or removing from an empty stack."""
    pass


class ArrayStack:

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, element):
        self._stack.append(element)

    def top(self):
        if self.is_empty():
            raise Empty("No top element; stack is empty!")

        return self._stack[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("No top element; stack is empty!")

        return self._stack.pop()
