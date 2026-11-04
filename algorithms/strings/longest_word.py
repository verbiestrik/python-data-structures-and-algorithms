"""
Find the longest word in a sequence of words or a text containing sentences.

Problem description
-------------------
Given either a string containing one or more sentences or a sequence of
individual words, return the longest word.

Words in text are defined as contiguous sequences of alphabetic characters.
Whitespace, punctuation and digits act as separators.

If multiple words have the same maximum length, the first occurrence is
returned.

Approach
--------
1. For string input, scan the text once and identify alphabetic sequences.
   Keep track of the start and length of the longest sequence found.
2. For sequence input, iterate through the words and compare their lengths.
3. Raise an appropriate exception for empty inputs or invalid elements.

Complexity analysis
-------------------
Let N represent the total input size (characters and sequence elements).

- Time complexity: O(N), since each character or sequence element is
  processed at most once.
- Auxiliary space complexity: O(1), excluding the returned string.
  The returned string requires O(L) space, where L is its length.

Python alternatives
-------------------
- max(words, key=len) is a concise alternative for an already-tokenised
  sequence of words.
"""

from collections.abc import Sequence

def longest_word(words: str | Sequence[str]) -> str:
    """Return the first longest word in a string or sequence of words."""

    # Handle text input.
    if isinstance(words, str):
        longest = ""
        longest_length = 0
        word_start = None

        for i, char in enumerate(words):
            if char.isalpha():
                if word_start is None:
                    word_start = i

            elif word_start is not None:
                current_length = i - word_start

                if current_length > longest_length:
                    longest = words[word_start:i]
                    longest_length = current_length

                word_start = None

        # Handle a word ending at the final character.
        if word_start is not None:
            current_length = len(words) - word_start

            if current_length > longest_length:
                longest = words[word_start:]

        if not longest:
            raise ValueError("The input contains no words.")

        return longest

    # Validate sequence input.
    if not isinstance(words, Sequence):
        raise TypeError("Input must be a string or a sequence of strings.")

    if len(words) == 0:
        raise ValueError("The input sequence cannot be empty.")

    longest = ""
    longest_length = -1

    for word in words:
        if not isinstance(word, str):
            raise TypeError("All sequence elements must be strings.")

        if not word.strip():
            raise ValueError("Words cannot be empty or contain only whitespace.")

        current_length = len(word)

        if current_length > longest_length:
            longest = word
            longest_length = current_length

    return longest
