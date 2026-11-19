"""
All Permutations of a String
============================

Problem
-------
Generate all unique permutations of the characters in a given string.

For example:
    Input:  "alg"
    Output: ["agl", "alg", "gal", "gla", "lag", "lga"]

Repeated characters should not produce duplicate permutations.

Approach
--------
Use recursive backtracking to construct permutations one character at a time.

1. Sort the characters to obtain a lexicographical ordering.
2. Maintain a boolean list indicating which character positions have already
   been used in the current permutation.
3. At each recursive call, iterate over the available characters:
   - Skip characters that have already been used.
   - Skip a character if it is identical to the previous character and that
     previous character has not been used in the current permutation.
     This prevents generating duplicate permutations.
   - Otherwise, add the character to the current permutation and recurse.
4. Once the current permutation contains all characters, join them into a
   string and append it to the result list.
5. Backtrack by removing the last character and marking its position as
   available again.

An empty string produces a list containing one empty permutation, following
the mathematical convention that there is exactly one permutation of an
empty set.

Complexity
----------
Let n be the length of the input string.

Time: O(n * n!) in the worst case, when all characters are distinct.
      This includes generating and storing every permutation.

Space: O(n) auxiliary space for the recursion stack, current permutation
       and boolean list, excluding the output list.

       The output list requires O(n * n!) space in the worst case.

Python alternatives
-------------------
- itertools.permutations: Generates permutations using the standard library.
  However, it generates duplicate results when the input contains repeated
  characters. These would need to be removed separately.
- set: Can be used to remove duplicate permutations, but would generate
  unnecessary permutations before eliminating duplicates.

The backtracking implementation avoids generating duplicate permutations
in the first place.
"""

def all_permutations(word: str) -> list[str]:

    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    characters = sorted(word)

    used = [False] * len(characters)
    current_permutation = []
    permutations = []

    def backtrack():

        # A complete permutation has been constructed.
        if len(current_permutation) == len(characters):
            permutations.append("".join(current_permutation))
            return

        for i, character in enumerate(characters):

            if used[i]:
                continue

            # Skip duplicate characters at the same recursion level.
            if i > 0 and character == characters[i - 1] and not used[i - 1]:
                continue

            # Choose the character.
            used[i] = True
            current_permutation.append(character)

            backtrack()

            # Undo the choice (backtracking).
            current_permutation.pop()
            used[i] = False

    backtrack()

    return permutations
