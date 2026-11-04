"""
Problem: Find the Most Frequent Element

Given a sequence of numbers, find the element(s) that occur
most frequently.

An optional argument, include_ties, determines whether all
equally frequent elements are returned or only one.

Approach:
1. Use a dictionary to count the occurrences of each element.
2. Iterate through the dictionary to find the highest frequency.
3. Store the element(s) with that frequency in a set.
4. If include_ties=False, only the first element encountered
   with the highest frequency is returned.

If multiple elements are tied and include_ties=False, the
element that appeared first in the original input is returned.

Returns an empty set if the input is empty.

Complexity Analysis:
- Time Complexity: O(n).
  Counting the elements takes O(n). Finding the maximum
  frequency and collecting the corresponding elements takes
  O(k), where k is the number of distinct elements.
  Total: O(n + k) = O(n).

- Space Complexity: O(k).
  The dictionary stores the frequency of each distinct
  element, and the result set contains at most k elements.

Python Alternative:
The built-in max() function can find one most frequent
element using max(elements, key=elements.count).
However, this approach has O(n^2) time complexity because
elements.count() takes O(n) time.
"""


from collections.abc import Iterable


def find_most_frequent_element(
    elements: Iterable[int | float],
    include_ties: bool = True
) -> set[int | float]:

    counts = {}

    for element in elements:
        counts[element] = counts.get(element, 0) + 1

    most_frequent = set()
    highest_frequency = 0

    for element, frequency in counts.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            most_frequent = {element}

        elif include_ties and frequency == highest_frequency:
            most_frequent.add(element)

    return most_frequent
