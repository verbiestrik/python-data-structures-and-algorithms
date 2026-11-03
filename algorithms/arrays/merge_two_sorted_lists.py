"""
Problem: Merge Two Sorted Lists

Given two lists sorted in ascending order, merge them into
a single sorted list.

Approach:
1. Use two pointers, one for each input list.
2. Compare the elements at the two pointers.
3. Append the smaller element to the result and advance
   the corresponding pointer.
4. Once one list is exhausted, append all remaining elements
   from the other list.

Complexity Analysis:
- Time Complexity: O(n + m).
  Each element from both lists is processed exactly once,
  where n and m are the lengths of the input lists.

- Space Complexity: O(n + m).
  The resulting list contains all elements from both inputs.

Python Alternative:
The standard library provides heapq.merge(), which merges
multiple sorted iterables. It returns an iterator, so use
list(heapq.merge(list1, list2)) to obtain a list. 
heapq.merge() can be used with an aribtrary number of
sorted lists and has time complexity O(n*log(k)) for k lists
with a total of n numbers in all the lists.
"""

def merge_two_sorted_lists(list1: list[int | float],
                           list2: list[int | float]) -> list[int | float]:

    merged = []
    i = j = 0
    n = len(list1)
    m = len(list2)

    while i < n and j < m:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < n:
        merged.append(list1[i])
        i += 1

    while j < m:
        merged.append(list2[j])
        j += 1

    return merged
