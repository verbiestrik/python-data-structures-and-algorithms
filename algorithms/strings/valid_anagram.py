"""
Check whether two strings are anagrams.

Problem description
-------------------
Given two strings, determine whether they are anagrams of each other.

Two strings are anagrams if they contain exactly the same characters
with the same frequencies, regardless of their order.

This implementation is case-insensitive and ignores all non-alphabetic
characters, including whitespace, punctuation and digits.

Approach
--------
1. Iterate over the first string and build a frequency dictionary.
2. Convert alphabetic characters to their case-folded representation
   before counting them.
3. Iterate over the second string and decrement the corresponding
   character frequencies.
4. Return False if a character is missing or its frequency is exhausted.
5. Return True if all frequencies have been matched.

An empty string and a string containing no alphabetic characters are
considered anagrams of each other.

Complexity analysis
-------------------
Let n and m represent the lengths of the two input strings.

- Time complexity: O(n + m), since each character is processed once.
- Auxiliary space complexity: O(u), where u is the number of distinct
  characters in the normalised input. In the worst case, this is O(n).

Python alternatives
-------------------
- collections.Counter provides a convenient standard-library solution
  for comparing character frequencies.
- sorted() can also be used to compare the normalised characters, but
  requires O(n log n + m log m) time due to sorting.

str.casefold() is used instead of str.lower() for more comprehensive
Unicode-aware case-insensitive comparisons.
"""


def valid_anagram(expression1: str, expression2: str) -> bool:
    """Return True if the two strings are anagrams."""

    if not isinstance(expression1, str) or not isinstance(expression2, str):
        raise TypeError("Both inputs must be strings.")

    character_counts = {}

    # Count the alphabetic characters in the first string.
    for character in expression1:
        if character.isalpha():
            for folded_character in character.casefold():
                character_counts[folded_character] = (
                    character_counts.get(folded_character, 0) + 1
                )

    # Decrement the corresponding frequencies using the second string.
    for character in expression2:
        if character.isalpha():
            for folded_character in character.casefold():
                if folded_character not in character_counts:
                    return False

                character_counts[folded_character] -= 1

                if character_counts[folded_character] == 0:
                    del character_counts[folded_character]

    # All frequencies must have been matched.
    return not character_counts
