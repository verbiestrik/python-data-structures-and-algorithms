"""
Problem: Balanced Parentheses

Given a mathematical expression containing different types
of parentheses (), {}, and [], determine whether all opening
and closing parentheses are correctly matched and nested.

Non-parenthesis characters should be ignored.

Approach:
1. Use a stack to keep track of opening parentheses.
2. When an opening parenthesis is encountered, push it onto
   the stack.
3. When a closing parenthesis is encountered:
   - Check whether the stack is empty.
   - Check whether the top element matches the closing
     parenthesis.
   - Return False if either condition is violated.
4. At the end, return True only if the stack is empty,
   otherwise there is at least one unclosed parenthese.

Complexity Analysis:
- Time Complexity: O(n).
  Each character is processed once. Stack operations take
  O(1) time.

- Space Complexity: O(n).
  In the worst case, the stack contains all opening
  parentheses.

Python Alternative:
Python does not have a dedicated built-in function for
checking balanced parentheses. A stack is the standard
approach to solving this problem.
"""


def check_balanced_parentheses(sequence: str) -> bool:
    matching_parentheses = {")": "(", "}": "{", "]": "["}
    stack = []

    for character in sequence:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if not stack or stack.pop() != matching_parentheses[character]:
                return False

    return not stack
