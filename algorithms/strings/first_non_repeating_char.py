"""
Problem: First Non-Repeating Character

Given a string, find the first character (from left to right)
that occurs exactly once. The search is case-insensitive.

Approach:
1. Remove leading/trailing whitespace and convert to lowercase.
2. Use a dictionary to count the occurrences of each character.
3. Iterate through the string again and return the first
   character whose count is exactly one.
4. Return None if no such character exists.

Complexity Analysis:
- Time Complexity: O(n).
  Two iterations over the string, each taking O(n) time.
  Dictionary lookups and insertions take O(1) average time.

- Space Complexity: O(k), where k is the number of distinct
  characters. O(n) in the worst case.

Python Alternative:
The method 'Counter' from 'collections' can count occurrences
of a character.
"""

def first_non_repeating_char(word: str) -> str | None:
    normalized = word.strip().lower()
    letter_count = {}

    for letter in normalized:
        letter_count[letter] = letter_count.get(letter,0) + 1

    for letter in normalized:
        if letter_count[letter] == 1:
            return letter

    return None
