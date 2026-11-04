"""
Check whether a string is a palindrome.

Problem description
-------------------
Given a string, determine whether it is a palindrome.

A palindrome reads identically forwards and backwards. For this
implementation, the comparison is case-insensitive and ignores all
non-alphabetic characters (including whitespace, punctuation and digits).

Approach
--------
1. Construct a normalised string containing only alphabetic characters.
2. Convert characters to lowercase using casefold() for robust
   case-insensitive comparison.
3. Compare characters from opposite ends, moving towards the centre.
4. Return False immediately when a mismatch is found.

An empty normalised string is considered a palindrome.

Complexity analysis
-------------------
Let N represent the length of the input string.

- Time complexity: O(N), since normalisation and palindrome checking
  each require at most one traversal of the input.
- Auxiliary space complexity: O(N), due to the normalised string.

Python alternatives
-------------------
- word == word[::-1] provides a concise palindrome check after
  normalisation, but creates a reversed copy.
- reversed(word) returns an iterator over the characters in reverse order.
- str.casefold() provides more comprehensive case-insensitive conversion
  than str.lower().
"""


def check_palindrome(word: str) -> bool:
    """Return True if the input string is a palindrome."""

    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    # Normalise the input: ignore non-alphabetic characters and case.
    normalized = "".join(
        char.casefold() for char in word if char.isalpha()
    )

    n = len(normalized)

    # Compare characters from opposite ends.
    for i in range(n // 2):
        if normalized[i] != normalized[n - i - 1]:
            return False

    return True
