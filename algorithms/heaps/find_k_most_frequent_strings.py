"""
Problem: Find the K Most Frequent Strings

Given a sequence of strings, find the k most frequently
occurring strings and return them together with their
frequencies.

Four different implementations are provided.

Approach 1: Repeated Maximum (repeated_max)
1. Build a frequency dictionary.
2. Repeatedly find the string with the highest frequency.
3. Remove that string from the remaining elements.

Approach 2: Sorting (sorting)
1. Build a frequency dictionary.
2. Sort its entries by decreasing frequency and alphabetical
   order.
3. Return the first k entries.

Approach 3: Full Heap (full_heap)
1. Build a frequency dictionary.
2. Construct a max-heap containing all distinct strings.
3. Extract the maximum k times.

Approach 4: Bounded Heap (bounded_heap)
1. Build a frequency dictionary.
2. Assign each distinct string an alphabetical rank.
3. Construct a min-heap containing at most k strings.
4. The root represents the least desirable element:
   lowest frequency, and alphabetically last in case of ties.
5. Replace the root whenever a more desirable string appears.
6. Extract the retained strings and reverse their order.

Tie-breaking:
Strings with equal frequencies are ordered alphabetically
using Python's case-sensitive lexicographical ordering.

Input:
- strings: Iterable of strings.
- k: Number of strings to return (non-negative integer).
- method: One of the four implementation names.

Output:
A list of (string, frequency) tuples.

If k exceeds the number of distinct strings, all distinct
strings are returned. Empty input or k=0 returns an empty list.

Complexity Analysis:

Let:
- n = Number of input strings.
- m = Number of distinct strings.
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
   Time: O(n + m*log(m) + m*log(k+1))
   Space: O(m)

The bounded heap requires alphabetical ranking beforehand.
This takes O(m*log(m)) time. The heap itself contains at most
k elements and requires O(k) additional space.

Python Alternative:
collections.Counter(strings).most_common(k) returns the k
most frequent strings and their frequencies. However, its
tie-breaking behaviour does not guarantee alphabetical
ordering, so additional sorting is necessary.
"""

from collections.abc import Iterable
import heapq


def find_k_most_frequent_strings(
    strings: Iterable[str],
    k: int,
    method: str = "repeated_max"
) -> list[tuple[str, int]]:

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k < 0:
        raise ValueError("k must be non-negative.")

    methods = {
        "repeated_max",
        "sorting",
        "full_heap",
        "bounded_heap"
    }

    if method not in methods:
        raise ValueError("Invalid method.")

    if k == 0:
        return []

    # Build the frequency dictionary.
    counts = {}

    for string in strings:
        counts[string] = counts.get(string, 0) + 1

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

            max_index = min(
                range(len(remaining)),
                key=lambda i: (
                    -remaining[i][1],
                    remaining[i][0]
                )
            )

            result.append(remaining.pop(max_index))

        return result

    # --------------------------------------------------
    # Method 2: Sorting
    # --------------------------------------------------

    elif method == "sorting":

        sorted_strings = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        return sorted_strings[:limit]

    # --------------------------------------------------
    # Method 3: Full heap
    # --------------------------------------------------

    elif method == "full_heap":

        heap = [
            (-frequency, string)
            for string, frequency in counts.items()
        ]

        heapq.heapify(heap)

        result = []

        for _ in range(limit):
            negative_frequency, string = heapq.heappop(heap)

            result.append((string, -negative_frequency))

        return result

    # --------------------------------------------------
    # Method 4: Bounded heap
    # --------------------------------------------------

    elif method == "bounded_heap":

        # Assign alphabetical ranks to all distinct strings.
        alphabetical_rank = {
            string: rank
            for rank, string in enumerate(sorted(counts))
        }

        heap = []

        for string, frequency in counts.items():

            rank = alphabetical_rank[string]

            # The heap root should be the least desirable
            # element: lowest frequency, then alphabetically last.
            entry = (frequency, -rank, string)

            if len(heap) < limit:
                heapq.heappush(heap, entry)

            elif entry > heap[0]:
                heapq.heapreplace(heap, entry)

        result = []

        while heap:
            frequency, negative_rank, string = heapq.heappop(heap)

            result.append((string, frequency))

        # Reverse to obtain decreasing frequency and
        # alphabetical ordering for ties.
        result.reverse()

        return result
