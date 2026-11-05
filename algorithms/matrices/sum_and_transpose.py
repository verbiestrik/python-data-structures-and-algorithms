"""
Compute row sums and the transpose of a matrix.

Problem description
-------------------
Given a rectangular matrix of integers or floats, return:
1. A list containing the sum of each row.
2. The transpose of the original matrix.

Approach
--------
1. Validate that the matrix is non-empty, rectangular and contains numbers.
2. Calculate the sum of each row using sum().
3. Calculate the transpose using zip(*matrix).
4. Convert the resulting rows into lists.

Complexity analysis
-------------------
Let m represent the number of rows and n the number of columns.

- Time complexity: O(m * n), since every element is processed a
  constant number of times.
- Auxiliary space complexity: O(m * n), for the transposed matrix.

Python alternatives
-------------------
- sum(row) calculates the sum of a sequence.
- zip(*matrix) efficiently groups elements by column.
- A nested loop can also implement the transpose without zip().
"""


def sum_and_transpose(matrix: list) -> tuple[list, list]:
    """Return the row sums and transpose of a matrix."""

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("Input must be a list of lists.")

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be rectangular.")

    if not all(
        isinstance(number, (int, float))
        for row in matrix
        for number in row
    ):
        raise TypeError("All matrix elements must be integers or floats.")

    row_sums = [sum(row) for row in matrix]

    transposed_matrix = [list(row) for row in zip(*matrix)]

    return row_sums, transposed_matrix
