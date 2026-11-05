"""
Group anagrams in a sequence of strings.

Problem description
-------------------
Given a sequence of strings, group together all strings that are anagrams
of each other.

Comparison is case-insensitive and ignores non-alphabetic characters,
including whitespace, punctuation and digits.

Original strings are preserved, and the order of words within each group
follows their original order.

Approach
--------
1. Create a dictionary mapping character-frequency signatures to groups.
2. Iterate through the input strings.
3. Build a dictionary containing the frequency of each alphabetic
   character in the current word.
4. Convert the frequency dictionary into a sorted tuple, which serves
   as the group identifier.
5. Add the original word to the corresponding group.
6. Return all groups.

Complexity analysis
-------------------
Let n represent the number of strings, L the maximum string length,
and U the maximum number of distinct characters in a string.

- Time complexity: O(n * (L + U log U)), since each word is processed
  once and its distinct characters are sorted to construct its key.
- Auxiliary space complexity: O(n * L), for the frequency signatures
  and grouped strings.

Python alternatives
-------------------
- sorted() can generate an alternative anagram key by sorting all
  characters in each normalised word.
- collections.Counter can replace the frequency dictionary.
- collections.defaultdict(list) can simplify group initialisation.
"""


def group_anagrams(words: list | tuple) -> list[list[str]]:
    """Group anagrams while preserving original strings and their order."""

    if not isinstance(words, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    if not all(isinstance(word, str) for word in words):
        raise TypeError("All elements must be strings.")

    groups = {}

    for word in words:
        character_counts = {}

        for char in word:
            if char.isalpha():
                for char_casefold in char.casefold():
                    character_counts[char_casefold] = (
                        character_counts.get(char_casefold, 0) + 1
                    )

        # The sorted frequency pairs uniquely identify the anagram group.
        key = tuple(sorted(character_counts.items()))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())
