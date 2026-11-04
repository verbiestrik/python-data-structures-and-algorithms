"""
Problem: Find the K Most Frequent Elements

Given a sequence of numbers, find the k most frequently
occurring elements and return them together with their
frequencies.

Four different implementations are provided,
and time and space complexities are compared.

Approach 1: Repeated Maximum (repeated_max)
1. Build a frequency dictionary.
2. Repeatedly find the element with the highest frequency.
3. Remove that element from the remaining elements.

Approach 2: Sorting (sorting)
1. Build a frequency dictionary.
2. Sort its entries by frequency in descending order.
3. Return the first k entries.

Approach 3: Full Heap (full_heap)
1. Build a frequency dictionary.
2. Construct a max-heap containing all elements.
3. Extract the maximum k times.

Approach 4: Bounded Heap (bounded_heap)
1. Build a frequency dictionary.
2. Construct a min-heap containing at most k elements.
3. For each remaining element, compare its frequency with
   the smallest frequency in the heap.
4. Replace the smallest element whenever a more frequent
   element is encountered.
5. Return the elements in descending frequency order.

Tie-breaking:
When two elements have the same frequency, the element
appearing first in the original input is prioritised.

Input:
- elements: Iterable of numbers.
- k: Number of elements to return (non-negative integer).
- method: One of the four implementation names.

Output:
A list of (element, frequency) tuples. If k exceeds the
number of distinct elements, all distinct elements are
returned. An empty list is returned when k = 0.

Complexity Analysis:

Let:
- n = Number of input elements.
- m = Number of distinct elements.
- q = min(k, m).

1. Repeated Maximum:
   Time: O(n + q*m)
   Space: O(m)

2. Sorting:
   Time: O(n + m*log(m))
   Space: O(m)

3. Full Heap:
   Time: O(n + m + q*log(m))
   Space: O(m)

4. Bounded Heap:
   Time: O(n + m*log(k+1))
   Space: O(m) overall, with O(k) additional heap space.

Python Alternative:
The standard library provides Counter(elements).most_common(k),
which directly returns the k most frequent elements and their
frequencies.
"""

from collections.abc import Iterable
import heapq


def find_k_most_frequent_elements(
    elements: Iterable[int | float],
    k: int,
    method: str = "repeated_max"
) -> list[tuple[int | float, int]]:

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k < 0:
        raise ValueError("k must be non-negative.")

    methods = {"repeated_max", "sorting", "full_heap", "bounded_heap"}

    if method not in methods:
        raise ValueError(f"Method must be one of {methods}.")

    if k == 0:
        return []

    # Build the frequency dictionary.
    counts = {}

    for element in elements:
        counts[element] = counts.get(element, 0) + 1

    limit = min(k, len(counts))

    if limit == 0:
        return []

    # --------------------------------------------------
    # Method 1: Repeated maximum
    # --------------------------------------------------

    if method == "repeated_max":

        remaining = list(counts.items())
        result = []

        for _ in range(limit):
            max_index = max(
                range(len(remaining)),
                key=lambda i: remaining[i][1]
            )

            result.append(remaining.pop(max_index))

        return result

    # --------------------------------------------------
    # Method 2: Sorting
    # --------------------------------------------------

    elif method == "sorting":

        sorted_elements = sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_elements[:limit]

    # --------------------------------------------------
    # Method 3: Full heap
    # --------------------------------------------------

    elif method == "full_heap":

        heap = [
            (-frequency, order, element)
            for order, (element, frequency) in enumerate(counts.items())
        ]

        heapq.heapify(heap)

        result = []

        for _ in range(limit):
            negative_frequency, order, element = heapq.heappop(heap)

            result.append((element, -negative_frequency))

        return result

    # --------------------------------------------------
    # Method 4: Bounded heap
    # --------------------------------------------------

    elif method == "bounded_heap":

        heap = []

        for order, (element, frequency) in enumerate(counts.items()):

            # Earlier elements have higher priority in case
            # of equal frequencies.
            entry = (frequency, -order, element)

            if len(heap) < limit:
                heapq.heappush(heap, entry)

            elif entry > heap[0]:
                heapq.heapreplace(heap, entry)

        result = []

        while heap:
            frequency, negative_order, element = heapq.heappop(heap)
            result.append((element, frequency))

        # The heap returns elements in ascending priority order.
        result.reverse()

        return result
