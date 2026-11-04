"""
Rotate a list by a given number of positions.

Problem description
-------------------
Given a list and an integer rotation, return a new list with its elements
rotated by the specified number of positions.

- Positive rotation: rotate to the right.
- Negative rotation: rotate to the left.
- Rotations larger than the list length are handled using modulo.

Approach
--------
1. Calculate the effective rotation using modulo.
2. Create a new list of the same length.
3. Iterate through the original list and place each element at its
   new position.
4. Return the rotated list.

Complexity analysis
-------------------
Let n represent the length of the input list.

- Time complexity: O(n), since each element is processed once.
- Auxiliary space complexity: O(n), for the new list.

Python alternatives
-------------------
- Slicing can provide a concise alternative:
  items[-rotation:] + items[:-rotation]
  after normalising the rotation.
- collections.deque offers a rotate() method, which can be useful
  when working with queues that need repeated rotations.
"""


def rotate_list(items: list, rotation: int) -> list:
    """Return a new list rotated by the specified number of positions."""

    if not isinstance(items, list):
        raise TypeError("Input must be a list.")

    if not isinstance(rotation, int):
        raise TypeError("Rotation must be an integer.")

    n = len(items)

    if n == 0:
        return []

    rotation %= n

    rotated_list = [None] * n

    for i in range(n):
        rotated_list[(i + rotation) % n] = items[i]

    return rotated_list
