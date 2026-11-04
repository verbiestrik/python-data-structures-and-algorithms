"""
Find the length of the longest substring without repeated characters.

Problem description
-------------------
Given a string, find the length of its longest contiguous substring
in which every character occurs at most once.

Characters are compared exactly as they appear in the input.
No normalisation or removal of whitespace or punctuation is performed.

Approach
--------
Use a sliding window defined by two indices: left and right.

1. Maintain a dictionary recording the last position of each character.
2. Iterate through the string using the right index.
3. If a character has already appeared inside the current window,
   move the left boundary immediately past its previous occurrence.
4. Update the character's last recorded position.
5. Update the maximum window length.

Complexity analysis
-------------------
Let n represent the length of the input string.

- Time complexity: O(n), since each character is processed once.
- Auxiliary space complexity: O(min(n, a)), where a is the number
  of possible distinct characters.

Python alternatives
-------------------
- set() can also track characters in a sliding window, although a
  dictionary allows us to jump directly to the previous occurrence.
- enumerate() provides a convenient way to iterate over characters
  while keeping track of their indices.
"""


def longest_substring(word: str) -> int:
    """Return the length of the longest substring without repeated characters."""

    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    last_seen = {}
    left = 0
    longest = 0

    for right, character in enumerate(word):

        # Move the left boundary if the character occurs in the current window.
        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1

        last_seen[character] = right

        # Update the longest substring found so far.
        longest = max(longest, right - left + 1)

    return longest
