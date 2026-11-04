"""
Reverse a string without using Python's built-in slicing shortcuts.

Problem description
-------------------
Given a string, return a new string containing the same characters in
reverse order. All characters, including whitespace and punctuation,
must be preserved.

Approach
--------
1. Convert the string into a mutable list of characters.
2. Iterate through the first half of the list.
3. Swap each character with its corresponding character at the opposite end.
4. Join the resulting list into a string.

Complexity analysis
-------------------
Let N represent the length of the input string.

- Time complexity: O(N), since each character is processed at most once.
- Auxiliary space complexity: O(N), due to the temporary character list
  and the resulting string.

Python alternatives
-------------------
- word[::-1] reverses a string using extended slicing.
- reversed(word) returns an iterator over the characters in reverse order.
- "".join(reversed(word)) produces the reversed string without explicitly
  implementing the swapping algorithm.
"""


def reverse_string(word: str) -> str:
    """Return the input string with its characters in reverse order."""

    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    characters = list(word)
    n = len(characters)

    for i in range(n // 2):
        opposite_index = n - i - 1
        characters[i], characters[opposite_index] = (
            characters[opposite_index],
            characters[i],
        )

    return "".join(characters)
