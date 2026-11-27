
"""
Quick Sort
==========

Problem:
    Sort the elements of a LinkedQueue in ascending order using the
    quick sort algorithm. The original queue is modified in place.

Approach:
    Implement recursive, three-way quick sort using three auxiliary
    linked queues.

    1. Select the first element as the pivot.
    2. Remove each element from the original queue and partition it into:
       - smaller: elements smaller than the pivot.
       - equal: elements equivalent to the pivot.
       - larger: elements larger than the pivot.
    3. Recursively sort the smaller and larger queues.
    4. Reconstruct the original queue by concatenating the three queues
       in ascending order.

    The equal queue prevents unnecessary recursive calls for elements
    equivalent to the pivot. This makes the algorithm particularly
    efficient when many duplicate elements are present.

    The algorithm is stable because the elements maintain their relative
    order within each partition.

    The first element is used as the pivot. Consequently, performance
    depends on how evenly the pivot partitions the elements.

Complexity:
    Time:
        O(n log n) in the best and average cases, assuming reasonably
        balanced partitions.
        O(n^2) in the worst case, when the pivot repeatedly produces
        highly unbalanced partitions (e.g. sorted input with distinct
        elements).

        O(n) when all elements are equivalent.

    Auxiliary space:
        O(n) for the auxiliary linked queues.
        O(log n) recursion stack space on average.
        O(n) recursion stack space in the worst case.
        Total auxiliary space complexity: O(n).

Built-in alternatives:
    - sorted(iterable) returns a new sorted list.
    - list.sort() sorts a list in place.
    Both use Python's highly optimised Timsort implementation.

    These alternatives require converting the queue into a list first.
    This implementation demonstrates quick sort directly on a linked
    queue without relying on Python's built-in sorting algorithms.
"""

from data_structures.queues.linked_queue import LinkedQueue


def quick_sort(numbers: LinkedQueue) -> None:
    """Sort a LinkedQueue in ascending order using quick sort."""
    if not isinstance(numbers, LinkedQueue):
        raise TypeError("numbers must be a LinkedQueue")

    if len(numbers) < 2:
        return

    pivot = numbers.first()

    smaller = LinkedQueue()
    equal = LinkedQueue()
    larger = LinkedQueue()

    # Partition the original queue into three queues.
    while not numbers.is_empty():
        element = numbers.dequeue()

        if element < pivot:
            smaller.enqueue(element)
        elif pivot < element:
            larger.enqueue(element)
        else:
            equal.enqueue(element)

    # Recursively sort the smaller and larger partitions.
    quick_sort(smaller)
    quick_sort(larger)

    # Reconstruct the original queue in ascending order.
    while not smaller.is_empty():
        numbers.enqueue(smaller.dequeue())

    while not equal.is_empty():
        numbers.enqueue(equal.dequeue())

    while not larger.is_empty():
        numbers.enqueue(larger.dequeue())
